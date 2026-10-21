---
title: "SRUM - System Resource Utilization Monitor"
status: complete
completed: 2026-10-20
authors: [kalink0 (Marco Neumann)]
topics: [program-execution, network]
---

# SRUM - System Resource Utilization Monitor

## Bedeutung

Der System Resource Utilization Monitor ist ein Feature in modernen Windows Betriebssystemen. Es dient dazu Informationen zu ausgeführten Programmen und deren Ressourcennutzung zu überwachen. Es werden mitunter Informationen zur Netzwerknutzung (Datenmenge, verwendete Netzwerke, verwendete Netzwerkadapter), Systemnutzung (Dateipfad, CPU-Nutzung, Datenmenge) und genutztes Nutzerkonto gespeichert.

Aus digitalforensischer Sicht geben Einträge des SRUM Aufschluss über ausgeführte Programme, deren Ressourcenverbrauch und welches Nutzerkonto das Programm ausgeführt hat. Die Genauigkeit der Ausführung liegt bei standardmäßig 60 Minuten. Ein aufgeführtes Programm ist daher mit den angegeben Daten in dem Zeitraum und mit den Nutzerkonto aktiv gewesen. Für das Zeitfenster werden die entsprechenden Ressourcen (z.B. hochgeladene Datenmenge) angegeben.

## Spezifische Kurzinformation

1. Verfügbar ab Windows 8
2. Zeitfenster für das Erstellen von Einträgen liegt bei standardmäßig 60 Minuten - eine genauere Aussage über die Ressourcennutzung ist daher nicht möglich
3. Ablagedauer beträgt etwa 30 - 60 Tage.
4. Infomation werden nicht SOFORT in die Datenbank geschrieben. Es liegen noch nicht geschriebene Daten in der Registry vor. Die Registry dient als temporärer Speicher.
5. Ablageort temporär (Reigstry): **`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SRUM`**
6. Ablageort persistiert: **`C:\Windows\System32\sru\SRUDB.dat`**

## Referenzen

2026-09: <https://www.it-connect.tech/windows-forensics-part-12-analyzing-srum/>

2026-02: <https://www.cyberengage.org/post/unpacking-srum-the-digital-forensics-goldmine-in-windows>

2022-10: <https://www.magnetforensics.com/blog/srum-forensic-analysis-of-windows-system-resource-utilization-monitor/>

2019-12: <https://docs.velociraptor.app/blog/2019/2019-12-31_digging-into-the-system-resource-usage-monitor-srum-afbadb1a375/>

## Tools

SrumECmd - <https://ericzimmerman.github.io/>

Srum dump - <https://github.com/MarkBaggett/srum-dump>

ESE Database View - <https://www.nirsoft.net/utils/ese_database_view.html>

DLEAPP (Parser: SRUM Network Usage, SRUM Application Resource Usage, SRUM Network Connections) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (Artefakt: Windows.Forensics.SRUM) - <https://docs.velociraptor.app/artifact_references/pages/windows.forensics.srum/>

Dissect (Plugin: sru) - <https://docs.dissect.tools/en/stable/plugins/sru.html>