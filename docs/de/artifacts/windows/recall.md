---
title: "Windows Recall"
status: complete
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
topics: [program-execution]
---

# Windows Recall

## Bedeutung

Windows Recall ist eine KI-gestützte Funktion für sogenannte Copilot+-PCs (Windows 11, ab Version 24H2, benötigt entsprechende NPU-Hardware), die in periodischen Abständen Screenshots des Bildschirminhalts anfertigt. Die Screenshots werden lokal per OCR (Texterkennung) sowie semantischer Analyse ausgewertet und durchsuchbar gemacht, sodass Nutzer frühere Bildschirminhalte per Stichwort- oder inhaltlicher Suche wiederfinden können.

Aus digitalforensischer Sicht bedeutet ein Recall-Eintrag, dass zum protokollierten Zeitpunkt das erfasste Fenster/die erfasste Anwendung auf dem Bildschirm sichtbar war – inklusive des zu diesem Zeitpunkt dargestellten Inhalts. Nicht belegt ist dagegen, dass der Nutzer den Inhalt wahrgenommen oder mit ihm interagiert hat. Ebenso belegt das Fehlen eines Inhalts nicht, dass er nicht angezeigt wurde.

## Spezifische Kurzinformation

1. Voraussetzung: Copilot+-PC-Hardware (NPU)
2. Standardmäßig deaktiviert; Aktivierung erfordert aktive Nutzerinteraktion (Opt-in). Einzelne Anwendungen können sich zusätzlich selbst von der Erfassung ausschließen
3. Vor April 2025 unverschlüsselt zugänglich (aber nicht breit verteilt). Seit April 2025 (breite Verfügbarkeit) via VBS-Enclave verschlüsselt, Entschlüsselung nur durch Windows Hello des Nutzers am laufenden System
4. Inkognito-/Privates Browsing wird im Screenshot ausgeblendet – Fenstertitel-Änderungen werden aber weiterhin erfasst
5. Sensible Inhalte (Passwörter, Ausweis- und Kreditkartennummern) sollen standardmäßig herausgefiltert werden
6. Älteste Snapshots werden bei Erreichen des Speicherlimits gelöscht; optional zeitliche Begrenzung (30–180 Tage)
7. Zentrale Tabelle: `WindowCapture`; Fensterereignisse mit Zeitstempel und Fenstertitel, Snapshot-Ereignisse verweisen auf den Screenshot
8. Screenshots liegen als JPEG separat vor (`ImageStore`), referenziert aus der Datenbank; enthalten zusätzlich EXIF-Daten
9. Ablageort:  
   **`%USERPROFILE%\AppData\Local\CoreAIPlatform.00\UKP\{GUID}\`** (darin: ukg.db, SemanticTextStore.sidb, SemanticImageStore.sidb, Ordner ImageStore)

## Referenzen

2026-04: <https://www.windowscentral.com/microsoft/windows-11/why-this-windows-recall-feature-raises-real-security-questions>

2025-12: <https://learn.microsoft.com/en-us/windows/client-management/manage-recall>

2025-10: <https://securelist.com/forensic-artifacts-in-windows-11/117680/>

2024-09: <https://blogs.windows.com/windowsexperience/2024/09/27/update-on-recall-security-and-privacy-architecture/>

2024-09: <https://medium.com/@boutnaru/the-windows-forensic-journey-ukg-db-windows-recall-e2413841ade8>

2024-06: <https://cybercx.com.au/blog/forensic-applications-of-microsoft-recall/>

## Tools

TotalRecall / TotalRecall Reloaded - <https://github.com/xaitax/TotalRecall>

KAPE (Target: WindowsCopilotRecall) - <https://github.com/EricZimmerman/KapeFiles/blob/master/Targets/Windows/WindowsCopilotRecall.tkape>

Velociraptor (Artefakte: Windows.System.Recall.WindowCaptureEvent, Windows.System.Recall.AllWindowEvents) - <https://docs.velociraptor.app/exchange/artifacts/pages/windows.system.recall.windowcaptureevent/>