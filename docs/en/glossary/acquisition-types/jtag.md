---
title: "JTAG"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# JTAG

In a JTAG acquisition, a device's memory is read via the JTAG interface (Joint Test Action Group, IEEE 1149.1), a test and debug interface of the processor.

For this, wires are soldered to test points on the circuit board or connected with spring contacts. The processor is controlled via the interface and reads out the memory. The result is a physical acquisition.

From a digital forensics perspective, the memory chip stays on the circuit board, so the device usually remains functional. The acquisition is slow, and on many devices the interface is not accessible or is disabled. If the memory is encrypted, the acquired data is only available in encrypted form and can only be decrypted with the password or key. If the key is bound to the device's processor, as is often the case with modern smartphones, this is not possible even with the password.
