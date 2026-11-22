---
title: "Flatpak"
status: complete
completed: 2026-11-22
authors: [kalink0 (Marco Neumann)]
---

# Flatpak

Flatpak ist ein Paketformat und Verteilungssystem für Linux-Desktop-Programme, bei dem Programme zusammen mit gemeinsam genutzten Laufzeitumgebungen (Runtimes) unabhängig von den Paketen der Distribution installiert werden und in einer Sandbox laufen.

Programme werden aus Quellen (Remotes) installiert, meist von Flathub, und tragen eine eindeutige Kennung, deren vorderer Teil den Entwickler bezeichnet (z. B. `org.mozilla.firefox`). Eine Installation ist systemweit für alle Benutzer oder nur für einen Benutzer möglich. Flatpak speichert Programme und Runtimes in einem lokalen Repository auf Basis von OSTree, das ähnlich wie Git versioniert. Die Sandbox (bubblewrap) beschränkt den Zugriff auf Dateien und Geräte; Zugriff auf Dateien außerhalb erhält ein Programm über Berechtigungen oder über Portale, z. B. den Dateidialog des Desktops.

Aus digitalforensischer Sicht legen Flatpak-Programme ihre Einstellungen, Daten und Caches nicht an den üblichen Orten im Benutzerordner ab, sondern in einem eigenen Ordner je Programm. Was ein Programm über ein Portal öffnet, kann der Desktop unter dem Namen des Portals statt unter dem Namen des Programms protokollieren.

- Programmdaten je Benutzer: **`~/.var/app/{APP_ID}/`** mit den Unterordnern `config`, `data` und `cache`
- Systemweite Installation: **`/var/lib/flatpak/`**
- Installation je Benutzer: **`~/.local/share/flatpak/`**
