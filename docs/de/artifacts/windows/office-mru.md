---
title: "Office MRU"
status: reviewed
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
reviewers: [dugeonlady]
reviewed: 2026-10-26
topics: [file-access]
---

# Office MRU

## Bedeutung

Microsoft Office speichert die zuletzt geöffneten Dateien und die zuletzt verwendeten Ordner, in denen die Dateien lagen, um die Bedienung durch den Nutzer angenehmer zu gestalten.

Aus digitalforensischer Sicht bedeuten Einträge in der Office MRU, dass die angegebenen Dateien (gemäß Dateiname) unter dem angegebenen Dateipfad durch das Nutzerkonto in Microsoft Office geöffnet wurden. Der angegebene Zeitstempel entspricht hierbei dem Zeitpunkt des letzten Öffnens des Dokumentes.

## Spezifische Kurzinformation

1. Format und Struktur: File MRU = Zuletzt geöffnete Dateien. Place MRU = Zuletzt aufgerufene/verwendete Ordner zum Öffnen/Speichern von Dateien
2. Besonderheiten und Fallstricke: Wenn ACCOUNT = LiveID_xxxx -> Microsoft Account, wenn ACCOUNT = ADAL -> Azure Active Directory (heute Microsoft Entra ID); zusätzlich kommt ACCOUNT = AD_xxxx vor
3. Ablageort:  
   **`HKCU\SOFTWARE\Microsoft\Office\{VERSION}\{APPNAME}\User MRU\{ACCOUNT}\File MRU`**  
   **`HKCU\SOFTWARE\Microsoft\Office\{VERSION}\{APPNAME}\User MRU\{ACCOUNT}\Place MRU`**  
   **`HKCU\SOFTWARE\Microsoft\Office\{VERSION}\{APPNAME}\File MRU`**  
   **`HKCU\SOFTWARE\Microsoft\Office\{VERSION}\{APPNAME}\Place MRU`**

## Referenzen

2024-02: <https://nk0.gitbook.io/dfir/windows/forensics/evidence-of-execution/office-apps-forensics/file-mru>

2023-05: <https://www.cyberengage.org/post/registry-user-activity-tracking-recently-opened-files-in-microsoft-office-a-forensic-guide>

## Tools

RegRipper (msoffice) - <https://github.com/keydet89/RegRipper4.0>