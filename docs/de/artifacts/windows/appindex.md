---
title: "Windows AppIndex"
status: reviewed
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
reviewers: [dugeonlady]
reviewed: 2026-10-25
topics: [program-execution, installed-software]
---

# Windows AppIndex

## Bedeutung

AppsIndex.db ist eine SQLite-Datenbank des "Windows Feature Experience Pack" unter Windows 11, die installierte bzw. im Startmenü vorhandene Anwendungen für die Startmenü-Suche indiziert. Erfasst werden nur Anwendungen, die entweder über die Installation (Verknüpfung im Startmenü-Ordner) oder manuell durch "An Start anheften" im Startmenü vertreten sind – nicht alle auf dem System vorhandenen ausführbaren Dateien.

Aus digitalforensischer Sicht bedeutet ein Eintrag mit einem Ausführungszähler ("Launch Count") größer 0, dass die betreffende Anwendung unter diesem Benutzerkonto ausgeführt wurde. Eine Aussage zum genauen Zeitpunkt der (letzten) Ausführung kann anhand dieses Artefakts nicht getroffen werden, da keine Zeitstempel gespeichert werden.

## Spezifische Kurzinformation

1. Voraussetzungen: Deaktivierbar über "Start- und Suchergebnisse verbessern" - RegKey: HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced - Start_TrackProgs = 0
2. Aufbewahrung: Begrenzte Historie: Datensatz wird bei Entpinnen/Deinstallation zeitnah entfernt - Zeitpunkt der Löschung nicht deterministisch
3. Format und Struktur: Relevante Tabellen: tiles und tiles_content – enthalten Anwendungspfad, Anzeigename und Ausführungszähler (launchCount)
4. Besonderheiten und Fallstricke: Nur im Startmenü verknüpfte Apps werden pro User getrackt -
5. Ablageort:  
   **`%LOCALAPPDATA%\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\LocalState\Search\AppsIndex.db`**

## Referenzen

2025-09: <https://detect.fyi/introducing-appsindex-db-new-windows-11-artifact-for-tracking-start-menu-application-execution-b294c8e764fa>

## Tools

*Noch kein Inhalt.*