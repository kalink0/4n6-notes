---
title: "Samsung Secure Folder HistoryLog"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-existence, data-transfer]
---

# Samsung Secure Folder HistoryLog

## Meaning

The Samsung Secure Folder HistoryLog logs move operations of files and folders between an Android user profile and a Secure Folder. The entries contain the source and target UID, the number of files and the new locations.

From a digital forensics perspective, the entries show that a move operation with the respective logged values took place.

## Key facts

1. `request` records the request, `result` the response. A definite match via a shared ID is not possible.
2. Individual file names are not stored.
3. Timestamps: stored as a string, time zone unknown.
4. Location:  
   **`/data/data/com.samsung.knox.securefolder/databases/history_log_database`**

## References

2026-06: <https://github.com/4n6Wizard/Samsung-HistoryLog-Parser>

## Tools

ALEAPP (Samsung Secure Folder - History Log) - <https://github.com/abrignoni/ALEAPP>

Samsung Secure Folder History Log Parser - <https://github.com/4n6Wizard/Samsung-HistoryLog-Parser>
