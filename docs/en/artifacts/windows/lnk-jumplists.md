---
title: "LNK - JumpLists"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-access, program-execution]
---

# LNK - JumpLists

## Meaning

JumpLists have been used in the operating system since Windows 7. JumpLists show the user recently opened files and recently used programs, for example in the Start menu. The feature serves to increase usability and is carried out by the operating system itself based on the user's operation.

A user can also "pin" entries themselves, e.g. to the Start menu - this feature also serves usability, and the entries are also stored in JumpLists. This feature can be described as setting "favourites". In addition, for the automatically generated entries, the timestamps of the last access and the number of accesses are stored.

From a digital forensics perspective, the existence of JumpLists means the following:

1. For the automatically generated entries:
   1. The user account last opened/started the given target file (according to the file name) at the given time (last accessed).
   2. The user account opened the file/program for the first time at the given time (creation date). The system therefore created the entry.
2. For the manually created entries:
   1. The user account last opened/started the given target file (according to the file name) at the given time (last accessed).
   2. The user account actively "pinned" the file/program at the given time (creation date). This can also be done as part of a program installation.

## Key facts

1. JumpLists are assigned to apps, which can be identified by AppID (lists see below) - an AppID indicates in which context the JumpList exists and therefore gives information on how the user account performed the action.
2. The number of accesses (interaction count) cannot be exactly explained/traced according to current knowledge, and the value should therefore be treated with caution.
3. Location:  
   **`%AppData%\Microsoft\Windows\Recent\AutomaticDestinations`**  
   **`%AppData%\Microsoft\Windows\Recent\CustomDestinations`**

## References

2025-01: <https://www.cybertriage.com/blog/what-is-jump-list-cache/>

2025-01: <https://www.cybertriage.com/blog/jump-list-forensics-2025/>

2025-01: <https://windowsir.blogspot.com/2025/01/artifacts-jump-lists.html>

2020-09: <https://dfir.pubpub.org/pub/wfuxlu9v/release/1>

2020-02: <https://cloud.google.com/blog/topics/threat-intelligence/the-missing-lnk-correlating-user-search-lnk-files/>

2016-02: <https://binaryforay.blogspot.com/2016/02/jump-lists-in-depth-understand-format.html>

2010-06: <http://computerforensics.parsonage.co.uk/downloads/TheMeaningofLIFE.pdf>

#### JumpList IDs:

<https://forensics.wiki/list_of_jump_list_ids/>

<https://github.com/EricZimmerman/JumpList/blob/master/JumpList/Resources/AppIDs.txt>

## Tools

JLECmd - <https://ericzimmerman.github.io/>

JumpList Explorer - <https://ericzimmerman.github.io/>

LECmd - <https://ericzimmerman.github.io/>

Jumplist-Browser - <https://github.com/kacos2000/Jumplist-Browser>
