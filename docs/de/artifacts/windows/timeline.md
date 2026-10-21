---
title: "Windows Timeline"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [program-execution, file-access]
---

# Windows Timeline

## Bedeutung

Die Windows Timeline ist ein Feature in modernen Windows Systemen (Windows 10, ab Version 1803), welche die Aktivitäten von Nutzeraccounts mitschneidet und diese, wenn eingerichtet, mit der Cloud und anderen Geräten synchronisiert. Die Timeline ist hierbei Nutzerkonto gebunden, zeigt aber auch an, auf welchem Gerät die Aktion durchgeführt wurde.

Es werden Daten wie zum Beispiel laufende Applikationen oder geöffnete Dokumente mitgeschnitten.

Aus digitalforensischer Sicht bedeuten Einträge in der Windows Timeline, dass das entsprechende Nutzerkonto zum angegebenen Zeitpunkt die angegebene Aktion auf dem angegebenen Gerät durchgeführt hat. Eine Aktion kann hier zum Beispiel das Starten eines Programms, das Öffnen einer Datei oder das Holen einer Anwendung in den Vordergrund sein.

## Spezifische Kurzinformation

1. Verfügbar ab Windows 10, Version 1803, in Windows 11 entfernt
2. Speicherdauer 30 Tage mit Online-Account, ca. 5 Tage mit Offline-Account
3. Potentiell Daten von anderen Geräten (Account-gebunden, auch O365 ohne Windows; bei Microsoft-Konten nur bis Juli 2021, bei Azure-AD-Konten auch danach)
4. Ablageort: **`C:\Users\{user}\AppData\Local\ConnectedDevicesPlatform\{userId}\ActivitiesCache.db`**

   userID kann sein: lokaler Username, Microsoft-Account ID, Azure-AD-Account

## Referenzen

2025-10: <https://securelist.com/forensic-artifacts-in-windows-11/117680/>

2020-08: <https://cellebrite.com/en/exploring-the-windows-activity-timeline-part-3-the-value-of-clipboard-content/>

2020-07: <https://cellebrite.com/en/exploring-the-windows-activity-timeline-part-1-the-high-points/>

2020-07: <https://cellebrite.com/en/exploring-the-windows-activity-timeline-part-2-syncing-across-devices/>

## Tools

WxTCmd - <https://ericzimmerman.github.io/>

WindowsTimeline (kacos2000) - <https://github.com/kacos2000/WindowsTimeline>

DLEAPP (Parser: ActivitiesCache) - <https://github.com/abrignoni/DLEAPP>

Dissect (Plugin: activitiescache) - <https://docs.dissect.tools/en/stable/plugins/activitiescache.html>