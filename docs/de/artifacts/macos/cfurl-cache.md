---
title: "CFURL Cache"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [web-activity]
---

# CFURL Cache

## Bedeutung

Programme, die Daten über die Standard-Netzwerkschnittstellen von macOS abrufen, legen die Antworten der Server in einem Cache ab. So können wiederholte Anfragen schneller und ohne erneute Übertragung beantwortet werden. Jedes Programm hat eine eigene Datenbank (Cache.db) mit der abgerufenen URL, dem Zeitpunkt sowie den gespeicherten Anfragen und Antworten; größere Antworten liegen als einzelne Dateien im Ordner fsCachedData.

Aus digitalforensischer Sicht belegt ein Eintrag, dass das Programm die URL zum gespeicherten Zeitpunkt abgerufen hat. Nicht belegt ist, dass der Abruf vom Benutzer ausgelöst oder der Inhalt dem Benutzer angezeigt wurde.

## Spezifische Kurzinformation

1. Das abrufende Programm ergibt sich aus dem Ordnernamen (Bundle-ID) des Caches
2. Ob eine Antwort als Datei in fsCachedData liegt, zeigt in der Cache.db die Spalte `isDataOnFS` der Tabelle `cfurl_cache_response`
3. Gespeicherte Anfragen und Antworten können Header mit Sitzungs-Cookies und Tokens enthalten
4. Zeitstempel der Datenbank in UTC; der Zeitstempel im gespeicherten Antwortobjekt weicht davon teils ab
5. Die Cache-Größe ist begrenzt; Programme können Einträge selbst löschen oder einen anderen Ablageort festlegen
6. Ablageort:

   **`/Users/{USER}/Library/Caches/{BUNDLE_ID}/Cache.db`**

   **`/Users/{USER}/Library/Caches/{BUNDLE_ID}/fsCachedData/`**

   Programme mit Sandbox: **`/Users/{USER}/Library/Containers/{BUNDLE_ID}/Data/Library/Caches/{BUNDLE_ID}/`**

## Referenzen

2026-10: <https://developer.apple.com/documentation/foundation/urlcache> (abgerufen)

2026-10: <https://stinger.io/mobile/ios/Dynamic-Analysis/iOS-HTTP-Caching/> (abgerufen)

2022-12: <https://trustedsec.com/blog/looting-ios-apps-cache-db>

2008-10: <https://dreness.com/blog/archives/73>

## Tools

DLEAPP (Parser: App URL Cache) - <https://github.com/abrignoni/DLEAPP>

mac_apt (Plugin: CFURLCACHE) - <https://github.com/ydkhatri/mac_apt>

Velociraptor (Artefakt: MacOS.Applications.Cache) - <https://docs.velociraptor.app/exchange/artifacts/pages/macos.applications.cache>