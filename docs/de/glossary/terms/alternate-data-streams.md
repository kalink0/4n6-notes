---
title: "Alternate Data Streams"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
---

# Alternate Data Streams

Alternate Data Streams (ADS) sind eine Funktion des NTFS-Dateisystems, die es ermöglicht, einer Datei neben ihrem eigentlichen Inhalt einen oder mehrere zusätzliche Datenströme beizufügen. Der Hauptdatenstrom enthält den sichtbaren Inhalt der Datei, zum Beispiel ein Word-Dokument und dessen Inhalt, während ADS zusätzliche Daten speichern können – beispielsweise Metadaten oder andere Informationen –, die für Standardanwendungen unsichtbar bleiben.

Diese versteckten Datenströme können über spezielle Kommandos und Tools erstellt und gelesen werden. ADS können sowohl für legitime Zwecke (z. B. zur Speicherung des Zone.Identifier bei heruntergeladenen Dateien) als auch für bösartige Zwecke (z. B. zum Verstecken von Malware) genutzt werden.