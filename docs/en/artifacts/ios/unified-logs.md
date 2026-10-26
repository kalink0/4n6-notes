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

Since iOS 10 and macOS 10.12, the Unified Logs have been Apple's central logging system and replaced the older text logs (syslog, ASL). Almost all system processes and many apps write their messages there at different levels (default, info, debug, error, fault). They are intended for developers and Apple itself for troubleshooting; they have no direct function for the user.

From a digital forensics perspective, an entry shows that a certain process logged the respective message at the given time. What a message says about a user action depends on the individual message and must be examined separately for each event. It does not show, however, that an action did not take place if there is no entry: many values are redacted as `<private>`, and most entries are overwritten after a few days.

## Key facts

The Unified Logs can be packed as a logarchive. In this step, all necessary files are put together into one archive.

A single tracev3 can be read on its own, but the exact timestamps (as they depend on the device's boot time - monotonic timestamps) and the OS strings are missing. The following table shows the files/folders required for a complete display.

| .logarchive path                    | iOS full-FS path                                |
|-------------------------------------|-------------------------------------------------|
| `foo.logarchive/Persist/*.tracev3`  | `private/var/db/diagnostics/Persist/*.tracev3`  |
| `foo.logarchive/Special/*.tracev3`  | `private/var/db/diagnostics/Special/*.tracev3`  |
| `foo.logarchive/Signpost/*.tracev3` | `private/var/db/diagnostics/Signpost/*.tracev3` |
| `foo.logarchive/timesync/`          | `private/var/db/diagnostics/timesync/`          |
| `foo.logarchive/uuidtext/`          | `private/var/db/uuidtext/` ← different parent folder! |

1. The logs rotate by size, not by a fixed number of days; most entries are only kept for a few days, only a small part for 14 days or longer - if relevant, secure them as quickly as possible.
2. A sysdiagnose contains a much shorter period than the logs on the device (2 instead of 14 days in tests)
3. Binary format, compressed; the files cannot be read directly and must be decoded with a parser or `log show` on a Mac
4. Very extensive, targeted filtering is necessary for the analysis
5. Decoded, the amount of data multiplies (in tests about 35 GB from around 200 MB of logarchive) - plan storage space accordingly
6. Location:  
   **`/private/var/db/diagnostics`**  
   **`/private/var/db/uuidtext`**

## References

2026-10 (accessed): <https://developer.apple.com/documentation/os/logging>

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

UnifiedLogReader - <https://github.com/ydkhatri/UnifiedLogReader> (old versions only)
