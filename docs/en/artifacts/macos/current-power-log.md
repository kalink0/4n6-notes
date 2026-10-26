---
title: "macOS CurrentPowerLog"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [device-state, program-execution]
---

# macOS CurrentPowerLog

## Meaning

With Powerlog, macOS records the energy consumption and activities of various system components. This information helps to analyse the energy consumption and behaviour of the system, for example in connection with battery life.

From a digital forensics perspective, the stored events can provide indications of app activities and other system events. The specific evidential value depends on the event tables present and the data stored in them.

## Key facts

1. File format: SQLite, file extension `.PLSQL`
2. Data for roughly the last 3 days is available
3. Timestamps may have to be calculated with an offset (monotonic clock)
4. The database contains event tables of different system components
5. In addition to the current database, archived Powerlog files may be present
6. Location:  
   **`/private/var/db/powerlog/Library/BatteryLife/CurrentPowerlog.PLSQL`**  
   Archive: **`/private/var/db/powerlog/Library/BatteryLife/Archives/*.PLSQL.gz`**

## References

2026-10: <https://housekeeping101.github.io/sec-research-site/dfir--and--forensics/forensics/macos_forensics_framework_v1_9>

2026-10: <https://objectivebythesea.org/v8/talks/OBTS_v8_sEdwards.pdf>

2025-06: <https://doubleblak.com/blogPost.php?k=powerlog>

## Tools

APOLLO - <https://github.com/mac4n6/APOLLO>

EffectivePower - <https://github.com/saagarjha/EffectivePower>
