---
title: "Windows Registry"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [system-config]
---

# Windows Registry

## Meaning

The Windows Registry is the central configuration database of Windows operating systems. Among other things, it contains data on user profiles, system hardware, installed programs, network connections, traces of connected USB devices and recently opened files.

The digital forensic meaning of the respective data has to be assessed individually by key/type – the registry is not a single artifact but a container for a large number of independent forensic questions.

## Key facts

1. A distinction is made between hives with their own backing file in the file system and root keys that are assembled by the system at runtime and have no file of their own:
   - **HKEY_CURRENT_USER (HKCU)** is an alias for `HKEY_USERS\{USER_SID}`. In an offline image, the individual `NTUSER.DAT` files of the profiles are authoritative.
   - **HKEY_CLASSES_ROOT (HKCR)** is a view merged at runtime from `HKLM\Software\Classes` and `HKCU\Software\Classes` (user entries take precedence over system entries).
   - **HKEY_CURRENT_CONFIG (HKCC)** points to `HKLM\SYSTEM\CurrentControlSet\Hardware Profiles\Current`.
2. **`HKLM\HARDWARE`** is built dynamically from hardware detection at system start and has no backing file – it can only be captured via live acquisition.
3. SAM, SECURITY, SOFTWARE and SYSTEM load early in the boot process. **NTUSER.DAT and UsrClass.dat only load at logon** of the respective user
4. Timestamps only per key (LastWrite, UTC), not per value
5. The `.LOG1`**/**`.LOG2` **files** belonging to each hive (transaction/journal files) contain "dirty pages" – changes that have not yet been committed to the main hive; since Windows 8.1 often also older transactions
6. Deleted keys and values can remain in the hive
7. Historical registry states may additionally be available via **RegBack** (`C:\Windows\System32\config\RegBack`, disabled by default since Windows 10 1803 (can be re-enabled via EnablePeriodicBackup) – otherwise only empty placeholders) or via Volume Shadow Copies.
8. Location:  
   **`C:\Windows\System32\config`** (SYSTEM, SOFTWARE, SECURITY, SAM, DEFAULT)  
   **`%USERPROFILE%\NTUSER.DAT`**  
   **`%LOCALAPPDATA%\Microsoft\Windows\UsrClass.dat`**

### Mapping root key / hive → registry file

| Root key / hive                | Type                                                    | Registry file              | Load time                  |
|--------------------------------|---------------------------------------------------------|----------------------------|----------------------------|
| HKEY_LOCAL_MACHINE\\SAM        | real hive                                               | SAM                        | Boot                       |
| HKEY_LOCAL_MACHINE\\SECURITY   | real hive                                               | SECURITY                   | Boot                       |
| HKEY_LOCAL_MACHINE\\SOFTWARE   | real hive                                               | SOFTWARE                   | Boot                       |
| HKEY_LOCAL_MACHINE\\SYSTEM     | real hive                                               | SYSTEM                     | Boot                       |
| HKEY_LOCAL_MACHINE\\HARDWARE   | volatile, no backing file                               | –                          | Boot (built dynamically)   |
| HKEY_USERS\\{USER_SID}         | real hive                                               | NTUSER.DAT (in profile path) | Logon                    |
| HKEY_USERS\\{USER_SID}_Classes | real hive                                               | UsrClass.dat               | Logon                      |
| HKEY_USERS\\.DEFAULT           | real hive                                               | DEFAULT                    | Boot                       |
| HKEY_CURRENT_USER              | alias for HKEY_USERS\\{USER_SID}                        | –                          | –                          |
| HKEY_CLASSES_ROOT              | merge of HKLM...\\Classes + HKCU...\\Classes            | –                          | –                          |
| HKEY_CURRENT_CONFIG            | points to HKLM\\SYSTEM...\\Hardware Profiles\\Current   | SYSTEM                     | Boot                       |

## References

2026-05: <https://github.com/libyal/libregf/blob/main/documentation/Windows%20NT%20Registry%20File%20(REGF)%20format.asciidoc>

2026-02: <https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/windows-registry-advanced-users>

2026-02: <https://learn.microsoft.com/en-us/troubleshoot/windows-client/installing-updates-features-roles/system-registry-no-backed-up-regback-folder>

2025-06: <https://www.cybertriage.com/blog/windows-registry-forensics-cheat-sheet-2025/>

2024-10: <https://projectzero.google/2024/10/the-windows-registry-adventure-4-hives.html>

2021-01: <https://learn.microsoft.com/en-us/windows/win32/sysinfo/hkey-classes-root-key>

2019-01: <https://cloud.google.com/blog/topics/threat-intelligence/digging-up-the-past-windows-registry-forensics-revisited/>

2026-10 (accessed): <https://renenyffenegger.ch/notes/Windows/registry/tree-structure/hive>

## Tools

RECmd - <https://github.com/EricZimmerman/RECmd>

RegRipper - <https://github.com/keydet89/RegRipper4.0>

Registry Explorer - <https://ericzimmerman.github.io/>

regipy (Python; transaction logs: regipy-process-transaction-logs) - <https://github.com/mkorman90/regipy>

yarp - <https://github.com/msuhanov/yarp>

libregf - <https://github.com/libyal/libregf>
