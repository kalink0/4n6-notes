---
title: "Biome"
status: complete
completed: 2026-10-22
authors: [kalink0 (Marco Neumann)]
topics: [device-state]
---

# Biome

## Bedeutung

Biome ist ein Framework von Apple, in dem macOS Informationen über die Nutzung des Geräts speichert, etwa App-Nutzung, Benachrichtigungen oder Medienwiedergabe. Daraus erstellt macOS Vorhersagen und Vorschläge, z.B. für Siri, proaktive Vorschläge und die Personalisierung des Systems. Seit macOS 13 hat Biome einen Großteil der Aufgaben von KnowledgeC übernommen. Die Daten sind in thematische Streams gegliedert, jeder Stream in einem eigenen Ordner mit Dateien im Format SEGB.

Aus digitalforensischer Sicht belegt ein Eintrag, dass macOS zum angegebenen Zeitpunkt das jeweilige Ereignis im betreffenden Stream erfasst hat; was das Ereignis über eine Nutzeraktion aussagt, hängt vom Stream ab. Einträge aus dem Unterordner remote stammen von anderen Geräten derselben Apple-ID und belegen nicht, dass das Ereignis auf dem untersuchten Gerät stattfand. Nicht belegt ist dagegen, dass ein Ereignis nicht stattfand, wenn kein Eintrag vorhanden ist.

## Spezifische Kurzinformation

1. Biome ist ab macOS 12 aktiv in Nutzung, als Hauptquelle anstelle von KnowledgeC ab macOS 13
2. Es gibt Streams je Benutzer und systemweite Streams; am laufenden System sind die restricted-Streams nur mit erhöhten Rechten lesbar
3. Format SEGB (v1 und v2); Dateien ohne Endung, benannt nach dem Erstellungszeitpunkt; Inhalte meist Protobuf ohne veröffentlichtes Schema
4. Zeitstempel im Format Mac Absolute Time (Sekunden seit 2001-01-01, UTC)
5. Jeder Stream hat die Unterordner local und remote (Daten anderer Geräte derselben Apple-ID, je Gerät ein Ordner); abgelaufene Dateien liegen in local/tombstone
6. Gelöschte Einträge behalten Zeitstempel und Status, ihr Inhalt ist leer
7. Die Geräte hinter remote sind in **`/Users/{USER}/Library/Biome/sync/sync.db`** verzeichnet
8. Neben streams gibt es den Ordner sets mit SQLite-Datenbanken, z.B. zu installierten Apps oder Kontakten
9. Ablageorte:  
   **`/Users/{USER}/Library/Biome/streams/public/`**  
   **`/Users/{USER}/Library/Biome/streams/restricted/`**  
   **`/private/var/db/biome/streams/`**

## Referenzen

2026-06: <https://unit42.paloaltonetworks.com/new-macos-artifact-discovered/>

2023-10: <https://cellebrite.com/en/understanding-and-decoding-the-newest-ios-segb-format/>

2022-06: <https://eclecticlight.co/2022/06/27/biome-isnt-about-biometrics-but-suggestions/>

## Tools

ccl-segb - <https://github.com/cclgroupltd/ccl-segb>

crush-forensics (SEGB) - <https://github.com/kalink0/crush-forensics>

DLEAPP (Biome, Biome Sets) - <https://github.com/abrignoni/DLEAPP>

mac_apt (BIOME) - <https://github.com/ydkhatri/mac_apt>

peach-forensics (Biome) - <https://github.com/kalink0/peach-forensics>