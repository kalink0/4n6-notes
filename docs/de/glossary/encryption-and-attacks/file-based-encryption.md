---
title: "Dateibasierte Verschlüsselung (FBE)"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Dateibasierte Verschlüsselung (FBE)

Bei einer dateibasierten Verschlüsselung (File-Based Encryption, FBE) wird jede Datei mit einem eigenen Schlüssel verschlüsselt.

Der Schlüssel einer Datei bzw. die Information, aus der er abgeleitet wird, ist in den Metadaten der Datei im Dateisystem gespeichert und selbst mit einem übergeordneten Schlüssel geschützt. Neben dem Dateiinhalt werden je nach Umsetzung auch die Dateinamen verschlüsselt.

Aus digitalforensischer Sicht ist eine Wiederherstellung gelöschter Dateien in der Regel nicht möglich: Mit dem Löschen der Datei geht auch ihr Schlüssel verloren, sodass z. B. mittels Carving gefundene Daten nicht mehr entschlüsselt werden können. Beispiele sind die Verschlüsselung von Android (seit Android 7, ab Android 10 Voraussetzung für die Zertifizierung durch Google; nicht zertifizierte Geräte können auch unverschlüsselt sein) und von iOS/iPadOS (Data Protection) sowie fscrypt unter Linux.
