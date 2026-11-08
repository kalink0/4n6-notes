---
title: "Zone.Identifier (Mark of the Web)"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
topics: [web-activity]
---

# Zone.Identifier (Mark of the Web)

## Bedeutung

Speichert ein Browser, ein E-Mail-Programm oder eine andere Anwendung eine Datei aus dem Internet oder einer anderen nicht vertrauenswürdigen Quelle, hängt sie an die Datei einen Alternate Data Stream namens `Zone.Identifier` an, die sogenannte Mark of the Web (MotW). Er hält fest, aus welcher Sicherheitszone die Datei stammt, und bei aktuellen Browsern auch, von welcher Adresse sie heruntergeladen wurde und von welcher Seite aus. Windows warnt anhand dieser Markierung vor dem Öffnen (SmartScreen, Sicherheitswarnung beim Start), Office öffnet solche Dokumente in der geschützten Ansicht und blockiert Makros. Entpackt der Windows Explorer ein markiertes Archiv, erhalten auch die entpackten Dateien einen `Zone.Identifier`, der auf das Archiv verweist.

Aus digitalforensischer Sicht belegt ein `Zone.Identifier`, dass die Datei von einer Anwendung als aus der angegebenen Zone stammend gespeichert wurde, und nennt ggf. die Download-Adresse und die verweisende Seite. Die Markierung gehört zur Datei und bleibt beim Verschieben und Kopieren innerhalb von NTFS erhalten, auch wenn die Datei umbenannt wird. Fehlt sie bei einer heruntergeladenen Datei, wurde sie entweder nie gesetzt oder später entfernt (siehe Kurzinformation).

## Spezifische Kurzinformation

1. Verfügbarkeit: seit Windows XP SP2; nur auf Dateisystemen mit Alternate Data Streams (NTFS, seit Windows 8.1 auch ReFS)
2. Voraussetzungen: wird von der speichernden Anwendung gesetzt, z. B. von Browsern, von Outlook beim Öffnen oder Speichern eines Anhangs (nicht beim Herausziehen per Drag-and-drop) und von Entpackprogrammen; 7-Zip überträgt die Markierung seit Version 22 nur, wenn das in den Einstellungen aktiviert ist; Downloads per Kommandozeile (z. B. curl, PowerShell, bitsadmin) erhalten keine Markierung
3. Aufbewahrung: besteht, solange die Datei existiert; entfernt wird sie durch „Zulassen“ in den Dateieigenschaften, z. B. mit `Unblock-File` in PowerShell, und seit 2023-02 unter Windows 11 automatisch, wenn ein Programm aus der Shell gestartet wird und die SmartScreen-Prüfung erfolgreich ist
4. Format und Struktur: Text im INI-Format mit dem Abschnitt `[ZoneTransfer]`; `ZoneId` gibt die Zone an (0 = Lokaler Computer, 1 = Lokales Intranet, 2 = Vertrauenswürdige Sites, 3 = Internet, 4 = Eingeschränkte Sites), `HostUrl` die Download-Adresse und `ReferrerUrl` die verweisende Seite bzw. bei entpackten Dateien den Pfad des Archivs; ältere Anwendungen schreiben nur `ZoneId`, neuere teils weitere Schlüssel; der Stream ist meist so klein, dass er resident im MFT-Eintrag der Datei liegt
5. Zeitstempel: Der Stream hat keine eigenen Zeitstempel; maßgeblich sind die Zeitstempel der Datei
6. Besonderheiten und Fallstricke: Chromium-basierte Browser (Chrome, Edge) schreiben im Inkognito-Modus statt der Adressen `HostUrl=about:internet`; dasselbe steht bei Dateien, die erst im Browser erzeugt wurden (z. B. aus `blob:`- oder `data:`-Adressen, HTML Smuggling); beim Kopieren auf FAT32 oder exFAT, über Remote Desktop und mit manchen Sync-Programmen geht die Markierung verloren
7. Ablageort:  
   **`{PFAD}\{DATEI}:Zone.Identifier`**

## Referenzen

2026-09: <https://textslashplain.com/2016/04/04/downloads-and-the-mark-of-the-web/>

2021-10: <https://www.digital-detective.net/forensic-analysis-of-zone-identifier-stream/>

## Tools

MFTECmd - <https://ericzimmerman.github.io/>

DLEAPP (Parser: Zone.Identifier Streams) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (Artefakte: Windows.Analysis.EvidenceOfDownload, Windows.NTFS.ADSHunter) - <https://docs.velociraptor.app/>

Autopsy (Recent Activity) - <https://www.autopsy.com/>

juntei (parse-ntfs mft) - <https://github.com/Yamato-Security/juntei>

ntfstool (mft) - <https://github.com/thewhiteninja/ntfstool>
