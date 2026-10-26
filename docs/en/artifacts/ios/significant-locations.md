---
title: "Frequent - Significant Locations"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [location]
---

# Frequent - Significant Locations

## Meaning

Frequent Locations is a feature within the iOS Location Services that automatically stores places where a user repeatedly stays. The aim is to provide personalised services such as location-based reminders or improved map and traffic predictions.

The algorithm that decides when a place becomes a "frequent location" is not public.

From a digital forensics perspective, Frequent Locations entries mean that a device was at the frequent location. The record contains the frequency, the start and the end of the stays, and how/how long the trip to the place took.

The accuracy with regard to time and place must be taken into account when interpreting the data.

## Key facts

1. The data is deleted after 3-4 months if the place is no longer visited. The column ZPLACEEXPIRATIONDATE in table ZRTLEARNEDLOCATIONOFINTERESTMO stores when entries are deleted.
2. Timestamps in Mac Absolute Time format (seconds since 2001-01-01, UTC)
3. The time accuracy is +- 15 minutes
4. Entries are only written after leaving the place, when the processing runs (every 2 to 4 days in tests)
5. The location accuracy is up to 250 m with regard to leaving
6. The cloud database can contain stays recorded by other devices of the same Apple Account (e.g. iPad, Mac)
7. Location:  
   **`/private/var/mobile/Library/Caches/com.apple.routined/Local.sqlite`**  
   **`/private/var/mobile/Library/Caches/com.apple.routined/Cloud.sqlite`**  
   **`/private/var/mobile/Library/Caches/com.apple.routined/Cloud-V2.sqlite`**

## References

2024-08: <https://dfir.pubpub.org/pub/4fkeiv34/release/1>

2020-07: <https://doubleblak.com/blog/locations>

## Tools

APOLLO (routined_local_*, routined_cloud_*) - <https://github.com/mac4n6/APOLLO>

ArtEx2 (Frequent Locations, Location Transitions) - <https://www.doubleblak.com/app.php?id=ArtEx2>

iLEAPP (appleMapsSignificantLocations, appleMapsSignificantLocationsVisits, appleMapsTrips, routinedCloudVisits) - <https://github.com/abrignoni/iLEAPP>
