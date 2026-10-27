---
title: "Secure Element"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Secure Element

A Secure Element (SE) is a standalone, tamper-resistant chip with its own processor and memory that stores keys and performs cryptographic operations separately from the main processor.

Well-known examples are SIM cards, chips in bank or ID cards and chips for contactless payment in smartphones. Since Android 9, keys of the Android Keystore can be stored in a Secure Element (StrongBox), e.g. in the Titan M or Titan M2 of Google Pixel devices or in the Secure Element of current Samsung Galaxy devices. The verification of the screen lock, including the failed-attempt counter, can also take place there (Weaver). Apple also uses a Secure Element for Apple Pay; it must not be confused with the Secure Enclave, which is sometimes also abbreviated SE.

From a digital forensics perspective, a failed-attempt counter in the Secure Element provides protection even if the operating system or the isolated area in the main processor (Trusted Execution Environment, TEE) has been compromised through a vulnerability. An attack on the screen lock is then only possible with the delays enforced by the Secure Element, unless a vulnerability in the Secure Element itself can be exploited. The keys are bound to the device; decryption outside the device is not possible.
