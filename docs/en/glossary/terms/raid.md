---
title: "RAID"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# RAID

RAID (Redundant Array of Independent Disks) is the combination of several storage devices into one logical drive to increase fault tolerance, speed or both.

How the data is distributed across the devices is defined by the RAID level. The most common ones are:

- **RAID 0 (striping):** The data is split into blocks (stripes) and written alternately to all devices. There is no redundancy; if one device fails, the data is lost.
- **RAID 1 (mirroring):** Each device holds a complete copy of the data.
- **RAID 5:** Striping with parity information distributed across all devices. The failure of one device can be compensated.
- **RAID 6:** Like RAID 5, but with double parity. The failure of two devices can be compensated.
- **RAID 10:** Combination of RAID 1 and RAID 0, i.e. striping across mirrored pairs of devices.

A RAID is managed either by a dedicated controller (hardware RAID), by the operating system (software RAID, e.g. mdadm on Linux or Storage Spaces on Windows) or by the mainboard firmware together with a driver (firmware RAID, e.g. Intel RST). NAS systems mostly use software RAID. The configuration, including level, stripe size and order of the devices, is stored in metadata on the devices or in the controller.

From a digital forensics perspective, a single device of a RAID 0, 5, 6 or 10 holds only parts of the data; a readable file system only results from reassembling the array. The devices are therefore acquired individually and the RAID is then reconstructed from the images. This requires level, stripe size, order of the devices and, for RAID 5 and 6, the parity layout to be known or determined from the data. If a hardware controller stores the configuration in its own format, an additional acquisition of the logical drive through the controller can be useful. With RAID 1, each device holds the complete data.
