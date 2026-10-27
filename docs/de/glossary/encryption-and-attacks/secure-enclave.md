---
title: "Secure Enclave"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Secure Enclave

Die Secure Enclave ist ein vom Hauptprozessor getrenntes Sicherheitssubsystem in Apple-Chips, das Schlüssel verwaltet und die Prüfung des Gerätecodes übernimmt.

Sie ist seit dem iPhone 5s (A7) in iPhones und iPads verbaut, bei Macs im T2-Chip und in den Apple-Silicon-Prozessoren. Die Secure Enclave hat einen eigenen Prozessor und ein eigenes Betriebssystem (sepOS). Sie besitzt einen bei der Herstellung festgelegten, gerätespezifischen Schlüssel (UID), der sich nicht auslesen lässt. Aus diesem Schlüssel und dem Gerätecode werden die Schlüssel für die Datenverschlüsselung abgeleitet. Daneben verarbeitet sie die Daten für Touch ID und Face ID. Häufig wird sie mit SEP (Secure Enclave Processor) abgekürzt. Die Abkürzung SE steht dagegen meist für den eigenständigen Sicherheitschip (Secure Element), den Apple getrennt davon für Apple Pay einsetzt.

Aus digitalforensischer Sicht lassen sich die Daten nur auf dem Gerät selbst entschlüsseln, da die Schlüssel an die UID gebunden sind; das Auslesen des abgelösten Speicherchips (Chip-Off) oder ein Passwortangriff auf einem anderen System führt nicht zum Ziel. Die Secure Enclave setzt nach Fehlversuchen zunehmende Wartezeiten durch und löscht, falls eingestellt, nach zehn Fehlversuchen die Schlüssel. Seit dem A12 (iPhone XS) wird der Fehlversuchszähler zusätzlich in einem eigenen Speicherbaustein (Secure Storage Component) geschützt. Ob und wie schnell ein Angriff auf den Gerätecode möglich ist, hängt daher von Gerätegeneration, iOS-Version und verfügbaren Exploits ab.
