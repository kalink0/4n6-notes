---
title: "recently-used.xbel"
status: complete
completed: 2026-11-22
authors: [kalink0 (Marco Neumann)]
topics: [file-access]
---

# recently-used.xbel

## Bedeutung

recently-used.xbel ist die Liste der zuletzt verwendeten Dateien eines Benutzers auf dem Linux-Desktop. Programme, die auf GTK aufbauen (z. B. Nautilus, Dokumentenbetrachter, LibreOffice, GIMP, Thunderbird), tragen eine Datei ein, wenn sie über das Programm geöffnet, gespeichert oder im Dateidialog ausgewählt wird; KDE-Programme schreiben über KDE Frameworks in dieselbe Datei. Das Format folgt der freedesktop.org-Spezifikation „Desktop Bookmarks“. Dateidialoge und Dateimanager zeigen daraus die Ansicht „Zuletzt verwendet“. Ein Eintrag enthält die Adresse der Datei, ihren Dateityp, Zeitpunkte und die Programme, die die Datei eingetragen haben, jeweils mit Anzahl und Zeitpunkt ihrer letzten Meldung.

Aus digitalforensischer Sicht belegt ein Eintrag, dass ein Programm die Datei unter dieser Adresse im Benutzerkonto als verwendet gemeldet hat, wann das zum ersten Mal geschah und wann jedes der genannten Programme die Datei zuletzt gemeldet hat. Die Liste kann auch Dateien und Programme enthalten, die es auf dem System nicht mehr gibt.

## Spezifische Kurzinformation

1. Verfügbarkeit: alle Linux-Desktops mit GTK-Programmen (seit GTK 2.10); KDE-Programme schreiben seit KDE Frameworks 5.93 ebenfalls hinein
2. Voraussetzungen: standardmäßig aktiv; abschaltbar unter GNOME in den Einstellungen (Datenschutz, Dateiverlauf), unter KDE mit `UseRecent=false` in der Gruppe `RecentDocuments` von **`~/.config/kdeglobals`**; bei abgeschaltetem Verlauf leert GTK die Datei beim nächsten Schreiben, KDE löscht sie
3. Aufbewahrung: GTK behält höchstens 1000 Einträge (seit GTK 3.22.4 bzw. 2.24.32) und entfernt darüber hinaus die zuerst aufgenommenen, unabhängig von ihrer letzten Verwendung; KDE behält standardmäßig höchstens 300 Einträge (`MaxEntries` in derselben Gruppe) und entfernt die mit dem ältesten `modified`; die Grenze des Programms, das gerade schreibt, gilt für alle Einträge, auch die der anderen Programme; GTK entfernt zusätzlich Einträge, deren `modified` älter ist als das eingestellte Höchstalter in Tagen (GNOME-Standard: unbegrenzt; ohne Einstellung der Desktop-Umgebung GTK-Standard 30 Tage); „Verlauf löschen“ in den GNOME-Einstellungen leert die Datei
4. Format und Struktur: XML im Format XBEL 1.0; je Datei ein `bookmark`-Element mit der Adresse (`href`, auch `smb://` und andere Orte außer `file://`), Dateityp (`mime:mime-type`), optional Gruppen (z. B. `Graphics`, `Totem`) und je Programm ein `bookmark:application`-Element mit Name, Startbefehl (`exec`), Zeitpunkt (`modified`) und Anzahl (`count`); Einträge stehen in der Reihenfolge, in der sie aufgenommen wurden
5. Zeitstempel: ISO 8601 in UTC mit Mikrosekunden; `added` = erste Aufnahme in die Liste; `modified` = letzte Meldung durch irgendein Programm; `visited` setzt GTK nur bei der Aufnahme (dann gleich `added`), KDE bei jeder Meldung; `modified` am Programmeintrag = letzte Meldung durch dieses Programm
6. Besonderheiten und Fallstricke: Der Programmname ist der Name, den das Programm selbst angibt (z. B. `org.gnome.Nautilus`, `Document Viewer`, `python`); Dateien, die über den Dateidialog des GNOME-Portals ausgewählt werden (z. B. von Flatpak-Programmen), trägt das Portal unter dem Namen `xdg-desktop-portal-gnome` ein, das eigentliche Programm steht dann nicht in der Liste; Flatpak- und Snap-Programme, die selbst eintragen, schreiben in eine eigene Datei im App-Ordner, Snap-Programme (außer mit Classic-Confinement) je Revision; bei einem Update kopiert snapd die Daten in die neue Revision, die Ordner der behaltenen älteren Revisionen (standardmäßig eine) enthalten den Stand vor dem Update; Nautilus trägt Dateien ein, die darüber geöffnet werden, auch wenn das geöffnete Programm selbst keinen Eintrag schreibt; KDE übernimmt keine versteckten Dateien (Pfad mit `/.`) und keine Dateien im temporären Ordner und entfernt beim Schreiben versteckte Dateien, die GTK eingetragen hat; GTK schreibt die Datei über eine temporäre Datei `recently-used.xbel.XXXXXX` (sechs zufällige Zeichen); bricht das Schreiben ab, bleibt sie mit dem Stand dieses Zeitpunkts liegen; GTK 2 vor 2.24 speicherte die Datei als **`~/.recently-used.xbel`**, GTK 2.24 verschiebt sie beim ersten Zugriff in den neuen Ablageort oder führt sie mit einer dort vorhandenen Datei zusammen
7. Ablageort:  
   **`~/.local/share/recently-used.xbel`**  
   Flatpak-Programme: **`~/.var/app/{APP_ID}/data/recently-used.xbel`**  
   Snap-Programme: **`~/snap/{SNAP_NAME}/{REVISION}/.local/share/recently-used.xbel`**  
   GTK 2 vor 2.24: **`~/.recently-used.xbel`**

## Referenzen

2026-11 (abgerufen): <https://docs.gtk.org/gtk4/class.RecentManager.html>

2026-11 (abgerufen): <https://help.gnome.org/users/gnome-help/stable/privacy-history-recent-off.html.en>

2023-03: <https://doi.org/10.1016/j.fsidi.2022.301498>

2018-05: <https://wiki.freedesktop.org/Specifications/desktop-bookmark-spec/>

## Tools

### Kern-Tools

DLEAPP (Parser: Recently Used Files (GTK)) - <https://github.com/abrignoni/DLEAPP>

Dissect (Plugin: recently_used) - <https://docs.dissect.tools/>

Velociraptor (Exchange-Artefakt: Linux.Forensics.RecentlyUsed) - <https://docs.velociraptor.app/>

TRACE - <https://github.com/Gadzhovski/TRACE-Forensic-Toolkit>

### Weitere Tools

linuxthumbnailforensics (recentlyused.py) - <https://github.com/teescdf/linuxthumbnailforensics>
