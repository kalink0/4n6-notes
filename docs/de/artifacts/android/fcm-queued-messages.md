---
title: "FCM Queued Messages"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [notifications, communication]
---

# FCM Queued Messages

## Bedeutung

Firebase Cloud Messaging (FCM) ist Googles Dienst, über den Apps Nachrichten von ihren Servern auf das Gerät geschickt bekommen, z. B. Benachrichtigungen, Chatnachrichten oder Steuerdaten. So muss nicht jede App eine eigene Verbindung zu ihrem Server offen halten. Die Google Play-Dienste nehmen die Nachrichten entgegen, legen sie in einer Warteschlange ab und reichen sie an die jeweilige App weiter.

Aus digitalforensischer Sicht belegt ein Eintrag, dass die genannte App zum angegebenen Zeitpunkt eine Nachricht von ihrem Server erhalten hat, mit dem Inhalt, den der Server mitgeschickt hat.

Nicht belegt ist, dass der Nutzer die Nachricht gesehen oder geöffnet hat.

## Spezifische Kurzinformation

1. Vorhanden ab Android 10
2. Enthält nur eingehende Nachrichten vom Server an die App
3. Je nach App z. B.:
   - Absender und Empfänger
   - Nachrichtentext
   - Art der Benachrichtigung
   - Standortdaten
   - nur ein Verweis (URL), über den die App den eigentlichen Inhalt abruft
4. Einträge werden gelöscht, sobald die Google Play-Dienste die Nachricht an die App weitergegeben haben
5. Zeitstempel im Schlüssel: Unix-Zeit in Mikrosekunden, Zeitpunkt des Eingangs der Nachricht
6. Ablageort:  
   **`/data/data/com.google.android.gms/files/fcm_queued_messages.ldb/`**

## Referenzen

2024-11: <https://forensafe.com/blogs/AndroidFCM.html>

2020-11: <https://www.cclsolutionsgroup.com/post/fcm-queued-messages-on-android>

## Tools

ALEAPP (Parser: FCM Dump, dazu app-spezifische FCM-Parser) - <https://github.com/abrignoni/ALEAPP>

crush (LevelDB-Viewer) - <https://github.com/kalink0/crush-forensics>