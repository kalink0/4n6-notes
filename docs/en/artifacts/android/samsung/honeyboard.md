---
title: "Samsung Honeyboard"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de:sha256:09eb99e8d495
topics: [commands-input]
---

# Samsung Honeyboard

## Meaning

Honeyboard (com.samsung.android.honeyboard) is the Samsung keyboard, the default keyboard on Samsung devices. It keeps a clipboard history so that the user can paste previously copied texts and images again. It also stores words the user has removed from the word suggestions.

From a digital forensics perspective, an entry in the clipboard history shows that the content was copied to the clipboard from within the named app at the given time. It does not show that or where the content was pasted.

## Key facts

1. Copied texts are kept for about 30 days
2. Copied images are not stored in the database but as the file **`clip`** in a subfolder of **`clipboard`** whose name is a Unix timestamp in milliseconds
3. Older versions store the UID of the app instead of the package name, which has to be resolved via **`packages.xml`**
4. Timestamps: Unix time in milliseconds (UTC)
5. Location:  
   **`[…]/com.samsung.android.honeyboard/`**  
   Clipboard (text): **`databases/ClipItem.db`**  
   Clipboard (images): **`clipboard/{TIMESTAMP}/clip`**  
   Removed word suggestions: **`databases/RemoveListManager`**

## References

2024-05: <https://forensafe.com/blogs/SamsungClipboard.html>

## Tools

ALEAPP (parser: Samsung Honeyboard - Clipboard, Samsung Honeyboard - Clipboard Image Clips) - <https://github.com/abrignoni/ALEAPP>

SELECT queries - <https://github.com/kalink0/useful_scripts/blob/master/sql/Android/Samsung%20Apps/sHoneyboard.sql>
