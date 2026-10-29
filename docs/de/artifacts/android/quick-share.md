---
title: "Quick Share"
status: draft
authors: [kalink0 (Marco Neumann)]
topics: [data-transfer]
---

# Quick Share

## Bedeutung

Quick Share ist die Funktion zur Übertragung von Dateien an Geräte in der Nähe über Bluetooth und WLAN. Auf Android-Geräten ist sie Teil der Google Play-Dienste; bis 2024 hieß sie Nearby Share. Die Play-Dienste speichern dazu die Einstellungen, eine Liste möglicher Empfänger aus den Kontakten und die Kontaktbilder der Geräte, die beim Teilen zur Auswahl angezeigt wurden.

Aus digitalforensischer Sicht belegen die Dateien, dass Quick Share mit dem genannten Konto und Gerätenamen eingerichtet war und wann es zuletzt genutzt wurde. Welche Dateien an wen gesendet wurden, ist auf dem sendenden Gerät nicht ersichtlich.

## Spezifische Kurzinformation

1. Android-Geräte mit Google Play-Diensten; untersucht unter Android 14 (Stand 2024-07)
2. Format: XML und Protobuf
3. Zeitstempel: Unix-Zeit in Millisekunden (UTC); der Zeitstempel in der Empfängerliste entspricht der letzten Nutzung
4. Ein Kontaktbild im Cache zeigt nur, dass das Gerät dieses Kontakts als Ziel angezeigt wurde, nicht, dass an ihn gesendet wurde
5. Ablageort:  
   **`/data/data/com.google.android.gms/shared_prefs/nearbysharing:service:state.xml`**  
   **`/data/data/com.google.android.gms/files/nearby/sharing/`**  
   **`/data/data/com.google.android.gms/cache/nearby/share/images/`**

## Referenzen

2020-08: <https://thebinaryhick.blog/2020/08/22/nearby-share-airdrop-for-android-return-of-the-unsolicited-richard-photograph/>

## Tools

*Noch kein Inhalt.*
