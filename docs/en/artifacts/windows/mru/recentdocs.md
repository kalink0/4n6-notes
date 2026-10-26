---
title: "MRU - RecentDocs"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-access]
---

# MRU - RecentDocs

## Meaning

The Windows operating system keeps several so-called MRU (Most Recently Used) lists. Per user account, these generally store recently opened or saved files, recently executed commands and recently opened folders.

The purpose of the MRU lists is to give users a smoother experience, for example by offering the user their recently opened files.

From a digital forensics perspective, entries in the RecentDocs MRU list mean that the user account last opened, saved or created the listed files/folders, in the order of the respective last access, via Windows Explorer or an application that reports the file to the Windows shell as recently used. No statement can necessarily be made about the full path of the file/folder.

## Key facts

1. Subkeys per file extension and Folder, each with its own MRUListEx; files are usually listed in the main key and in the subkey of their extension
2. The last modification timestamp of the MRUListEx can indicate the opening of the most recent file. However, this timestamp is also changed by other actions (e.g. deleting an entry from the respective MRU). This artifact alone therefore only allows a very limited statement about the exact timestamp. More reliable is the last write time of the subkeys per file extension or Folder; it belongs to the newest entry there.
3. Files with identical names but different paths will only create one entry in the MRU list.
4. When a file is created or opened, the parent folder and possibly its parent folder are also entered; a folder entry therefore does not show that the folder was opened
5. Locations:  
   **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`**

## References

2022-09: <https://www.magnetforensics.com/blog/what-is-mru-most-recently-used/>

2019-03: <https://forensic4cast.com/2019/03/the-recentdocs-key-in-windows-10/>

## Tools

DLEAPP (windowsRecentDocs) - <https://github.com/abrignoni/DLEAPP>

Registry Explorer (RecentDocs Bookmark) - <https://ericzimmerman.github.io/>

RegRipper (recentdocs) - <https://github.com/keydet89/RegRipper4.0>
