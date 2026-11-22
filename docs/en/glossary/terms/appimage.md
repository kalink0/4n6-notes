---
title: "AppImage"
status: complete
completed: 2026-11-22
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# AppImage

AppImage is a format in which a Linux program is packaged with all the libraries it needs in a single executable file that is started directly without installation.

The file consists of a runtime, the executable part, and an appended file system image (SquashFS). On start, the runtime mounts the image read-only through FUSE in a temporary folder for as long as the program runs. AppImages are not managed by a package manager; the file can be located anywhere, e.g. in the downloads folder.

From a digital forensics perspective, an AppImage does not appear in the package manager; the program can only be traced through the file itself. Unlike Snap and Flatpak, it does not run in a sandbox and writes its data to the usual locations in the home folder. The mount folder only exists while the program runs; its name contains the first six characters of the file name and six random characters.

- Mount folder during execution: **`/tmp/.mount_{NAME}XXXXXX`** (or under `$TMPDIR`, if set)
