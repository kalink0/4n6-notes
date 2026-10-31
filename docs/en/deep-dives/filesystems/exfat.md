---
title: "exFAT"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# exFAT

## Meaning

exFAT is a file system developed by Microsoft in 2006, intended primarily for flash storage such as USB sticks, SD cards and external hard drives. It was designed as the successor to FAT32 to support larger files and storage media without the limitations of FAT32 and without bringing along the complexity of NTFS.

## Key facts

1. Maximum volume size: 128 PiB
2. Maximum file size: 128 PiB
3. Maximum file name length: 255 characters
4. Timestamps:
   1. Timestamps stored as absolute values
   2. Local/system time, plus time zone information
   3. Creation and modified timestamps with 10 ms resolution, access timestamp with 2 s resolution

### Components

#### Volume Boot Record

##### How it works

Located in sectors 0 - 11 of the volume.

A backup of the VBR follows directly in sectors 12 - 23.

The first sector of the VBR holds the Main Boot Sector, directly followed by 8 Extended Boot Sectors (boot code only). These are followed by the OEM Parameters (sector 9), a reserved sector (10) and the boot checksum (11).

##### Forensic value

Forensically relevant are the Main Boot Sector (among other things Volume Serial Number, location of the FAT, Cluster Heap and Root Directory, cluster size, VolumeFlags) and the boot checksum in sector 11. In the backup, VolumeFlags and PercentInUse are outdated.

#### File Allocation Table (FAT)

##### How it works

As with FAT32, the File Allocation Table in exFAT describes the cluster chains. A chain exists for fragmented files and directories and always for the Root Directory. For non-fragmented files and directories (NoFatChain set in the Stream Extension), the FAT entries are invalid and are not evaluated. In exFAT, the allocation status of the clusters is not stored in the FAT but exclusively in the Allocation Bitmap.

Each cluster in the volume is represented by a 4-byte entry in the FAT. Cluster numbering starts at 2.

A FAT entry can have the following values:

- 0xFF FF FF F7: cluster is marked as "bad" and must no longer be used
- 0xFF FF FF FF: cluster contains the end of a chain and therefore the end of a file
- OR: the next cluster in the chain, e.g. 0x71 01 00 00 (0x0171 LE) -> next file fragment in cluster 369

The sector of a cluster is calculated as ClusterHeapOffset + (cluster number − 2) × sectors per cluster.

##### Forensic value

The FAT is needed to recover fragmented files and directories. A FAT entry with the value 0 does not mean that the cluster is free – an allocated, contiguously stored file usually has no entries in the FAT.

#### Directory Entries

##### How it works

Directory entries can be understood as a kind of table of contents, possibly with additional metadata. Each directory entry is 32 bytes in size. There are different types. Some types only contain the offset where the actual data is located, others contain additional metadata such as timestamps and file names.

The most significant bit of the type byte (InUse) marks an entry as in use. 0x00 marks the end of the directory.

The types and the files behind them are briefly explained below.

###### Allocation Bitmap (0x81)

The directory entry contains the offset, the length and the corresponding FAT.

The Allocation Bitmap file tracks all clusters of the file system by their status, allocated or unallocated. One bit corresponds to one cluster.

###### Up-Case Table (0x82)

The directory entry contains the offset and the length of the Up-Case Table.

The Up-Case Table is used to search for file and directory names case-insensitively.

Since exFAT is case-insensitive by definition, this is necessary to detect identical file names.

The Up-Case Table contains the mapping of lowercase letters to their corresponding uppercase letters.

###### Volume Label (0x83)

The directory entry contains the label that was set for the volume.

###### File (0x85)

The File directory entry contains the metadata of the file, such as the timestamps.

In addition, each File directory entry has at least two secondary directory entries: a Stream Extension, which contains the location of the file in the volume, and a Filename Extension, which contains the file name. If necessary, further secondary directory entries can be present (e.g. for long file names).

The File directory entry also contains a checksum (SetChecksum) over the entire entry set, i.e. the File entry and all associated secondary entries.

###### Volume GUID (0xA0)

Contains the GUID (Globally Unique Identifier) of the volume.

###### Stream Extension (0xC0)

Contains the location of the file, the file size and the information whether the file is stored fragmented.

###### Filename Extension (0xC1)

The Filename Extension contains the file name - it can hold a maximum of 15 characters. For longer file names, further Filename Extensions are created. A file can have a maximum of 17 Filename Extensions. A file name can therefore be a maximum of 255 characters long.

##### Forensic value

- Deleted entries: on deletion, the InUse bit is cleared (0x85 → 0x05, 0xC0 → 0x40, 0xC1 → 0x41) and the clusters are released in the Allocation Bitmap. Name, first cluster, file size and timestamps are retained until overwritten.
- Non-fragmented deleted files can be recovered using the first cluster and the file size, as long as the clusters have not been reallocated. For fragmented files, recovery is only possible as long as the FAT chain is intact.
- Orphaned entries: there can be directory clusters that are marked as allocated in the Allocation Bitmap but are no longer reachable from the directory tree. The entry sets in them are still marked as in use and do not appear in any regular directory listing.
- The SetChecksum can be used to check whether a found or carved entry set is complete and unmodified.

### Analysis checklist

1. Evaluate the Main Boot Sector (cluster size, location of the FAT, Cluster Heap and Root Directory, Volume Serial Number), verify the boot checksum, and if it does not match, use the backup in sectors 12 - 23
2. Read the Root Directory via the FAT chain and evaluate the Allocation Bitmap, Up-Case Table, Volume Label and Volume GUID
3. Evaluate subdirectories, verifying the SetChecksum of the entry sets
4. Search for deleted entries (0x05, 0x40, 0x41)
5. Recover metadata and file contents, checking beforehand in the Allocation Bitmap whether the clusters are still free
   1. Small files (non-fragmented): from the first cluster according to the file size
   2. Large files (fragmented): along the FAT chain, if intact
6. Check allocated directory clusters that are not reachable from the directory tree for orphaned entry sets
7. Evaluate timestamps together with the respective time zone offset

## References

2022-10: [Nordvik et al. – It is about time: Do exFAT implementations handle timestamps correctly?](https://doi.org/10.1016/j.fsidi.2022.301476)

2018-05: [Vandermeer et al. – Forensic Analysis of the exFAT Artefacts](https://commons.erau.edu/adfsl/2018/presentations/4)

2014-06: [The Sleuth Kit – exFAT Implementation Notes](https://wiki.sleuthkit.org/ExFAT-Implementation-Notes/)

2009-12: [Shullich – Reverse Engineering the Microsoft exFAT File System](https://www.sans.org/white-papers/33274)

2026-10: [NTFS.com – exFAT Overview](https://www.ntfs.com/exfat-overview.htm) (accessed)

**Documentation**

2025-07: [Microsoft – exFAT File System Specification](https://learn.microsoft.com/en-us/windows/win32/fileio/exfat-specification)

2026-10: [libyal – File Allocation Table (FAT) format (incl. exFAT)](https://github.com/libyal/libfsfat/blob/main/documentation/File%20Allocation%20Table%20%28FAT%29%20format.asciidoc) (accessed)

2026-10: [Crush Format Reference – exFAT](https://kalink0.github.io/crush-forensics/formats/exfat/)

## Tools

Sleuthkit - <https://sleuthkit.org/sleuthkit/download.php> (fsstat, fls, istat, icat)

qnxprobe - <https://github.com/abrignoni/qnxprobe>

exfatprogs - <https://github.com/exfatprogs/exfatprogs> (dump.exfat)
