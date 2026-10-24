---
title: "LNK - JumpLists"
status: complete
completed: 2026-10-19
authors: [kalink0 (Marco Neumann)]
topics: [file-access, program-execution]
---

# LNK - JumpLists

## Bedeutung

JumpLists werden seit Windows 7 im Betriebssystem verwendet. JumpLists zeigen dem Benutzer zuletzt geöffnete Dateien und zuletzt verwendete Programme zum Beispiel im Startmenü an. Die Funktion dient der Erhöhung der Benutzerfreundlichkeit und wird vom Betriebssystem selbst ausgeführt anhand der Bedienung des Benutzers.

Ein Benutzer kann auch selbst Einträge an z.B. das Startmenü "anpinnen" - diese Funktion dient ebenfalls der Benutzerfreundlichkeit und die Ablage erfolgt ebenfalls in JumpLists. Man kann diese Funktion als setzen von "Favoriten" bezeichnen. Zusätzlich werden bei den automatisch generierten Einträgen die Zeitstempel des letzten Zugriffs gespeichert und die Anzahl der Zugriffe.

Aus digitalforensischer Sicht bedeutet die Existenz von Jumplists folgendes:

1. Bei den automatisch generierten Einträgen:
   1. Der Nutzeraccount hat zum angegeben Zeitpunkt (Zuletzt zugegriffen) zuletzt die angegebene Zieldatei (gemäß dem Dateinamen) aufgerufen/gestartet.
   2. Der Nutzeraccount hat zum angegeben Zeitpunkt (Erstelldatum) die Datei/das Programm zum ersten Mal aufgerufen. Das System hat somit den Eintrag erstellt.
2. Bei den manuell angelegten Einträgen:
   1. Der Nutzeraccount hat zum angegeben Zeitpunkt (Zuletzt zugegriffen) zuletzt die angegebene Zieldatei (gemäß dem Dateinamen) aufgerufen/gestartet.
   2. Der Nutzeraccount hat zum angegeben Zeitpunkt (Erstelldatum) die Datei/das Programm aktiv "angepinnt". Dies kann auch im Zuge einer Programminstallation durchgeführt werden.

## Spezifische Kurzinformation

1. JumpLists werden Apps zugeordnet, welche per AppID identifiziert werden können (Listen siehe unten) - eine AppID gibt an, in welchem Kontext die JumpList vorliegt und gibt daher Info darüber, wie der Nutzeraccount die Aktion durchgeführt hat.
2. Die Anzahl der Aufrufe (Interaction Account) ist nach derzeitigem Stand nicht genau erklärbar/nachvollziehbar und daher ist der Wert mit Vorsicht zu behandeln.
3. Ablageort:  
   **`%AppData%\Microsoft\Windows\Recent\AutomaticDestinations`**  
   **`%AppData%\Microsoft\Windows\Recent\CustomDestinations`**

## Referenzen

2025-01: <https://www.cybertriage.com/blog/what-is-jump-list-cache/>

2025-01: <https://www.cybertriage.com/blog/jump-list-forensics-2025/>

2025-01: <https://windowsir.blogspot.com/2025/01/artifacts-jump-lists.html>

2020-09: <https://dfir.pubpub.org/pub/wfuxlu9v/release/1>

2020-02: <https://cloud.google.com/blog/topics/threat-intelligence/the-missing-lnk-correlating-user-search-lnk-files/>

2016-02: <https://binaryforay.blogspot.com/2016/02/jump-lists-in-depth-understand-format.html>

2010-06: <http://computerforensics.parsonage.co.uk/downloads/TheMeaningofLIFE.pdf>

#### JumpList IDs:

<https://forensics.wiki/list_of_jump_list_ids/>

<https://github.com/EricZimmerman/JumpList/blob/master/JumpList/Resources/AppIDs.txt>

## Tools

JLECmd - <https://ericzimmerman.github.io/>

JumpList Explorer - <https://ericzimmerman.github.io/>

LECmd - <https://ericzimmerman.github.io/>

Jumplist-Browser - <https://github.com/kacos2000/Jumplist-Browser>
