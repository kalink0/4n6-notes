---
title: "Sysmon"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution, network, file-existence, persistence]
---

# Sysmon

## Meaning

Sysmon (System Monitor) is a Windows system service and device driver from Microsoft (Sysinternals) that remains permanently in the system after installation and logs detailed process, file, network and registry activity. Unlike the standard Windows event logs, Sysmon is **not active by default** and must be installed separately (Sysinternals) or enabled (from Windows 11/Server 2025 as an optional feature) and configured – the availability of Sysmon data on an examined system is therefore not guaranteed but depends on prior use (usually by the organisation concerned, e.g. as part of EDR/monitoring).

From a digital forensics perspective, Sysmon – if installed and active beforehand – provides a much more granular view of system activity than the built-in Windows tools, including full command lines, hash values of executed files and parent-child process relationships.

## Key facts

1. Sysmon is part of the **Sysinternals suite** (Microsoft); since 2026 also included as an optional feature in Windows 11/Server 2025, disabled by default
2. Runs as a system service and kernel driver; the scope of logging depends on the XML configuration and differs per installation
3. Events go to a separate event log channel: `Microsoft-Windows-Sysmon/Operational` (not the classic Security log).
4. Provides, among other things, full command lines, hash values of executed files as well as parent process information
5. Location:  
   Event log: **`%SystemRoot%\System32\Winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx`**  
   Binary: **`%SystemRoot%\Sysmon64.exe`** (name can be changed during installation)  
   Configuration: **`HKLM\SYSTEM\CurrentControlSet\Services\SysmonDrv\Parameters`** (value `Rules`; key name follows a renamed driver if applicable)

## References

2026-09: <https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon>

2026-02: <https://learn.microsoft.com/en-us/windows/security/operating-system-security/sysmon/sysmon-events>

2026-02: <https://learn.microsoft.com/en-us/windows/security/operating-system-security/sysmon/overview>

## List of event codes

| Event ID | Event | An entry shows that … |
|---|---|---|
| 1 | Process Create | a process with the given image, command line and parent process was started under the given user account |
| 2 | File creation time changed | a process changed the creation timestamp of a file (old and new value) |
| 3 | Network connection | a process had a TCP/UDP connection with the given source and destination addresses |
| 4 | Sysmon service state changed | the Sysmon service was started or stopped |
| 5 | Process terminated | a process was terminated |
| 6 | Driver loaded | a driver was loaded |
| 7 | Image loaded | a process loaded a module (e.g. DLL) |
| 8 | CreateRemoteThread | a process created a thread in another process |
| 9 | RawAccessRead | a process directly read from a drive (`\\.\`) |
| 10 | ProcessAccess | a process opened a handle to another process |
| 11 | FileCreate | a file was created or overwritten |
| 12 | RegistryEvent (Object create and delete) | a registry key or value was created or deleted |
| 13 | RegistryEvent (Value Set) | a registry value was set |
| 14 | RegistryEvent (Key and Value Rename) | a registry key or value was renamed |
| 15 | FileCreateStreamHash | an alternate data stream was created (e.g. Zone.Identifier) |
| 16 | ServiceConfigurationChange | the Sysmon configuration was changed |
| 17 | PipeEvent (Pipe Created) | a named pipe was created |
| 18 | PipeEvent (Pipe Connected) | a connection to a named pipe was established |
| 19 | WmiEvent (WmiEventFilter) | a WMI event filter was registered |
| 20 | WmiEvent (WmiEventConsumer) | a WMI consumer was registered |
| 21 | WmiEvent (WmiEventConsumerToFilter) | a WMI consumer was bound to a filter |
| 22 | DNSEvent | a process made a DNS query (name and result) |
| 23 | FileDelete | a file was deleted and a copy archived |
| 24 | ClipboardChange | the content of the clipboard was changed |
| 25 | ProcessTampering | the image of a running process was modified (e.g. process hollowing) |
| 26 | FileDeleteDetected | a file was deleted (without archiving) |
| 27 | FileBlockExecutable | the creation of an executable file was blocked |
| 28 | FileBlockShredding | the overwriting (shredding) of a file was blocked |
| 29 | FileExecutableDetected | the creation of an executable file was detected |
| 255 | Error | an internal Sysmon error occurred |

## Tools

EvtxECmd (Eric Zimmerman) - <https://github.com/EricZimmerman/evtx>

Chainsaw - <https://github.com/WithSecureLabs/chainsaw>

Hayabusa - <https://github.com/Yamato-Security/hayabusa>

DLEAPP (parser: Sysmon) - <https://github.com/abrignoni/DLEAPP>
