---
title: "Uninitialized Cluster / Slack Space"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Uninitialized Cluster / Slack Space

Slack space refers to the storage area at the end of an allocated cluster that is not occupied by the file because of the fixed cluster size and the possibly smaller file size, and that may still contain small amounts of previously existing files. A special case are uninitialized clusters (uninitialised storage areas, also called VDL slack): clusters that were assigned to a file but never written to and can therefore also contain data of previously existing files.

Due to the cluster sizes (currently mostly 4 kB by default), the amount of data to be expected in the slack at the end of a file is always smaller than the cluster size.

There is no file system metadata for the recovered data. Therefore, no statement can be made about timestamps, file path and an attributable user account. Also, possibly only parts of a file (e.g. individual words of a text file) can be recovered.
