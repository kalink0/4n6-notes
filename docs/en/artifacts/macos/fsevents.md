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

From a digital forensics perspective, FSEvents entries allow statements about actions in the file system in relation to file names and file path. The sequential event IDs allow the order of the first change of different objects to be determined. However, several changes to the same object are combined into one entry; their order and frequency cannot be determined. The data also allows statements about files and folders that existed in the past. No statements can be made about the content of the files or about the actors.

## Key facts

1. The timestamps are NOT directly included in the FSEvents storage. However, the files, which contain up to 5000 events, have a timestamp of their own that narrows down the time period.
2. In addition to the storage in the file system, there is a buffer in memory - this means that the most recent file changes may not yet have been written to disk on a running system. In the event of a crash, hard reset, unclean unmounting of the volume or system upgrade, the events in the buffer are lost.
3. Location (root directory of each partition):  
   **`/.fseventsd`**  
   Data volume from macOS 10.15: **`/System/Volumes/Data/.fseventsd`**

## References

2024-06: <https://www.hexordia.com/blog/mac-forensics-analysis>

2018-11: <https://github.com/libyal/dtformats/blob/main/documentation/MacOS%20File%20System%20Events%20Disk%20Log%20Stream%20format.asciidoc>

2017-10: <https://www.osdfcon.org/presentations/2017/Ibrahim-Understanding-MacOS-File-Ststem-Events-with-FSEvents-Parser.pdf>

## Tools

DLEAPP (parser: FSEvents) - <https://github.com/abrignoni/DLEAPP>

FSEParser - <https://github.com/dlcowen/FSEventsParser>

FSEventsParser - <https://github.com/mac4n6/FSEventsParser>

FSEventsParser-rs - <https://github.com/Houwenda/FSEventsParser-rs>

mac_apt (plugin: FSEVENTS) - <https://github.com/ydkhatri/mac_apt>

Plaso (parser: fseventsd) - <https://github.com/log2timeline/plaso>

Velociraptor (artifact: MacOS.Forensics.FSEvents) - <https://docs.velociraptor.app/artifact_references/pages/macos.forensics.fsevents/>
