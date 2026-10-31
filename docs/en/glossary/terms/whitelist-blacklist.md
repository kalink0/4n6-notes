---
title: "Whitelist / Blacklist"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Whitelist / Blacklist

A whitelist or blacklist is a list of entries, e.g. files, IP addresses, websites or ports, that are classified as permitted or harmless (whitelist) or as not permitted or relevant (blacklist).

Whitelists and blacklists are used e.g. in firewalls, proxies or email filters to allow or block connections or content. The lists are also referred to as allowlist/blocklist or known-good/known-bad.

In the digital forensic context, mainly lists of hash values are used, against which files are compared. A whitelist (e.g. NIST's NSRL with files from operating systems and standard software) reduces the amount of data to be reviewed, since known harmless files can be hidden. A blacklist (e.g. known malware or already known illegal material) allows known files to be found quickly. Even a minimal change to a file results in a different hash value, so modified files are not detected.
