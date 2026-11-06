---
title: "Notepad TabState"
status: complete
completed: 2026-11-06
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [commands-input, user-content]
---

# Notepad TabState

## Meaning

Windows 11 Notepad supports tabs and stores the state of each open tab in a file of its own. This lets it restore all tabs at the next start, including text that was never saved to a file and changes to open files that have not been saved yet. While Notepad is running, it records unsaved changes as individual edit steps (position, deleted and inserted characters) and only merges them into the text when it closes or the file is saved. Further files hold, per window, the tabs, their order and the active tab, as well as Notepad's settings.

From a digital forensics perspective, a tab file shows that the text it contains was typed or pasted into Notepad, or that the named file was open in Notepad. Text in a tab without a file was never saved and may exist only here. The individual edit steps show the sequence in which text was typed and deleted.

## Key facts

1. Windows 11 with Notepad as an app from the Microsoft Store; session saving since Notepad version 11.2307 (Windows Insider 2023-08)
2. Enabled by default; can be disabled in Notepad's settings by opening a new window instead of the previous session at start; then no tab and window files are created
3. The tab file exists as long as the tab is open, also across restarts of Notepad; it is deleted when the tab is closed; IDs of closed tabs can remain in the unused part of the window files
4. File format: a proprietary binary format with the signature `NP`, the text is stored in UTF-16LE; each tab has a file `{GUID}.bin` and, where present, the state files `{GUID}.0.bin` and `{GUID}.1.bin`
5. The settings (`settings.dat`) are a separate application registry hive
6. Tabs with a file (path of the file on disk stored) are distinguished from tabs without a file (text never saved); whether tabs with a file also hold the content, size and SHA-256 hash of the saved file depends on the Notepad version
7. Timestamp for tabs with a file as FILETIME: set at the first unsaved change, not updated by later changes, reset to 0 on save
8. Of each `*.0.bin` / `*.1.bin` pair, the file with the higher sequence number is the current one; Notepad writes to both alternately
9. `settings.dat` holds, among other things, the list of recently opened files and the last used find and replace terms
10. Location:  
   Tabs: **`%LOCALAPPDATA%\Packages\Microsoft.WindowsNotepad_8wekyb3d8bbwe\LocalState\TabState`**  
   Windows: **`%LOCALAPPDATA%\Packages\Microsoft.WindowsNotepad_8wekyb3d8bbwe\LocalState\WindowState`**  
   Settings: **`%LOCALAPPDATA%\Packages\Microsoft.WindowsNotepad_8wekyb3d8bbwe\Settings\settings.dat`**

## References

2025-12: <https://doi.org/10.21428/b0ac9c28.a8c471f1>

2024-08: <https://u0041.co/posts/articals/exploring-windows-artifacts-notepad-files/>

2023-08: <https://blogs.windows.com/windows-insider/2023/08/31/new-updates-for-snipping-tool-and-notepad-for-windows-insiders/>

## Tools

Notepad-State-Library (WindowsNotepadParser) - <https://github.com/ogmini/Notepad-State-Library>

notepad_parser - <https://github.com/AbdulRhmanAlfaifi/notepad_parser>

DLEAPP (windowsNotepad) - <https://github.com/abrignoni/DLEAPP>
