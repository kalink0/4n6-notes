---
title: "Recycle Bin"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-existence]
---

# Recycle Bin

## Meaning

The Recycle Bin contains files deleted by the user. These files can be restored by the user. The Recycle Bin contains metadata on the files such as the deleting user, previous file path, timestamps of the file and time of deletion of the file. For the user, the SID of the user account that was used to delete the file is stored.

From a digital forensics perspective, the files in the Recycle Bin allow the statement that the user account with the stored SID actively deleted the file at the time of deletion.

## Key facts

1. From Windows Vista; one Recycle Bin per drive
2. For each deleted file, one $I file (metadata) and one $R file (content)
3. Time of deletion in UTC
4. For the FAT32 file system, no reference to the user account is stored
5. When restoring, only the $R file is removed, the $I file is retained
6. Deleting via Shift+Del, PowerShell or CMD leaves no traces in the Recycle Bin
7. Location:  
   NTFS: **`{DRIVE}:\$Recycle.Bin\{USER_SID}`**  
   FAT32: **`{DRIVE}:\$Recycle.Bin`**

## References

2026-09: <https://www.it-connect.tech/windows-forensics-part-9-what-the-recycle-bin-can-reveal/>

2026-09: <https://www.magnetforensics.com/blog/artifact-profile-recycle-bin/>

2025-01: <https://bebinary4n6.blogspot.com/2025/01/windows-recycle-bin-known-and-unknown.html>

## Tools

Rifiuti2 - <https://abelcheung.github.io/rifiuti2/>

RBCmd - <https://ericzimmerman.github.io/>

DLEAPP (parser: Recycle Bin) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (artifact: Windows.Forensics.RecycleBin) - <https://docs.velociraptor.app/artifact_references/pages/windows.forensics.recyclebin/>

Dissect (plugin: recyclebin) - <https://docs.dissect.tools/en/stable/plugins/recyclebin.html>
