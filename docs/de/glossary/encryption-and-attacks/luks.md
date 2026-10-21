---
title: "LUKS"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
---

# LUKS

LUKS (Linux Unified Key Setup) ist ein Standardverfahren zur Festplattenverschlüsselung unter Linux. Es definiert ein plattformunabhängiges On-Disk-Format, das es ermöglicht, ganze Partitionen oder Container zu verschlüsseln.

Aus digitalforensischer Sicht kann gesagt werden, dass bei einem ausreichend komplexen Passwort keine bekannten Möglichkeiten bestehen, Zugriff auf die Daten innerhalb eines geschlossenen LUKS-Volumes ohne das Passwort zu erlangen.

Passwortangriffe, welche versuchen mittels Ausprobieren von Passwörtern Zugriff auf die Daten im LUKS-Volume zu erlangen, können je nach Komplexität des Passworts mehrere Jahrzehnte bis zum Erfolg benötigen.