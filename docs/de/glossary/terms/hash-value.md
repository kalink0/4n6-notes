---
title: "Hash-Wert"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Hash-Wert

Ein Hash-Wert ist eine Zeichenfolge fester Länge, die mit einem festgelegten Rechenverfahren (Hash-Funktion) aus beliebigen Daten berechnet wird und diese Daten wie ein Fingerabdruck kennzeichnet.

Gleiche Daten ergeben immer denselben Hash-Wert, schon die Änderung eines einzelnen Bits führt zu einem völlig anderen. Aus dem Hash-Wert lassen sich die ursprünglichen Daten nicht zurückrechnen. In der Forensik verbreitete Hash-Funktionen sind MD5, SHA-1 und SHA-256.
Aus digitalforensischer Sicht dienen Hash-Werte zwei Zwecken. Zum einen belegen sie die Unverändertheit einer Sicherung: Der Hash-Wert wird bei der Sicherung berechnet und dokumentiert; stimmt er bei einer späteren Prüfung überein, wurden die Daten nicht verändert. Bei Sicherungen, die sich nicht identisch wiederholen lassen, z. B. von laufenden Systemen oder Mobilgeräten, belegt er nur die Unverändertheit der Sicherungsdatei, nicht deren Übereinstimmung mit dem Original. Zum anderen lassen sich Dateien über ihren Hash-Wert identifizieren und mit Listen bekannter Dateien abgleichen, z. B. um bekannte Systemdateien auszublenden oder bekannte strafbare Inhalte zu erkennen (Whitelist/Blacklist). Ein abweichender Hash-Wert zeigt nur, dass sich Daten unterscheiden, nicht wie stark.