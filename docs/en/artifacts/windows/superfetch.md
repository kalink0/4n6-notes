---
title: "Superfetch"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution]
---

# Superfetch

## Meaning

Superfetch is an extension of Prefetch that was introduced with Windows Vista. While Prefetch speeds up the start of individual programs, Superfetch analyses usage behaviour over a longer period and preloads data into memory that is likely to be needed. Since Windows 10, Prefetch and Superfetch run together in the SysMain service. The service stores the results in its own database files.

From a digital forensics perspective, entries show that programs and files were used on the system, including those that have since been uninstalled. Exact execution times are not shown.

## Key facts

1. Since Windows Vista; since Windows 10 part of the SysMain service
2. Sometimes disabled on systems with an SSD
3. Records the usage of all users of the system, besides programs also paths of libraries and configuration files
4. Most databases are only written when the service stops, AgAppLaunch.db at startup
5. Compressed on newer systems (file extension .db.trx), not directly readable
6. Format only partially documented
7. Location:  
   **`C:\Windows\Prefetch\Ag*.db`**  
   **`C:\Windows\Prefetch\Ag*.db.trx`**

## References

2026-07: <https://www.it-connect.tech/forensic-windows-part-4-exploiting-superfetch-artifacts/>

2020-08: <https://i.blackhat.com/USA-20/Thursday/us-20-Venault-Fooling-Windows-Through-Superfetch.pdf>

2015-06: <https://blog.digital-forensics.it/2015/06/a-first-look-at-windows-10-prefetch.html>

2026-10 (accessed): <https://forensics.wiki/superfetch/>

## Tools

SysMainView - <https://github.com/MathildeVenault/SysMainView>

rewolf-superfetch-dumper - <https://github.com/rwfpl/rewolf-superfetch-dumper>

libagdb - <https://github.com/libyal/libagdb>
