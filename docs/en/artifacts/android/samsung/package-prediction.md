---
title: "Samsung Package Prediction"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de:sha256:501494b1f8f5
topics: [program-execution, installed-software]
---

# Samsung Package Prediction

## Meaning

Samsung Package Prediction is a system service that monitors when a user opens an app and which three apps they opened before. It also stores data on the current screen orientation, Bluetooth and Wi-Fi connection status and which user runs the app. To a certain extent, it also stores which function was used/called in the respective app - e.g. contact list or message list.

The aim is to give the device user a smoother experience by predicting, on the basis of this data, what the user wants to open next, offering it to them if appropriate and speeding up the call.

From a digital forensics perspective, the entries mean that the app in the column "running_pkg" was run on the device by the given user at the given time. This app must therefore have been installed on the device at that time.

## Key facts

1. The data goes back a long time - current data → 6 months - not yet conclusively validated.
2. Timestamps: Unix time in milliseconds (UTC)
3. Location:  
   **`/data/system/PkgPredictions.db`**

## References

2025-11: <https://blog.digital-forensics.it/2025/11/beyond-known-call-to-forensic-research.html>

2023-12: <https://blog.digital-forensics.it/2023/12/has-user-ever-used-xyz-application-aka.html>

## Tools

ALEAPP (parser: pkgPredictions) - <https://github.com/abrignoni/ALEAPP>
