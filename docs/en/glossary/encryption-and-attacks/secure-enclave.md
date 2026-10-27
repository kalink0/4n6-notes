---
title: "Secure Enclave"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Secure Enclave

The Secure Enclave is a security subsystem in Apple chips, separate from the main processor, that manages keys and verifies the device passcode.

It has been built into iPhones and iPads since the iPhone 5s (A7), and into Macs in the T2 chip and the Apple silicon processors. The Secure Enclave has its own processor and its own operating system (sepOS). It holds a device-specific key (UID) set during manufacturing that cannot be read out. The keys for data encryption are derived from this key and the device passcode. It also processes the data for Touch ID and Face ID. It is often abbreviated SEP (Secure Enclave Processor). The abbreviation SE, on the other hand, usually refers to the standalone security chip (Secure Element) that Apple uses separately for Apple Pay.

From a digital forensics perspective, the data can only be decrypted on the device itself, since the keys are bound to the UID; reading the removed memory chip (chip-off) or a password attack on another system does not succeed. The Secure Enclave enforces increasing delays after failed attempts and, if configured, erases the keys after ten failed attempts. Since the A12 (iPhone XS), the failed-attempt counter is additionally protected in a separate storage component (Secure Storage Component). Whether and how quickly an attack on the device passcode is possible therefore depends on the device generation, the iOS version and the available exploits.
