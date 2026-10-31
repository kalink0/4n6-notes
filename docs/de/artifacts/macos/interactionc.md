---
title: "InteractionC"
status: complete
completed: 2026-10-22
authors: [kalink0 (Marco Neumann)]
topics: [communication]
---

# InteractionC

## Bedeutung

InteractionC ist eine Datenbank von CoreDuet, in der macOS Interaktionen des Geräts mit anderen Personen festhält, z.B. Nachrichten, E-Mails und Kalendereinträge. Auf dieser Grundlage schlägt macOS dem Nutzer häufige Gesprächspartner vor, etwa im Teilen-Menü. Gespeichert werden die beteiligte App, die beteiligten Kontakte als Absender bzw. Empfänger, Zeitpunkte und ggf. Anhänge, aber kaum Inhalte wie Nachrichtentexte.

Aus digitalforensischer Sicht belegt ein Eintrag, dass zum angegebenen Zeitpunkt über die angegebene App eine Interaktion mit den verknüpften Kontakten stattfand. Nicht belegt ist dagegen der Inhalt der Interaktion.

## Spezifische Kurzinformation

1. Seit macOS 10.15 vorhanden, unter macOS 15 weiterhin befüllt
2. SQLite-Datenbank; zentrale Tabelle `ZINTERACTIONS`, dazu `ZCONTACTS` (je Kontakt Interaktionszähler sowie erster und letzter Kontakt), `ZATTACHMENT` und `ZKEYWORDS`
3. Zeitstempel im Format Mac Absolute Time (Sekunden seit 2001-01-01, UTC)
4. Ablageort:  
   **`/private/var/db/CoreDuet/People/interactionC.db`**

## Referenzen

2026-10 (abgerufen): <https://developer.apple.com/documentation/foundation/supporting-suggestions-in-your-app-s-share-extension>

2021-09: <https://www.sentinelone.com/labs/macos-incident-response-part-2-user-data-activity-and-behavior/>

2020-06: <https://www.mac4n6.com/blog/2020/6/21/socially-distant-but-still-interacting-new-and-improved-updates-to-macosios-coreduet-interactioncdb-apollo-modules>

## Tools

APOLLO (interaction_contact_interactions, interaction_contact_interactions_keywords) - <https://github.com/mac4n6/APOLLO>

DLEAPP (InteractionC) - <https://github.com/abrignoni/DLEAPP>