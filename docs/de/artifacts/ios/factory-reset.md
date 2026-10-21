---
title: "Factory Reset"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [device-state]
---

# Factory Reset

## Bedeutung

Beim Zurücksetzen auf Werkseinstellungen („Alle Inhalte & Einstellungen löschen“) werden die Nutzerdaten eines iPhones gelöscht. Beim ersten Start danach legt iOS mehrere Dateien neu an und protokolliert die Ersteinrichtung, sodass sich das Zurücksetzen und sein ungefährer Zeitpunkt rekonstruieren lassen.

Aus digitalforensischer Sicht belegen diese Spuren, dass das Gerät zurückgesetzt und anschließend neu gestartet bzw. eingerichtet wurde, und wann dieser erste Start ungefähr stattfand. Nicht belegt ist dagegen, dass ein späteres Zurücksetzen ausgeschlossen ist, wenn nach einer Wiederherstellung aus einem iCloud-Backup nur ältere Spuren zu sehen sind.

| Eintragstyp | Belegt | Relevante Felder |
| --- | --- | --- |
| `.obliterated` | Erster Start nach dem Zurücksetzen | Erstellungszeitpunkt der Datei |
| `containermanager.log.{N}` | Erster Start nach dem Zurücksetzen und Abgrenzung zu einem Update: Bei der Prüfung der OS-Version fehlt die vorherige Build-Angabe | – |
| `com.apple.purplebuddy.plist` | Ersteinrichtung nach dem Zurücksetzen bzw. Wiederherstellung aus einem iCloud-Backup | `GuessedCountry`, `SetupState` |
| `AddressBook.sqlitedb`, `CallHistory.storedata` | Neu angelegt kurz nach dem Zurücksetzen | Erstellungszeitpunkt der Datei |

## Spezifische Kurzinformation

1. `.obliterated` und die containermanager-Logs sind nur in Full-File-System-Extraktionen enthalten, die purplebuddy.plist auch in iTunes-Backups
2. Bei den containermanager-Logs ist die Datei mit der höchsten Nummer die älteste
3. Die containermanager-Logs stehen in Gerätezeit; vor der Ersteinrichtung ist das US-Pazifikzeit (UTC-8)
4. `GuessedCountry` markiert den ersten Start nur, wenn `SetupState` den Wert `SetupUsingAssistant` hat; `RestoredFromiCloudBackup` kann auf ein älteres Zurücksetzen verweisen
5. `SetupLastExit` ist unzuverlässig, es ändert sich auch bei späteren Einstellungsänderungen (z.B. Apple Pay)
6. Bei AddressBook und CallHistory zählt der Erstellungs-, nicht der Änderungszeitpunkt
7. Ablageorte:  
   **/private/var/root/.obliterated**  
   **/private/var/root/Library/Logs/MobileContainerManager/containermanager.log.{N}**  
   **/private/var/mobile/Library/Preferences/com.apple.purplebuddy.plist**  
   **/private/var/mobile/Library/AddressBook/AddressBook.sqlitedb**  
   **/private/var/mobile/Library/CallHistoryDB/CallHistory.storedata**

## Referenzen

2026-06: <https://cellebrite.com/en/blog/upgrade-from-null-detecting-ios-wipe-artifacts/>

## Tools

ArtEx2 (Wipe Events) - <https://www.doubleblak.com/app.php?id=ArtEx2>

iLEAPP (wipe_indicators) - <https://github.com/abrignoni/iLEAPP>