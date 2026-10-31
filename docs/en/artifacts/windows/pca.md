---
title: "PCA - Program Compatibility Assistant"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution]
---

# PCA - Program Compatibility Assistant

## Meaning

The Program Compatibility Assistant is a feature in Windows systems that ensures older programs can run on the latest Windows systems.

From a digital forensics perspective, entries in PcaAppLaunchDic.txt mean that the applications were last executed on the system at the given time. They were started via the graphical user interface. A statement can be made about the location and the name of the application. The PcaGeneralDb files additionally log events such as abnormal program terminations or blocked drivers; their meaning depends on the entry type.

## Key facts

1. Availability: exists since Windows 11, 22H2
2. Retention: PcaGeneralDb0/1 rotate at 2 MB each (2–4 MB history)
3. Format and structure: regular text files, pipe-delimited format
4. Timestamps: UTC; in PcaAppLaunchDic.txt the time of the last execution
5. Special features and pitfalls: only GUI-based applications or applications started from the GUI. PcaAppLaunchDic.txt is ANSI-encoded: after a path with non-ANSI characters, no new programs are recorded. Paths in PcaGeneralDb are normalised (lower case, without drive letter, user names replaced).
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
