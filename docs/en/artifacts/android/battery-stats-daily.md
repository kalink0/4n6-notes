---
title: "Battery Stats Daily"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de:sha256:7e53f8c9dcb8
topics: [device-state]
---

# Battery Stats Daily

## Meaning

Android keeps daily statistics on the charging and discharging history of the battery, split into individual charge and discharge steps per daily entry. In addition, each daily entry records package changes with package name and version number.

From a digital forensics perspective, an entry shows that during the given daily period the battery was charged or discharged in steps of the respective duration, which battery level was reached, and which screen state (on, off, Doze, Doze Suspend) as well as which power save and idle state applied at the start of the step. For power save mode and idle, it also shows whether they changed during the step. A package entry shows that this package was changed during the daily period.

It does not show at which exact point in time a single step or a package change took place.

## Key facts

1. XML or ABX; in the examined images XML up to Android 13, ABX from Android 14
2. Contains roughly the last 10 days
3. Steps are stored in reverse order, newest first
4. Step as `state-level-duration`, battery level and duration in hexadecimal (e.g. `oZI-35-c2957` = 53%, 796,503 ms)
5. Times of the individual steps are durations in milliseconds, not points in time; only the start and end of the daily entry are Unix timestamps in milliseconds (UTC)
6. Location:  
   **`/data/system/batterystats-daily.xml`**

## References

2026-10: <https://bebinary4n6.blogspot.com/2026/10/ten-days-of-android-battery-history-and.html>  
2024-01: <https://blog.digital-forensics.it/2024/01/a-first-look-at-android-14-forensics.html>

## Tools

ALEAPP (Android Battery Stats Daily) - <https://github.com/abrignoni/ALEAPP>
