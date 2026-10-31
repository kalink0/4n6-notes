---
title: "exFAT"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# exFAT

## Bedeutung

exFAT ist ein von Microsoft 2006 entwickeltes Dateisystem, das primär für Flash-Speicher wie USB-Sticks, SD-Karten und externe Festplatten gedacht ist. Es wurde als Nachfolger von FAT32 konzipiert, um größere Dateien und Speichermedien ohne die Einschränkungen von FAT32 zu unterstützen und ohne dabei die Komplexität von NTFS mitzubringen.

## Spezifische Kurzinformation

1. Maximale Volumegröße: 128 PiB
2. Maximale Dateigröße: 128 PiB
3. Maximale Dateinamenlänge: 255 Zeichen
4. Zeitstempel:
   1. Zeitstempel absolut abgespeichert
   2. Lokale/Systemzeit, zusätzlich Zeitzoneninformation
   3. Creation und Modified Zeitstempel in 10 ms Auflösung, Access Zeitstempel in 2 s Auflösung

### Komponenten

#### Volume Boot Record

##### Funktionsweise

Liegt in den Sektoren 0 - 11 im Volume.

Ein Backup des VBR liegt direkt dahinter in den Sektoren 12 - 23.

Der VBR enthält im ersten Sektor den Main Boot Sektor, direkt gefolgt von 8 Extended Boot Sektoren (nur Boot-Code). Danach folgen die OEM Parameter (Sektor 9), ein reservierter Sektor (10) und die Boot-Checksumme (11).

##### Forensischer Nutzen

Forensisch relevant sind der Main Boot Sektor (u.a. Volume Serial Number, Lage von FAT, Cluster Heap und Root Directory, Clustergröße, VolumeFlags) und die Boot-Checksumme in Sektor 11. Im Backup sind VolumeFlags und PercentInUse veraltet.

#### File Allocation Table (FAT)

##### Funktionsweise

Die File Allocation Table bei exFAT beschreibt wie bei FAT32 die Cluster Chains. Eine Chain existiert für fragmentierte Dateien und Ordner sowie immer für das Root Directory. Bei nicht fragmentierten Dateien und Ordnern (NoFatChain in der Stream Extension gesetzt) sind die FAT-Einträge ungültig und werden nicht ausgewertet. Der Belegungsstatus der Cluster steht bei exFAT nicht in der FAT, sondern ausschließlich in der Allocation Bitmap.

Jeder Cluster im Volume wird von einem 4 Byte Eintrag in der FAT repräsentiert. Die Clusternummerierung beginnt bei 2.

Folgende Werte kann ein FAT Eintrag haben:

- 0xFF FF FF F7: Cluster ist als "Bad" markiert und ist nicht mehr zu verwenden
- 0xFF FF FF FF: Cluster enthält das Ende einer Chain und somit das Ende einer Datei
- ODER: Den nächsten Cluster in der Chain z.B. 0x71 01 00 00 (0x0171 LE) -> nächstes Dateifragment in Cluster 369

Der Sektor eines Clusters berechnet sich als ClusterHeapOffset + (Clusternummer − 2) × Sektoren pro Cluster.

##### Forensischer Nutzen

Die FAT wird benötigt, um fragmentierte Dateien und Ordner wiederherzustellen. Ein FAT-Eintrag mit dem Wert 0 bedeutet nicht, dass der Cluster frei ist – eine belegte, zusammenhängend gespeicherte Datei hat in der Regel keine Einträge in der FAT.

#### Directory Entries

##### Funktionsweise

Directory Entries sind als eine Art Inhaltsverzeichnis mit ggf. zusätzlichen Metadaten zu verstehen. Jeder Directory Entry ist 32 Byte groß. Es existieren unterschiedliche Typen. Einige Typen beinhalten lediglich den Offset, wo sich die eigentlichen Daten befinden, andere beinhalten zusätzliche Metadaten wie z.B. Zeitstempel und Dateinamen.

Das oberste Bit des Typ-Bytes (InUse) kennzeichnet einen Eintrag als in Verwendung. 0x00 markiert das Ende des Verzeichnisses.

Im Folgenden werden die Typen und die dahinterliegenden Dateien kurz erklärt.

###### Allocation Bitmap (0x81)

Der Directory Entry enthält den Offset, die Länge und die korrespondierende FAT.

Die Allocation Bitmap File tracked alle Cluster des Dateisystems nach Status Allocated und unallocated. 1 Bit entspricht hierbei einem Cluster.

###### Up-Case Table (0x82)

Der Directory Entry enthält den Offset und die Länge der Up-Case Table.

Die Up-Case-Table dient dazu, nach Dateinamen und Ordnernamen "case-insensitive" zu suchen.

Da exFAT per Definition keinen Wert auf Groß- und Kleinschreibung legt, ist dies notwendig, um identische Dateinamen zu erkennen.

Die Up-Case-Table beinhaltet das Mapping von Kleinbuchstaben zu deren korrespondierenden Großbuchstaben.

###### Volume Label (0x83)

Der Directory Entry enthält das Label des Volumes, welches festgelegt wurde.

###### File (0x85)

Der File Directory Entry enthält die Metadaten wie z.B. die Zeitstempel zur Datei.

Zusätzlich hat jeder File Directory Entry mindestens zwei sekundäre Directory Entries. Eine Stream Extension, welche den Ort der Datei im Volume enthält, und eine Filename Extension, welche den Dateinamen enthält. Bei Notwendigkeit können noch weitere sekundäre Directory Entries vorliegen (z.B. lange Dateinamen).

Der File Directory Entry enthält zudem eine Checksumme (SetChecksum) über das gesamte Entry-Set, also den File Entry und alle zugehörigen sekundären Entries.

###### Volume GUID (0xA0)

Enthält die GUID (Globally Unique Identifier) des Volumes.

###### Stream Extension (0xC0)

Enthält den Speicherort der Datei, die Dateigröße und die Information, ob die Datei fragmentiert abgelegt ist.

###### Filename Extension (0xC1)

Die Filename Extension enthält den Dateinamen - er kann maximal 15 Buchstaben enthalten. Bei längeren Dateinamen würden weitere Filename Extensions angelegt werden. Es können maximal 17 Filename Extensions zu einer Datei vorliegen. Ein Dateiname kann dementsprechend maximal 255 Zeichen lang sein.

##### Forensischer Nutzen

- Gelöschte Einträge: Beim Löschen wird das InUse-Bit gelöscht (0x85 → 0x05, 0xC0 → 0x40, 0xC1 → 0x41) und die Cluster in der Allocation Bitmap freigegeben. Name, erster Cluster, Dateigröße und Zeitstempel bleiben bis zum Überschreiben erhalten.
- Nicht fragmentierte gelöschte Dateien lassen sich anhand von erstem Cluster und Dateigröße wiederherstellen, solange die Cluster nicht neu belegt sind. Bei fragmentierten Dateien ist die Wiederherstellung nur möglich, solange die FAT-Chain erhalten ist.
- Verwaiste Einträge: Es können Verzeichniscluster vorliegen, die in der Allocation Bitmap als belegt markiert sind, aber vom Verzeichnisbaum nicht mehr erreicht werden. Die Entry-Sets darin sind weiterhin als in Verwendung markiert und erscheinen in keiner regulären Verzeichnisauflistung.
- Über die SetChecksum lässt sich prüfen, ob ein gefundenes oder gecarvtes Entry-Set vollständig und unverändert ist.

### Checkliste Analyse

1. Main Boot Sektor auswerten (Clustergröße, Lage von FAT, Cluster Heap und Root Directory, Volume Serial Number), Boot-Checksumme prüfen, bei Abweichung den Backup in den Sektoren 12 - 23 heranziehen
2. Root Directory über die FAT-Chain lesen und Allocation Bitmap, Up-Case Table, Volume Label und Volume GUID auswerten
3. Subdirectories auswerten, dabei die SetChecksum der Entry-Sets prüfen
4. Gelöschte Einträge (0x05, 0x40, 0x41) suchen
5. Wiederherstellen von Metadaten und Dateiinhalten, vorher in der Allocation Bitmap prüfen, ob die Cluster noch frei sind
   1. Kleine Dateien (Nicht fragmentiert): ab dem ersten Cluster entsprechend der Dateigröße
   2. Große Dateien (Fragmentiert): entlang der FAT-Chain, sofern erhalten
6. Belegte Verzeichniscluster, die vom Verzeichnisbaum nicht erreicht werden, auf verwaiste Entry-Sets prüfen
7. Zeitstempel zusammen mit dem jeweiligen Zeitzonen-Offset auswerten

## Referenzen

2022-10: [Nordvik et al. – It is about time: Do exFAT implementations handle timestamps correctly?](https://doi.org/10.1016/j.fsidi.2022.301476)

2018-05: [Vandermeer et al. – Forensic Analysis of the exFAT Artefacts](https://commons.erau.edu/adfsl/2018/presentations/4)

2014-06: [The Sleuth Kit – exFAT Implementation Notes](https://wiki.sleuthkit.org/ExFAT-Implementation-Notes/)

2009-12: [Shullich – Reverse Engineering the Microsoft exFAT File System](https://www.sans.org/white-papers/33274)

2026-10: [NTFS.com – exFAT Overview](https://www.ntfs.com/exfat-overview.htm) (abgerufen)

**Dokumentation**

2025-07: [Microsoft – exFAT File System Specification](https://learn.microsoft.com/en-us/windows/win32/fileio/exfat-specification)

2026-10: [libyal – File Allocation Table (FAT) format (incl. exFAT)](https://github.com/libyal/libfsfat/blob/main/documentation/File%20Allocation%20Table%20%28FAT%29%20format.asciidoc) (abgerufen)

2026-10: [Crush Format Reference – exFAT](https://kalink0.github.io/crush-forensics/formats/exfat/)

## Tools

Sleuthkit - <https://sleuthkit.org/sleuthkit/download.php> (fsstat, fls, istat, icat)

qnxprobe - <https://github.com/abrignoni/qnxprobe>

exfatprogs - <https://github.com/exfatprogs/exfatprogs> (dump.exfat)