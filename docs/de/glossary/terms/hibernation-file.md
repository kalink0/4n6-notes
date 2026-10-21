---
title: "Hibernation File"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
---

# Hibernation File

Die Hibernation File existiert in MS-Windows-Systemen. Es ist eine versteckte Systemdatei, normalerweise im Root-Verzeichnis der Systemfestplatte mit dem Namen *hiberfil.sys*.

Die Datei dient dazu, den Inhalt des Arbeitsspeichers beim Übergang in den Ruhezustand (Hibernation) auf der Festplatte zu speichern. Dies ermöglicht beim Wiedereinschalten des Systems den System- und Anwendungsstatus für den Nutzer schnell wiederherzustellen.

Potentiell befinden sich in der Datei Informationen zu geöffneten Programmen, auch Browser-Tabs einer Inkognito-Sitzung können enthalten sein, laufende Prozesse und Services und zum Beispiel nicht gespeicherte Dokumente.