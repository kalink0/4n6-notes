---
title: "Superfetch"
status: complete
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
topics: [program-execution]
---

# Superfetch

## Bedeutung

Superfetch ist eine Erweiterung von Prefetch, die mit Windows Vista eingeführt wurde. Während Prefetch den Start einzelner Programme beschleunigt, wertet Superfetch das Nutzungsverhalten über längere Zeit aus und lädt Daten vorab in den Arbeitsspeicher, die voraussichtlich benötigt werden. Seit Windows 10 laufen Prefetch und Superfetch gemeinsam im Dienst SysMain. Die Ergebnisse speichert der Dienst in eigenen Datenbankdateien.

Aus digitalforensischer Sicht belegen Einträge, dass Programme und Dateien auf dem System genutzt wurden, auch solche, die inzwischen deinstalliert sind. Nicht belegt sind genaue Ausführungszeitpunkte.

## Spezifische Kurzinformation

1. Seit Windows Vista; seit Windows 10 Teil des Dienstes SysMain
2. Auf Systemen mit SSD teils deaktiviert
3. Erfasst die Nutzung aller Benutzer des Systems, neben Programmen auch Pfade von Libraries und Konfigurationsdateien
4. Die meisten Datenbanken werden erst beim Beenden des Dienstes geschrieben, AgAppLaunch.db beim Start
5. Auf neueren Systemen komprimiert (Dateiendung .db.trx), nicht direkt lesbar
6. Format nur teilweise dokumentiert
7. Ablageort:  
   **`C:\Windows\Prefetch\Ag*.db`**  
   **`C:\Windows\Prefetch\Ag*.db.trx`**

## Referenzen

2026-07: <https://www.it-connect.tech/forensic-windows-part-4-exploiting-superfetch-artifacts/>

2020-08: <https://i.blackhat.com/USA-20/Thursday/us-20-Venault-Fooling-Windows-Through-Superfetch.pdf>

2015-06: <https://blog.digital-forensics.it/2015/06/a-first-look-at-windows-10-prefetch.html>

2026-10 (abgerufen): <https://forensics.wiki/superfetch/>

## Tools

SysMainView - <https://github.com/MathildeVenault/SysMainView>

rewolf-superfetch-dumper - <https://github.com/rwfpl/rewolf-superfetch-dumper>

libagdb - <https://github.com/libyal/libagdb>