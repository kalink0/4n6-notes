---
title: "Unallocated Cluster"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Unallocated Cluster

Unallocated clusters (unallocated storage areas) have been marked as free by the operating system within a partition.

When a file is deleted, the operating system marks the storage areas in which the data of the file is located as "unallocated" and thus as free space. The actual data, however, is not deleted immediately. Previously existing data can therefore be recovered from these storage areas.

If data is recovered without reference to the file system (e.g. by carving), there is no file system metadata. Therefore, no statement can be made about timestamps, file path and an attributable user account. Also, possibly only parts of a file (for example image sections) can be recovered.
