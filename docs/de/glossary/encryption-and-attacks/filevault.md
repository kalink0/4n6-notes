---
title: "FileVault"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
---

# FileVault

FileVault ist Apples native Lösung zur Festplattenverschlüsselung in macOS. Es verschlüsselt das gesamte Startvolume – also alle darauf gespeicherten Daten – sodass ohne die Eingabe des korrekten Benutzerpassworts (und damit der Entschlüsselungsschlüssel) kein Zugriff möglich ist. Seit FileVault 2, das mit Mac OS X Lion eingeführt wurde, erfolgt diese Vollverschlüsselung mit modernen Algorithmen, wodurch die Daten selbst bei Verlust oder Diebstahl des Geräts effektiv geschützt sind.

Aus digitalforensischer Sicht kann gesagt werden, dass bei einem ausreichend komplexen Passwort keine bekannten Möglichkeiten bestehen, Zugriff auf die Daten innerhalb eines geschlossenen FileVault-Volumes ohne das Passwort oder den Recovery Key zu erlangen.

Passwortangriffe, welche versuchen mittels Ausprobieren von Passwörtern Zugriff auf die Daten im FileVault-Volume zu erlangen, können je nach Komplexität des Passworts mehrere Jahrzehnte bis zum Erfolg benötigen. Bei Macs mit T2-Chip oder Apple-Chip begrenzt die Secure Enclave die Anzahl der Passworteingaben, wodurch Passwortangriffe deutlich schwieriger bis gar nicht umsetzbar sind.