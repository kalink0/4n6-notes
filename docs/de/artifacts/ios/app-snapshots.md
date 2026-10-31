---
title: "App Snapshots"
status: complete
completed: 2026-10-25
authors: [kalink0 (Marco Neumann)]
topics: [program-execution]
---

# App Snapshots

## Bedeutung

iOS erstellt App Snapshots, wenn eine App in den Hintergrund wechselt. Sie halten den angezeigten Bildschirmzustand fest und dienen unter anderem als Vorschau im App-Umschalter.

Aus digitalforensischer Sicht zeigen die Snapshots den letzten auf dem Bildschirm angezeigten Inhalt der App bevor diese vom Nutzer oder System zuletzt in den Hintergrund geschoben wurde.

## Spezifische Kurzinformation

1. Zuerst unter iOS 10 festgestellt
2. Snapshot-Metadaten liegen in `applicationState.db` unter dem Schlüssel `XBApplicationSnapshotManifest` (key=2, Tabelle=kvs) vor. Die zugehörigen Informationen sind in bplists gespeichert. Die Snapshot-Bilder liegen im KTX-Format oder bei aktuellen iOS-Version als PNG vor
3. Das `creationDate` entspricht der Erstellung der Datei. Die genaue Bedeutung vom `lastUsedDate` ist nicht abschließend geklärt
4. Die Inhalte können ausgeblendet sein wenn die App vom App-Entwickler und/oder Nutzer als sensibel deklariert wurden - der Snapshot ist dann schwarz
5. Ablageorte:  
   **`/private/var/mobile/Library/FrontBoard/applicationState.db`**  
   **`/private/var/mobile/Library/SplashBoard/Snapshots/`**  
   **`/private/var/mobile/Containers/Data/Application/{UUID}/Library/SplashBoard/Snapshots`**  
   **`/private/var/mobile/Containers/Data/Application/{UUID}/Library/Caches/Snapshots/`**

## Referenzen

2026-08: <https://leapps.org/blog-post?post=2026-08-10-ios-app-snapshots-seven-years-later>

2025-05: <https://www.magnetforensics.com/blog/that-one-artifact-snapshot-to-justice/>

2019-09: <https://abrignoni.blogspot.com/2019/09/ios-snapshots-triage-parser-working.html>

2019-09: <https://gforce4n6.blogspot.com/2019/09/a-quick-look-into-ios-snapshots.html>

## Tools

iLEAPP (App Snapshots) - <https://github.com/abrignoni/iLEAPP>