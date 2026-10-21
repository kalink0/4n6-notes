---
title: "Office Read Location"
status: complete
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
topics: [file-access]
---

# Office Read Location

## Bedeutung

Microsoft Word speichert die letzte Position, an der ein Nutzerkonto in einem Dokument zuletzt gelesen bzw. betrachtet hat ("Reading Locations"-Feature, auch bekannt als "Pick up where you left off"). Dies dient dazu, das Nutzerkonto beim erneuten Öffnen des Dokuments an diese Position navigieren zu können – auch geräteübergreifend, sofern über ein Microsoft-Konto angemeldet.

Aus digitalforensischer Sicht kann anhand der Daten gesagt werden, dass das angegebene Dokument durch das Nutzerkonto geöffnet war und zu dem angegebenen Zeitpunkt geschlossen wurde. Die zuletzt angezeigte Position im Dokument (Zeichen-Position der obersten sichtbaren Zeile ab Dokumentanfang) lässt sich anhand der Daten ebenfalls bestimmen.

## Spezifische Kurzinformation

1. Verfügbarkeit: Existiert seit **Word 2013** (Version 15.0).
2. Aufbewahrung: Es werden die Daten der **zuletzt 50 gelesenen Dokumente** gespeichert.
3. Format und Struktur: Pro Dokument wird ein Unterschlüssel `Document n` angelegt, mit den Werten `File Path` (Pfad des Dokuments) und `Datetime` (Zeitpunkt des letzten Schließens, **lokale Systemzeit**, Format ohne Sekundenangabe, z.B. `2025-08-23T14:39`). Der Wert `Position` besteht aus **zwei durch Leerzeichen getrennten Zahlen**: die erste entspricht der `w14:paraId` des zuletzt betrachteten Absatzes (aus der internen `document.xml`), die zweite der **Zeichen-Position vom Dokumentanfang**
4. Zeitstempel: Cross-Validierung: Der `Datetime`-Wert (lokale Zeit) sollte nach Umrechnung in UTC mit der **Last-Write-Time des jeweiligen** `Document n`**-Unterschlüssels** übereinstimmen
5. Besonderheiten und Fallstricke: Erfasst werden auch PDFs und über Outlook geöffnete Dokumente; deren Pfad zeigt dann auf den temporären Outlook-Cache. Dokumente auf Netzlaufwerken werden ebenfalls erfasst.
6. Ablageort:  
   **HKCU\\Software\\Microsoft\\Office\\{VERSION}\\Word\\Reading Locations**

## Referenzen

2026-10 (abgerufen): <https://renenyffenegger.ch/notes/Windows/registry/tree/HKEY_CURRENT_USER/Software/Microsoft/Office/application_version/Word/Reading-Locations/index>

2025-08: <https://isc.sans.edu/diary/32224>

2025-02: <https://www.cyberengage.org/post/registry-user-activity-tracking-recently-opened-files-in-microsoft-office-a-forensic-guide>

2022-10: <https://office-watch.com/2014/how-do-they-know-where-you-left-off/>

2019-02: <https://thinkdfir.com/2019/02/11/microsoft-office-reading-locations-part-1/>

## Tools

RegRipper (msoffice) - <https://github.com/keydet89/RegRipper4.0>