---
title: "Samsung Secure Folder HistoryLog"
status: complete
completed: 2026-10-24
authors: [kalink0 (Marco Neumann)]
topics: [file-existence, data-transfer]
---

# Samsung Secure Folder HistoryLog

## Bedeutung

Das Samsung Secure Folder HistoryLog protokolliert Verschiebeaktionen von Dateien und Ordnern zwischen einem Android-Benutzerprofil und einem Secure Folder. Die Einträge enthalten die Quell- und Ziel-UID, die Anzahl der Dateien und die neuen Speicherorte.

Aus digitalforensischer Sicht belegen die Einträge, dass eine Verschiebeaktion mit den jeweils protokollierten Werten stattgefunden hat.

## Spezifische Kurzinformation

1. `request` dokumentiert die Anforderung, `result` die Rückmeldung. Eine eindeutige Zuordnung über eine gemeinsame ID ist nicht möglich.
2. Einzelne Dateinamen werden nicht gespeichert.
3. Zeitstempel: als String gespeichert, Zeitzone unbekannt.

Ablageort:

**`/data/data/com.samsung.knox.securefolder/databases/history_log_database`**

## Referenzen

2026-06: <https://github.com/4n6Wizard/Samsung-HistoryLog-Parser>

## Tools

ALEAPP (Samsung Secure Folder - History Log) - <https://github.com/abrignoni/ALEAPP>

Samsung Secure Folder History Log Parser - <https://github.com/4n6Wizard/Samsung-HistoryLog-Parser>