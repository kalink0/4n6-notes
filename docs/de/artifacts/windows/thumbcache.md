---
title: "Thumbcache"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [file-existence]
---

# Thumbcache

## Bedeutung

Das Betriebssystem Microsoft Windows bringt die Funktion des Thumbnail Caches mit um Benutzern eine bessere Bedienung anbieten zu können, wenn diese z.B. im Windows Explorer navigieren und Dateien suchen oder anschauen möchten. Der Thumbnail Cache verringert die Ladezeiten von Dateien indem Vorschaubilder generiert werden, die schnell geladen werden können, wenn der Benutzer des Systems im Windows Explorer die Dateien anzeigen möchte oder in einem Ordner navigiert. Die Vorschaubilder zeigen den Inhalt oder einen Teil des Inhalts der Originaldatei in reduzierter Größe.

Aus digitalforensischer Sicht kann anhand der Existenz einer Datei im Thumbnail Cache gesagt werden, dass die Originaldatei auf einem aktiv oder ehemals angeschlossenen Datenträger (auch Netzlaufwerk) gespeichert war oder ist.
Anhand des Thumbnail Caches alleine kann nicht genau gesagt werden, was genau ein Nutzer mit der Datei gemacht hat. Zum Beispiel ob der Nutzer die Datei aktiv angeschaut, kopiert oder anderweitig genutzt hat.

## Spezifische Kurzinformation

1. Originalpfad kann unter bestimmen Umständen ermittelt werden (siehe zusätzliche Hinweise)
2. Ablageort: **`%LOCALAPPDATA%\Microsoft\Windows\Explorer\thumbcache_*.db`**

### Zusätzliche Hinweise (Forensik)

#### Pfad zur Originaldatei

Der Originalpfad der Datei ist nicht im Thumbnail Cache gespeichert. Es gibt mehrere Möglichkeiten um die Originaldatei, wenn möglich, zu finden.

1. Berechnung der ThumbnailCacheID aller vorliegenen Dateien und Abgleich mit der ThumbnailCacheIDs im Thumbnail Cache.
2. Prüfen der Windows Search (Windows.edb, ab Windows 11 Windows.db) auf die ThumbnailCacheID aus dem Thumbnail Cache.
3. Prüfen aller vorliegenden Dateien auf visuelle Gleichheit

Für die Vorgehensweisen 1 und 3 muss die Originaldatei im Datenbestand noch vorliegen. Die Berechnung der ThumbnailCacheID (Vorgehensweise 1) muss auf demselben System erfolgen, auf dem der Thumbnail Cache entstanden ist.

Für die ältere Version, die thumbs.db, ergibt sich der Originalpfad der Datei aus dem Ort der thumbs.db selbst. Diese thumbs.db wird im jeweiligen Ordner der Originaldatei erzeugt. Bei Netzwerkordnern wird die thumbs.db auch in aktuellen Windows-Versionen weiterhin erzeugt.

## Referenzen

2026-07: <https://www.it-connect.tech/windows-forensics-part-6-analyzing-image-caches/>

2025-08: <https://www.pentestpartners.com/security-blog/thumbnail-forensics-dfir-techniques-for-analysing-windows-thumbcache/>

2023-09: <https://it-forensik.fiw.hs-wismar.de/index.php/Stefan_Augustin>

2012-01: <http://computerforensics.parsonage.co.uk/downloads/UnderMyThumbs.pdf>

## Tools

Thumbcache Viewer - <https://thumbcacheviewer.github.io/>

Thumb Viewer - <https://thumbsviewer.github.io/>

DLEAPP (Parser: Thumbnail Cache) - <https://github.com/abrignoni/DLEAPP>

Dissect (Plugin: thumbcache) - <https://docs.dissect.tools/en/stable/plugins/thumbcache.html>