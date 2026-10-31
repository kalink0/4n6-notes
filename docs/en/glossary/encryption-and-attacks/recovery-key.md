---
title: "Recovery Key"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Recovery Key

A recovery key is a key generated when encryption is set up, with which the data can be unlocked even without the actual password.

It is intended for cases where regular unlocking is no longer possible, e.g. because the password has been forgotten or the device no longer releases the key automatically after a change to the hardware or firmware. Recovery keys exist not only for the encryption of storage devices but also, for example, for end-to-end encrypted cloud data (iCloud Advanced Data Protection), for encrypted chat backups (WhatsApp) or for password managers. With BitLocker, it is a 48-digit numerical password in eight blocks of six digits each. When unlocking, a key ID is displayed that can be used to identify the matching recovery key. With FileVault, it consists of 24 letters and digits in six blocks.

From a digital forensics perspective, the recovery key is often stored outside the device: BitLocker keys can be stored in the Microsoft account, in organisations in Active Directory, in Entra ID or in a device management system (MDM). FileVault keys can be stored in the iCloud account or in an MDM. Recovery keys are also found as printouts, as text files (for BitLocker with the key ID in the file name) on USB sticks or other devices, or in password managers. Searching other seized storage devices and a request to the account provider are therefore often the most promising way to access encrypted data. With end-to-end encrypted services, by contrast, the provider should not have the recovery key.
