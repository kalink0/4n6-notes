---
title: "Snap"
status: complete
completed: 2026-11-22
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Snap

Snap is a package format and distribution system for Linux programs by Canonical, in which a program is packaged with the libraries it needs in a read-only file system image (SquashFS) and runs independently of the distribution's packages.

Snaps are installed through the snapd service, mostly from the Snap Store, and are updated automatically by default (up to four times a day). Each version of a snap is a revision; snapd mounts the image of each revision in its own folder. Most snaps run isolated from the rest of the system (strict confinement) and only get access to granted interfaces; snaps with classic confinement run without this isolation. Snap is preinstalled on Ubuntu.

From a digital forensics perspective, confined snaps do not store their data in the usual locations in the home folder but in a separate folder per snap and revision. On an update, snapd copies the data to the new revision; the folders of older revisions that snapd still retains hold the state before the update. Data shared by all revisions is in the `common` folder.

- Program files: **`/var/lib/snapd/snaps/{SNAP_NAME}_{REVISION}.snap`**, mounted under **`/snap/{SNAP_NAME}/{REVISION}`** (on some distributions **`/var/lib/snapd/snap`**)
- User data: **`~/snap/{SNAP_NAME}/{REVISION}`**, **`~/snap/{SNAP_NAME}/common`**
- System data: **`/var/snap/{SNAP_NAME}/{REVISION}`**, **`/var/snap/{SNAP_NAME}/common`**
