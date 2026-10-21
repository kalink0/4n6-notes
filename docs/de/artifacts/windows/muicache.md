---
title: "MUI - Multilingual User Interface - Cache"
status: complete
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
topics: [program-execution]
---

# MUI - Multilingual User Interface - Cache

## Bedeutung

Der MUI (Multilingual User Interface) Cache dient in Windows Betriebssystemen dazu den Mehrsprachensupport zu gewährleisten. Ziel ist es, dass versucht wird, dem Nutzer eine möglichst vollständige Übersetzung aller ausgeführten Programme im Windowssystem anbieten zu können. Hierfür werden Daten wie Dateipfad und -name *gespeichert/verwendet/...*

Aus digitalforensischer Sicht bedeuten Einträge in dem MUI Cache, dass das Programm auf dem System unter dem angegebenen Pfad und Namen in der Sitzung des Benutzerkontos ausgeführt wurde und dort eine Oberfläche angezeigt hat. Das Konto, unter dem der Prozess lief, kann davon abweichen (z.B. bei "Ausführen als").

## Spezifische Kurzinformation

1. Format und Struktur: Enhält den Pfad, den Namen und ggf. Versionsinfo aus der PE-File
2. Zeitstempel: Es liegen keine Zeitstempel vor
3. Besonderheiten und Fallstricke: Nur Programme mit GUI-Komponente werden protokolliert. Nutzerkontenbasiert
4. Ablageort:  
   Bis Windows XP: **NTUSER.dat - HKCU\\Software\\Microsoft\\Windows\\ShellNoRoam\\MUICache**  
   Ab Windows Vista: **USRCLASS.dat - Local Settings\\Software\\Microsoft\\Windows\\Shell\\MuiCache**  
   Ab Windows Vista (Live-System): **HKCU\\Software\\Classes\\Local Settings\\Software\\Microsoft\\Windows\\Shell\\MuiCache**

## Referenzen

2026-03: <https://www.cybertriage.com/blog/muicache-2026-guide/>

2022-04: <https://www.magnetforensics.com/blog/forensic-analysis-of-muicache-files-in-windows/>

## Tools

RegRipper (muicache) - <https://github.com/keydet89/RegRipper4.0>

Registry Explorer - <https://ericzimmerman.github.io/>

MUICacheView - <https://www.nirsoft.net/utils/muicache_view.html>