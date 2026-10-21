---
title: "Usagestats"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [program-execution, device-state]
---

# Usagestats

## Bedeutung

Der Systemdienst UsageStats protokolliert die Nutzung von Apps und bestimmte Geräteereignisse. Android stellt die Daten Apps mit der Berechtigung zum Nutzungszugriff bereit, etwa für Bildschirmzeit-Auswertungen.

Aus digitalforensischer Sicht belegt ein Ereigniseintrag, dass zum angegebenen Zeitpunkt eine Activity der App in den Vordergrund gewechselt ist (ACTIVITY_RESUMED) bzw. ihn verlassen hat (ACTIVITY_PAUSED, ACTIVITY_STOPPED). Zusätzlich werden Geräteereignisse erfasst, z. B. Bildschirm aktiv/inaktiv (SCREEN_INTERACTIVE/SCREEN_NON_INTERACTIVE), Sperrbildschirm angezeigt/aufgehoben (KEYGUARD_SHOWN/KEYGUARD_HIDDEN) sowie Herunterfahren und Start des Geräts. Die zusammengefassten Werte je Intervall belegen pro App den letzten Nutzungszeitpunkt und die Gesamtdauer im Vordergrund.

Nicht belegt ist, dass eine Person die App aktiv bedient hat oder auf welche Weise der Sperrbildschirm aufgehoben wurde.

## Spezifische Kurzinformation

1. Bis Android 9 XML, ab Android 10 Protobuf
2. Ab Android 11 sind Paket- und Klassennamen durch Token ersetzt, die nur über die Datei `mappings` im selben Ordner aufgelöst werden können
3. Daten liegen je Nutzer in den Unterordnern `daily`, `weekly`, `monthly` und `yearly`; dieselben Einträge können in mehreren Intervallordnern vorkommen
4. Zeitstempel: Unix-Zeit in Millisekunden (UTC), gespeichert als Versatz zum Dateinamen (Beginn des Intervalls); negative Werte sind absolute Zeitstempel
5. Ablageort:  
   bis Android 10: **`/data/system/usagestats/{USER_ID}/`**  
   ab Android 11: **`/data/system_ce/{USER_ID}/usagestats/`**

## Referenzen

2026-08: <https://leapps.org/blog-post?post=2026-08-03-android-usagestats-recent-tasks>  
2026-04: <https://andreafortuna.org/2026/04/23/android-pattern-of-life-hidden-artifacts-reconstruct-daily-routine/>  
2025-11: <https://forensafe.com/blogs/android-app-usage-history.html>  
2021-04: <https://www.sans.org/white-papers/40265>  
2020-01: <https://www.swiftforensics.com/2020/01/usagestats-on-android-10-q.html>  
2019-02: <https://abrignoni.blogspot.com/2019/02/android-usagestats-xml-parser.html>

## Tools

ALEAPP (Usage Stats) - <https://github.com/abrignoni/ALEAPP>