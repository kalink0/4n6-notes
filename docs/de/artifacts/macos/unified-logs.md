---
title: "Unified Logs"
status: complete
completed: 2026-10-22
authors: [kalink0 (Marco Neumann)]
topics: [device-state]
---

# Unified Logs

## Bedeutung

Die Unified Logs sind seit macOS 10.12 (Sierra) das zentrale Protokollierungssystem von Apple und haben die älteren Textlogs (syslog, ASL) abgelöst. Nahezu alle Systemprozesse und viele Apps schreiben dort ihre Meldungen in verschiedenen Stufen (default, info, debug, error, fault). Gedacht sind sie für Entwickler und Apple selbst zur Fehlersuche; für den Nutzer haben sie keine direkte Funktion.

Aus digitalforensischer Sicht belegt ein Eintrag, dass ein bestimmter Prozess zum angegebenen Zeitpunkt die jeweilige Meldung protokolliert hat. Was eine Meldung über eine Nutzeraktion aussagt, hängt von der einzelnen Meldung ab und muss für jedes Ereignis gesondert untersucht sein. Nicht belegt ist dagegen, dass ein Vorgang nicht stattfand, wenn kein Eintrag vorhanden ist: Viele Werte sind als `<private>` geschwärzt, und ein Großteil der Einträge wird nach wenigen Tagen überschrieben.

## Spezifische Kurzinformation

Die Unified-Logs können als logarchive gepackt werden. In diesem Schritt werden alle notwendigen Dateien zusammen in ein Archiv gelegt. Am laufenden System erstellt `sudo log collect` ein logarchive.

Eine einzelne tracev3 kann zwar auch gelesen werden, jedoch fehlen die genauen Zeitstempel (da abhängig von Boot-Time des Geräts - Monotonic Timestamps) und die OS Strings. Folgende Tabelle zeigt die Dateien/Ordner, die für eine vollständige Anzeige notwendig sind.

| .logarchive path                      | macOS-Pfad                                        |
|---------------------------------------|---------------------------------------------------|
| `foo.logarchive/Persist/*.tracev3`    | `/private/var/db/diagnostics/Persist/*.tracev3`   |
| `foo.logarchive/Special/*.tracev3`    | `/private/var/db/diagnostics/Special/*.tracev3`   |
| `foo.logarchive/Signpost/*.tracev3`   | `/private/var/db/diagnostics/Signpost/*.tracev3`  |
| `foo.logarchive/HighVolume/*.tracev3` | `/private/var/db/diagnostics/HighVolume/*.tracev3` |
| `foo.logarchive/timesync/`            | `/private/var/db/diagnostics/timesync/`           |
| `foo.logarchive/uuidtext/`            | `/private/var/db/uuidtext/` ← anderer Stammordner! |

1. Die Logs rotieren nach Größe, nicht nach festen Tagen. Persist wird als Ganzes auf rund 500 MB gehalten, Special wird eintragsweise ausgedünnt. Der Großteil der Einträge bleibt nur wenige Tage erhalten, einzelne Special-Einträge mehrere Wochen. Bei Relevanz schnellstmöglich sichern.
2. Die älteste tracev3 in Persist markiert den Beginn des weitgehend vollständigen Zeitraums; davor sind nur noch lückenhaft einzelne Einträge vorhanden.
3. Binärformat, komprimiert; die Dateien sind nicht direkt lesbar und müssen mit `log show` oder einem Parser dekodiert werden
4. Sehr umfangreich: auf einem Mac mehrere Millionen Einträge, gezieltes Filtern ist für die Auswertung notwendig
5. Dekodiert vervielfacht sich die Datenmenge (in Tests aus rund 200 MB logarchive etwa 35 GB) - entsprechend Speicherplatz einplanen
6. Ablageort:  
   **`/private/var/db/diagnostics`**  
   **`/private/var/db/uuidtext`**

## Referenzen

2026-10: <https://eclecticlight.co/2026/10/19/can-i-browse-log-entries-from-2-weeks-ago/>

2026-10: <https://developer.apple.com/documentation/os/logging> (abgerufen)

2026-09: <https://thesisfriday.com/how-to-investigate-the-apple-unified-log/>

2026-09: <https://thesisfriday.com/what-is-the-apple-unified-log/>

2026-08: <https://leapps.org/blog-post?post=2026-08-01-unified-log-predicate-reference>

2026-03: <https://eclecticlight.co/2026/03/12/how-long-does-the-log-keep-entries/>

2025-06: <https://thesisfriday.com/wp-content/uploads/2025/06/CheatSheet_CLI_AUL_ENG-2.pdf>

2022-08: <https://cloud.google.com/blog/topics/threat-intelligence/reviewing-macos-unified-logs/>

2021-04: <https://eclecticlight.co/2021/04/20/how-some-log-entries-vanish-sooner-than-others/>

2020-04: <https://www.mac4n6.com/blog/2020/4/19/introducing-analysis-of-apple-unified-logs-quarantine-edition-entry-0>

## Tools

DLEAPP (Unified Logs) - <https://github.com/abrignoni/DLEAPP>

macos-UnifiedLogs - <https://github.com/mandiant/macos-UnifiedLogs>

peach-forensics (AUL) - <https://github.com/kalink0/peach-forensics>

Velociraptor (Exchange: MacOS.UnifiedLogParser, MacOS.UnifiedLogHunter) - <https://github.com/Velocidex/velociraptor>

UnifiedLogReader - <https://github.com/ydkhatri/UnifiedLogReader> (nur alte Versionen)