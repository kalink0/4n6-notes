---
title: "BAM - Background Activity Moderator"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution]
---

# BAM - Background Activity Moderator

## Meaning

The BAM is a Windows service that monitors and controls background processes. The aim is to optimise performance and energy consumption. The data is deleted by the system after 7 days. For the user, the associated SID is stored. The path of the executable and the time of the last execution are stored.

From a digital forensics perspective, BAM entries mean that an application was executed in the context of the user account at the given time.

## Key facts

1. Availability: introduced with Windows 10 - update 1709
2. Retention: the data is available for approx. 7 days.
3. Special features and pitfalls: applications started in the terminal are NOT logged. Applications started from external media (e.g. USB sticks, network drives) are NOT logged.
4. Location (registry):  
   from Windows 10 1809: **`HKLM\SYSTEM\{CURRENT_CONTROL_SET}\Services\bam\State\UserSettings\{USER_SID}`**  
   Windows 10 1709/1803: **`HKLM\SYSTEM\{CURRENT_CONTROL_SET}\Services\bam\UserSettings\{USER_SID}`**

## References

2026-07: <https://www.it-connect.tech/forensic-windows-part-5-analyzing-bam-and-dam/>

2024-08: <https://github.com/Psmths/windows-forensic-artifacts/blob/main/execution/bam-dam.md>

## Tools

RegRipper (bam) - <https://github.com/keydet89/RegRipper4.0>

Registry Explorer - <https://ericzimmerman.github.io/>

Velociraptor (Windows.Forensics.Bam) - <https://docs.velociraptor.app/>
