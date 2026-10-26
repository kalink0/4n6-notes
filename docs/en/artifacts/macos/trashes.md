---
title: "Trashes Folder"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-existence]
---

# Trashes Folder

## Meaning

The Trash contains files and folders that the user has deleted in the Finder. Until the Trash is emptied, the user can move them back to their original location with "Put Back". For this, the Finder stores the original name and location of each item in the .DS_Store file of the Trash.

From a digital forensics perspective, an item in the Trash shows that it was moved to the Trash via the user account to which the Trash belongs. A Put Back entry additionally shows under which name and in which location the item was stored before. A time of deletion cannot be derived from it.

## Key facts

1. The original name and location are stored in the **`.DS_Store`** of the Trash, not with the item itself
2. No time of deletion is stored
3. The original location is sometimes given in the firmlink form **`System/Volumes/Data/…`**
4. Put Back entries are retained after putting back or emptying the Trash until the next restart (tested up to macOS 10.12)
5. A Put Back entry may be missing for items in the Trash (observed on macOS 15 and 26)
6. With "Delete Immediately", items are deleted without going through the Trash
7. Optional automatic emptying after 30 days (Finder setting); deleted iCloud Drive items are always removed after 30 days
8. Location:  
   On the disk with the home directory: **`/Users/{USER}/.Trash/`**  
   On all other disks: **`/.Trashes/{UID}/`**  
   iCloud Drive: **`/Users/{USER}/Library/Mobile Documents/com~apple~CloudDocs/.Trash/`**

## References

2026-10 (accessed): <https://support.apple.com/guide/mac-help/delete-files-and-folders-on-mac-mchlp1093/26/mac>

2019-07: <https://papers.put.as/papers/macosx/2019/summit_archive_1565288427.pdf>

2017-01: <https://ponderthebits.com/2017/01/mac-dumpster-diving-identifying-deleted-file-references-in-the-trash-ds_store-files-part-1/>

## Tools

DLEAPP (parser: Trash Put Back) - <https://github.com/abrignoni/DLEAPP>

DSStoreParser - <https://github.com/nicoleibrahim/DSStoreParser>

mac_apt (plugin: TRASH) - <https://github.com/ydkhatri/mac_apt>
