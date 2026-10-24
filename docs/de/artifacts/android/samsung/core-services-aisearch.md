---
title: "Samsung Core Services - AISearch"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [file-existence]
---

# Samsung Core Services - AISearch

## Bedeutung

Samsung Core Services (com.samsung.android.scs) ist eine Systemkomponente ohne eigene Oberfläche, die Grundfunktionen für Samsung-Apps bereitstellt. Das Modul AI Search indexiert Inhalte auf dem Gerät, damit sie über die Suche auffindbar sind. Dafür extrahiert es den Text von Dokumenten und speichert ihn.

Aus digitalforensischer Sicht belegt eine Textdatei im Index, dass ein Dokument mit dem angegebenen Dateinamen und diesem Textinhalt für den angegebenen Benutzer auf dem Gerät vorhanden war und indexiert wurde.

## Spezifische Kurzinformation

1. Der extrahierte Volltext liegt je Dokument als Textdatei in **`raw_txt/`**, nachgewiesen für PDF-Dateien
2. Dateiname der Textdatei: **`{USER_ID}_{FILE_ID}_{FILE_NAME}.txt`**; Benutzer-ID 0 = Hauptnutzer, 150 = Sicherer Ordner
3. Gespeichert wird nur der Dateiname zum Zeitpunkt der Indexierung, nicht der ursprüngliche Ablageort
4. Der Text gelöschter Dokumente bleibt erhalten (beobachtet ca. 2 Wochen nach Löschung)
5. Der Zeitstempel der Textdatei entspricht ungefähr dem Zeitpunkt der Indexierung, nicht der Erstellung des Originals
6. Ablageort:  
   **`/data/data/com.samsung.android.scs/files/aisearch/`**

## Referenzen

2025-12: <https://bebinary4n6.blogspot.com/2025/12/samsung-core-services-module-ai-search.html>

## Tools

*Noch kein Inhalt.*