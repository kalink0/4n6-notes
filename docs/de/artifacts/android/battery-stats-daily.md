---
title: "Battery Stats Daily"
status: complete
completed: 2026-10-24
authors: [kalink0 (Marco Neumann)]
topics: [device-state]
---

# Battery Stats Daily

## Bedeutung

Android führt tägliche Statistiken über den Lade- und Entladeverlauf des Akkus, aufgeteilt in einzelne Lade- bzw. Entladeschritte je Tageseintrag. Zusätzlich werden je Tageseintrag Paketänderungen mit Paketname und Versionsnummer festgehalten.

Aus digitalforensischer Sicht belegt ein Eintrag, dass der Akku im angegebenen Tageszeitraum in Schritten mit der jeweiligen Dauer geladen bzw. entladen wurde, welcher Akkustand dabei erreicht wurde und welcher Bildschirmstatus (an, aus, Doze, Doze Suspend) sowie welcher Energiespar- und Leerlaufzustand (Idle) zu Beginn des Schritts vorlag. Für Energiesparmodus und Idle ist zusätzlich belegt, ob sie sich während des Schritts geändert haben. Ein Paketeintrag belegt, dass es im Tageszeitraum eine Änderung an diesem Paket gab.

Nicht belegt ist, zu welchem genauen Zeitpunkt ein einzelner Schritt oder eine Paketänderung stattfand.

## Spezifische Kurzinformation

1. XML oder ABX; in den geprüften Images bis Android 13 XML, ab Android 14 ABX
2. Enthält etwa die letzten 10 Tage
3. Schritte sind in umgekehrter Reihenfolge gespeichert, der neueste zuerst
4. Schritt als `Zustand-Akkustand-Dauer`, Akkustand und Dauer hexadezimal (z.B. `oZI-35-c2957` = 53 %, 796 503 ms)
5. Zeitangaben der einzelnen Schritte sind Dauer in Millisekunden, keine Zeitpunkte; nur Beginn und Ende des Tageseintrags sind Unix-Zeitstempel in Millisekunden (UTC)
6. Ablageort:  
   **`/data/system/batterystats-daily.xml`**

## Referenzen

2026-10: <https://bebinary4n6.blogspot.com/2026/10/ten-days-of-android-battery-history-and.html>  
2024-01: <https://blog.digital-forensics.it/2024/01/a-first-look-at-android-14-forensics.html>

## Tools

ALEAPP (Android Battery Stats Daily) - <https://github.com/abrignoni/ALEAPP>