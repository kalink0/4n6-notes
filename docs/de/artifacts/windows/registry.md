---
title: "Windows Registry"
status: complete
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
topics: [system-config]
---

# Windows Registry

## Bedeutung

Die Windows Registry ist die zentrale Konfigurationsdatenbank von Windows-Betriebssystemen. Sie enthält u.a. Daten zu Benutzerprofilen, Systemhardware, installierten Programmen, Netzwerkverbindungen, Spuren angeschlossener USB-Geräte und zuletzt geöffneten Dateien.

Die digitalforensische Bedeutung der jeweiligen Daten muss individuell nach Schlüssel/Typ bewertet werden – die Registry ist kein einzelnes Artefakt, sondern ein Container für eine Vielzahl unabhängiger forensischer Fragestellungen.

## Spezifische Kurzinformation

1. Man unterscheidet Hives mit eigener Backing-File im Dateisystem und Root Keys, die zur Laufzeit vom System zusammengesetzt werden und keine eigene Datei besitzen:
   - **HKEY_CURRENT_USER (HKCU)** ist ein Alias auf `HKEY_USERS\{USER_SID}`. In einem Offline-Image sind die einzelnen `NTUSER.DAT`-Dateien der Profile maßgeblich.
   - **HKEY_CLASSES_ROOT (HKCR)** ist eine zur Laufzeit gemergte Sicht aus `HKLM\Software\Classes` und `HKCU\Software\Classes` (User-Einträge haben Vorrang vor System-Einträgen).
   - **HKEY_CURRENT_CONFIG (HKCC)** verweist auf `HKLM\SYSTEM\CurrentControlSet\Hardware Profiles\Current`.
2. **`HKLM\HARDWARE`** wird beim Systemstart dynamisch aus der Hardwareerkennung aufgebaut und besitzt keine Backing-File – nur per Live-Akquise erfassbar.
3. SAM, SECURITY, SOFTWARE und SYSTEM laden früh im Bootprozess. **NTUSER.DAT und UsrClass.dat laden erst beim Logon** des jeweiligen Users
4. Zeitstempel nur pro Schlüssel (LastWrite, UTC), nicht pro Wert
5. Zu jedem Hive gehörige `.LOG1`**/**`.LOG2`**-Dateien** (Transaktions-/Journal-Dateien) enthalten "dirty pages" – Änderungen, die noch nicht in den Haupt-Hive committet wurden; seit Windows 8.1 oft auch ältere Transaktionen
6. Gelöschte Schlüssel und Werte können im Hive verbleiben
7. Historische Registry-Stände können ergänzend über **RegBack** (`C:\Windows\System32\config\RegBack`, seit Windows 10 1803 standardmäßig deaktiviert (reaktivierbar über EnablePeriodicBackup) – sonst nur leere Platzhalter) oder über Volume Shadow Copies vorliegen.
8. Ablageort:  
   **`C:\Windows\System32\config`** (SYSTEM, SOFTWARE, SECURITY, SAM, DEFAULT)  
   **`%USERPROFILE%\NTUSER.DAT`**  
   **`%LOCALAPPDATA%\Microsoft\Windows\UsrClass.dat`**

### Mapping Root Key / Hive → Registry-Datei

| Root Key / Hive                | Typ                                                     | Registry-Datei             | Ladezeitpunkt              |
|--------------------------------|---------------------------------------------------------|----------------------------|----------------------------|
| HKEY_LOCAL_MACHINE\\SAM        | echter Hive                                             | SAM                        | Boot                       |
| HKEY_LOCAL_MACHINE\\SECURITY   | echter Hive                                             | SECURITY                   | Boot                       |
| HKEY_LOCAL_MACHINE\\SOFTWARE   | echter Hive                                             | SOFTWARE                   | Boot                       |
| HKEY_LOCAL_MACHINE\\SYSTEM     | echter Hive                                             | SYSTEM                     | Boot                       |
| HKEY_LOCAL_MACHINE\\HARDWARE   | volatil, kein Backing-File                              | –                          | Boot (dynamisch aufgebaut) |
| HKEY_USERS\\{USER_SID}         | echter Hive                                             | NTUSER.DAT (im Profilpfad) | Logon                      |
| HKEY_USERS\\{USER_SID}_Classes | echter Hive                                             | UsrClass.dat               | Logon                      |
| HKEY_USERS\\.DEFAULT           | echter Hive                                             | DEFAULT                    | Boot                       |
| HKEY_CURRENT_USER              | Alias auf HKEY_USERS\\{USER_SID}                        | –                          | –                          |
| HKEY_CLASSES_ROOT              | Merge aus HKLM...\\Classes + HKCU...\\Classes           | –                          | –                          |
| HKEY_CURRENT_CONFIG            | Verweis auf HKLM\\SYSTEM...\\Hardware Profiles\\Current | SYSTEM                     | Boot                       |

## Referenzen

2026-05: <https://github.com/libyal/libregf/blob/main/documentation/Windows%20NT%20Registry%20File%20(REGF)%20format.asciidoc>

2026-02: <https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/windows-registry-advanced-users>

2026-02: <https://learn.microsoft.com/en-us/troubleshoot/windows-client/installing-updates-features-roles/system-registry-no-backed-up-regback-folder>

2025-06: <https://www.cybertriage.com/blog/windows-registry-forensics-cheat-sheet-2025/>

2024-10: <https://projectzero.google/2024/10/the-windows-registry-adventure-4-hives.html>

2021-01: <https://learn.microsoft.com/en-us/windows/win32/sysinfo/hkey-classes-root-key>

2019-01: <https://cloud.google.com/blog/topics/threat-intelligence/digging-up-the-past-windows-registry-forensics-revisited/>

2026-10 (abgerufen): <https://renenyffenegger.ch/notes/Windows/registry/tree-structure/hive>

## Tools

RECmd - <https://github.com/EricZimmerman/RECmd>

RegRipper - <https://github.com/keydet89/RegRipper4.0>

Registry Explorer - <https://ericzimmerman.github.io/>

regipy (Python; Transaktionslogs: regipy-process-transaction-logs) - <https://github.com/mkorman90/regipy>

yarp - <https://github.com/msuhanov/yarp>

libregf - <https://github.com/libyal/libregf>