---
title: "MSISDN"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# MSISDN

The MSISDN (Mobile Station International Subscriber Directory Number) is the phone number of a mobile subscription in international format.

In the mobile operator's network, the MSISDN is assigned to the subscriber's IMSI. It is not necessarily stored on the SIM card or in the eSIM profile, so a device does not always display its own phone number. Because of number portability, the MSISDN does not reliably indicate the current mobile operator.

Structure (max. 15 digits according to ITU-T E.164):

- **CC (Country Code):** country calling code (e.g. 49 = Germany)
- **NDC (National Destination Code):** network prefix (e.g. 151)
- **SN (Subscriber Number):** subscriber number
