---
title: "MRU - TypedPaths"
status: complete
completed: 2026-11-06
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-access]
---

# MRU - TypedPaths

## Meaning

Per user account, File Explorer stores the paths that were typed or pasted into its address bar. It offers them again in the address bar's drop-down list the next time the user types. Besides local folders and network shares, these can also be programs started from the address bar by path or name.

From a digital forensics perspective, an entry shows that the path was typed or pasted into the File Explorer address bar in the context of the user account and that Explorer could resolve it at that time.

## Key facts

1. Windows 7 to Windows 11
2. A maximum of 25 entries; the newest entry is always in `url1`, older ones move down, the oldest one drops out
3. Values `url1` to `url25`, type REG_SZ; the order follows from the value name, there is no `MRUList`
4. Only paths that could be resolved when typed are stored; inputs that cannot be resolved are not
5. According to several tests, the entries are only written to the key when the Explorer window is closed; the last write time of the key is then the time of closing, not of the input
6. If several Explorer windows are open, each keeps its own list; the window closed last overwrites the key, and entries from the other windows are lost
7. Cleared with "Clear File Explorer history" in the folder options
8. Location:  
   **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths`**

## References

2024-03: <https://artefacts.help/windows_registry_typedpaths.html>

2021-10: <https://forensafe.com/blogs/typedpaths.html>

2018-09: <https://www.hecfblog.com/2018/09/daily-blog-483-typed-paths-amnesia.html>

## Tools

### Core tools

DLEAPP (parser: Explorer Typed Paths) - <https://github.com/abrignoni/DLEAPP>

RECmd (Kroll_Batch) - <https://ericzimmerman.github.io/>

TRACE - <https://github.com/Gadzhovski/TRACE-Forensic-Toolkit>

### Other tools

juntei (parse-registry mru) - <https://github.com/Yamato-Security/juntei>

Plaso (parser: windows_typed_urls) - <https://github.com/log2timeline/plaso>

regipy (plugin: typed_paths) - <https://github.com/mkorman90/regipy>

RegRipper (typedpaths) - <https://github.com/keydet89/RegRipper4.0>
