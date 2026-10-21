---
title: "Swap File (Windows)"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
---

# Swap File (Windows)

Seit Windows 8 gibt es eine Swap File in Windows-Betriebssystemen. Sie hat eine ähnliche Funktion wie die Pagefile unter Windows und liegt als versteckte Systemdatei normalerweise im Root-Verzeichnis der Systemfestplatte mit dem Namen *swapfile.sys*.

Diese Datei dient speziell der performanten Auslagerung von Daten der sogenannten UWP (Universal Windows Platform)-Anwendungen. Diese Anwendungen benutzen die neuesten Programmierschnittstellen und Libraries in Windows und sollen dem Nutzer ein einheitliches Benutzungserlebnis über alle Windows-Systeme bieten. Zumeist werden die UWP-Anwendungen über den Windows-Store verteilt.

Potentiell liegen in der Swap File Daten zu offenen Apps und deren Inhalt. Weitere Inhalte der Swap File sind abhängig von der Programmierung der Apps.