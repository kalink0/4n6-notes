---
title: "Thumbcache"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-existence]
---

# Thumbcache

## Meaning

The Microsoft Windows operating system comes with the thumbnail cache feature to give users a better experience when they, for example, navigate in Windows Explorer and want to search for or view files. The thumbnail cache reduces the loading times of files by generating thumbnails that can be loaded quickly when the user of the system wants to display the files in Windows Explorer or navigates in a folder. The thumbnails show the content or part of the content of the original file in reduced size.

From a digital forensics perspective, the existence of a file in the thumbnail cache allows the statement that the original file was or is stored on a currently or formerly connected drive (including network drives).
The thumbnail cache alone does not allow an exact statement about what exactly a user did with the file, for example whether the user actively viewed, copied or otherwise used the file.

## Key facts

1. The original path can be determined under certain circumstances (see additional notes)
2. Location:  
   **`%LOCALAPPDATA%\Microsoft\Windows\Explorer\thumbcache_*.db`**

### Additional notes (forensics)

#### Path to the original file

The original path of the file is not stored in the thumbnail cache. There are several ways to find the original file, if possible.

1. Calculating the ThumbnailCacheID of all available files and comparing it with the ThumbnailCacheIDs in the thumbnail cache.
2. Checking Windows Search (Windows.edb, from Windows 11 Windows.db) for the ThumbnailCacheID from the thumbnail cache.
3. Checking all available files for visual equality

For approaches 1 and 3, the original file must still be present in the data. The calculation of the ThumbnailCacheID (approach 1) must be done on the same system on which the thumbnail cache was created.

For the older version, thumbs.db, the original path of the file follows from the location of the thumbs.db itself. This thumbs.db is created in the respective folder of the original file. For network folders, thumbs.db is still created in current Windows versions.

## References

2026-07: <https://www.it-connect.tech/windows-forensics-part-6-analyzing-image-caches/>

2025-08: <https://www.pentestpartners.com/security-blog/thumbnail-forensics-dfir-techniques-for-analysing-windows-thumbcache/>

2023-09: <https://it-forensik.fiw.hs-wismar.de/index.php/Stefan_Augustin>

2012-01: <http://computerforensics.parsonage.co.uk/downloads/UnderMyThumbs.pdf>

## Tools

Thumbcache Viewer - <https://thumbcacheviewer.github.io/>

Thumb Viewer - <https://thumbsviewer.github.io/>

DLEAPP (parser: Thumbnail Cache) - <https://github.com/abrignoni/DLEAPP>

Dissect (plugin: thumbcache) - <https://docs.dissect.tools/en/stable/plugins/thumbcache.html>
