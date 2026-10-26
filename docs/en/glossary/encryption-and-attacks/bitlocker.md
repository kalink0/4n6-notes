---
title: "BitLocker"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# BitLocker

BitLocker is a disk encryption technology developed by Microsoft that is integrated into certain Windows versions. It protects data by encrypting entire drives – such as the operating system drive or external storage media – using advanced encryption algorithms.

From a digital forensics perspective, it can be said that with a sufficiently complex password there are no known ways to gain access to the data within a locked BitLocker volume without the password or the recovery key.

Password attacks, which try to gain access to the data in the BitLocker volume by trying out passwords, can take several decades to succeed, depending on the complexity of the password. If BitLocker is used in conjunction with a Trusted Platform Module (TPM), password attacks are considerably more difficult or not feasible at all.
