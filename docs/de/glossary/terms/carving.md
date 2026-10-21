---
title: "Carving"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
---

# Carving

Carving in der digitalen Forensik bezeichnet den Prozess, bei dem Dateien oder Datenfragmente aus einem Datenträger rekonstruiert werden – und zwar ohne auf die regulären Dateisystemmetadaten (wie etwa den Eintrag in einer Master File Table) zurückzugreifen. Dabei werden charakteristische Dateisignaturen (Header, oft auch Footer) im Rohdatenstrom, beispielsweise im Unallocated Space, identifiziert, um die Grenzen von gelöschten oder beschädigten Dateien zu bestimmen und diese anschließend wieder zugreifbar zu machen.

Diese Methode ist besonders nützlich, wenn Dateien gelöscht wurden oder das Dateisystem beschädigt ist und somit keine herkömmlichen Metadaten mehr vorliegen, die eine direkte Wiederherstellung ermöglichen würden.

Für die wiederhergestellten Daten liegen keine Dateisystemmetadaten vor. Somit kann keine Aussage über Zeitstempel, Dateipfad und zuordenbaren Benutzeraccount getroffen werden. Auch können ggf. nur Teile einer Datei (zum Beispiel Bildausschnitte) wiederhergestellt werden, insbesondere wenn die Datei fragmentiert war.

Carving kann auch auf Dateien selbst angewendet werden, um darin befindliche (ggf. versteckte) Dateien zu extrahieren. Auch hier wird dann nicht auf Dateimetadaten, z. B. interne Dateiverzeichnisse wie das Central Directory eines ZIP-Archivs, zurückgegriffen.