---
title: "Thumbnail-Cache"
status: complete
completed: 2026-11-22
authors: [kalink0 (Marco Neumann)]
topics: [file-existence]
---

# Thumbnail-Cache

## Bedeutung

Der Thumbnail-Cache ist der gemeinsame Speicher für Vorschaubilder (Thumbnails) eines Benutzers auf dem Linux-Desktop. Dateimanager wie Nautilus, Dolphin oder Thunar und andere Programme, z. B. Bildbetrachter, erzeugen ein Vorschaubild, wenn sie eine Datei mit Vorschau anzeigen, etwa beim Öffnen eines Ordners, und legen es dort ab, damit es beim nächsten Mal nicht neu berechnet werden muss. Aufbau und Ablage folgen der freedesktop.org-Spezifikation „Thumbnail Managing Standard“, sodass GNOME-, KDE- und XFCE-Programme denselben Cache nutzen. Jedes Vorschaubild ist eine PNG-Datei, deren Name sich aus der Adresse der Originaldatei ergibt und die diese Adresse und den Änderungszeitpunkt der Originaldatei enthält.

Aus digitalforensischer Sicht belegt ein Vorschaubild, dass eine Datei mit diesem Inhalt unter der gespeicherten Adresse vorhanden war und dass ein Programm im Benutzerkonto sie mit Vorschau angezeigt hat, z. B. beim Öffnen des Ordners im Dateimanager. Unter GNOME und KDE bleiben Vorschaubilder beim Löschen oder Verschieben der Originaldatei bestehen; sie zeigen dann auch Inhalt, Namen und Pfad von Dateien, die nicht mehr vorhanden sind.

## Spezifische Kurzinformation

1. Verfügbarkeit: alle Linux-Desktops, deren Programme der Spezifikation folgen (GNOME, KDE, XFCE u. a.); die Größen `x-large` und `xx-large` seit Version 0.9.0 der Spezifikation (2020)
2. Voraussetzungen: Vorschauen sind in Nautilus und Dolphin standardmäßig aktiv; Nautilus erstellt standardmäßig keine Vorschaubilder für Dateien auf Netzwerkfreigaben und für Bilder über 50 MB, wohl aber für Dateien auf USB-Datenträgern und per MTP angeschlossenen Smartphones; KDE erstellt standardmäßig keine Vorschaubilder für Dateien an entfernten Orten (`MaximumRemoteSize` = 0) und speichert seit KDE Frameworks 5.57 keine für Dateien auf einem anderen verschlüsselten Datenträger, solange der Cache selbst nicht verschlüsselt liegt; GNOME prüft das nicht, Vorschaubilder von Dateien aus verschlüsselten Containern können daher unverschlüsselt im Cache liegen
3. Aufbewahrung: GNOME löscht Vorschaubilder, die seit 180 Tagen nicht gelesen wurden (seit GNOME 3.36 nach dem Zugriffszeitpunkt, davor nach dem Änderungszeitpunkt der PNG-Datei), und darüber hinaus die ältesten, wenn der Cache größer als 512 MB ist; die Prüfung läuft kurz nach der Anmeldung und dann täglich, `x-large` und `xx-large` werden erst seit GNOME 45 bereinigt; KDE und XFCE bereinigen den Cache nicht nach Alter oder Größe; ob die Originaldatei noch existiert, prüfen weder GNOME noch KDE; Thunar (XFCE) löscht das Vorschaubild, wenn es eine Datei endgültig löscht, beim Verschieben in den Papierkorb bleibt es; ein Vorschaubild wird ersetzt, wenn sich Änderungszeitpunkt oder Größe der Originaldatei ändern
4. Format und Struktur: PNG-Dateien in Ordnern je Größe: `normal` (bis 128 Pixel), `large` (256), `x-large` (512), `xx-large` (1024); Dateiname = MD5-Hash der vollständigen Adresse der Originaldatei (z. B. `file:///home/…/bild.jpg`, Sonderzeichen URL-kodiert) mit Endung `.png`; Textfelder in der PNG-Datei: `Thumb::URI` (Adresse), `Thumb::MTime` (Änderungszeitpunkt der Originaldatei), optional `Thumb::Size`, `Thumb::Mimetype`, `Thumb::Image::Width`/`Height`, `Thumb::Document::Pages`, `Thumb::Movie::Length` und `Software` (erzeugendes Programm, z. B. `GNOME::ThumbnailFactory`, `KDE Thumbnail Generator`); im Ordner `fail` je Programm leere PNG-Dateien mit Adresse und Änderungszeitpunkt für Dateien, für die kein Vorschaubild erstellt werden konnte
5. Zeitstempel: `Thumb::MTime` in Sekunden seit 1970-01-01 (UTC) = Änderungszeitpunkt der Originaldatei bei der Erstellung des Vorschaubilds; der Änderungszeitpunkt der PNG-Datei = Zeitpunkt der Erstellung des Vorschaubilds, da es nicht verändert, sondern immer neu geschrieben wird
6. Besonderheiten und Fallstricke: Ordner und Dateien haben die Rechte 700 bzw. 600; wird eine Datei unter GNOME oder KDE umbenannt oder verschoben, entsteht ein neues Vorschaubild unter dem neuen Namen, das alte bleibt; Thunar verschiebt das Vorschaubild mit; aus einem bekannten Pfad lässt sich der Name des Vorschaubilds berechnen und so prüfen, ob für eine Datei eines existiert; Ordner mit eigenen Vorschaubildern, z. B. auf Datenträgern, enthalten einen Unterordner `.sh_thumbnails`, der nur gelesen wird und Adressen relativ zu diesem Ordner speichert (`./bild.jpg`); vor Version 0.8.0 der Spezifikation (2012) lag der Cache unter **`~/.thumbnails`**
7. Ablageort:  
   **`~/.cache/thumbnails/{normal|large|x-large|xx-large}/{MD5}.png`**  
   Fehlgeschlagene Vorschauen: **`~/.cache/thumbnails/fail/{PROGRAMM}/{MD5}.png`**  
   Älterer Ablageort: **`~/.thumbnails/`**

## Referenzen

2023-03: <https://doi.org/10.1016/j.fsidi.2022.301498>

2020-12: <https://specifications.freedesktop.org/thumbnail/latest/>

## Tools

DLEAPP (Parser: Thumbnail Cache (freedesktop)) - <https://github.com/abrignoni/DLEAPP>
