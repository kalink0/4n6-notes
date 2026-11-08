---
title: "RAID"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
---

# RAID

RAID (Redundant Array of Independent Disks) bezeichnet den Verbund mehrerer Datenträger zu einem logischen Laufwerk, um die Ausfallsicherheit, die Geschwindigkeit oder beides zu erhöhen.

Wie die Daten auf die Datenträger verteilt werden, legt das RAID-Level fest. Die gebräuchlichsten sind:

- **RAID 0 (Striping):** Die Daten werden in Blöcken (Stripes) abwechselnd auf alle Datenträger verteilt. Es gibt keine Redundanz; fällt ein Datenträger aus, sind die Daten verloren.
- **RAID 1 (Mirroring):** Jeder Datenträger enthält eine vollständige Kopie der Daten.
- **RAID 5:** Striping mit Paritätsinformationen, die über alle Datenträger verteilt sind. Der Ausfall eines Datenträgers kann ausgeglichen werden.
- **RAID 6:** Wie RAID 5, aber mit doppelter Parität. Der Ausfall von zwei Datenträgern kann ausgeglichen werden.
- **RAID 10:** Kombination aus RAID 1 und RAID 0, d. h. Striping über gespiegelte Datenträgerpaare.

Ein RAID wird entweder von einem eigenen Controller (Hardware-RAID), vom Betriebssystem (Software-RAID, z. B. mdadm unter Linux oder Speicherplätze unter Windows) oder von der Firmware des Mainboards zusammen mit einem Treiber (Firmware-RAID, z. B. Intel RST) verwaltet. NAS-Systeme verwenden meist Software-RAID. Die Konfiguration, u. a. Level, Stripe-Größe und Reihenfolge der Datenträger, wird in Metadaten auf den Datenträgern oder im Controller gespeichert.

Aus digitalforensischer Sicht enthält ein einzelner Datenträger eines RAID 0, 5, 6 oder 10 nur Teile der Daten; ein lesbares Dateisystem ergibt sich erst aus dem Zusammenbau. Die Datenträger werden daher einzeln gesichert und das RAID anschließend aus den Sicherungen rekonstruiert. Dafür müssen Level, Stripe-Größe, Reihenfolge der Datenträger und bei RAID 5 und 6 die Anordnung der Parität bekannt sein oder aus den Daten ermittelt werden. Speichert ein Hardware-Controller die Konfiguration in einem eigenen Format, kann eine zusätzliche Sicherung des logischen Laufwerks über den Controller sinnvoll sein. Bei RAID 1 enthält jeder Datenträger die vollständigen Daten.
