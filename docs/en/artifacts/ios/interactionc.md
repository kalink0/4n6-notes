---
title: "InteractionC"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [communication]
---

# InteractionC

## Meaning

InteractionC is a CoreDuet database in which iOS records interactions of the device with other people, e.g. calls, messages, emails and calendar entries. On this basis, iOS suggests frequent contacts to the user, for example in the share sheet. It stores the app involved, the contacts involved as sender or recipient, times and, where applicable, attachments, but hardly any content such as message texts.

From a digital forensics perspective, an entry shows that an interaction with the linked contacts took place via the given app at the given time. It does not show, however, the content of the interaction.

## Key facts

1. Also included in iTunes backups
2. Sometimes goes back several months (about six months in one examined case)
3. SQLite database; central table `ZINTERACTIONS`, plus `ZCONTACTS` (per contact interaction counters as well as first and last contact), `ZATTACHMENT` and `ZKEYWORDS`
4. Timestamps in Mac Absolute Time format (seconds since 2001-01-01, UTC)
5. Contacts can be matched with the address book via GUIDs
6. The recipient count does not include the device user
7. Some of the attachments are no longer assigned to any interaction and have no timestamp
8. Location:  
   **`/private/var/mobile/Library/CoreDuet/People/interactionC.db`**

## References

2026-10 (accessed): <https://developer.apple.com/documentation/foundation/supporting-suggestions-in-your-app-s-share-extension>

2024-03: <https://www.msab.com/blog/hidden-gems-in-apple-ios-digital-forensics/>

2022-07: <https://doubleblak.com/knowledgec>

2020-06: <https://www.mac4n6.com/blog/2020/6/21/socially-distant-but-still-interacting-new-and-improved-updates-to-macosios-coreduet-interactioncdb-apollo-modules>

## Tools

APOLLO (interaction_contact_interactions, interaction_contact_interactions_keywords) - <https://github.com/mac4n6/APOLLO>

iLEAPP (interactionCContacts, interactionCAttachments) - <https://github.com/abrignoni/iLEAPP>
