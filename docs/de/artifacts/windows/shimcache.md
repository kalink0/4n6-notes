---
title: "ShimCache - AppCompatCache"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [program-execution, file-existence]
---

# ShimCache - AppCompatCache

## Bedeutung

Der ShimCache ist ein Feature in Windows-Systemen um die Ausführung von älteren Programmen auf den neuesten Windows-Systemen zu gewährleisten.

Es können der Dateipfad, der Dateiname, die Dateigröße (nur Windows XP/Server 2003) und das letzte Änderungsdatum abgelesen werden.

Aus digitalforensischer Sicht bedeuten Einträge im Shimcache, dass:

1. Wenn das Feld "Is Executed" wahr ist: die Datei mit dem angegeben Namen unter dem angegeben Pfad auf dem System ausgeführt wurde
2. Wenn das Feld "Is Executed" falsch ist: die Datei mit dem angegebenen Namen sich unter dem angegebenen Pfad befunden hat

Es kann anhand dieses Artefakts keine Aussage zum genauen Zeitpunkt getroffen werden - jedoch sehr wohl zur zeitlichen Reihenfolge der Ereignisse.

## Spezifische Kurzinformation

1. Aktuelle/neue ShimCaches werden erst beim Neustart/Herunterfahren des Systems in die Registry geschrieben
2. Der ShimCache beinhaltet bis zu 1024 Einträge
3. Das Feld "Is Executed" gibt es erst ab Windows Vista
4. Ablageort (Registry):
   1. Windows XP: **`HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatibility\AppCompatCache`**
   2. Ab Windows Vista: **`HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache\AppCompatCache`**

## Referenzen

2024-10: <https://www.magnetforensics.com/blog/shimcache-vs-amcache-key-windows-forensic-artifacts/>

2024-08: <https://nullsec.us/windows-10-11-appcompatcache-deep-dive/>

2015-06: <https://cloud.google.com/blog/topics/threat-intelligence/caching-out-the-val/>

## Tools

AppCompatCacheParser - <https://ericzimmerman.github.io/>

RegRipper (Plugin: appcompatcache) - <https://github.com/keydet89/RegRipper4.0>

DLEAPP (Parser: AppCompatCache (Shimcache)) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (Artefakt: Windows.Registry.AppCompatCache) - <https://docs.velociraptor.app/artifact_references/pages/windows.registry.appcompatcache/>

Dissect (Plugin: shimcache) - <https://docs.dissect.tools/en/stable/plugins/shimcache.html>

Volatility 3 (Plugin: windows.shimcachemem, aus dem Arbeitsspeicher) - <https://github.com/volatilityfoundation/volatility3>