---
title: "Tracker Detection"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
topics: [location, external-devices]
---

# Tracker Detection

## Bedeutung

Android warnt über die Google Play Services vor unbekannten Bluetooth-Trackern, die sich mit dem Gerät mitbewegen. Das sind AirTags und Tracker aus dem Find-My-Device-Netzwerk (FMD), Letztere seit Mai 2024. Das Gerät scannt dafür passiv. Der Nutzer kann zusätzlich manuell scannen. Wird ein Tracker als „folgend“ eingestuft, erscheint die Meldung, dass ein unbekannter Tracker mit dem Nutzer unterwegs ist.

Auf demselben Gerät können Spuren von beiden Seiten liegen:

- **Verfolgten-Seite (Gerät wurde getrackt / hat Tracker gesehen):**
    - Welche Tracker in der Nähe erkannt wurden: MAC, Zeitpunkt der ersten und letzten Erfassung.
    - Standort und Bewegungszustand des Geräts zu jedem Scan, unabhängig davon, ob eine Warnung ausgelöst wurde.
    - Ob und wann eine Warnung ausgelöst (STAGED) und angezeigt (SENT) wurde.
    - Wann zuletzt gescannt wurde. Unter Umständen ist auch erkennbar, ob das passive Scannen an oder aus ist.
    - Ob die Warnmeldung tatsächlich als Benachrichtigung angezeigt wurde. Das ist nur belegbar, wenn der Benachrichtigungsverlauf aktiviert ist.
- **Owner-Seite (Gerät gehört zum Besitzer eines Trackers):**
    - Welche Fast-Pair-Zubehörteile (u. a. FMD-Tracker) dem Gerät bekannt sind: MAC, Name bzw. vom Nutzer vergebener Name, Zeitpunkte der ersten und letzten Beobachtung.

**Nicht belegt:**

- Die Standorthistorie eigener Tracker. Sie liegt nicht lokal auf dem Gerät.
- Die Identität des Owners eines fremden Trackers. Für FMD-Tracker wird ein Ring Key gespeichert, über den Google den Owner zuordnen kann. Lokal ist der Owner nicht ersichtlich.
- Eine dauerhafte Zuordnung über die MAC. Tracker rotieren ihre MAC-Adresse.
- Dass ein Fast-Pair-Eintrag eine tatsächliche Kopplung belegt.

| Eintragstyp (in ...) | Belegt | Relevante Felder |
|---|---|---|
| Scan (`personalsafety_db`) | Verfolgt | Alle gesehenen Tracker inkl. manueller Scans; MAC, erste/letzte Erfassung, `state` (`STATE_STILL`, `STATE_MOVING`), BLOB `locationScan` (Standort des Geräts) |
| DeviceData (`personalsafety_db`) | Verfolgt | Warnungen mit Status STAGED / SENT; bei FMD-Trackern Modell und Ring Key |
| `personalsafety_info.pb` | Verfolgt | Zeitpunkt des letzten Scans (Unix ms) |
| `personalsafety_optin.pb` | Verfolgt | Status des passiven Scannens |
| Benachrichtigungsverlauf (`notification_history`) | Verfolgt | Package, Zeitpunkt und Inhalt der Tracker-Warnung |
| `nearby_fast_pair_item_cache.db` | Owner | MAC, Gerätename, Titel (vom Nutzer vergebener Name), erste und letzte Beobachtung, Bild |

## Kurzinfo

1. **Vorhaltezeit:** Scan-Einträge werden nur etwa zwei Tage vorgehalten. Eine leere Datenbank belegt nicht, dass das Scannen deaktiviert war.

2. **Standort:** `locationScan` enthält Breiten- und Längengrad des Geräts zum Scanzeitpunkt (Protobuf, Werte × 10.000.000), `state` den Bewegungszustand.

3. **`personalsafety_optin.pb`:** Die Datei ist nicht immer vorhanden. Die Belegung 1 = an, 2 = aus ist nicht abschließend belegt.

4. **Benachrichtigungsverlauf:** Er wird nur geschrieben, wenn der Nutzer ihn aktiviert hat.

5. **Fast-Pair-Cache:** Einträge bleiben auch nach dem Entkoppeln erhalten. Ein Eintrag belegt nicht sicher, dass das Zubehör gekoppelt war.

6. Ablageorte:  
   **`/data/data/com.google.android.gms/databases/personalsafety_db`**  
   **`/data/data/com.google.android.gms/files/personalsafety/shared/`** (`personalsafety_info.pb`, `personalsafety_optin.pb`)  
   **`/data/system_ce/{USER_ID}/notification_history/history/`**  
   **`/data/data/com.google.android.gms/files/nearby-fast-pair/nearby_fast_pair_item_cache.db`** (LevelDB)

## Referenzen

- 2026-10 (abgerufen) - Google - Unbekannte Tracker erkennen - <https://support.google.com/android/answer/13658562>
- 2024-08 - Josh Hickman - Not All Androids Who Wander Are Lost: A Look at Android's Find My Device Network - <https://thebinaryhick.blog/2024/08/23/not-all-androids-who-wonder-are-lost-a-look-at-androids-find-my-device-network/>
- 2023-08 - Josh Hickman - Android & AirTags Part II - <https://thebinaryhick.blog/2023/08/13/android-airtags-part-ii/>

## Tools

- ALEAPP (Android Airtag Alerts / Scans / Last Scan / Passive Scan) - <https://github.com/abrignoni/ALEAPP>
- ALEAPP (Android Notification History) - <https://github.com/abrignoni/ALEAPP>
- ALEAPP (Nearby - Fast Pair Devices) - <https://github.com/abrignoni/ALEAPP>