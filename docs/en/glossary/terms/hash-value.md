---
title: "Hash Value"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Hash Value

A hash value is a fixed-length string calculated from arbitrary data using a defined calculation method (hash function), which identifies this data like a fingerprint.

Identical data always results in the same hash value; changing even a single bit leads to a completely different one. The original data cannot be calculated back from the hash value. Hash functions commonly used in forensics are MD5, SHA-1 and SHA-256.
From a digital forensics perspective, hash values serve two purposes. First, they prove that an acquisition is unchanged: the hash value is calculated and documented during the acquisition; if it matches in a later check, the data has not been changed. For acquisitions that cannot be repeated identically, e.g. of running systems or mobile devices, it only proves that the acquisition file is unchanged, not that it matches the original. Second, files can be identified by their hash value and compared against lists of known files, e.g. to hide known system files or to detect known illegal content (whitelist/blacklist). A differing hash value only shows that data differs, not by how much.