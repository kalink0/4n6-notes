---
title: "PowerShell Command History"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [commands-input]
---

# PowerShell Command History

## Meaning

The PowerShell Command History stores the last 4096 (by default) commands executed in PowerShell. This feature serves to easily make the last executed commands available to the user again. The entries are stored chronologically, but without exact times.

From a digital forensics perspective, the existence of entries in the Command History means that the listed commands were executed in the user context. It does not show, however, that a command was executed successfully. Likewise, the absence of a command does not show that it was not executed.

## Key facts

1. From PowerShell v5, Windows 10, enabled by default
2. By default, the last 4096 commands are stored chronologically, without exact timestamps; identical commands repeated directly are only stored once
3. The creation date and last modification date allow conclusions about the time period of the history.
4. NOT written when using the PowerShell ISE - console use only
5. Commands containing password, token, secret and similar are not stored from PowerShell 7
6. Location:  
   **`%userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\*_history.txt`**

## References

2026-03: <https://learn.microsoft.com/en-us/powershell/module/psreadline/about/about_psreadline>

2022-11: <https://www.blackhillsinfosec.com/new-powershell-history-defense-evasion-technique/>

2020-08: <https://community.sophos.com/sophos-labs/b/blog/posts/powershell-command-history-forensics>

2018-11: <https://0xdf.gitlab.io/2018/11/08/powershell-history-file.html>

## Tools

DLEAPP (parser: PowerShell PSReadLine History) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (artifact: Windows.System.Powershell.PSReadline) - <https://docs.velociraptor.app/artifact_references/pages/windows.system.powershell.psreadline>

Dissect (plugin: powershell_history) - <https://dissect.readthedocs.io/en/stable/plugins/powershell_history.html>
