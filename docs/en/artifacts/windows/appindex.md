---
title: "Windows AppIndex"
status: reviewed
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
reviewers: [dugeonlady]
reviewed: 2026-10-30
topics: [program-execution, installed-software]
---

# Windows AppIndex

## Meaning

AppsIndex.db is an SQLite database of the "Windows Feature Experience Pack" on Windows 11. It indexes installed applications or applications present in the Start menu for the Start menu search. Only applications that are present in the Start menu either through installation (shortcut in the Start menu folder) or manually added through "Pin to Start" are recorded – not all executable files present on the system.

From a digital forensics perspective, an entry with a launch count greater than 0 means that a specific application was executed under this user account. No statement about the exact time of the (last) execution can be made on the basis of this artifact, as no timestamps are stored.

## Key facts

1. Prerequisites: can be disabled via "Improve Start and search results" - RegKey: HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced - Start_TrackProgs = 0
2. Retention: limited history - the record is removed soon after unpinning/uninstalling - time of deletion not deterministic
3. Format and structure: relevant tables: tiles and tiles_content – contain application path, display name and launch count (launchCount)
4. Special features and pitfalls: only apps linked in the Start menu are tracked per user
5. Location:  
   **`%LOCALAPPDATA%\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\LocalState\Search\AppsIndex.db`**

## References

2025-09: <https://detect.fyi/introducing-appsindex-db-new-windows-11-artifact-for-tracking-start-menu-application-execution-b294c8e764fa>

## Tools

*No content yet.*
