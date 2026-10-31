---
title: "JTAG"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# JTAG

Bei einer JTAG-Sicherung wird der Speicher eines Geräts über die JTAG-Schnittstelle (Joint Test Action Group, IEEE 1149.1) ausgelesen, eine Test- und Debug-Schnittstelle des Prozessors.

Dazu werden Kabel an Testpunkte auf der Platine gelötet oder mit Federkontakten angeschlossen. Über die Schnittstelle wird der Prozessor gesteuert, der den Speicher ausliest. Das Ergebnis ist eine physische Sicherung.

Aus digitalforensischer Sicht verbleibt der Speicherchip auf der Platine, sodass das Gerät in der Regel funktionsfähig bleibt. Die Sicherung ist langsam, und die Schnittstelle ist bei vielen Geräten nicht zugänglich oder deaktiviert. Ist der Speicher verschlüsselt, liegen die gesicherten Daten nur verschlüsselt vor und lassen sich nur mit dem Passwort bzw. Schlüssel entschlüsseln. Ist der Schlüssel an den Prozessor des Geräts gebunden, wie häufig bei modernen Smartphones, ist das auch mit dem Passwort nicht möglich.
