---
title: "InteractionC"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [communication]
---

# InteractionC

## Bedeutung

InteractionC ist eine Datenbank von CoreDuet, in der iOS Interaktionen des Geräts mit anderen Personen festhält, z.B. Anrufe, Nachrichten, E-Mails und Kalendereinträge. Auf dieser Grundlage schlägt iOS dem Nutzer häufige Gesprächspartner vor, etwa im Teilen-Menü. Gespeichert werden die beteiligte App, die beteiligten Kontakte als Absender bzw. Empfänger, Zeitpunkte und ggf. Anhänge, aber kaum Inhalte wie Nachrichtentexte.

Aus digitalforensischer Sicht belegt ein Eintrag, dass zum angegebenen Zeitpunkt über die angegebene App eine Interaktion mit den verknüpften Kontakten stattfand. Nicht belegt ist dagegen der Inhalt der Interaktion.

## Spezifische Kurzinformation

1. Auch in iTunes-Backups enthalten
2. Reicht teils mehrere Monate zurück (in einem untersuchten Fall etwa sechs Monate)
3. SQLite-Datenbank; zentrale Tabelle `ZINTERACTIONS`, dazu `ZCONTACTS` (je Kontakt Interaktionszähler sowie erster und letzter Kontakt), `ZATTACHMENT` und `ZKEYWORDS`
4. Zeitstempel im Format Mac Absolute Time (Sekunden seit 2001-01-01, UTC)
5. Kontakte sind über GUIDs mit dem Adressbuch abgleichbar
6. Die Empfängeranzahl zählt den Gerätenutzer nicht mit
7. Ein Teil der Anhänge ist keiner Interaktion mehr zugeordnet und hat keinen Zeitstempel
8. Ablageort:  
   **`/private/var/mobile/Library/CoreDuet/People/interactionC.db`**

## Referenzen

2026-10: <https://developer.apple.com/documentation/foundation/supporting-suggestions-in-your-app-s-share-extension> (abgerufen)

2024-03: <https://www.msab.com/blog/hidden-gems-in-apple-ios-digital-forensics/>

2022-07: <https://doubleblak.com/knowledgec>

2020-06: <https://www.mac4n6.com/blog/2020/6/21/socially-distant-but-still-interacting-new-and-improved-updates-to-macosios-coreduet-interactioncdb-apollo-modules>

## Tools

APOLLO (interaction_contact_interactions, interaction_contact_interactions_keywords) - <https://github.com/mac4n6/APOLLO>

iLEAPP (interactionCContacts, interactionCAttachments) - <https://github.com/abrignoni/iLEAPP>