---
title: "Usagestats"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution, device-state]
---

# Usagestats

## Meaning

The UsageStats system service logs the use of apps and certain device events. Android provides the data to apps with usage access permission, for example for screen time analyses.

From a digital forensics perspective, an event entry shows that at the given time an activity of the app moved to the foreground (ACTIVITY_RESUMED) or left it (ACTIVITY_PAUSED, ACTIVITY_STOPPED). In addition, device events are recorded, e.g. screen interactive/non-interactive (SCREEN_INTERACTIVE/SCREEN_NON_INTERACTIVE), lock screen shown/dismissed (KEYGUARD_SHOWN/KEYGUARD_HIDDEN) as well as shutdown and startup of the device. The aggregated values per interval show, per app, the time of last use and the total time in the foreground.

It does not show that a person actively operated the app, or in which way the lock screen was dismissed.

## Key facts

1. XML up to Android 9, Protobuf from Android 10
2. From Android 11, package and class names are replaced by tokens that can only be resolved via the file `mappings` in the same folder
3. Data is stored per user in the subfolders `daily`, `weekly`, `monthly` and `yearly`; the same entries can appear in several interval folders
4. Timestamps: Unix time in milliseconds (UTC), stored as an offset to the file name (start of the interval); negative values are absolute timestamps
5. Location:  
   up to Android 10: **`/data/system/usagestats/{USER_ID}/`**  
   from Android 11: **`/data/system_ce/{USER_ID}/usagestats/`**

## References

2026-08: <https://leapps.org/blog-post?post=2026-08-03-android-usagestats-recent-tasks>  
2026-04: <https://andreafortuna.org/2026/04/23/android-pattern-of-life-hidden-artifacts-reconstruct-daily-routine/>  
2025-11: <https://forensafe.com/blogs/android-app-usage-history.html>  
2021-04: <https://www.sans.org/white-papers/40265>  
2020-01: <https://www.swiftforensics.com/2020/01/usagestats-on-android-10-q.html>  
2019-02: <https://abrignoni.blogspot.com/2019/02/android-usagestats-xml-parser.html>

## Tools

ALEAPP (Usage Stats) - <https://github.com/abrignoni/ALEAPP>
