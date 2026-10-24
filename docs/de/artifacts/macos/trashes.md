---
title: "Trashes Folder"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [file-existence]
---

# Trashes Folder

## Bedeutung

Der Papierkorb (Trash) enthält Dateien und Ordner, die der Benutzer im Finder gelöscht hat. Bis zum Leeren des Papierkorbs kann der Benutzer sie mit „Zurücklegen“ (Put Back) wieder an ihren ursprünglichen Ort verschieben. Dafür speichert der Finder in der .DS_Store-Datei des Papierkorbs zu jedem Objekt den ursprünglichen Namen und Ablageort.

Aus digitalforensischer Sicht belegt ein Objekt im Papierkorb, dass es über das Benutzerkonto, dem der Papierkorb zugeordnet ist, in den Papierkorb verschoben wurde. Ein Put-Back-Eintrag belegt zusätzlich, unter welchem Namen und an welchem Ort das Objekt vorher lag. Ein Zeitpunkt des Löschens lässt sich daraus nicht ableiten.

## Spezifische Kurzinformation

1. Ursprünglicher Name und Ablageort stehen in der **`.DS_Store`** des Papierkorbs, nicht beim Objekt selbst
2. Es wird kein Löschzeitpunkt gespeichert
3. Der ursprüngliche Ablageort steht teils in der Firmlink-Form **`System/Volumes/Data/…`**
4. Put-Back-Einträge bleiben nach Zurücklegen oder Leeren des Papierkorbs bis zum Neustart erhalten (getestet bis macOS 10.12)
5. Zu Objekten im Papierkorb kann ein Put-Back-Eintrag fehlen (beobachtet unter macOS 15 und 26)
6. Mit „Sofort löschen“ werden Objekte ohne Umweg über den Papierkorb gelöscht
7. Optional automatisches Leeren nach 30 Tagen (Finder-Einstellung); gelöschte iCloud-Drive-Objekte werden immer nach 30 Tagen entfernt
8. Ablageort:  
   Auf Disk mit Home-Verzeichnis: **`/Users/{USER}/.Trash/`**  
   Auf allen anderen Disks: **`/.Trashes/{UID}/`**  
   iCloud Drive: **`/Users/{USER}/Library/Mobile Documents/com~apple~CloudDocs/.Trash/`**

## Referenzen

2026-10: <https://support.apple.com/guide/mac-help/delete-files-and-folders-on-mac-mchlp1093/26/mac> (abgerufen)

2019-07: <https://papers.put.as/papers/macosx/2019/summit_archive_1565288427.pdf>

2017-01: <https://ponderthebits.com/2017/01/mac-dumpster-diving-identifying-deleted-file-references-in-the-trash-ds_store-files-part-1/>

## Tools

DLEAPP (Parser: Trash Put Back) - <https://github.com/abrignoni/DLEAPP>

mac_apt (Plugin: TRASH) - <https://github.com/ydkhatri/mac_apt>

DSStoreParser - <https://github.com/nicoleibrahim/DSStoreParser>