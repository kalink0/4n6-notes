---
title: "App Ops"
status: draft
authors: [kalink0 (Marco Neumann)]
topics: [program-execution]
---

# App Ops

## Bedeutung

App Ops (App Operations) ist ein Dienst von Android, der für jede App festhält, welche geschützten Operationen sie ausführt, etwa den Zugriff auf Standort, Kamera, Mikrofon oder Kontakte, und welcher Modus für jede Operation eingestellt ist. Android nutzt diese Daten für die Prüfung von Berechtigungen und für die Anzeige der Berechtigungsnutzung in den Einstellungen. Der Dienst schreibt mehrere Dateien, von einzelnen Zugriffen der letzten Tage bis zu Zählern über die gesamte Nutzungszeit des Geräts. Jede Operation ist durch einen festen Zahlencode bezeichnet, z. B. 0 = ungefährer Standort, 1 = genauer Standort, 26 = Kamera, 27 = Mikrofon; vollständige Liste: <https://android.googlesource.com/platform/frameworks/proto_logging/+/refs/tags/android-17.0.0_r1/stats/enums/app_shared/app_op_enums.proto>

Aus digitalforensischer Sicht belegen die Einträge, dass eine App eine Operation zu einem Zeitpunkt oder in einem Zeitfenster ausgeführt hat oder dabei abgelehnt wurde, und in welchem Zustand die App dabei war, z. B. sichtbar im Vordergrund oder im Hintergrund. Viele Einträge stammen von Systemprozessen. Fehlende Einträge belegen nicht, dass kein Zugriff stattfand: Discrete erfasst nur bestimmte Operationen, und Modi werden nur gespeichert, wenn sie vom Standard abweichen.

| Eintragstyp | Belegt | Relevante Felder |
| --- | --- | --- |
| Modes | Welcher Modus für eine Operation je App bzw. UID eingestellt ist (0 = erlaubt, 1 = ignoriert, 2 = Fehler, 3 = Standard, 4 = nur im Vordergrund) | `n`, `m` |
| Letzte Zugriffe | Wann eine App eine Operation zuletzt ausgeführt hat bzw. zuletzt abgelehnt wurde, je Zustand der App; ein neuer Zugriff überschreibt den vorherigen | `n`, `t`, `r`, `d`, `pp` |
| Discrete | Einzelne Zugriffe einer App auf eine Operation mit Zeitpunkt, Dauer und Zustand | `nt`, `nd`, `us`, `f` |
| History | Anzahl der Zugriffe und Ablehnungen sowie Gesamtdauer je App und Operation in einem Zeitfenster | `beg`, `end`, `na`, `ac`, `rc`, `du` |

### Discrete

Erfasst werden nur bestimmte Operationen, standardmäßig Standort, Kamera, Mikrofon sowie Mikrofon und Kamera während eines Telefonats; Google bzw. der Hersteller kann die Liste ändern. Ablehnungen stehen nicht in Discrete, und weitere Zugriffe derselben App in derselben Minute mit gleichem Zustand werden nicht gespeichert. Ein Zugriff mit Dauer steht zweimal da, beim Beginn ohne Dauer und beim Ende mit derselben Startzeit und der Dauer.

### History

Das jüngste Zeitfenster umfasst 15 Minuten, jede ältere Datei fasst zehnmal so lange Zeitfenster zusammen. Ältere Daten werden nicht gelöscht, sondern in immer gröbere Zeitfenster übernommen; History reicht daher grundsätzlich bis zur Einrichtung des Geräts zurück, der genaue Zeitpunkt eines Zugriffs ist aber nicht ablesbar.

## Spezifische Kurzinformation

1. Verfügbarkeit: alle Android-Geräte; History seit Android 10, Discrete seit Android 12, Letzte Zugriffe als eigene Datei seit Android 14; Modes seit Android 15 im Berechtigungsspeicher (`access.abx`), auf einigen Geräten weiterhin in `appops.xml`
2. Voraussetzungen: standardmäßig aktiv; welche Operationen Discrete erfasst und wie lange, kann Google bzw. der Hersteller über die Gerätekonfiguration ändern
3. Aufbewahrung: Discrete standardmäßig 7 Tage (Android 12: 24 Stunden), einstellbar bis 30 Tage; History ohne zeitliche Grenze; bei der Deinstallation einer App löscht Android ihre Einträge in Discrete und History
4. Format und Struktur: Binäres Android-XML (ABX); Zustand der App: 100 = dauerhaft, 200 = sichtbar im Vordergrund, 300 = Vordergrunddienst mit Standort, 400 = Vordergrunddienst, 500 = Vordergrund, 600 = Hintergrund, 700 = zwischengespeichert; Art des Zugriffs als Bitmaske: 0x1 = selbst, 0x2/0x4 = als Proxy für eine andere App, 0x8/0x10 = über eine andere App als Proxy; bei Letzten Zugriffen und History stehen beide Angaben in einem Schlüssel (Zustand × 2³¹ + Bitmaske)
5. Zeitstempel: Unix-Zeit in Millisekunden (UTC); History als Abstand in Millisekunden vor der letzten Speicherung, absolute Zeit ≈ Änderungszeitpunkt von `900000.xml` − Abstand
6. Besonderheiten und Fallstricke: Seit Android 16 kann Android Discrete und History abhängig von Feature-Flags in der SQLite-Datenbank `app_op_history.db` speichern und die XML-Dateien dorthin übernehmen
7. Ablageort:  
   Modes (bis Android 14), Letzte Zugriffe (bis Android 13): **`/data/system/appops.xml`**  
   Modes (ab Android 15): **`/data/misc_de/{USER_ID}/apexdata/com.android.permission/access.abx`**  
   Modes (ab Android 15, systemweit): **`/data/misc/apexdata/com.android.permission/access.abx`**  
   Letzte Zugriffe (ab Android 14): **`/data/system/appops_accesses.xml`**  
   Discrete: **`/data/system/appops/discrete/{ZEITSTEMPEL}tl`**  
   History: **`/data/system/appops/history/{INTERVALL}.xml`**  
   Discrete und History (ab Android 16, je nach Feature-Flags): **`/data/system/appops/app_op_history.db`**

## Referenzen

2026-08: <https://forensafe.com/blogs/android-privacy-dashboard.html>

2022-01: <https://thebinaryhick.blog/2022/01/22/snooping-on-android-12s-privacy-dashboard/>

## Tools

ALEAPP (Parser: App Ops) - <https://github.com/abrignoni/ALEAPP>
