---
title: "GPS"
status: complete
completed: 2026-10-31
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# GPS

GPS (Global Positioning System) is a satellite-based navigation system of the USA with which a receiver can determine its position, altitude and the exact time.

The receiver calculates its position from the signal travel time from at least four satellites. Under open sky, the accuracy is a few metres; in buildings, tunnels or between tall buildings it is considerably worse, or no position can be determined at all. Besides GPS, there are other satellite navigation systems such as Galileo (EU), GLONASS (Russia) and BeiDou (China), collectively referred to as GNSS (Global Navigation Satellite System). Current smartphones use several of them at the same time; "GPS" is commonly used for all of them. Smartphones speed up positioning with assistance data from the internet or the mobile network (A-GPS) and combine it with positioning via Wi-Fi and radio cells.

From a digital forensics perspective, GPS positions are found, for example, in the metadata of photos (EXIF), in location histories of operating systems and apps, in fitness trackers, navigation devices and vehicles. Smartphones often store an accuracy value for a location as a radius in metres. A radius of a few metres indicates positioning via GNSS, a considerably larger one positioning via Wi-Fi or radio cell.
