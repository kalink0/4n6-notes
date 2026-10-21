---
title: "AmCache - Application Activity Cache"
status: complete
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
topics: [installed-software, program-execution]
---

# AmCache - Application Activity Cache

## Bedeutung

Der AmCache ist Teil der Kompatibilitätsinfrastruktur von Windows. Er speichert Informationen zu Programmdateien (Executables, DLLs), installierten Anwendungen sowie Geräten und Treibern. Ziel ist es, die Kompatibilität von Programmen und Treibern regelmäßig zu überprüfen und so eine schnelle und komplikationsfreie Ausführung zu gewährleisten. Die Einträge werden unter anderem durch einen geplanten Task (Microsoft Compatibility Appraiser) erstellt und aktualisiert.

Aus digitalforensischer Sicht belegt ein Eintrag, dass die Applikation bzw. der Treiber zum Zeitpunkt der Erfassung für das System erreichbar war, lokal, auf einem Wechseldatenträger oder auf einem Netzlaufwerk. Einträge liefern zudem Identifikationsmerkmale wie Hashwerte, Pfade und Signatur. Nicht belegt ist dagegen, dass die Applikation bzw. der Treiber ausgeführt wurde, und ebenso wenig, dass der Zeitstempel eines Eintrags dem Zeitpunkt entspricht, zu dem die Datei auf das System gelangt ist.

## Spezifische Kurzinformation

1. Verfügbarkeit: nativ ab Windows 8; unter Windows 7 durch Updates nachgerüstet (davor RecentFileCache.bcf)
2. Voraussetzungen: standardmäßig aktiv
3. Format und Struktur: Registry-Hive; Aufbau abhängig von Windows-Version und Update-Stand
4. Zeitstempel: FILETIME, UTC; LastWrite-Zeit eines Eintrags = letzte Aktualisierung, nicht Ausführung
5. Besonderheiten und Fallstricke: SHA1 bei großen Dateien nur über die ersten 30 MB; Transaktionslogs (`.LOG1`/`.LOG2`) einbeziehen
6. Ablageort:  
   **C:\Windows\AppCompat\Programs\Amcache.hve**

## Referenzen

2025-10: <https://securelist.com/amcache-forensic-artifact/117622/>

2024-10: <https://www.magnetforensics.com/blog/shimcache-vs-amcache-key-windows-forensic-artifacts/>

2024-05: <https://www.thedfirspot.com/post/evidence-of-program-existence-amcache>

2019-07: <https://cyber.gouv.fr/sites/default/files/2019/01/anssi_dfirsummit_2019-amcache_investigation.pdf>

2019-01: <https://cyber.gouv.fr/sites/default/files/2019/01/anssi-coriin_2019-analysis_amcache.pdf>

## Tools

AmcacheParser - <https://github.com/EricZimmerman/AmcacheParser>

AmCache-EvilHunter - <https://github.com/cristianzsh/amcache-evilhunter>

RegRipper (amcache) - <https://github.com/keydet89/RegRipper4.0>