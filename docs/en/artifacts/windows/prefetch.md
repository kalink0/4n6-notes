---
title: "Prefetch"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution]
---

# Prefetch

## Meaning

The Windows operating system creates so-called prefetch files. These files contain at least the last execution of a program, the number of executions and the libraries and files loaded at startup. In addition, up to 7 further times of program executions can be included. The benefit of these prefetch files is that the operating system can take technical measures to enable applications to start faster and thus improve the user experience.

From a digital forensics perspective, the existence and content of a prefetch file mean that a referenced application was started on the system at the given times. In addition, it can be said which libraries and files are used when the application starts.

## Key facts

1. Can be disabled via **`HKLM\SYSTEM\{CURRENT_CONTROL_SET}\Control\Session Manager\Memory Management\PrefetchParameters\EnablePrefetcher`**; sometimes not active on servers
2. Since Windows 8 a maximum of 1024 files, before that 128
3. Compressed since Windows 10 (MAM), not directly readable
4. Timestamps as FILETIME in UTC
5. The first execution follows from the creation date of the .pf file; the file is written approx. 10 seconds after the start
6. The file name contains a hash of the program path; the same program from different paths results in separate files
7. Location:  
   **`C:\Windows\Prefetch\*.pf`**

## References

2026-07: <https://github.com/libyal/libscca/blob/main/documentation/Windows%20Prefetch%20File%20(PF)%20format.asciidoc>

2025-12: <https://y0sh1mitsu.github.io/posts/how-are-prefetch-created/>

2023-07: <https://trustedsec.com/blog/prefetch-the-little-snitch-that-tells-on-you>

2022-10: <https://isc.sans.edu/diary/Forensic+Value+of+Prefetch/29168/>

2015-06: <https://blog.digital-forensics.it/2015/06/a-first-look-at-windows-10-prefetch.html>

2013-09: <https://www.hecfblog.com/2013/09/daily-blog-72-understanding-artifacts.html>

2026-10 (accessed): <https://forensics.wiki/prefetch/>

## Tools

PECmd - <https://ericzimmerman.github.io/>

WinPrefetchView - <https://www.nirsoft.net/utils/win_prefetch_view.html>

DLEAPP (parser: Prefetch, Prefetch Files Loaded) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (artifact: Windows.Forensics.Prefetch) - <https://docs.velociraptor.app/artifact_references/pages/windows.forensics.prefetch>

Dissect (plugin: prefetch) - <https://docs.dissect.tools/en/stable/plugins/prefetch.html>
