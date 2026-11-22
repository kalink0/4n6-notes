---
title: "AppImage"
status: complete
completed: 2026-11-22
authors: [kalink0 (Marco Neumann)]
---

# AppImage

AppImage ist ein Format, in dem ein Linux-Programm mit allen benötigten Bibliotheken in einer einzigen ausführbaren Datei steckt, die ohne Installation direkt gestartet wird.

Die Datei besteht aus einer Laufzeit (Runtime), dem ausführbaren Teil, und einem angehängten Dateisystem-Abbild (SquashFS). Beim Start hängt die Laufzeit das Abbild über FUSE schreibgeschützt in einen temporären Ordner ein, solange das Programm läuft. AppImages werden nicht über eine Paketverwaltung verwaltet; die Datei kann an beliebiger Stelle liegen, z. B. im Download-Ordner.

Aus digitalforensischer Sicht erscheint ein AppImage nicht in der Paketverwaltung; das Programm ist nur über die Datei selbst nachweisbar. Anders als Snap und Flatpak läuft es nicht in einer Sandbox und schreibt seine Daten an die üblichen Orte im Benutzerordner. Der Einhängeordner besteht nur, solange das Programm läuft; sein Name enthält die ersten sechs Zeichen des Dateinamens und sechs zufällige Zeichen.

- Einhängeordner während der Ausführung: **`/tmp/.mount_{NAME}XXXXXX`** (bzw. unter `$TMPDIR`, falls gesetzt)
