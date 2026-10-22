---
title: "MRU - RecentDocs"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [file-access]
---

# MRU - RecentDocs

## Bedeutung

Das Betriebssystem Windows legt mehrere sogenannte MRU (Most Recently Used) Listen ab. Diese speichern pro Benutzerkonto im Allgemeinen zuletzt aufgerufene oder gespeicherte Dateien, zuletzt ausgeführte Befehle, zuletzt aufgerufene Ordner.

Der Zweck der MRU Listen ist es, den Benutzern ein angenehmeres Bediengefühl zu liefern, indem zum Beispiel dem Nutzer seine zuletzt geöffneten Dateien angeboten werden.

Aus digitalforensischer Sicht bedeuten Einträge in der RecentDocs MRU Liste, dass das Nutzerkonto die aufgeführten Dateien/Ordner in der Reihenfolge des jeweils letzten Zugriffs mittels des Windows Explorers oder einer Anwendung, die die Datei bei der Windows-Shell als zuletzt verwendet meldet, zuletzt geöffnet, gespeichert oder erstellt hat. Zu dem vollständigen Dateipfad der Datei/des Ordners kann nicht zwingend eine Aussage getroffen werden.

## Spezifische Kurzinformation

1. Unterschlüssel pro Dateiendung und Folder mit jeweils eigener MRUListEx; Dateien stehen meist im Hauptschlüssel und im Unterschlüssel ihrer Endung
2. Der Zeitstempel zur letzten Änderung der MRUListEx kann auf die Öffnung der Most Recent Datei hindeuten. Jedoch wird dieser Zeitstempel auch von anderen Aktionen geändert (z.B. Löschen eines Eintrags aus der jeweiligen MRU). Somit lässt sich anhand dieses Artefakts alleine nur sehr bedingt eine Aussage zu dem genauen Zeitstempel treffen. Verlässlicher ist die letzte Schreibzeit der Unterschlüssel pro Dateiendung bzw. Folder; sie gehört zum dort neuesten Eintrag.
3. Dateien mit identischen Namen, aber unterschiedlichen Pfaden werden nur einen Eintrag in der MRU-Liste erzeugen.
4. Beim Erstellen oder Öffnen einer Datei werden auch der übergeordnete Ordner und ggf. dessen übergeordneter Ordner eingetragen; ein Ordner-Eintrag belegt daher nicht, dass der Ordner geöffnet wurde
5. Ablageorte:  
   **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`**

## Referenzen

2022-09: <https://www.magnetforensics.com/blog/what-is-mru-most-recently-used/>

2019-03: <https://forensic4cast.com/2019/03/the-recentdocs-key-in-windows-10/>

## Tools

DLEAPP (windowsRecentDocs) - <https://github.com/abrignoni/DLEAPP>

Registry Explorer (RecentDocs Bookmark) - <https://ericzimmerman.github.io/>

RegRipper (recentdocs) - <https://github.com/keydet89/RegRipper4.0>