---
title: "Unallocated Cluster"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
---

# Unallocated Cluster

Unallocated Cluster (nicht allozierte Speicherbereiche) wurden vom Betriebssystem innerhalb einer Partition als frei markiert.

Wenn eine Datei gelöscht wird, markiert das Betriebssystem die Speicherbereiche, in denen die Daten der Datei liegen, als „Unallocated“ und somit freien Speicher. Die eigentlichen Daten werden jedoch nicht umgehend gelöscht. Somit können ehemals existierende Daten aus diesen Speicherbereichen wiederhergestellt werden.

Werden Daten ohne Bezug zum Dateisystem (z. B. durch Carving) wiederhergestellt, liegen keine Dateisystemmetadaten vor. Somit kann keine Aussage über Zeitstempel, Dateipfad und zuordenbaren Benutzeraccount getroffen werden. Auch können ggf. nur Teile einer Datei (zum Beispiel Bildausschnitte) wiederhergestellt werden.