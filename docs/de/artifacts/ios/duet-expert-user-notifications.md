---
title: "Duet Expert User Notifications"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [notifications]
---

# Duet Expert User Notifications

## Bedeutung

iOS führt in einer Datenbank im Bereich DuetExpertCenter einen Verlauf der auf dem Gerät eingegangenen Benachrichtigungen. Gespeichert werden Metadaten wie die App, von der die Benachrichtigung stammt, der Empfangszeitpunkt sowie Kennungen der Konversation bzw. des Absenders. Der Text der Benachrichtigung wird nicht gespeichert, nur seine Länge. Wofür Apple die Datenbank verwendet, ist nicht dokumentiert.

Aus digitalforensischer Sicht belegt ein Eintrag, dass zum angegebenen Zeitpunkt eine Benachrichtigung der angegebenen App auf dem Gerät eingegangen ist, je nach App mit einer Kennung der Konversation oder des Absenders, z.B. einer Telefonnummer. Nicht belegt sind dagegen der Inhalt der Benachrichtigung und ob der Nutzer sie gelesen oder darauf reagiert hat.

## Spezifische Kurzinformation

1. Beobachtet von iOS 15 bis iOS 26 (Stand 2026-07)
2. Einträge reichen etwa 60 Tage zurück
3. SQLite-Datenbank, Tabelle `notifications`
4. Zeitstempel im Format Mac Absolute Time (Sekunden seit 2001-01-01, UTC)
5. Wo die Absenderkennung steht, hängt von der App ab, z.B. Telefonnummer bei WhatsApp und Signal meist in `rawIdentifier`, bei SMS in `ThreadID`
6. Ablageort:  
   **`/private/var/mobile/Library/DuetExpertCenter/notificationAndSuggestionDB.db`**

## Referenzen

2026-07: <https://blog.digital-forensics.it/2026/07/after-signal-fix-exploring-apples.html>

## Tools

iLEAPP (duetNotifications) - <https://github.com/abrignoni/iLEAPP>