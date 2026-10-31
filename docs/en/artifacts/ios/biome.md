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

Biome is an Apple framework in which iOS stores information about the use of the device, such as app usage, notifications, media playback or visited places. From this, iOS creates predictions and suggestions, e.g. for Siri, proactive suggestions and the personalisation of the system. Since iOS 16, Biome has taken over most of the tasks of KnowledgeC. The data is divided into several hundred thematic streams, each stream in its own folder with files in the SEGB format.

From a digital forensics perspective, an entry shows that iOS recorded the respective event in the stream concerned at the given time; what the event says about a user action depends on the stream. Entries from the subfolder remote come from other devices with the same Apple ID and do not show that the event took place on the examined device. It does not show, however, that an event did not take place if there is no entry.

## Key facts

1. SEGB files first from iOS 14, Biome as the main source from iOS 16
2. Only included in full file system extractions, not in logical acquisitions
3. Retention differs per stream: many streams about four weeks, some several months
4. SEGB format: v1 up to iOS 16, v2 from iOS 17 (with trailer at the end of the file); files without extension, named after the creation time; content mostly Protobuf without a published schema
5. Timestamps in Mac Absolute Time format (seconds since 2001-01-01, UTC)
6. Each stream has the subfolders local, remote (data from other devices with the same Apple ID) and tombstone (expired entries)
7. Deleted entries keep their timestamp and status, their content is empty
8. Entries about an app are retained even after the app has been deleted
9. SEGB files also occur outside of Biome, e.g. in DuetExpertCenter/streams
10. Locations:  
    **`/private/var/mobile/Library/Biome/streams/public/`** (iOS 14 to 16)  
    **`/private/var/mobile/Library/Biome/streams/restricted/`** (from iOS 15)  
    **`/private/var/db/biome/streams/restricted/`** (from iOS 16)

## References

2026-07: <https://blog.digital-forensics.it/2026/07/84-streams-later-exploring-evolution-of.html>

2026-05: <https://bebinary4n6.blogspot.com/2026/05/beyond-c-segb-and-biome-forensics-with.html>

2023-10: <https://cellebrite.com/en/understanding-and-decoding-the-newest-ios-segb-format/>

2022-09: <https://blog.d204n6.com/2022/09/ios-16-now-you-c-it-now-you-dont.html>

## Tools

ArtEx2 (Biome parser) - <https://www.doubleblak.com/app.php?id=ArtEx2>

ccl-segb - <https://github.com/cclgroupltd/ccl-segb>

crush-forensics (SEGB) - <https://github.com/kalink0/crush-forensics>

iLEAPP (Biome modules) - <https://github.com/abrignoni/iLEAPP>

mac_apt (BIOME) - <https://github.com/ydkhatri/mac_apt>

peach-forensics (Biome) - <https://github.com/kalink0/peach-forensics>
