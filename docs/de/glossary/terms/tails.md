---
title: "Tails Linux"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
---

# Tails Linux

Tails ist ein portables Betriebssystem, das von einem USB-Stick gestartet wird und über besondere Sicherheitsmechanismen zum Schutz vor Überwachung verfügt.

Bei jedem Ausschalten des Systems werden standardmäßig alle Änderungen, die während des Betriebs vorgenommen wurden, verworfen und das Betriebssystem auf den Ursprungszustand zurückgesetzt. Dies betrifft sowohl Änderungen, die durch den Nutzer vorgenommen wurden, als auch durch das System bzw. Programme getätigte Änderungen. Insbesondere werden auch alle Log-Dateien, die durch Verwendung von Software erzeugt wurden, gelöscht. Lediglich ein gesonderter Speicherbereich („Persistent Storage“) kann zur dauerhaften Ablage von Nutzerdaten verwendet werden und wird nicht überschrieben. In diesem Bereich werden jedoch keinerlei Systemdateien gespeichert.

Der Persistent Storage ist mit LUKS verschlüsselt; zur Extraktion der eventuell dort gespeicherten Daten ist das Nutzerpasswort notwendig.