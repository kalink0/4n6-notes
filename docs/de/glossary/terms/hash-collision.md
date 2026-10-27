---
title: "Hash-Kollision"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Hash-Kollision

Eine Hash-Kollision liegt vor, wenn zwei unterschiedliche Daten denselben Hash-Wert ergeben.

Da ein Hash-Wert eine feste Länge hat, es aber beliebig viele mögliche Daten gibt, existieren solche Kollisionen bei jeder Hash-Funktion zwangsläufig. Eine Hash-Funktion gilt als sicher, solange sie sich nicht mit vertretbarem Aufwand gezielt finden lassen. Bei Angriffen auf Hash-Funktionen werden zwei Arten unterschieden. Beim Kollisionsangriff (Collision Attack) erstellt der Angreifer zwei Dateien selbst und verändert beide so lange, bis sie denselben Hash-Wert haben; welcher Hash-Wert dabei herauskommt, kann er nicht festlegen. Für MD5 sind solche Angriffe seit 2004 praktisch möglich, für SHA-1 seit 2017. Inzwischen kann der Angreifer den Anfang beider Dateien frei wählen (Chosen-Prefix-Kollision), die für die Kollision eingefügten Datenblöcke sehen jedoch zufällig aus. Beim Preimage-Angriff (Preimage Attack) ist dagegen ein Hash-Wert vorgegeben, und der Angreifer sucht Daten, die genau diesen Hash-Wert ergeben. Ist eine Datei vorgegeben, zu der eine zweite mit demselben Hash-Wert gefunden werden soll, spricht man von einem Second-Preimage-Angriff. Für MD5 und SHA-1 ist kein praktisch durchführbarer Preimage-Angriff bekannt; der beste bekannte Angriff auf MD5 benötigt etwa 2^123 Rechenschritte und ist damit nicht durchführbar.

Aus digitalforensischer Sicht wäre ein Second-Preimage-Angriff nötig, um eine Sicherung unbemerkt auszutauschen oder eine Datei so zu verändern, dass sie den Hash-Wert einer bekannten, unverdächtigen Datei annimmt, da die Datei und ihr Hash-Wert in diesen Fällen bereits feststehen. Die bekannten Kollisionen bei MD5 und SHA-1 stellen die Prüfung von Sicherungen und die Identifikation von Dateien über ihren Hash-Wert daher nicht in Frage. Ein Kollisionsangriff ist nur dort relevant, wo jemand beide Dateien selbst erstellen konnte, bevor ihr Hash-Wert erfasst wurde, z. B. wenn eine harmlose Datei in eine Liste bekannter Dateien aufgenommen und später gegen die zweite, präparierte Datei ausgetauscht wird.