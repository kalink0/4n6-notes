---
title: "Android Keystore"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Android Keystore

Der Android Keystore ist der Systemdienst von Android, in dem Apps und Betriebssystem kryptografische Schlüssel so ablegen, dass sie verwendet, aber nicht ausgelesen werden können.

Im Unterschied zur Keychain von Apple speichert der Keystore nur Schlüssel, keine Passwörter oder sonstigen Zugangsdaten. Apps legen diese selbst ab und verschlüsseln sie häufig mit einem Keystore-Schlüssel. Bei einem hardwaregestützten Keystore werden die Schlüssel in einem vom Betriebssystem abgeschotteten Bereich des Prozessors (Trusted Execution Environment, TEE) oder in einem eigenen Sicherheitschip (Secure Element) verwaltet und verlassen diesen nicht; im Dateisystem liegen nur damit verschlüsselte Schlüsselblobs (seit Android 12 in `/data/misc/keystore/persistent.sqlite`). Ein Schlüssel kann zusätzlich daran gebunden werden, dass das Gerät entsperrt ist oder sich der Benutzer kurz zuvor authentifiziert hat.

Aus digitalforensischer Sicht lassen sich Daten, die eine App mit einem hardwaregestützten Keystore-Schlüssel verschlüsselt hat, auch mit Root-Rechten und vollständiger Dateisystemsicherung nicht direkt entschlüsseln, da der Schlüssel das Gerät nicht verlässt. Eine Entschlüsselung ist nur auf dem Gerät über den Keystore möglich, z. B. über die App selbst oder durch Instrumentierung der App zur Laufzeit. Bei älteren Geräten ohne hardwaregestützten Keystore sind die Schlüssel dagegen nur in Software geschützt und können mit Root-Rechten unter Umständen ausgelesen werden.
