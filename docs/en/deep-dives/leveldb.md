---
title: "LevelDB"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# LevelDB

## Meaning

### Technical description:

LevelDB is a key-value database developed by Google that is frequently used by apps and operating systems to store configuration and history data. The content is not standardised and can range from plain text through binary data to serialised structures. Forensically relevant is that it can contain sensitive information such as settings, tokens or usage histories of an application.

### Non-technical description:

LevelDB is a kind of data store that many apps use in the background. It can hold very different information – for example settings, history entries or login data. For an investigation, this store can therefore provide important clues as to how an app was used and what data was created in the process.

## Key facts

### Components

Location:

- All files of a database are stored together in one directory

#### log file

##### How it works

The log file is comparable to a WAL file in SQLite and is sometimes also called that. All new data is stored in the log file.

New data can be the following:

1. Completely new data
2. Changes to existing data
3. Deletion of existing data

All entries have a sequence number. This number can be used to reconstruct the history.   
  
The key-value pairs are stored unencrypted, unencoded and uncompressed.

The format of the values themselves is up to the program code of the component creating the data - accordingly, decoding steps may be necessary, for example, to be able to interpret data.

The file structure is as follows:

1. Blocks with a fixed size of 32 KB can contain any number of records. If fewer than 7 bytes remain at the end of a block, they are padded with zeros.
2. Each record contains a 7-byte header; if necessary, it is repeated at the start of a block with the corresponding values for the record type.
   1. Bytes 0 to 3: CRC-32C of type and payload
   2. Bytes 4 to 5: length of the record as UInt16 (little endian)
   3. Byte 6: record type (1 = Full, 2 = First, 3 = Middle, 4 = Last)
      1. Full = entire record in the current block
      2. First = first part of the record, a further part is in the next block
      3. Middle = the previous and the next block contain data of the record
      4. Last = only the previous block contains data of the record
3. The record header is followed by the payload with the given length.
4. The payload is usually a WriteBatch (several operations are written in one go). Therefore, an additional 12-byte header is added:
   1. Bytes 0 to 7: sequence number of the first operation; each further operation in the batch counts up by one
   2. Bytes 8 to 11: number of operations in the batch (Int32)
5. The 12-byte batch header is followed by the operations; an operation is structured as follows:
   1. Length = 1 byte ; *operation type*

      0 = Delete (deletion of an entry by specifying the key)

      1 = Put (addition or change of an entry by specifying key and value)
   2. Length = 1 to 5 bytes ; *key length*

      Key length as VarInt32
   3. Length = key length ; *key*

      Key
   4. Length = 1 to 5 bytes ; *value length*

      Value length as VarInt32
   5. Length = value length ; *value*

When the log file exceeds a size of 4 MB (default), the data is transferred to an ldb file (SSTable). (Technically, this goes through a MemTable, which is a copy of the log file.)

##### Forensic value

The log file contains every write operation individually with its sequence number – including overwritten values and deletions. This makes it possible to trace the order of the changes, and deleted keys remain visible (deletion markers without value).

Keys and values are stored uncompressed, so string searches work. If a record spans a block boundary, the 7-byte header at the 32 KB boundary interrupts the data.

#### ldb file

##### How it works

The LDB file is the storage layer for longer-term storage. Older implementations use the extension `.sst` instead of `.ldb`; the structure is the same.

LDB files are SSTables (Sorted String Tables), i.e. files in which the entries are stored sorted by key. They are not changed after creation - new data always ends up in new files.

When ldb files are created, different levels are created; this has no influence on the internal structure. The manifest file provides the information which key range is in which ldb file.

In ldb files, data may be compressed and key sharing is used - more on this in the description of the file structure.

__Level 0:__ 

The ldb file receives a new, sequential number – not the number of the associated log file. It contains the same entries as the log file (including overwritten and deleted entries), but sorted by key. An ldb file is created once the log file reaches a size of 4 MB by default. In addition, when the database is opened, the existing log file is converted into a level 0 file. Blocks can be compressed with Snappy.

__Level 1 and higher:__ 

As soon as 4 level 0 ldb files (default) exist, they are merged with the overlapping level 1 files into new level 1 files (approx. 2 MB each). This process is called compaction. The data is sorted, deduplicated and possibly compressed. Overwritten values are discarded, deletion markers only if no higher level can still contain the key.

From level 1, the total size of a level triggers the next compaction (level 1: 10 MB, level 2: 100 MB, etc.).

The file structure is as follows:

1. Data block

   This is where the data is stored. Several data blocks can exist in one file.
   1. Block entries (key-value pairs), per entry:
      1. Shared key length (VarInt32): number of bytes taken over from the previous key
      2. Non-shared key length (VarInt32)
      3. Value length (VarInt32)
      4. Non-shared part of the key
      5. Value
   2. Restart array at the end of the block (only needed for fast searching)
   3. Trailer (5 bytes)
      1. Compression (1 byte)

         0 = no compression

         1 = Snappy
      2. CRC-32 of the block data (4 bytes)

   The last 8 bytes of each key are not part of the user key: 7 bytes sequence number and 1 byte status (0 = deleted, 1 = active).
2. Meta block

   Contains e.g. Bloom filters to quickly determine whether a key exists in the data
3. Meta index block

   Index of the existing meta blocks
4. Index block

   Index of the existing data blocks
5. Footer

   Length: 48 bytes
   1. Metaindex block handle (offset and size, each varint64)

      Gives the position and size of the meta index block
   2. Index block handle (offset and size, each varint64)

      Gives the position and size of the index block
   3. Padding with zeros so that 1. to 3. together make 40 bytes
   4. Magic number (8 bytes)
      1. 0xdb4775248b80fb57 (little endian, on disk `57 FB 80 8B 24 75 47 DB`)

The index blocks serve to find entries quickly but are not necessary for reading/dumping all entries.

##### Forensic value

Level 0 files contain the same entries as the log file they were created from, including overwritten and deleted entries.

From level 1, overwritten values have been removed by compaction. Deletion markers can remain.

Due to Snappy compression and key sharing, a string search without prior decompression is not reliable.

After a compaction, the old ldb files are deleted.

#### MANIFEST

##### How it works

Contains, per ldb file, level, size and key range (smallest/largest key), plus comparator, current log file and last sequence number. The MANIFEST has the same format as the log file but contains VersionEdits instead of WriteBatches. Each time the database is opened, a new MANIFEST is created.

##### Forensic value

The last sequence number shows how many write operations took place on the database in total. Older MANIFEST files can refer to ldb files that no longer exist.

#### CURRENT

##### How it works

Text file with the name of the current MANIFEST.

##### Forensic value

Shows which MANIFEST is current. This makes it possible to classify an older MANIFEST as historical.

#### LOG / LOG.old

##### How it works

Text log of LevelDB itself – not to be confused with the binary log file. LOG.old is the previous LOG.

##### Forensic value

Contains compactions, the opening of the database and errors, and thus helps to understand what happened to the database.

The timestamps are in the local time of the device, without time zone information.

#### LOCK

##### How it works

Lock file, without forensic value.

## Analysis checklist

1. Secure the entire directory, all files together.
2. Never open the database on the original with the app or a LevelDB library. When opening, the current log file is converted into a level 0 file and files no longer needed are deleted.
3. Read CURRENT: which MANIFEST is current?
4. Analyse the MANIFEST: active ldb files per level, current log file, last sequence number, comparator.
5. Analyse files that are not in the current MANIFEST separately – they do not belong to the current state.
6. Analyse the log file, including deletions.
7. Analyse the ldb files, first level 0, then the higher levels. For a string search, decompress the blocks first.
8. Merge the entries of all files via the sequence number: the highest sequence number per key is the current state, lower ones are older versions.
9. Decode the values – the format is defined by the app (e.g. Protobuf, JSON).
10. Use LOG / LOG.old for context.

## References

2026-05: [beBinary: Reading the CURRENT – LevelDB Forensics with crush](https://bebinary4n6.blogspot.com/2026/05/reading-current-leveldb-forensics-with.html)

2020-10: [CCL: IndexedDB on Chromium](https://www.cclsolutionsgroup.com/post/indexeddb-on-chromium)

2020-09: [CCL: Hang on! That's not SQLite! Chrome, Electron and LevelDB](https://www.cclsolutionsgroup.com/post/hang-on-thats-not-sqlite-chrome-electron-and-leveldb)

2015-12: [Kevin Kwok: Recovering Deleted Data from LevelDB](https://antimatter15.com/2015/12/recovering-deleted-data-from-leveldb/)

[Forensics Wiki: LevelDB format](https://forensics.wiki/leveldb_format/)

LevelDB documentation:
- Files, levels and compaction: <https://github.com/google/leveldb/blob/main/doc/impl.md>
- Log format: <https://github.com/google/leveldb/blob/main/doc/log_format.md>
- Table format (ldb): <https://github.com/google/leveldb/blob/main/doc/table_format.md>

crush format reference:
- <https://kalink0.github.io/crush-forensics/formats/de/leveldb/>

## Tools

crush - <https://github.com/kalink0/crush-forensics>

dfindexeddb (dfleveldb) - <https://github.com/google/dfindexeddb>

LevelDB Dumper - <https://github.com/mdawsonuk/LevelDBDumper>

LevelDBtoSQLite - <https://github.com/SpyderForensics/Digital4n6withDamien/tree/main/LevelDBtoSQLite>

ccl_chromium_reader (storage_formats/ccl_leveldb.py) - <https://github.com/cclgroupltd/ccl_chromium_reader/>
