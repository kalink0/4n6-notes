---
title: "In-System Programming (ISP)"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# In-System Programming (ISP)

In an ISP acquisition, a memory chip, usually an eMMC chip, is read directly on the circuit board by connecting a reader to its data lines, without removing the chip.

For this, fine wires are soldered to test points or components on the circuit board that are connected to the chip's data lines. The device's processor is prevented from accessing the memory in the process. The result is a physical acquisition.

From a digital forensics perspective, ISP is faster than JTAG and less risky than chip-off, since the chip is not exposed to heat and the device usually remains functional. If the memory is encrypted, the acquired data is only available in encrypted form and can only be decrypted with the password or key. If the key is bound to the device's processor, as is often the case with modern smartphones, this is not possible even with the password.
