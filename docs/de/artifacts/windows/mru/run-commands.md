---
title: "MRU - RunMRU"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [commands-input]
---

# MRU - RunMRU

## Bedeutung

Das Betriebssystem Windows legt mehrere sogenannte MRU (Most Recently Used) Listen ab. Diese speichern pro Benutzerkonto im Allgemeinen zuletzt aufgerufene oder gespeicherte Dateien, zuletzt ausgeführte Befehle, zuletzt aufgerufene Ordner.

Der Zweck der MRU Listen ist es, den Benutzern ein angenehmeres Bediengefühl zu liefern, indem zum Beispiel dem Nutzer seine zuletzt geöffneten Dateien angeboten werden.

Einträge in der Run Commands MRU bedeuten aus digitalforensischer Sicht, dass im Kontext des Benutzerkontos die aufgeführten Befehle in der Reihenfolge der jeweils letzten Ausführung im "Ausführen"-Dialog des Betriebssystems ausgeführt wurden.

## Spezifische Kurzinformation

1. Wird nicht geschrieben, wenn in den Datenschutzeinstellungen das Nachverfolgen von App-Starts deaktiviert ist
2. Werte a bis z, maximal 26 Einträge; ein erneut ausgeführter Befehl rückt nur in der Reihenfolge nach oben
3. Reihenfolge über `MRUList`; die letzte Schreibzeit des Schlüssels gehört nur zum neuesten Eintrag
4. Befehle, die nicht ausgeführt werden können (z.B. nicht existierende Datei), werden nicht eingetragen
5. Ablageorte:  
   **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU`**

## Referenzen

2026-03: <https://www.cybertriage.com/blog/how-to-investigate-runmru-2025/>

2022-09: <https://www.magnetforensics.com/blog/what-is-mru-most-recently-used/>

## Tools

DLEAPP (windowsUserMru) - <https://github.com/abrignoni/DLEAPP>

Registry Explorer (RunMRU Bookmark) - <https://ericzimmerman.github.io/>

RegRipper (runmru) - <https://github.com/keydet89/RegRipper4.0>