---
title: "Notepad TabState"
status: complete
completed: 2026-11-06
authors: [kalink0 (Marco Neumann)]
topics: [commands-input, user-content]
---

# Notepad TabState

## Bedeutung

Der Editor (Notepad) von Windows 11 unterstützt Tabs und speichert den Zustand jedes geöffneten Tabs in einer eigenen Datei. Beim nächsten Start stellt er so alle Tabs wieder her, auch mit Text, der nie in eine Datei gespeichert wurde, und mit noch nicht gespeicherten Änderungen an geöffneten Dateien. Ungespeicherte Änderungen hält der Editor, solange er läuft, als einzelne Änderungsschritte fest (Position, gelöschte und eingefügte Zeichen) und übernimmt sie erst beim Beenden oder Speichern in den Text. Weitere Dateien halten pro Fenster die Tabs, ihre Reihenfolge und den aktiven Tab sowie die Einstellungen des Editors fest.

Aus digitalforensischer Sicht belegt eine Tab-Datei, dass der darin enthaltene Text im Editor eingegeben oder eingefügt wurde bzw. dass die genannte Datei im Editor geöffnet war. Text in einem Tab ohne Datei wurde nie gespeichert und existiert unter Umständen nur hier. Aus den einzelnen Änderungsschritten lässt sich nachvollziehen, in welcher Abfolge Text eingegeben und gelöscht wurde.

## Spezifische Kurzinformation

1. Windows 11 mit dem Editor als App aus dem Microsoft Store; Speicherung der Sitzung seit Editor-Version 11.2307 (Windows Insider 2023-08)
2. Standardmäßig aktiv; abschaltbar in den Editor-Einstellungen, indem beim Start ein neues Fenster statt der vorherigen Sitzung geöffnet wird; dann entstehen keine Tab- und Fensterdateien
3. Die Tab-Datei besteht, solange der Tab offen ist, auch über Neustarts des Editors hinweg; beim Schließen des Tabs wird sie gelöscht; in den Fensterdateien können Kennungen geschlossener Tabs im ungenutzten Bereich der Datei erhalten bleiben
4. Dateiformat: eigenes Binärformat mit der Signatur `NP`, der Text ist in UTF-16LE gespeichert; pro Tab gibt es eine Datei `{GUID}.bin` und ggf. die Zustandsdateien `{GUID}.0.bin` und `{GUID}.1.bin`
5. Die Einstellungen (`settings.dat`) sind ein eigener Registry-Hive der App
6. Unterschieden werden Tabs mit Datei (Pfad der Datei auf dem Datenträger gespeichert) und Tabs ohne Datei (Text nie gespeichert); ob bei Tabs mit Datei zusätzlich Inhalt, Größe und SHA-256-Hash der gespeicherten Datei enthalten sind, hängt von der Editor-Version ab
7. Zeitstempel bei Tabs mit Datei als FILETIME: gesetzt bei der ersten ungespeicherten Änderung, durch spätere Änderungen nicht aktualisiert, beim Speichern auf 0 zurückgesetzt
8. Von den Paaren `*.0.bin` / `*.1.bin` ist jeweils die Datei mit der höheren Sequenznummer die aktuelle; der Editor schreibt abwechselnd in beide
9. `settings.dat` enthält u.a. die Liste zuletzt geöffneter Dateien und die zuletzt verwendeten Such- und Ersetzungsbegriffe
10. Ablageort:  
   Tabs: **`%LOCALAPPDATA%\Packages\Microsoft.WindowsNotepad_8wekyb3d8bbwe\LocalState\TabState`**  
   Fenster: **`%LOCALAPPDATA%\Packages\Microsoft.WindowsNotepad_8wekyb3d8bbwe\LocalState\WindowState`**  
   Einstellungen: **`%LOCALAPPDATA%\Packages\Microsoft.WindowsNotepad_8wekyb3d8bbwe\Settings\settings.dat`**

## Referenzen

2025-12: <https://doi.org/10.21428/b0ac9c28.a8c471f1>

2024-08: <https://u0041.co/posts/articals/exploring-windows-artifacts-notepad-files/>

2023-08: <https://blogs.windows.com/windows-insider/2023/08/31/new-updates-for-snipping-tool-and-notepad-for-windows-insiders/>

## Tools

Notepad-State-Library (WindowsNotepadParser) - <https://github.com/ogmini/Notepad-State-Library>

notepad_parser - <https://github.com/AbdulRhmanAlfaifi/notepad_parser>

DLEAPP (windowsNotepad) - <https://github.com/abrignoni/DLEAPP>
