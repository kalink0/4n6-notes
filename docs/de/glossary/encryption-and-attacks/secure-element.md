---
title: "Secure Element"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Secure Element

Ein Secure Element (SE) ist ein eigenständiger, gegen Manipulation geschützter Chip mit eigenem Prozessor und Speicher, der Schlüssel speichert und kryptografische Operationen getrennt vom Hauptprozessor ausführt.

Bekannte Beispiele sind SIM-Karten, Chips in Bank- oder Ausweiskarten und Chips für kontaktloses Bezahlen in Smartphones. Seit Android 9 können Schlüssel des Android Keystore in einem Secure Element abgelegt werden (StrongBox), z. B. im Titan M bzw. Titan M2 der Google-Pixel-Geräte oder im Secure Element aktueller Samsung-Galaxy-Geräte. Dort kann auch die Prüfung der Bildschirmsperre samt Fehlversuchszähler stattfinden (Weaver). Apple setzt für Apple Pay ebenfalls ein Secure Element ein; es ist nicht mit der Secure Enclave zu verwechseln, die teilweise ebenfalls mit SE abgekürzt wird.

Aus digitalforensischer Sicht schützt ein Fehlversuchszähler im Secure Element auch dann, wenn das Betriebssystem oder der abgeschottete Bereich im Hauptprozessor (Trusted Execution Environment, TEE) durch eine Schwachstelle kompromittiert sind. Ein Angriff auf die Bildschirmsperre ist dann nur mit den vom Secure Element vorgegebenen Wartezeiten möglich, sofern nicht eine Schwachstelle im Secure Element selbst ausgenutzt werden kann. Die Schlüssel sind an das Gerät gebunden, eine Entschlüsselung außerhalb des Geräts ist nicht möglich.
