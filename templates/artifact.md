---
title: "Name des Artefakts"
status: draft
authors: [github-handle]  # optional mit Namen: [kalink0 (Marco Neumann)]
topics: []  # mindestens ein Schlüssel aus extra.topics in mkdocs.base.yml
---

<!--
Vorlage für Artefaktseiten. Alle Regeln im Detail: CONTRIBUTING.md.
Hinweise stehen in Kommentaren wie diesem; sie sind auf der Website unsichtbar.
Ein Abschnitt ohne Inhalt bleibt stehen und enthält nur: *Noch kein Inhalt.*
Status: draft (unfertig) → complete (vom Autor fertiggestellt) → reviewed (von einer zweiten
Person gegengelesen). Personen als GitHub-Handle, optional mit Namen in Klammern.

Fertiggestellt, setzt der Autor:
    status: complete
    completed: 2026-10-19
    authors: [kalink0 (Marco Neumann)]

Reviewed, ergänzt der Reviewer (nie einer der Autoren); completed und authors bleiben:
    status: reviewed
    completed: 2026-10-19
    authors: [kalink0 (Marco Neumann)]
    reviewers: [max-mustermann (Max Mustermann), erika-m]
    reviewed: 2026-10-21

Ändert sich der Inhalt einer reviewed-Seite, geht sie zurück auf complete (oder draft);
reviewers und reviewed werden entfernt.
-->

# Name des Artefakts

## Bedeutung

<!--
Fließtext in zwei Teilen:
1. Was ist das Artefakt? Welche Komponente schreibt es, wann und wozu?
2. Was belegt ein Eintrag forensisch, und was belegt er NICHT (Grenzen, Fehlinterpretationen)?
Keine Pfade, Versionslisten, Feldnamen oder Tools; die gehören in die Kurzinformation.
Links auf andere Artefakte nur, wo der Text ohnehin darauf Bezug nimmt (z.B. Nachfolger),
nicht als "siehe auch" und nicht auf dasselbe Artefakt auf einer anderen Plattform.
-->

Was ist das Artefakt, welche Komponente schreibt es und wann? Wozu dient es dem System?

Aus digitalforensischer Sicht belegt ein Eintrag, dass … Nicht belegt ist dagegen, dass …

<!--
Tabelle nur bei Artefakten mit einer Reihe von Unterartefakten (z.B. Streams in KnowledgeC
oder Biome); ob ein Artefakt sie bekommt, legt der Maintainer fest. Sonst Tabelle löschen.
"Belegt": kurz, möglichst ein Satz. "Relevante Felder": nur die für diese Aussage nötigen.
-->

| Eintragstyp | Belegt | Relevante Felder |
| --- | --- | --- |
| `typ/a` | … | `FELD_X`, `FELD_Y` |

<!-- Eigener Unterabschnitt nur, wenn ein Typ mehr als zwei Sätze braucht. Sonst löschen. -->

### `typ/a`

Ausführliche Bedeutung dieses Eintragstyps.

## Spezifische Kurzinformation

<!--
Ein Fakt pro Punkt, kurz, in dieser Reihenfolge. Was nicht zutrifft oder unbekannt ist, entfällt.
Aussagen, die sich mit Updates ändern, bekommen einen Stand: "seit iOS 16", "Stand 2026-07".
Pfade (Dateien, Ordner, Registry-Schlüssel) stehen immer fett und in Backticks, im Ablageort
wie im Fließtext:
    **`C:\Windows\Prefetch\*.pf`**
    **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`**
    **`/private/var/db/diagnostics`**
Backslashes einfach, nie doppelt (in Backticks wird nichts maskiert).
Platzhalter in geschweiften Klammern: {USER}, {USER_SID}, {DRIVE}, {UUID}; nie spitze Klammern.
Ausnahme: In Tabellenzellen stehen Pfade nur in Backticks, nicht fett.
Ablageort: Pfad eingerückt (3 Leerzeichen, unter dem Listenpunkt).
Bei mehreren Ablageorten einer pro Zeile, mit zwei Leerzeichen am Zeilenende:
7. Ablageort:  
   iOS: **`/private/var/…`**  
   macOS: **`~/Library/…`**
-->

1. Verfügbarkeit: Betriebssystem/Version, ggf. Hardware
2. Voraussetzungen: standardmäßig aktiv oder Opt-in, abschaltbar durch …
3. Aufbewahrung: Zeitraum, Rotation, Löschverhalten
4. Format und Struktur: Dateityp, zentrale Tabellen/Felder in `Code`-Schreibweise
5. Zeitstempel: Format, Zeitzone, Bedeutung der einzelnen Zeitstempel
6. Besonderheiten und Fallstricke
7. Ablageort:  
   **`/pfad/zur/datei`**

## Referenzen

<!--
Format: YYYY-MM: <URL>, eine Quelle pro Absatz, neueste zuerst.
Datum = Veröffentlichung bzw. letzte Überarbeitung (jede Überarbeitung zählt). Nicht sichtbar?
Metadaten der Seite prüfen (z.B. datePublished). Sonst Abrufdatum mit Zusatz (abgerufen).
Nur Quellen zu diesem Artefakt, die einem Analysten helfen (Artikel, Vorträge,
Formatbeschreibungen). Kein Quellcode als reiner Beleg.
Ohne URL: YYYY-MM: Autor: Titel *(Quelle wird ergänzt)*
-->

YYYY-MM: <https://…>

## Tools

<!--
Format: Name - <URL> bzw. Name (Modul) - <URL>, ein Tool pro Absatz.
URL = Hauptseite des Tools (zum Herunterladen), nicht der Quellcode eines Moduls.
Nur freie Tools (Open Source oder kostenlos), keine kommerziellen.
Nur Tools, die das Artefakt dekodieren; Formaterkennung oder generische Viewer reichen nicht.
crush-forensics und peach-forensics nach demselben Kriterium prüfen.
Keine Versionsangaben. Einzige erlaubte Ergänzung: (nur alte Versionen), wenn das Tool nicht
mehr weiterentwickelt wird und nur ältere Versionen des Artefakts kann.
-->

Name - <https://…>
