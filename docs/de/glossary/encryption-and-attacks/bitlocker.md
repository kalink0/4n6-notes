---
title: "BitLocker"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
---

# BitLocker

BitLocker ist eine von Microsoft entwickelte Festplattenverschlüsselungstechnologie, die in bestimmten Windows-Versionen integriert ist. Sie schützt Daten, indem sie ganze Laufwerke – wie das Betriebssystemlaufwerk oder externe Speichermedien – mittels fortschrittlicher Verschlüsselungsalgorithmen verschlüsselt.

Aus digitalforensischer Sicht kann gesagt werden, dass bei einem ausreichend komplexen Passwort keine bekannten Möglichkeiten bestehen, Zugriff auf die Daten innerhalb eines geschlossenen BitLocker-Volumes ohne das Passwort oder den Recovery Key zu erlangen.

Passwortangriffe, welche versuchen mittels Ausprobieren von Passwörtern Zugriff auf die Daten im BitLocker-Volume zu erlangen, können je nach Komplexität des Passworts mehrere Jahrzehnte bis zum Erfolg benötigen. Sollte BitLocker in Kooperation mit einem Trusted Platform Module (TPM) eingesetzt werden, sind Passwortangriffe deutlich schwieriger bis gar nicht umsetzbar.