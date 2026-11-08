---
title: "Autostart entries in the registry"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [persistence, program-execution]
---

# Autostart entries in the registry

## Meaning

Programs registered under certain registry keys are started automatically by Windows when a user logs on. The best known are the `Run` and `RunOnce` keys, each for the individual user and for all users of the system; programs under `RunOnce` are started only once, and the entry is deleted in the process. Entries are mostly created by installers, e.g. for messengers, cloud storage or updaters; they can, however, also be created directly in the registry. There are further autostart locations in the registry, e.g. Winlogon values and policy keys. If an autostart entry is disabled in Task Manager or in Settings, it remains in place; Windows stores the state separately under `StartupApproved`.

From a digital forensics perspective, an entry shows that the program with the given command line is to be started at every logon of the user or, for entries for all users, at every logon of any user. That an entry from `Run` or `RunOnce` was actually started is shown by the Shell-Core event log: Explorer records every command it starts there with its full command line and time. An entry marked as disabled under `StartupApproved` shows that the autostart was turned off and contains the time it was disabled.

## Key facts

1. Availability: `Run` and `RunOnce` in all Windows versions; `StartupApproved` since Windows 8
2. Prerequisites: entries for all users (HKLM) require administrator rights, entries for one's own user (HKCU) do not; `RunOnce` under HKLM is only run when a member of the Administrators group logs on; in Safe Mode the keys are ignored, except `RunOnce` values with `*` in front of the name
3. Retention: `Run` entries remain until they are deleted, e.g. on uninstallation; `RunOnce` values are deleted before they run, with `!` in front of the name only afterwards; if a `Run` value is deleted, the corresponding value under `StartupApproved` remains
4. Format and structure: one registry value per program, name freely chosen, data = command line; under `StartupApproved` a binary value with the same name and 12 bytes: first 4 bytes `02` or `06` = enabled, `03` = disabled, the remaining 8 bytes contain the time of disabling for disabled entries
5. Timestamps: the entries themselves have no timestamp; the key's LastWrite timestamp (UTC) gives the last change to any value below it; the time of disabling under `StartupApproved` is a FILETIME (UTC)
6. Particularities and pitfalls: values under `StartupApproved` are only created through Task Manager, Settings or installers, not when a `Run` value is created directly; a `Run` entry without a corresponding value counts as enabled; a disabling value can also be written directly to the registry; the order in which Windows starts the programs is not defined, and the start can be delayed; entries of 32-bit programs on 64-bit Windows are under `WOW6432Node`, their state under `StartupApproved\Run32`; the log `Microsoft-Windows-Shell-Core/Operational` records the start and end of processing a `Run` or `RunOnce` key (9705, 9706) and the start and end of each command with command line and process ID (9707, 9708), without stating whether the key belongs to the user or the system
7. Location:  
   User (NTUSER.DAT): **`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`**  
   User (NTUSER.DAT): **`HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce`**  
   All users (SOFTWARE): **`HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`**  
   All users (SOFTWARE): **`HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce`**  
   32-bit programs (SOFTWARE): **`HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run`**  
   State: **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved`**  
   State: **`HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved`**  
   Policies: **`HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run`**  
   Policies: **`HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run`**  
   Winlogon (values `Userinit`, `Shell`): **`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`**  
   Execution: **`C:\Windows\System32\winevt\Logs\Microsoft-Windows-Shell-Core%4Operational.evtx`**

## References

2024-07: <https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys>

2022-07: <https://windowsir.blogspot.com/2022/07/startupapprovedrun-pt-ii.html>

2022-07: <https://windowsir.blogspot.com/2022/07/does-autostart-really-mean-autostart.html>

2021-02: <https://nasbench.medium.com/finding-forensic-goodness-in-obscure-windows-event-logs-60e978ea45a3>

2019-02: <https://www.hexacorn.com/blog/2019/02/23/beyond-good-ol-run-key-part-104/>

## Tools

### Core tools

DLEAPP (parser: Autostart) - <https://github.com/abrignoni/DLEAPP>

Dissect (Plugin: runkeys) - <https://docs.dissect.tools/>

Velociraptor (artifact: Windows.Sys.StartupItems) - <https://docs.velociraptor.app/>

### Other tools

Autoruns - <https://learn.microsoft.com/sysinternals/downloads/autoruns>

juntei (parse-registry persistence) - <https://github.com/Yamato-Security/juntei>

PersistenceSniper (Get-RunAndRunOnce) - <https://github.com/last-byte/PersistenceSniper>

Plaso (Parser: windows_run) - <https://github.com/log2timeline/plaso>

regipy (Plugin: software_plugin, ntuser_persistence) - <https://github.com/mkorman90/regipy>

RegRipper (run, rundisabled) - <https://github.com/keydet89/RegRipper4.0>

WhatInStartup - <https://www.nirsoft.net/utils/what_run_in_startup.html>
