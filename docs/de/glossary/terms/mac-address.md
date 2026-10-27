---
title: "MAC-Adresse"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# MAC-Adresse

Die MAC-Adresse (Media Access Control) ist die Hardware-Adresse einer Netzwerkschnittstelle, über die Geräte innerhalb eines lokalen Netzwerks adressiert werden.

Sie ist 48 Bit lang und wird meist als sechs hexadezimale Bytes geschrieben (z. B. 00:1A:2B:3C:4D:5E). Die ersten drei Bytes (OUI, Organizationally Unique Identifier) kennzeichnen den Hersteller der Netzwerkschnittstelle. Die MAC-Adresse wird nur im lokalen Netzwerk übertragen und nicht über Router hinweg ins Internet weitergegeben.

Aus digitalforensischer Sicht kann eine MAC-Adresse, z. B. aus den Protokollen eines Routers, einem Gerät zugeordnet werden. Über die OUI lässt sich zudem potenziell der Hersteller der Netzwerkschnittstelle bzw. des Geräts ermitteln. Die MAC-Adresse lässt sich jedoch per Software ändern. iOS und Android verwenden zudem standardmäßig pro WLAN zufällig erzeugte MAC-Adressen, sodass die in einem Netzwerk gesehene Adresse nicht der Hardware-Adresse des Geräts entsprechen muss.
