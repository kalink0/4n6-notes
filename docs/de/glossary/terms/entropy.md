---
title: "Entropie"
status: complete
completed: 2026-10-31
authors: [kalink0 (Marco Neumann)]
---

# Entropie

Entropie ist ein Maß für die Zufälligkeit bzw. den Informationsgehalt von Daten.

In der digitalen Forensik wird meist die Shannon-Entropie in Bit pro Byte verwendet, mit Werten zwischen 0 (z. B. nur Nullbytes) und 8 (vollständig zufällige Daten). Klartext liegt meist bei etwa 4 bis 5, komprimierte und verschlüsselte Daten nahe 8. Berechnet wird sie für eine ganze Datei oder blockweise für Abschnitte eines Datenträgers.

Aus digitalforensischer Sicht weist eine hohe Entropie auf verschlüsselte oder komprimierte Daten hin. Die beiden lassen sich über die Entropie allein nicht unterscheiden; komprimierte Formate (z. B. ZIP, JPEG) haben jedoch meist eine Dateisignatur, verschlüsselte Container (z. B. VeraCrypt) nicht.
