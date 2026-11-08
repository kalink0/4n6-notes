---
title: "MRU - WordWheelQuery"
status: complete
completed: 2026-11-06
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [commands-input]
---

# MRU - WordWheelQuery

## Meaning

Per user account, File Explorer stores the terms that were searched for in the Explorer search box. It uses them to suggest earlier search terms the next time the user types. The terms are kept in the registry as an MRU (Most Recently Used) list, ordered by the respective last search.

From a digital forensics perspective, an entry shows that the term was searched for in the File Explorer search box in the context of the user account. The order shows the sequence in which the terms were last searched. The folder or drive that was searched and the results found are not stored.

## Key facts

1. Since Windows 7 up to Windows 11; on Windows XP, the search history was kept in the `ACMru` key
2. Only records searches in the File Explorer search box, not searches in the Start menu or in Windows Search
3. A term is only stored once the search is run; a term that is searched again is not added twice but moves up in the order
4. Values named with numbers (`0`, `1`, `2` …), type REG_BINARY, term as a UTF-16LE string; the value name says nothing about age, as numbers are reused
5. Order via `MRUListEx`: a list of 4-byte values (little endian) holding the value names, newest first, terminated by `0xFFFFFFFF`
6. The last write time of the key only belongs to the newest term; older terms only have their position in the order
7. If the user opens a search result, an LNK file named after the search term (e.g. `passw.lnk`) is created in the folder **`%APPDATA%\Microsoft\Windows\Recent`**; it also holds the search location, and its timestamps then give the time of the search
8. Location:  
   **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery`**

## References

2026-05: <https://forenza.io/registry-ntuser-word-wheel/>

2020-02: <https://cloud.google.com/blog/topics/threat-intelligence/the-missing-lnk-correlating-user-search-lnk-files>

## Tools

DLEAPP (parser: Explorer Search History) - <https://github.com/abrignoni/DLEAPP>

Registry Explorer (WordWheelQuery Plugin) - <https://ericzimmerman.github.io/>

RegRipper (wordwheelquery) - <https://github.com/keydet89/RegRipper4.0>

regipy (plugin: word_wheel_query) - <https://github.com/mkorman90/regipy>

juntei (parse-registry mru) - <https://github.com/Yamato-Security/juntei>
