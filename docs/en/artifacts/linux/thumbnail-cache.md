---
title: "Thumbnail Cache"
status: complete
completed: 2026-11-22
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-existence]
---

# Thumbnail Cache

## Meaning

The thumbnail cache is a user's shared store for preview images (thumbnails) on the Linux desktop. File managers such as Nautilus, Dolphin or Thunar and other programs, e.g. image viewers, create a thumbnail when they show a file with a preview, for instance when a folder is opened, and store it there so it does not have to be computed again next time. Structure and storage follow the freedesktop.org "Thumbnail Managing Standard" specification, so GNOME, KDE and XFCE programs use the same cache. Each thumbnail is a PNG file whose name is derived from the address of the original file and which contains this address and the original file's modification time.

From a digital forensics perspective, a thumbnail shows that a file with this content existed at the stored address and that a program in the user account showed it with a preview, e.g. when the folder was opened in the file manager. In GNOME and KDE, thumbnails remain when the original file is deleted or moved; they then also show the content, name and path of files that no longer exist.

## Key facts

1. Availability: all Linux desktops whose programs follow the specification (GNOME, KDE, XFCE and others); the `x-large` and `xx-large` sizes since version 0.9.0 of the specification (2020)
2. Prerequisites: previews are enabled by default in Nautilus and Dolphin; by default, Nautilus creates no thumbnails for files on network shares and for images over 50 MB, but does for files on USB drives and smartphones connected via MTP; by default, KDE creates no thumbnails for files in remote locations (`MaximumRemoteSize` = 0) and since KDE Frameworks 5.57 stores none for files on another encrypted drive as long as the cache itself is not on an encrypted location; GNOME does not check this, so thumbnails of files from encrypted containers can be stored unencrypted in the cache
3. Retention: GNOME deletes thumbnails that have not been read for 180 days (since GNOME 3.36 by access time, before that by the PNG file's modification time) and beyond that the oldest ones when the cache exceeds 512 MB; the check runs shortly after login and then daily, `x-large` and `xx-large` are only cleaned since GNOME 45; KDE and XFCE do not clean the cache by age or size; neither GNOME nor KDE checks whether the original file still exists; Thunar (XFCE) deletes the thumbnail when it deletes a file permanently, on moving to the trash it remains; a thumbnail is replaced when the original file's modification time or size changes
4. Format and structure: PNG files in folders per size: `normal` (up to 128 pixels), `large` (256), `x-large` (512), `xx-large` (1024); file name = MD5 hash of the original file's full address (e.g. `file:///home/…/picture.jpg`, special characters URL-encoded) with extension `.png`; text fields in the PNG file: `Thumb::URI` (address), `Thumb::MTime` (original file's modification time), optionally `Thumb::Size`, `Thumb::Mimetype`, `Thumb::Image::Width`/`Height`, `Thumb::Document::Pages`, `Thumb::Movie::Length` and `Software` (creating program, e.g. `GNOME::ThumbnailFactory`, `KDE Thumbnail Generator`); in the `fail` folder, per program, empty PNG files with address and modification time for files for which no thumbnail could be created
5. Timestamps: `Thumb::MTime` in seconds since 1970-01-01 (UTC) = original file's modification time when the thumbnail was created; the PNG file's modification time = time the thumbnail was created, as it is not modified but always written anew
6. Particularities and pitfalls: folders and files have permissions 700 and 600; when a file is renamed or moved in GNOME or KDE, a new thumbnail is created under the new name and the old one remains; Thunar moves the thumbnail along; from a known path the thumbnail's name can be computed to check whether a thumbnail exists for a file; folders with their own thumbnails, e.g. on media, contain a `.sh_thumbnails` subfolder that is only read and stores addresses relative to this folder (`./picture.jpg`); before version 0.8.0 of the specification (2012) the cache was located under **`~/.thumbnails`**
7. Location:  
   **`~/.cache/thumbnails/{normal|large|x-large|xx-large}/{MD5}.png`**  
   Failed thumbnails: **`~/.cache/thumbnails/fail/{PROGRAM}/{MD5}.png`**  
   Older location: **`~/.thumbnails/`**

## References

2023-03: <https://doi.org/10.1016/j.fsidi.2022.301498>

2020-12: <https://specifications.freedesktop.org/thumbnail/latest/>

## Tools

DLEAPP (parser: Thumbnail Cache (freedesktop)) - <https://github.com/abrignoni/DLEAPP>
