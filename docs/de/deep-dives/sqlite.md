---
title: "SQLite Datenbanken"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
---

# SQLite Datenbanken

## Beschreibung

SQLite ist ein relationales "Single-File"-Datenbanksystem in Form einer eingebetteten, serverlosen Bibliothek. Es wird häufig von Applikationen (z. B. Web Browser und Messenger) zum Speichern von Daten verwendet.

Die Sprache zur Definition und Abfrage ist SQL. SQLite implementiert dabei einen eigenen Dialekt mit einigen Abweichungen vom Standard (z. B. dynamische Typisierung / Type Affinity, eingeschränktes `ALTER TABLE`).

## Spezifische Kurzinformation

### Dateitypen/Komponenten

#### Datenbankdatei

Die Datenbankdatei enthält sowohl das Schema der Datenbank als auch einen Großteil der aktiven Daten (weitere Daten liegen ggf. in Rollback Journals oder der WAL).

Die Datenbankdatei besteht aus Tabellen und Indizes, welche als B-Trees organisiert sind (Tabellen als B+-Trees, d. h. die eigentlichen Daten liegen nur in den Leaf-Pages; Indizes als B-Trees). Ein B-Tree ist kein Binärbaum. Die kleinste Einheit ist die Page. Die Page-Größe ist eine Zweierpotenz zwischen 512 und 65536 Bytes; seit SQLite 3.12.0 (2016) ist der Default 4096 Bytes, ältere Datenbanken verwenden häufig 1024 Bytes. Eine B-Tree-Page beinhaltet immer nur Daten aus einer Tabelle oder einem Index. Eine Tabelle/ein Index kann aber auf mehrere Pages verteilt sein.

Die erste Page enthält einen 100 Byte Header mit Informationen zur Datenbank. Unter anderem folgende Informationen können dem Header entnommen werden:

- Format-Signatur "SQLite format 3\0" (Offset 0) – dies ist keine Versionsangabe
- SQLite-Version, die zuletzt in die Datei geschrieben hat (Offset 96)
- Page-Größe (Offset 16)
- Nutzung von Rollback Journal oder WAL (Offset 18/19: 1 = Legacy/Rollback Journal, 2 = WAL)
- File Change Counter (Offset 24)
- Größe der Datenbank in Pages (Offset 28; nur gültig, wenn der Wert an Offset 92 dem File Change Counter entspricht)
- Erste Freelist-Trunk-Page (Offset 32) und Anzahl der Freelist-Pages (Offset 36)
- Auto-Vacuum-Einstellung (Offset 52/64)
- Encoding (Offset 56)
- user_version (Offset 60) und application_id (Offset 68) – können bei der Zuordnung zu einer Applikation helfen

Zusätzlich liegt auf der ersten Page immer die Root-Page der Tabelle `sqlite_master` (seit 3.33.0 auch `sqlite_schema` genannt). Bei umfangreichen Schemata ist sie selbst ein B-Tree über mehrere Pages. Sie enthält das Schema der Datenbank, die Root-Pages pro Tabelle und Index und die Definitionen von Views und Triggern.

Neben den B-Tree-Pages können weitere Page-Typen existieren:

- Overflow-Pages: Fortsetzung von Datensätzen, die nicht in eine Page passen
- Freelist-Pages (Trunk- und Leaf-Pages): Pages, die nicht mehr Teil der aktuellen B-Tree-Struktur sind, z. B. weil sie durch Löschen leer geworden sind oder eine Tabelle/ein Index gelöscht wurde
- Pointer-Map-Pages: nur bei aktiviertem auto_vacuum
- Lock-Byte-Page: nur bei Datenbanken größer als 1 GiB

##### Forensischer Nutzen

Die Datenbankdatei enthält das Schema und dient somit der Interpretation der Daten. Im WAL-Modus können aktuelle Daten noch ausschließlich in der WAL liegen – die Datenbankdatei allein zeigt dann nicht zwingend den aktuellen Stand.

Gelöschte Einträge lassen sich ggf. aus der Datenbankdatei selbst rekonstruieren:

- Freeblocks innerhalb einer Page: Die ersten 4 Bytes einer gelöschten Zelle werden durch den Freeblock-Header überschrieben, dadurch fehlt meist der Anfang des Datensatzes (Payload-Länge, rowid, Teile des Record-Headers).
- Unallozierter Bereich innerhalb einer Page (zwischen Cell-Pointer-Array und Cell-Content-Area)
- Freelist-Pages

Voraussetzungen:

- `secure_delete` = OFF: alle drei Quellen können Altdaten enthalten
- `secure_delete` = FAST (seit 3.20): Altdaten in B-Tree-Pages werden überschrieben, Freelist-Pages bleiben jedoch unangetastet
- `secure_delete` = ON: Altdaten werden überschrieben
- Für Freelist-Pages zusätzlich: `auto_vacuum` != FULL (bei FULL werden Freelist-Pages beim Commit abgeschnitten) und kein manuelles `VACUUM` (baut die Datei komplett neu auf)

Die Schwierigkeit der Interpretation liegt darin, dass bei Freelist-Pages eine sichere Zuordnung zur ursprünglichen Tabelle möglich sein muss, da die Page nicht mehr Teil der B-Tree-Struktur ist. Hierfür sind Inhalt und Struktur (z. B. Anzahl und Typen der Spalten im Record-Header) zu betrachten.

Bei Tabellen mit `AUTOINCREMENT` speichert `sqlite_sequence` die höchste je vergebene rowid. Ist dieser Wert größer als die höchste vorhandene rowid oder weist die Tabelle Lücken in der rowid-Folge auf, deutet das auf gelöschte Einträge hin (Lücken können aber auch durch abgebrochene Transaktionen entstehen).

#### Rollback Journal

Ablageort:

- Selbes Verzeichnis wie Datenbankdatei
- Name identisch zu Datenbankdatei mit Suffix "-journal"

##### Funktionsweise

Das Rollback Journal dient dazu, die Integrität der Datenbank bei z. B. einem Systemabsturz sicherzustellen. Um dies zu erreichen wird exemplarisch wie folgt vorgegangen:

1. Der Originalinhalt der Page, die geändert/gelöscht werden soll, wird aus der Datenbank in das Journal kopiert, und das Journal wird auf den Datenträger geschrieben.
2. Die Änderung/Löschung wird in die Datenbank geschrieben.
3. Commit: Das Journal wird ungültig gemacht (je nach Journal-Mode DELETE/TRUNCATE/PERSIST, s. u.). Damit ist klar, dass die Änderung vollständig geschrieben wurde.

Ein Journal, das nach einem Absturz oder Abbruch noch gültig vorliegt und beim nächsten Öffnen zurückgespielt werden muss, wird als "Hot Journal" bezeichnet.

##### Forensischer Nutzen

Das Journal enthält die Page-Inhalte vor der Änderung. Was davon nach dem Commit erhalten bleibt, hängt vom Journal-Mode ab:

- DELETE (Default): Die Journal-Datei wird gelöscht.
- TRUNCATE: Die Journal-Datei wird auf 0 Bytes gekürzt.
- PERSIST: Nur der Journal-Header (inkl. Magic) wird mit Nullen überschrieben. Die Pages bleiben in der Datei erhalten (ggf. begrenzt durch `journal_size_limit`).

Bei DELETE und TRUNCATE sind die Daten nicht mehr alloziert. Eine Wiederherstellung ist nur über das Dateisystem möglich. Bei PERSIST lassen sich die Daten unabhängig vom Dateisystem direkt aus dem Journal auslesen.

So lassen sich ggf. frühere Datenbankstände rekonstruieren.

#### Rollback Master Journal (Super-Journal)

Seit SQLite 3.33.0 (2020) offiziell als "Super-Journal" bezeichnet.

Das Super-Journal dient der Organisation, wenn mehrere Datenbanken (verbunden über `ATTACH`) innerhalb einer Transaktion geändert werden. Es wird nur verwendet, wenn die Datenbanken nicht im WAL-Modus betrieben werden.

Ablageort:

- Selbes Verzeichnis wie die Hauptdatenbank
- Name identisch zur Hauptdatenbank mit Suffix "-mj" + 9 Hex-Zeichen (laut SQLite-Quellcode ist das 7. Zeichen dabei immer "9")

##### Funktionsweise

Das Super-Journal enthält die Pfade aller beteiligten Rollback Journals, jeweils durch ein NUL-Byte getrennt. Jedes beteiligte Rollback Journal enthält umgekehrt am Ende den Namen des Super-Journals. Nach erfolgreichem Commit wird das Super-Journal gelöscht.

##### Forensischer Nutzen

Wenn ein Super-Journal existiert, weiß man, dass eine datenbankübergreifende Transaktion nicht abgeschlossen wurde. Anhand des Inhalts kann gesagt werden, auf welche Datenbanken sich die Änderungen beziehen. In den jeweiligen Rollback Journals der Datenbanken kann dann geschaut werden, welche Änderungen durchgeführt werden sollten.

#### Write-Ahead Log (WAL)

Ablageort:

- Selbes Verzeichnis wie Datenbankdatei
- Name identisch zu Datenbankdatei mit Suffix "-wal"

##### Funktionsweise

Das Write-Ahead Log hat dasselbe Ziel wie das Rollback Journal, arbeitet aber andersherum: Änderungen werden nicht direkt in die Datenbank geschrieben, sondern zunächst als vollständige Page-Kopien an die WAL angehängt.

Die WAL besteht aus einem 32 Byte Header (u. a. mit zwei Salt-Werten) und Frames. Jeder Frame besteht aus einem 24 Byte Frame-Header und einer vollständigen Page. Ein Frame, der eine Transaktion abschließt (Commit-Frame), ist daran erkennbar, dass das Feld für die Datenbankgröße im Frame-Header ungleich 0 ist.

1. Zu ändernde/löschende/hinzufügende Pages werden als Frames in die WAL geschrieben.
2. Die Transaktion wird in der WAL bestätigt (Commit-Frame).
3. Weitere Pages werden geändert/gelöscht/hinzugefügt.
4. Die Transaktion wird in der WAL bestätigt (Commit-Frame).
5. Beim Checkpoint werden die Änderungen in die Datenbankdatei übertragen. Auslöser sind:
   1. Automatisch, sobald die WAL 1000 Frames erreicht (Default, `wal_autocheckpoint`). Der Checkpoint wird beim Commit ausgeführt, der diese Grenze überschreitet.
   2. Explizit über `PRAGMA wal_checkpoint` bzw. die entsprechende API-Funktion.
   3. Beim sauberen Schließen der letzten Datenbankverbindung. Die WAL wird dabei in der Regel gelöscht (Ausnahme: persistente WAL). Ein Absturz oder das Abschießen der App löst keinen Checkpoint aus; die WAL bleibt dann bestehen und wird beim nächsten Öffnen berücksichtigt.

Nach einem vollständigen Checkpoint wird die WAL beim nächsten Schreibvorgang von vorne neu beschrieben. Dabei werden im WAL-Header neue Salt-Werte gesetzt. Die Datei wird standardmäßig nicht gekürzt (Ausnahme: `journal_size_limit` ist gesetzt).

##### Forensischer Nutzen

Solange die WAL existiert, bleiben ältere Frames nach einem Checkpoint in der Datei erhalten, bis sie überschrieben werden. Frames, deren Salt-Werte nicht zum aktuellen WAL-Header passen, stammen aus früheren Durchläufen. Wurde die WAL gelöscht (sauberes Schließen), ist eine Wiederherstellung nur noch über das Dateisystem möglich.

Ältere Frames enthalten ältere Versionen einer Page. Alte Datenbankstände lassen sich daher auch rekonstruieren, wenn `secure_delete` aktiv ist.

Die WAL kann sogar Einträge enthalten, die nie in der Datenbankdatei standen. Beispiel: Eine Nachricht geht ein und wird vor dem nächsten Checkpoint gelöscht.

Zeitleisten lassen sich nur rekonstruieren, wenn die Daten selbst Zeitstempel enthalten.

#### Shared Memory File (shm)

Ablageort:

- Selbes Verzeichnis wie Datenbankdatei
- Name identisch zu Datenbankdatei mit Suffix "-shm"

##### Funktionsweise

Dient als Index (wal-index) der Frames in der WAL, um schneller die letzte gültige Version einer Page zu finden. Ein neuer Frame in der WAL führt zu einem neuen Eintrag in der shm. Die shm ist nicht absturzsicher, liegt in der nativen Byte-Order des Systems vor und kann jederzeit aus der WAL neu aufgebaut werden. Im Modus `locking_mode=EXCLUSIVE` wird keine shm-Datei angelegt.

##### Forensischer Nutzen

Der forensische Nutzen ist gering, da die Index-Daten der shm auch aus der WAL gewonnen werden können und die shm nur so lange existiert wie die WAL. Hilfreich sind die Werte `mxFrame` (letzter gültiger Frame) und `nBackfill` (bis zu welchem Frame bereits ein Checkpoint erfolgt ist), um einzuordnen, welche Frames aktuell sind.

## Checkliste Analyse

- [ ] **Sicherung:** Datenbankdatei, `-wal`, `-shm` und `-journal` gemeinsam sichern.
- [ ] **Nur an Kopien arbeiten.**
- [ ] **Begleitdateien und Header prüfen:** Welche Dateien existieren (Größe, Zeitstempel)? Page-Größe, Journal-/WAL-Nutzung und Anzahl Freelist-Pages aus dem Header auslesen.
- [ ] **Schema auswerten:** Tabellen, Indizes, Views und Trigger in `sqlite_master` prüfen, um zu verstehen, wo welche Daten landen.
- [ ] **Stand DB vs. DB+WAL vergleichen:** je eine Kopie ohne und mit WAL öffnen.
  - Fallstrick: Der Vergleich zeigt nur die Unterschiede der Endstände. Zwischenstände innerhalb der WAL erfordern eine Auswertung der einzelnen Frames.
- [ ] **Altdaten prüfen:** Freeblocks, unallozierte Bereiche, Freelist-Pages, alte WAL-Frames, Journal-Pages. Normale SQL-Abfragen zeigen nur aktive Daten.

## Referenzen

2026-05: [beBinary: What Hides in the WAL – SQLite Forensics with crush](https://bebinary4n6.blogspot.com/2026/05/what-hides-in-wal-sqlite-forensics-with.html)

2025: [Lee et al.: Survey zu Techniken der Wiederherstellung gelöschter SQLite-Records (FSI: Digital Investigation)](https://www.sciencedirect.com/science/article/abs/pii/S2666281725001714)

2022: [Mobile Forensics – The File Format Handbook, Kapitel 5: SQLite (Springer, Open Access)](https://doi.org/10.1007/978-3-030-98467-0_5)

2021-07: [SANS/GIAC: Missing SQLite Records Analysis](https://www.sans.org/white-papers/40195)

2018: Umfangreiche Erklärungen zu Aufbau und interner Funktionsweise im Buch "SQLite Forensics" von Paul Sanderson - ISBN 9781980293071

2015-03: [Sanderson Forensics: Forensic examination of SQLite WAL files](https://sqliteforensictoolkit.com/forensic-examination-of-sqlite-write-ahead-log-wal-files/)

[Belkasoft: SQLite Forensics with Belkasoft X)](https://belkasoft.com/sqlite)

SQLite-Dokumentation:
- Dateiformat: <https://www.sqlite.org/fileformat2.html>
- WAL-Index und Locking: <https://www.sqlite.org/walformat.html>
- Journal-Modes: <https://www.sqlite.org/pragma.html#pragma_journal_mode>

crush Format Reference:
- <https://kalink0.github.io/crush-forensics/formats/de/sqlite/>
- <https://kalink0.github.io/crush-forensics/formats/de/sqlite-journal/>
- <https://kalink0.github.io/crush-forensics/formats/de/sqlite-wal/>

## Tools

crush - <https://github.com/kalink0/crush-forensics>

DB Browser for SQLite - <https://sqlitebrowser.org/>

DBeaver Community - <https://dbeaver.io/>

fqlite - <https://github.com/pawlaszczyk/fqlite>

SQBite - <https://github.com/SpyderForensics/SQLite_Forensics/tree/main/SQBite>

sqlite-dissect - <https://github.com/dod-cyber-crime-center/sqlite-dissect>

sqlite-gui-analyzer - <https://github.com/akhil-dara/sqlite-gui-analyzer>
