---
title: "ShimCache - AppCompatCache"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution, file-existence]
---

# ShimCache - AppCompatCache

## Meaning

The ShimCache is a feature in Windows systems that ensures older programs can run on the latest Windows systems.

The file path, the file name, the file size (Windows XP/Server 2003 only) and the last modification date can be read.

From a digital forensics perspective, entries in the ShimCache mean that:

1. If the field "Is Executed" is true: the file with the given name was executed on the system under the given path
2. If the field "Is Executed" is false: the file with the given name was located under the given path

This artifact does not allow a statement about the exact time - but it does allow one about the chronological order of the events.

## Key facts

1. Current/new ShimCaches are only written to the registry when the system is restarted/shut down
2. The ShimCache contains up to 1024 entries
3. The field "Is Executed" only exists from Windows Vista
4. Location (registry):  
   Windows XP: **`HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatibility\AppCompatCache`**  
   From Windows Vista: **`HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache\AppCompatCache`**

## References

2024-10: <https://www.magnetforensics.com/blog/shimcache-vs-amcache-key-windows-forensic-artifacts/>

2024-08: <https://nullsec.us/windows-10-11-appcompatcache-deep-dive/>

2015-06: <https://cloud.google.com/blog/topics/threat-intelligence/caching-out-the-val/>

## Tools

AppCompatCacheParser - <https://ericzimmerman.github.io/>

RegRipper (plugin: appcompatcache) - <https://github.com/keydet89/RegRipper4.0>

DLEAPP (parser: AppCompatCache (Shimcache)) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (artifact: Windows.Registry.AppCompatCache) - <https://docs.velociraptor.app/artifact_references/pages/windows.registry.appcompatcache/>

Dissect (plugin: shimcache) - <https://docs.dissect.tools/en/stable/plugins/shimcache.html>

Volatility 3 (plugin: windows.shimcachemem, from memory) - <https://github.com/volatilityfoundation/volatility3>
