---
title: "VSS - Volume Shadow Copy Service"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-existence]
---

# VSS - Volume Shadow Copy Service

## Meaning

Since Windows Vista, the Microsoft Windows operating system has had the Volume Shadow Copy Service (VSS) mechanism for the NTFS file system.
This feature enables users to restore files that existed in the past and former versions of files.

From a digital forensics perspective, this means that files that existed in the past and/or former versions of files may be present in these volume shadow copies.
If a file is in a volume shadow copy, it can be said from a digital forensics perspective from when this "snapshot" of the file dates. This makes it possible to state when this file was present on the system in this version.

## Key facts

1. On Windows 10/11, system protection is not enabled by default
2. Created, among other things, during software installation, Windows Update or a manual restore point
3. If the reserved storage space is full, the oldest shadow copy is deleted
4. Location:  
   **`{DRIVE}:\System Volume Information\{GUID}{3808876b-c176-4e48-b7ae-04046e6cc752}`**

## References

2026-09: <https://www.it-connect.tech/forensic-windows-part-14-exploring-shadow-copies-vss/>

2026-07: <https://digitalinvestigator.blogspot.com/2026/07/volume-shadow-copies-in-windows.html>

2018-03: <https://www.iiis.org/CDs2018/CD2018Spring/papers/ZA288KS.pdf>

2017-10: <https://andreafortuna.org/2017/10/02/volume-shadow-copies-in-forensic-analysis/>

2011-01: <https://windowsir.blogspot.com/2011/01/accessing-volume-shadow-copies.html>

## Tools

libvshadow - <https://github.com/libyal/libvshadow>

VSCMount - <https://github.com/EricZimmerman/VSCMount>

Shadow Copy View - <https://www.nirsoft.net/utils/shadow_copy_view.html>

Arsenal Image Mounter - <https://arsenalrecon.com/downloads/>

ShadowExplorer - <https://www.shadowexplorer.com/downloads.html>

vss_carver - <https://github.com/mnrkbys/vss_carver>
