---
title: "Biome"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [device-state]
---

# Biome

## Meaning

Biome is an Apple framework in which macOS stores information about the use of the device, such as app usage, notifications or media playback. From this, macOS creates predictions and suggestions, e.g. for Siri, proactive suggestions and the personalisation of the system. Since macOS 13, Biome has taken over most of the tasks of KnowledgeC. The data is divided into thematic streams, each stream in its own folder with files in the SEGB format.

From a digital forensics perspective, an entry shows that macOS recorded the respective event in the stream concerned at the given time; what the event says about a user action depends on the stream. Entries from the subfolder remote come from other devices with the same Apple ID and do not show that the event took place on the examined device. It does not show, however, that an event did not take place if there is no entry.

## Key facts

1. Biome is actively used from macOS 12, as the main source instead of KnowledgeC from macOS 13
2. There are per-user streams and system-wide streams; on a running system, the restricted streams can only be read with elevated privileges
3. SEGB format (v1 and v2); files without extension, named after the creation time; content mostly Protobuf without a published schema
4. Timestamps in Mac Absolute Time format (seconds since 2001-01-01, UTC)
5. Each stream has the subfolders local and remote (data from other devices with the same Apple ID, one folder per device); expired files are stored in local/tombstone
6. Deleted entries keep their timestamp and status, their content is empty
7. The devices behind remote are listed in **`/Users/{USER}/Library/Biome/sync/sync.db`**
8. Besides streams there is the folder sets with SQLite databases, e.g. on installed apps or contacts
9. Locations:  
   **`/Users/{USER}/Library/Biome/streams/public/`**  
   **`/Users/{USER}/Library/Biome/streams/restricted/`**  
   **`/private/var/db/biome/streams/`**

## References

2026-06: <https://unit42.paloaltonetworks.com/new-macos-artifact-discovered/>

2023-10: <https://cellebrite.com/en/understanding-and-decoding-the-newest-ios-segb-format/>

2022-06: <https://eclecticlight.co/2022/06/27/biome-isnt-about-biometrics-but-suggestions/>

## Tools

ccl-segb - <https://github.com/cclgroupltd/ccl-segb>

crush-forensics (SEGB) - <https://github.com/kalink0/crush-forensics>

DLEAPP (Biome, Biome Sets) - <https://github.com/abrignoni/DLEAPP>

mac_apt (BIOME) - <https://github.com/ydkhatri/mac_apt>

peach-forensics (Biome) - <https://github.com/kalink0/peach-forensics>
