---
title: "FAT(32)"
status: draft
---

# FAT(32)

## Bedeutung

*Noch kein Inhalt.*

## Spezifische Kurzinformation

1. Maximale Volumegröße: 2 TiB
2. Maximale Dateigröße: 4 GiB
3. Zeitstempel:
   1. Zeitstempel absolut abgespeichert
   2. Lokale/Systemzeit, keine Zeitzoneninformation
   3. Access Zeitstempel nur auf den Tag genau
   4. Die weiteren Zeitstempel (Creation und Modified) sind auf 2 Sekunden genau
   5. Zeitstempeltyp: DOStime/DOSdate

### Komponenten

Das FAT Dateisystem teilt sich in drei Hauptbereiche:

1. Reserved Space
2. FAT Space
3. Root Directory Space (nur FAT12/16)
4. Data Space

Im Weiteren werden die Inhalte dieser Bereiche betrachtet.

#### Reserved Space

##### Volume Boot Record

Ort: Sektor 0 des Volumes

##### File System Information (FSINFO)

*Noch kein Inhalt.*

#### FAT Space

##### File Allocation Table (FAT)

*Noch kein Inhalt.*

#### Root Directory Space

ORt: Standard: CLusternummer 2, erster CLuster des Data Spaces in FAT32

#### Data Space

##### Directory Entries

###### Volume Label

*Noch kein Inhalt.*

### Vorgehen manuelle Analyse

1. VBR analysieren (Reserve area, FAT Area und Data area identifizieren)
2. Analysieren des Root Directories
3. Analysieren Subdirectories
4. Wiederherstellen von Metadaten und Dateiinhalten
   1. Kleine Dateien (kleiner Clsuter)
   2. Große Dateien (größer Cluster)

## Referenzen

2005-03: Brian Carrier: File System Forensic Analysis (Addison-Wesley, 2005), ISBN 978-0-321-26817-4

2000-12: [https://www.cs.fsu.edu/~cop4610t/assignments/project3/spec/fatspec.pdf](https://www.cs.fsu.edu/~cop4610t/assignments/project3/spec/fatspec.pdf)

<https://www.ntfs.com/fat_systems.htm> (Last Accessed: 2025-08-31)

<https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc776720(v=ws.10)> (Last Accessed: 2025-09-07)

## Tools

Sleuthkit - <https://sleuthkit.org/sleuthkit/download.php>
