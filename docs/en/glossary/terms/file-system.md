---
title: "File system"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# File system

A file system defines how files and directories are stored, named and found on a storage device or in a partition.

Besides the content of the files, it manages their metadata, e.g. name, path, size, timestamps and permissions, as well as the information which areas of the device are in use and which are free. Storage space is allocated in units of fixed size (clusters or blocks). Many file systems record changes in a journal or write changed data to a new location (copy-on-write) in order to restore a consistent state after a crash. Examples of file systems are NTFS, FAT32, exFAT, APFS and ext4.

From a digital forensics perspective, when a file is deleted, a file system usually only marks its entry and storage space as free. Whether the content can still be read afterwards depends on the storage device: on magnetic hard drives it usually remains until the area is overwritten; with flash memory (e.g. SSD, eMMC, UFS), the controller can erase freed areas shortly after a TRIM command. Which timestamps exist, in which resolution and time zone they are stored and when they change depends on the file system and the operating system. Journals and areas replaced through copy-on-write can contain older states of metadata.
