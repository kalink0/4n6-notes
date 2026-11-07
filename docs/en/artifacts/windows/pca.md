---
title: "PCA - Program Compatibility Assistant"
status: reviewed
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: human
translation_of: de
reviewers: [dugeonlady]
reviewed: 2026-11-07
topics: [program-execution]
---

# PCA - Program Compatibility Assistant

## Meaning

The Program Compatibility Assistant is a feature in Windows systems that enables the execution of legacy software on the latest Windows systems.

From a digital forensics perspective, entries in PcaAppLaunchDic.txt show that the applications were last executed on the system at a certain time. They were started via the graphical user interface. A statement can be made about the location and the name of the application. The PcaGeneralDb files additionally log events such as abnormal program terminations or blocked drivers; their meaning depends on the entry type.

## Key facts

1. Availability: exists starting with Windows 11, 22H2
2. Retention: PcaGeneralDb0/1 rotate at 2 MB each (2–4 MB history)
3. Format and structure: regular text files, pipe-delimited format
4. Timestamps: UTC; PcaAppLaunchDic.txt contains the time of the last execution
5. Particularities and pitfalls: only GUI-based applications or applications started from the GUI. PcaAppLaunchDic.txt is ANSI-encoded: following a path with non-ANSI characters, no new programs are recorded. Paths in PcaGeneralDb are normalised (lower case, no drive letter, usernames replaced).
6. Location:  
   **`C:\Windows\appcompat\pca\PcaAppLaunchDic.txt`**  
   **`C:\Windows\appcompat\pca\PcaGeneralDb0.txt`**  
   **`C:\Windows\appcompat\pca\PcaGeneralDb1.txt`**

## References

2024-05: <https://www.sygnia.co/blog/new-windows-11-pca-artifact/>

2023-07: <https://aboutdfir.com/new-windows-11-pro-22h2-evidence-of-execution-artifact/>

2023-01: <https://www.youtube.com/watch?v=rV8aErDj06A>

## Tools

Program Compatibility Parser - <https://github.com/kacos2000/Win10/tree/master/ProgramCompatibility>

PCAParser - <https://github.com/AndrewRathbun/PCAParser>
