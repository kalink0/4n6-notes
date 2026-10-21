---
title: "NTFS"
status: draft
---

# NTFS

## Bedeutung

*Noch kein Inhalt.*

## Spezifische Kurzinformation

1. Maximale Volumegröße: 8 PiB
2. Maximale Dateigröße: 8 PiB
3. Zeitstempel:
   1. Zeitstempel realtiv abgespeichert zum 01.01.1601 00:00:00
   2. Zeitstempel in UTC+0
   3. Alle Zeitstempel in 100 ns Auflösung

### Komponenten

#### $Boot

*Noch kein Inhalt.*

#### Master File Table ($MFT)

Resident

Non-Resident

$STANDARD_INFORMATION (0x10)

$ATTRIBUTE_LIST (0x20)

$FILENAME (0x30)

$OBJECT_ID (0x40)

$SECURITY_DESCRIPTOR (0x50)

$VOLUME_NAME (0x60)

$VOLUME_INFORMATION (0x70)

$DATA (0x80)

$INDEX_ROOT (0x90)

$INDEX_ALLOCATION (0xA0)

$BITMAP (0xB0)

$REPARSE_POINT (0xC0)

#### Logfile ($Logfile)

...

### Vorgehen manuelle Analyse

1. $Boot analyiseren
2. $MFT wiederherstellen und analysieren
3. Analysieren von Directories
4. Wiederherstellen von Metadaten und Dateiinhalten
   1. Named Secondary $DATA attribute (Alternate Data Stream)

## Referenzen

2008: [Richard Russon, Yuval Fledel: NTFS Documentation (Linux-NTFS project)](https://flatcap.github.io/linux-ntfs/ntfs/)

2005-03: Brian Carrier: File System Forensic Analysis (Addison-Wesley, 2005), ISBN 978-0-321-26817-4

<https://www.ntfs.com/ntfs_basics.htm> (Last Accessed: 2025-08-31)

<https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc781134(v=ws.10)#how-ntfs-works-1> (Last Accessed: 2025-09-07)

## Tools

*Noch kein Inhalt.*
