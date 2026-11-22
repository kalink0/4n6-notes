---
title: "Snap"
status: complete
completed: 2026-11-22
authors: [kalink0 (Marco Neumann)]
---

# Snap

Snap ist ein Paketformat und Verteilungssystem für Linux-Programme von Canonical, bei dem ein Programm mit den benötigten Bibliotheken in einem schreibgeschützten Dateisystem-Abbild (SquashFS) steckt und unabhängig von den Paketen der Distribution läuft.

Snaps werden über den Dienst snapd installiert, meist aus dem Snap Store, und standardmäßig automatisch aktualisiert (bis zu viermal am Tag). Jede Version eines Snaps ist eine Revision; snapd hängt das Abbild jeder Revision in einem eigenen Ordner ein. Die meisten Snaps laufen abgeschottet vom übrigen System (Strict-Confinement) und erhalten nur Zugriff auf freigegebene Schnittstellen; Snaps mit Classic-Confinement laufen ohne diese Abschottung. Unter Ubuntu ist Snap vorinstalliert.

Aus digitalforensischer Sicht legen abgeschottete Snaps ihre Daten nicht an den üblichen Orten im Benutzerordner ab, sondern in einem eigenen Ordner je Snap und Revision. Bei einem Update kopiert snapd die Daten in die neue Revision; die Ordner älterer Revisionen, die snapd noch behält, enthalten den Stand vor dem Update. Daten, die für alle Revisionen gelten, liegen im Ordner `common`.

- Programmdateien: **`/var/lib/snapd/snaps/{SNAP_NAME}_{REVISION}.snap`**, eingehängt unter **`/snap/{SNAP_NAME}/{REVISION}`** (auf manchen Distributionen **`/var/lib/snapd/snap`**)
- Benutzerdaten: **`~/snap/{SNAP_NAME}/{REVISION}`**, **`~/snap/{SNAP_NAME}/common`**
- Systemdaten: **`/var/snap/{SNAP_NAME}/{REVISION}`**, **`/var/snap/{SNAP_NAME}/common`**
