---
title: "Dateisystem"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
---

# Dateisystem

Ein Dateisystem legt fest, wie Dateien und Verzeichnisse auf einem Datenträger bzw. in einer Partition gespeichert, benannt und wiedergefunden werden.

Neben dem Inhalt der Dateien verwaltet es deren Metadaten, z. B. Name, Pfad, Größe, Zeitstempel und Berechtigungen, sowie die Information, welche Bereiche des Datenträgers belegt und welche frei sind. Der Speicherplatz wird dabei in Einheiten fester Größe (Cluster bzw. Blöcke) vergeben. Viele Dateisysteme protokollieren Änderungen in einem Journal oder schreiben geänderte Daten an eine neue Stelle (Copy-on-Write), um nach einem Absturz einen konsistenten Zustand wiederherzustellen. Beispiele für Dateisysteme sind NTFS, FAT32, exFAT, APFS und ext4.

Aus digitalforensischer Sicht markiert ein Dateisystem beim Löschen einer Datei meist nur deren Eintrag und Speicherplatz als frei. Ob der Inhalt danach noch auslesbar ist, hängt vom Datenträger ab: Auf magnetischen Festplatten bleibt er in der Regel erhalten, bis der Bereich überschrieben wird; bei Flash-Speicher (z. B. SSD, eMMC, UFS) kann der Controller freigegebene Bereiche nach einem TRIM-Befehl bereits kurz darauf löschen. Welche Zeitstempel es gibt, in welcher Auflösung und Zeitzone sie gespeichert werden und wann sie sich ändern, hängt vom Dateisystem und vom Betriebssystem ab. Journale und per Copy-on-Write ersetzte Bereiche können ältere Stände von Metadaten enthalten.
