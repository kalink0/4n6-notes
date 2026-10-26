---
title: "IMEI"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# IMEI

The IMEI (International Mobile Equipment Identity) is the unique serial number of a mobile device. The IMEI is assigned per SIM slot - there is one IMEI per SIM slot (including eSIM).

The IMEI can be used to identify devices.

Structure:

- **TAC (Type Allocation Code, 8 digits):** device type/manufacturer
- **SNR (Serial Number, 6 digits):** individual device identifier
- **Check digit (1 digit):** check digit according to the Luhn algorithm
