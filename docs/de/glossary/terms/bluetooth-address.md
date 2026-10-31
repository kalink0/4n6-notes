---
title: "Bluetooth-Adresse (BD_ADDR)"
status: complete
completed: 2026-10-31
authors: [kalink0 (Marco Neumann)]
---

# Bluetooth-Adresse (BD_ADDR)

Die Bluetooth-Adresse (BD_ADDR, Bluetooth Device Address) ist die 48 Bit lange Hardware-Adresse einer Bluetooth-Schnittstelle.

Sie wird wie eine MAC-Adresse als sechs hexadezimale Bytes geschrieben (z. B. 00:1A:2B:3C:4D:5E); bei einer festen (öffentlichen) Adresse kennzeichnen die ersten drei Bytes den Hersteller (OUI). Klassisches Bluetooth verwendet diese feste Adresse. Bei Bluetooth Low Energy (BLE) verwenden Geräte häufig zufällige Adressen, die regelmäßig wechseln; gekoppelte Geräte können sie über einen beim Koppeln ausgetauschten Schlüssel weiterhin zuordnen.

Aus digitalforensischer Sicht speichern Geräte gekoppelte Bluetooth-Geräte mit deren Adresse, z. B. Kopfhörer oder Fahrzeuge. Haben zwei Geräte jeweils die Adresse des anderen gespeichert, belegt das, dass sie miteinander gekoppelt waren.
