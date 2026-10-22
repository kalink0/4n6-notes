---
title: "MRU - Remote Desktop Connection"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [network]
---

# MRU - Remote Desktop Connection

## Bedeutung

Das Betriebssystem Windows legt mehrere sogenannte MRU (Most Recently Used) Listen ab. Diese speichern pro Benutzerkonto im Allgemeinen zuletzt aufgerufene oder gespeicherte Dateien, zuletzt ausgeführte Befehle, zuletzt aufgerufene Ordner.

Der Zweck der MRU Listen ist es, den Benutzern ein angenehmeres Bediengefühl zu liefern, indem zum Beispiel dem Nutzer seine zuletzt geöffneten Dateien angeboten werden.

Die Liste wird vom Windows-Client Remotedesktopverbindung (mstsc.exe) geschrieben.

Aus digitalforensischer Sicht bedeuten Einträge in der MRU-Liste für RDC, dass durch den Benutzeraccount versucht wurde eine Remote-Verbindung zu den aufgeführten Hostnamen/IP-Adressen aufzubauen. Die Reihenfolge in der MRU entspricht hierbei der Reihenfolge der jeweils letzten Verbindungsversuche zu den Hostnamen/IP-Adressen.

## Spezifische Kurzinformation

1. Pro IP/Hostname gibt es nur einen Eintrag in der MRU-Liste
2. Werte MRU0 bis MRU9, MRU0 ist der neueste Eintrag
3. Die letzte Schreibzeit des Schlüssels Default gehört nur zu MRU0
4. Der Unterschlüssel Servers enthält pro Ziel einen eigenen Schlüssel mit UsernameHint (verwendeter Benutzername) und ist nicht auf zehn Einträge begrenzt
5. Mit mstsc /public werden weder MRU noch Servers geschrieben
6. Ablageorte:  
   **`HKCU\Software\Microsoft\Terminal Server Client\Default`**  
   **`HKCU\Software\Microsoft\Terminal Server Client\Servers\{HOST}`**

## Referenzen

2026-02: <https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/remove-entries-from-remote-desktop-connection-computer>

2025-03: <https://devolutions.net/blog/using-rdp-without-leaving-traces-the-mstsc-public-mode/>

## Tools

DLEAPP (windowsRdpClientServers) - <https://github.com/abrignoni/DLEAPP>

RegRipper (tsclient) - <https://github.com/keydet89/RegRipper4.0>

Velociraptor (Windows.Registry.RDP) - <https://docs.velociraptor.app/>