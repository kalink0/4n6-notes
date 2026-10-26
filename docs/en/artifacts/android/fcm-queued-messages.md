---
title: "FCM Queued Messages"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [notifications, communication]
---

# FCM Queued Messages

## Meaning

Firebase Cloud Messaging (FCM) is Google's service through which apps receive messages from their servers on the device, e.g. notifications, chat messages or control data. This way, not every app has to keep its own connection to its server open. Google Play services receive the messages, put them in a queue and pass them on to the respective app.

From a digital forensics perspective, an entry shows that the named app received a message from its server at the given time, with the content the server sent along.

It does not show that the user saw or opened the message.

## Key facts

1. Present from Android 10
2. Contains only incoming messages from the server to the app
3. Depending on the app, e.g.:
   - sender and recipient
   - message text
   - type of notification
   - location data
   - only a reference (URL) through which the app retrieves the actual content
4. Entries are deleted as soon as Google Play services have passed the message on to the app
5. Timestamp in the key: Unix time in microseconds, time the message was received
6. Location:  
   **`/data/data/com.google.android.gms/files/fcm_queued_messages.ldb/`**

## References

2024-11: <https://forensafe.com/blogs/AndroidFCM.html>

2020-11: <https://www.cclsolutionsgroup.com/post/fcm-queued-messages-on-android>

## Tools

ALEAPP (parser: FCM Dump, plus app-specific FCM parsers) - <https://github.com/abrignoni/ALEAPP>

crush (LevelDB viewer) - <https://github.com/kalink0/crush-forensics>
