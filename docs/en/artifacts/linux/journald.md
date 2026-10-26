---
title: "Journald"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [device-state]
---

# Journald

## Meaning

Journald (systemd-journald) is the central logging service on Linux systems with systemd. It collects messages from the kernel, system services, the boot phase and programs, and stores them together with metadata such as process, user and systemd unit in its own binary format. The journal is intended for administrators for troubleshooting and monitoring the system.

From a digital forensics perspective, an entry shows that the given process passed the respective message to the journal at the given time. What a message says about a user action depends on the individual message. It does not show, however, that an action did not take place if there is no entry.

## Key facts

1. Depending on distribution and configuration, data is only stored volatilely under /run/log/journal; these entries are lost after a reboot
2. Retention by size, by default at most 10% of the file system (maximum 4 GB); no time-based deletion, files are rotated after one month at the latest
3. system.journal contains the system messages, user-{UID}.journal the messages per user; rotated files have an @ in their name, files with the extension .journal~ were renamed after an unclean shutdown or corruption
4. Timestamps: real time in microseconds since 1970-01-01 (UTC), additionally monotonic time, which is only unique together with the boot ID
5. Fields with a leading underscore (e.g. _PID, _UID, _SYSTEMD_UNIT) are set by journald itself; the logging process cannot specify them, but it can specify the message text
6. Tamper protection (Forward Secure Sealing) only if a key has been set up for it
7. Binary format, partly compressed; the files cannot be read directly and must be decoded with journalctl or a parser
8. Location:  
   **`/var/log/journal/{MACHINE_ID}/`**  
   **`/run/log/journal/{MACHINE_ID}/`**

## References

2026-10 (accessed): <https://www.freedesktop.org/software/systemd/man/latest/journald.conf.html>

2026-10 (accessed): <https://www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html>

2026-10 (accessed): <https://systemd.io/JOURNAL_FILE_FORMAT/>

2022-07: <https://mcsi-library.readthedocs.io/articles/2022/07/linux-systemd-journal-in-digital-forensics/linux-systemd-journal-in-digital-forensics.html>

## Tools

DLEAPP (systemd Journal) - <https://github.com/abrignoni/DLEAPP>

dissect.target (journal) - <https://github.com/fox-it/dissect.target>

journalctl - <https://github.com/systemd/systemd>

peach-forensics (journald) - <https://github.com/kalink0/peach-forensics>

plaso (systemd_journal) - <https://github.com/log2timeline/plaso>

Velociraptor (Linux.Forensics.Journal) - <https://github.com/Velocidex/velociraptor>
