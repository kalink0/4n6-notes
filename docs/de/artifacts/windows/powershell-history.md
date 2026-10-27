---
title: "PowerShell Command History"
status: reviewed
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
reviewers: [dugeonlady]
reviewed: 2026-10-26
topics: [commands-input]
---

# PowerShell Command History

## Bedeutung

Die PowerShell Command History speichert die letzten standardmäßig 4096 ausgeführten Befehle in der PowerShell. Diese Funktion dient dazu, dem Anwender die zuletzt ausgeführten Befehle einfach wieder zur Verfügung zu stellen. Die Ablage der Einträge ist chronologisch, jedoch ohne genaue Zeitangaben.

Aus digitalforensischer Sicht bedeutet die Existenz von Einträgen in der Command History, dass die gelisteten Befehle im Nutzerkontext ausgeführt wurden. Nicht belegt ist dagegen, ob ein Befehl erfolgreich ausgeführt wurde. Ebenso belegt das Fehlen eines Befehls nicht, dass er nicht ausgeführt wurde.

## Spezifische Kurzinformation

1. Ab PowerShell v5, Windows 10, standardmäßig aktiviert
2. Standardmäßig werden die letzten 4096 Befehle chronologisch gespeichert, ohne genaue Zeitstempel; direkt wiederholte identische Befehle werden nur einmal gespeichert
3. Anhand des Erstelldatums und letzten Bearbeitungsdatums kann Rückschluss auf den Zeitraum der History getroffen werden.
4. Wird NICHT geschrieben bei Verwendung der PowerShell ISE - nur Konsolenverwendung
5. Befehle mit password, token, secret u.ä. werden ab PowerShell 7 nicht gespeichert
6. Ablageort:  
   **`%userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\*_history.txt`**

## Referenzen

2026-03: <https://learn.microsoft.com/en-us/powershell/module/psreadline/about/about_psreadline>

2022-11: <https://www.blackhillsinfosec.com/new-powershell-history-defense-evasion-technique/>

2020-08: <https://community.sophos.com/sophos-labs/b/blog/posts/powershell-command-history-forensics>

2018-11: <https://0xdf.gitlab.io/2018/11/08/powershell-history-file.html>

## Tools

DLEAPP (Parser: PowerShell PSReadLine History) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (Artefakt: Windows.System.Powershell.PSReadline) - <https://docs.velociraptor.app/artifact_references/pages/windows.system.powershell.psreadline>

Dissect (Plugin: powershell_history) - <https://dissect.readthedocs.io/en/stable/plugins/powershell_history.html>