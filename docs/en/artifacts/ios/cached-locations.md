---
title: "Cached Locations"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [location]
---

# Cached Locations

## Meaning

Where possible and enabled by the user, the iOS operating system stores the current location of the device at short intervals. The locations are cached by the system service routined.
Depending on the positioning technique used, the accuracy is higher or lower. Positioning can be done, for example, via the mobile network, surrounding Wi-Fi networks or GPS.

From a digital forensics perspective, the stored cached locations allow the statement that the device was at the stored coordinate at the given time with the given accuracy. The accuracy is understood as a radius in metres around the given coordinate. With a value of 25 metres, this means that, according to iOS's estimate, the device was within a radius of 25 metres around the stored coordinate; in one test, positions were slightly outside the given radius in individual cases (approx. 0.4% of the entries).

## Key facts

1. The data is available on the device for roughly the last 7 days
2. SQLite database, table `ZRTCLLOCATIONMO`
3. Timestamps in Mac Absolute Time format (seconds since 2001-01-01, UTC)
4. The intervals between entries are irregular (seconds to more than 20 minutes); a gap does not show that the device was off or did not move
5. Location:  
   **`/private/var/mobile/Library/Caches/com.apple.routined/Cache.sqlite`**

## References

2024-08: <https://dfir.pubpub.org/pub/4fkeiv34/release/1>

2023-06: <https://www.doubleblak.com/blogPost.php?k=LocationAccuracy>

2021-09: <https://theforensicscooter.com/2021/09/22/iphone-device-speeds-in-cache-sqlite-zrtcllocationmo/>

2020-07: <https://doubleblak.com/blog/locations>

## Tools

APOLLO (routined_cache_zrtcllocationmo) - <https://github.com/mac4n6/APOLLO>

ArtEx2 (Cached Locations) - <https://www.doubleblak.com/app.php?id=ArtEx2>

iLEAPP (CacheSQLite_Locations) - <https://github.com/abrignoni/iLEAPP>
