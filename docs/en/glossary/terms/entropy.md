---
title: "Entropy"
status: complete
completed: 2026-10-31
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Entropy

Entropy is a measure of the randomness or information content of data.

In digital forensics, Shannon entropy in bits per byte is usually used, with values between 0 (e.g. only null bytes) and 8 (completely random data). Plain text is usually around 4 to 5, compressed and encrypted data close to 8. It is calculated for a whole file or block by block for sections of a storage device.

From a digital forensics perspective, high entropy indicates encrypted or compressed data. The two cannot be told apart by entropy alone; compressed formats (e.g. ZIP, JPEG), however, usually have a file signature, encrypted containers (e.g. VeraCrypt) do not.
