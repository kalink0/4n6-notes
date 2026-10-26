---
title: "Recycle Bin"
status: reviewed
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
reviewers: [dugeonlady]
reviewed: 2026-10-26
topics: [file-existence]
---

# Recycle Bin

## Bedeutung

Der Recycle Bin, im deutschen "Papierkorb", enthält vom Benutzer gelöschte Dateien. Diese Dateien können vom Benutzer wiederhergestellt werden. Der Recycle Bin enthält Metadaten zu den Dateien wie z.B. löschender Benutzer, vorheriger Dateipfad, Zeitstempel der Datei und Löschzeitpunkt der Datei. Für den Nutzer wird die SID des Benutzerkontos gespeichert, welches verwendet wurde, um die Datei zu löschen.

Aus digitalforensischer Sicht kann anhand der Dateien im Recycle Bin gesagt werden, dass der Nutzer-Account mit der hinterlegten SID die Datei aktiv zu dem Löschzeitpunkt gelöscht hat.

## Spezifische Kurzinformation

1. Ab Windows Vista; ein Recycle Bin pro Laufwerk
2. Je gelöschter Datei eine $I-Datei (Metadaten) und eine $R-Datei (Inhalt)
3. Löschzeitpunkt in UTC
4. Für das Dateisystem FAT32 wird kein Bezug zum Nutzerkonto gespeichert
5. Beim Wiederherstellen wird nur die $R-Datei entfernt, die $I-Datei bleibt erhalten
6. Löschen über Shift+Entf, PowerShell oder CMD hinterlässt keine Spuren im Recycle Bin
7. Ablageort:  
   NTFS: **`{DRIVE}:\$Recycle.Bin\{USER_SID}`**  
   FAT32: **`{DRIVE}:\$Recycle.Bin`**

## Referenzen

2026-09: <https://www.it-connect.tech/windows-forensics-part-9-what-the-recycle-bin-can-reveal/>

2026-09: <https://www.magnetforensics.com/blog/artifact-profile-recycle-bin/>

2025-01: <https://bebinary4n6.blogspot.com/2025/01/windows-recycle-bin-known-and-unknown.html>

## Tools

Rifiuti2 - <https://abelcheung.github.io/rifiuti2/>

RBCmd - <https://ericzimmerman.github.io/>

DLEAPP (Parser: Recycle Bin) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (Artefakt: Windows.Forensics.RecycleBin) - <https://docs.velociraptor.app/artifact_references/pages/windows.forensics.recyclebin/>

Dissect (Plugin: recyclebin) - <https://docs.dissect.tools/en/stable/plugins/recyclebin.html>