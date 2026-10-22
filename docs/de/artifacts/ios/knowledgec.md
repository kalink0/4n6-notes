---
title: "KnowledgeC"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [program-execution, device-state, external-devices, web-activity, notifications, communication]
---

# KnowledgeC

## Bedeutung

Die Datenbank knowledgeC ist eine systeminterne iOS Datenbank. Das Betriebssystem nutzt diese Datenbank um Informationen zu zum Beispiel App-Nutzung des Nutzers, Batterie-Nutzung des Geräts inkl. Ladezyklen oder Verbindungsstatus zu Bluetooth/WLAN zu speichern. Ziel ist es das Bedienerlebnis zu optimieren.

Aus digitalforensischer Sicht lassen sich anhand der Einträge in der Datenbank je nach Eintragstyp unterschiedliche Aussagen treffen. 
Die Bedeutung der einzelnen Einträge wird im Folgenden beschrieben. Es könnne noch mehr Typen vorliegen.

| Eintragstyp | Belegt | Relevante Felder |
| --- | --- | --- |
| `/app/inFocus` | App war im Vordergrund, mit Beginn, Ende und Startgrund (z.B. Spotlight, Widget, Siri, Benachrichtigung) | `ZVALUESTRING`, `ZSTARTDATE`, `ZENDDATE` |
| `/app/usage` | App wurde vom System ausgeführt, nicht zwingend im Vordergrund | `ZVALUESTRING` |
| `/app/intents` | Daten wurden zwischen Apps übergeben, z.B. Anruf gestartet oder Nachricht gesendet; kann den vollständigen Nachrichtentext enthalten | `ZVALUESTRING` |
| `/app/webUsage` | App hat auf das Web zugegriffen, ggf. mit Seitentitel und URL | `ZVALUESTRING` |
| `/safari/history` | URL wurde in Safari aufgerufen; privates Surfen wird nicht erfasst | `ZVALUESTRING` |
| `/notification/usage` | Benachrichtigung wurde empfangen bzw. auf eine bestimmte Art behandelt (z.B. geöffnet, gelöscht, weggewischt) | `ZVALUESTRING` |
| `/device/isLocked` | Gerät war gesperrt (1) bzw. entsperrt (0), mit Beginn und Ende | `ZVALUEINTEGER` |
| `/display/isBacklit` | Display war an (1) bzw. aus (0) | `ZVALUEINTEGER` |
| `/device/isPluggedIn` | Gerät wurde geladen, auch kabellos | `ZVALUEINTEGER` |
| `/bluetooth/isConnected` | Bluetooth-Verbindung bestand, ggf. mit Gerätename und MAC-Adresse | `ZVALUEINTEGER` |

## Spezifische Kurzinformation

1. Die Datenbank wurde eingeführt mit iOS 10. Seit iOS 16 sind immer mehr der sonst in KnowledgeC zu findenden Daten in die Biome geschoben worden.
2. Der Aufbewahrungszeitraum ist abhängig von den Eintragstypen, meist etwa vier Wochen.
3. Ablageort:  
   **`/private/var/mobile/Library/CoreDuet/Knowledge/knowledgeC.db`**

## Referenzen

2023-08: <https://www.doubleblak.com/blogPost.php?k=knowledgec2>

2022-11: <https://dfir.pubpub.org/pub/g2v1z97i/release/1>

2021-10: <https://theforensicscooter.com/2021/10/03/ios-knowledgec-db-notifications/>

2019-10: <https://www.doubleblak.com/blogPost.php?k=knowledgec>

2018-08: <https://www.mac4n6.com/blog/2018/8/5/knowledge-is-power-using-the-knowledgecdb-database-on-macos-and-ios-to-determine-precise-user-and-application-usage>

## Tools

APOLLO (knowledge_*) - <https://github.com/mac4n6/APOLLO>

ArtEx2 (KnowledgeC-Parser) - <https://www.doubleblak.com/app.php?id=ArtEx2>

iLEAPP (knowledgeC) - <https://github.com/abrignoni/iLEAPP>