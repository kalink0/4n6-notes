---
title: "AirDrop"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [data-transfer]
---

# AirDrop

## Meaning

AirDrop is the Apple feature for directly transferring photos, files, links and other content between nearby Apple devices. The transfer is handled by the system service sharingd. In the process, it logs in the Unified Logs when content was shared, when a transfer was offered, accepted or declined, and how AirDrop visibility is set. It also stores the current AirDrop ID and the visibility setting in a preferences file.

From a digital forensics perspective, the entries on the sending device show that a certain piece of content from a certain app was to be sent to another device via AirDrop, and whether the transfer was accepted. On the receiving device, they show that a transfer came in from a device with the logged device name and whether it was accepted, declined or cancelled. Changes to visibility (Off, Contacts Only, Everyone) can also be traced. The logged device name alone, however, does not show who the sender was, as it can be changed freely.

## Key facts

1. The AirDrop entries in the Unified Logs are only kept for a few days up to about a week
2. Unified Logs: process sharingd, subsystem `com.apple.sharing`, category `AirDrop`; in addition a property list with AirDrop ID and visibility mode
3. The AirDrop ID is not permanent, it changes frequently; after a longer period of non-use the property list may contain no ID
4. The receiver's log contains partial hashes (SHA-256) of the phone number or email address of the sender's Apple ID; these may allow the sender to be identified
5. Received photos and videos usually end up in the Photos app
6. To attribute a transfer to a counterpart, the logs of both devices are needed
7. Further AirDrop traces: PowerLog (table `PLXPCAgent_EventForward_AirDrop`, examined up to iOS 14), KnowledgeC (stream `/photos/share/airdrop`, iOS 13 and 14) and InteractionC
8. Locations:  
   **`/private/var/db/diagnostics/`** (Unified Logs, also in the sysdiagnose as system_logs.logarchive)  
   **`/private/var/mobile/Library/Preferences/com.apple.sharingd.plist`**

## References

2026-09: <https://magnetforensics.com/blog/following-the-airdrop-breadcrumbs-with-axiom>

2022-03: <https://gforce4n6.blogspot.com/2022/03/airdropping-some-knowledge-using-rleapp.html>

2020-06: <https://www.mac4n6.com/blog/2020/6/5/analysis-of-apple-unified-logs-quarantine-edition-entry-11-airdropping-some-knowledge>

## Tools

APOLLO (powerlog_airdrop, knowledge_photos_share_airdrop) - <https://github.com/mac4n6/APOLLO>

ArtEx2 (AirDrop) - <https://www.doubleblak.com/app.php?id=ArtEx2>

iLEAPP (airdropId, logarchive_airdrop) - <https://github.com/abrignoni/iLEAPP>

RLEAPP (airdropNumbers, airdropEmails, airdropRealname, airdropdiscoverable) - <https://github.com/abrignoni/RLEAPP>
