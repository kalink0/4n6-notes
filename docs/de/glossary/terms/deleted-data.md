---
title: "Gelöschte Daten"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
---

# Gelöschte Daten

Gelöschte Daten sind Daten, die aus Sicht des Nutzers, einer Anwendung oder des Dateisystems entfernt wurden; je nachdem, auf welcher Ebene gelöscht wurde, sind sie danach noch vollständig, teilweise oder gar nicht mehr vorhanden.

Was „gelöscht“ bedeutet, hängt von dieser Ebene ab; häufige Fälle sind z. B.:

- **Papierkorb bzw. Ordner „Zuletzt gelöscht“:** Die Datei wird nur verschoben und ist weiterhin vollständig als Datei vorhanden, meist bis zu einer festen Frist oder bis der Papierkorb geleert wird.
- **In einer Anwendung als gelöscht markiert:** Der Eintrag, z. B. eine Nachricht, bleibt in der Datenbank der Anwendung erhalten und wird nur über ein Kennzeichen ausgeblendet oder durch einen Platzhalter ersetzt.
- **Aus einer Datenbank entfernt:** Der Datensatz ist aus Sicht der Datenbank nicht mehr vorhanden, sein Inhalt kann aber noch in freien Bereichen der Datenbankdatei oder in zugehörigen Journal- bzw. WAL-Dateien stehen.
- **Im Dateisystem gelöscht:** Der Eintrag der Datei und ihr Speicherplatz werden als frei markiert. Bis sie neu belegt werden, bleiben Inhalt und Metadaten je nach Dateisystem erhalten: Unter NTFS z. B. bleibt der Eintrag mit Name, Zeitstempeln und Lage der Daten bestehen, sodass die Datei vollständig zuordenbar ist; unter ext4 dagegen werden die Verweise auf die Datenblöcke gelöscht und der Inhalt liegt ohne Zuordnung im nicht zugeordneten Speicher.
- **Physisch gelöscht:** Der Inhalt ist auf dem Datenträger nicht mehr vorhanden, z. B. weil er überschrieben, nach einem TRIM-Befehl vom Controller eines Flash-Speichers gelöscht oder der zugehörige Schlüssel einer verschlüsselten Datei vernichtet wurde.

Gelöscht werden Daten aktiv durch den Nutzer, systemgesteuert durch das Betriebssystem oder eine Anwendung, z. B. durch Ablauffristen, Speicherbereinigung oder das Rotieren von Protokollen, oder durch einen externen Auslöser, z. B. eine Fernlöschung, eine vom Kommunikationspartner für alle gelöschte Nachricht oder eine Löschung, die über die Synchronisation von einem anderen Gerät übernommen wurde.

Aus digitalforensischer Sicht ist im Einzelfall zu prüfen, was „gelöscht“ für die jeweiligen Daten bedeutet, auf welcher Ebene sie gelöscht wurden und ob das Löschen durch den Nutzer, systemgesteuert oder durch einen externen Auslöser erfolgte. Forensische Tools kennzeichnen Daten aus unterschiedlichen Ebenen häufig einheitlich als „gelöscht“, z. B. Papierkorb-Inhalte, markierte Datenbankeinträge oder per Carving gefundene Dateien.
