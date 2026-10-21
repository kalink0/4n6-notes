---
title: "Biome"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [device-state]
---

# Biome

## Bedeutung

Biome ist ein Framework von Apple, in dem iOS Informationen über die Nutzung des Geräts speichert, etwa App-Nutzung, Benachrichtigungen, Medienwiedergabe oder besuchte Orte. Daraus erstellt iOS Vorhersagen und Vorschläge, z.B. für Siri, proaktive Vorschläge und die Personalisierung des Systems. Seit iOS 16 hat Biome einen Großteil der Aufgaben von KnowledgeC übernommen. Die Daten sind in mehrere hundert thematische Streams gegliedert, jeder Stream in einem eigenen Ordner mit Dateien im Format SEGB.

Aus digitalforensischer Sicht belegt ein Eintrag, dass iOS zum angegebenen Zeitpunkt das jeweilige Ereignis im betreffenden Stream erfasst hat; was das Ereignis über eine Nutzeraktion aussagt, hängt vom Stream ab. Einträge aus dem Unterordner remote stammen von anderen Geräten derselben Apple-ID und belegen nicht, dass das Ereignis auf dem untersuchten Gerät stattfand. Nicht belegt ist dagegen, dass ein Ereignis nicht stattfand, wenn kein Eintrag vorhanden ist.

## Spezifische Kurzinformation

1. SEGB-Dateien erstmals ab iOS 14, Biome als Hauptquelle ab iOS 16
2. Nur in Full-File-System-Extraktionen enthalten, nicht in logischen Sicherungen
3. Aufbewahrung je Stream unterschiedlich: viele Streams etwa vier Wochen, manche mehrere Monate
4. Format SEGB: v1 bis iOS 16, v2 ab iOS 17 (mit Trailer am Dateiende); Dateien ohne Endung, benannt nach dem Erstellungszeitpunkt; Inhalte meist Protobuf ohne veröffentlichtes Schema
5. Zeitstempel im Format Mac Absolute Time (Sekunden seit 2001-01-01, UTC)
6. Jeder Stream hat die Unterordner local, remote (Daten anderer Geräte derselben Apple-ID) und tombstone (abgelaufene Einträge)
7. Gelöschte Einträge behalten Zeitstempel und Status, ihr Inhalt ist leer
8. Einträge zu einer App bleiben auch nach dem Löschen der App erhalten
9. SEGB-Dateien kommen auch außerhalb von Biome vor, z.B. in DuetExpertCenter/streams
10. Ablageorte:  
    **/private/var/mobile/Library/Biome/streams/public/** (iOS 14 bis 16)  
    **/private/var/mobile/Library/Biome/streams/restricted/** (ab iOS 15)  
    **/private/var/db/biome/streams/restricted/** (ab iOS 16)
    
## Referenzen

2026-07: <https://blog.digital-forensics.it/2026/07/84-streams-later-exploring-evolution-of.html>

2026-07: <https://bebinary4n6.blogspot.com/2026/05/beyond-c-segb-and-biome-forensics-with.html>

2023-10: <https://cellebrite.com/en/understanding-and-decoding-the-newest-ios-segb-format/>

2022-09: <https://blog.d204n6.com/2022/09/ios-16-now-you-c-it-now-you-dont.html>

## Tools

ArtEx2 (Biome-Parser) - <https://www.doubleblak.com/app.php?id=ArtEx2>

ccl-segb - <https://github.com/cclgroupltd/ccl-segb>

crush-forensics (SEGB) - <https://github.com/kalink0/crush-forensics>

iLEAPP (Biome-Module) - <https://github.com/abrignoni/iLEAPP>

mac_apt (BIOME) - <https://github.com/ydkhatri/mac_apt>

peach-forensics (Biome) - <https://github.com/kalink0/peach-forensics>