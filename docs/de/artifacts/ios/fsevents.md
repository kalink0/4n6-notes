---
title: "FSEvents"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [file-system-changes, file-existence]
---

# FSEvents

## Bedeutung

FSEvents (File System Events) ist ein systemnahes Framework in Apple Betriebssystemen, welches dafür entwickelt wurde, sämtliche Änderungen im Dateisystem in Echtzeit zu protokollieren. Es werden Erstellung, Änderung (Inhalt und Metadaten), Umbenennung und Löschung von Dateien und Ordnern mit den zugehörigen Dateinamen und Dateipfaden protokolliert. Lesende Zugriffe werden nicht erfasst.

Aus digitalforensischer Sicht lassen sich anhand von Einträgen des FSEvents Aussagen zu Aktionen im Dateisystem treffen bezogen auf Dateinamen und Dateipfad. Die Reihenfolge der Einträge kann ebenfalls genannt werden; mehrere Aktionen am selben Pfad können jedoch in einem Eintrag zusammengefasst sein, ohne dass ihre Reihenfolge erkennbar ist. Anhand der Daten können auch Aussagen über ehemals existierende Dateien und Ordner getroffen werden. Es lassen sich keine Aussagen zu dem Inhalt der Dateien oder den Akteuren treffen.

## Spezifische Kurzinformation

1. Die Zeitstempel sind NICHT direkt enthalten in der Ablage des FSEvents. Die Dateien, welche bis zu 5000 Events enthalten, haben aber selbst einen Zeitstempel, der den Zeitraum eingrenzt.
2. Es gibt zusätzlich zur Ablage im Dateisystem einen Puffer im Arbeitsspeicher - dies bedeutet, dass die Most Recent File Changes ggf. noch nicht auf den Datenträger geschrieben sind im laufenden System.
3. Ablageort (ggf. noch mehr Orte in iOS):  
   **`/private/var/.fseventsd`**  
   **`/private/var/mobile/.fseventsd`**

## Referenzen

2024-02: <https://github.com/libyal/dtformats/blob/main/documentation/MacOS%20File%20System%20Events%20Disk%20Log%20Stream%20format.asciidoc>

2017-10: <https://www.osdfcon.org/presentations/2017/Ibrahim-Understanding-MacOS-File-Ststem-Events-with-FSEvents-Parser.pdf>

## Tools

FSEParser - <https://github.com/dlcowen/FSEventsParser>

FSEventsParser - <https://github.com/mac4n6/FSEventsParser>

FSEventsParser-rs - <https://github.com/Houwenda/FSEventsParser-rs>

iLEAPP (iosFileSystemEvents) - <https://github.com/abrignoni/iLEAPP>

mac_apt (FSEVENTS) - <https://github.com/ydkhatri/mac_apt>