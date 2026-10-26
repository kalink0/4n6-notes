---
title: "Orphaned Files"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Orphaned Files

So-called orphaned files are files that are still physically present on the storage medium but no longer have a valid link in the directory tree. This means that they can no longer be accessed by a user via the file system. Unlike, for example, files in unallocated space, some metadata may still exist for orphaned files. For example, timestamps of creation/modification or the file name may still be available. Statements about the previous location of the file in the file system may also be possible.

Orphaned files can occur, for example, if the parent folder was deleted and its entry in the file system was overwritten, as well as through system crashes or unclean deletion processes.
