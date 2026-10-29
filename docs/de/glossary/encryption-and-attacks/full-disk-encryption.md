---
title: "Vollverschlüsselung (FDE)"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Vollverschlüsselung (FDE)

Bei einer Vollverschlüsselung (Full Disk Encryption, FDE) wird ein gesamter Datenträger oder ein gesamtes Volume mit einem gemeinsamen Schlüssel verschlüsselt, unabhängig davon, welche Dateien darauf gespeichert sind.

Der Schlüssel wird beim Start des Systems bzw. beim Einbinden des Volumes einmalig freigeschaltet, z. B. durch ein Passwort, eine PIN oder ein Trusted Platform Module (TPM). Danach sind alle Daten auf dem Volume für das Betriebssystem im Klartext lesbar, bis es wieder gesperrt bzw. das System ausgeschaltet wird. Beispiele sind BitLocker, FileVault, LUKS und VeraCrypt. Ältere Android-Versionen (bis Android 9) setzten ebenfalls auf FDE.

Aus digitalforensischer Sicht ist ein Volume mit FDE entweder vollständig oder gar nicht zugänglich. Wird ein laufendes System mit entsperrtem Volume vorgefunden, kann eine Live-Sicherung die Daten im Klartext sichern, die nach dem Ausschalten ohne Passwort oder Recovery Key nicht mehr zugänglich wären. Nach der Entschlüsselung lassen sich gelöschte Dateien wie bei einem unverschlüsselten Volume wiederherstellen, da der Schlüssel für das gesamte Volume gilt.
