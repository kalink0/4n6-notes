---
title: "ExFAT"
status: draft
---

# ExFAT

## Bedeutung

exFAT ist ein von Microsoft 2006 entwickeltes Dateisystem, das primär für Flash-Speicher wie USB-Sticks, SD-Karten und externe Festplatten gedacht ist. Es wurde als Nachfolger von FAT32 konzipiert, um größere Dateien und Speichermedien ohne die Einschränkungen von FAT32 zu unterstützen und ohne dabei die Komplexität von NTFS mitzubringen.

## Spezifische Kurzinformation

1. Maximale Volumegröße: 128 PiB
2. Maximale Dateigröße: 128 PiB
3. Maximale Dateinamenlänge: 255 Zeichen
4. Zeitstempel:
   1. Zeitstempel absolut abgespeichert
   2. Lokale/Systemzeit, zusätzlich Zeitzoneninformation
   3. Access, Creation und Modified Zeitstempel in 10 ms Auflösung

### Komponenten

#### Volume Boot Record

Liegt in den Sektoren 0 - 11 im Volume. 

Ein Backup des VBR liegt direkt hinter dahinter in den Sektoren 12 - 23.

Der VBR enthält im ersten Sektor den Main Boot Sektor, direkt gefolgt vom Extended Boot Sektor. Diese beiden Bereiche enthalten die relevantesten Informationen für die digitale Forensik.

#### File Allocation Table (FAT)

Die File Allocation Table bei exFAT hat dieselbe Aufgabe wie bei FAT32. Sie enthält die die FAT chains bei großen Ordnern und fragmentierten Dateien und wird daher benötigt um diese wiederherzustellen.

Jeder Cluster im Volume wird von einem  4 Byte Eintrag in der FAT repräsentiert.

Folgende Werte kann ein FAT Eintrag haben:

- 0x00 00 00 00: Cluster ist nicht belegt
- 0xFF FF FF F7: Cluster ist als "Bad" markiert und ist nicht mehr zu verwenden
- 0xFF FF FF FF: Cluster enthält das Ende einer Chain und somit das Ende einer Datei
- ODER: Den nächsten Cluster in der Chain z.b. 0x71 01 00 00 (0x0171 LE) -> nächstes Dateifragment in Sektor 369

#### Directory Entries

Directory Entries sind als eine Art Inhaltsverzeichnis mit ggf. zusätzlichen Metadaten zu verstehen. Es existieren unterschiedliche Typen. Eineige Typen beinhalten lediglich den Offset wo sich die eigentlichen Daten befinden, andere beinhalten zusätzliche Metadaten wie z.B. Zeitstempel und Dateinamen.

Im Folgenden werden die Typen und die dahinterliegen Datein kurz erkärt.

##### Allocation Bitmap (0x81)

Der Directory Entry enthält den Offset, die Länge und die korrespondierende FAT.

Die Allocation Bitmap File tracked alle Cluster des Dateisystem nach Status Allocated und unallocated. 1 Bit entspricht hierbei einem Cluster.

##### Up-Case Table (0x82)

Der Directory Entry enthält den Offset und die Länge der Up-Case Table.

Die Up-Case-Table dient dazu nach Dateinamen und Ordnernamen "case-insensitive" zu suchen.

Da exFAT per Definition keinen Wert auf Groß- und Kleinschreibung legt, ist dies notwendig um identische Dateinamen zu erkennen.

Die Up-Case-Table beinhaltet das Mapping von Kleinbuchstaben zu deren korrespondierenden Großbuchstaben.

##### Volume Label (0x83)

Der Directory Entry enthält das Label des Volumes welches festgelegt wurde.

##### File (0x85)

Der File Directory Entry enthält die Metadaten wie z.B. die Zeitstempel zur Datei.

Zusätzlich hat jeder File Directory Entry mindestens zwei sekundäre Directory Entries. Eine Stream Extension, welche den Ort der Datei im Volume enthält und eine Filename Extension, welche den Dateinamen enthält. Bei Notwendigkeit können noch weitere sekundäre Directory Entries vorliegen (z.B. lange Dateinamen)

##### Volume GUID (0xA0)

Enthält die GUID (Global Unique Identifier) des Volumes.

##### Stream Extension (0xC0)

Enhält den Speicherort der Datei, Die Dateigröße und die Information, ob die Datei fragmentiert abgelegt ist.

##### Filename Extension (0xC1)

Die Filename Extension enthält den Dateinamen - er kann maximal 15 Buchstaben enthalten. Bei längeren Dateinamen würden weitere Filename Extnesions angelegt werden. Es können maximal 17 Filename Extensions zu einer Datei vorliegen. Ein Dateiname kann dementsprechend maximal 255 Zeichen lang sein.

### Vorgehen manuelle Analyse

1. VBR analysieren
2. Analysieren des Root Directories
3. Analysieren Subdirectories
4. Wiederherstellen von Metadaten und Dateiinhalten
   1. Kleine Dateien (Nicht fragmentiert)
   2. Große Dateien (Fragmentiert)

## Referenzen

2025-07: <https://learn.microsoft.com/en-us/windows/win32/fileio/exfat-specification>

<https://www.ntfs.com/exfat-overview.htm> (Last Accessed: 2025-08-31)

## Tools

Sleuthkit - <https://sleuthkit.org/sleuthkit/download.php>
