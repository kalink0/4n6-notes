---
title: "Trusted Platform Module (TPM)"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Trusted Platform Module (TPM)

A Trusted Platform Module (TPM) is a security component in PCs and laptops that stores cryptographic keys in protected form and only releases them under defined conditions.

The TPM can be a separate chip on the mainboard or implemented as a firmware TPM in the processor (e.g. Intel PTT, AMD fTPM). During system startup, it measures the individual stages of the boot process (firmware, bootloader, configuration). A key can be bound to these measurements and is only released if the boot chain is unchanged. In addition, the release can be tied to a PIN; after several failed attempts, the TPM locks itself temporarily. Windows 11 requires a TPM 2.0, and the Windows disk encryption (BitLocker) uses it by default. On Linux, for example, a storage device encrypted with LUKS can be unlocked via the TPM.

From a digital forensics perspective, a storage device protected with a TPM is bound to the device: if it is removed and acquired on another system, the data is only available in encrypted form and can only be decrypted with the recovery key generated during setup. Changes to the boot chain, e.g. booting from another medium or changed firmware settings, also cause the TPM not to release the key. Without an additional PIN, the TPM unlocks the volume automatically at startup; the data is then essentially only protected by the operating system login. With separate TPM chips, it has already been possible in this case to read the key on the connection between the TPM and the processor.
