---
title: "Startup folder"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [persistence]
---

# Startup folder

## Meaning

The Startup folder is a folder in the Start menu whose content Windows Explorer starts automatically when a user logs on. There is one folder per user and one for all users of the system. It usually contains shortcuts (LNK files) to programs created by installers or by the user; other files are opened with the program associated with their file type, so executables and scripts (e.g. `.exe`, `.bat`, `.vbs`) are run. If an entry is disabled in Task Manager or in Settings, the file remains in the folder; Windows stores the state separately in the registry under `StartupApproved`.

From a digital forensics perspective, a file in the Startup folder shows that it is to be started at every logon of the user or, for the all-users folder, at every logon of any user. The file's timestamps show when it was created in the folder and last modified; a shortcut additionally contains the path and metadata of its target. A value marked as disabled under `StartupApproved` shows that the autostart was turned off and contains the time it was disabled.

## Key facts

1. Availability: in all Windows versions; `StartupApproved\StartupFolder` since Windows 8
2. Prerequisites: files in the all-users folder require administrator rights, in one's own folder they do not
3. Retention: the file remains until it is deleted; a value under `StartupApproved\StartupFolder` is only created when the entry is toggled in Task Manager or in Settings; a file without a corresponding value counts as enabled
4. Format and structure: any files, usually LNK; Explorer shows the folder as "Startup" (localized), on disk it has been named `Startup` or `StartUp` since Windows Vista; under `StartupApproved\StartupFolder` a binary value named after the file with 12 bytes: first 4 bytes `02` or `06` = enabled, `03` = disabled, the remaining 8 bytes contain the time of disabling for disabled entries
5. Timestamps: the file's timestamps in the file system; for LNK files additionally the timestamps of the target stored in them; the time of disabling under `StartupApproved` is a FILETIME (UTC)
6. Particularities and pitfalls: the location of the folders can be redirected via the values `Startup` and `Common Startup` under `User Shell Folders`; Windows then starts the files in the new folder, and the default folder stays empty; if a file is moved into the folder within the same drive, it keeps its original creation time; the order in which Windows starts the files is not defined, and the start can be delayed
7. Location:  
   User: **`%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`**  
   All users: **`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`**  
   Up to Windows XP (English): **`C:\Documents and Settings\{USER}\Start Menu\Programs\Startup`**  
   State: **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\StartupFolder`**  
   State: **`HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\StartupFolder`**  
   Redirection (value `Startup`): **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders`**  
   Redirection (value `Common Startup`): **`HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders`**

## References

2026-11: <https://attack.mitre.org/techniques/T1547/001/>

2022-07: <https://windowsir.blogspot.com/2022/07/does-autostart-really-mean-autostart.html>

## Tools

### Core tools

DLEAPP (Parser: Startup Folder Items, Startup Approved States) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (artifact: Windows.Sys.StartupItems) - <https://docs.velociraptor.app/>

LECmd - <https://ericzimmerman.github.io/>

### Other tools

Autoruns - <https://learn.microsoft.com/sysinternals/downloads/autoruns>

juntei (persistence-hunter) - <https://github.com/Yamato-Security/juntei>

PersistenceSniper (Get-StartupPrograms) - <https://github.com/last-byte/PersistenceSniper>

RegRipper (rundisabled) - <https://github.com/keydet89/RegRipper4.0>

WhatInStartup - <https://www.nirsoft.net/utils/what_run_in_startup.html>
