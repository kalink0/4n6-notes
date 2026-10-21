---
title: "Prefetch"
status: complete
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
topics: [program-execution]
---

# Prefetch

## Bedeutung

Das Betriebssystem Windows erstellt sogenannte Prefetch-Dateien. Diese Dateien beinhalten mindestens die letzte Ausführung eines Programms, die Anzahl der Ausführungen und die geladenen Libraries und Dateien beim Starten. Zusätzlich können bis zu 7 weitere Zeitpunkte von Programmausführungen enthalten sein. Der Nutzen dieser Prefetch Dateien liegt darin, dass das Betriebssystem technische Maßnahmen ergreifen kann um einen schnelleren Start von Applikationen zu ermöglichen und somit die Benutzererfahrung verbessert.

Aus digitalforensischer Sicht bedeutet die Existenz und der Inhalt einer Prefetch Datei, dass eine referenzierte Applikation auf dem System zu den angegebenen Zeitpunkten gestartet wurde. Zusätzlich lässt sich sagen, welche Libraries und Dateien beim Start der Applikation verwendet werden.

## Spezifische Kurzinformation

1. Kann über **`HKLM\SYSTEM\{CURRENT_CONTROL_SET}\Control\Session Manager\Memory Management\PrefetchParameters\EnablePrefetcher`** deaktiviert sein; auf Servern teils nicht aktiv
2. Seit Windows 8 maximal 1024 Dateien, davor 128
3. Seit Windows 10 komprimiert (MAM), nicht direkt lesbar
4. Zeitstempel als FILETIME in UTC
5. Die erste Ausführung ergibt sich aus dem Erstelldatum der .pf-Datei; die Datei wird ca. 10 Sekunden nach dem Start geschrieben
6. Dateiname enthält einen Hash des Programmpfads; dasselbe Programm aus verschiedenen Pfaden ergibt getrennte Dateien
7. Ablageort:  
   **`C:\Windows\Prefetch\*.pf`**

## Referenzen

2026-07: <https://github.com/libyal/libscca/blob/main/documentation/Windows%20Prefetch%20File%20(PF)%20format.asciidoc>

2025-12: <https://y0sh1mitsu.github.io/posts/how-are-prefetch-created/>

2023-07: <https://trustedsec.com/blog/prefetch-the-little-snitch-that-tells-on-you>

2022-10: <https://isc.sans.edu/diary/Forensic+Value+of+Prefetch/29168/>

2015-06: <https://blog.digital-forensics.it/2015/06/a-first-look-at-windows-10-prefetch.html>

2015-01: <https://www.sans.org/blog/what-is-new-in-windows-application-execution/>

2013-09: <https://www.hecfblog.com/2013/09/daily-blog-72-understanding-artifacts.html>

2026-10 (abgerufen): <https://forensics.wiki/prefetch/>

## Tools

PECmd - <https://ericzimmerman.github.io/>

WinPrefetchView - <https://www.nirsoft.net/utils/win_prefetch_view.html>

DLEAPP (Parser: Prefetch, Prefetch Files Loaded) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (Artefakt: Windows.Forensics.Prefetch) - <https://docs.velociraptor.app/artifact_references/pages/windows.forensics.prefetch>

Dissect (Plugin: prefetch) - <https://docs.dissect.tools/en/stable/plugins/prefetch.html>