---
title: "Journald"
status: complete
completed: 2026-10-22
authors: [kalink0 (Marco Neumann)]
topics: [device-state]
---

# Journald

## Bedeutung

Journald (systemd-journald) ist auf Linux-Systemen mit systemd der zentrale Protokolldienst. Er sammelt Meldungen von Kernel, Systemdiensten, der Startphase und von Programmen und speichert sie zusammen mit Metadaten wie Prozess, Benutzer und systemd-Unit in einem eigenen Binärformat. Gedacht ist das Journal für Administratoren zur Fehlersuche und Überwachung des Systems.

Aus digitalforensischer Sicht belegt ein Eintrag, dass der angegebene Prozess zum angegebenen Zeitpunkt die jeweilige Meldung an das Journal übergeben hat. Was eine Meldung über eine Nutzeraktion aussagt, hängt von der einzelnen Meldung ab. Nicht belegt ist dagegen, dass ein Vorgang nicht stattfand, wenn kein Eintrag vorhanden ist.

## Spezifische Kurzinformation

1. Je nach Distribution und Konfiguration wird nur flüchtig unter /run/log/journal gespeichert; diese Einträge sind nach einem Neustart verloren
2. Aufbewahrung nach Größe, standardmäßig höchstens 10 % des Dateisystems (maximal 4 GB); keine zeitbasierte Löschung, Dateien werden spätestens nach einem Monat rotiert
3. system.journal enthält die Systemmeldungen, user-{UID}.journal die Meldungen je Benutzer; rotierte Dateien tragen ein @ im Namen, Dateien mit Endung .journal~ wurden nach unsauberem Beenden oder Beschädigung umbenannt
4. Zeitstempel: Echtzeit in Mikrosekunden seit 1970-01-01 (UTC), zusätzlich monotone Zeit, die nur zusammen mit der Boot-ID eindeutig ist
5. Felder mit führendem Unterstrich (z.B. _PID, _UID, _SYSTEMD_UNIT) setzt journald selbst; der protokollierende Prozess kann sie nicht vorgeben, den Meldungstext dagegen schon
6. Manipulationsschutz (Forward Secure Sealing) nur, wenn dafür ein Schlüssel eingerichtet wurde
7. Binärformat, teils komprimiert; die Dateien sind nicht direkt lesbar und müssen mit journalctl oder einem Parser dekodiert werden
8. Ablageort:  
   **`/var/log/journal/{MACHINE_ID}/`**  
   **`/run/log/journal/{MACHINE_ID}/`**

## Referenzen

2026-10: <https://www.freedesktop.org/software/systemd/man/latest/journald.conf.html> (abgerufen)

2026-10: <https://www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html> (abgerufen)

2026-10: <https://systemd.io/JOURNAL_FILE_FORMAT/> (abgerufen)

2022-07: <https://mcsi-library.readthedocs.io/articles/2022/07/linux-systemd-journal-in-digital-forensics/linux-systemd-journal-in-digital-forensics.html>

## Tools

DLEAPP (systemd Journal) - <https://github.com/abrignoni/DLEAPP>

dissect.target (journal) - <https://github.com/fox-it/dissect.target>

journalctl - <https://github.com/systemd/systemd>

peach-forensics (journald) - <https://github.com/kalink0/peach-forensics>

plaso (systemd_journal) - <https://github.com/log2timeline/plaso>

Velociraptor (Linux.Forensics.Journal) - <https://github.com/Velocidex/velociraptor>