---
title: "Recovery Key"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Recovery Key

Ein Recovery Key (Wiederherstellungsschlüssel) ist ein beim Einrichten einer Verschlüsselung erzeugter Schlüssel, mit dem sich die Daten auch ohne das eigentliche Passwort entsperren lassen.

Er ist für den Fall gedacht, dass das reguläre Entsperren nicht mehr möglich ist, z. B. weil das Passwort vergessen wurde oder das Gerät den Schlüssel nach einer Änderung an Hardware oder Firmware nicht mehr automatisch freigibt. Recovery Keys gibt es nicht nur bei der Verschlüsselung von Datenträgern, sondern z. B. auch für Ende-zu-Ende-verschlüsselte Cloud-Daten (erweiterter Datenschutz für iCloud), für verschlüsselte Chat-Backups (WhatsApp) oder für Passwortmanager. Bei BitLocker ist er ein 48-stelliges Zahlenpasswort in acht Blöcken zu je sechs Ziffern. Beim Entsperren wird eine Schlüssel-ID angezeigt, über die sich der passende Recovery Key zuordnen lässt. Bei FileVault besteht er aus 24 Buchstaben und Ziffern in sechs Blöcken.

Aus digitalforensischer Sicht wird der Recovery Key häufig außerhalb des Geräts gespeichert: BitLocker-Schlüssel können im Microsoft-Konto hinterlegt sein, in Unternehmen im Active Directory, in Entra ID oder in einer Geräteverwaltung (MDM). FileVault-Schlüssel können im iCloud-Konto oder in einer MDM hinterlegt sein. Daneben finden sich Recovery Keys als Ausdruck, als Textdatei (bei BitLocker mit der Schlüssel-ID im Dateinamen) auf USB-Sticks oder anderen Geräten oder in Passwortmanagern. Die Suche auf anderen sichergestellten Datenträgern und eine Anfrage beim Anbieter des Kontos sind daher oft der aussichtsreichste Weg zu verschlüsselten Daten. Bei Ende-zu-Ende-verschlüsselten Diensten sollte der Recovery Key dem Anbieter dagegen nicht vorliegen.
