---
title: "TRIM-Command"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
---

# TRIM-Command

Der TRIM-Command ist ein ATA-Befehl (vergleichbar mit dem UNMAP SCSI-Befehl bzw. Deallocate bei NVMe), welcher es dem Betriebssystem erlaubt, einer angeschlossenen SSD mitzuteilen, welche Speicherbereiche nicht mehr in Verwendung sind.

Der interne Controller der SSD markiert die freigegebenen Speicherbereiche als ungültig und löscht sie im Rahmen seiner internen Speicherverwaltung. Viele SSDs liefern bereits unmittelbar nach dem Befehl beim Lesen dieser Bereiche nur noch Nullen. Ziel ist es, die Schreibleistung und Lebensdauer der SSD zu erhalten.

Durch die Ausführung des Befehls ist eine nachträgliche Wiederherstellung gelöschter Dateien mittels regulärem Carving bei SSDs nicht erfolgversprechend.

Der TRIM-Command kann auch bei magnetischen Datenträgern zum Einsatz kommen, sogenannten SMR (Shingled Magnetic Recording)-Festplatten.