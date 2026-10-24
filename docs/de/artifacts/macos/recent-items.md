---
title: "Recent Items"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [file-access, program-execution, network]
---

# Recent Items

## Bedeutung

macOS führt pro Benutzer Listen der zuletzt verwendeten Programme, Dokumente und Server, z.B. im Apple-Menü unter „Benutzte Objekte“ und in Programmen unter „Zuletzt benutzt“. Darüber kann der Benutzer diese Objekte schnell erneut öffnen.

Aus digitalforensischer Sicht belegt ein Eintrag, dass über das Benutzerkonto das Dokument geöffnet, das Programm gestartet bzw. die Verbindung zum Server hergestellt wurde, und wo das Objekt zu diesem Zeitpunkt lag. Ein Zeitpunkt der Nutzung lässt sich daraus nicht ableiten.

## Spezifische Kurzinformation

1. Bis macOS 10.10 als plist-Dateien, ab macOS 10.11 als Shared File Lists (**`.sfl`**, ab 10.13 **`.sfl2`**, später **`.sfl3`** und **`.sfl4`**)
2. Ältere Shared-File-List-Dateien bleiben nach einem Upgrade erhalten, eine Liste kann daher unter mehreren Endungen vorliegen
3. Kein Zeitstempel der Nutzung; die Reihenfolge der Einträge gibt die Aktualität an
4. Die Listenlänge ist begrenzt, der älteste Eintrag fällt beim Überschreiten heraus
5. Das im Bookmark enthaltene Erstellungsdatum ist das der Zieldatei, nicht der Zeitpunkt der Nutzung
6. Listen einzelner Programme werden nur aktualisiert, wenn das Programm läuft, und können daher sehr alte Einträge enthalten
7. Ablageort:  
   Bis macOS 10.10: **`/Users/{USER}/Library/Preferences/com.apple.recentitems.plist`**  
   **`/Users/{USER}/Library/Preferences/*LSSharedFileList.plist`**  
   Ab macOS 10.11: **`/Users/{USER}/Library/Application Support/com.apple.sharedfilelist/`**  
   Ab macOS 10.11 (je Programm eine Liste): **`/Users/{USER}/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.ApplicationRecentDocuments/`**

## Referenzen

2023-08: <https://eclecticlight.co/2023/08/04/recent-items-property-lists-bookmarks-and-resolvers/>

2017-08: <https://eclecticlight.co/2017/08/10/recent-items-launch-services-and-sharedfilelists/>

2016-07: <https://www.mac4n6.com/blog/2016/7/10/new-script-macmru-most-recently-used-plist-parser>

## Tools

mac_apt (Plugin: RECENTITEMS) - <https://github.com/ydkhatri/mac_apt>

DLEAPP (Parser: Shared File Lists (sfl2, sfl3, sfl4)) - <https://github.com/abrignoni/DLEAPP>

macMRU-Parser - <https://github.com/mac4n6/macMRU-Parser>