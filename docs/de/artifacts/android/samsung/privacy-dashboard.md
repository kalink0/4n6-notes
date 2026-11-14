---
title: "Samsung Privacy Dashboard"
status: complete
completed: 2026-11-14
authors: [kalink0 (Marco Neumann)]
topics: [program-execution]
---

# Samsung Privacy Dashboard

## Bedeutung

Das Samsung Privacy Dashboard (App `com.samsung.android.privacydashboard`) zeigt dem Nutzer in den Einstellungen unter „Datenschutz“, welche Apps zuletzt auf Berechtigungen wie Standort, Kamera, Mikrofon oder Fotos zugegriffen haben. Dafür führt die App eine eigene Datenbank, in der sie jeden Zugriff einer App auf eine geschützte Funktion mit dem Zeitpunkt festhält: die Berechtigungsgruppe, die genaue Android-Operation (AppOps), ob der Zugriff im Hintergrund erfolgte und ob er über eine andere App (Proxy) lief. Die Datenbank gibt es nur auf Samsung-Geräten. Sie kann Zugriffe enthalten, die im Verlauf der Berechtigungsnutzung von Android selbst (AppOps) fehlen.

Aus digitalforensischer Sicht belegt ein Eintrag, dass die genannte App zum angegebenen Zeitpunkt die genannte Funktion genutzt hat, z. B. den genauen Standort abgefragt oder auf die gespeicherten Bilder zugegriffen hat. Die App war zu diesem Zeitpunkt also aktiv, im Vordergrund oder im Hintergrund. Über die UID lässt sich zudem erkennen, in welchem Android-Benutzer bzw. Profil die App lief, z. B. im Secure Folder.

## Spezifische Kurzinformation

1. Verfügbarkeit: Samsung-Geräte mit Samsung Privacy Dashboard, vorhanden ab OneUI 4.0
2. Aufbewahrung: bis zu 14 Tage
3. Format und Struktur: SQLite-Datenbank ohne Dateiendung; die genaue Operation ist als AppOps-Operationscode gespeichert (z. B. 0 = ungefährer Standort, 1 = genauer Standort, 26 = Kamera, 27 = Mikrofon, 85 = Zugriff auf Bilder, 123 = Zugriff nur auf vom Nutzer ausgewählte Fotos/Videos); Zugriff im Hintergrund als 1, im Vordergrund als 0
4. Zeitstempel: Unix-Zeit in Millisekunden (UTC), Zeitpunkt des Zugriffs
5. Besonderheiten und Fallstricke: Die UID setzt sich aus Benutzer-ID × 100000 + App-ID zusammen; ältere One-UI-Versionen speichern keine UID
6. Ablageort:  
   **`/data/data/com.samsung.android.privacydashboard/databases/permission_db`**

## Referenzen

2025-11: <https://blog.digital-forensics.it/2025/11/beyond-known-call-to-forensic-research.html>

2023-08: <https://insights.samsung.com/2022/09/06/what-is-privacy-dashboard-and-how-does-it-protect-my-data>

## Tools

ALEAPP (Parser: Samsung Privacy Dashboard Permission Access) - <https://github.com/abrignoni/ALEAPP>
