---
title: "Autostart-Ordner"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
topics: [persistence]
---

# Autostart-Ordner

## Bedeutung

Der Autostart-Ordner ist ein Ordner im Startmenü, dessen Inhalt der Windows Explorer bei der Anmeldung eines Benutzers automatisch startet. Es gibt einen Ordner pro Benutzer und einen für alle Benutzer des Systems. Meist liegen dort Verknüpfungen (LNK-Dateien) auf Programme, die Installationsprogramme oder der Nutzer angelegt haben; andere Dateien werden mit dem Programm geöffnet, das ihrem Dateityp zugeordnet ist, ausführbare Dateien und Skripte (z. B. `.exe`, `.bat`, `.vbs`) also ausgeführt. Wird ein Eintrag im Task-Manager oder in den Einstellungen deaktiviert, bleibt die Datei im Ordner; Windows speichert den Zustand getrennt davon in der Registry unter `StartupApproved`.

Aus digitalforensischer Sicht belegt eine Datei im Autostart-Ordner, dass sie bei jeder Anmeldung des Benutzers bzw. beim Ordner für alle Benutzer bei jeder Anmeldung eines Benutzers gestartet werden soll. Die Zeitstempel der Datei zeigen, wann sie im Ordner angelegt und zuletzt geändert wurde; eine Verknüpfung enthält zusätzlich den Pfad und Metadaten ihres Ziels. Ein als deaktiviert gekennzeichneter Wert unter `StartupApproved` zeigt, dass der Autostart abgeschaltet wurde, und enthält den Zeitpunkt der Deaktivierung.

## Spezifische Kurzinformation

1. Verfügbarkeit: in allen Windows-Versionen; `StartupApproved\StartupFolder` seit Windows 8
2. Voraussetzungen: Dateien im Ordner für alle Benutzer erfordern Administratorrechte, im eigenen Ordner nicht
3. Aufbewahrung: Die Datei bleibt, bis sie gelöscht wird; ein Wert unter `StartupApproved\StartupFolder` entsteht erst, wenn der Eintrag im Task-Manager oder in den Einstellungen umgeschaltet wird; eine Datei ohne zugehörigen Wert gilt als aktiviert
4. Format und Struktur: beliebige Dateien, meist LNK; der Explorer zeigt den Ordner als „Autostart“ an, auf dem Datenträger heißt er seit Windows Vista `Startup` bzw. `StartUp`; unter `StartupApproved\StartupFolder` ein Binärwert mit dem Dateinamen als Namen und 12 Byte: die ersten 4 Byte `02` oder `06` = aktiviert, `03` = deaktiviert, die übrigen 8 Byte enthalten bei deaktivierten Einträgen den Zeitpunkt der Deaktivierung
5. Zeitstempel: Zeitstempel der Datei im Dateisystem; bei LNK-Dateien zusätzlich die darin gespeicherten Zeitstempel des Ziels; der Deaktivierungszeitpunkt unter `StartupApproved` ist ein FILETIME (UTC)
6. Besonderheiten und Fallstricke: Die Lage der Ordner lässt sich über die Werte `Startup` und `Common Startup` unter `User Shell Folders` umleiten; Windows startet dann die Dateien im neuen Ordner, der Standardordner bleibt leer; wird eine Datei innerhalb desselben Laufwerks in den Ordner verschoben, behält sie ihre ursprüngliche Erstellungszeit; die Reihenfolge, in der Windows die Dateien startet, ist nicht festgelegt, und der Start kann verzögert erfolgen
7. Ablageort:  
   Benutzer: **`%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`**  
   Alle Benutzer: **`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`**  
   Bis Windows XP (deutsch): **`C:\Dokumente und Einstellungen\{USER}\Startmenü\Programme\Autostart`**  
   Zustand: **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\StartupFolder`**  
   Zustand: **`HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\StartupFolder`**  
   Umleitung (Wert `Startup`): **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders`**  
   Umleitung (Wert `Common Startup`): **`HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders`**

## Referenzen

2026-11: <https://attack.mitre.org/techniques/T1547/001/>

2022-07: <https://windowsir.blogspot.com/2022/07/does-autostart-really-mean-autostart.html>

## Tools

Autoruns - <https://learn.microsoft.com/sysinternals/downloads/autoruns>

RegRipper (rundisabled) - <https://github.com/keydet89/RegRipper4.0>

LECmd - <https://ericzimmerman.github.io/>

DLEAPP (Parser: Startup Folder Items, Startup Approved States) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (Artefakte: Windows.Sys.StartupItems) - <https://docs.velociraptor.app/>

WhatInStartup - <https://www.nirsoft.net/utils/what_run_in_startup.html>

juntei (persistence-hunter) - <https://github.com/Yamato-Security/juntei>

PersistenceSniper (Get-StartupPrograms) - <https://github.com/last-byte/PersistenceSniper>
