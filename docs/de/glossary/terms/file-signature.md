---
title: "Dateisignatur (Magic Bytes)"
status: complete
completed: 2026-10-31
authors: [kalink0 (Marco Neumann)]
---

# Dateisignatur (Magic Bytes)

Eine Dateisignatur (Magic Bytes) ist eine feste Bytefolge, meist am Anfang einer Datei, an der sich das Dateiformat erkennen lässt.

Beispiele sind `FF D8 FF` für JPEG, `89 50 4E 47` (`‰PNG`) für PNG, `25 50 44 46` (`%PDF`) für PDF und `50 4B 03 04` (`PK`) für ZIP. Manche Formate haben zusätzlich eine Endsignatur, z. B. `FF D9` am Ende einer JPEG-Datei. Formate, die auf ZIP aufbauen (z. B. DOCX, XLSX, APK), haben dieselbe Signatur wie ZIP und lassen sich erst am Inhalt unterscheiden. Nicht jedes Format hat eine Signatur, z. B. reiner Text.

Aus digitalforensischer Sicht lässt sich anhand der Signatur der tatsächliche Dateityp unabhängig vom Dateinamen und der Dateiendung bestimmen, z. B. bei umbenannten Dateien. Beim Carving dienen Anfangs- und Endsignaturen dazu, Dateien in nicht zugeordnetem Speicher zu finden.
