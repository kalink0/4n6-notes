---
title: "USN Journal"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [file-system-changes]
---

# USN Journal

## Bedeutung

Das USN (Update Sequence Number) - Journal wid vom Windows Betriebssystem für NTFS-Dateisysteme geschrieben. Es enthält Informationen zu ausgeführten Befehlen bezogen auf Dateien. Zum Beispiel *"Datei erstellt", "Datei gelöscht", Datei vergrößert/verkleinert".*

Je nach Aktitivät auf der NTFS-Partition liegen Daten für bis zu mehreren Wochen vor.

Aus digitalforensischer Sicht kann gesagt werden, dass Einträge im USN Journal bedeuten, dass die aufgeführten Aktionen zu dem angegebenen Zeitpunkt auf den aufgeführten Dateien ausgeführt wurden. Es liegen hier der Dateiname und der Verweis zum Dateipfad im USN Journal vor.

## Spezifische Kurzinformation

1. USN Journal ist seit Windows Vista standardmäßig aktivert
2. Um die Pfade einer Datei ebenfalls zu erhalten, müssen die Daten mit den Einträgen der MFT korreliert werden
3. Maximale Größe liegt standardmäßig bei 30 - 40 MB (logische Dateigröße von $J durch Sparse-Bereich deutlich größer) - je nach Verwendung der Partition kann man 1 - 2 Wochen in die Vergangenheit schauen
4. Ablageort (Im Root-Verzeichnis einer NTFS-Partition):  
   **`\$Extend\$UsnJrnl`**  
   **`$J`** - Alternate Data Stream - beinhaltet das eigentliche Journal  
   **`$Max`** - Alternate Data Stream - beinhaltet Metadaten zur maximalen Größe des Journals

## Referenzen

2026-09: <https://www.it-connect.tech/windows-forensics-part-10-analyzing-the-ntfs-usn-journal/>

2022-11: <https://blog.haboob.sa/blog/advanced-usn-journal-forensics>

2020-11: <https://docs.velociraptor.app/blog/2020/2020-11-13-the-windows-usn-journal-f0c55c9010e/>

2013-01: <https://journeyintoir.blogspot.com/2013/01/re-introducing-usnjrnl.html>

## Tools

Usnjrnl2Csv - <https://github.com/jschicht/UsnJrnl2Csv>

MFTECmd - <https://ericzimmerman.github.io/>

DLEAPP (Parser: USN Journal) - <https://github.com/abrignoni/DLEAPP>

Dissect (Plugin: usnjrnl) - <https://docs.dissect.tools/en/stable/plugins/usnjrnl.html>

dfir_ntfs - <https://github.com/msuhanov/dfir_ntfs>