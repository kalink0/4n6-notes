---
title: "Keychain"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Keychain

The keychain is Apple's system service in which apps and the operating system on iOS and macOS store passwords, tokens, certificates and keys in protected form.

Typical entries are Wi-Fi passwords, credentials for accounts and websites, and keys for encrypted app databases. On iOS, the keychain is located in an SQLite database (`/private/var/Keychains/keychain-2.db`) whose entries are encrypted with keys bound to the security subsystem of the Apple chip that is separate from the main processor (Secure Enclave). On macOS, there are additionally file-based keychains, e.g. `~/Library/Keychains/login.keychain-db`, which are protected with the user password. Via iCloud Keychain, entries can be synchronised between the devices of an Apple account.

From a digital forensics perspective, the iOS keychain can only be decrypted on the device itself. Forensic tools acquire it as part of an acquisition of the complete file system (full file system). Which entries can be decrypted depends on whether the device has already been unlocked once since the last restart (After First Unlock, AFU) or not (Before First Unlock, BFU). Encrypted iTunes or Finder backups contain keychain entries unless they are restricted to the device; in unencrypted backups they cannot be analysed. Since some apps encrypt their databases with a key from the keychain, the keychain is often a prerequisite for analysing this data at all.
