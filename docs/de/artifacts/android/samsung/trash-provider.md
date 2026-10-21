---
title: "Samsung Trash Provider"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [file-existence]
---

# Samsung Trash Provider

## Bedeutung

Der Samsung Trash Provider ist eine Systemkomponente auf Samsung-Geräten, die den gemeinsamen Papierkorb für Samsung-Apps wie Eigene Dateien (My Files) und Galerie verwaltet. Gelöschte Dateien werden zunächst in den Papierkorb verschoben, damit der Benutzer sie innerhalb der Aufbewahrungsfrist wiederherstellen kann. Dafür speichert der Provider zu jeder Datei den ursprünglichen Ablageort und Namen sowie den Zeitpunkt der Löschung.

Aus digitalforensischer Sicht belegt ein Eintrag, dass die Datei zum angegebenen Zeitpunkt aus der genannten App heraus unter dem angegebenen Benutzer in den Papierkorb verschoben wurde, sowie unter welchem Namen und an welchem Ort sie vorher lag.

## Spezifische Kurzinformation

1. Die Daten im Papierkorb liegen für ca. 30 Tage ab Löschung vor
2. Gemeinsamer Papierkorb für Eigene Dateien, Galerie und Sprachrekorder seit One UI 6.0; in älteren Versionen haben die Apps eigene Papierkörbe
3. Der Pfad der Datei im Papierkorb enthält App-Kontext, ursprünglichen Pfad und Dateinamen und ist auch ohne Datenbank auswertbar
4. Beim Wiederherstellen wird der Datenbankeintrag sofort gelöscht; nach Ablauf der Frist kann der Eintrag erhalten bleiben, obwohl die Datei entfernt ist
5. Einträge aus dem Sicheren Ordner sind an der Benutzer-ID 150 erkennbar
6. Zeitstempel: Unix-Zeit in Millisekunden (UTC)
7. Ablageort:

   Datenbank: **`/data/data/com.samsung.android.providers.trash/databases/trash.db`**

   Dateien: **`/data/media/{USER_ID}/Android/.Trash/`**

## Referenzen

2026-02: <https://bebinary4n6.blogspot.com/2026/02/samsung-trash-provider-app-traces-of.html>

2024-01: <https://www.samsung.com/uk/support/apps-services/the-updated-recycle-bin-feature-in-my-files-on-galaxy-devices-with-one-ui-6/>

## Tools

ALEAPP (Parser: Samsung Trash, My Files Trash) - <https://github.com/abrignoni/ALEAPP>