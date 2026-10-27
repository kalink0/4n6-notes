---
title: "Office Trust Records"
status: reviewed
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
reviewers: [dugeonlady]
reviewed: 2026-10-26
topics: [file-access]
---

# Office Trust Records

## Bedeutung

Microsoft Office öffnet Dokumente, die aus dem Internet kommen oder aus einer anderen nicht vertrauten Quelle in der sogenannten *Protected View*. Diese Ansicht dient dazu, dass keine schädlichen Funktionen in dem Dokument ausgeführt werden können.

Der Nutzer wird aktiv gefragt, ob die *Protected View* verlassen werden soll um das Dokument bearbeiten zu können und im zweiten Schritt, ob eventuell vorhandene Makros aktiviert werden sollen. Wenn der Nutzer dies bestätigt, wird ein sogenannter *Trust Record* erstellt.

Aus digitalforensischer Sicht bedeutet die Existenz eines *Trust Records*, dass der Nutzer aktiv die Bearbeitungsansicht des Dokuments, mit dem angegeben Dateipfad und Dateinamen, und gegebenenfalls Makros aktiviert hat - dies ist ablesbar anhand des Data Values.

## Spezifische Kurzinformation

1. Verfügbarkeit: Die Sicherheitsfunktion gibt es seit MS Office 2010
2. Voraussetzungen: Trust Records werden nur gesetzt, wenn die Standardeinstellungen eine aktive Zustimmung des Nutzers erfordern.
3. Format und Struktur: Bedeutung letzte 4 Bytes im Data Value:  
   01 00 00 00 = "Enable Editing" wurde durch das Nutzerkonto geklickt  
   ff ff ff 7f = "Enable Content" wurde durch das Nutzerkonto geklickt (Makros aktiviert)
4. Zeitstempel: Bedeutung der ersten 8 Bytes im Data Value: Zeitstempel der Erstellung des Dokumentes
5. Ablageort:  
   **`HKCU\Software\Microsoft\Office\{VERSION}\{APPNAME}\Security\Trusted Documents\TrustRecords`**

## Referenzen

2020-03: <https://www.bleepingcomputer.com/news/security/windows-registry-helps-find-malicious-docs-behind-infections/>

2016-02: <https://az4n6.blogspot.com/2016/02/more-on-trust-records-macros-and.html>

## Tools

RegRipper (msoffice) - <https://github.com/keydet89/RegRipper4.0>