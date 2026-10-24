---
title: "EventLogs"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [accounts, network, external-devices, program-execution, persistence, device-state, commands-input, system-config]
---

# EventLogs

## Bedeutung

Windows protokolliert über den Dienst Windows-Ereignisprotokoll Ereignisse des Betriebssystems, von Diensten und von Anwendungen. Administratoren nutzen die Protokolle zur Fehlersuche und Überwachung, das Security-Protokoll dient der Sicherheitsüberwachung, etwa von Anmeldungen und Rechteänderungen. Jedes Ereignis hat eine Ereignis-ID, einen Zeitstempel und je nach Typ weitere Datenfelder.

Was ein Ereignis aus digitalforensischer Sicht belegt, hängt von Protokoll und Ereignis-ID ab. Das Fehlen eines Ereignisses belegt nicht, dass der Vorgang nicht stattgefunden hat, da die Protokollierung von Überwachungsrichtlinie und Protokollgröße abhängt.

Die Tabelle enthält nur eine Auswahl häufig relevanter Ereignisse; Windows protokolliert in zahlreichen weiteren Protokollen weit mehr Ereignis-IDs.

| Eintragstyp (Protokoll, Ereignis-ID) | Belegt | Relevante Felder |
| --- | --- | --- |
| `Security` 4624 | Erfolgreiche Anmeldung; die Art ergibt sich aus dem Logon Type (2 lokal, 3 Netzwerk, 10 RDP) | `TargetUserName`, `LogonType`, `IpAddress`, `TargetLogonId` |
| `Security` 4625 | Fehlgeschlagene Anmeldung | `TargetUserName`, `LogonType`, `IpAddress`, `Status`, `SubStatus` |
| `Security` 4634, 4647 | Abmeldung bzw. vom Benutzer ausgelöste Abmeldung | `TargetLogonId` |
| `Security` 4648 | Anmeldung mit explizit angegebenen Anmeldedaten, z. B. „Ausführen als“ | `SubjectUserName`, `TargetUserName`, `TargetServerName`, `ProcessName` |
| `Security` 4672 | Anmeldung mit besonderen Rechten (Administrator) | `SubjectUserName`, `SubjectLogonId` |
| `Security` 4720, 4726, 4732 | Benutzerkonto angelegt, gelöscht bzw. einer lokalen Gruppe hinzugefügt | `TargetUserName`, `SubjectUserName`, `MemberSid` |
| `Security` 4688 | Prozess gestartet | `NewProcessName`, `CommandLine`, `SubjectUserName` |
| `Security` 4697, `System` 7045 | Dienst installiert | `ServiceName`, `ServiceFileName` bzw. `ImagePath` |
| `Security` 4698 | Geplanter Task angelegt | `TaskName`, `TaskContent` |
| `TaskScheduler/Operational` 106, 200 | Task registriert bzw. Aktion eines Tasks gestartet | `TaskName` |
| `TerminalServices-LocalSessionManager/Operational` 21, 22, 24, 25 | RDP-Sitzung angemeldet, Shell gestartet, Sitzung getrennt bzw. wiederverbunden | `User`, `Address` |
| `TerminalServices-RemoteConnectionManager/Operational` 1149 | Erfolgreiche Authentifizierung einer RDP-Verbindung | `Param1`, `Param3` |
| `TerminalServices-RDPClient/Operational` 1024 | Ausgehende RDP-Verbindung zum genannten Zielsystem | `Value` |
| `Partition/Diagnostic` 1006 | Datenträger angeschlossen bzw. entfernt, mit Hersteller, Modell und Seriennummer | `Manufacturer`, `Model`, `SerialNumber`, `Vbr0` |
| `WLAN-AutoConfig/Operational` 8001, 8003 | Verbindung mit einem WLAN hergestellt bzw. getrennt | `SSID` |
| `PowerShell/Operational` 4104 | Ausgeführter PowerShell-Skriptblock | `ScriptBlockText` |
| `System` 12, 13 | Systemstart bzw. Herunterfahren | `StartTime`, `StopTime` |
| `System` 1074, 6008 | Herunterfahren oder Neustart durch Prozess bzw. Benutzer; unerwartetes Herunterfahren | – |
| `Security` 4616 | Systemzeit geändert | `PreviousTime`, `NewTime`, `ProcessName` |
| `Security` 1102, `System` 104 | Security-Protokoll bzw. ein anderes Protokoll gelöscht | `SubjectUserName`, `Channel` |

## Spezifische Kurzinformation

1. Seit Windows Vista im Format EVTX, bis Windows XP / Server 2003 im älteren Format EVT
2. Eine Datei pro Protokoll; neben Application, Security und System zahlreiche weitere Protokolle von Diensten und Anwendungen (im Dateinamen `%4` statt `/`)
3. Standardgröße der Hauptprotokolle ca. 20 MB; ist sie erreicht, werden die ältesten Einträge überschrieben, alternativ archiviert Windows das volle Protokoll als `Archive-*.evtx`
4. Viele Security-Ereignisse entstehen nur bei entsprechend gesetzter Überwachungsrichtlinie, z. B. Prozessstart (4688, die Befehlszeile zusätzlich) und geplante Tasks (4698)
5. Ein Protokoll lässt sich nur vollständig löschen, und das Löschen wird selbst protokolliert (1102 bzw. 104)
6. Zeitstempel in UTC
7. Der Ablageort der Hauptprotokolle kann über die Registry geändert sein, Wert `File` unter:  
   **`HKLM\SYSTEM\CurrentControlSet\Services\EventLog\{LOG}`**

8. Ablageort (Default):  
   Ab Windows Vista: **`C:\Windows\System32\winevt\Logs\*.evtx`**  
   Bis Windows XP: **`C:\Windows\System32\config\*.evt`**

## Referenzen

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

DLEAPP (Parser: Windows Security Logons, Windows Account Management, Windows Process Creation, Windows Service Installations, Task Scheduler Task Registrations, Task Scheduler Task Actions, Windows Terminal Services Sessions, Windows Remote Desktop Connections, Remote Desktop Client Connections, Partition Diagnostic Disk Events, WLAN Connection Events, PowerShell Script Blocks, Kernel Boot Events, Windows Security Time Changes, Event Logs Cleared) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (Artefakte: Windows.EventLogs.Evtx, Windows.EventLogs.EvtxHunter, Windows.EventLogs.RDPAuth) - <https://github.com/Velocidex/velociraptor>

Dissect (Plugin: evtx, evt) - <https://github.com/fox-it/dissect>

Partition-4DiagnosticParser - <https://github.com/theAtropos4n6/Partition-4DiagnosticParser>