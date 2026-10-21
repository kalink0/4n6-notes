---
title: "AirDrop"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [data-transfer]
---

# AirDrop

## Bedeutung

AirDrop ist die Apple-Funktion zur direkten Übertragung von Fotos, Dateien, Links und anderen Inhalten zwischen Apple-Geräten in der Nähe. Die Übertragung wickelt der Systemdienst sharingd ab. Er protokolliert dabei in den Unified Logs, wann ein Inhalt geteilt, eine Übertragung angeboten, angenommen oder abgelehnt wurde und wie die AirDrop-Sichtbarkeit eingestellt ist. Die aktuelle AirDrop-ID und die Sichtbarkeitseinstellung legt er zusätzlich in einer Einstellungsdatei ab.

Aus digitalforensischer Sicht belegen die Einträge auf dem sendenden Gerät, dass ein bestimmter Inhalt aus einer bestimmten App per AirDrop an ein anderes Gerät gesendet werden sollte, und ob die Übertragung angenommen wurde. Auf dem empfangenden Gerät belegen sie, dass eine Übertragung von einem Gerät mit dem geloggten Gerätenamen einging und ob sie angenommen, abgelehnt oder abgebrochen wurde. Änderungen der Sichtbarkeit (Aus, Nur Kontakte, Jeder) lassen sich ebenfalls nachvollziehen. Der geloggte Gerätename allein belegt dagegen nicht, wer der Absender war, da er frei änderbar ist.

## Spezifische Kurzinformation

1. Die AirDrop-Einträge in den Unified Logs bleiben nur wenige Tage bis etwa eine Woche erhalten
2. Unified Logs: Prozess sharingd, Subsystem `com.apple.sharing`, Kategorie `AirDrop`; zusätzlich Property List mit AirDrop-ID und Sichtbarkeitsmodus
3. Die AirDrop-ID ist nicht dauerhaft, sie wechselt häufig; nach längerer Nichtnutzung kann die Property List keine ID enthalten
4. Im Log des Empfängers stehen Teil-Hashes (SHA-256) von Telefonnummer bzw. E-Mail-Adresse der Apple-ID des Absenders; darüber lässt sich der Absender ggf. ermitteln
5. Empfangene Fotos und Videos landen in der Regel in der Fotos-App
6. Für die Zuordnung einer Übertragung zu einem Gegenüber werden die Logs beider Geräte benötigt
7. Weitere AirDrop-Spuren: PowerLog (Tabelle `PLXPCAgent_EventForward_AirDrop`, untersucht bis iOS 14), KnowledgeC (Stream `/photos/share/airdrop`, iOS 13 und 14) und InteractionC
8. Ablageorte:  
   **/private/var/db/diagnostics/** (Unified Logs, auch im sysdiagnose als system_logs.logarchive)  
   **/private/var/mobile/Library/Preferences/com.apple.sharingd.plist**

## Referenzen

2026-09: <https://magnetforensics.com/blog/following-the-airdrop-breadcrumbs-with-axiom>

2022-03: <https://gforce4n6.blogspot.com/2022/03/airdropping-some-knowledge-using-rleapp.html>

2020-06: <https://www.mac4n6.com/blog/2020/6/5/analysis-of-apple-unified-logs-quarantine-edition-entry-11-airdropping-some-knowledge>

## Tools

APOLLO (powerlog_airdrop, knowledge_photos_share_airdrop) - <https://github.com/mac4n6/APOLLO>

ArtEx2 (AirDrop) - <https://www.doubleblak.com/app.php?id=ArtEx2>

iLEAPP (airdropId, logarchive_airdrop) - <https://github.com/abrignoni/iLEAPP>

RLEAPP (airdropNumbers, airdropEmails, airdropRealname, airdropdiscoverable) - <https://github.com/abrignoni/RLEAPP>