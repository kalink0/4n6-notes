---
title: "MRU - OpenSavePidlMRU"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-access]
---

# MRU - OpenSavePidlMRU

## Meaning

The Windows operating system keeps several so-called MRU (Most Recently Used) lists. Per user account, these generally store recently opened or saved files, recently executed commands and recently opened folders.

The purpose of the MRU lists is to give users a smoother experience, for example by offering the user their recently opened files.

From a digital forensics perspective, entries in the Open/Save MRU mean that the user account opened/saved the folder/file via the Microsoft dialog box (Open/Save). The order in the MRU list corresponds to the order of the respective last opening/saving.

## Key facts

1. There is one MRU per file extension; in addition, the subkey `*` contains the recently opened/saved files of all extensions
2. Order via `MRUListEx` (Windows XP: `MRUList`); the last write time of a subkey only belongs to the respective newest entry
3. This MRU correlates with the MRU - LastVisitedPidlMRU - a new entry there is also a new entry in this MRU
4. Locations:  
   from Windows Vista: **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU`**  
   Windows XP: **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU`**

## References

2024-04: <https://www.dr-datenschutz.de/it-forensische-informationen-durch-dateioeffnungen-gewinnen/>

2022-09: <https://www.magnetforensics.com/blog/what-is-mru-most-recently-used/>

2010-04: <https://www.sans.org/blog/opensavemru-and-lastvisitedmru/>

## Tools

DLEAPP (windowsUserMru) - <https://github.com/abrignoni/DLEAPP>

Registry Explorer (ComDlg32 Bookmark) - <https://ericzimmerman.github.io/>

RegRipper (comdlg32) - <https://github.com/keydet89/RegRipper4.0>
