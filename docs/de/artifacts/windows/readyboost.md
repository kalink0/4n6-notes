---
title: "EMDMgmt - ReadyBoost"
status: complete
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
topics: [external-devices]
---

# EMDMgmt - ReadyBoost

## Bedeutung

EMDMgmt (External Memory Device Management) ist der Registry-Schlüssel des ReadyBoost-Dienstes. ReadyBoost nutzt externe Flash-Speicher als zusätzlichen Cache. Beim Anschließen eines Datenträgers testet der Dienst dessen Eignung und speichert das Ergebnis zusammen mit Angaben zum Datenträger, unabhängig davon, ob ReadyBoost tatsächlich genutzt wird.

Aus digitalforensischer Sicht belegt ein Eintrag, dass ein Datenträger mit den angegebenen Geräte- und Volume-Angaben am System angeschlossen war. Nicht belegt ist der Zeitpunkt des Anschließens.

## Spezifische Kurzinformation

1. Seit Windows Vista; unter Windows 11 ist ReadyBoost ausgeblendet, laut Microsoft aber weiterhin vorhanden
2. Wird befüllt, auch wenn ReadyBoost nicht genutzt wird; auf Systemen mit SSD kann der Schlüssel fehlen, weil ReadyBoost dann deaktiviert ist
3. Erfasst neben USB-Datenträgern auch eSATA, FireWire und lokale Nicht-Systemlaufwerke
4. Ein Unterschlüssel je Gerät; der Name enthält Hersteller, Produkt, Geräteseriennummer, Volume-Label (falls vorhanden) und Volume-Seriennummer
5. Die LastWrite-Zeiten der Unterschlüssel entsprechen nicht dem Anschließen des Datenträgers
6. Ablageort:  
   **`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\EMDMgmt`**

## Referenzen

2024-01: <https://artefacts.help/windows_registry_usb_activity.html>

2023-08: <https://learn.microsoft.com/en-us/answers/questions/415341/readyboost-what-data-is-cached>

2022-05: <https://windowsir.blogspot.com/2022/05/usb-devices-redux.html>

2013-08: <https://www.hecfblog.com/2013/08/daily-blog-65-understanding-artifacts.html>

2013-04: <https://windowsir.blogspot.com/2013/04/plugin-emdmgmt.html>

2012-02: <https://windowsir.blogspot.com/2012/02/howto-usb-thumb-drives.html>

## Tools

RegRipper (Plugin: emdmgmt) - <https://github.com/keydet89/RegRipper4.0>

usb-forensic - <https://github.com/SecurityRonin/usb-forensic>