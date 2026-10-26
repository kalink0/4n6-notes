---
title: "Windows Search Index"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-existence]
---

# Windows Search Index

## Meaning

The Windows Search Index is an index populated by the Windows Search service. The files in the indexed locations (by default the user profile and the Start menu) are indexed in order to enable the user to search the system easily and quickly. Besides files and folders, further data is also indexed, such as Outlook email data.

From a digital forensics perspective, entries for files and folders in the Windows Search Index mean that they must have been present on the system under the given path and file name at the time of the last change to this file in the index.

## Key facts

1. Up to Windows 10 the data is stored in an ESE database, from Windows 11 in 2 SQLite databases
2. Indexed by default: user profile (without AppData) and Start menu; not active by default on Windows Server
3. Also contains data on other artifacts (e.g. Windows Timeline).
4. Also contains excerpts of file contents as well as the browser history of Internet Explorer and Edge
5. Deleted entries can remain in the database
6. Location:  
   Windows XP: **`C:\Documents and Settings\All Users\Application Data\Microsoft\Search\Data\Applications\Windows\Windows.edb`**  
   Windows Vista - Windows 10: **`C:\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.edb`**  
   From Windows 11: **`C:\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.db*`**  
   From Windows 11: **`C:\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows-gather.db*`**

## References

2023-04: <https://levelblue.com/blogs/strozfriedberg/windows-search-index-the-forensic-artifact-youve-been-searching-for>

2020-05: <https://www.forensicfocus.com/articles/windows-search-forensics/>

## Tools

Search Index DB Reporter - <https://github.com/strozfriedberg/sidr>

DLEAPP (parser: Windows Search Index, Windows 11 Search Index) - <https://github.com/abrignoni/DLEAPP>

WinSearchDBAnalyzer (up to Windows 10) - <https://github.com/moaistory/WinSearchDBAnalyzer>

ESEDatabaseView (up to Windows 10) - <https://www.nirsoft.net/utils/ese_database_view.html>

DB Browser for SQLite (from Windows 11) - <https://sqlitebrowser.org/>
