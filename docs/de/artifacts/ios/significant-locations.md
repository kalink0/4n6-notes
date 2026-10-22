---
title: "Frequent - Significant Locations"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [location]
---

# Frequent - Significant Locations

## Bedeutung

Frequent Locations (deutsch: „Häufige Orte“) ist eine Funktion innerhalb der Ortungsdienste von iOS, die automatisch Orte speichert, an denen sich ein Nutzer wiederholt aufhält. Ziel ist es, personalisierte Dienste wie standortbasierte Erinnerungen oder die Verbesserung von Karten- und Verkehrsprognosen bereitzustellen.

Der Algorithmus, der entscheidet wann ein Ort zu einem "häufigen Ort" wird, ist nicht publik.

Aus digitalforensischer Sicht heißen Einträge zu Frequent Locations, dass ein Gerät an der Frequent Location war. Der Datensatz beinhaltet die Häufigkeit, den Beginn der Aufenthalte und das Ende der Aufenthalte und wie/wie lange man zu dem Ort gereist ist.

Die Genauigkeit bzgl. Zeit und Ort ist bei der Interpretation hierbei mit zu beachten.

## Spezifische Kurzinformation

1. Die Daten werden nach 3-4 Monaten gelöscht, wenn der Ort nicht mehr aufgesucht wird. Spalte ZPLACEEXPIRATIONDATE in Tabelle ZRTLEARNEDLOCATIONOFINTERESTMO speichert, wann Einträge gelöscht werden.
2. Zeitstempel im Format Mac Absolute Time (Sekunden seit 2001-01-01, UTC)
3. Die zeitliche Genauigkeit liegt bei +- 15 Minuten
4. Einträge werden erst nach dem Verlassen des Ortes geschrieben, wenn der Verarbeitungsprozess läuft (in Tests alle 2 bis 4 Tage)
5. Die örtliche Genauigkeit liegt bei bis zu 250 m bzgl. des Verlassens
6. Die Cloud-Datenbank kann Aufenthalte enthalten, die andere Geräte desselben Apple-Accounts erfasst haben (z.B. iPad, Mac)
7. Ablageort:  
   **`/private/var/mobile/Library/Caches/com.apple.routined/Local.sqlite`**  
   **`/private/var/mobile/Library/Caches/com.apple.routined/Cloud.sqlite`**  
   **`/private/var/mobile/Library/Caches/com.apple.routined/Cloud-V2.sqlite`**

## Referenzen

2024-08: <https://dfir.pubpub.org/pub/4fkeiv34/release/1>

2020-07: <https://doubleblak.com/blog/locations>

## Tools

APOLLO (routined_local_*, routined_cloud_*) - <https://github.com/mac4n6/APOLLO>

ArtEx2 (Frequent Locations, Location Transitions) - <https://www.doubleblak.com/app.php?id=ArtEx2>

iLEAPP (appleMapsSignificantLocations, appleMapsSignificantLocationsVisits, appleMapsTrips, routinedCloudVisits) - <https://github.com/abrignoni/iLEAPP>