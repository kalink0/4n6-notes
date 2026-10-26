---
title: "FSEvents"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [file-system-changes, file-existence]
---

# FSEvents

## Bedeutung

FSEvents (File System Events) ist ein systemnahes Framework in Apple Betriebssystemen, welches dafür entwickelt wurde, sämtliche Änderungen im Dateisystem in Echtzeit zu protokollieren. Es werden Erstellung, Änderung (Inhalt und Metadaten), Umbenennung und Löschung von Dateien und Ordnern mit den zugehörigen Dateinamen und Dateipfaden protokolliert. Lesende Zugriffe werden nicht erfasst.

Aus digitalforensischer Sicht lassen sich anhand von Einträgen des FSEvents Aussagen zu Aktionen im Dateisystem treffen bezogen auf Dateinamen und Dateipfad. Über die fortlaufenden Event-IDs lässt sich die Reihenfolge der ersten Änderung verschiedener Objekte bestimmen. Mehrere Änderungen am selben Objekt werden jedoch zu einem Eintrag zusammengefasst; deren Reihenfolge und Häufigkeit sind nicht bestimmbar. Anhand der Daten können auch Aussagen über ehemals existierende Dateien und Ordner getroffen werden. Es lassen sich keine Aussagen zu dem Inhalt der Dateien oder den Akteuren treffen.

## Spezifische Kurzinformation

1. Die Zeitstempel sind NICHT direkt enthalten in der Ablage des FSEvents. Die Dateien, welche bis zu 5000 Events enthalten, haben aber selbst einen Zeitstempel, der den Zeitraum eingrenzt.
2. Es gibt zusätzlich zur Ablage im Dateisystem einen Puffer im Arbeitsspeicher - dies bedeutet, dass die Most Recent File Changes ggf. noch nicht auf den Datenträger geschrieben sind im laufenden System. Bei Absturz, Hard-Reset, unsauberem Aushängen des Volumes oder System-Upgrade gehen die Events im Puffer verloren.
3. Ablageort (Root-Verzeichnis jeder Partition):  
   **`/.fseventsd`**  
   Data-Volume ab macOS 10.15: **`/System/Volumes/Data/.fseventsd`**

## Referenzen

2024-06: <https://www.hexordia.com/blog/mac-forensics-analysis>

2018-11: <https://github.com/libyal/dtformats/blob/main/documentation/MacOS%20File%20System%20Events%20Disk%20Log%20Stream%20format.asciidoc>

2017-10: <https://www.osdfcon.org/presentations/2017/Ibrahim-Understanding-MacOS-File-Ststem-Events-with-FSEvents-Parser.pdf>

## Tools

DLEAPP (Parser: FSEvents) - <https://github.com/abrignoni/DLEAPP>

FSEParser - <https://github.com/dlcowen/FSEventsParser>

FSEventsParser - <https://github.com/mac4n6/FSEventsParser>

FSEventsParser-rs - <https://github.com/Houwenda/FSEventsParser-rs>

mac_apt (Plugin: FSEVENTS) - <https://github.com/ydkhatri/mac_apt>

Plaso (Parser: fseventsd) - <https://github.com/log2timeline/plaso>

Velociraptor (Artefakt: MacOS.Forensics.FSEvents) - <https://docs.velociraptor.app/artifact_references/pages/macos.forensics.fsevents/>