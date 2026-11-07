---
title: "Apple Remote Desktop"
status: complete
completed: 2026-11-07
authors: [kalink0 (Marco Neumann)]
topics: [program-execution, accounts]
---

# Apple Remote Desktop

## Bedeutung

Apple Remote Desktop (ARD) ist Apples Software zur Verwaltung mehrerer Macs. Auf den verwalteten Macs (Clients) läuft dafür der Dienst Entfernte Verwaltung (Remote Management); das Programm Remote Desktop läuft auf dem Mac des Administrators. Nach einer Reporting-Richtlinie, die der Administrator festlegt, sammelt der Client Daten zur Programmnutzung, zu Benutzeranmeldungen, zum System und eine Liste aller Dateien in lokalen Cache-Dateien. Zum geplanten Zeitpunkt (standardmäßig täglich um Mitternacht) überträgt er sie an den Admin-Mac oder einen Task Server, der sie in seiner Datenbank speichert und die Cache-Dateien jedes Clients zusätzlich ablegt.

Aus digitalforensischer Sicht belegen die Einträge zur Programmnutzung, dass ein Programm auf dem Client lief, mit Startzeit, Laufzeit und Benutzer. Die Einträge zu Anmeldungen belegen An- und Abmeldezeiten eines Benutzers mit Art der Sitzung (Konsole, Terminal, SSH) und teils dem Ursprungsrechner. Auf dem Admin-Mac liegen diese Daten für alle berichtenden Clients, auch wenn sie dort selbst schon gelöscht sind. Unabhängig vom Reporting zeigt der Inhalt `enabled` in der Startkonfiguration der Entfernten Verwaltung, dass sie aktiviert wurde, z.B. über den Befehl `kickstart`.

| Eintragstyp | Belegt | Relevante Felder |
| --- | --- | --- |
| `AppUsage.plist` (Client) | Programm lief auf dem Client, mit Startzeit, Laufzeit und Benutzer | `Launched`, `runLength`, `Frontmost`, `userName` |
| `UserAcct.tmp` (Client) | An- und Abmeldung eines Benutzers am Client | `inTime`, `outTime`, `host` |
| `filesystem.cache` (Client) | Datei war zum Zeitpunkt der Erfassung auf dem Client vorhanden | |
| `rmdb.sqlite3` (Admin) | Programmnutzung und Anmeldungen aller berichtenden Clients | |
| `RemoteManagement.launchd` (Client) | Entfernte Verwaltung wurde aktiviert | |

## Spezifische Kurzinformation

1. Die Pfade sind für macOS 10.14 beschrieben; für neuere Versionen sind sie nicht öffentlich dokumentiert
2. Daten entstehen nur, wenn die Entfernte Verwaltung auf dem Client aktiv ist; Programmnutzung und Anmeldungen nur, wenn die Reporting-Richtlinie des Administrators sie erfasst. Datenbank und Client-Kopien nur auf dem Admin-Mac mit installiertem Remote Desktop
3. Die Cache-Dateien auf dem Client werden nach der Übertragung an den Admin-Mac oft gelöscht; die Datenbank des Admin-Macs kann Daten von über einem Jahr enthalten
4. Plists (`AppUsage.plist` XML oder binär, `AppUsage.tmp` und `UserAcct.tmp` binär), `filesystem.cache` als Datenbank, Admin-Datenbank SQLite
5. Zeitstempel in den Plists als Mac Absolute Time (Sekunden seit 2001-01-01, UTC)
6. Auf dem Admin-Mac sind die Kopien der Client-Caches nach der MAC-Adresse des jeweiligen Clients benannt
7. In der Admin-Datenbank sind laut Mandiant Startzeit und Vordergrundzeit der Programmnutzung vertauscht beschriftet (geprüft unter macOS 10.14)
8. `AppUsage.tmp` enthält meist dieselben oder weniger Einträge als `AppUsage.plist`
9. Ablageort:  
   Client: **`/private/var/db/RemoteManagement/caches/`**  
   Client: **`/Library/Application Support/Apple/Remote Desktop/RemoteManagement.launchd`**  
   Admin: **`/private/var/db/RemoteManagement/RMDB/rmdb.sqlite3`**  
   Admin: **`/private/var/db/RemoteManagement/ClientCaches/`**

## Referenzen

2026-11 (abgerufen): <https://support.apple.com/guide/remote-desktop/apd36ca108c/mac>

2019-10: <https://cloud.google.com/blog/topics/threat-intelligence/leveraging-apple-remote-desktop-for-good-and-evil/>

## Tools

ARDvark - <https://github.com/mandiant/ARDvark>

mac_apt (Plugin: ARD) - <https://github.com/ydkhatri/mac_apt>
