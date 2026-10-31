---
title: "eSIM"
status: complete
completed: 2026-10-31
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# eSIM

An eSIM (embedded SIM) is a SIM chip permanently built into the device (eUICC) onto which mobile network profiles are downloaded instead of being provided on a removable SIM card.

A profile contains the same data as a SIM card, including the IMSI and ICCID; the ICCID identifies the profile, not the chip. The chip itself has its own 32-digit identifier, the EID (eUICC Identifier). An eSIM can store several profiles, one or more of which are active. Profiles are installed, for example, via a QR code or an app of the mobile network operator.

From a digital forensics perspective, an eSIM cannot be removed like a SIM card and read separately from the device with a SIM card reader. The EID is shown in the device settings and is often also printed on the device's packaging.
