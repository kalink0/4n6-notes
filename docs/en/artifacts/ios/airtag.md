---
title: "AirTag"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [location, external-devices]
---

# AirTag

## Meaning

AirTags are Apple tracking tags that are located via the Find My network. On the iPhone, the system service searchpartyd manages both the user account's own and shared AirTags and unknown trackers that move along with the device and that the iPhone warns about. For this, it creates separate, encrypted records as well as databases per record type.

From a digital forensics perspective, the data on the owner's device shows which AirTags were assigned to or shared with the Apple Account, when they were paired or shared, and at which locations they were reported. On the device of a tracked person, it shows that an unknown tracker was detected and an alert was triggered, and at which locations it was detected together with the device. It does not show, however, when and where an unknown tracker was placed, who it belongs to, or that the examined device itself was at a reported AirTag location.

| Entry type (in `com.apple.icloud.searchpartyd/`) | Shows | Relevant fields |
| --- | --- | --- |
| `OwnedBeacons/` | AirTag is assigned to the account, with pairing time and serial number | `pairingTime`, `stableIdentifier` |
| `BeaconNamingRecord/` | Name and emoji of the AirTag given by the user | `associatedBeacon` |
| `SharedBeacons/` | AirTag was shared with the account, by whom and when | `destination`, `shareDate` |
| `OwnerSharingCircle/`, `OwnerPeerTrust/` | Own AirTag was shared, with the recipient's Apple ID | `acceptanceState` |
| `SafeLocations/` | Places without alerts for items left behind; does not show a stay | – |
| `BeaconEstimatedLocation/` | Reported locations of the AirTag with timestamp | – |
| `WildModeAssociationRecord/` | Unknown tracker was detected and an alert triggered, with locations and manufacturer/model | – |
| `Observations.db` | Find My devices nearby, with location, time and signal strength | – |

## Key facts

1. Records on unknown trackers observed from iOS 15.3.1, `Observations.db` from iOS 16
2. Can only be analysed in full file system extractions with keychain, not in logical acquisitions
3. Locations and observations are discarded quickly, alerts on unknown trackers after about 48 hours; data on own and shared AirTags is kept longer
4. Records are AES-GCM-encrypted binary plists, key in the keychain (service BeaconStore); the databases are encrypted with the SQLite Encryption Extension, with their own keychain entry
5. Timestamps in UTC
6. The Bluetooth MAC address of an AirTag changes about every 24 hours; the first recorded location of an unknown tracker is therefore not necessarily the place where it was placed
7. The identifier of an unknown tracker is unique per victim device; a link to the owner is not possible without Apple
8. Alerts are also triggered by other Find My devices, e.g. AirPods
9. In addition, the Find My app stores name, serial number and last location of own AirTags in the cache `Items.data`, which can only be analysed if unencrypted
10. Locations:  
    **`/private/var/mobile/Library/com.apple.icloud.searchpartyd/`**  
    **`/private/var/mobile/Library/Caches/com.apple.findmy.fmipcore/Items.data`**

## References

2026-03: <https://thebinaryhick.blog/2026/03/22/old-dog-new-tricks-lost-apples-2-0/>

2025-08: <https://thebinaryhick.blog/2025/08/19/further-observations-more-on-ios-search-party/>

2024-09: <https://thebinaryhick.blog/2024/09/02/where-the-wild-tags-are-other-airtag-stories/>

2022-04: <https://blog.d204n6.com/2022/04/airtag-youre-it.html>

## Tools

ArtEx2 (Find My) - <https://www.doubleblak.com/app.php?id=ArtEx2>

iLEAPP (findMyItemsInfo) - <https://github.com/abrignoni/iLEAPP>

Lost Apples - <https://github.com/joshuahickman1/Lost_Apples>
