---
title: "MRU - WordWheelQuery"
status: complete
completed: 2026-11-06
authors: [kalink0 (Marco Neumann)]
topics: [commands-input]
---

# MRU - WordWheelQuery

## Bedeutung

Der Datei-Explorer speichert pro Benutzerkonto die Begriffe, nach denen im Suchfeld des Explorers gesucht wurde. Damit schlägt er dem Benutzer bei der nächsten Eingabe frühere Suchbegriffe vor. Die Begriffe stehen als MRU-Liste (Most Recently Used) in der Registry, sortiert nach der jeweils letzten Suche.

Aus digitalforensischer Sicht belegt ein Eintrag, dass im Kontext des Benutzerkontos im Suchfeld des Datei-Explorers nach dem Begriff gesucht wurde. Aus der Reihenfolge ergibt sich, in welcher Abfolge die Begriffe zuletzt gesucht wurden. Nicht gespeichert sind der Ordner oder das Laufwerk, in dem gesucht wurde, und die gefundenen Ergebnisse.

## Spezifische Kurzinformation

1. Seit Windows 7 bis Windows 11; unter Windows XP stand die Suchhistorie im Schlüssel `ACMru`
2. Erfasst nur Suchen im Suchfeld des Datei-Explorers, nicht die Suche im Startmenü oder in der Windows-Suche
3. Ein Begriff wird erst gespeichert, wenn die Suche ausgeführt wird; ein erneut gesuchter Begriff wird nicht doppelt angelegt, sondern rückt in der Reihenfolge nach vorn
4. Werte mit Zahlen als Namen (`0`, `1`, `2` …), Typ REG_BINARY, Begriff als UTF-16LE-Zeichenkette; der Wertname sagt nichts über das Alter aus, da Nummern wiederverwendet werden
5. Reihenfolge über `MRUListEx`: Liste von 4-Byte-Werten (Little Endian) mit den Wertnamen, neuester zuerst, abgeschlossen mit `0xFFFFFFFF`
6. Die letzte Schreibzeit des Schlüssels gehört nur zum neuesten Begriff; ältere Begriffe haben nur ihre Position in der Reihenfolge
7. Öffnet der Benutzer ein Suchergebnis, entsteht im Ordner **`%APPDATA%\Microsoft\Windows\Recent`** eine LNK-Datei mit dem Suchbegriff als Namen (z.B. `passw.lnk`), die auch den Suchort enthält; ihre Zeitstempel geben dann den Zeitpunkt der Suche an
8. Ablageort:  
   **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery`**

## Referenzen

2026-05: <https://forenza.io/registry-ntuser-word-wheel/>

2020-02: <https://cloud.google.com/blog/topics/threat-intelligence/the-missing-lnk-correlating-user-search-lnk-files>

## Tools

DLEAPP (windowsUserMru) - <https://github.com/abrignoni/DLEAPP>

Registry Explorer (WordWheelQuery Plugin) - <https://ericzimmerman.github.io/>

RegRipper (wordwheelquery) - <https://github.com/keydet89/RegRipper4.0>
