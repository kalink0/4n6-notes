---
title: "Geplante Aufgaben"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
topics: [persistence, program-execution]
---

# Geplante Aufgaben

## Bedeutung

Die Aufgabenplanung (Task Scheduler) von Windows startet Programme, Skripte oder Befehle zu festgelegten Zeitpunkten oder bei bestimmten Ereignissen, z. B. bei der Anmeldung, beim Systemstart oder im Leerlauf. Aufgaben legen Windows selbst, installierte Programme (z. B. für Updates), Administratoren und Nutzer an, über die Aufgabenplanung, über `schtasks` oder über die Programmierschnittstelle. Jede Aufgabe ist als XML-Datei gespeichert, die u. a. Autor, Erstellungsdatum, Auslöser, die auszuführenden Aktionen und das Benutzerkonto enthält, unter dem sie läuft. Zusätzlich registriert die Aufgabenplanung jede Aufgabe in der Registry. Aus der Registry lädt der Dienst die Aufgaben tatsächlich; dort hält er auch fest, wann eine Aufgabe registriert und wann sie zuletzt ausgeführt wurde.

Aus digitalforensischer Sicht belegt eine Aufgabe, dass das genannte Programm bzw. der Befehl unter den angegebenen Bedingungen automatisch gestartet werden soll, mit den Rechten des angegebenen Kontos. Der Zeitpunkt der letzten Ausführung in der Registry belegt, dass die Aktion der Aufgabe zu diesem Zeitpunkt gestartet wurde. Gibt es eine Aufgabe nur in der Registry, aber nicht als XML-Datei, oder weichen beide voneinander ab, wurde die Aufgabe außerhalb der Aufgabenplanung verändert oder versteckt.

## Spezifische Kurzinformation

1. Verfügbarkeit: XML-Format seit Windows Vista; bis Windows XP Binärdateien im Format `.job`, die auch später noch vorkommen, z. B. für mit `at.exe` angelegte Aufgaben
2. Voraussetzungen: Die Aufgabenplanung ist standardmäßig aktiv; der Verlauf (Protokoll `Microsoft-Windows-TaskScheduler/Operational`) ist unter Windows 10 und 11 standardmäßig deaktiviert; die Security-Ereignisse 4698 (erstellt), 4699 (gelöscht), 4700 (aktiviert), 4701 (deaktiviert) und 4702 (geändert) entstehen nur mit der Überwachungsrichtlinie „Andere Objektzugriffsereignisse überwachen“
3. Aufbewahrung: Beim Löschen über die Aufgabenplanung werden XML-Datei und Registry-Einträge entfernt; wird nur die XML-Datei gelöscht, bleibt die Aufgabe registriert und wird weiter ausgeführt
4. Format und Struktur: XML in UTF-16 ohne Dateiendung, die Unterordner entsprechen den Ordnern in der Aufgabenplanung; in der Registry pro Aufgabe ein Schlüssel unter `Tree` mit Kennung und Sicherheitsbeschreibung (`SD`) und ein Schlüssel unter `Tasks\{GUID}` mit Pfad, Aktionen, Auslösern und Laufzeitinformationen als undokumentierte Binärdaten
5. Zeitstempel: Das Erstellungsdatum in der XML-Datei setzt das erstellende Programm, es kann frei gewählt sein und steht häufig in Ortszeit ohne Zeitzone; in der Registry (`DynamicInfo`) als FILETIME (UTC) Zeitpunkt der Registrierung und der letzten Ausführung, in neueren Windows-Versionen auch der letzten erfolgreichen Ausführung
6. Besonderheiten und Fallstricke: Fehlt der Wert `SD` einer Aufgabe oder ist er ungültig, zeigen Aufgabenplanung und `schtasks` die Aufgabe nicht an, sie wird aber weiter ausgeführt (bekannt seit 2022 durch die Schadsoftware Tarrask); das Entfernen erfordert SYSTEM-Rechte; direkt in die Registry geschriebene Aufgaben erzeugen keine Ereignisse zur Erstellung; Ereignis-IDs im Verlauf: 106 (registriert), 140 (geändert), 141 (gelöscht), 100 (Aufgabe gestartet), 200 (Aktion gestartet), 201 (Aktion beendet)
7. Ablageort:  
   XML: **`C:\Windows\System32\Tasks`**  
   Registry: **`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache`**  
   `.job`: **`C:\Windows\Tasks`**  
   Verlauf: **`C:\Windows\System32\winevt\Logs\Microsoft-Windows-TaskScheduler%4Operational.evtx`**

## Referenzen

2026-05: <https://forenza.io/persistence-task-cache/>

2024-02: <https://www.cybertriage.com/blog/windows-scheduled-tasks-for-dfir-investigations/>

2022-04: <https://www.microsoft.com/en-us/security/blog/2022/04/12/tarrask-malware-uses-scheduled-tasks-for-defense-evasion/>

## Tools

### Kern-Tools

DLEAPP (Parser: Scheduled Tasks) - <https://github.com/abrignoni/DLEAPP>

Dissect (Plugin: tasks) - <https://docs.dissect.tools/>

Velociraptor (Artefakte: Windows.System.TaskScheduler, Windows.Registry.TaskCache, Windows.EventLogs.ScheduledTasks) - <https://docs.velociraptor.app/>

EvtxECmd - <https://ericzimmerman.github.io/>

Registry Explorer (Plugin: TaskCache) - <https://ericzimmerman.github.io/>

### Weitere Tools

Autoruns - <https://learn.microsoft.com/sysinternals/downloads/autoruns>

juntei (parse-registry taskcache, persistence-hunter) - <https://github.com/Yamato-Security/juntei>

PersistenceSniper (Get-ScheduledTasks) - <https://github.com/last-byte/PersistenceSniper>

Plaso (Parser: winjob, windows_task_cache) - <https://github.com/log2timeline/plaso>

RegRipper (tasks, hiddentasks) - <https://github.com/keydet89/RegRipper4.0>

TaskSchedulerView - <https://www.nirsoft.net/utils/task_scheduler_view.html>

Windows-Scheduled-Task-Parser - <https://github.com/gajos112/Windows-Scheduled-Task-Parser>
