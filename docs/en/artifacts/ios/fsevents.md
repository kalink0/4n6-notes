---
title: "FSEvents"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-system-changes, file-existence]
---

# FSEvents

## Meaning

FSEvents (File System Events) is a low-level framework in Apple operating systems designed to log all changes in the file system in real time. Creation, modification (content and metadata), renaming and deletion of files and folders are logged with the associated file names and file paths. Read access is not recorded.

From a digital forensics perspective, FSEvents entries allow statements about actions in the file system in relation to file names and file paths. The order of the entries can also be given; however, several actions on the same path can be combined in one entry without their order being recognisable. The data also allows statements about files and folders that existed in the past. No statements can be made about the content of the files or about the actors.

## Key facts

1. The timestamps are NOT directly included in the FSEvents storage. However, the files, which contain up to 5000 events, have a timestamp of their own that narrows down the time period.
2. In addition to the storage in the file system, there is a buffer in memory - this means that the most recent file changes may not yet have been written to disk on a running system.
3. Location (possibly more locations in iOS):  
   **`/private/var/.fseventsd`**  
   **`/private/var/mobile/.fseventsd`**

## References

2024-02: <https://github.com/libyal/dtformats/blob/main/documentation/MacOS%20File%20System%20Events%20Disk%20Log%20Stream%20format.asciidoc>

2017-10: <https://www.osdfcon.org/presentations/2017/Ibrahim-Understanding-MacOS-File-Ststem-Events-with-FSEvents-Parser.pdf>

## Tools

FSEParser - <https://github.com/dlcowen/FSEventsParser>

FSEventsParser - <https://github.com/mac4n6/FSEventsParser>

FSEventsParser-rs - <https://github.com/Houwenda/FSEventsParser-rs>

iLEAPP (iosFileSystemEvents) - <https://github.com/abrignoni/iLEAPP>

mac_apt (FSEVENTS) - <https://github.com/ydkhatri/mac_apt>
