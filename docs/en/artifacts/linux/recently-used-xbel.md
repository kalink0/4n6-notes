---
title: "recently-used.xbel"
status: complete
completed: 2026-11-22
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-access]
---

# recently-used.xbel

## Meaning

recently-used.xbel is the list of a user's recently used files on the Linux desktop. Programs built on GTK (e.g. Nautilus, Document Viewer, LibreOffice, GIMP, Thunderbird) add a file when it is opened or saved through the program or selected in the file dialog; KDE programs write to the same file through KDE Frameworks. The format follows the freedesktop.org "Desktop Bookmarks" specification. File dialogs and file managers show their "Recent" view from it. An entry holds the file's address, its file type, timestamps and the programs that added the file, each with a count and the time of its last registration.

From a digital forensics perspective, an entry shows that a program registered the file at this address as used in the user account, when this first happened and when each of the listed programs last registered the file. The list can also contain files and programs that no longer exist on the system.

## Key facts

1. Availability: all Linux desktops with GTK programs (since GTK 2.10); KDE programs also write to it since KDE Frameworks 5.93
2. Prerequisites: enabled by default; can be turned off in GNOME in Settings (Privacy, File History), in KDE with `UseRecent=false` in the `RecentDocuments` group of **`~/.config/kdeglobals`**; with the history turned off, GTK empties the file on its next write, KDE deletes it
3. Retention: GTK keeps at most 1000 entries (since GTK 3.22.4 and 2.24.32) and beyond that removes the ones added first, regardless of when they were last used; KDE keeps at most 300 entries by default (`MaxEntries` in the same group) and removes those with the oldest `modified`; the limit of the program currently writing applies to all entries, including those of other programs; GTK also removes entries whose `modified` is older than the configured maximum age in days (GNOME default: unlimited; without a setting from the desktop environment, GTK default of 30 days); "Clear History" in GNOME Settings empties the file
4. Format and structure: XML in XBEL 1.0 format; per file a `bookmark` element with the address (`href`, also `smb://` and other locations besides `file://`), file type (`mime:mime-type`), optional groups (e.g. `Graphics`, `Totem`) and per program a `bookmark:application` element with name, launch command (`exec`), time (`modified`) and count (`count`); entries are in the order in which they were added
5. Timestamps: ISO 8601 in UTC with microseconds; `added` = first addition to the list; `modified` = last registration by any program; GTK sets `visited` only when adding the entry (then equal to `added`), KDE on every registration; `modified` on the program element = last registration by this program
6. Particularities and pitfalls: The program name is the name the program itself reports (e.g. `org.gnome.Nautilus`, `Document Viewer`, `python`); files selected through the file dialog of the GNOME portal (e.g. by Flatpak programs) are added by the portal under the name `xdg-desktop-portal-gnome`, the actual program is then not in the list; Flatpak and Snap programs that add entries themselves write to their own file in the app folder, Snap programs (except with classic confinement) per revision; on an update, snapd copies the data to the new revision, the folders of the retained older revisions (one by default) hold the state before the update; Nautilus adds files opened through it, even if the opened program does not write an entry itself; KDE does not add hidden files (path containing `/.`) or files in the temporary folder, and on writing removes hidden files that GTK added; GTK writes the file through a temporary file `recently-used.xbel.XXXXXX` (six random characters); if writing is interrupted, it remains with the state of that moment; GTK 2 before 2.24 stored the file as **`~/.recently-used.xbel`**, GTK 2.24 moves it to the new location on first access or merges it with a file already there
7. Location:  
   **`~/.local/share/recently-used.xbel`**  
   Flatpak programs: **`~/.var/app/{APP_ID}/data/recently-used.xbel`**  
   Snap programs: **`~/snap/{SNAP_NAME}/{REVISION}/.local/share/recently-used.xbel`**  
   GTK 2 before 2.24: **`~/.recently-used.xbel`**

## References

2026-11 (retrieved): <https://docs.gtk.org/gtk4/class.RecentManager.html>

2026-11 (retrieved): <https://help.gnome.org/users/gnome-help/stable/privacy-history-recent-off.html.en>

2023-03: <https://doi.org/10.1016/j.fsidi.2022.301498>

2018-05: <https://wiki.freedesktop.org/Specifications/desktop-bookmark-spec/>

## Tools

### Core tools

DLEAPP (parser: Recently Used Files (GTK)) - <https://github.com/abrignoni/DLEAPP>

Dissect (plugin: recently_used) - <https://docs.dissect.tools/>

Velociraptor (Exchange artifact: Linux.Forensics.RecentlyUsed) - <https://docs.velociraptor.app/>

TRACE - <https://github.com/Gadzhovski/TRACE-Forensic-Toolkit>

### Other tools

linuxthumbnailforensics (recentlyused.py) - <https://github.com/teescdf/linuxthumbnailforensics>
