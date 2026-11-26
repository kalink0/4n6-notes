---
title: "Prefetch"
status: reviewed
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: human
translation_of: de
reviewers: [dugeonlady]
reviewed: 2026-11-26
topics: [program-execution]
---

# Prefetch

## Meaning

The Windows operating system creates so-called prefetch files. These files contain at least the last execution of a program, the number of executions and the libraries and files loaded at startup. Timestamps of up to 7 further program executions are also included if available. The operating system uses these prefetch files to take technical measures to decrease application startup times and thus improve the user experience.

From a digital forensics perspective, the existence and content of a prefetch file shows that a referenced application was started on the system at the given times. In addition, it shows which libraries and files are used when the application starts.

## Key facts

1. Availability: up to Windows 8, 128 files stored; starting with Windows 8, 1024 files stored
2. Prerequisites: Enabled by default; can be disabled via **`HKLM\SYSTEM\{CURRENT_CONTROL_SET}\Control\Session Manager\Memory Management\PrefetchParameters\EnablePrefetcher`**; sometimes not active on servers
3. Format and Structure: Compressed since Windows 10 (MAM), not directly readable
4. Timestamps: as FILETIME in UTC
5. Particularities and pitfalls: The first execution follows from the creation date of the .pf file -> the file is written approx. 10 seconds after the start; the file name contains a hash of the program path; the same program from different paths results in separate files
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

### Core tools

DLEAPP (parser: Prefetch, Prefetch Files Loaded) - <https://github.com/abrignoni/DLEAPP>

Dissect (plugin: prefetch) - <https://docs.dissect.tools/en/stable/plugins/prefetch.html>

Velociraptor (artifact: Windows.Forensics.Prefetch) - <https://docs.velociraptor.app/>

PECmd - <https://ericzimmerman.github.io/>

TRACE - <https://github.com/Gadzhovski/TRACE-Forensic-Toolkit>

### Other tools

artemis - <https://github.com/puffycid/artemis>

juntei (parse-file prefetch) - <https://github.com/Yamato-Security/juntei>

Plaso (parser: prefetch) - <https://github.com/log2timeline/plaso>

Windows-Prefetch-Parser - <https://github.com/PoorBillionaire/Windows-Prefetch-Parser> (old versions only)

WinPrefetchView - <https://www.nirsoft.net/utils/win_prefetch_view.html>
