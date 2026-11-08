---
title: "MRU - TypedPaths"
status: complete
completed: 2026-11-06
authors: [kalink0 (Marco Neumann)]
topics: [file-access]
---

# MRU - TypedPaths

## Bedeutung

Der Datei-Explorer speichert pro Benutzerkonto die Pfade, die in seine Adressleiste eingegeben oder eingefügt wurden. Damit bietet er sie bei der nächsten Eingabe in der Auswahlliste der Adressleiste wieder an. Neben lokalen Ordnern und Netzwerkfreigaben können das auch Programme sein, die über die Adressleiste mit Pfad oder Namen gestartet wurden.

Aus digitalforensischer Sicht belegt ein Eintrag, dass im Kontext des Benutzerkontos der Pfad in die Adressleiste des Datei-Explorers eingegeben oder eingefügt wurde und der Explorer ihn zu diesem Zeitpunkt auflösen konnte.

## Spezifische Kurzinformation

1. Windows 7 bis Windows 11
2. Maximal 25 Einträge; der neueste Eintrag steht immer in `url1`, ältere rücken nach, der älteste fällt heraus
3. Werte `url1` bis `url25`, Typ REG_SZ; die Reihenfolge ergibt sich aus dem Wertnamen, eine `MRUList` gibt es nicht
4. Nur Pfade, die beim Eintippen aufgelöst werden konnten, werden gespeichert; nicht auflösbare Eingaben nicht
5. Nach mehreren Tests werden die Einträge erst beim Schließen des Explorer-Fensters in den Schlüssel geschrieben; die letzte Schreibzeit des Schlüssels ist dann der Zeitpunkt des Schließens, nicht der Eingabe
6. Sind mehrere Explorer-Fenster offen, führt jedes seine eigene Liste; das zuletzt geschlossene Fenster überschreibt den Schlüssel, Einträge aus den anderen Fenstern gehen dabei verloren
7. Wird mit „Datei-Explorer-Verlauf löschen“ in den Ordneroptionen geleert
8. Ablageort:  
   **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths`**

## Referenzen

2024-03: <https://artefacts.help/windows_registry_typedpaths.html>

2021-10: <https://forensafe.com/blogs/typedpaths.html>

2018-09: <https://www.hecfblog.com/2018/09/daily-blog-483-typed-paths-amnesia.html>

## Tools

DLEAPP (Parser: Explorer Typed Paths) - <https://github.com/abrignoni/DLEAPP>

RECmd (Kroll_Batch) - <https://ericzimmerman.github.io/>

RegRipper (typedpaths) - <https://github.com/keydet89/RegRipper4.0>

Plaso (Parser: windows_typed_urls) - <https://github.com/log2timeline/plaso>

regipy (Plugin: typed_paths) - <https://github.com/mkorman90/regipy>

juntei (parse-registry mru) - <https://github.com/Yamato-Security/juntei>
