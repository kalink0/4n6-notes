---
title: "EXT2"
status: draft
---

# EXT2

## Bedeutung

*Noch kein Inhalt.*

## Spezifische Kurzinformation

1. Maximale Volumegröße: 32 TiB
2. Maximale Dateigröße: 2 TiB
3. Zeitstempel:
   1. Zeitstempel relativ zu 01.01.1970 00:00:00 in UTC+0
   2. Zeitstempel auf eine Sekunde genau
   3. Kein Erstellzeitstempel
   4. Zusätzlich ein Löschzeitstempel

### Komponenten

#### Superblock

*Noch kein Inhalt.*

#### Block Groups

*Noch kein Inhalt.*

#### Block Group Descriptor Table

*Noch kein Inhalt.*

#### Inode Table

##### Mode/Permission

*Noch kein Inhalt.*

##### Inode Flags

*Noch kein Inhalt.*

##### Block Pointers

*Noch kein Inhalt.*

#### Bitmaps (Data and Inode)

*Noch kein Inhalt.*

### Vorgehen manuelle Analyse

1. Analysieren des Superblocks
2. Mappen der Block Groups
3. Analysieren des Root Directories Inode
4. Analysieren des Root Directories
5. Analysieren Directories
6. Analysieren Dateien

## Referenzen

2005-03: Brian Carrier: File System Forensic Analysis (Addison-Wesley, 2005), ISBN 978-0-321-26817-4

## Tools

*Noch kein Inhalt.*
