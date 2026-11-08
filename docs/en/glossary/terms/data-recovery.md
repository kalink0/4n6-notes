---
title: "Data recovery"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Data recovery

Data recovery is the retrieval of data that has been deleted, is damaged or can no longer be accessed in the normal way.

Which method is possible depends on the level at which the data was deleted or what is damaged; common methods are, for example:

- **Through file system metadata:** If the entry of a deleted file still exists, the file can be recovered with name, path and timestamps, as long as its storage space has not been reallocated.
- **By carving:** Without file system metadata, files are searched for in unallocated space by their file signatures. Name, path and timestamps are not known.
- **From databases:** Deleted records are reconstructed from free areas of the database file or from journal or WAL files.
- **From older states:** Snapshots, shadow copies, backups or synchronized cloud data can contain a state from before the deletion.
- **From damaged storage devices (data rescue):** With defective hardware, the device is repaired or the memory chip is read directly; with damaged file systems, their structures are reconstructed.

Data cannot be recovered if it was overwritten, if the controller of a flash memory erased its storage areas after a TRIM command, or if its encryption key was destroyed. On current smartphones, each file is encrypted with its own key, which is deleted together with the file; carving there therefore usually yields no usable files.

From a digital forensics perspective, the evidential value of recovered data depends on the method: files recovered through file system metadata are associated with a path and timestamps, files found by carving are not. Recovered data can be incomplete or partly consist of other, later written data if its storage space has already been reallocated. The method used should therefore be documented.
