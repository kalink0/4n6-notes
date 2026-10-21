---
title: "Realm Datenbanken"
status: draft
---

# Realm Datenbanken

## Bedeutung

*Noch kein Inhalt.*

## Spezifische Kurzinformation

*Noch kein Inhalt.*

## REALM DB Dateistruktur

Quelle: „Mobile Forensics – The File Format Handbook“, Kapitel 8 (Cobley/Geneste 2022)

---

### 1. Datei-Header (24 Byte) – vollständig geparst, als korrekt bestätigt

Die Struktur ist in `alloc_slab.hpp` definiert (Quellcode von Realm Core):

```
Offset  Größe Feld             Hinweise
0x00     8    m_top_ref[0]     little-endian uint64 – Datei-Offset des Root-Arrays A
0x08     8    m_top_ref[1]     little-endian uint64 – Datei-Offset des Root-Arrays B
0x10     4    m_mnemonic       ASCII "T-DB" (0x54 2D 44 42); Magic Value
0x14     2    m_file_format    Version des Dateiformats; in der Praxis 0x18 (=24) gesehen
0x16     1    m_reserved       zum Zeitpunkt der Erstellung immer 0x00
0x17     1    m_flags          Bit 0 (LSB): 0 = top_ref[0] aktiv, 1 = top_ref[1] aktiv
                               Bits 1–7: zum Zeitpunkt der Erstellung ungenutzt
```

**Vergleich mit Journaling / WAL**: Die beiden top_refs entsprechen in Realm dem WAL von SQLite.  
Der „aktuelle“ (lesekonsistente) Zweig ist der, den Bit 0 der Flags auswählt. Alle Schreibvorgänge  
gehen in den *anderen* Zweig. Checkpoint = Umschalten des Flags.

---

### 2. Realm Arrays – die einzige Struktur nach dem Header

Nach dem 24-Byte-Header besteht die Datei **ausschließlich** aus Realm Arrays, die als B+-Baum
angeordnet sind. Es gibt zwei Arten:

| Typ             | has_refs | Rolle                                        |
|-----------------|----------|----------------------------------------------|
| Reference Array | 1        | Verzweigungsknoten – Payload = Datei-Offsets |
| Data Array      | 0        | Blattknoten – Payload = eigentliche Werte    |

Arrays beginnen mit einem festen **8-Byte-Header**, gefolgt von einer Payload variabler Länge.
Aufeinanderfolgende Arrays lassen sich finden, indem man nach dem 4-Byte-Prüfsummenmuster `AAAA`
(0x41414141) sucht.

---

### 3. Array-Header (8 Byte)

```
Offset  Größe Feld             Hinweise
0x00     4    checksum         immer 0x41414141 ("AAAA") – Platzhalter, kann sich künftig ändern
0x04     1    flags            siehe Tabelle der Bitgruppen unten
0x05     3    size             big-endian uint24 – Anzahl der *Elemente* in der Payload
```

#### 3a. Flags-Byte – Bitgruppen (MSB = Bit 7)

```
Bit(s)  Maske Name                 Werte / Bedeutung
7       0x80  is_inner_bptree_node 1 = innerer Knoten des B+-Baums; setzt immer auch has_refs
6       0x40  has_refs             1 = Reference Array (Payload = Datei-Offsets der Kindknoten)
                                   0 = Data Array (Payload = eigentliche Datenwerte)
5       0x20  context_flag         Zweck unklar, selten gesetzt; kann den Typ des Blattknotens kennzeichnen
[4:3]   0x18  width_scheme         2-Bit-Wert 0–2; wählt die Formel für die Payload-Größe (siehe unten)
[2:0]   0x07  width_ndx            3-Bit-Index 0–7 in die Umrechnungstabelle für width (siehe unten)
```

#### 3b. Umrechnungstabelle width_ndx → width

```
width_ndx  : 	0   1   2   3   4    5    6    7
width      :  0   1   2   4   8   16   32   64
```

„width“ = Größe eines Elements (bei Schema 0 in Bit, bei Schema 1 in Byte).

#### 3c. Formel width_scheme → Anzahl der Payload-Bytes

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

### 4. Inhalte

#### 4.1 Datenbanken

*Noch kein Inhalt.*

#### 4.2 Parameter

*Noch kein Inhalt.*

#### 4.3 Objekte

*Noch kein Inhalt.*

## Referenzen

2026-01: <https://digital4n6withdamien.blogspot.com/2026/01/the-realm-files-vol-3-realm-header.html>

2025-11: <https://digital4n6withdamien.blogspot.com/2025/11/the-realm-files-vol-2-physical.html>

2025-09: <https://digital4n6withdamien.blogspot.com/2025/09/the-realm-files-vol-1-intro-to-realmdb.html>

2022: [Cobley, Geneste: Realm, in Mobile Forensics – The File Format Handbook (Springer, 2022)](https://doi.org/10.1007/978-3-030-98467-0_8)

## Tools

realm-studio - <https://github.com/realm/realm-studio>
