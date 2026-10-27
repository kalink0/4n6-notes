---
title: "Trusted Execution Environment (TEE)"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Trusted Execution Environment (TEE)

Eine Trusted Execution Environment (TEE) ist ein vom normalen Betriebssystem abgeschotteter Bereich im Hauptprozessor, in dem sicherheitskritische Programme und Schlüssel getrennt vom übrigen System ausgeführt bzw. gespeichert werden.

Die Trennung wird durch die Hardware umgesetzt, bei Smartphones meist durch eine Sicherheitserweiterung der ARM-Prozessoren (ARM TrustZone). In der TEE läuft ein eigenes kleines Betriebssystem, z. B. Trusty bei Google, QSEE bei Qualcomm oder TEEgris bei Samsung. Unter Android laufen dort unter anderem Keymaster bzw. KeyMint, die die Schlüssel des Android Keystore verwalten, und Gatekeeper, der die Bildschirmsperre prüft und nach Fehlversuchen Wartezeiten durchsetzt. Die Schlüssel für die Datenverschlüsselung werden aus der Bildschirmsperre und einem hardwaregebundenen Schlüssel abgeleitet. Im Unterschied zum Sicherheitssubsystem in Apple-Chips (Secure Enclave) oder zu einem eigenständigen Sicherheitschip (Secure Element) hat die TEE keinen eigenen Prozessor, sondern nutzt denselben wie das normale Betriebssystem.

Aus digitalforensischer Sicht lassen sich die Daten nur auf dem Gerät selbst entschlüsseln; ein Angriff auf die Bildschirmsperre ist nur über das Gerät und nur mit den vorgegebenen Wartezeiten möglich. Da sich die TEE den Prozessor mit dem normalen Betriebssystem teilt, ermöglichen Schwachstellen in der TEE-Implementierung eines Chipsatzherstellers teilweise, diese Schutzmechanismen zu umgehen. Ob und wie schnell ein Zugriff möglich ist, hängt daher stark von Chipsatz, Hersteller und Patchstand ab.
