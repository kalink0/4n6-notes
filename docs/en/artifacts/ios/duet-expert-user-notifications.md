---
title: "Duet Expert User Notifications"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [notifications]
---

# Duet Expert User Notifications

## Meaning

In a database in the DuetExpertCenter area, iOS keeps a history of the notifications received on the device. It stores metadata such as the app the notification came from, the time of receipt and identifiers of the conversation or the sender. The text of the notification is not stored, only its length. What Apple uses the database for is not documented.

From a digital forensics perspective, an entry shows that a notification from the given app was received on the device at the given time, depending on the app with an identifier of the conversation or the sender, e.g. a phone number. It does not show, however, the content of the notification or whether the user read it or reacted to it.

## Key facts

1. Observed from iOS 15 to iOS 26 (as of 2026-07)
2. Entries go back about 60 days
3. SQLite database, table `notifications`
4. Timestamps in Mac Absolute Time format (seconds since 2001-01-01, UTC)
5. Where the sender identifier is stored depends on the app, e.g. phone number for WhatsApp and Signal mostly in `rawIdentifier`, for SMS in `ThreadID`
6. Location:  
   **`/private/var/mobile/Library/DuetExpertCenter/notificationAndSuggestionDB.db`**

## References

2026-07: <https://blog.digital-forensics.it/2026/07/after-signal-fix-exploring-apples.html>

## Tools

iLEAPP (duetNotifications) - <https://github.com/abrignoni/iLEAPP>
