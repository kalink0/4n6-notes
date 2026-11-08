---
title: "Deleted data"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Deleted data

Deleted data is data that has been removed from the point of view of the user, an application or the file system; depending on the level at which it was deleted, it is afterwards still completely, partially or no longer present.

What "deleted" means depends on this level; common cases are, for example:

- **Recycle bin or "Recently Deleted" folder:** The file is only moved and is still completely present as a file, usually until a fixed period expires or the recycle bin is emptied.
- **Marked as deleted in an application:** The entry, e.g. a message, remains in the application's database and is only hidden by a flag or replaced by a placeholder.
- **Removed from a database:** The record no longer exists from the database's point of view, but its content can still be in free areas of the database file or in associated journal or WAL files.
- **Deleted in the file system:** The file's entry and its storage space are marked as free. Until they are reallocated, content and metadata remain depending on the file system: on NTFS, for example, the entry with name, timestamps and location of the data remains, so the file can be fully attributed; on ext4, by contrast, the references to the data blocks are deleted and the content lies in unallocated space without attribution.
- **Physically deleted:** The content is no longer present on the storage device, e.g. because it was overwritten, erased by the controller of a flash memory after a TRIM command, or the key of an encrypted file was destroyed.

Data is deleted actively by the user, under system control by the operating system or an application, e.g. through expiry periods, storage cleanup or log rotation, or by an external trigger, e.g. a remote wipe, a message deleted for everyone by the communication partner or a deletion taken over through synchronization from another device.

From a digital forensics perspective, it has to be checked in each case what "deleted" means for the data in question, at which level it was deleted and whether the deletion was carried out by the user, under system control or by an external trigger. Forensic tools often label data from different levels uniformly as "deleted", e.g. recycle bin content, flagged database entries or files found by carving.
