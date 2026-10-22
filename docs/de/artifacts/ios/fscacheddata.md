---
title: "FSCachedData"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [web-activity]
---

# FSCachedData

## Bedeutung

Apps, die Netzwerkanfragen über die Standardschnittstellen von iOS stellen, legen die Antworten der Server in einem Cache ab. Die Metadaten der Anfragen und ein Teil der Antworten stehen in einer Datenbank, weitere Antworten speichert iOS als einzelne Dateien im Ordner fsCachedData. Je nach App sind das z.B. JSON-Daten mit Chatnachrichten, Bilder oder andere Medien.

Aus digitalforensischer Sicht belegt eine Datei in fsCachedData, dass die zugehörige App diesen Inhalt von einem Server abgerufen hat. Nicht belegt ist dagegen, dass der Inhalt dem Nutzer angezeigt wurde.

## Spezifische Kurzinformation

1. Ordner pro App im Cache-Verzeichnis; Entwickler können ihn auch an anderer Stelle im App-Container anlegen
2. Dateinamen sind UUID-ähnlich; der Dateityp ist nur am Inhalt erkennbar
3. Ob eine Antwort in fsCachedData liegt, zeigt in der Cache.db die Spalte `isDataOnFS` der Tabelle `cfurl_cache_response`
4. Ablageort:  
   **`/private/var/mobile/Containers/Data/Application/{UUID}/Library/Caches/{BUNDLE_ID}/fsCachedData/`**

## Referenzen

2026-10: <https://stinger.io/mobile/ios/Dynamic-Analysis/iOS-HTTP-Caching/> (abgerufen)

2018-08: <https://abrignoni.blogspot.com/2018/08/finding-discord-chats-in-ios.html>

## Tools

iLEAPP (fsCachedData) - <https://github.com/abrignoni/iLEAPP>