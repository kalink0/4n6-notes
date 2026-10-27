---
title: "In-System Programming (ISP)"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# In-System Programming (ISP)

Bei einer ISP-Sicherung wird ein Speicherchip, meist ein eMMC-Chip, direkt auf der Platine ausgelesen, indem ein Lesegerät an dessen Datenleitungen angeschlossen wird, ohne den Chip abzulösen.

Dazu werden feine Drähte an Testpunkte oder Bauteile auf der Platine gelötet, die mit den Datenleitungen des Chips verbunden sind. Der Prozessor des Geräts wird dabei vom Zugriff auf den Speicher abgehalten. Das Ergebnis ist eine physische Sicherung.

Aus digitalforensischer Sicht ist ISP schneller als JTAG und weniger riskant als ein Chip-Off, da der Chip keiner Hitze ausgesetzt wird und das Gerät in der Regel funktionsfähig bleibt. Ist der Speicher verschlüsselt, liegen die gesicherten Daten nur verschlüsselt vor und lassen sich nur mit dem Passwort bzw. Schlüssel entschlüsseln. Ist der Schlüssel an den Prozessor des Geräts gebunden, wie häufig bei modernen Smartphones, ist das auch mit dem Passwort nicht möglich.
