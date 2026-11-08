---
title: "OAlerts"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
topics: [file-access]
---

# OAlerts

## Bedeutung

Microsoft Office protokolliert die Dialoge, die eine Office-Anwendung dem Nutzer anzeigt (Office Alerts), in einem eigenen Ereignisprotokoll. Ein Eintrag enthält die Anwendung (z. B. Word, Excel, Outlook) und den vollständigen Text des Dialogs, z. B. die Frage, ob Änderungen an einem Dokument gespeichert werden sollen, die Fehlermeldung bei einem falschen Kennwort für ein geschütztes Dokument oder die Rückfrage beim Leeren des Ordners „Gelöschte Elemente“ in Outlook.

Aus digitalforensischer Sicht belegt ein Eintrag, dass die Anwendung den Dialog zum angegebenen Zeitpunkt angezeigt hat. Nennt der Text eine Datei, war sie zu diesem Zeitpunkt in der Anwendung geöffnet oder es wurde versucht, sie zu öffnen; die Speichern-Abfrage zeigt zusätzlich, dass das Dokument ungespeicherte Änderungen hatte. Welche Schaltfläche der Nutzer im Dialog gewählt hat und unter welchem Benutzerkonto die Anwendung lief, ist nicht protokolliert.

## Spezifische Kurzinformation

1. Verfügbarkeit: seit Office 2010, für alle Office-Desktopanwendungen
2. Voraussetzungen: standardmäßig aktiv; Einträge entstehen nur, wenn ein Dialog angezeigt wird
3. Aufbewahrung: wie bei anderen Ereignisprotokollen werden bei Erreichen der Maximalgröße die ältesten Einträge überschrieben; das Protokoll kann gelöscht werden
4. Format und Struktur: EVTX-Protokoll `OAlerts`; alle Einträge haben die Ereignis-ID 300, die Quelle nennt die Office-Version (z. B. `Microsoft Office 16 Alerts`); der Dialogtext steht in der Sprache der Office-Oberfläche und enthält bei Dateien meist nur den Dateinamen, nicht den Pfad
5. Zeitstempel: UTC; Zeitpunkt, zu dem der Dialog angezeigt wurde
6. Besonderheiten und Fallstricke: nicht jeder Eintrag geht auf einen sichtbaren Dialog zurück; manche sind interne Meldungen, z. B. Fehler beim Laden von Add-ins
7. Ablageort:  
   **`C:\Windows\System32\winevt\Logs\OAlerts.evtx`**

## Referenzen

2026-11 (abgerufen): <https://www.cyberengage.org/post/oalerts-evtx-the-hidden-microsoft-office-evidence-log>

2024-03: <https://dsforensics.com/ds-forensics-inc-articles/windows-event-logs-tracking-file-edits-and-deletions>

2021-02: <https://nasbench.medium.com/finding-forensic-goodness-in-obscure-windows-event-logs-60e978ea45a3>

## Tools

EvtxECmd - <https://ericzimmerman.github.io/>

evtx (evtx_dump) - <https://github.com/omerbenamram/evtx>

DLEAPP (Parser: Office Alerts) - <https://github.com/abrignoni/DLEAPP>

evtx2json (oalerts) - <https://github.com/Silv3rHorn/evtx2json>
