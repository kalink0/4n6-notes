---
title: "SRUM - System Resource Utilization Monitor"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution, network]
---

# SRUM - System Resource Utilization Monitor

## Meaning

The System Resource Utilization Monitor is a feature in modern Windows operating systems. It serves to monitor information on executed programs and their resource usage. Among other things, information on network usage (amount of data, networks used, network adapters used), system usage (file path, CPU usage, amount of data) and the user account used is stored.

From a digital forensics perspective, SRUM entries provide information about executed programs, their resource consumption and which user account executed the program. The accuracy of the execution is 60 minutes by default. A listed program was therefore active with the given data in the period and with the user account. For the time window, the corresponding resources (e.g. amount of data uploaded) are given.

## Key facts

1. Available from Windows 8
2. The time window for creating entries is 60 minutes by default - a more precise statement about resource usage is therefore not possible
3. Retention is about 30 - 60 days.
4. Information is not written to the database IMMEDIATELY. Data not yet written is held in the registry. The registry serves as temporary storage.
5. Location:  
   Temporary (registry): **`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SRUM`**  
   Persisted: **`C:\Windows\System32\sru\SRUDB.dat`**

## References

2026-09: <https://www.it-connect.tech/windows-forensics-part-12-analyzing-srum/>

2026-02: <https://www.cyberengage.org/post/unpacking-srum-the-digital-forensics-goldmine-in-windows>

2022-10: <https://www.magnetforensics.com/blog/srum-forensic-analysis-of-windows-system-resource-utilization-monitor/>

2019-12: <https://docs.velociraptor.app/blog/2019/2019-12-31_digging-into-the-system-resource-usage-monitor-srum-afbadb1a375/>

## Tools

SrumECmd - <https://ericzimmerman.github.io/>

Srum dump - <https://github.com/MarkBaggett/srum-dump>

ESE Database View - <https://www.nirsoft.net/utils/ese_database_view.html>

DLEAPP (parser: SRUM Network Usage, SRUM Application Resource Usage, SRUM Network Connections) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (artifact: Windows.Forensics.SRUM) - <https://docs.velociraptor.app/artifact_references/pages/windows.forensics.srum/>

Dissect (plugin: sru) - <https://docs.dissect.tools/en/stable/plugins/sru.html>
