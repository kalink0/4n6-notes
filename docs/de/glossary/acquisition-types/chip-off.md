---
title: "Chip-Off"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Chip-Off

Bei einem Chip-Off wird der Speicherchip von der Platine eines Geräts abgelöst und mit einem Lesegerät direkt ausgelesen.

Das Ergebnis ist eine physische Sicherung des Speicherchips. Bei reinen NAND-Flash-Chips ohne eigenen Controller muss die Zuordnung der Daten (Fehlerkorrektur, Wear Leveling, Reihenfolge der Blöcke) anschließend rekonstruiert werden, bei eMMC- und UFS-Chips übernimmt das der Controller im Chip.

Aus digitalforensischer Sicht ist ein Chip-Off ein zerstörendes Verfahren: Das Gerät ist danach in der Regel nicht mehr funktionsfähig, und durch die Hitze beim Ablösen können Chip oder Daten beschädigt werden. Ist der Speicher verschlüsselt, liegen die gesicherten Daten nur verschlüsselt vor und lassen sich nur mit dem Passwort bzw. Schlüssel entschlüsseln. Ist der Schlüssel an den Prozessor des Geräts gebunden, wie häufig bei modernen Smartphones, ist das auch mit dem Passwort nicht möglich. Chip-Off wird daher vor allem bei unverschlüsselten oder beschädigten Geräten eingesetzt, z. B. älteren Mobiltelefonen, Navigationsgeräten, Drohnen oder Fahrzeugsystemen.
