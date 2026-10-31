---
title: "Jailbreak"
status: complete
completed: 2026-10-31
authors: [kalink0 (Marco Neumann)]
---

# Jailbreak

Ein Jailbreak hebt die Sicherheitsbeschränkungen von iOS bzw. iPadOS auf, sodass sich Code ohne Signatur von Apple und mit Root-Rechten ausführen lässt.

Ein Jailbreak nutzt Sicherheitslücken im Betriebssystem oder in der Startkette des Geräts aus. Lücken im Boot-ROM (z. B. checkm8 bei Geräten bis zum A11-Chip) lassen sich nicht per Update schließen. Je nach Art muss der Jailbreak nach jedem Neustart erneut ausgeführt werden. Danach sind Zugriff auf das gesamte Dateisystem, eine Root-Shell und die Installation von Erweiterungen (Tweaks) über Paketmanager wie Cydia oder Sileo möglich. Neuere Jailbreaks (rootless, seit iOS 15) verändern das Systemvolume nicht, sondern legen ihre Dateien unter **`/var/jb`** ab.

Aus digitalforensischer Sicht verändert ein Jailbreak das System. Spuren eines Jailbreaks sind z. B. installierte Paketmanager oder der Ordner **`/var/jb`**. Bei einem Gerät mit Jailbreak ist ein weitergehender Zugriff möglich, z. B. auf das gesamte Dateisystem, solange der Jailbreak aktiv ist.
