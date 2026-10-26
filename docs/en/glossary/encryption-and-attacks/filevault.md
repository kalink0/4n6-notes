---
title: "FileVault"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# FileVault

FileVault is Apple's native disk encryption solution in macOS. It encrypts the entire startup volume – i.e. all data stored on it – so that no access is possible without entering the correct user password (and thus the decryption key). Since FileVault 2, which was introduced with Mac OS X Lion, this full encryption is done with modern algorithms, so that the data is effectively protected even if the device is lost or stolen.

From a digital forensics perspective, it can be said that with a sufficiently complex password there are no known ways to gain access to the data within a locked FileVault volume without the password or the recovery key.

Password attacks, which try to gain access to the data in the FileVault volume by trying out passwords, can take several decades to succeed, depending on the complexity of the password. On Macs with a T2 chip or Apple silicon, the Secure Enclave limits the number of password attempts, which makes password attacks considerably more difficult or not feasible at all.
