---
title: "PCA - Program Compatibility Assistant"
status: reviewed
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
reviewers: [dugeonlady]
reviewed: 2026-10-26
topics: [program-execution]
---

# PCA - Program Compatibility Assistant

## Bedeutung

Der Program Compatibility Assistant ist ein Feature in Windows-Systemen um die Ausführung von älteren Programmen auf den neuesten Windows-Systemen zu gewährleisten.

Aus digitalforensischer Sicht bedeuten Einträge in der PcaAppLaunchDic.txt, dass die Applikationen zum angegebenen Zeitpunkt zuletzt auf dem System ausgeführt wurden. Sie wurden über die grafische Oberfläche gestartet. Es kann eine Aussage über den Ort und den Namen der Anwendung getroffen werden. Die PcaGeneralDb-Dateien protokollieren zusätzlich Ereignisse wie abnormale Programmbeendigungen oder blockierte Treiber; deren Bedeutung hängt vom Eintragstyp ab.

## Spezifische Kurzinformation

1. Verfügbarkeit: Seit Windows 11, 22H2, existent
2. Aufbewahrung: PcaGeneralDb0/1 rotieren bei je 2 MB (2–4 MB Historie)
3. Format und Struktur: Reguläre Text-Dateien, Pipe-delimited format
4. Zeitstempel: UTC; in der PcaAppLaunchDic.txt Zeitpunkt der letzten Ausführung
5. Besonderheiten und Fallstricke: Nur GUI-based Applikationen bzw. Applikationen die aus der GUI heraus gestartet wurden. PcaAppLaunchDic.txt ist ANSI-kodiert: nach einem Pfad mit Nicht-ANSI-Zeichen werden keine neuen Programme mehr erfasst. Pfade in PcaGeneralDb sind normalisiert (kleingeschrieben, ohne Laufwerksbuchstabe, Benutzernamen ersetzt).
6. Ablageort:  
   **`C:\Windows\appcompat\pca\PcaAppLaunchDic.txt`**  
   **`C:\Windows\appcompat\pca\PcaGeneralDb0.txt`**  
   **`C:\Windows\appcompat\pca\PcaGeneralDb1.txt`**

## Referenzen

2024-05: <https://www.sygnia.co/blog/new-windows-11-pca-artifact/>

2023-07: <https://aboutdfir.com/new-windows-11-pro-22h2-evidence-of-execution-artifact/>

2023-01: <https://www.youtube.com/watch?v=rV8aErDj06A>

## Tools

Program Compatibility Parser - <https://github.com/kacos2000/Win10/tree/master/ProgramCompatibility>

PCAParser - <https://github.com/AndrewRathbun/PCAParser>