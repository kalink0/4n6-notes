---
title: "JBOD"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
---

# JBOD

JBOD (Just a Bunch of Disks) bezeichnet mehrere Datenträger, die ohne Striping und ohne Redundanz betrieben werden, entweder jeweils als eigenes Laufwerk oder hintereinander verbunden zu einem logischen Laufwerk (Spanning).

Beim Spanning wird der Speicherplatz der Datenträger aneinandergehängt: Ist der erste Datenträger voll, werden die Daten auf dem nächsten fortgesetzt. Die Datenträger können unterschiedlich groß sein. Fällt ein Datenträger aus, sind die darauf liegenden Daten verloren und das Dateisystem ist in der Regel nicht mehr vollständig lesbar. Spanning bieten u. a. RAID-Controller, NAS-Systeme und Betriebssysteme an, z. B. als Modus „linear“ in mdadm unter Linux oder als übergreifendes Volume unter Windows.

Aus digitalforensischer Sicht ergibt sich bei Spanning ein lesbares Dateisystem erst aus dem Zusammenbau der einzeln gesicherten Datenträger in der richtigen Reihenfolge. Da die Daten nicht in Stripes verteilt werden, liegen Dateien auf einem einzelnen Datenträger meist zusammenhängend vor und lassen sich auch ohne die übrigen Datenträger per Carving wiederherstellen, sofern sie nicht über die Grenze zwischen zwei Datenträgern reichen oder fragmentiert sind.
