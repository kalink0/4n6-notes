---
title: "Battery Stats Daily"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [device-state]
---

# Battery Stats Daily

## Bedeutung

Android führt tägliche Statistiken über den Lade- und Entladeverlauf des Akkus. Je Tageseintrag (Beginn und Ende) werden die einzelnen Lade- bzw. Entladeschritte gespeichert, jeweils mit Akkustand, Dauer des Schritts und dem Gerätezustand: Bildschirmstatus (an, aus, Doze) sowie Energiesparmodus und Geräte-Leerlauf (Idle), jeweils zu Beginn des Schritts und ob sich der Zustand während des Schritts geändert hat.

Aus digitalforensischer Sicht belegt ein Eintrag, dass der Akku im angegebenen Tageszeitraum in Schritten mit der jeweiligen Dauer geladen bzw. entladen wurde und welcher Bildschirm- und Energiezustand dabei vorlag.

Nicht belegt ist, zu welchem genauen Zeitpunkt ein einzelner Schritt stattfand.

## Spezifische Kurzinformation

1. Bis Android 13 XML, ab Android 14 ABX
2. Zeitangaben der einzelnen Schritte sind Dauern in Millisekunden, keine Zeitpunkte; nur Beginn und Ende des Tageseintrags sind Unix-Zeitstempel in Millisekunden (UTC)
3. Ablageort:  
   **`/data/system/batterystats-daily.xml`**

## Referenzen

2024-01: <https://blog.digital-forensics.it/2024/01/a-first-look-at-android-14-forensics.html>

## Tools

ALEAPP (Android Battery Stats Daily) - <https://github.com/abrignoni/ALEAPP>