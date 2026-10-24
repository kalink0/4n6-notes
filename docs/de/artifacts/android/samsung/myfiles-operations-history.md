---
title: "Samsung MyFiles Operations History"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [file-existence]
---

# Samsung MyFiles Operations History

## Bedeutung

Die Samsung MyFiles Operations History speichert Dateioperationen, die sich auf Ordner und Dateien beziehen. Es werden die Operationen Erstellen, Umbenennen, Verschieben, Kopieren und Löschen gespeichert pro Datei/Ordner. Die Operation muss hierbei mit dem Samsung Dateimanager durchgeführt worden sein. Bei Verwendung einer anderen App werden die Daten nicht geschrieben.

Aus digitalforensischer Sicht bedeuten die Einträge, dass die jeweilige Datei/der jeweilige Ordner samt darin befindlichen Dateien/Ordnern zum angegebenen Zeitpunkt gemäß der angegebenen Operation geändert wurden. Also z.B. angelegt, kopiert, umbenannt oder gelöscht wurden.

## Spezifische Kurzinformation

1. Die Datenbank liegt, wenn MyFiles so verwendet wurde, pro Nutzer und für den SecureFolder vor
2. Nur Dateioperationen, die über die Samsung MyFiles-App durchgeführt wurden, sind darin aufgeführt.
3. Keine automatische Löschung beobachtet; Einträge reichten ca. 1,5 Jahre zurück
4. Zeitstempel: als Text gespeichert, UTC
5. Ablageort:  
   **`/data/data/com.sec.android.app.myfiles/databases/OperationHistory.db`**  
   **`/data/user/{USER_ID}/com.sec.android.app.myfiles/databases/OperationHistory.db`**

## Referenzen

2026-01: <https://bebinary4n6.blogspot.com/2026/01/android-samsung-my-files-app-exploring.html>

## Tools

ALEAPP (Parser: My Files Operation History, My Files - File Operations) - <https://github.com/abrignoni/ALEAPP>

SELECT-Queries - <https://github.com/kalink0/useful_scripts/blob/master/sql/Android/Samsung%20Apps/sMyFiles.sql>