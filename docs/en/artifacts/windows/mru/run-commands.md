---
title: "MRU - RunMRU"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [commands-input]
---

# MRU - RunMRU

## Meaning

The Windows operating system keeps several so-called MRU (Most Recently Used) lists. Per user account, these generally store recently opened or saved files, recently executed commands and recently opened folders.

The purpose of the MRU lists is to give users a smoother experience, for example by offering the user their recently opened files.

From a digital forensics perspective, entries in the Run commands MRU mean that the listed commands were executed in the context of the user account in the operating system's "Run" dialog, in the order of the respective last execution.

## Key facts

1. Not written if tracking of app launches is disabled in the privacy settings
2. Values a to z, a maximum of 26 entries; a command that is executed again only moves up in the order
3. Order via `MRUList`; the last write time of the key only belongs to the newest entry
4. Commands that cannot be executed (e.g. non-existent file) are not entered
5. Locations:  
   **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU`**

## References

2026-03: <https://www.cybertriage.com/blog/how-to-investigate-runmru-2025/>

2022-09: <https://www.magnetforensics.com/blog/what-is-mru-most-recently-used/>

## Tools

DLEAPP (windowsUserMru) - <https://github.com/abrignoni/DLEAPP>

Registry Explorer (RunMRU Bookmark) - <https://ericzimmerman.github.io/>

RegRipper (runmru) - <https://github.com/keydet89/RegRipper4.0>
