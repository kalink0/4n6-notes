---
title: "Datenwiederherstellung"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
---

# Datenwiederherstellung

Datenwiederherstellung bezeichnet das Zurückgewinnen von Daten, die gelöscht wurden, beschädigt sind oder auf normalem Weg nicht mehr zugänglich sind.

Welches Verfahren möglich ist, hängt davon ab, auf welcher Ebene die Daten gelöscht wurden bzw. was beschädigt ist; häufige Verfahren sind z. B.:

- **Über die Metadaten des Dateisystems:** Ist der Eintrag einer gelöschten Datei noch vorhanden, lässt sich die Datei mit Name, Pfad und Zeitstempeln wiederherstellen, solange ihr Speicherplatz nicht neu belegt wurde.
- **Per Carving:** Ohne Dateisystem-Metadaten werden Dateien anhand ihrer Dateisignaturen im nicht zugeordneten Speicher gesucht. Name, Pfad und Zeitstempel sind dabei nicht bekannt.
- **Aus Datenbanken:** Gelöschte Datensätze werden aus freien Bereichen der Datenbankdatei oder aus Journal- bzw. WAL-Dateien rekonstruiert.
- **Aus älteren Ständen:** Snapshots, Schattenkopien, Backups oder synchronisierte Cloud-Daten können einen Stand vor dem Löschen enthalten.
- **Von beschädigten Datenträgern (Datenrettung):** Bei defekter Hardware wird der Datenträger repariert oder der Speicherchip direkt ausgelesen, bei beschädigten Dateisystemen werden deren Strukturen rekonstruiert.

Nicht wiederherstellbar sind Daten, die überschrieben wurden, deren Speicherbereiche der Controller eines Flash-Speichers nach einem TRIM-Befehl gelöscht hat oder deren Schlüssel bei einer Verschlüsselung vernichtet wurde. Auf aktuellen Smartphones wird jede Datei mit einem eigenen Schlüssel verschlüsselt, der beim Löschen der Datei mit gelöscht wird; Carving liefert dort daher in der Regel keine verwertbaren Dateien.

Aus digitalforensischer Sicht hängt der Aussagewert wiederhergestellter Daten vom Verfahren ab: Über die Dateisystem-Metadaten wiederhergestellte Dateien sind einem Pfad und Zeitstempeln zugeordnet, per Carving gefundene nicht. Wiederhergestellte Daten können unvollständig sein oder teilweise aus anderen, später geschriebenen Daten bestehen, wenn ihr Speicherplatz bereits neu belegt wurde. Das verwendete Verfahren ist daher zu dokumentieren.
