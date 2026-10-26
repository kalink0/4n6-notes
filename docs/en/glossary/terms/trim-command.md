---
title: "TRIM Command"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# TRIM Command

The TRIM command is an ATA command (comparable to the SCSI UNMAP command or Deallocate in NVMe) that allows the operating system to tell a connected SSD which storage areas are no longer in use.

The internal controller of the SSD marks the released storage areas as invalid and erases them as part of its internal storage management. Many SSDs already return only zeros when these areas are read immediately after the command. The aim is to maintain the write performance and lifetime of the SSD.

Due to the execution of the command, a subsequent recovery of deleted files by means of regular carving is not promising on SSDs.

The TRIM command can also be used on magnetic storage media, so-called SMR (Shingled Magnetic Recording) hard disks.
