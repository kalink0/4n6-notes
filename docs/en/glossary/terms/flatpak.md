---
title: "Flatpak"
status: complete
completed: 2026-11-22
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Flatpak

Flatpak is a package format and distribution system for Linux desktop programs, in which programs are installed together with shared runtime environments (runtimes) independently of the distribution's packages and run in a sandbox.

Programs are installed from sources (remotes), mostly from Flathub, and carry a unique identifier whose leading part identifies the developer (e.g. `org.mozilla.firefox`). An installation can be system-wide for all users or for a single user only. Flatpak stores programs and runtimes in a local repository based on OSTree, which versions content similar to Git. The sandbox (bubblewrap) restricts access to files and devices; a program gets access to files outside it through permissions or through portals, e.g. the desktop's file dialog.

From a digital forensics perspective, Flatpak programs do not store their settings, data and caches in the usual locations in the home folder but in a separate folder per program. What a program opens through a portal may be logged by the desktop under the portal's name instead of the program's name.

- Program data per user: **`~/.var/app/{APP_ID}/`** with the subfolders `config`, `data` and `cache`
- System-wide installation: **`/var/lib/flatpak/`**
- Per-user installation: **`~/.local/share/flatpak/`**
