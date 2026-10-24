---
title: "Shellbags"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [file-access]
---

# Shellbags

## Bedeutung

Shellbags werden in modernen Windows Systemen (ab Windows XP) verwendet um die Ordnerstruktur für vom Nutzerkonto besuchte Ordner zu speichern. Ziel ist es, die Ordnerstruktur so anzuzeigen, wie das Nutzerkonto es präferiert. Es werden Daten wie Ordnernamen und Datum des Aufrufs gespeichert.

Aus digitalforensischer Sicht bedeuten abgelegte Shellbags, dass der Nutzeraccount aktiv zu dem angegeben Zeitpunkt über den Windows Explorer (auch Öffnen-/Speichern-Dialoge in Apps) in der Ordnerstruktur navigiert hat. Es kann nich gesagt werden, was in Dateien gespeichert war/ist oder ob diese vom Nuzerkonto geöffnet wurden. Es kann nicht gesagt werden, auf welchem Weg zu einem Ordner navigiert wurde. Es kann gesagt werden, dass zum Zeitpunkt der Navigation die Ordner mit den in den Shellbags vorliegenden Daten namentlich übereinstimmten.

## Spezifische Kurzinformation

1. Nur Ordner, welche mit dem Windows Explorer (auch Öffnen-/Speichern-Dialoge in Apps) geöffnet wurden, landen in den Shellbags
2. Shellbags bleiben erhalten, auch wenn der eigentliche Dateipfad nicht mehr exisitiert (Löschung, Abziehen externer Datenspeicher)
3. Ab Windows 11 22H2 werden auch Archive (ZIP, 7-ZIP, RAR, TAR, GZIP) unterstützt
4. In Windows Store Apps werden ggf. zusätzlich Shellbags erzeugt. Diese liegen in eigenen User.dat und UserClasses.dat in der jeweiligen Windows App Verzeichnis-Struktur
5. Ablageorte (Registry):  
   Bis Windows XP, NTUSER.dat: **`HKCU\Software\Microsoft\Windows\ShellNoRoam\BagMRU`**  
   Bis Windows XP, NTUSER.dat: **`HKCU\Software\Microsoft\Windows\ShellNoRoam\Bags`**  
   Bis Windows XP, NTUSER.dat: **`HKCU\Software\Microsoft\Windows\Shell\BagMRU`**  
   Bis Windows XP, NTUSER.dat: **`HKCU\Software\Microsoft\Windows\Shell\Bags`**  
   Ab Windows Vista, NTUSER.dat: **`HKCU\Software\Microsoft\Windows\Shell\BagMRU`**  
   Ab Windows Vista, NTUSER.dat: **`HKCU\Software\Microsoft\Windows\Shell\Bags`**  
   Ab Windows Vista, UsrClass.dat: **`HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\BagMRU`**  
   Ab Windows Vista, UsrClass.dat: **`HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\Bags`**  
   Store-Apps: **`%USERPROFILE%\AppData\Local\Packages\{PACKAGE}\SystemAppData\Helium\User.dat`**  
   Store-Apps: **`%USERPROFILE%\AppData\Local\Packages\{PACKAGE}\SystemAppData\Helium\UserClasses.dat`**

## Referenzen

2026-03: <https://www.cybertriage.com/blog/shellbags-forensic-analysis-2025/>

2025-02: <https://www.ilyakobzar.com/p/revisiting-shellbags-in-windows-11>

2014-08: <https://www.magnetforensics.com/blog/forensic-analysis-of-windows-shellbags/>

2014-04: <https://www.sans.org/white-papers/34545>

## Tools

SBECmd - <https://ericzimmerman.github.io/>

Shellbag Explorer - <https://ericzimmerman.github.io/>

ShellBags View - <https://www.nirsoft.net/utils/shell_bags_view.html>

RegRipper (Plugin: shellbags) - <https://github.com/keydet89/RegRipper4.0>

DLEAPP (Parser: ShellBags) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (Artefakt: Windows.Forensics.Shellbags) - <https://docs.velociraptor.app/artifact_references/pages/windows.forensics.shellbags/>

Dissect (Plugin: shellbags) - <https://docs.dissect.tools/en/stable/plugins/shellbags.html>