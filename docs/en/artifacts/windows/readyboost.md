---
title: "EMDMgmt - ReadyBoost"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [external-devices]
---

# EMDMgmt - ReadyBoost

## Meaning

EMDMgmt (External Memory Device Management) is the registry key of the ReadyBoost service. ReadyBoost uses external flash memory as an additional cache. When a drive is connected, the service tests its suitability and stores the result together with information about the drive, regardless of whether ReadyBoost is actually used.

From a digital forensics perspective, an entry shows that a drive with the given device and volume information was connected to the system. It does not show the time of connection.

## Key facts

1. Since Windows Vista; on Windows 11 ReadyBoost is hidden, but according to Microsoft still present
2. Populated even if ReadyBoost is not used; on systems with an SSD the key may be missing because ReadyBoost is then disabled
3. Besides USB drives, also records eSATA, FireWire and local non-system drives
4. One subkey per device; the name contains manufacturer, product, device serial number, volume label (if present) and volume serial number
5. The LastWrite times of the subkeys do not correspond to the connection of the drive
6. Location:  
   **`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\EMDMgmt`**

## References

2024-01: <https://artefacts.help/windows_registry_usb_activity.html>

2023-08: <https://learn.microsoft.com/en-us/answers/questions/415341/readyboost-what-data-is-cached>

2022-05: <https://windowsir.blogspot.com/2022/05/usb-devices-redux.html>

2013-08: <https://www.hecfblog.com/2013/08/daily-blog-65-understanding-artifacts.html>

2013-04: <https://windowsir.blogspot.com/2013/04/plugin-emdmgmt.html>

2012-02: <https://windowsir.blogspot.com/2012/02/howto-usb-thumb-drives.html>

## Tools

RegRipper (plugin: emdmgmt) - <https://github.com/keydet89/RegRipper4.0>

usb-forensic - <https://github.com/SecurityRonin/usb-forensic>
