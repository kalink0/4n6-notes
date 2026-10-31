---
title: "Write-Blocker"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Write-Blocker

Ein Write-Blocker ist ein Gerät oder eine Software, die lesenden Zugriff auf einen Datenträger erlaubt, schreibende Zugriffe aber verhindert.

Hardware-Write-Blocker werden zwischen Datenträger und Analysesystem geschaltet und lassen nur Lesebefehle durch. Software-Write-Blocker setzen die Schreibsperre im Betriebssystem des Analysesystems um.

Aus digitalforensischer Sicht verhindert ein Write-Blocker, dass ein Datenträger bei der Sicherung verändert wird, z. B. durch das automatische Einbinden durch das Betriebssystem, das Metadaten oder Journale schreiben kann. Interne Vorgänge eines SSD-Controllers (z. B. Garbage Collection) kann ein Write-Blocker nicht verhindern.
