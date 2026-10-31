---
title: "MUI - Multilingual User Interface - Cache"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution]
---

# MUI - Multilingual User Interface - Cache

## Meaning

In Windows operating systems, the MUI (Multilingual User Interface) cache serves to ensure multilingual support. The aim is to be able to offer the user as complete a translation as possible of all programs executed on the Windows system. For this, data such as file path and name is *stored/used/...*

From a digital forensics perspective, entries in the MUI cache mean that the program was executed on the system under the given path and name in the session of the user account and displayed a user interface there. The account under which the process ran can differ (e.g. with "Run as").

## Key facts

1. Format and structure: contains the path, the name and possibly version information from the PE file
2. Timestamps: there are no timestamps
3. Special features and pitfalls: only programs with a GUI component are logged. Per user account
4. Location:  
   Up to Windows XP: **`NTUSER.dat - HKCU\Software\Microsoft\Windows\ShellNoRoam\MUICache`**  
   From Windows Vista: **`USRCLASS.dat - Local Settings\Software\Microsoft\Windows\Shell\MuiCache`**  
   From Windows Vista (live system): **`HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache`**

## References

2026-03: <https://www.cybertriage.com/blog/muicache-2026-guide/>

2022-04: <https://www.magnetforensics.com/blog/forensic-analysis-of-muicache-files-in-windows/>

## Tools

RegRipper (muicache) - <https://github.com/keydet89/RegRipper4.0>

Registry Explorer - <https://ericzimmerman.github.io/>

MUICacheView - <https://www.nirsoft.net/utils/muicache_view.html>
