---
title: "Apple Remote Desktop"
status: complete
completed: 2026-11-07
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution, accounts]
---

# Apple Remote Desktop

## Meaning

Apple Remote Desktop (ARD) is Apple's software for managing multiple Macs. The managed Macs (clients) run the Remote Management service; the Remote Desktop program runs on the administrator's Mac. Following a reporting policy set by the administrator, the client collects data on program usage, user logins, the system and a list of all files in local cache files. At the scheduled time (by default daily at midnight) it transfers them to the admin Mac or a Task Server, which stores them in its database and additionally keeps each client's cache files.

From a digital forensics perspective, the program usage entries show that a program ran on the client, with launch time, run length and user. The login entries show login and logout times of a user with the session type (console, terminal, SSH) and partly the originating computer. The admin Mac holds this data for all reporting clients, even if it has already been deleted on the client itself. Independently of reporting, the content `enabled` in the Remote Management launch configuration shows that it was turned on, e.g. via the `kickstart` command.

| Entry type | Shows | Relevant fields |
| --- | --- | --- |
| `AppUsage.plist` (client) | Program ran on the client, with launch time, run length and user | `Launched`, `runLength`, `Frontmost`, `userName` |
| `UserAcct.tmp` (client) | Login and logout of a user on the client | `inTime`, `outTime`, `host` |
| `filesystem.cache` (client) | File was present on the client at the time of collection | |
| `rmdb.sqlite3` (admin) | Program usage and logins of all reporting clients | |
| `RemoteManagement.launchd` (client) | Remote Management was turned on | |

## Key facts

1. The paths are described for macOS 10.14; for newer versions they are not publicly documented
2. Data is only created if Remote Management is active on the client; program usage and logins only if the administrator's reporting policy collects them. Database and client copies only on the admin Mac with Remote Desktop installed
3. The cache files on the client are often deleted after the transfer to the admin Mac; the admin Mac's database can contain data from more than a year
4. Plists (`AppUsage.plist` XML or binary, `AppUsage.tmp` and `UserAcct.tmp` binary), `filesystem.cache` as a database, admin database SQLite
5. Timestamps in the plists as Mac Absolute Time (seconds since 2001-01-01, UTC)
6. On the admin Mac, the copies of the client caches are named after the MAC address of the respective client
7. According to Mandiant, launch time and frontmost time of program usage are labeled the wrong way round in the admin database (checked on macOS 10.14)
8. `AppUsage.tmp` usually contains the same or fewer entries than `AppUsage.plist`
9. Location:  
   Client: **`/private/var/db/RemoteManagement/caches/`**  
   Client: **`/Library/Application Support/Apple/Remote Desktop/RemoteManagement.launchd`**  
   Admin: **`/private/var/db/RemoteManagement/RMDB/rmdb.sqlite3`**  
   Admin: **`/private/var/db/RemoteManagement/ClientCaches/`**

## References

2026-11 (accessed): <https://support.apple.com/guide/remote-desktop/apd36ca108c/mac>

2019-10: <https://cloud.google.com/blog/topics/threat-intelligence/leveraging-apple-remote-desktop-for-good-and-evil/>

## Tools

### Core tools

mac_apt (Plugin: ARD) - <https://github.com/ydkhatri/mac_apt>

### Other tools

ARDvark - <https://github.com/mandiant/ARDvark>
