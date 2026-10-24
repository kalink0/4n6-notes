---
title: "Samsung Package Prediction"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [program-execution, installed-software]
---

# Samsung Package Prediction

## Bedeutung

Die Samsung Package Prediction ist ein System Service, der überwacht, wann ein Nutzer eine App öffnet und welche drei Apps er zuvor geöffnet hat. Ebenfalls werden Daten zur aktuellen Bildschirmlage, Bluetooth- und W-LAN-Verbindungsstatus und welcher User die App ausführt gespeichert. Bis zu einem gewissen Grad wird auch gespeichert, welche Funktion in der jeweiligen App bedient/aufgerufen wurde - z.B. Kontaktliste oder Nachrichtenliste.

Ziel ist es, dem Gerätenutzer ein angenehmeres Bediengefühl zu geben, um auf Grundlage dieser Daten vorherzusagen, was der Nutzer als Nächstes aufrufen möchte, ihm dies ggf. anzubieten und den Aufruf zu beschleunigen.

Aus digitalforensischer Sicht bedeuten die Einträge, dass die App in der Spalte “running_pkg” zum angegebenen Zeitpunkt vom angegebenen Nutzer auf dem Gerät ausgeführt wurde. Somit muss diese App zu diesem Zeitpunkt auf dem Gerät installiert gewesen sein.

## Spezifische Kurzinformation

1. Die Daten gehen zeitlich weit nach hinten - derzeitige Datenlage → 6 Monate - noch nicht abschließend validiert.
2. Zeitstempel: Unix-Zeit in Millisekunden (UTC)
3. Ablageort:  
   **`/data/system/PkgPredictions.db`**

## Referenzen

2025-11: <https://blog.digital-forensics.it/2025/11/beyond-known-call-to-forensic-research.html>

2023-12: <https://blog.digital-forensics.it/2023/12/has-user-ever-used-xyz-application-aka.html>

## Tools

ALEAPP (Parser: pkgPredictions) - <https://github.com/abrignoni/ALEAPP>