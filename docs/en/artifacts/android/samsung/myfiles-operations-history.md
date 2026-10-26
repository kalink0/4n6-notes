---
title: "Samsung MyFiles Operations History"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-existence]
---

# Samsung MyFiles Operations History

## Meaning

The Samsung MyFiles Operations History stores file operations on folders and files. The operations create, rename, move, copy and delete are stored per file/folder. The operation must have been carried out with the Samsung file manager. If another app is used, the data is not written.

From a digital forensics perspective, the entries mean that the respective file/folder, including the files/folders it contains, was changed at the given time according to the given operation, i.e. for example created, copied, renamed or deleted.

## Key facts

1. If MyFiles was used this way, the database exists per user and for the Secure Folder
2. Only file operations carried out via the Samsung MyFiles app are listed in it.
3. No automatic deletion observed; entries went back approx. 1.5 years
4. Timestamps: stored as text, UTC
5. Location:  
   **`/data/data/com.sec.android.app.myfiles/databases/OperationHistory.db`**  
   **`/data/user/{USER_ID}/com.sec.android.app.myfiles/databases/OperationHistory.db`**

## References

2026-01: <https://bebinary4n6.blogspot.com/2026/01/android-samsung-my-files-app-exploring.html>

## Tools

ALEAPP (parser: My Files Operation History, My Files - File Operations) - <https://github.com/abrignoni/ALEAPP>

SELECT queries - <https://github.com/kalink0/useful_scripts/blob/master/sql/Android/Samsung%20Apps/sMyFiles.sql>
