---
title: "MRU - LastVisitedPidlMRU"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-access]
---

# MRU - LastVisitedPidlMRU

## Meaning

The Windows operating system keeps several so-called MRU (Most Recently Used) lists. Per user account, these generally store recently opened or saved files, recently executed commands and recently opened folders.

The purpose of the MRU lists is to give users a smoother experience, for example by offering the user their recently opened files.

From a digital forensics perspective, entries in the LastVisited MRU mean that the user account used the Microsoft dialog box (Open/Save) via the listed application and that the given folder was the last folder used in it.

## Key facts

1. There is only one entry per application
2. Order via `MRUListEx` (Windows XP: `MRUList`); the last write time of the key only belongs to the newest entry
3. This MRU correlates with the MRU - OpenSavePidlMRU - a new entry there also updates the application's entry in this MRU
4. Locations:  
   from Windows Vista: **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU`**  
   Windows XP: **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedMRU`**

## References

2024-04: <https://www.dr-datenschutz.de/it-forensische-informationen-durch-dateioeffnungen-gewinnen/>

2022-09: <https://www.magnetforensics.com/blog/what-is-mru-most-recently-used/>

2010-04: <https://www.sans.org/blog/opensavemru-and-lastvisitedmru/>

## Tools

DLEAPP (windowsUserMru) - <https://github.com/abrignoni/DLEAPP>

Registry Explorer (ComDlg32 Bookmark) - <https://ericzimmerman.github.io/>

RegRipper (comdlg32) - <https://github.com/keydet89/RegRipper4.0>
