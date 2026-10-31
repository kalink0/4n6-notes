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

InteractionC is a CoreDuet database in which macOS records interactions of the device with other people, e.g. messages, emails and calendar entries. On this basis, macOS suggests frequent contacts to the user, for example in the share menu. It stores the app involved, the contacts involved as sender or recipient, times and, where applicable, attachments, but hardly any content such as message texts.

From a digital forensics perspective, an entry shows that an interaction with the linked contacts took place via the given app at the given time. It does not show, however, the content of the interaction.

## Key facts

1. Present since macOS 10.15, still populated on macOS 15
2. SQLite database; central table `ZINTERACTIONS`, plus `ZCONTACTS` (per contact interaction counters as well as first and last contact), `ZATTACHMENT` and `ZKEYWORDS`
3. Timestamps in Mac Absolute Time format (seconds since 2001-01-01, UTC)
4. Location:  
   **`/private/var/db/CoreDuet/People/interactionC.db`**

## References

2026-10 (accessed): <https://developer.apple.com/documentation/foundation/supporting-suggestions-in-your-app-s-share-extension>

2021-09: <https://www.sentinelone.com/labs/macos-incident-response-part-2-user-data-activity-and-behavior/>

2020-06: <https://www.mac4n6.com/blog/2020/6/21/socially-distant-but-still-interacting-new-and-improved-updates-to-macosios-coreduet-interactioncdb-apollo-modules>

## Tools

APOLLO (interaction_contact_interactions, interaction_contact_interactions_keywords) - <https://github.com/mac4n6/APOLLO>

DLEAPP (InteractionC) - <https://github.com/abrignoni/DLEAPP>
