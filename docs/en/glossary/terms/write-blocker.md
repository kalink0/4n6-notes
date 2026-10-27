---
title: "Write Blocker"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Write Blocker

A write blocker is a device or software that allows read access to a storage medium but prevents write access.

Hardware write blockers are connected between the storage medium and the analysis system and only pass through read commands. Software write blockers implement the write protection in the operating system of the analysis system.

From a digital forensics perspective, a write blocker prevents a storage medium from being altered during acquisition, e.g. by the operating system mounting it automatically, which can write metadata or journals. A write blocker cannot prevent internal operations of an SSD controller (e.g. garbage collection).
