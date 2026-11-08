---
title: "Bildschirmfreigabe"
status: complete
completed: 2026-11-07
authors: [kalink0 (Marco Neumann)]
topics: [data-transfer, network, accounts]
---

# Bildschirmfreigabe

## Bedeutung

Mit der Bildschirmfreigabe (Screen Sharing) sieht und steuert ein Benutzer den Bildschirm eines anderen Macs über das Netzwerk und kopiert Dateien zwischen beiden Rechnern. Die Verbindung hat zwei Seiten, die jeweils eigene Spuren hinterlassen:

- **Verbindender Mac:** Die App Bildschirmfreigabe speichert in ihrer Einstellungsdatei die Verbindungen aus ihrer Verbindungsliste (Adresse, Anzeigename, Benutzername, Gruppen, Zeitpunkt der letzten Verbindung) und eine Liste der Dateiübertragungen (entfernter Rechner, Dateiname, Quell- und Zielpfad, Byte-Zähler, Richtung und Status als Zahlenwerte). Die Sitzungen protokolliert die App in den Unified Logs.
- **Freigebender Mac:** Die Freigabe ist standardmäßig aus und wird in den Systemeinstellungen unter „Teilen“ oder per Befehl eingeschaltet. Dabei ändert macOS die Startkonfiguration des Dienstes und legt eine Einstellungsdatei an; ist der Zugriff für VNC-Programme mit Passwort erlaubt, zusätzlich eine Datei mit diesem Passwort. Der Dienst screensharingd protokolliert jeden Anmeldeversuch in den Unified Logs.

Aus digitalforensischer Sicht belegt eine gespeicherte Verbindung, dass aus diesem Benutzerkonto mit der App eine Verbindung zum angegebenen Rechner bestand, zuletzt zum gespeicherten Zeitpunkt; frühere Verbindungen zum selben Rechner sind nicht einzeln erfasst. Ein Übertragungseintrag belegt, dass über die App eine Datei zwischen diesem Mac und dem genannten Rechner kopiert werden sollte, mit Quell- und Zielpfad auf beiden Seiten; einen Zeitstempel hat er nicht. Auf dem freigebenden Mac belegt ein Anmeldeeintrag den Zeitpunkt, den verwendeten Benutzernamen, die IP-Adresse des verbindenden Rechners und ob die Anmeldung erfolgreich war. Die Konfigurationsdateien belegen, dass die Freigabe eingerichtet wurde, nicht aber eine Verbindung.

| Eintragstyp | Belegt | Relevante Felder |
| --- | --- | --- |
| `com.apple.ScreenSharing.plist`, `connectionsStore` (verbindender Mac) | Verbindung aus diesem Benutzerkonto zum genannten Rechner, zuletzt zum gespeicherten Zeitpunkt | `address`, `username`, `displayName`, `lastConnectedDate` |
| `com.apple.ScreenSharing.plist`, `FileTransferHistory` (verbindender Mac) | Dateiübertragung zwischen diesem Mac und dem genannten Rechner | `remoteComputerName`, `sourcePath`, `destinationPath`, `bytesCopied`, `bytesToCopy` |
| Unified Logs, Prozess `Screen Sharing` (verbindender Mac) | Ausgehende Sitzung zum Zeitpunkt des Eintrags | |
| Unified Logs, Prozess `screensharingd`, Meldung `Authentication:` (freigebender Mac) | Anmeldeversuch mit Benutzername, IP-Adresse des verbindenden Rechners und Ergebnis | `User Name`, `Viewer Address`, `SUCCEEDED` / `FAILED` |
| `disabled.plist`, Schlüssel `com.apple.screensharing` (freigebender Mac) | Freigabe ist ein- oder ausgeschaltet | |
| `com.apple.RemoteManagement.plist` (freigebender Mac) | Bildschirmfreigabe oder Entfernte Verwaltung wurde eingerichtet | |
| `com.apple.VNCSettings.txt` (freigebender Mac) | Zugriff für VNC-Programme mit Passwort wurde erlaubt | |

## Spezifische Kurzinformation

1. Dateiübertragungen bisher nur unter macOS 27 untersucht
2. Die Freigabe ist standardmäßig ausgeschaltet; gespeicherte Verbindungen kann der Benutzer in der App bearbeiten und löschen
3. Die Einträge in den Unified Logs werden nach Größe und Alter rotiert und können auf einem viel genutzten Mac schon nach kurzer Zeit überschrieben sein
4. `com.apple.ScreenSharing.plist` ist eine Binary Plist; `connectionsStore` ist darin eine eingebettete Binary Plist, die separat dekodiert werden muss, `FileTransferHistory` ein Array in der äußeren Plist
5. `lastConnectedDate` in UTC, nur die letzte Verbindung je Rechner; Übertragungseinträge ohne Zeitstempel
6. Die Zahlenwerte für Richtung (`direction`) und Status (`state`) der Übertragungen sind nicht dokumentiert; welcher Pfad auf welchem Rechner liegt, ergibt sich nur aus den Pfaden selbst
7. `com.apple.VNCSettings.txt` enthält das VNC-Passwort, nur mit einem festen Schlüssel verschleiert
8. `com.apple.RemoteManagement.plist` und die Einträge von `screensharingd` entstehen auch bei Verbindungen über Apple Remote Desktop
9. Ablageort:  
   Verbindender Mac: **`/Users/{USER}/Library/Containers/com.apple.ScreenSharing/Data/Library/Preferences/com.apple.ScreenSharing.plist`**  
   Freigebender Mac: **`/private/var/db/com.apple.xpc.launchd/disabled.plist`**  
   Freigebender Mac: **`/Library/Preferences/com.apple.RemoteManagement.plist`**  
   Freigebender Mac: **`/Library/Preferences/com.apple.VNCSettings.txt`**  
   Beide: **`/private/var/db/diagnostics/`** (Unified Logs)

## Referenzen

2026-11: <https://doi.org/10.5281/zenodo.23876165>

2025-04: <https://www.cyberengage.org/post/macos-system-artifacts-macos-finder-gui-configurations-time-changes-bluetooth-printing-and-sha>

2020-04: <http://www.mac4n6.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins>

## Tools

### Kern-Tools

mac_apt (Plugin: SCREENSHARING) - <https://github.com/ydkhatri/mac_apt>

TRACE - <https://github.com/Gadzhovski/TRACE-Forensic-Toolkit>

### Weitere Tools

macOS Screen Sharing FileTransferHistory Parser - <https://github.com/Forensic-IT/macos-screensharing-filetransferhistory>
