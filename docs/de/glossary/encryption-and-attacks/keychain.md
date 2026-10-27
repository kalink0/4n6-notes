---
title: "Keychain"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Keychain

Die Keychain (Schlüsselbund) ist der Systemdienst von Apple, in dem Apps und Betriebssystem unter iOS und macOS Passwörter, Tokens, Zertifikate und Schlüssel geschützt ablegen.

Typische Einträge sind WLAN-Passwörter, Zugangsdaten von Konten und Webseiten sowie Schlüssel für verschlüsselte App-Datenbanken. Unter iOS liegt die Keychain in einer SQLite-Datenbank (`/private/var/Keychains/keychain-2.db`), deren Einträge mit Schlüsseln verschlüsselt sind, die an das vom Hauptprozessor getrennte Sicherheitssubsystem des Apple-Chips (Secure Enclave) gebunden sind. Unter macOS gibt es zusätzlich dateibasierte Keychains, z. B. `~/Library/Keychains/login.keychain-db`, die mit dem Benutzerpasswort geschützt sind. Über die iCloud-Keychain können Einträge zwischen den Geräten eines Apple-Kontos synchronisiert werden.

Aus digitalforensischer Sicht lässt sich die iOS-Keychain nur auf dem Gerät selbst entschlüsseln. Forensische Tools sichern sie bei einer Sicherung des vollständigen Dateisystems (Full File System) mit. Welche Einträge entschlüsselt werden können, hängt davon ab, ob das Gerät seit dem letzten Neustart bereits einmal entsperrt wurde (After First Unlock, AFU) oder nicht (Before First Unlock, BFU). In verschlüsselten iTunes- bzw. Finder-Backups sind Keychain-Einträge enthalten, sofern sie nicht auf das Gerät beschränkt sind; in unverschlüsselten Backups sind sie nicht auswertbar. Da manche Apps ihre Datenbanken mit einem Schlüssel aus der Keychain verschlüsseln, ist die Keychain häufig Voraussetzung, um diese Daten überhaupt auswerten zu können.
