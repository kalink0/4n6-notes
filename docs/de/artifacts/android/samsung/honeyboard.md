---
title: "Samsung Honeyboard"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [commands-input]
---

# Samsung Honeyboard

## Bedeutung

Honeyboard (com.samsung.android.honeyboard) ist die Samsung-Tastatur, die Standardtastatur auf Samsung-Geräten. Sie führt eine Zwischenablage-Historie, damit der Benutzer früher kopierte Texte und Bilder erneut einfügen kann. Außerdem speichert sie Wörter, die der Benutzer aus den Wortvorschlägen entfernt hat.

Aus digitalforensischer Sicht belegt ein Eintrag in der Zwischenablage-Historie, dass der Inhalt zum angegebenen Zeitpunkt aus der genannten App heraus in die Zwischenablage kopiert wurde. Nicht belegt ist, dass oder wo der Inhalt eingefügt wurde.

## Spezifische Kurzinformation

1. Kopierte Texte liegen etwa 30 Tage vor
2. Kopierte Bilder liegen nicht in der Datenbank, sondern als Datei **`clip`** in einem Unterordner von **`clipboard`**, dessen Name ein Unix-Zeitstempel in Millisekunden ist
3. Ältere Versionen speichern statt des Paketnamens die UID der App, die über **`packages.xml`** aufgelöst werden muss
4. Zeitstempel: Unix-Zeit in Millisekunden (UTC)
5. Ablageort:  
   **`[…]/com.samsung.android.honeyboard/`**  
   Zwischenablage (Text): **`databases/ClipItem.db`**  
   Zwischenablage (Bilder): **`clipboard/{TIMESTAMP}/clip`**  
   Entfernte Wortvorschläge: **`databases/RemoveListManager`**

## Referenzen

2024-05: <https://forensafe.com/blogs/SamsungClipboard.html>

## Tools

ALEAPP (Parser: Samsung Honeyboard - Clipboard, Samsung Honeyboard - Clipboard Image Clips) - <https://github.com/abrignoni/ALEAPP>

SELECT-Queries - <https://github.com/kalink0/useful_scripts/blob/master/sql/Android/Samsung%20Apps/sHoneyboard.sql>