---
title: "Notifications"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [communication]
---

# Notifications

## Meaning

Programs inform the user through notifications, e.g. about new emails, chat messages or reminders. macOS displays them and stores the delivered notifications in a database so that the user can read them later in Notification Center.

From a digital forensics perspective, an entry shows that the program delivered a notification with the stored content to the user account at the stored time. An entry does not show that the user saw or read the notification.

## Key facts

1. Title, subtitle and text of the notification are stored as a binary plist in the database
2. Content is retained even if the program deletes the message itself (e.g. disappearing messages)
3. Timestamps in Cocoa format (seconds since 2001-01-01), UTC
4. Under **`/private/var/folders`**, the assignment to the user is made via the owner (UID) of the folder
5. After an upgrade, older databases may be present next to the current one
6. Protected by TCC from macOS 15; cannot be read on a running system without permission
7. Location:  
   Up to macOS 10.9: **`/Users/{USER}/Library/Application Support/NotificationCenter/{UUID}.db`**  
   macOS 10.10 to 10.12: **`/private/var/folders/{XX}/{ID}/0/com.apple.notificationcenter/db/db`**  
   macOS 10.13 to 14: **`/private/var/folders/{XX}/{ID}/0/com.apple.notificationcenter/db2/db`**  
   From macOS 15: **`/Users/{USER}/Library/Group Containers/group.com.apple.usernoted/db2/db`**

## References

2024-09: <https://9to5mac.com/2024/09/01/security-bite-apple-addresses-privacy-concerns-around-notification-center-database-in-macos-sequoia/>

2021-09: <https://www.sentinelone.com/labs/macos-incident-response-part-2-user-data-activity-and-behavior/>

2018-05: <https://objective-see.org/blog/blog_0x2E.html>

## Tools

DLEAPP (parser: Notification Center Records) - <https://github.com/abrignoni/DLEAPP>

mac_apt (plugin: NOTIFICATIONS) - <https://github.com/ydkhatri/mac_apt>

Plaso (parser: mac_notificationcenter) - <https://github.com/log2timeline/plaso>
