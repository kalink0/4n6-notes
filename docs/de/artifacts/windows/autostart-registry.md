---
title: "Autostart-Einträge in der Registry"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
topics: [persistence, program-execution]
---

# Autostart-Einträge in der Registry

## Bedeutung

Programme, die unter bestimmten Registry-Schlüsseln eingetragen sind, startet Windows automatisch, wenn sich ein Benutzer anmeldet. Die bekanntesten sind die Schlüssel `Run` und `RunOnce`, jeweils für den einzelnen Benutzer und für alle Benutzer des Systems; Programme unter `RunOnce` werden nur einmal gestartet, der Eintrag wird dabei gelöscht. Einträge legen meist Installationsprogramme an, z. B. für Messenger, Cloud-Speicher oder Updater; sie lassen sich aber auch direkt in der Registry anlegen. Daneben gibt es weitere Autostart-Orte in der Registry, z. B. Werte von Winlogon und Richtlinien-Schlüssel. Wird ein Autostart-Eintrag im Task-Manager oder in den Einstellungen deaktiviert, bleibt er bestehen; Windows speichert den Zustand getrennt davon unter `StartupApproved`.

Aus digitalforensischer Sicht belegt ein Eintrag, dass das Programm mit der angegebenen Befehlszeile bei jeder Anmeldung des Benutzers bzw. bei Einträgen für alle Benutzer bei jeder Anmeldung eines Benutzers gestartet werden soll. Dass ein Eintrag aus `Run` oder `RunOnce` tatsächlich gestartet wurde, zeigt das Ereignisprotokoll Shell-Core: Der Explorer hält dort jeden gestarteten Befehl mit vollständiger Befehlszeile und Zeitpunkt fest. Ein als deaktiviert gekennzeichneter Eintrag unter `StartupApproved` zeigt, dass der Autostart abgeschaltet wurde, und enthält den Zeitpunkt der Deaktivierung.

## Spezifische Kurzinformation

1. Verfügbarkeit: `Run` und `RunOnce` in allen Windows-Versionen; `StartupApproved` seit Windows 8
2. Voraussetzungen: Einträge für alle Benutzer (HKLM) erfordern Administratorrechte, Einträge für den eigenen Benutzer (HKCU) nicht; `RunOnce` unter HKLM wird nur ausgeführt, wenn sich ein Mitglied der Administratoren anmeldet; im abgesicherten Modus werden die Schlüssel ignoriert, außer `RunOnce`-Werte mit `*` vor dem Namen
3. Aufbewahrung: `Run`-Einträge bleiben, bis sie gelöscht werden, z. B. bei der Deinstallation; `RunOnce`-Werte werden vor der Ausführung gelöscht, mit `!` vor dem Namen erst danach; wird ein `Run`-Wert gelöscht, bleibt der zugehörige Wert unter `StartupApproved` erhalten
4. Format und Struktur: ein Registry-Wert pro Programm, Name frei wählbar, Daten = Befehlszeile; unter `StartupApproved` ein Binärwert gleichen Namens mit 12 Byte: die ersten 4 Byte `02` oder `06` = aktiviert, `03` = deaktiviert, die übrigen 8 Byte enthalten bei deaktivierten Einträgen den Zeitpunkt der Deaktivierung
5. Zeitstempel: Die Einträge selbst haben keinen Zeitstempel; der LastWrite-Zeitstempel des Schlüssels (UTC) gibt die letzte Änderung an irgendeinem Wert darunter an; der Deaktivierungszeitpunkt unter `StartupApproved` ist ein FILETIME (UTC)
6. Besonderheiten und Fallstricke: Werte unter `StartupApproved` entstehen nur über Task-Manager, Einstellungen oder Installationsprogramme, nicht beim direkten Anlegen eines `Run`-Werts; ein `Run`-Eintrag ohne zugehörigen Wert gilt als aktiviert; ein Deaktivierungswert kann auch direkt in die Registry geschrieben werden; die Reihenfolge, in der Windows die Programme startet, ist nicht festgelegt, und der Start kann verzögert erfolgen; Einträge von 32-Bit-Programmen auf 64-Bit-Windows liegen unter `WOW6432Node`, ihr Zustand unter `StartupApproved\Run32`; im Protokoll `Microsoft-Windows-Shell-Core/Operational` stehen Beginn und Ende der Abarbeitung eines `Run`- bzw. `RunOnce`-Schlüssels (9705, 9706) sowie Start und Ende jedes Befehls mit Befehlszeile und Prozess-ID (9707, 9708), ohne Angabe, ob der Schlüssel zum Benutzer oder zum System gehört
7. Ablageort:  
   Benutzer (NTUSER.DAT): **`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`**  
   Benutzer (NTUSER.DAT): **`HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce`**  
   Alle Benutzer (SOFTWARE): **`HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`**  
   Alle Benutzer (SOFTWARE): **`HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce`**  
   32-Bit-Programme (SOFTWARE): **`HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run`**  
   Zustand: **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved`**  
   Zustand: **`HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved`**  
   Richtlinien: **`HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run`**  
   Richtlinien: **`HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run`**  
   Winlogon (Werte `Userinit`, `Shell`): **`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`**  
   Ausführung: **`C:\Windows\System32\winevt\Logs\Microsoft-Windows-Shell-Core%4Operational.evtx`**

## Referenzen

2024-07: <https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys>

2022-07: <https://windowsir.blogspot.com/2022/07/startupapprovedrun-pt-ii.html>

2022-07: <https://windowsir.blogspot.com/2022/07/does-autostart-really-mean-autostart.html>

2021-02: <https://nasbench.medium.com/finding-forensic-goodness-in-obscure-windows-event-logs-60e978ea45a3>

2019-02: <https://www.hexacorn.com/blog/2019/02/23/beyond-good-ol-run-key-part-104/>

## Tools

### Kern-Tools

DLEAPP (Parser: Autostart) - <https://github.com/abrignoni/DLEAPP>

Dissect (Plugin: runkeys) - <https://docs.dissect.tools/>

Velociraptor (Artefakt: Windows.Sys.StartupItems) - <https://docs.velociraptor.app/>

### Weitere Tools

Autoruns - <https://learn.microsoft.com/sysinternals/downloads/autoruns>

juntei (parse-registry persistence) - <https://github.com/Yamato-Security/juntei>

PersistenceSniper (Get-RunAndRunOnce) - <https://github.com/last-byte/PersistenceSniper>

Plaso (Parser: windows_run) - <https://github.com/log2timeline/plaso>

regipy (Plugin: software_plugin, ntuser_persistence) - <https://github.com/mkorman90/regipy>

RegRipper (run, rundisabled) - <https://github.com/keydet89/RegRipper4.0>

WhatInStartup - <https://www.nirsoft.net/utils/what_run_in_startup.html>
