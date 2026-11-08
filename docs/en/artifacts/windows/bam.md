---
title: "BAM - Background Activity Moderator"
status: reviewed
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: human
translation_of: de
reviewers: [dugeonlady]
reviewed: 2026-11-06
topics: [program-execution]
---

# BAM - Background Activity Moderator

## Meaning

The BAM is a Windows service that monitors and controls background processes. It is being used to optimise performance and energy consumption. The BAM is stored per user identified by the corresponding SID. The executable's path and the last execution time are being recorded. Data is stored for 7 days and then automatically deleted by the system.

From a digital forensics perspective, BAM entries show that an application was executed in the context of a certain user account at a given point in time.

## Key facts

1. Availability: introduced with Windows 10 - update 1709
2. Retention: the data is available for approx. 7 days.
3. Particularities and pitfalls: applications started in the terminal are NOT logged. Applications started from external media (e.g. USB sticks, network drives) are NOT logged.
4. Location (registry):  
   Starting with Windows 10 1809: **`HKLM\SYSTEM\{CURRENT_CONTROL_SET}\Services\bam\State\UserSettings\{USER_SID}`**  
   Windows 10 1709/1803: **`HKLM\SYSTEM\{CURRENT_CONTROL_SET}\Services\bam\UserSettings\{USER_SID}`**

## References

2026-07: <https://www.it-connect.tech/forensic-windows-part-5-analyzing-bam-and-dam/>

2024-08: <https://github.com/Psmths/windows-forensic-artifacts/blob/main/execution/bam-dam.md>

## Tools

### Core tools

DLEAPP (parser: Background and Desktop Activity Moderator) - <https://github.com/abrignoni/DLEAPP>

Dissect (plugin: bam) - <https://docs.dissect.tools/>

Velociraptor (artifact: Windows.Forensics.Bam) - <https://docs.velociraptor.app/>

Registry Explorer - <https://ericzimmerman.github.io/>

TRACE - <https://github.com/Gadzhovski/TRACE-Forensic-Toolkit>

### Other tools

juntei (parse-registry bam) - <https://github.com/Yamato-Security/juntei>

Plaso (parser: bam) - <https://github.com/log2timeline/plaso>

regipy (plugin: background_activity_moderator) - <https://github.com/mkorman90/regipy>

RegRipper (bam) - <https://github.com/keydet89/RegRipper4.0>
