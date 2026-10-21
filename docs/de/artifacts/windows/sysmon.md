---
title: "Sysmon"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [program-execution, network, file-existence, persistence]
---

# Sysmon

## Bedeutung

Sysmon (System Monitor) ist ein Windows-Systemdienst und Gerätetreiber von Microsoft (Sysinternals), der nach Installation dauerhaft im System verbleibt und detaillierte Prozess-, Datei-, Netzwerk- und Registry-Aktivitäten protokolliert. Im Gegensatz zu den Windows-Standard-Eventlogs ist Sysmon **standardmäßig nicht aktiv** und muss separat installiert (Sysinternals) bzw. aktiviert (ab Windows 11/Server 2025 als optionales Feature) und konfiguriert werden – die Verfügbarkeit von Sysmon-Daten auf einem untersuchten System ist daher nicht garantiert, sondern hängt vom vorherigen Einsatz (i.d.R. durch die betroffene Organisation, z.B. im Rahmen von EDR/Monitoring) ab.

Aus digitalforensischer Sicht liefert Sysmon – sofern vorab installiert und aktiv – eine deutlich granularere Sicht auf Systemaktivität als die Windows-Bordmittel, u.a. mit vollständigen Kommandozeilen, Hash-Werten ausgeführter Dateien und Eltern-Kind-Prozessbeziehungen.

## Spezifische Kurzinformation

1. Sysmon ist Teil der **Sysinternals-Suite** (Microsoft); seit 2026 zusätzlich als optionales Feature in Windows 11/Server 2025 enthalten, standardmäßig deaktiviert
2. Läuft als Systemdienst und Kernel-Treiber; Protokollierungsumfang hängt von der XML-Konfiguration ab und ist je Installation unterschiedlich
3. Events landen in einem eigenen Eventlog-Kanal: `Microsoft-Windows-Sysmon/Operational` (nicht im klassischen Security-Log).
4. Liefert u.a. vollständige Kommandozeilen, Hash-Werte ausgeführter Dateien sowie Eltern-Prozess-Informationen
5. Ablageort:  
   Eventlog: **`%SystemRoot%\System32\Winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx`**  
   Binary: **`%SystemRoot%\Sysmon64.exe`** (Name bei Installation änderbar)  
   Konfiguration: **`HKLM\SYSTEM\CurrentControlSet\Services\SysmonDrv\Parameters`** (Wert `Rules`; Schlüsselname folgt ggf. umbenanntem Treiber)

## Referenzen

2026-09: <https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon>

2026-02: <https://learn.microsoft.com/en-us/windows/security/operating-system-security/sysmon/sysmon-events>

2026-02: <https://learn.microsoft.com/en-us/windows/security/operating-system-security/sysmon/overview>

## Auflistung Event Codes

| Event-ID | Ereignis | Ein Eintrag belegt, dass … |
|---|---|---|
| 1 | Process Create | ein Prozess mit dem angegebenen Image, der Kommandozeile und dem Elternprozess unter dem angegebenen Benutzerkonto gestartet wurde |
| 2 | File creation time changed | ein Prozess den Erstellungszeitstempel einer Datei geändert hat (alter und neuer Wert) |
| 3 | Network connection | ein Prozess eine TCP-/UDP-Verbindung mit den angegebenen Quell- und Zieladressen hatte |
| 4 | Sysmon service state changed | der Sysmon-Dienst gestartet oder gestoppt wurde |
| 5 | Process terminated | ein Prozess beendet wurde |
| 6 | Driver loaded | ein Treiber geladen wurde |
| 7 | Image loaded | ein Prozess ein Modul (z.B. DLL) geladen hat |
| 8 | CreateRemoteThread | ein Prozess einen Thread in einem anderen Prozess erzeugt hat |
| 9 | RawAccessRead | ein Prozess direkt lesend auf ein Laufwerk zugegriffen hat (`\\.\`) |
| 10 | ProcessAccess | ein Prozess ein Handle auf einen anderen Prozess geöffnet hat |
| 11 | FileCreate | eine Datei erstellt oder überschrieben wurde |
| 12 | RegistryEvent (Object create and delete) | ein Registry-Schlüssel oder -Wert erstellt oder gelöscht wurde |
| 13 | RegistryEvent (Value Set) | ein Registry-Wert gesetzt wurde |
| 14 | RegistryEvent (Key and Value Rename) | ein Registry-Schlüssel oder -Wert umbenannt wurde |
| 15 | FileCreateStreamHash | ein Alternate Data Stream erstellt wurde (z.B. Zone.Identifier) |
| 16 | ServiceConfigurationChange | die Sysmon-Konfiguration geändert wurde |
| 17 | PipeEvent (Pipe Created) | eine Named Pipe erstellt wurde |
| 18 | PipeEvent (Pipe Connected) | eine Verbindung zu einer Named Pipe aufgebaut wurde |
| 19 | WmiEvent (WmiEventFilter) | ein WMI-Ereignisfilter registriert wurde |
| 20 | WmiEvent (WmiEventConsumer) | ein WMI-Consumer registriert wurde |
| 21 | WmiEvent (WmiEventConsumerToFilter) | ein WMI-Consumer an einen Filter gebunden wurde |
| 22 | DNSEvent | ein Prozess eine DNS-Abfrage gestellt hat (Name und Ergebnis) |
| 23 | FileDelete | eine Datei gelöscht und eine Kopie archiviert wurde |
| 24 | ClipboardChange | der Inhalt der Zwischenablage geändert wurde |
| 25 | ProcessTampering | das Image eines laufenden Prozesses verändert wurde (z.B. Process Hollowing) |
| 26 | FileDeleteDetected | eine Datei gelöscht wurde (ohne Archivierung) |
| 27 | FileBlockExecutable | das Erstellen einer ausführbaren Datei blockiert wurde |
| 28 | FileBlockShredding | das Überschreiben (Shredding) einer Datei blockiert wurde |
| 29 | FileExecutableDetected | das Erstellen einer ausführbaren Datei erkannt wurde |
| 255 | Error | ein interner Sysmon-Fehler aufgetreten ist |

## Tools

EvtxECmd (Eric Zimmerman) - <https://github.com/EricZimmerman/evtx>

Chainsaw - <https://github.com/WithSecureLabs/chainsaw>

Hayabusa - <https://github.com/Yamato-Security/hayabusa>

DLEAPP (Parser: Sysmon) - <https://github.com/abrignoni/DLEAPP>