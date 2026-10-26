---
title: "Realm Databases"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Realm Databases

## Meaning

### Technical description:

Realm is an object-oriented database for mobile apps that is used as an alternative to SQLite. Data is stored as objects with properties, not as rows in tables. A database consists of a single file; there are no separate journal or WAL files. Forensically relevant is that, besides the current state, the file can also contain the state before the last commit and remnants of older data.

### Non-technical description:

Realm is a data store that some apps use instead of the usual SQLite database. The app stores its data in it, for example user data, content or settings. For an investigation, this store can show which data the app stored and what recently changed in it.

## Key facts

### Components

Location:

- In the data directory of the respective app, file extension usually `.realm`

#### File header (24 bytes)

##### How it works

```
Offset  Size  Field            Notes
0x00     8    m_top_ref[0]     little-endian uint64 – file offset of root array A
0x08     8    m_top_ref[1]     little-endian uint64 – file offset of root array B
0x10     4    m_mnemonic       ASCII "T-DB" (0x54 2D 44 42); magic value
0x14     1    m_file_format[0] file format version for top_ref[0]; currently 24
0x15     1    m_file_format[1] file format version for top_ref[1]; currently 24
0x16     1    m_reserved       always 0x00 at the time of creation
0x17     1    m_flags          bit 0 (LSB): 0 = top_ref[0] active, 1 = top_ref[1] active
                               bits 1–7: unused at the time of creation
```

Realm works according to the copy-on-write principle: during a commit, changed arrays are not overwritten but written anew to free locations. Afterwards, the inactive top ref points to the new state and the flag is switched. The previously active top ref is retained as the state before the last commit.

##### Forensic value

The flag shows which top ref contains the current state. The other top ref contains the state before the last commit. By comparing both states, objects that were deleted or changed in the last transaction can be identified.

Different file format values of the two top refs show that a format upgrade took place during the last commit.

#### Realm arrays

##### How it works

After the 24-byte header, the file consists of Realm arrays, which are arranged as a B+ tree, and free areas. There are two kinds of arrays:

| Type            | has_refs | Role                                          |
|-----------------|----------|-----------------------------------------------|
| Reference array | 1        | Branch node – payload = file offsets          |
| Data array      | 0        | Leaf node – payload = actual values           |

Arrays start with a fixed **8-byte header**, followed by a payload of variable length.
Consecutive arrays can be found by searching for the 4-byte checksum pattern `AAAA`
(0x41414141).

Array header (8 bytes):

```
Offset  Size  Field            Notes
0x00     4    checksum         always 0x41414141 ("AAAA") – placeholder, may change in future
0x04     1    flags            see the table of bit groups below
0x05     3    size             big-endian uint24 – number of *elements* in the payload
```

Flags byte – bit groups (MSB = bit 7):

```
Bit(s)  Mask  Name                 Values / meaning
7       0x80  is_inner_bptree_node 1 = inner node of the B+ tree; always also sets has_refs
6       0x40  has_refs             1 = reference array (payload = file offsets of the child nodes)
                                   0 = data array (payload = actual data values)
5       0x20  context_flag         purpose unclear, rarely set; can mark the type of the leaf node
[4:3]   0x18  width_scheme         2-bit value 0–2; selects the formula for the payload size (see below)
[2:0]   0x07  width_ndx            3-bit index 0–7 into the conversion table for width (see below)
```

Conversion table width_ndx → width:

```
width_ndx  :  0   1   2   3   4    5    6    7
width      :  0   1   2   4   8   16   32   64
```

"width" = size of an element (in bits for scheme 0, in bytes for scheme 1).

Formula width_scheme → number of payload bytes:

```
width_scheme  Meaning            Formula
0             size in bits       payload_bytes = ceil(width × size / 8)
1             size in bytes      payload_bytes = width × size
2             ignore width       payload_bytes = size
```

After calculating `payload_bytes`, **round up to the next 8-byte boundary**:

```python
payload_bytes = (payload_bytes + 7) & ~7
```

Total length of the array in bytes = 8 (header) + payload_bytes_aligned.

#### Logical structure

##### How it works

The arrays form a hierarchy:

1. Group: top node that a top ref points to
2. Tables: one per class of the schema (class names with the prefix `class_`)
3. Cluster tree: B+ tree per table
4. Clusters: leaves of the cluster tree, contain the actual object data

References between objects (links) are stored via ObjKeys, the internal identifiers of the objects.

##### Forensic value

The class names in the schema show what kinds of data the app stores. To assign object data to a class and its properties, the hierarchy has to be traversed from the top ref down to the clusters.

#### Free areas

##### How it works

Areas that do not belong to either of the two top refs. Realm marks them as free and reuses them in later commits.

##### Forensic value

Free areas can contain remnants of older or deleted objects until Realm reuses them. Arrays can be found in them via the pattern `AAAA`.

## Analysis checklist

1. Never open the file on the original in Realm Studio or with the app. Realm Studio upgrades older files to the current format and writes a new commit in the process.
2. Check the signature `T-DB` at offset 16.
3. Analyse the header: determine the active top ref via the flag, compare the file format of both top refs.
4. Analyse the active top ref: schema, tables (classes), objects.
5. Analyse the inactive top ref and compare it with the active one.
6. Search the free areas for arrays.

## References

2026-05: [beBinary: Object by Object – RealmDB Forensics with crush](https://bebinary4n6.blogspot.com/2026/05/object-by-object-realmdb-forensics-with.html)

2026-01: [Damien Attoe: The Realm Files – Vol 3 – The Realm Header](https://digital4n6withdamien.blogspot.com/2026/01/the-realm-files-vol-3-realm-header.html)

2025-11: [Damien Attoe: The Realm Files – Vol 2 – Physical Structure Overview](https://digital4n6withdamien.blogspot.com/2025/11/the-realm-files-vol-2-physical.html)

2025-09: [Damien Attoe: The Realm Files – Vol 1 – Intro to RealmDB](https://digital4n6withdamien.blogspot.com/2025/09/the-realm-files-vol-1-intro-to-realmdb.html)

2022-05: [Cobley, Geneste: Realm – Mobile Forensics – The File Format Handbook, chapter 8 (Springer, open access)](https://doi.org/10.1007/978-3-030-98467-0_8)

2022: [Kim et al.: Methods for recovering deleted data from the Realm database (FSI: Digital Investigation)](https://www.sciencedirect.com/science/article/abs/pii/S2666281722000221)

2019-11: [Alexis Brignoni: Realm database storage primer for digital forensic examiners](https://abrignoni.blogspot.com/2019/11/realm-database-storage-primer-for.html)

crush format reference:
- <https://kalink0.github.io/crush-forensics/formats/realm/>

## Tools

crush - <https://github.com/kalink0/crush-forensics>

Realm Studio - <https://github.com/realm/realm-studio>
