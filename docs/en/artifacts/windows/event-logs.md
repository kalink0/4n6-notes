---
title: "EventLogs"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [accounts, network, external-devices, program-execution, persistence, device-state, commands-input, system-config]
---

# EventLogs

## Meaning

Through the Windows Event Log service, Windows logs events of the operating system, of services and of applications. Administrators use the logs for troubleshooting and monitoring; the Security log is used for security monitoring, for example of logons and privilege changes. Each event has an event ID, a timestamp and, depending on the type, further data fields.

What an event shows from a digital forensics perspective depends on the log and event ID. The absence of an event does not show that the action did not take place, as logging depends on the audit policy and the log size.

The table only contains a selection of frequently relevant events; Windows logs far more event IDs in numerous further logs.

| Entry type (log, event ID) | Shows | Relevant fields |
| --- | --- | --- |
| `Security` 4624 | Successful logon; the type follows from the logon type (2 local, 3 network, 10 RDP) | `TargetUserName`, `LogonType`, `IpAddress`, `TargetLogonId` |
| `Security` 4625 | Failed logon | `TargetUserName`, `LogonType`, `IpAddress`, `Status`, `SubStatus` |
| `Security` 4634, 4647 | Logoff or user-initiated logoff | `TargetLogonId` |
| `Security` 4648 | Logon with explicitly specified credentials, e.g. "Run as" | `SubjectUserName`, `TargetUserName`, `TargetServerName`, `ProcessName` |
| `Security` 4672 | Logon with special privileges (administrator) | `SubjectUserName`, `SubjectLogonId` |
| `Security` 4720, 4726, 4732 | User account created, deleted or added to a local group | `TargetUserName`, `SubjectUserName`, `MemberSid` |
| `Security` 4688 | Process started | `NewProcessName`, `CommandLine`, `SubjectUserName` |
| `Security` 4697, `System` 7045 | Service installed | `ServiceName`, `ServiceFileName` or `ImagePath` |
| `Security` 4698 | Scheduled task created | `TaskName`, `TaskContent` |
| `TaskScheduler/Operational` 106, 200 | Task registered or action of a task started | `TaskName` |
| `TerminalServices-LocalSessionManager/Operational` 21, 22, 24, 25 | RDP session logged on, shell started, session disconnected or reconnected | `User`, `Address` |
| `TerminalServices-RemoteConnectionManager/Operational` 1149 | Successful authentication of an RDP connection | `Param1`, `Param3` |
| `TerminalServices-RDPClient/Operational` 1024 | Outgoing RDP connection to the named target system | `Value` |
| `Partition/Diagnostic` 1006 | Drive connected or removed, with manufacturer, model and serial number | `Manufacturer`, `Model`, `SerialNumber`, `Vbr0` |
| `WLAN-AutoConfig/Operational` 8001, 8003 | Connection to a Wi-Fi network established or disconnected | `SSID` |
| `PowerShell/Operational` 4104 | Executed PowerShell script block | `ScriptBlockText` |
| `System` 12, 13 | System start or shutdown | `StartTime`, `StopTime` |
| `System` 1074, 6008 | Shutdown or restart by a process or user; unexpected shutdown | – |
| `Security` 4616 | System time changed | `PreviousTime`, `NewTime`, `ProcessName` |
| `Security` 1102, `System` 104 | Security log or another log cleared | `SubjectUserName`, `Channel` |

## Key facts

1. Since Windows Vista in the EVTX format, up to Windows XP / Server 2003 in the older EVT format
2. One file per log; besides Application, Security and System, numerous further logs of services and applications (`%4` instead of `/` in the file name)
3. Default size of the main logs approx. 20 MB; once it is reached, the oldest entries are overwritten, alternatively Windows archives the full log as `Archive-*.evtx`
4. Many Security events are only created if the audit policy is set accordingly, e.g. process start (4688, additionally the command line) and scheduled tasks (4698)
5. A log can only be cleared completely, and the clearing is itself logged (1102 or 104)
6. Timestamps in UTC
7. The location of the main logs may have been changed via the registry, value `File` under:  
   **`HKLM\SYSTEM\CurrentControlSet\Services\EventLog\{LOG}`**

8. Location (default):  
   From Windows Vista: **`C:\Windows\System32\winevt\Logs\*.evtx`**  
   Up to Windows XP: **`C:\Windows\System32\config\*.evt`**

## References

2026-09: <https://nxlog.co/news-and-blog/posts/windows-task-scheduler-event-ids/>

2026-02: <https://blog.elcomsoft.com/2026/02/forensic-analysis-of-windows-10-and-11-event-logs/>

2021-07: <https://atropos4n6.com/windows/extract-vsns-from-windows-partition4diagnostic-evtx/>

2017-12: <https://blogs.jpcert.or.jp/en/2017/12/research-report-released-detecting-lateral-movement-through-tracking-event-logs-version-2.html>

2015-11: [Microsoft: Windows security audit events (spreadsheet)](https://www.microsoft.com/download/details.aspx?id=50034)

## Tools

EvtxECmd - <https://ericzimmerman.github.io/>

evtx (evtx_dump) - <https://github.com/omerbenamram/evtx>

Hayabusa - <https://github.com/Yamato-Security/hayabusa>

Chainsaw - <https://github.com/WithSecureLabs/chainsaw>

peach - <https://github.com/kalink0/peach-forensics>

DLEAPP (parser: Windows Security Logons, Windows Account Management, Windows Process Creation, Windows Service Installations, Task Scheduler Task Registrations, Task Scheduler Task Actions, Windows Terminal Services Sessions, Windows Remote Desktop Connections, Remote Desktop Client Connections, Partition Diagnostic Disk Events, WLAN Connection Events, PowerShell Script Blocks, Kernel Boot Events, Windows Security Time Changes, Event Logs Cleared) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (artifacts: Windows.EventLogs.Evtx, Windows.EventLogs.EvtxHunter, Windows.EventLogs.RDPAuth) - <https://github.com/Velocidex/velociraptor>

Dissect (plugin: evtx, evt) - <https://github.com/fox-it/dissect>

Partition-4DiagnosticParser - <https://github.com/theAtropos4n6/Partition-4DiagnosticParser>
