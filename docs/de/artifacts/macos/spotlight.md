---
title: "Spotlight Datenbank"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [file-existence]
---

# Spotlight Datenbank

## Bedeutung

Spotlight ist die systemweite Suche von macOS. Damit der Benutzer Dateien schnell über Namen, Inhalt oder Eigenschaften findet, legt macOS für jedes indexierte Volume eine Datenbank mit den Metadaten und Textinhalten der Dateien an.

Aus digitalforensischer Sicht belegt ein Eintrag in der Spotlight-Datenbank, dass die Datei mit den gespeicherten Metadaten zum Zeitpunkt der Indexierung auf dem Volume vorhanden war. Einträge können auch nach dem Löschen der Datei noch vorhanden sein. Je nach Dateityp enthält ein Eintrag weitere Metadaten, z.B. zur Nutzung oder zur Herkunft eines Downloads; was diese belegen, hängt vom jeweiligen Attribut ab.

## Spezifische Kurzinformation

1. Nur auf indexierten Volumes vorhanden; einzelne Ordner und Volumes können über die Datenschutz-Einstellungen von Spotlight ausgeschlossen sein
2. Je Store zwei Datenbanken: **`.store.db`** (aktuell) und **`store.db`** (zeitverzögert aktualisierte Kopie)
3. Einträge gelöschter Dateien bleiben eine Zeit lang in **`store.db`** erhalten; gelöschte Datenbankseiten lassen sich aus dem freien Speicher wiederherstellen
4. Von Apple nicht dokumentiertes Format mit komprimierten Seiten
5. Nicht jedes Datumsfeld ist ein echter Zeitstempel, teils stehen Platzhalterwerte (z.B. Jahr 2247)
6. Ablageort:  
   **`/Volumes/{VOLUME}/.Spotlight-V100/Store-V2/{UUID}/`** (Root-Verzeichnis eines Laufwerks)  
   Startvolume ab macOS 10.15: **`/System/Volumes/Data/.Spotlight-V100/Store-V2/{UUID}/`**

## Referenzen

2026-07: <https://eclecticlight.co/2026/07/04/spotlight-and-core-spotlight-are-different/>

2024-01: <https://github.com/libyal/dtformats/blob/main/documentation/Apple%20Spotlight%20store%20database%20file%20format.asciidoc>

2021-10: <https://www.forensicfocus.com/webinars/shining-a-light-on-spotlight-leveraging-apples-desktop-search-utility-to-recover-deleted-file-metadata-on-macos/>

2019-07: <https://papers.put.as/papers/macosx/2019/summit_archive_1564171500.pdf>

2019-04: <https://doi.org/10.1016/j.diin.2019.01.019>

## Tools

DLEAPP (Parser: Spotlight Store Files) - <https://github.com/abrignoni/DLEAPP>

mac_apt (Plugin: SPOTLIGHT) - <https://github.com/ydkhatri/mac_apt>

spotlight_parser - <https://github.com/ydkhatri/spotlight_parser>
