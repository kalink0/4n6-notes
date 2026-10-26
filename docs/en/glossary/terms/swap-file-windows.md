---
title: "Swap File (Windows)"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Swap File (Windows)

Since Windows 8 there has been a swap file in Windows operating systems. It has a similar function to the pagefile on Windows and is a hidden system file, usually in the root directory of the system drive, named *swapfile.sys*.

This file is used specifically for efficiently paging out data of so-called UWP (Universal Windows Platform) applications. These applications use the latest programming interfaces and libraries in Windows and are intended to offer the user a uniform experience across all Windows systems. UWP applications are mostly distributed via the Windows Store.

The swap file potentially contains data on open apps and their content. Further content of the swap file depends on how the apps are programmed.
