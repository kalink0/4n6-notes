---
title: "Trusted Execution Environment (TEE)"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Trusted Execution Environment (TEE)

A Trusted Execution Environment (TEE) is an area in the main processor, isolated from the normal operating system, in which security-critical programs and keys are executed or stored separately from the rest of the system.

The separation is enforced by the hardware, on smartphones usually by a security extension of ARM processors (ARM TrustZone). The TEE runs its own small operating system, e.g. Trusty from Google, QSEE from Qualcomm or TEEgris from Samsung. On Android, this includes Keymaster or KeyMint, which manage the keys of the Android Keystore, and Gatekeeper, which verifies the screen lock and enforces delays after failed attempts. The keys for data encryption are derived from the screen lock and a hardware-bound key. Unlike the security subsystem in Apple chips (Secure Enclave) or a standalone security chip (Secure Element), the TEE does not have its own processor but uses the same one as the normal operating system.

From a digital forensics perspective, the data can only be decrypted on the device itself; an attack on the screen lock is only possible via the device and only with the enforced delays. Since the TEE shares the processor with the normal operating system, vulnerabilities in a chipset manufacturer's TEE implementation sometimes make it possible to bypass these protection mechanisms. Whether and how quickly access is possible therefore depends heavily on the chipset, the manufacturer and the patch level.
