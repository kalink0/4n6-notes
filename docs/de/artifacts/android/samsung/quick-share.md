---
title: "Samsung Quick Share"
status: complete
completed: 2026-10-29
authors: [kalink0 (Marco Neumann)]
topics: [data-transfer]
---

# Samsung Quick Share

## Bedeutung

Quick Share ist eine Funktion zur Übertragung von Fotos, Videos und anderen Dateien an Geräte in der Nähe über WLAN und Bluetooth. Ursprünglich stammt sie von Samsung; seit 2024 heißt auch die Google-Variante in den Play-Diensten (vorher Nearby Share) auf anderen Android-Geräten Quick Share. Auf Galaxy-Geräten protokolliert die Samsung-App Quick Share, welche Dateien gesendet und empfangen wurden und mit welchen Geräten eine Verbindung bestand. Übertragungen per Private Share, bei der der Empfänger die Inhalte nur bis zu einem Ablaufdatum ansehen, aber nicht speichern oder weiterleiten kann, stehen in einer eigenen Datenbank.

Aus digitalforensischer Sicht belegen die Einträge, dass eine bestimmte Datei per Quick Share gesendet bzw. empfangen wurde und dass das Gerät mit einem Gerät des geloggten Namens verbunden war. Abgebrochene und fehlgeschlagene Übertragungen sind ebenfalls erkennbar.

## Spezifische Kurzinformation

1. Samsung-Galaxy-Geräte
2. Voraussetzung für die Übertragung: WLAN und Bluetooth aktiv; die Empfangseinstellung (Niemand, Kontakte, Jeder) legt fest, wer an das Gerät senden kann
3. Private-Share-Inhalte werden beim Empfänger nach Ablauf gelöscht (Standard 2 Tage, höchstens knapp 7 Tage)
4. SQLite-Datenbanken: `linkShare.db` (Quick Share), `privacy_library_database.db` (Private Share)
5. Seit One UI 8.5 auch mit AirDrop kompatibel (zunächst Galaxy S26, Stand 2026-03)
6. Ablageort:  
   **`/data/data/com.samsung.android.app.sharelive/databases/linkShare.db`**  
   **`/data/data/com.samsung.android.app.sharelive/databases/privacy_library_database.db`**

## Referenzen

2026-10: <https://www.gmdsoft.com/blog/gmdsoft-tech-letter-vol-22-quick-share-history-analysis-amid-expanding-device-and-os-support/>

## Tools

*Noch kein Inhalt.*
