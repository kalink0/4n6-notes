---
title: "BAM - Background Activity Moderator"
status: reviewed
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
reviewers: [dugeonlady]
reviewed: 2026-10-26
topics: [program-execution]
---

# BAM - Background Activity Moderator

## Bedeutung

Der BAM ist ein Windowsdienst, welcher Hintergrundprozesse überwacht und kontrolliert. Ziel ist die Optimierung der Performance und des Energieverbrauchs. Die Daten werden nach 7 Tagen vom System gelöscht. Der BAM wird pro Nutzer unter der zugehörigen SID gespeichert. Es wird der Pfad der Executable und der Zeitpunkt der letzten Ausführung gespeichert.

Aus digitalforensischer Sicht bedeuten Einträge des BAM, dass eine Applikation im Kontext des Nutzerkontos zu dem angegebenen Zeitpunkt ausgeführt wurde.

## Spezifische Kurzinformation

1. Verfügbarkeit: Eingeführt mit Windows 10 - Update 1709
2. Aufbewahrung: Die Daten liegen ca. 7 Tage vor.
3. Besonderheiten und Fallstricke: Applikationen, welche im Terminal gestartet wurden, werden NICHT geloggt. Applikationen, welche von externen Medien (z.B. USB-Sticks, Netzlaufwerke) gestartet wurden, werden NICHT geloggt.
4. Ablageort (Registry):  
   ab Windows 10 1809: **`HKLM\SYSTEM\{CURRENT_CONTROL_SET}\Services\bam\State\UserSettings\{USER_SID}`**  
   Windows 10 1709/1803: **`HKLM\SYSTEM\{CURRENT_CONTROL_SET}\Services\bam\UserSettings\{USER_SID}`**

## Referenzen

2026-07: <https://www.it-connect.tech/forensic-windows-part-5-analyzing-bam-and-dam/>

2024-08: <https://github.com/Psmths/windows-forensic-artifacts/blob/main/execution/bam-dam.md>

## Tools

RegRipper (bam) - <https://github.com/keydet89/RegRipper4.0>

Registry Explorer - <https://ericzimmerman.github.io/>

Velociraptor (Windows.Forensics.Bam) - <https://docs.velociraptor.app/>