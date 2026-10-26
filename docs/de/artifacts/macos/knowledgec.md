---
title: "KnowledgeC"
status: complete
completed: 2026-10-22
authors: [kalink0 (Marco Neumann)]
topics: [program-execution, device-state, web-activity, notifications, communication]
---

# KnowledgeC

## Bedeutung

Die Datenbank knowledgeC ist eine systeminterne macOS Datenbank. Das Betriebssystem nutzt diese Datenbank, um zum Beispiel Informationen zur App-Nutzung des Nutzers, zum Display-Status oder zum Ladezustand des Geräts zu speichern. Ziel ist es, das Bedienerlebnis zu optimieren.

Aus digitalforensischer Sicht lassen sich anhand der Einträge in der Datenbank je nach Eintragstyp unterschiedliche Aussagen treffen. 
Die Bedeutung der einzelnen Einträge wird im Folgenden beschrieben. Es können noch mehr Typen vorliegen.

| Eintragstyp | Belegt | Relevante Felder |
| --- | --- | --- |
| `/app/inFocus` | App war im Vordergrund, mit Beginn und Ende; erfasst werden nur Apps mit grafischer Oberfläche | `ZVALUESTRING`, `ZSTARTDATE`, `ZENDDATE` |
| `/app/usage` | App wurde vom System ausgeführt, nicht zwingend im Vordergrund | `ZVALUESTRING` |
| `/app/activity` | App hat eine Nutzeraktivität gemeldet, z.B. eine geöffnete E-Mail oder Notiz | `ZVALUESTRING` |
| `/app/intents` | Daten wurden zwischen Apps übergeben, z.B. Anruf gestartet oder Nachricht gesendet; bei auf den Mac synchronisierten Anrufen kann der Zeitstempel die Synchronisation statt den Anruf wiedergeben | `ZVALUESTRING` |
| `/app/webUsage` | App hat auf das Web zugegriffen, ggf. mit Domain und URL | `ZVALUESTRING` |
| `/safari/history` | URL wurde in Safari aufgerufen; privates Surfen wird nicht erfasst | `ZVALUESTRING` |
| `/notification/usage` | Benachrichtigung wurde empfangen bzw. auf eine bestimmte Art behandelt | `ZVALUESTRING` |
| `/device/isLocked` | Gerät war gesperrt (1) bzw. entsperrt (0), mit Beginn und Ende | `ZVALUEINTEGER` |
| `/display/isBacklit` | Display war an (1) bzw. aus (0) | `ZVALUEINTEGER` |
| `/device/isPluggedIn` | Gerät war am Netzteil angeschlossen | `ZVALUEINTEGER` |

## Spezifische Kurzinformation

1. Die Datenbank ist seit macOS 10.13 dokumentiert. Ab macOS 13 sind immer mehr Daten in die Biome verlagert worden; unter macOS 15 werden einzelne Eintragstypen (z.B. `/app/usage`, `/app/webUsage`, `/display/isBacklit`) noch befüllt.
2. Es gibt eine systemweite Datenbank und je Benutzer eine eigene, mit unterschiedlichen Eintragstypen.
3. Der Aufbewahrungszeitraum ist abhängig von den Eintragstypen, meist etwa vier Wochen.
4. Ablageort:  
   **`/private/var/db/CoreDuet/Knowledge/knowledgeC.db`**  
   **`/Users/{USER}/Library/Application Support/Knowledge/knowledgeC.db`**

## Referenzen

2018-08: <https://www.mac4n6.com/blog/2018/8/5/knowledge-is-power-using-the-knowledgecdb-database-on-macos-and-ios-to-determine-precise-user-and-application-usage>

## Tools

APOLLO (knowledge_*) - <https://github.com/mac4n6/APOLLO>

DLEAPP (KnowledgeC) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (Exchange: MacOS.Applications.KnowledgeC) - <https://github.com/Velocidex/velociraptor>