---
title: "Hash Collision"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Hash Collision

A hash collision occurs when two different pieces of data result in the same hash value.

Since a hash value has a fixed length but there is an unlimited number of possible data, such collisions inevitably exist for every hash function. A hash function is considered secure as long as they cannot be found deliberately with reasonable effort. Attacks on hash functions are divided into two types. In a collision attack, the attacker creates two files themselves and modifies both until they have the same hash value; they cannot determine which hash value results. For MD5, such attacks have been practically possible since 2004, for SHA-1 since 2017. Meanwhile, the attacker can freely choose the beginning of both files (chosen-prefix collision), but the data blocks inserted for the collision look random. In a preimage attack, by contrast, a hash value is given, and the attacker searches for data that results in exactly this hash value. If a file is given for which a second one with the same hash value is to be found, this is called a second preimage attack. No practically feasible preimage attack is known for MD5 or SHA-1; the best known attack on MD5 requires about 2^123 computation steps and is therefore not feasible.

From a digital forensics perspective, a second preimage attack would be required to replace an acquisition unnoticed or to modify a file so that it takes on the hash value of a known, unsuspicious file, since in these cases the file and its hash value are already fixed. The known collisions in MD5 and SHA-1 therefore do not call into question the verification of acquisitions or the identification of files by their hash value. A collision attack is only relevant where someone was able to create both files themselves before their hash value was recorded, e.g. if a harmless file is added to a list of known files and later replaced with the second, prepared file.