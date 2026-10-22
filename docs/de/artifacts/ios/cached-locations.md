---
title: "Cached Locations"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [location]
---

# Cached Locations

## Bedeutung

Das Betriebssystem iOS speichert, soweit möglich und vom Nutzer eingestellt, in kurzen Intervallen den aktuellen Standort des Gerätes. Zwischengespeichert werden die Standorte vom Systemdienst routined.
Je nach Art der genutzten Ortungstechnik ist die Genauigkeit höher oder niedriger. Die Ortung kann zum Beispiel über das Mobilfunknetz, umliegende WLANs oder GPS erfolgen.

Aus digitalforensischer Sicht kann anhand der gespeicherten Cached Locations gesagt werden, dass das Gerät mit der angegebenen Genauigkeit zu dem angegebenen Zeitpunkt an der gespeicherten Koordinate war. Die Genauigkeit wird hierbei in Metern als Radius um die angegebene Koordinate verstanden. Dies bedeutet bei einer Angabe von 25 Metern, dass sich das Gerät nach der Schätzung von iOS in einem Radius von 25 Metern um die gespeicherte Koordinate befunden hat; in einem Test lagen in Einzelfällen (ca. 0,4 % der Einträge) Positionen geringfügig außerhalb des angegebenen Radius.

## Spezifische Kurzinformation

1. Die Daten liegen für die letzten ca. 7 Tage auf dem Gerät vor
2. SQLite-Datenbank, Tabelle `ZRTCLLOCATIONMO`
3. Zeitstempel im Format Mac Absolute Time (Sekunden seit 2001-01-01, UTC)
4. Die Abstände zwischen den Einträgen sind unregelmäßig (Sekunden bis über 20 Minuten); eine Lücke belegt nicht, dass das Gerät aus war oder sich nicht bewegt hat
5. Ablageort:  
   **`/private/var/mobile/Library/Caches/com.apple.routined/Cache.sqlite`**

## Referenzen

2024-08: <https://dfir.pubpub.org/pub/4fkeiv34/release/1>

2023-06: <https://www.doubleblak.com/blogPost.php?k=LocationAccuracy>

2021-09: <https://theforensicscooter.com/2021/09/22/iphone-device-speeds-in-cache-sqlite-zrtcllocationmo/>

2020-07: <https://doubleblak.com/blog/locations>

## Tools

APOLLO (routined_cache_zrtcllocationmo) - <https://github.com/mac4n6/APOLLO>

ArtEx2 (Cached Locations) - <https://www.doubleblak.com/app.php?id=ArtEx2>

iLEAPP (CacheSQLite_Locations) - <https://github.com/abrignoni/iLEAPP>