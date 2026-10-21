---
title: "Windows Search Index"
status: complete
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
topics: [file-existence]
---

# Windows Search Index

## Bedeutung

Der Windows Search Index ist ein Index der vom Windows Search Dienst gefüllt wird. Es sollen hierbei die Dateien in den indizierten Orten (standardmäßig das Benutzerprofil und das Startmenü) indiziert werden um dem Nutzer eine einfache und schnelle Suche im System zu ermöglichen. Neben Dateien und Ordnern werden auch weitere Daten indiziert, wie z.B. Outlook E-Mail Daten.

Aus digitalforensischer Sicht bedeuten Einträge zu Dateien und Ordner im Windows Search Index, dass diese zu dem Zeitpunkt der letzten Änderung zu dieser Datei in dem Index auf dem System unter dem angegebenen Pfad und dem Dateinamen vorgelegen haben müssen.

## Spezifische Kurzinformation

1. Daten liegen bis Windows 10 in ESE-Datenbank, ab Windows 11 in 2 Sqlite-Datenbanken
2. Standardmäßig indiziert: Benutzerprofil (ohne AppData) und Startmenü; auf Windows Server standardmäßig nicht aktiv
3. Enthält auch Daten zu anderen Artefakten (z.B. Windows Timeline).
4. Enthält auch Auszüge aus Dateiinhalten sowie den Browserverlauf von Internet Explorer und Edge
5. Gelöschte Einträge können in der Datenbank verbleiben
6. Ablageort:  
   Windows XP: **`C:\Documents and Settings\All Users\Application Data\Microsoft\Search\Data\Applications\Windows\Windows.edb`**  
   Windows Vista - Windows 10: **`C:\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.edb`**  
   Ab Windows 11: **`C:\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.db*`**  
   Ab Windows 11: **`C:\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows-gather.db*`**

## Referenzen

2023-04: <https://levelblue.com/blogs/strozfriedberg/windows-search-index-the-forensic-artifact-youve-been-searching-for>

2020-05: <https://www.forensicfocus.com/articles/windows-search-forensics/>

## Tools

Search Index DB Reporter - <https://github.com/strozfriedberg/sidr>

DLEAPP (Parser: Windows Search Index, Windows 11 Search Index) - <https://github.com/abrignoni/DLEAPP>

WinSearchDBAnalyzer (bis Windows 10) - <https://github.com/moaistory/WinSearchDBAnalyzer>

ESEDatabaseView (bis Windows 10) - <https://www.nirsoft.net/utils/ese_database_view.html>

DB Browser for SQLite (ab Windows 11) - <https://sqlitebrowser.org/>