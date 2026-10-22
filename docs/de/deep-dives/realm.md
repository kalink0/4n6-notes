---
title: "Realm Datenbanken"
status: complete
completed: 2026-10-22
authors: [kalink0 (Marco Neumann)]
---

# Realm Datenbanken

## Bedeutung

### Technische Beschreibung:

Realm ist eine objektorientierte Datenbank für mobile Apps, die als Alternative zu SQLite eingesetzt wird. Daten werden als Objekte mit Eigenschaften gespeichert, nicht als Zeilen in Tabellen. Eine Datenbank besteht aus einer einzelnen Datei, separate Journal- oder WAL-Dateien gibt es nicht. Forensisch relevant ist, dass die Datei neben dem aktuellen Stand auch den Stand vor dem letzten Commit und Reste älterer Daten enthalten kann.

### Nicht-technische Beschreibung:

Realm ist ein Datenspeicher, den manche Apps statt der üblichen SQLite-Datenbank nutzen. Darin legt die App ihre Daten ab, zum Beispiel Nutzerdaten, Inhalte oder Einstellungen. Für eine Untersuchung kann dieser Speicher zeigen, welche Daten die App gespeichert hat und was sich zuletzt daran geändert hat.

## Spezifische Kurzinformation

### Komponenten

Ablageort:

- Im Datenverzeichnis der jeweiligen App, Dateiendung meist `.realm`

#### Datei-Header (24 Byte)

##### Funktionsweise

```
Offset  Größe Feld             Hinweise
0x00     8    m_top_ref[0]     little-endian uint64 – Datei-Offset des Root-Arrays A
0x08     8    m_top_ref[1]     little-endian uint64 – Datei-Offset des Root-Arrays B
0x10     4    m_mnemonic       ASCII "T-DB" (0x54 2D 44 42); Magic Value
0x14     1    m_file_format[0] Version des Dateiformats für top_ref[0]; aktuell 24
0x15     1    m_file_format[1] Version des Dateiformats für top_ref[1]; aktuell 24
0x16     1    m_reserved       zum Zeitpunkt der Erstellung immer 0x00
0x17     1    m_flags          Bit 0 (LSB): 0 = top_ref[0] aktiv, 1 = top_ref[1] aktiv
                               Bits 1–7: zum Zeitpunkt der Erstellung ungenutzt
```

Realm arbeitet nach dem Copy-on-Write-Prinzip: Bei einem Commit werden geänderte Arrays nicht überschrieben, sondern an freie Stellen neu geschrieben. Danach zeigt der inaktive Top Ref auf den neuen Stand und das Flag wird umgeschaltet. Der bisher aktive Top Ref bleibt als Stand vor dem letzten Commit erhalten.

##### Forensischer Nutzen

Das Flag zeigt, welcher Top Ref den aktuellen Stand enthält. Der andere Top Ref enthält den Stand vor dem letzten Commit. Durch den Vergleich beider Stände lassen sich Objekte erkennen, die bei der letzten Transaktion gelöscht oder geändert wurden.

Unterschiedliche File-Format-Werte der beiden Top Refs zeigen, dass beim letzten Commit ein Format-Upgrade stattfand.

#### Realm Arrays

##### Funktionsweise

Nach dem 24-Byte-Header besteht die Datei aus Realm Arrays, die als B+-Baum angeordnet sind, und freien Bereichen. Es gibt zwei Arten von Arrays:

| Typ             | has_refs | Rolle                                        |
|-----------------|----------|----------------------------------------------|
| Reference Array | 1        | Verzweigungsknoten – Payload = Datei-Offsets |
| Data Array      | 0        | Blattknoten – Payload = eigentliche Werte    |

Arrays beginnen mit einem festen **8-Byte-Header**, gefolgt von einer Payload variabler Länge.
Aufeinanderfolgende Arrays lassen sich finden, indem man nach dem 4-Byte-Prüfsummenmuster `AAAA`
(0x41414141) sucht.

Array-Header (8 Byte):

```
Offset  Größe Feld             Hinweise
0x00     4    checksum         immer 0x41414141 ("AAAA") – Platzhalter, kann sich künftig ändern
0x04     1    flags            siehe Tabelle der Bitgruppen unten
0x05     3    size             big-endian uint24 – Anzahl der *Elemente* in der Payload
```

Flags-Byte – Bitgruppen (MSB = Bit 7):

```
Bit(s)  Maske Name                 Werte / Bedeutung
7       0x80  is_inner_bptree_node 1 = innerer Knoten des B+-Baums; setzt immer auch has_refs
6       0x40  has_refs             1 = Reference Array (Payload = Datei-Offsets der Kindknoten)
                                   0 = Data Array (Payload = eigentliche Datenwerte)
5       0x20  context_flag         Zweck unklar, selten gesetzt; kann den Typ des Blattknotens kennzeichnen
[4:3]   0x18  width_scheme         2-Bit-Wert 0–2; wählt die Formel für die Payload-Größe (siehe unten)
[2:0]   0x07  width_ndx            3-Bit-Index 0–7 in die Umrechnungstabelle für width (siehe unten)
```

Umrechnungstabelle width_ndx → width:

```
width_ndx  :  0   1   2   3   4    5    6    7
width      :  0   1   2   4   8   16   32   64
```

„width“ = Größe eines Elements (bei Schema 0 in Bit, bei Schema 1 in Byte).

Formel width_scheme → Anzahl der Payload-Bytes:

```
width_scheme  Bedeutung          Formel
0             Größe in Bit       payload_bytes = ceil(width × size / 8)
1             Größe in Byte      payload_bytes = width × size
2             width ignorieren   payload_bytes = size
```

Nach der Berechnung von `payload_bytes` **auf die nächste 8-Byte-Grenze aufrunden**:

```python
payload_bytes = (payload_bytes + 7) & ~7
```

Gesamtlänge des Arrays in Byte = 8 (Header) + payload_bytes_aligned.

#### Logischer Aufbau

##### Funktionsweise

Die Arrays bilden eine Hierarchie:

1. Group: oberster Knoten, auf den ein Top Ref zeigt
2. Tables: je eine pro Klasse des Schemas (Klassennamen mit Präfix `class_`)
3. Cluster Tree: B+-Baum je Tabelle
4. Clusters: Blätter des Cluster Trees, enthalten die eigentlichen Objektdaten

Verweise zwischen Objekten (Links) werden über ObjKeys gespeichert, die internen Kennungen der Objekte.

##### Forensischer Nutzen

Die Klassennamen im Schema zeigen, welche Arten von Daten die App speichert. Um Objektdaten einer Klasse und ihren Eigenschaften zuzuordnen, muss die Hierarchie vom Top Ref bis zu den Clusters durchlaufen werden.

#### Freie Bereiche

##### Funktionsweise

Bereiche, die zu keinem der beiden Top Refs gehören. Realm markiert sie als frei und verwendet sie bei späteren Commits wieder.

##### Forensischer Nutzen

Freie Bereiche können Reste älterer oder gelöschter Objekte enthalten, bis Realm sie wiederverwendet. Über das Muster `AAAA` lassen sich darin Arrays finden.

## Checkliste Analyse

1. Die Datei nie in Realm Studio oder mit der App am Original öffnen. Realm Studio aktualisiert ältere Dateien auf das aktuelle Format und schreibt dabei einen neuen Commit.
2. Signatur `T-DB` an Offset 16 prüfen.
3. Header auswerten: aktiven Top Ref über das Flag bestimmen, File-Format beider Top Refs vergleichen.
4. Aktiven Top Ref auswerten: Schema, Tabellen (Klassen), Objekte.
5. Inaktiven Top Ref auswerten und mit dem aktiven vergleichen.
6. Freie Bereiche nach Arrays durchsuchen.

## Referenzen

2026-05: [beBinary: Object by Object – RealmDB Forensics with crush](https://bebinary4n6.blogspot.com/2026/05/object-by-object-realmdb-forensics-with.html)

2026-01: [Damien Attoe: The Realm Files – Vol 3 – The Realm Header](https://digital4n6withdamien.blogspot.com/2026/01/the-realm-files-vol-3-realm-header.html)

2025-11: [Damien Attoe: The Realm Files – Vol 2 – Physical Structure Overview](https://digital4n6withdamien.blogspot.com/2025/11/the-realm-files-vol-2-physical.html)

2025-09: [Damien Attoe: The Realm Files – Vol 1 – Intro to RealmDB](https://digital4n6withdamien.blogspot.com/2025/09/the-realm-files-vol-1-intro-to-realmdb.html)

2022-05: [Cobley, Geneste: Realm – Mobile Forensics – The File Format Handbook, Kapitel 8 (Springer, Open Access)](https://doi.org/10.1007/978-3-030-98467-0_8)

2022: [Kim et al.: Methods for recovering deleted data from the Realm database (FSI: Digital Investigation)](https://www.sciencedirect.com/science/article/abs/pii/S2666281722000221)

2019-11: [Alexis Brignoni: Realm database storage primer for digital forensic examiners](https://abrignoni.blogspot.com/2019/11/realm-database-storage-primer-for.html)

crush Format Reference:
- <https://kalink0.github.io/crush-forensics/formats/realm/>

## Tools

crush - <https://github.com/kalink0/crush-forensics>

Realm Studio - <https://github.com/realm/realm-studio>