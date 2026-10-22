---
title: "LevelDB"
status: complete
completed: 2026-10-22
authors: [kalink0 (Marco Neumann)]
---

# LevelDB

## Bedeutung

### Technische Beschreibung:

LevelDB ist eine von Google entwickelte Key-Value-Datenbank, die häufig von Apps und Betriebssystemen genutzt wird, um Konfigurations- und Verlaufsdaten zu speichern. Der Inhalt ist nicht standardisiert und kann von Klartext über Binärdaten bis hin zu serialisierten Strukturen reichen. Forensisch relevant ist, dass darin sensible Informationen wie Einstellungen, Tokens oder Nutzungsverläufe einer Anwendung enthalten sein können.

### Nicht-technische Beschreibung:

LevelDB ist eine Art Datenspeicher, den viele Apps im Hintergrund nutzen. Darin können sehr unterschiedliche Informationen liegen – zum Beispiel Einstellungen, Verlaufseinträge oder Anmeldedaten. Für eine Untersuchung kann dieser Speicher deshalb wichtige Hinweise darauf geben, wie eine App genutzt wurde und welche Daten dabei entstanden sind.

## Spezifische Kurzinformation

### Komponenten

Ablageort:

- Alle Dateien einer Datenbank liegen gemeinsam in einem Verzeichnis

#### log-Datei

##### Funktionsweise

Die log-Datei ist vergleichbar mit einer WAL-Datei bei SQLite und wird manchmal auch so genannt. Alle neuen Daten werden in die log-Datei gespeichert.

Neue Daten können hierbei folgende sein:

1. Komplett neue Daten
2. Änderung von bestehenden Daten
3. Löschen von bestehenden Daten

Alle Einträge haben eine Sequence-Number. Mittels dieser Nummer lässt sich die Historie darstellen.   
  
Die Key-Value-Paare liegen unverschlüsselt, uncodiert und nicht komprimiert vor.

In welchem Format die Values selbst vorliegen, obliegt dem Programmcode der datenerstellenden Komponente - dementsprechend können z.B. Dekodierungsschritte notwendig sein, um Daten interpretieren zu können.

Die Dateistruktur ist wie folgt:

1. Blöcke mit einer festen Größe von 32 KB können eine beliebige Anzahl von Records beinhalten. Bleiben am Blockende weniger als 7 Bytes, werden diese mit Nullen aufgefüllt.
2. Jeder Record beinhaltet einen 7 Byte Header, dieser wird wenn notwendig zum Beginn eines Blocks wiederholt mit den entsprechenden Werten für Record Type.
   1. Byte 0 bis 3: CRC-32C von Type und Payload
   2. Byte 4 bis 5: Länge des Records als UInt16 (Little Endian)
   3. Byte 6: Record Type (1 = Full, 2 = First, 3 = Middle, 4 = Last)
      1. Full = Gesamter Record im aktuellen Block
      2. First = Erster Teil des Records, weiterer Teil befindet sich im nächsten Block
      3. Middle = Im vorherigen und nächsten Block befinden sich Daten zu dem Record
      4. Last = Nur im vorherigen Block befinden sich Daten zu dem Record
3. Nach dem Record Header folgt die Payload mit der angegebenen Länge.
4. Die Payload ist meist ein WriteBatch (mehrere Operationen werden an einem Stück geschrieben). Daher kommt zusätzlich ein 12 Byte Header hinzu:
   1. Byte 0 bis 7: Sequence Number der ersten Operation; jede weitere Operation im Batch zählt um eins hoch
   2. Byte 8 bis 11: Anzahl von Operations im Batch (Int32)
5. Nach dem 12 Byte Batch kommen die Operations, eine Operation ist wie folgt aufgebaut:
   1. Länge = 1 Byte ; *Operation Type*

      0 = Delete (Löschen eines Eintrags unter Angabe des Keys)

      1 = Put (Hinzufügen oder Ändern eines Eintrags unter Angabe von Key und Value)
   2. Länge = 1 bis 5 Bytes ; *Schlüssellänge*

      Key Länge in VarInt32
   3. Länge = Schlüssellänge ; *Schlüssel*

      Key
   4. Länge = 1 bis 5 Bytes ; *Wertlänge*

      Wertlänge in VarInt32
   5. Länge = Wertlänge ; *Wert*

Wenn die log-Datei eine Größe von 4 MB (Default) übersteigt, werden die Daten in eine ldb-Datei (SSTable) übertragen. (läuft technisch über eine MemTable, die eine Kopie der log-Datei ist)

##### Forensischer Nutzen

Die log-Datei enthält jede Schreiboperation einzeln mit Sequence Number – auch überschriebene Werte und Löschungen. Damit lässt sich die Reihenfolge der Änderungen nachvollziehen, und gelöschte Keys bleiben sichtbar (Löschmarker ohne Value).

Keys und Values liegen unkomprimiert vor, Stringsuche funktioniert daher. Liegt ein Record über einer Blockgrenze, unterbricht der 7 Byte Header an der 32-KB-Grenze die Daten.

#### ldb-Datei

##### Funktionsweise

Die LDB-Datei ist die Speicherebene für das längerfristige Speichern. Ältere Implementierungen verwenden die Endung `.sst` statt `.ldb`, die Struktur ist gleich.

LDB-Dateien sind SSTables (Sorted String Tables), also Dateien, in denen die Einträge nach Key sortiert gespeichert sind. Sie werden nach dem Erstellen nicht mehr verändert - neue Daten landen immer in neuen Dateien.

Bei der Erstellung von ldb-Dateien werden unterschiedliche Level erstellt, dies hat keinen Einfluss auf die interne Struktur. Über die Manifest-Datei kann man die Information erhalten, welcher Key-Bereich in welcher ldb-Datei liegt.

In ldb-Dateien werden Daten ggf. komprimiert und es wird Key-Sharing verwendet - Näheres dazu in der Aufführung der Dateistruktur.

__Level 0:__ 

Die ldb-Datei erhält eine neue, fortlaufende Nummer – nicht die Nummer der zugehörigen log-Datei. Sie beinhaltet dieselben Einträge wie die log-Datei (inklusive überschriebener und gelöschter Einträge), aber nach Key sortiert. Nach dem Erreichen einer Dateigröße der log-Datei von standardmäßig 4 MB erfolgt die Erstellung einer ldb-Datei. Zusätzlich wird beim Öffnen der Datenbank die vorhandene log-Datei in eine Level-0-Datei überführt. Blöcke können mittels Snappy komprimiert sein.

__Level 1 und höher:__ 

Sobald standardmäßig 4 Level 0 ldb-Dateien vorliegen, werden diese mit den überlappenden Level-1-Dateien zu neuen Level-1-Dateien (je ca. 2 MB) zusammengeführt. Dieser Prozess wird als Compaction bezeichnet. Die Daten werden hierbei sortiert und dedupliziert und ggf. komprimiert. Überschriebene Werte werden verworfen, Löschmarker nur, wenn kein höheres Level den Key noch enthalten kann.

Ab Level 1 löst die Gesamtgröße eines Levels die nächste Compaction aus (Level 1: 10 MB, Level 2: 100 MB usw.).

Die Dateistruktur ist wie folgt:

1. Data Block

   Hier werden die Daten gespeichert. Es können mehrere Data Blocks existieren in einer Datei.
   1. Block Entries (Key-Value Paare), je Eintrag:
      1. Shared-Key-Länge (VarInt32): Anzahl der Bytes, die vom vorherigen Key übernommen werden
      2. Non-Shared-Key-Länge (VarInt32)
      3. Wertlänge (VarInt32)
      4. Nicht geteilter Teil des Keys
      5. Wert
   2. Restart-Array am Blockende (nur zum schnellen Suchen nötig)
   3. Trailer (5 Bytes)
      1. Kompression (1 Byte)

         0 = Keine Kompression

         1 = Snappy
      2. CRC-32 der Block Daten (4 Bytes)

   Die letzten 8 Bytes jedes Keys sind kein Teil des Nutzer-Keys: 7 Bytes Sequence Number und 1 Byte Status (0 = gelöscht, 1 = aktiv).
2. Meta Block

   Beinhaltet z.B. Bloom Filter, um schnell zu ermitteln, ob ein Key in den Daten existiert
3. Meta Index Block

   Index der existierenden Meta Blocks
4. Index Block

   Index der existierenden Data Blocks
5. Footer

   Länge: 48 Bytes
   1. Metaindex Block Handle (Offset und Size, je varint64)

      Gibt Position und Größe des Meta Index Blocks an
   2. Index Block Handle (Offset und Size, je varint64)

      Gibt Position und Größe des Index Blocks an
   3. Auffüllung mit Nullen, sodass 1. bis 3. zusammen 40 Bytes ergeben
   4. Magic Number (8 Bytes)
      1. 0xdb4775248b80fb57 (Little Endian, auf dem Datenträger `57 FB 80 8B 24 75 47 DB`)

Die Index Blöcke dienen dem schnellen Finden von Einträgen sind aber zum Lesen/Dumpen aller Einträge nicht notwendig.

##### Forensischer Nutzen

Level-0-Dateien enthalten dieselben Einträge wie die log-Datei, aus der sie entstanden sind, inklusive überschriebener und gelöschter Einträge.

Ab Level 1 sind überschriebene Werte durch die Compaction entfernt. Löschmarker können erhalten bleiben.

Durch Snappy-Kompression und Key-Sharing ist eine Stringsuche ohne vorheriges Dekomprimieren nicht zuverlässig.

Nach einer Compaction werden die alten ldb-Dateien gelöscht.

#### MANIFEST

##### Funktionsweise

Beinhaltet pro ldb-Datei Level, Größe und Key-Bereich (kleinster/größter Key), dazu Comparator, aktuelle log-Datei und letzte Sequence Number. Das MANIFEST hat dasselbe Format wie die log-Datei, enthält aber VersionEdits statt WriteBatches. Bei jedem Öffnen der Datenbank entsteht ein neues MANIFEST.

##### Forensischer Nutzen

Die letzte Sequence Number zeigt, wie viele Schreiboperationen insgesamt auf der Datenbank stattgefunden haben. Ältere MANIFEST-Dateien können auf ldb-Dateien verweisen, die nicht mehr vorhanden sind.

#### CURRENT

##### Funktionsweise

Textdatei mit dem Namen des aktuellen MANIFEST.

##### Forensischer Nutzen

Zeigt, welches MANIFEST aktuell ist. Damit lässt sich ein älteres MANIFEST als historisch einordnen.

#### LOG / LOG.old

##### Funktionsweise

Text-Log von LevelDB selbst – nicht zu verwechseln mit der binären log-Datei. LOG.old ist das vorherige LOG.

##### Forensischer Nutzen

Enthält Compactions, das Öffnen der Datenbank und Fehler und hilft so einzuordnen, was mit der Datenbank passiert ist.

Die Zeitstempel liegen in lokaler Zeit des Geräts vor, ohne Zeitzonenangabe.

#### LOCK

##### Funktionsweise

Sperrdatei, ohne forensischen Nutzen.

## Checkliste Analyse

1. Das gesamte Verzeichnis sichern, alle Dateien gemeinsam.
2. Die Datenbank nie mit der App oder einer LevelDB-Bibliothek am Original öffnen. Beim Öffnen wird die aktuelle log-Datei in eine Level-0-Datei überführt und nicht mehr benötigte Dateien werden gelöscht.
3. CURRENT lesen: Welches MANIFEST ist aktuell?
4. MANIFEST auswerten: aktive ldb-Dateien je Level, aktuelle log-Datei, letzte Sequence Number, Comparator.
5. Dateien, die nicht im aktuellen MANIFEST stehen, gesondert auswerten – sie gehören nicht zum aktuellen Stand.
6. log-Datei auswerten, inklusive Löschungen.
7. ldb-Dateien auswerten, zuerst Level 0, dann die höheren Level. Für eine Stringsuche Blöcke vorher dekomprimieren.
8. Einträge aller Dateien über die Sequence Number zusammenführen: Die höchste Sequence Number je Key ist der aktuelle Stand, niedrigere sind ältere Versionen.
9. Values dekodieren – das Format legt die App fest (z.B. Protobuf, JSON).
10. LOG / LOG.old für den Kontext heranziehen.

## Referenzen

2026-05: [beBinary: Reading the CURRENT – LevelDB Forensics with crush](https://bebinary4n6.blogspot.com/2026/05/reading-current-leveldb-forensics-with.html)

2020-10: [CCL: IndexedDB on Chromium](https://www.cclsolutionsgroup.com/post/indexeddb-on-chromium)

2020-09: [CCL: Hang on! That's not SQLite! Chrome, Electron and LevelDB](https://www.cclsolutionsgroup.com/post/hang-on-thats-not-sqlite-chrome-electron-and-leveldb)

2015-12: [Kevin Kwok: Recovering Deleted Data from LevelDB](https://antimatter15.com/2015/12/recovering-deleted-data-from-leveldb/)

[Forensics Wiki: LevelDB format](https://forensics.wiki/leveldb_format/)

LevelDB-Dokumentation:
- Dateien, Level und Compaction: <https://github.com/google/leveldb/blob/main/doc/impl.md>
- log-Format: <https://github.com/google/leveldb/blob/main/doc/log_format.md>
- Tabellenformat (ldb): <https://github.com/google/leveldb/blob/main/doc/table_format.md>

crush Format Reference:
- <https://kalink0.github.io/crush-forensics/formats/de/leveldb/>

## Tools

crush - <https://github.com/kalink0/crush-forensics>

dfindexeddb (dfleveldb) - <https://github.com/google/dfindexeddb>

LevelDB Dumper - <https://github.com/mdawsonuk/LevelDBDumper>

LevelDBtoSQLite - <https://github.com/SpyderForensics/Digital4n6withDamien/tree/main/LevelDBtoSQLite>

ccl_chromium_reader (storage_formats/ccl_leveldb.py) - <https://github.com/cclgroupltd/ccl_chromium_reader/>