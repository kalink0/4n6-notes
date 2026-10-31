---
title: "AirTag"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [location, external-devices]
---

# AirTag

## Bedeutung

AirTags sind Ortungsanhänger von Apple, die über das „Wo ist?“-Netzwerk geortet werden. Auf dem iPhone verwaltet der Systemdienst searchpartyd sowohl die eigenen und geteilten AirTags des Nutzerkontos als auch fremde Tracker, die sich mit dem Gerät mitbewegen und vor denen das iPhone warnt. Dazu legt er pro Datensatztyp eigene, verschlüsselte Records sowie Datenbanken an.

Aus digitalforensischer Sicht belegen die Daten auf dem Gerät des Besitzers, welche AirTags dem Apple-Account zugeordnet oder mit ihm geteilt waren, wann sie gekoppelt bzw. geteilt wurden und an welchen Orten sie gemeldet wurden. Auf dem Gerät einer verfolgten Person belegen sie, dass ein fremder Tracker erkannt und eine Warnung ausgelöst wurde, und an welchen Orten er zusammen mit dem Gerät erkannt wurde. Nicht belegt ist dagegen, wann und wo ein fremder Tracker platziert wurde, wem er gehört und dass sich das untersuchte Gerät selbst an einem gemeldeten AirTag-Standort befand.

| Eintragstyp (in `com.apple.icloud.searchpartyd/`) | Belegt | Relevante Felder |
| --- | --- | --- |
| `OwnedBeacons/` | AirTag ist dem Account zugeordnet, mit Kopplungszeitpunkt und Seriennummer | `pairingTime`, `stableIdentifier` |
| `BeaconNamingRecord/` | Vom Nutzer vergebener Name und Emoji des AirTags | `associatedBeacon` |
| `SharedBeacons/` | AirTag wurde mit dem Account geteilt, von wem und wann | `destination`, `shareDate` |
| `OwnerSharingCircle/`, `OwnerPeerTrust/` | Eigener AirTag wurde geteilt, mit Apple-ID des Empfängers | `acceptanceState` |
| `SafeLocations/` | Orte ohne Warnung bei zurückgelassenen Gegenständen; belegt keinen Aufenthalt | – |
| `BeaconEstimatedLocation/` | Gemeldete Standorte des AirTags mit Zeitstempel | – |
| `WildModeAssociationRecord/` | Fremder Tracker wurde erkannt und eine Warnung ausgelöst, mit Standorten und Hersteller/Modell | – |
| `Observations.db` | „Wo ist?“-Geräte in der Nähe, mit Ort, Zeit und Signalstärke | – |

## Spezifische Kurzinformation

1. Records zu fremden Trackern ab iOS 15.3.1 beobachtet, `Observations.db` ab iOS 16
2. Nur in Full-File-System-Extraktionen mit Keychain auswertbar, nicht in logischen Sicherungen
3. Standorte und Observations werden schnell verworfen, Warnungen zu fremden Trackern nach etwa 48 Stunden; Daten zu eigenen und geteilten AirTags bleiben länger erhalten
4. Records sind AES-GCM-verschlüsselte Binary Plists, Schlüssel in der Keychain (Dienst BeaconStore); die Datenbanken sind mit der SQLite Encryption Extension verschlüsselt, mit eigenem Keychain-Eintrag
5. Zeitstempel in UTC
6. Die Bluetooth-MAC-Adresse eines AirTags wechselt etwa alle 24 Stunden; der erste erfasste Ort eines fremden Trackers ist daher nicht zwingend der Ort der Platzierung
7. Die Kennung eines fremden Trackers ist pro Opfer-Gerät eigen; eine Verknüpfung zum Besitzer ist ohne Apple nicht möglich
8. Warnungen werden auch durch andere „Wo ist?“-Geräte ausgelöst, z.B. AirPods
9. Zusätzlich speichert die „Wo ist?“-App Name, Seriennummer und letzten Standort eigener AirTags im Cache `Items.data`, auswertbar nur wenn unverschlüsselt
10. Ablageorte:  
    **`/private/var/mobile/Library/com.apple.icloud.searchpartyd/`**  
    **`/private/var/mobile/Library/Caches/com.apple.findmy.fmipcore/Items.data`**

## Referenzen

2026-03: <https://thebinaryhick.blog/2026/03/22/old-dog-new-tricks-lost-apples-2-0/>

2025-08: <https://thebinaryhick.blog/2025/08/19/further-observations-more-on-ios-search-party/>

2024-09: <https://thebinaryhick.blog/2024/09/02/where-the-wild-tags-are-other-airtag-stories/>

2022-04: <https://blog.d204n6.com/2022/04/airtag-youre-it.html>

## Tools

ArtEx2 (Find My) - <https://www.doubleblak.com/app.php?id=ArtEx2>

iLEAPP (findMyItemsInfo) - <https://github.com/abrignoni/iLEAPP>

Lost Apples - <https://github.com/joshuahickman1/Lost_Apples>