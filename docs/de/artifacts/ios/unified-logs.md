---
title: "Unified Logs"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [device-state]
---

# Unified Logs

## Bedeutung

Die Unified Logs sind seit iOS 10 bzw. macOS 10.12 das zentrale Protokollierungssystem von Apple und haben die älteren Textlogs (syslog, ASL) abgelöst. Nahezu alle Systemprozesse und viele Apps schreiben dort ihre Meldungen in verschiedenen Stufen (default, info, debug, error, fault). Gedacht sind sie für Entwickler und Apple selbst zur Fehlersuche; für den Nutzer haben sie keine direkte Funktion.

Aus digitalforensischer Sicht belegt ein Eintrag, dass ein bestimmter Prozess zum angegebenen Zeitpunkt die jeweilige Meldung protokolliert hat. Was eine Meldung über eine Nutzeraktion aussagt, hängt von der einzelnen Meldung ab und muss für jedes Ereignis gesondert untersucht sein. Nicht belegt ist dagegen, dass ein Vorgang nicht stattfand, wenn kein Eintrag vorhanden ist: Viele Werte sind als `<private>` geschwärzt, und ein Großteil der Einträge wird nach wenigen Tagen überschrieben.

## Spezifische Kurzinformation

Die Unified-Logs können als logarchive gepackt werden. In diesem Schritt werden alle notwendigen Dateien zusammen in ein Archiv gelegt.

Eine einzelne tracev3 kann zwar auch gelesen werden, jedoch fehlen die genauen Zeitstempel (da abhängig von Boot-Time des Geräts - Monotonic Timestamps) und die OS Strings. Folgende Tabelle zeigt die Dateien/Ordner die für eine vollständige Anzeige notwendig sind.

| .logarchive path                    | iOS full-FS path                                |
|-------------------------------------|-------------------------------------------------|
| `foo.logarchive/Persist/*.tracev3`  | `private/var/db/diagnostics/Persist/*.tracev3`  |
| `foo.logarchive/Special/*.tracev3`  | `private/var/db/diagnostics/Special/*.tracev3`  |
| `foo.logarchive/Signpost/*.tracev3` | `private/var/db/diagnostics/Signpost/*.tracev3` |
| `foo.logarchive/timesync/`          | `private/var/db/diagnostics/timesync/`          |
| `foo.logarchive/uuidtext/`          | `private/var/db/uuidtext/` ← anderer Stammordner! |

1. Die Logs rotieren nach Größe, nicht nach festen Tagen; der Großteil der Einträge bleibt nur wenige Tage erhalten, nur ein kleiner Teil 14 Tage oder länger - bei Relevanz schnellstmöglich sichern.
2. Ein sysdiagnose enthält einen deutlich kürzeren Zeitraum als die Logs auf dem Gerät (in Tests 2 statt 14 Tage)
3. Binärformat, komprimiert; die Dateien sind nicht direkt lesbar und müssen mit einem Parser oder `log show` auf einem Mac dekodiert werden
4. Sehr umfangreich, gezieltes Filtern ist für die Auswertung notwendig
5. Dekodiert vervielfacht sich die Datenmenge (in Tests aus rund 200 MB logarchive etwa 35 GB) - entsprechend Speicherplatz einplanen
6. Ablageort:  
   **`/private/var/db/diagnostics`**  
   **`/private/var/db/uuidtext`**

## Referenzen

2026-10 (abgerufen): <https://developer.apple.com/documentation/os/logging>

2026-09: <https://thesisfriday.com/how-to-investigate-the-apple-unified-log/>

2026-09: <https://thesisfriday.com/what-is-the-apple-unified-log/>

2026-08: <https://leapps.org/blog-post?post=2026-08-01-unified-log-predicate-reference>

2025-06: <https://thesisfriday.com/wp-content/uploads/2025/06/CheatSheet_CLI_AUL_ENG-2.pdf>

2025-05: <https://www.ios-unifiedlogs.com/post/ios-unified-logs-the-myth-of-30days-retention>

2025-03: <https://www.ios-unifiedlogs.com/post/ios-unified-logs-don-t-trust-the-clock-timestamp>

2020-04: <https://www.mac4n6.com/blog/2020/4/19/introducing-analysis-of-apple-unified-logs-quarantine-edition-entry-0>

## Tools

iLEAPP (logarchive) - <https://github.com/abrignoni/iLEAPP>

macos-UnifiedLogs - <https://github.com/mandiant/macos-UnifiedLogs>

peach-forensics (AUL) - <https://github.com/kalink0/peach-forensics>

UnifiedLogReader - <https://github.com/ydkhatri/UnifiedLogReader> (nur alte Versionen)