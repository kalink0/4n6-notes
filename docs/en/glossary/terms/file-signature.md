---
title: "File signature (magic bytes)"
status: complete
completed: 2026-10-31
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# File signature (magic bytes)

A file signature (magic bytes) is a fixed byte sequence, usually at the beginning of a file, by which the file format can be recognised.

Examples are `FF D8 FF` for JPEG, `89 50 4E 47` (`‰PNG`) for PNG, `25 50 44 46` (`%PDF`) for PDF and `50 4B 03 04` (`PK`) for ZIP. Some formats also have an end signature, e.g. `FF D9` at the end of a JPEG file. Formats based on ZIP (e.g. DOCX, XLSX, APK) have the same signature as ZIP and can only be told apart by their content. Not every format has a signature, e.g. plain text.

From a digital forensics perspective, the signature can be used to determine the actual file type independently of the file name and the file extension, e.g. for renamed files. In carving, start and end signatures are used to find files in unallocated space.
