---
title: "JBOD"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# JBOD

JBOD (Just a Bunch of Disks) refers to several storage devices operated without striping and without redundancy, either each as a separate drive or joined one after another into one logical drive (spanning).

With spanning, the storage space of the devices is concatenated: when the first device is full, the data continues on the next one. The devices can differ in size. If one device fails, the data on it is lost and the file system can usually no longer be read completely. Spanning is offered by RAID controllers, NAS systems and operating systems, among others, e.g. as the "linear" mode in mdadm on Linux or as a spanned volume on Windows.

From a digital forensics perspective, with spanning a readable file system only results from joining the individually acquired devices in the correct order. Since the data is not distributed in stripes, files on a single device are usually contiguous and can be recovered by carving even without the other devices, provided they do not cross the boundary between two devices and are not fragmented.
