---
title: "UAL - User Access Logging"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [accounts, network]
---

# UAL - User Access Logging

## Bedeutung

Der UAL - User Access Logging Service protokolliert Zugriffe auf Services des lokalen Servers. Der Server kann von Administratoren dazu genutzt werden, zu ermitteln, wieviele Nutzer einen Service nutzen. Somit ist es für Administratoren möglich zu erkennen, ob ausreichend Lizenzen vorliegen für die Nutzung eines Services.

Aus digtalforensischer Sicht bedeuten Einträge, dass der Nutzeraccount von der geloggten IP-Adresse aus den entsprechenden Service aufgerufen hat. Es wird hierbei die Anzahl der Zugriffe pro Tag aufgelistet, wobei der erste Zugriff des Jahres und der letzte Zugriff des Jahres zusätzlich inklusive der Uhrzeit angezeigt werden.

## Spezifische Kurzinformation

1. Standardmäßig aktiviert unter Windows Server Versionen, ab Windows Server 2012
2. Logins der letzten 2-3 Jahre vorhanden
3. Zeitstempel in UTC
4. Ablageort: **`C:\Windows\System32\LogFiles\Sum`**  
   Current.mdb: aktives Jahr  
   {GUID}.mdb: Kopie von Current.mdb (alle 24 Stunden aktualisiert) sowie je eine Datei für die beiden Vorjahre  
   SystemIdentity.mdb: Serverrollen und Zuordnung RoleGuid zu Rollenname

## Referenzen

2026-02: <https://learn.microsoft.com/en-us/windows-server/security/windows-services/security-guidelines-for-disabling-system-services-in-windows-server#user-access-logging-service>

2024-05: <https://www.thedfirspot.com/post/sum-ual-investigating-server-access-with-user-access-logging>

2021-06: <https://www.crowdstrike.com/en-us/blog/user-access-logging-ual-overview>

2021-02: <https://svch0st.medium.com/windows-user-access-logs-ual-9580f1100635>

## Tools

SumECmd - <https://ericzimmerman.github.io/>

KStrike - <https://github.com/brimorlabs/KStrike>

DLEAPP (Parser: User Access Logging) - <https://github.com/abrignoni/DLEAPP>

Dissect (Plugin: ual) - <https://docs.dissect.tools/en/stable/plugins/ual.html>