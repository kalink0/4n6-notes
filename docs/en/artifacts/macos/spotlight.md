---
title: "Spotlight Database"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-existence]
---

# Spotlight Database

## Meaning

Spotlight is the system-wide search of macOS. So that the user can quickly find files by name, content or properties, macOS creates a database with the metadata and text content of the files for each indexed volume.

From a digital forensics perspective, an entry in the Spotlight database shows that the file with the stored metadata was present on the volume at the time of indexing. Entries can still be present after the file has been deleted. Depending on the file type, an entry contains further metadata, e.g. on usage or on the origin of a download; what these show depends on the respective attribute.

## Key facts

1. Only present on indexed volumes; individual folders and volumes can be excluded via the Spotlight privacy settings
2. Two databases per store: **`.store.db`** (current) and **`store.db`** (copy updated with a delay)
3. Entries of deleted files are kept in **`store.db`** for a while; deleted database pages can be recovered from free space
4. Format not documented by Apple, with compressed pages
5. Not every date field is a real timestamp, some contain placeholder values (e.g. year 2247)
6. Location:  
   **`/Volumes/{VOLUME}/.Spotlight-V100/Store-V2/{UUID}/`** (root directory of a drive)  
   Startup volume from macOS 10.15: **`/System/Volumes/Data/.Spotlight-V100/Store-V2/{UUID}/`**

## References

2026-07: <https://eclecticlight.co/2026/07/04/spotlight-and-core-spotlight-are-different/>

2024-01: <https://github.com/libyal/dtformats/blob/main/documentation/Apple%20Spotlight%20store%20database%20file%20format.asciidoc>

2021-10: <https://www.forensicfocus.com/webinars/shining-a-light-on-spotlight-leveraging-apples-desktop-search-utility-to-recover-deleted-file-metadata-on-macos/>

2019-07: <https://papers.put.as/papers/macosx/2019/summit_archive_1564171500.pdf>

2019-04: <https://doi.org/10.1016/j.diin.2019.01.019>

## Tools

DLEAPP (parser: Spotlight Store Files) - <https://github.com/abrignoni/DLEAPP>

mac_apt (plugin: SPOTLIGHT) - <https://github.com/ydkhatri/mac_apt>

spotlight_parser - <https://github.com/ydkhatri/spotlight_parser>
