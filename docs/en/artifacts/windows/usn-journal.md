---
title: "USN Journal"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-system-changes]
---

# USN Journal

## Meaning

The USN (Update Sequence Number) journal is written by the Windows operating system for NTFS file systems. It contains information on operations performed on files, for example *"file created", "file deleted", "file enlarged/reduced".*

Depending on the activity on the NTFS partition, data is available for up to several weeks.

From a digital forensics perspective, entries in the USN journal mean that the listed actions were performed on the listed files at the given time. The USN journal contains the file name and the reference to the file path.

## Key facts

1. The USN journal has been enabled by default since Windows Vista
2. To also obtain the paths of a file, the data must be correlated with the entries of the MFT
3. The maximum size is 30 - 40 MB by default (logical file size of $J considerably larger due to the sparse area) - depending on the use of the partition, you can look 1 - 2 weeks into the past
4. Location (in the root directory of an NTFS partition):  
   **`\$Extend\$UsnJrnl`**  
   **`$J`** - alternate data stream - contains the actual journal  
   **`$Max`** - alternate data stream - contains metadata on the maximum size of the journal

## References

2026-09: <https://www.it-connect.tech/windows-forensics-part-10-analyzing-the-ntfs-usn-journal/>

2020-11: <https://docs.velociraptor.app/blog/2020/2020-11-13-the-windows-usn-journal-f0c55c9010e/>

2013-01: <https://journeyintoir.blogspot.com/2013/01/re-introducing-usnjrnl.html>

## Tools

Usnjrnl2Csv - <https://github.com/jschicht/UsnJrnl2Csv>

MFTECmd - <https://ericzimmerman.github.io/>

DLEAPP (parser: USN Journal) - <https://github.com/abrignoni/DLEAPP>

Dissect (plugin: usnjrnl) - <https://docs.dissect.tools/en/stable/plugins/usnjrnl.html>

dfir_ntfs - <https://github.com/msuhanov/dfir_ntfs>
