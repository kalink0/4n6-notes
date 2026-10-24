---
title: "macOS CurrentPowerLog"
status: complete
completed: 2026-10-24
authors: [kalink0 (Marco Neumann)]
topics: [device-state, program-execution]
---

# macOS CurrentPowerLog

## Bedeutung

macOS erfasst mit Powerlog Energieverbrauch und Aktivitäten verschiedener Systemkomponenten. Diese Informationen helfen dabei, den Energieverbrauch und das Verhalten des Systems zu analysieren, beispielsweise im Zusammenhang mit der Batterielaufzeit.

Aus digitalforensischer Sicht können die gespeicherten Ereignisse Hinweise auf App-Aktivitäten und weitere Systemereignisse liefern. Die konkrete Aussagekraft hängt von den vorhandenen Ereignistabellen und den darin gespeicherten Daten ab.

## Spezifische Kurzinformation

1. Dateiformat: SQLite, Dateiendung `.PLSQL`.
2. Die Datenbank enthält Ereignistabellen unterschiedlicher Systemkomponenten.
3. Neben der aktuellen Datenbank können archivierte Powerlog-Dateien vorhanden sein.
4. Ablageort:  
   **`/private/var/db/powerlog/Library/BatteryLife/CurrentPowerlog.PLSQL`**  
   Archiv: **`/private/var/db/powerlog/Library/BatteryLife/Archives/*.PLSQL.gz`**

## Referenzen

2026-10: <https://housekeeping101.github.io/sec-research-site/dfir--and--forensics/forensics/macos_forensics_framework_v1_9>

2026-10: <https://objectivebythesea.org/v8/talks/OBTS_v8_sEdwards.pdf>

## Tools

APOLLO - <https://github.com/mac4n6/APOLLO>

EffectivePower - <https://github.com/saagarjha/EffectivePower>