---
title: "UserAssist"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [program-execution]
---

# UserAssist

## Bedeutung

Das Betriebssystem Windows bringt die Funktion "User Assist" mit. Diese Funktion dient dazu anhand der ausgeführten Programme des Benutzerkontos die zuletzt ausgeführten Programme im Startmenü des Betriebssystem anzeigen zu können. Es dient somit der Benutzerfreundlichkiet des Betriebssystems.

Aus digitalforensischer Sicht geben Einträge in der User Assist Auskunft darüber, wann zuletzt, wenn möglich wie häufig insgesamt und wie lange eine Applikation in Verwendung des referenzierten Benutzerkontos war. Zusätzlich kann gesagt werden, wie eine Applikation ausgeführt wurde. Die Applikation muss zum Zeitpunkt der Ausführung auf dem System zur Verfügung gestanden haben.

## Spezifische Kurzinformation

1. Einträge sind ROT-13 kodiert
2. Erfasst nur über die Windows-Oberfläche gestartete Programme (Startmenü/Suche, Desktop, Explorer, Taskleiste, Ausführen); Starts über die Kommandozeile i.d.R. nicht
3. Kann pro Benutzer über die Datenschutzeinstellung "App-Starts nachverfolgen" deaktiviert werden
4. Ablageort (Registry): **`HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{GUID}\Count`**

## Referenzen

2026-03: <https://www.cybertriage.com/blog/userassist-forensics-2025/>

2025-09: <https://www.magnetforensics.com/blog/artifact-profile-userassist/>

2013-08: <https://www.hecfblog.com/2013/08/daily-blog-45-understanding-artifacts.html>

2013-05: <https://www.4n6k.com/2013/05/userassist-forensics-timelines.html>

## Tools

UserAssistView - <https://www.nirsoft.net/utils/userassist_view.html>

RegRipper (Plugin: userassist) - <https://github.com/keydet89/RegRipper4.0>

Registry Explorer (Bookmark: UserAssist) - <https://ericzimmerman.github.io/>

DLEAPP (Parser: UserAssist) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (Artefakt: Windows.Registry.UserAssist) - <https://docs.velociraptor.app/artifact_references/pages/windows.registry.userassist/>

Dissect (Plugin: userassist) - <https://docs.dissect.tools/en/stable/plugins/userassist.html>