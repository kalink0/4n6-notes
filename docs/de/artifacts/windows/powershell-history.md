---
title: "PowerShell Command History"
status: reviewed
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
reviewers: [dugeonlady]
reviewed: 2026-11-06
topics: [commands-input]
---

# PowerShell Command History

## Bedeutung

Die PowerShell Command History speichert die letzten standardmäßig 4096 ausgeführten Befehle in der PowerShell. Diese Funktion dient dazu, dem Anwender die zuletzt ausgeführten Befehle einfach wieder zur Verfügung zu stellen. Die Ablage der Einträge ist chronologisch, jedoch ohne genaue Zeitangaben.

Aus digitalforensischer Sicht bedeutet die Existenz von Einträgen in der Command History, dass die gelisteten Befehle im Nutzerkontext ausgeführt wurden. Nicht belegt ist dagegen, ob ein Befehl erfolgreich ausgeführt wurde. Ebenso belegt das Fehlen eines Befehls nicht, dass er nicht ausgeführt wurde.

## Spezifische Kurzinformation

1. Voraussetzungen: Ab PowerShell v5, Windows 10, standardmäßig aktiviert
2. Aufbewahrung: Standardmäßig werden die letzten 4096 Befehle chronologisch gespeichert; direkt wiederholte identische Befehle werden nur einmal gespeichert; Anhand des Erstelldatums und letzten Bearbeitungsdatums kann Rückschluss auf den Zeitraum der History getroffen werden.
3. Zeitstempel: Es werden keine genauen Zeitstempel gespeichert.
4. Besonderheiten und Fallstricke: Wird NICHT geschrieben bei Verwendung der PowerShell ISE - nur Konsolenverwendung; Befehle mit password, token, secret u.ä. werden ab PowerShell 7 nicht gespeichert
6. Ablageort:  
   **`%userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\*_history.txt`**

## Referenzen

2026-03: <https://learn.microsoft.com/en-us/powershell/module/psreadline/about/about_psreadline>

2022-11: <https://www.blackhillsinfosec.com/new-powershell-history-defense-evasion-technique/>

2020-08: <https://community.sophos.com/sophos-labs/b/blog/posts/powershell-command-history-forensics>

2018-11: <https://0xdf.gitlab.io/2018/11/08/powershell-history-file.html>

## Tools

DLEAPP (Parser: PowerShell PSReadLine History) - <https://github.com/abrignoni/DLEAPP>

Dissect (Plugin: powershell_history) - <https://dissect.readthedocs.io/en/stable/plugins/powershell_history.html>

Velociraptor (Artefakt: Windows.System.Powershell.PSReadline) - <https://docs.velociraptor.app/>

TRACE - <https://github.com/Gadzhovski/TRACE-Forensic-Toolkit>
