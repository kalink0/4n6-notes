---
title: "File-Based Encryption (FBE)"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# File-Based Encryption (FBE)

With file-based encryption (FBE), each file is encrypted with its own key.

The key of a file, or the information from which it is derived, is stored in the file's metadata in the file system and is itself protected by a higher-level key. Besides the file content, the file names are also encrypted, depending on the implementation.

From a digital forensics perspective, recovering deleted files is generally not possible: when a file is deleted, its key is lost as well, so data found e.g. through carving can no longer be decrypted. Examples are the encryption of Android (since Android 7, from Android 10 a requirement for certification by Google; uncertified devices can also be unencrypted) and of iOS/iPadOS (Data Protection) as well as fscrypt on Linux.
