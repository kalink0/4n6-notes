---
title: "Jailbreak"
status: complete
completed: 2026-10-31
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Jailbreak

A jailbreak removes the security restrictions of iOS or iPadOS, so that code without Apple's signature can be run with root privileges.

A jailbreak exploits security vulnerabilities in the operating system or in the device's boot chain. Vulnerabilities in the boot ROM (e.g. checkm8 on devices up to the A11 chip) cannot be fixed by an update. Depending on the type, the jailbreak has to be run again after every restart. Afterwards, access to the entire file system, a root shell and the installation of extensions (tweaks) via package managers such as Cydia or Sileo are possible. Newer jailbreaks (rootless, since iOS 15) do not modify the system volume but store their files under **`/var/jb`**.

From a digital forensics perspective, a jailbreak modifies the system. Traces of a jailbreak are, for example, installed package managers or the folder **`/var/jb`**. On a jailbroken device, more extensive access is possible, e.g. to the entire file system, as long as the jailbreak is active.
