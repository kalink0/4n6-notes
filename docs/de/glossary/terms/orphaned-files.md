---
title: "Orphaned Files"
status: complete
completed: 2026-10-21
authors: [kalink0 (Marco Neumann)]
---

# Orphaned Files

Sogenannte Orphaned Files sind Dateien, die physisch auf dem Datenträger noch vorhanden sind, jedoch keine gültige Verknüpfung im Verzeichnisbaum mehr besitzen. Dies bedeutet, dass sie für einen Nutzer über das Dateisystem nicht mehr zugreifbar sind. Für Orphaned Files können aber, im Gegensatz zu beispielsweise Dateien im Unallocated Space, noch teilweise Metadaten vorliegen. Zum Beispiel können Zeitstempel zur Erstellung/Modifizierung oder der Dateiname noch vorliegen. Ebenfalls können ggf. Aussagen zum vorherigen Ablageort der Datei im Dateisystem getroffen werden.

Zu Orphaned Files kann es z. B. kommen, wenn der übergeordnete Ordner gelöscht und dessen Eintrag im Dateisystem überschrieben wurde, sowie durch Abstürze des Systems oder unsaubere Löschvorgänge.