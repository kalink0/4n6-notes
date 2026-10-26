---
title: "Quick Look Cache"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-existence]
---

# Quick Look Cache

## Meaning

Quick Look creates thumbnails and previews of file contents, e.g. for the icons in the Finder or the preview with the space bar, without the file having to be opened in its program. So that the thumbnails do not have to be created anew each time, macOS stores them per user in a cache.

From a digital forensics perspective, an entry shows that the file was present and a thumbnail was created for it, e.g. because its folder was displayed in the Finder. The thumbnail shows the content of the file at the time of creation, even if the file has since been deleted or was stored on a volume that is no longer available. An entry does not show that the file was opened.

## Key facts

1. The cache is located outside the home directory; the assignment to the user is made via the owner (UID) of the folder
2. Up to macOS 10.14 with path and file name, from macOS 10.15 only with file ID (inode); the assignment to the file is then only possible via the file system
3. Also contains thumbnails of files on external and encrypted volumes that are no longer mounted (tested on macOS 10.13)
4. The stored modification date and file size belong to the original file, not to the cache entry
5. Timestamps in Cocoa format (seconds since 2001-01-01), UTC
6. What is counted as an access (hit) has not been clarified
7. Protected by the system from macOS 10.14; cannot easily be read on a running system
8. The user can clear the cache with **`qlmanage -r cache`**
9. Location:  
   **`/private/var/folders/{XX}/{ID}/C/com.apple.QuickLook.thumbnailcache/`**

## References

2024-04: <https://eclecticlight.co/2024/04/05/a-quick-look-at-quicklook-and-its-problems/>

2018-06: <https://objective-see.org/blog/blog_0x30.html>

2018-06: <https://arsenalrecon.com/insights/quick-look-cache-parsing>

2016-05: <http://az4n6.blogspot.com/2016/05/quicklook-python-parser-all-your-blobs.html>

## Tools

DLEAPP (parser: QuickLook Thumbnails) - <https://github.com/abrignoni/DLEAPP>

mac_apt (plugin: QUICKLOOK) - <https://github.com/ydkhatri/mac_apt>

OSX-QuickLook-Parser - <https://github.com/mdegrazia/OSX-QuickLook-Parser> (old versions only)
