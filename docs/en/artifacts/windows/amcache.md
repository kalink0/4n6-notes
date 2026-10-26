---
title: "AmCache - Application Activity Cache"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [installed-software, program-execution]
---

# AmCache - Application Activity Cache

## Meaning

The AmCache is part of the Windows compatibility infrastructure. It stores information on program files (executables, DLLs), installed applications as well as devices and drivers. The aim is to regularly check the compatibility of programs and drivers and thus ensure fast and trouble-free execution. The entries are created and updated, among other things, by a scheduled task (Microsoft Compatibility Appraiser).

From a digital forensics perspective, an entry shows that the application or driver was accessible to the system at the time of recording, locally, on a removable drive or on a network drive. Entries also provide identifying characteristics such as hash values, paths and signature. It does not show, however, that the application or driver was executed, nor that the timestamp of an entry corresponds to the time the file arrived on the system.

## Key facts

1. Availability: natively from Windows 8; retrofitted to Windows 7 through updates (before that RecentFileCache.bcf)
2. Prerequisites: enabled by default
3. Format and structure: registry hive; structure depends on Windows version and update level
4. Timestamps: FILETIME, UTC; LastWrite time of an entry = last update, not execution
5. Special features and pitfalls: SHA1 for large files only over the first 30 MB; include transaction logs (`.LOG1`/`.LOG2`)
6. Location:  
   **`C:\Windows\AppCompat\Programs\Amcache.hve`**

## References

2025-10: <https://securelist.com/amcache-forensic-artifact/117622/>

2024-10: <https://www.magnetforensics.com/blog/shimcache-vs-amcache-key-windows-forensic-artifacts/>

2024-05: <https://www.thedfirspot.com/post/evidence-of-program-existence-amcache>

2019-07: <https://cyber.gouv.fr/sites/default/files/2019/01/anssi_dfirsummit_2019-amcache_investigation.pdf>

2019-01: <https://cyber.gouv.fr/sites/default/files/2019/01/anssi-coriin_2019-analysis_amcache.pdf>

## Tools

AmcacheParser - <https://github.com/EricZimmerman/AmcacheParser>

AmCache-EvilHunter - <https://github.com/cristianzsh/amcache-evilhunter>

RegRipper (amcache) - <https://github.com/keydet89/RegRipper4.0>
