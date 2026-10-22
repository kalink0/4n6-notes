---
title: "MRU - OpenSavePidlMRU"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [file-access]
---

# MRU - OpenSavePidlMRU

## Bedeutung

Das Betriebssystem Windows legt mehrere sogenannte MRU (Most Recently Used) Listen ab. Diese speichern pro Benutzerkonto im Allgemeinen zuletzt aufgerufene oder gespeicherte Dateien, zuletzt ausgeführte Befehle, zuletzt aufgerufene Ordner.

Der Zweck der MRU Listen ist es, den Benutzern ein angenehmeres Bediengefühl zu liefern, indem zum Beispiel dem Nutzer seine zuletzt geöffneten Dateien angeboten werden.

Aus digitalforensischer Sicht bedeuten Einträge in der Open/Save-MRU, dass das Nutzerkonto mittels der Microsoft-Dialog-Box (Öffnen/Speichern), den Ordner/die Datei geöffnet/gespeichert hat. Die Reihenfolge in der MRU-Liste entspricht hierbei der Reihenfolge des jeweils letzten Öffnens/Speicherns.

## Spezifische Kurzinformation

1. Pro Dateiendung liegt eine MRU vor, zusätzlich enthält der Unterschlüssel `*` die zuletzt geöffneten/gespeicherten Dateien aller Endungen
2. Reihenfolge über `MRUListEx` (Windows XP: `MRUList`); die letzte Schreibzeit eines Unterschlüssels gehört nur zum jeweils neuesten Eintrag
3. Diese MRU korreliert mit der MRU - LastVisitedPidlMRU - ein neuer Eintrag dort ist auch ein neuer Eintrag in dieser MRU
4. Ablageorte:  
   ab Windows Vista: **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU`**  
   Windows XP: **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU`**

## Referenzen

2024-04: <https://www.dr-datenschutz.de/it-forensische-informationen-durch-dateioeffnungen-gewinnen/>

2022-09: <https://www.magnetforensics.com/blog/what-is-mru-most-recently-used/>

2010-04: <https://www.sans.org/blog/opensavemru-and-lastvisitedmru/>

## Tools

DLEAPP (windowsUserMru) - <https://github.com/abrignoni/DLEAPP>

Registry Explorer (ComDlg32 Bookmark) - <https://ericzimmerman.github.io/>

RegRipper (comdlg32) - <https://github.com/keydet89/RegRipper4.0>