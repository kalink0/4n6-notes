---
title: "Quick Look Cache"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [file-existence]
---

# Quick Look Cache

## Bedeutung

Quick Look erzeugt Vorschaubilder (Thumbnails) und Vorschauen von Dateiinhalten, z.B. für die Symbole im Finder oder die Vorschau mit der Leertaste, ohne dass die Datei in ihrem Programm geöffnet werden muss. Damit die Vorschaubilder nicht jedes Mal neu erzeugt werden müssen, speichert macOS sie pro Benutzer in einem Cache.

Aus digitalforensischer Sicht belegt ein Eintrag, dass die Datei vorhanden war und für sie ein Vorschaubild erzeugt wurde, z.B. weil ihr Ordner im Finder angezeigt wurde. Das Vorschaubild zeigt den Inhalt der Datei zum Zeitpunkt der Erstellung, auch wenn die Datei inzwischen gelöscht wurde oder auf einem nicht mehr verfügbaren Datenträger lag. Ein Eintrag belegt nicht, dass die Datei geöffnet wurde.

## Spezifische Kurzinformation

1. Der Cache liegt außerhalb des Home-Verzeichnisses; die Zuordnung zum Benutzer erfolgt über den Besitzer (UID) des Ordners
2. Bis macOS 10.14 mit Pfad und Dateiname, ab macOS 10.15 nur mit Datei-ID (Inode); die Zuordnung zur Datei ist dann nur über das Dateisystem möglich
3. Enthält auch Vorschaubilder von Dateien auf externen und verschlüsselten Volumes, die nicht mehr eingebunden sind (getestet unter macOS 10.13)
4. Gespeichertes Änderungsdatum und Dateigröße gehören zur Originaldatei, nicht zum Cache-Eintrag
5. Zeitstempel im Cocoa-Format (Sekunden seit 2001-01-01), UTC
6. Was als Zugriff (hit) gezählt wird, ist nicht geklärt
7. Ab macOS 10.14 vom System geschützt; am laufenden System nicht ohne Weiteres lesbar
8. Der Benutzer kann den Cache mit **`qlmanage -r cache`** leeren
9. Ablageort:  
   **`/private/var/folders/{XX}/{ID}/C/com.apple.QuickLook.thumbnailcache/`**

## Referenzen

2024-04: <https://eclecticlight.co/2024/04/05/a-quick-look-at-quicklook-and-its-problems/>

2018-06: <https://objective-see.org/blog/blog_0x30.html>

2018-06: <https://arsenalrecon.com/insights/quick-look-cache-parsing>

2016-05: <http://az4n6.blogspot.com/2016/05/quicklook-python-parser-all-your-blobs.html>

## Tools

mac_apt (Plugin: QUICKLOOK) - <https://github.com/ydkhatri/mac_apt>

DLEAPP (Parser: QuickLook Thumbnails) - <https://github.com/abrignoni/DLEAPP>

OSX-QuickLook-Parser - <https://github.com/mdegrazia/OSX-QuickLook-Parser> (nur bis macOS 10.14)