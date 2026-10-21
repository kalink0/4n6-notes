---
title: "Windows Hello"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [accounts]
---

# Windows Hello

## Bedeutung

Windows Hello ist die biometrie- bzw. PIN-basierte Anmeldemethode von Windows (seit Windows 10) als Alternative zum klassischen Passwort – unterstützt werden u.a. Gesichtserkennung, Fingerabdruck und PIN.

Aus digitalforensischer Sicht kann anhand vorhandener Windows-Hello-Daten gesagt werden, welche Anmeldemethode(n) für ein Nutzerkonto eingerichtet sind, sowie – über zugehörige Anmeldeereignisse – wann eine erfolgreiche oder fehlgeschlagene Anmeldung/Entsperrung stattgefunden hat. Eine Anmeldung über Windows Hello mit biometrischen Merkmalen kann im Regelfall zur Zuordnung einer Person an eine Anmeldung/einen Anmeldeversuch genutzt.

## Spezifische Kurzinformation

1. Eingeführt mit Windows 10 (2015)
2. Biometrische Templates liegen pro Sensor/Methode als eigene, verschlüsselte `.DAT`-Datei vor – nicht reversibel zum Originalbild
3. Bei Sensoren mit "Enhanced Sign-in Security" (ESS) erfolgt der Abgleich direkt auf dem Sensor-Modul – dann liegen ggf. keine auswertbaren Templates im System
4. Log-Kanal: `Microsoft-Windows-Biometrics/Operational` – u.a. Event-ID 1004/1005 (Erkennung erfolgreich/fehlgeschlagen, mit Nutzer und Sensor), 1019 (genutzter Sensor) und 1605 (Autorisierung bestätigt, ohne Methode); fehlgeschlagene Gesichtserkennung ggf. nicht protokolliert; Security-Log ohne Hinweis auf Windows Hello
5. Zu unterscheiden von **Windows Hello for Business** (Domänen-/Unternehmensumgebung): dort schlüsselbasiert statt Template-basiert, Schlüssel TPM-gebunden, ggf. mit Active Directory/Entra ID synchronisiert (`msDS-KeyCredentialLink`) – eigenständige forensische Fragestellung im Domänenkontext
6. Ablageort:  
   **`C:\Windows\System32\WinBioDatabase\`** (systemweit, nicht pro Nutzerprofil – ein `.DAT` pro Sensor/Methode)  
   **`C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc\`** (Schlüssel für PIN/Windows Hello)

## Referenzen

2026-03: <https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/how-it-works>

2026-02: <https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/windows-hello-enhanced-sign-in-security>

2025-07: <https://insinuator.net/2025/07/windows-hello-for-business-the-face-swap/>

2025-02: <https://www.hecfblog.com/2025/02/daily-blog-745-solving-windows-hello.html>

2024-08: <https://media.defcon.org/DEF%20CON%2032/DEF%20CON%2032%20presentations/DEF%20CON%2032%20-%20Ceri%20Coburn%20Dirk-jan%20Mollema%20-%20Abusing%20Windows%20Hello%20Without%20a%20Severed%20Hand.pdf>

2018-11: <https://learn.microsoft.com/en-us/archive/msdn-technet-forums/7f2c39db-c4ea-48f5-a399-2df17f1edaad>

## Tools

EvtxECmd (Eric Zimmerman) - <https://github.com/EricZimmerman/evtx>

Chainsaw - <https://github.com/WithSecureLabs/chainsaw>

Hayabusa - <https://github.com/Yamato-Security/hayabusa>