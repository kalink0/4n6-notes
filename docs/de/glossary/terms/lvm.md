---
title: "LVM (Logical Volume Manager)"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
---

# LVM (Logical Volume Manager)

Der LVM (Logical Volume Manager) ist eine Speicherverwaltung unter Linux, die Datenträger oder Partitionen zu einem gemeinsamen Speicherpool zusammenfasst und daraus logische Laufwerke bereitstellt, die unabhängig von den Grenzen der Datenträger angelegt und in der Größe verändert werden können.

LVM arbeitet mit drei Ebenen:

- **Physical Volume (PV):** ein Datenträger oder eine Partition, die für LVM eingerichtet ist.
- **Volume Group (VG):** der Speicherpool aus einem oder mehreren Physical Volumes.
- **Logical Volume (LV):** ein logisches Laufwerk innerhalb einer Volume Group, das ein Dateisystem oder z. B. Swap enthält.

Ein Logical Volume kann über mehrere Physical Volumes verteilt sein, auch per Striping oder Mirroring. Zusätzlich unterstützt LVM Snapshots, die den Zustand eines Logical Volumes zu einem Zeitpunkt festhalten. Die Konfiguration wird als Text in einem Metadatenbereich am Anfang jedes Physical Volumes gespeichert. LVM wird häufig auf Linux-Servern und in Kombination mit einer LUKS-Verschlüsselung eingesetzt, wobei LVM dann innerhalb des entschlüsselten Containers liegt.

Aus digitalforensischer Sicht sind Logical Volumes nicht in der Partitionstabelle eingetragen; die Partition eines Physical Volumes enthält kein direkt lesbares Dateisystem. Das Analysetool muss LVM unterstützen oder die Volume Group muss vor der Analyse aus den Sicherungen aller zugehörigen Datenträger zusammengesetzt werden. Der Metadatenbereich enthält neben der aktuellen häufig auch ältere Fassungen der Konfiguration, aus denen sich gelöschte oder in der Größe veränderte Logical Volumes ableiten lassen. Snapshots können einen älteren Stand der Daten enthalten.
