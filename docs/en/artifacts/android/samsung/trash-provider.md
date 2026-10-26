---
title: "Samsung Trash Provider"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de:sha256:943987f935bc
topics: [file-existence]
---

# Samsung Trash Provider

## Meaning

The Samsung Trash Provider is a system component on Samsung devices that manages the shared trash for Samsung apps such as My Files and Gallery. Deleted files are first moved to the trash so that the user can restore them within the retention period. For this, the provider stores the original location and name of each file as well as the time of deletion.

From a digital forensics perspective, an entry shows that the file was moved to the trash at the given time from within the named app under the given user, as well as under which name and in which location it was stored before.

## Key facts

1. The data in the trash is kept for approx. 30 days from deletion
2. Shared trash for My Files, Gallery and Voice Recorder since One UI 6.0; in older versions the apps have their own trash
3. The path of the file in the trash contains the app context, original path and file name and can be analysed even without the database
4. When a file is restored, the database entry is deleted immediately; after the retention period has expired, the entry can remain although the file has been removed
5. Entries from the Secure Folder can be recognised by the user ID 150
6. Timestamps: Unix time in milliseconds (UTC)
7. Location:  
   Database: **`/data/data/com.samsung.android.providers.trash/databases/trash.db`**  
   Files: **`/data/media/{USER_ID}/Android/.Trash/`**

## References

2026-02: <https://bebinary4n6.blogspot.com/2026/02/samsung-trash-provider-app-traces-of.html>

2024-01: <https://www.samsung.com/uk/support/apps-services/the-updated-recycle-bin-feature-in-my-files-on-galaxy-devices-with-one-ui-6/>

## Tools

ALEAPP (parser: Samsung Trash, My Files Trash) - <https://github.com/abrignoni/ALEAPP>
