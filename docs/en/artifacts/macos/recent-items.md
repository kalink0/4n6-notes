---
title: "Recent Items"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-access, program-execution, network]
---

# Recent Items

## Meaning

macOS keeps lists of recently used applications, documents and servers per user, e.g. in the Apple menu under "Recent Items" and in applications under "Open Recent". Through them, the user can quickly open these items again.

From a digital forensics perspective, an entry shows that the document was opened, the application was launched or the connection to the server was established via the user account, and where the item was located at that time. A time of use cannot be derived from it.

## Key facts

1. Up to macOS 10.10 as plist files, from macOS 10.11 as shared file lists (**`.sfl`**, from 10.13 **`.sfl2`**, later **`.sfl3`** and **`.sfl4`**)
2. Older shared file list files are retained after an upgrade, so a list can exist under several extensions
3. No timestamp of use; the order of the entries indicates how recent they are
4. The length of the list is limited, the oldest entry drops out when it is exceeded
5. The creation date contained in the bookmark is that of the target file, not the time of use
6. Lists of individual applications are only updated while the application is running and can therefore contain very old entries
7. Location:  
   Up to macOS 10.10: **`/Users/{USER}/Library/Preferences/com.apple.recentitems.plist`**  
   **`/Users/{USER}/Library/Preferences/*LSSharedFileList.plist`**  
   From macOS 10.11: **`/Users/{USER}/Library/Application Support/com.apple.sharedfilelist/`**  
   From macOS 10.11 (one list per application): **`/Users/{USER}/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.ApplicationRecentDocuments/`**

## References

2023-08: <https://eclecticlight.co/2023/08/04/recent-items-property-lists-bookmarks-and-resolvers/>

2017-08: <https://eclecticlight.co/2017/08/10/recent-items-launch-services-and-sharedfilelists/>

2016-07: <https://www.mac4n6.com/blog/2016/7/10/new-script-macmru-most-recently-used-plist-parser>

## Tools

DLEAPP (parser: Shared File Lists (sfl2, sfl3, sfl4)) - <https://github.com/abrignoni/DLEAPP>

mac_apt (plugin: RECENTITEMS) - <https://github.com/ydkhatri/mac_apt>

macMRU-Parser - <https://github.com/mac4n6/macMRU-Parser>
