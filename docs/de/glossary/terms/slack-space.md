---
title: "Uninitialized Cluster / Slack Space"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
---

# Uninitialized Cluster / Slack Space

Slack Space bezeichnet den Speicherbereich am Ende eines allozierten Clusters, der aufgrund der festen Clustergröße und der ggf. kleineren Dateigröße nicht von der Datei belegt wird und noch kleine Mengen von ehemals vorhandenen Dateien enthalten kann. Ein Sonderfall sind Uninitialized Cluster (nicht-initialisierte Speicherbereiche, auch VDL Slack genannt): Cluster, die einer Datei zugewiesen, aber nie beschrieben wurden und daher ebenfalls Daten ehemals vorhandener Dateien enthalten können.

Aufgrund der Clustergrößen (aktuell zumeist 4 kByte Standard) ist die zu erwartende Datenmenge im Slack am Dateiende stets kleiner als die Clustergröße.

Für die wiederhergestellten Daten liegen keine Dateisystemmetadaten vor. Somit kann keine Aussage über Zeitstempel, Dateipfad und zuordenbaren Benutzeraccount getroffen werden. Auch können ggf. nur Teile einer Datei (z. B. einzelne Wörter einer Textdatei) wiederhergestellt werden.