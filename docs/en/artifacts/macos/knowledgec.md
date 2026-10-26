---
title: "KnowledgeC"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution, device-state, web-activity, notifications, communication]
---

# KnowledgeC

## Meaning

The knowledgeC database is an internal macOS system database. The operating system uses this database to store information on, for example, the user's app usage, the display state or the charging state of the device. The aim is to optimise the user experience.

From a digital forensics perspective, the entries in the database allow different statements depending on the entry type. 
The meaning of the individual entries is described below. There may be further types.

| Entry type | Shows | Relevant fields |
| --- | --- | --- |
| `/app/inFocus` | App was in the foreground, with start and end; only apps with a graphical user interface are recorded | `ZVALUESTRING`, `ZSTARTDATE`, `ZENDDATE` |
| `/app/usage` | App was run by the system, not necessarily in the foreground | `ZVALUESTRING` |
| `/app/activity` | App reported a user activity, e.g. an opened email or note | `ZVALUESTRING` |
| `/app/intents` | Data was passed between apps, e.g. call started or message sent; for calls synced to the Mac, the timestamp can reflect the sync instead of the call | `ZVALUESTRING` |
| `/app/webUsage` | App accessed the web, possibly with domain and URL | `ZVALUESTRING` |
| `/safari/history` | URL was opened in Safari; private browsing is not recorded | `ZVALUESTRING` |
| `/notification/usage` | Notification was received or handled in a certain way | `ZVALUESTRING` |
| `/device/isLocked` | Device was locked (1) or unlocked (0), with start and end | `ZVALUEINTEGER` |
| `/display/isBacklit` | Display was on (1) or off (0) | `ZVALUEINTEGER` |
| `/device/isPluggedIn` | Device was connected to the power adapter | `ZVALUEINTEGER` |

## Key facts

1. The database has been documented since macOS 10.13. From macOS 13, more and more data has been moved to Biome; on macOS 15, individual entry types (e.g. `/app/usage`, `/app/webUsage`, `/display/isBacklit`) are still populated.
2. There is a system-wide database and a separate one per user, with different entry types.
3. The retention period depends on the entry types, usually about four weeks.
4. Location:  
   **`/private/var/db/CoreDuet/Knowledge/knowledgeC.db`**  
   **`/Users/{USER}/Library/Application Support/Knowledge/knowledgeC.db`**

## References

2018-08: <https://www.mac4n6.com/blog/2018/8/5/knowledge-is-power-using-the-knowledgecdb-database-on-macos-and-ios-to-determine-precise-user-and-application-usage>

## Tools

APOLLO (knowledge_*) - <https://github.com/mac4n6/APOLLO>

DLEAPP (KnowledgeC) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (Exchange: MacOS.Applications.KnowledgeC) - <https://github.com/Velocidex/velociraptor>
