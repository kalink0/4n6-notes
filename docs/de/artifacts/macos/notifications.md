---
title: "Notifications"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [communication]
---

# Notifications

## Bedeutung

Programme informieren den Benutzer über Mitteilungen, z.B. neue E-Mails, Chatnachrichten oder Erinnerungen. macOS zeigt sie an und speichert die zugestellten Mitteilungen in einer Datenbank, damit der Benutzer sie später in der Mitteilungszentrale nachlesen kann.

Aus digitalforensischer Sicht belegt ein Eintrag, dass das Programm dem Benutzerkonto zum gespeicherten Zeitpunkt eine Mitteilung mit dem gespeicherten Inhalt zugestellt hat. Ein Eintrag belegt nicht, dass der Benutzer die Mitteilung gesehen oder gelesen hat.

## Spezifische Kurzinformation

1. Titel, Untertitel und Text der Mitteilung stehen als binäre plist in der Datenbank
2. Inhalte bleiben auch erhalten, wenn das Programm die Nachricht selbst löscht (z.B. verschwindende Nachrichten)
3. Zeitstempel im Cocoa-Format (Sekunden seit 2001-01-01), UTC
4. Unter **`/private/var/folders`** erfolgt die Zuordnung zum Benutzer über den Besitzer (UID) des Ordners
5. Nach einem Upgrade können ältere Datenbanken neben der aktuellen vorhanden sein
6. Ab macOS 15 durch TCC geschützt; am laufenden System nicht ohne Freigabe lesbar
7. Ablageort:  
   Bis macOS 10.9: **`/Users/{USER}/Library/Application Support/NotificationCenter/{UUID}.db`**  
   macOS 10.10 bis 10.12: **`/private/var/folders/{XX}/{ID}/0/com.apple.notificationcenter/db/db`**  
   macOS 10.13 bis 14: **`/private/var/folders/{XX}/{ID}/0/com.apple.notificationcenter/db2/db`**  
   Ab macOS 15: **`/Users/{USER}/Library/Group Containers/group.com.apple.usernoted/db2/db`**

## Referenzen

2024-09: <https://9to5mac.com/2024/09/01/security-bite-apple-addresses-privacy-concerns-around-notification-center-database-in-macos-sequoia/>

2021-09: <https://www.sentinelone.com/labs/macos-incident-response-part-2-user-data-activity-and-behavior/>

2018-05: <https://objective-see.org/blog/blog_0x2E.html>

## Tools

mac_apt (Plugin: NOTIFICATIONS) - <https://github.com/ydkhatri/mac_apt>

DLEAPP (Parser: Notification Center Records) - <https://github.com/abrignoni/DLEAPP>

Plaso (Parser: mac_notificationcenter) - <https://github.com/log2timeline/plaso>