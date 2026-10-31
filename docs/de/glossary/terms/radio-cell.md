---
title: "Funkzelle"
status: complete
completed: 2026-10-31
authors: [kalink0 (Marco Neumann)]
---

# Funkzelle

Eine Funkzelle ist der Bereich, den eine Antenne einer Mobilfunk-Basisstation versorgt.

Eine Basisstation hat meist mehrere Antennen, die jeweils einen Sektor abdecken (häufig drei Sektoren zu je 120°); jeder Sektor ist eine eigene Funkzelle. Die Größe einer Zelle reicht von wenigen hundert Metern in Städten bis zu mehreren Kilometern auf dem Land. Ein eingeschaltetes Mobilgerät ist immer bei einer Zelle angemeldet (versorgende Zelle). Welche das ist, hängt von Signalstärke und Auslastung ab; es muss nicht die nächstgelegene sein.

Jede Funkzelle hat eine weltweit eindeutige Kennung (CGI, Cell Global Identity; bei LTE ECGI, bei 5G NCGI):

- **MCC (Mobile Country Code, 3 Ziffern):** Land (z. B. 262 = Deutschland)
- **MNC (Mobile Network Code, 2–3 Ziffern):** Mobilfunknetz (z. B. 01 = Telekom)
- **LAC bzw. TAC (Location Area Code bei 2G/3G, Tracking Area Code bei 4G/5G):** Gebiet aus mehreren Funkzellen
- **Cell-ID:** Funkzelle innerhalb des Netzes; die Länge hängt vom Mobilfunkstandard ab (bei LTE 28 Bit aus Kennung der Basisstation und der Zelle)

Aus digitalforensischer Sicht belegt ein Eintrag mit einer Zellkennung, dass das Gerät mit dieser Zelle verbunden war. Der Standort des Geräts lässt sich damit nur auf das Versorgungsgebiet der Zelle eingrenzen.
