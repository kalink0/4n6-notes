---
title: "KnowledgeC"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution, device-state, external-devices, web-activity, notifications, communication]
---

# KnowledgeC

## Meaning

The knowledgeC database is an internal iOS system database. The operating system uses this database to store information on, for example, the user's app usage, the device's battery usage including charging cycles, or the connection status to Bluetooth/Wi-Fi. The aim is to optimise the user experience.

From a digital forensics perspective, the entries in the database allow different statements depending on the entry type. 
The meaning of the individual entries is described below. There may be further types.

| Entry type | Shows | Relevant fields |
| --- | --- | --- |
| `/app/inFocus` | App was in the foreground, with start, end and launch reason (e.g. Spotlight, widget, Siri, notification) | `ZVALUESTRING`, `ZSTARTDATE`, `ZENDDATE` |
| `/app/usage` | App was run by the system, not necessarily in the foreground | `ZVALUESTRING` |
| `/app/intents` | Data was passed between apps, e.g. call started or message sent; can contain the full message text | `ZVALUESTRING` |
| `/app/webUsage` | App accessed the web, possibly with page title and URL | `ZVALUESTRING` |
| `/safari/history` | URL was opened in Safari; private browsing is not recorded | `ZVALUESTRING` |
| `/notification/usage` | Notification was received or handled in a certain way (e.g. opened, deleted, swiped away) | `ZVALUESTRING` |
| `/device/isLocked` | Device was locked (1) or unlocked (0), with start and end | `ZVALUEINTEGER` |
| `/display/isBacklit` | Display was on (1) or off (0) | `ZVALUEINTEGER` |
| `/device/isPluggedIn` | Device was charging, also wirelessly | `ZVALUEINTEGER` |
| `/bluetooth/isConnected` | Bluetooth connection existed, possibly with device name and MAC address | `ZVALUEINTEGER` |

## Key facts

1. The database was introduced with iOS 10. Since iOS 16, more and more of the data otherwise found in KnowledgeC has been moved to Biome.
2. The retention period depends on the entry types, usually about four weeks.
3. Location:  
   **`/private/var/mobile/Library/CoreDuet/Knowledge/knowledgeC.db`**

## References

2023-08: <https://www.doubleblak.com/blogPost.php?k=knowledgec2>

2022-11: <https://dfir.pubpub.org/pub/g2v1z97i/release/1>

2021-10: <https://theforensicscooter.com/2021/10/03/ios-knowledgec-db-notifications/>

2019-10: <https://www.doubleblak.com/blogPost.php?k=knowledgec>

2018-08: <https://www.mac4n6.com/blog/2018/8/5/knowledge-is-power-using-the-knowledgecdb-database-on-macos-and-ios-to-determine-precise-user-and-application-usage>

## Tools

APOLLO (knowledge_*) - <https://github.com/mac4n6/APOLLO>

ArtEx2 (KnowledgeC parser) - <https://www.doubleblak.com/app.php?id=ArtEx2>

iLEAPP (knowledgeC) - <https://github.com/abrignoni/iLEAPP>
