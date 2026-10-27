---
title: "Full Disk Encryption (FDE)"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Full Disk Encryption (FDE)

With full disk encryption (FDE), an entire storage device or an entire volume is encrypted with a single shared key, regardless of which files are stored on it.

The key is unlocked once when the system starts or the volume is mounted, e.g. by a password, a PIN or a Trusted Platform Module (TPM). After that, all data on the volume is readable in plaintext for the operating system until it is locked again or the system is shut down. Examples are [BitLocker](bitlocker.md), [FileVault](filevault.md), [LUKS](luks.md) and [VeraCrypt](veracrypt.md). Older Android versions (up to Android 9) also used FDE.

From a digital forensics perspective, a volume with FDE is either fully accessible or not accessible at all. If a running system with an unlocked volume is found, a live acquisition can secure the data in plaintext that would no longer be accessible without the password or recovery key after shutdown. After decryption, deleted files can be recovered as on an unencrypted volume, since the key applies to the entire volume.
