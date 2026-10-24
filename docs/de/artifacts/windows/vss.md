---
title: "VSS - Volume Shadow Copy Service"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [file-existence]
---

# VSS - Volume Shadow Copy Service

## Bedeutung

Das Betriebssystem Microsoft Windows verfügt seit der Version Windows Vista für das Dateisystem NTFS über den Mechanismus des Volume Shadow Copy Services (VSS).
Diese Funktion ermöglicht es Nutzern ehemals existierende Dateien und ehemalige Versionen von Dateien wiederherzustellen.

Aus digitalforensischer Sicht bedeutet dies, dass ehemals existierende Dateien und/oder ehemalige Versionen von Dateien in diesen Volume Shadow Copies vorliegen können.
Wenn eine Datei sich in einer Volume Shadow Copy befindet, kann aus digitalforensischer Sicht gesagt werden, von wann dieser "Snapshot" der Datei stammt. Damit kann ausgedrückt werden wann diese Datei auf dem System in dieser Version vorgelegen hat.

## Spezifische Kurzinformation

1. Unter Windows 10/11 ist der Systemschutz standardmäßig nicht aktiviert
2. Erstellung u.a. bei Softwareinstallation, Windows-Update oder manuellem Wiederherstellungspunkt
3. Ist der reservierte Speicherplatz voll, wird die älteste Schattenkopie gelöscht
4. Ablageort:  
   **`{DRIVE}:\System Volume Information\{GUID}{3808876b-c176-4e48-b7ae-04046e6cc752}`**

## Referenzen

2026-09: <https://www.it-connect.tech/forensic-windows-part-14-exploring-shadow-copies-vss/>

2026-07: <https://digitalinvestigator.blogspot.com/2026/07/volume-shadow-copies-in-windows.html>

2018-03: <https://www.iiis.org/CDs2018/CD2018Spring/papers/ZA288KS.pdf>

2017-10: <https://andreafortuna.org/2017/10/02/volume-shadow-copies-in-forensic-analysis/>

2011-01: <https://windowsir.blogspot.com/2011/01/accessing-volume-shadow-copies.html>

## Tools

libvshadow - <https://github.com/libyal/libvshadow>

VSCMount - <https://github.com/EricZimmerman/VSCMount>

Shadow Copy View - <https://www.nirsoft.net/utils/shadow_copy_view.html>

Arsenal Image Mounter - <https://arsenalrecon.com/downloads/>

ShadowExplorer - <https://www.shadowexplorer.com/downloads.html>

vss_carver - <https://github.com/mnrkbys/vss_carver>