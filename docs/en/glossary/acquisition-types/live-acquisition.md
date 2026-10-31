---
title: "Live Acquisition"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Live Acquisition

In a live acquisition, data is secured from a running system without shutting it down first.

Depending on the goal, individual files, entire storage media or volumes, or the main memory are secured. The acquisition is carried out via the running operating system, e.g. with an acquisition program started from an external storage medium.

From a digital forensics perspective, a live acquisition provides access to data that would no longer be accessible after shutdown, e.g. contents of unlocked encrypted volumes, signed-in online services or the contents of main memory. Every action on the running system alters it, and the data keeps changing during the acquisition. A live acquisition therefore cannot be repeated, and its hash value cannot be verified against the original later. The steps taken are therefore documented precisely.
