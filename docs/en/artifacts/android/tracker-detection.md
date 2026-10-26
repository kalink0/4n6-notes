---
title: "Tracker Detection"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [location, external-devices]
---

# Tracker Detection

## Meaning

Through Google Play services, Android warns about unknown Bluetooth trackers moving along with the device. These are AirTags and trackers from the Find My Device network (FMD), the latter since May 2024. For this, the device scans passively. The user can also scan manually. If a tracker is classified as "following", a message appears that an unknown tracker is travelling with the user.

Traces from both sides can be present on the same device:

- **Tracked side (device was tracked / has seen trackers):**
    - Which trackers were detected nearby: MAC, time of first and last detection.
    - Location and motion state of the device for each scan, regardless of whether an alert was triggered.
    - Whether and when an alert was triggered (STAGED) and shown (SENT).
    - When the last scan took place. In some cases it can also be seen whether passive scanning is on or off.
    - Whether the alert was actually shown as a notification. This can only be shown if notification history is enabled.
- **Owner side (device belongs to the owner of a tracker):**
    - Which Fast Pair accessories (including FMD trackers) are known to the device: MAC, name or name given by the user, times of first and last observation.

**Not shown:**

- The location history of the user's own trackers. It is not stored locally on the device.
- The identity of the owner of someone else's tracker. For FMD trackers a ring key is stored, through which Google can identify the owner. Locally, the owner cannot be seen.
- A lasting attribution via the MAC. Trackers rotate their MAC address.
- That a Fast Pair entry shows an actual pairing.

| Entry type (in ...) | Shows | Relevant fields |
|---|---|---|
| Scan (`personalsafety_db`) | Tracked | All trackers seen, including manual scans; MAC, first/last detection, `state` (`STATE_STILL`, `STATE_MOVING`), BLOB `locationScan` (location of the device) |
| DeviceData (`personalsafety_db`) | Tracked | Alerts with status STAGED / SENT; for FMD trackers model and ring key |
| `personalsafety_info.pb` | Tracked | Time of the last scan (Unix ms) |
| `personalsafety_optin.pb` | Tracked | Status of passive scanning |
| Notification history (`notification_history`) | Tracked | Package, time and content of the tracker alert |
| `nearby_fast_pair_item_cache.db` | Owner | MAC, device name, title (name given by the user), first and last observation, image |

## Key facts

1. **Retention:** Scan entries are only kept for about two days. An empty database does not show that scanning was disabled.

2. **Location:** `locationScan` contains latitude and longitude of the device at scan time (Protobuf, values × 10,000,000), `state` the motion state.

3. **`personalsafety_optin.pb`:** The file is not always present. The values 1 = on, 2 = off are not conclusively confirmed.

4. **Notification history:** It is only written if the user has enabled it.

5. **Fast Pair cache:** Entries remain even after unpairing. An entry does not reliably show that the accessory was paired.

6. Locations:  
   **`/data/data/com.google.android.gms/databases/personalsafety_db`**  
   **`/data/data/com.google.android.gms/files/personalsafety/shared/`** (`personalsafety_info.pb`, `personalsafety_optin.pb`)  
   **`/data/system_ce/{USER_ID}/notification_history/history/`**  
   **`/data/data/com.google.android.gms/files/nearby-fast-pair/nearby_fast_pair_item_cache.db`** (LevelDB)

## References

2026-10 (accessed): <https://support.google.com/android/answer/13658562>

2024-08: <https://thebinaryhick.blog/2024/08/23/not-all-androids-who-wonder-are-lost-a-look-at-androids-find-my-device-network/>

2023-08: <https://thebinaryhick.blog/2023/08/13/android-airtags-part-ii/>

## Tools

ALEAPP (Android Airtag Alerts / Scans / Last Scan / Passive Scan, Android Notification History, Nearby - Fast Pair Devices) - <https://github.com/abrignoni/ALEAPP>
