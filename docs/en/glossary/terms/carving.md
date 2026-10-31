---
title: "Carving"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Carving

In digital forensics, carving refers to the process of reconstructing files or data fragments from a storage medium – without relying on the regular file system metadata (such as the entry in a Master File Table). Characteristic file signatures (headers, often also footers) are identified in the raw data stream, for example in unallocated space, in order to determine the boundaries of deleted or damaged files and then make them accessible again.

This method is particularly useful if files have been deleted or the file system is damaged, so that there is no longer any conventional metadata that would enable direct recovery.

There is no file system metadata for the recovered data. Therefore, no statement can be made about timestamps, file path and an attributable user account. Also, possibly only parts of a file (for example image sections) can be recovered, especially if the file was fragmented.

Carving can also be applied to files themselves in order to extract (possibly hidden) files contained within them. Here, too, file metadata, e.g. internal file directories such as the central directory of a ZIP archive, is not used.
