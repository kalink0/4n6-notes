---
title: "Factory Reset"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [device-state]
---

# Factory Reset

## Meaning

A factory reset ("Erase All Content and Settings") deletes the user data of an iPhone. On the first start afterwards, iOS creates several files anew and logs the initial setup, so that the reset and its approximate time can be reconstructed.

From a digital forensics perspective, these traces show that the device was reset and then restarted or set up again, and roughly when this first start took place. It does not show, however, that a later reset can be ruled out if only older traces can be seen after a restore from an iCloud backup.

| Entry type | Shows | Relevant fields |
| --- | --- | --- |
| `.obliterated` | First start after the reset | Creation time of the file |
| `containermanager.log.{N}` | First start after the reset and distinction from an update: the previous build is missing in the OS version check | – |
| `com.apple.purplebuddy.plist` | Initial setup after the reset or restore from an iCloud backup | `GuessedCountry`, `SetupState` |
| `AddressBook.sqlitedb`, `CallHistory.storedata` | Newly created shortly after the reset | Creation time of the file |

## Key facts

1. `.obliterated` and the containermanager logs are only included in full file system extractions, the purplebuddy.plist also in iTunes backups
2. For the containermanager logs, the file with the highest number is the oldest
3. The containermanager logs are in device time; before the initial setup this is US Pacific Time (UTC-8)
4. `GuessedCountry` only marks the first start if `SetupState` has the value `SetupUsingAssistant`; `RestoredFromiCloudBackup` can point to an older reset
5. `SetupLastExit` is unreliable, it also changes with later settings changes (e.g. Apple Pay)
6. For AddressBook and CallHistory, the creation time counts, not the modification time
7. Locations:  
   **`/private/var/root/.obliterated`**  
   **`/private/var/root/Library/Logs/MobileContainerManager/containermanager.log.{N}`**  
   **`/private/var/mobile/Library/Preferences/com.apple.purplebuddy.plist`**  
   **`/private/var/mobile/Library/AddressBook/AddressBook.sqlitedb`**  
   **`/private/var/mobile/Library/CallHistoryDB/CallHistory.storedata`**

## References

2026-06: <https://cellebrite.com/en/blog/upgrade-from-null-detecting-ios-wipe-artifacts/>

## Tools

ArtEx2 (Wipe Events) - <https://www.doubleblak.com/app.php?id=ArtEx2>

iLEAPP (wipe_indicators) - <https://github.com/abrignoni/iLEAPP>
