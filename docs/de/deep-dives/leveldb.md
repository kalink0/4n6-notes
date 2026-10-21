---
title: "LevelDB"
status: draft
---

# LevelDB

## Bedeutung

### Technische Beschreibung:

LevelDB ist eine von Google entwickelte Key-Value-Datenbank, die häufig von Apps und Betriebssystemen genutzt wird, um Konfigurations- und Verlaufsdaten zu speichern. Der Inhalt ist nicht standardisiert und kann von Klartext über Binärdaten bis hin zu serialisierten Strukturen reichen. Forensisch relevant ist, dass darin sensible Informationen wie Einstellungen, Tokens oder Nutzungsverläufe einer Anwendung enthalten sein können.

### Nicht-technische Beschreibung:

LevelDB ist eine Art Datenspeicher, den viele Apps im Hintergrund nutzen. Darin können sehr unterschiedliche Informationen liegen – zum Beispiel Einstellungen, Verlaufseinträge oder Anmeldedaten. Für eine Untersuchung kann dieser Speicher deshalb wichtige Hinweise darauf geben, wie eine App genutzt wurde und welche Daten dabei entstanden sind.

## Spezifische Kurzinformation

### Komponenten

#### log-Datei

Die log-Datei ist vergleichbar mit einer WAL-Datei bei SQLite und wird manchmal auch so genannt. Alle neuen Daten werden in die log-Datei gespeichert.

Neue Daten können hierbei folgende sein:

1. Komplett neue Daten
2. Änderung von bestehenden Daten
3. Löschen von bestehenden Daten

Alle Einträge haben eine Sequence-Number. Mittels dieser Nummer lässt sich die Historie darstellen.   
  
Die Key-Value-Paare liegen unverschlüsselt, uncodiert und nicht komprimiert vor.

In welchem Format die Values selbst vorliegen obliegt dem Programmcode der datenerstellenden Komponente - dementsprechend können z.B. Dekodierungsschritte notwendig sein um Daten interpretieren zu können.

Die Dateistruktur ist wie folgt:

1. Blöcke mit einer festen Größe von 32 KB können eine beliebige Anzahl von Records beinhalten. Wird mit Nullen aufgefüllt.
2. Jeder Record beinhaltet einen 7 Byte Header, dieser Wird wenn notwendig zum Begin eines Blocks wiederholt mit den entsprechenden Werte für Record Type.
   1. Byte 0 bis 3: CRC-32 von Type und Payload
   2. Byte 4 bis 5: Länge des Records als Int16
   3. Byte 6: Record Type (1 = Full, 2 = First, 3 = Middle, 4 = Last)
      1. Full = Gesamter Record im aktuellen Block
      2. First = Erster Teils des Records, weiterer Teil befindet sich im nächsten Block
      3. Middle = Im vorherigen und nächsten Block befinden sich Daten zu dem Records
      4. Last = Nur im vorherigen Block befinden sich Daten zu dem Records
3. Nach dem Record Header folgt die Payload mit der angegebenen Länge.
4. Die Payload ist meist ein WriteBatch (mehrere Operationen werden an einem Stück geschrieben). Daher kommt zusätzlich ein 12 Byte Header hinzu:
   1. Byte 0 bis 7: Sequence Number
   2. Byte 8 bis 11: Anzahl von Operations im Batch (Int32)
5. Nach dem 12 Byte Batch kommen die Operations, eine Operations ist wie folgt aufgebaut:
   1. Länge = 1 Byte ; *Operation Type*

      0 = Delete (Löschen eines Eintrags unter Angabe des Keys)

      1 = Put (Hinzufügen oder Ändern eines Eintrags unter Angabe von Key und Value)
   2. Länge = 1 bis 4 Bytes ; *Schlüssellänge*

      Key Länge in VarInt32
   3. Länge = Schlüssellänge ; *Schlüssel*

      Key
   4. Länge = 1 bis 4 Bytes ; *Wertlänge*

      Wertlänge in VarInt32
   5. Länge = Wertlänge ; *Wert*

Wenn die log-Datei eine Größe von 4 MB (Default) übersteigt, werden die Daten in eine ldb-Datei (SSTable) übertragen. (läuft technisch über eine MemTable die eine Kopie der log-Datei ist)

#### ldb-Datei

Die LDB-Datei ist die Speicherebene für das längerfristige Speichern. 

LDB-Dateien sind SSTables und somit nicht veränderbar - es erfolgt also kein Änderung der LDB-Datei nachdem sie erstellt wurde.

Bei der Erstellung von ldb-Dateien werden unterschiedliche Level erstellt, dies hat keinen Einfluss auf die interne Struktur. Über die Manifest-Datei kann man die Information erhalten, welche Key-Value Paare in welcher ldb-Datei liegen.

In ldb-Datein werden Daten ggf. komprimiert und es wird Key-Sharing verwendet - Näheres dazu in der Aufführung der Dateistruktur.

__Level 0:__ 

Die ldb-Datei hat den selben Namen wie die zugehörige log-Datei und beinhaltet die identischen Daten. Nach dem Erreichen einer Dateigröße der log-Datei von standardmäßig  4 MB erfolgt die Erstellung einer ldb-Datei. Die beinhalteten Daten sind identisch zur log-Datei. Einträge können mittels Snappy komprimiert sien.

__Level 1 und höher:__ 

Sobald standardmäßig 4 Level 0 ldb-Datei vorliegen erfolgt eine Erstellung einer Level 1 ldb-Datei aus den Daten. Dieser Prozess wird als Compaction bezeichnet. Die Daten werden hierbei sortiert und dedupliziert und ggf. komprimiert.

Die Dateistruktur ist wie folgt:

1. Data Block

   Hier werden die Daten gespeichert. Es können mehrere Data Blocks existeren in einer Datei.
   1. Block Entry Structure
   2. Daten (Key-Value Paare)
   3. Trailer (5 Bytes)
      1. Kompression (1 Byte)

         0 = Keine Kompression

         1 = Snappy
      2. CRC-32 der Block Daten (4 Bytes)
2. Meta Block

   Beinhaltet z.B. Bloom Filter um schnell zu ermitteln, ob ein Key in den Daten existiert
3. Meta Index Block

   Index der existierenden Meta Blocks
4. Index Block

   Index der existierenden Data Blocks
5. Footer

   Länge: 48 Bytes
   1. Metaindex Block Handle (16 Bytes)

      Gibt Position und Größe des Meta INdex Blocks an
      1. Offset (varint64)
      2. Size (varint64)
   2. Index Block Handle (16 Bytes)

      Gibt Position und Größe des Index Blocks an
      1. Offset (varint64)
      2. Size (varint64)
   3. Reserviert - noch ohne Nutzen (8 Bytes)
   4. Magic Number (8 Bytes)
      1. 0xdb4775248b80fb57

Die Index Blöcke dienen dem schnellen Finden von Einträgen sind aber zum Lesen/Dumpen aller Einträge nicht notwendig.

#### MANIFEST

Beinhaltet Info welche ldb-Dateien existieren und welche Keys in welchen ldb-Dateien zu finden sind.

### Vorgehen manuelle Analyse

#### Parsing log-Datei

1. Lese BLock (32 kB)
2. Parse Records aus Block

## Referenzen

2020-10: <https://www.cclsolutionsgroup.com/post/indexeddb-on-chromium>

2020-09: <https://www.cclsolutionsgroup.com/post/hang-on-thats-not-sqlite-chrome-electron-and-leveldb>

<https://github.com/chromium/chromium/blob/master/content/browser/indexed_db/docs/leveldb_coding_scheme.md>

## Tools

LevelDBtoSQLite - <https://github.com/SpyderForensics/Digital4n6withDamien/tree/main/LevelDBtoSQLite>

ccl_chromium_reader (storage_formats/ccl_leveldb.py) - <https://github.com/cclgroupltd/ccl_chromium_reader/>
