---
title: "Makros"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Makros

Ein Makro ist eine Folge von Befehlen, die in einem Dokument oder einer Anwendung gespeichert ist und automatisch oder auf Aufruf ausgeführt wird.

Bekannt sind vor allem Makros in Microsoft-Office-Dokumenten, die in der Programmiersprache Visual Basic for Applications (VBA) geschrieben sind. Sie können z. B. beim Öffnen eines Dokuments starten und dabei auf Dateien, das Netzwerk und das Betriebssystem zugreifen. Dokumente mit Makros haben in den aktuellen Office-Formaten eigene Dateiendungen (z. B. `.docm`, `.xlsm`); bei den älteren Formaten (`.doc`, `.xls`) ist am Dateinamen nicht erkennbar, ob ein Makro enthalten ist. Daneben gibt es ältere Excel-4.0-Makros (XLM) und Makros in anderen Office-Paketen wie LibreOffice.

Aus digitalforensischer Sicht sind Makros ein verbreiteter Weg, Schadsoftware über E-Mail-Anhänge oder Downloads auf ein System zu bringen. Seit 2022 blockiert Microsoft Office Makros in Dateien aus dem Internet standardmäßig; die Herkunft erkennt Windows an einer Markierung, die beim Download in einem zusätzlichen Datenstrom der Datei abgelegt wird (Mark of the Web, Alternate Data Stream `Zone.Identifier`). Ob ein Makro ausgeführt wurde, lässt sich am Dokument selbst nicht erkennen, sondern nur über Spuren auf dem System, z. B. Einträge zu Dokumenten, bei denen der Benutzer die Inhalte aktiviert hat (Registry-Schlüssel `TrustRecords`), gestartete Prozesse oder nachgeladene Dateien. Der Makro-Code lässt sich mit Tools wie olevba (oletools) aus Dokumenten auslesen, ohne ihn auszuführen.
