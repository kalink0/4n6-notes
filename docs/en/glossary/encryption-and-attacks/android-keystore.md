---
title: "Android Keystore"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Android Keystore

The Android Keystore is Android's system service in which apps and the operating system store cryptographic keys in such a way that they can be used but not read out.

Unlike Apple's keychain, the Keystore only stores keys, not passwords or other credentials. Apps store these themselves and often encrypt them with a Keystore key. With a hardware-backed Keystore, the keys are managed in an area of the processor isolated from the operating system (Trusted Execution Environment, TEE) or in a separate security chip (Secure Element) and never leave it; the file system only contains key blobs encrypted with them (since Android 12 in `/data/misc/keystore/persistent.sqlite`). A key can additionally be bound to the device being unlocked or to the user having authenticated shortly before.

From a digital forensics perspective, data that an app has encrypted with a hardware-backed Keystore key cannot be decrypted directly even with root privileges and a full file system acquisition, since the key never leaves the device. Decryption is only possible on the device via the Keystore, e.g. through the app itself or by instrumenting the app at runtime. On older devices without a hardware-backed Keystore, on the other hand, the keys are only protected in software and can possibly be read out with root privileges.
