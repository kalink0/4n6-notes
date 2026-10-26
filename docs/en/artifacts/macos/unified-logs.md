---
title: "Unified Logs"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [device-state]
---

# Unified Logs

## Meaning

Since macOS 10.12 (Sierra), the Unified Logs have been Apple's central logging system and replaced the older text logs (syslog, ASL). Almost all system processes and many apps write their messages there at different levels (default, info, debug, error, fault). They are intended for developers and Apple itself for troubleshooting; they have no direct function for the user.

From a digital forensics perspective, an entry shows that a certain process logged the respective message at the given time. What a message says about a user action depends on the individual message and must be examined separately for each event. It does not show, however, that an action did not take place if there is no entry: many values are redacted as `<private>`, and most entries are overwritten after a few days.

## Key facts

The Unified Logs can be packed as a logarchive. In this step, all necessary files are put together into one archive. On a running system, `sudo log collect` creates a logarchive.

A single tracev3 can be read on its own, but the exact timestamps (as they depend on the device's boot time - monotonic timestamps) and the OS strings are missing. The following table shows the files/folders required for a complete display.

| .logarchive path                      | macOS path                                        |
|---------------------------------------|---------------------------------------------------|
| `foo.logarchive/Persist/*.tracev3`    | `/private/var/db/diagnostics/Persist/*.tracev3`   |
| `foo.logarchive/Special/*.tracev3`    | `/private/var/db/diagnostics/Special/*.tracev3`   |
| `foo.logarchive/Signpost/*.tracev3`   | `/private/var/db/diagnostics/Signpost/*.tracev3`  |
| `foo.logarchive/HighVolume/*.tracev3` | `/private/var/db/diagnostics/HighVolume/*.tracev3` |
| `foo.logarchive/timesync/`            | `/private/var/db/diagnostics/timesync/`           |
| `foo.logarchive/uuidtext/`            | `/private/var/db/uuidtext/` ← different parent folder! |

1. The logs rotate by size, not by a fixed number of days. Persist as a whole is kept at around 500 MB, Special is thinned out entry by entry. Most entries are only kept for a few days, individual Special entries for several weeks. If relevant, secure them as quickly as possible.
2. The oldest tracev3 in Persist marks the start of the largely complete period; before that, only individual entries remain, with gaps.
3. Binary format, compressed; the files cannot be read directly and must be decoded with `log show` or a parser
4. Very extensive: several million entries on a Mac, targeted filtering is necessary for the analysis
5. Decoded, the amount of data multiplies (in tests about 35 GB from around 200 MB of logarchive) - plan storage space accordingly
6. Location:  
   **`/private/var/db/diagnostics`**  
   **`/private/var/db/uuidtext`**

## References

2026-10: <https://eclecticlight.co/2026/10/19/can-i-browse-log-entries-from-2-weeks-ago/>

2026-10 (accessed): <https://developer.apple.com/documentation/os/logging>

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

UnifiedLogReader - <https://github.com/ydkhatri/UnifiedLogReader> (old versions only)

Velociraptor (Exchange: MacOS.UnifiedLogParser, MacOS.UnifiedLogHunter) - <https://github.com/Velocidex/velociraptor>
