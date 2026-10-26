---
title: "LUKS"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# LUKS

LUKS (Linux Unified Key Setup) is a standard method for disk encryption on Linux. It defines a platform-independent on-disk format that makes it possible to encrypt entire partitions or containers.

From a digital forensics perspective, it can be said that with a sufficiently complex password there are no known ways to gain access to the data within a locked LUKS volume without the password.

Password attacks, which try to gain access to the data in the LUKS volume by trying out passwords, can take several decades to succeed, depending on the complexity of the password.
