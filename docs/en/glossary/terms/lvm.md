---
title: "LVM (Logical Volume Manager)"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# LVM (Logical Volume Manager)

LVM (Logical Volume Manager) is a storage management layer on Linux that combines storage devices or partitions into a shared storage pool and provides logical drives from it, which can be created and resized independently of the device boundaries.

LVM works with three layers:

- **Physical Volume (PV):** a storage device or partition set up for LVM.
- **Volume Group (VG):** the storage pool made up of one or more physical volumes.
- **Logical Volume (LV):** a logical drive within a volume group that holds a file system or e.g. swap.

A logical volume can be spread across several physical volumes, also with striping or mirroring. LVM also supports snapshots, which capture the state of a logical volume at a point in time. The configuration is stored as text in a metadata area at the start of each physical volume. LVM is commonly used on Linux servers and in combination with LUKS encryption, in which case LVM sits inside the decrypted container.

From a digital forensics perspective, logical volumes are not listed in the partition table; the partition of a physical volume does not contain a directly readable file system. The analysis tool has to support LVM, or the volume group has to be assembled from the images of all associated devices before the analysis. Besides the current configuration, the metadata area often also contains older versions of it, from which deleted or resized logical volumes can be derived. Snapshots can contain an older state of the data.
