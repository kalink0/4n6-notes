---
title: "Chip-Off"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Chip-Off

In a chip-off, the memory chip is removed from a device's circuit board and read directly with a reader.

The result is a physical acquisition of the memory chip. For raw NAND flash chips without their own controller, the arrangement of the data (error correction, wear levelling, order of the blocks) must then be reconstructed; for eMMC and UFS chips, the controller in the chip takes care of this.

From a digital forensics perspective, chip-off is a destructive method: the device is usually no longer functional afterwards, and the heat during removal can damage the chip or the data. If the memory is encrypted, the acquired data is only available in encrypted form and can only be decrypted with the password or key. If the key is bound to the device's processor, as is often the case with modern smartphones, this is not possible even with the password. Chip-off is therefore mainly used for unencrypted or damaged devices, e.g. older mobile phones, navigation devices, drones or vehicle systems.
