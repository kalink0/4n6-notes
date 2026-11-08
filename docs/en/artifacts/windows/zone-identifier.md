---
title: "Zone.Identifier (Mark of the Web)"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [web-activity]
---

# Zone.Identifier (Mark of the Web)

## Meaning

When a browser, an e-mail client or another application saves a file from the internet or another untrusted source, it attaches an alternate data stream named `Zone.Identifier` to the file, the so-called Mark of the Web (MotW). It records the security zone the file came from and, with current browsers, also the address it was downloaded from and the page that led to it. Windows uses this mark to warn before opening (SmartScreen, security warning at launch); Office opens such documents in Protected View and blocks macros. When Windows Explorer extracts a marked archive, the extracted files also receive a `Zone.Identifier` that points to the archive.

From a digital forensics perspective, a `Zone.Identifier` shows that the file was saved by an application as originating from the given zone and, where present, names the download address and the referring page. The mark belongs to the file and is kept when the file is moved or copied within NTFS, even if it is renamed. If it is missing on a downloaded file, it was either never set or removed later (see key facts).

## Key facts

1. Availability: since Windows XP SP2; only on file systems with alternate data streams (NTFS, since Windows 8.1 also ReFS)
2. Prerequisites: set by the saving application, e.g. by browsers, by Outlook when opening or saving an attachment (not when dragging it out) and by archive tools; 7-Zip propagates the mark since version 22 only if enabled in its settings; downloads via the command line (e.g. curl, PowerShell, bitsadmin) receive no mark
3. Retention: exists as long as the file exists; it is removed by "Unblock" in the file properties, e.g. with `Unblock-File` in PowerShell, and since 2023-02 on Windows 11 automatically when a program is launched from the shell and the SmartScreen check succeeds
4. Format and structure: text in INI format with the section `[ZoneTransfer]`; `ZoneId` gives the zone (0 = Local computer, 1 = Local intranet, 2 = Trusted sites, 3 = Internet, 4 = Restricted sites), `HostUrl` the download address and `ReferrerUrl` the referring page or, for extracted files, the path of the archive; older applications only write `ZoneId`, newer ones partly further keys; the stream is usually small enough to be resident in the file's MFT entry
5. Timestamps: the stream has no timestamps of its own; the file's timestamps apply
6. Particularities and pitfalls: Chromium-based browsers (Chrome, Edge) write `HostUrl=about:internet` instead of the addresses in incognito mode; the same appears for files created inside the browser (e.g. from `blob:` or `data:` addresses, HTML smuggling); the mark is lost when copying to FAT32 or exFAT, via Remote Desktop and with some sync programs
7. Location:  
   **`{PATH}\{FILE}:Zone.Identifier`**

## References

2026-09: <https://textslashplain.com/2016/04/04/downloads-and-the-mark-of-the-web/>

2021-10: <https://www.digital-detective.net/forensic-analysis-of-zone-identifier-stream/>

## Tools

### Core tools

DLEAPP (Parser: Zone.Identifier Streams) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (Artifacts: Windows.Analysis.EvidenceOfDownload, Windows.NTFS.ADSHunter) - <https://docs.velociraptor.app/>

MFTECmd - <https://ericzimmerman.github.io/>

### Other tools

Autopsy (Recent Activity) - <https://www.autopsy.com/>

juntei (parse-ntfs mft) - <https://github.com/Yamato-Security/juntei>

ntfstool (mft) - <https://github.com/thewhiteninja/ntfstool>
