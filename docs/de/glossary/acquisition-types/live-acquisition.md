---
title: "Live-Sicherung"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Live-Sicherung

Bei einer Live-Sicherung werden Daten von einem laufenden System gesichert, ohne es vorher auszuschalten.

Gesichert werden je nach Ziel einzelne Dateien, ganze Datenträger bzw. Volumes oder der Arbeitsspeicher. Die Sicherung erfolgt über das laufende Betriebssystem, z. B. mit einem Sicherungsprogramm, das von einem externen Datenträger gestartet wird.

Aus digitalforensischer Sicht ermöglicht eine Live-Sicherung den Zugriff auf Daten, die nach dem Ausschalten nicht mehr zugänglich wären, z. B. Inhalte entsperrter verschlüsselter Volumes, angemeldete Online-Dienste oder der Inhalt des Arbeitsspeichers. Jede Handlung am laufenden System verändert dieses, und die Daten ändern sich während der Sicherung weiter. Eine Live-Sicherung kann daher nicht wiederholt und ihr Hash-Wert nicht später am Original überprüft werden. Die durchgeführten Schritte werden deshalb genau dokumentiert.
