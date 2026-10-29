---
title: "Samsung Quick Share"
status: complete
completed: 2026-10-29
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [data-transfer]
---

# Samsung Quick Share

## Meaning

Quick Share is a feature for transferring photos, videos and other files to nearby devices over Wi-Fi and Bluetooth. It originally comes from Samsung; since 2024, the Google variant in Play services (previously Nearby Share) on other Android devices is also called Quick Share. On Galaxy devices, the Samsung Quick Share app logs which files were sent and received and which devices a connection was established with. Transfers via Private Share, where the recipient can only view the content until an expiration date but cannot save or forward it, are stored in a separate database.

From a digital forensics perspective, the entries show that a specific file was sent or received via Quick Share and that the device was connected to a device with the logged name. Cancelled and failed transfers can also be identified.

## Key facts

1. Samsung Galaxy devices
2. Prerequisite for transfers: Wi-Fi and Bluetooth enabled; the receive setting (No one, Contacts, Everyone) determines who can send to the device
3. Private Share content is deleted on the recipient's device after expiration (2 days by default, just under 7 days at most)
4. SQLite databases: `linkShare.db` (Quick Share), `privacy_library_database.db` (Private Share)
5. Since One UI 8.5 also compatible with AirDrop (initially Galaxy S26, as of 2026-03)
6. Location:  
   **`/data/data/com.samsung.android.app.sharelive/databases/linkShare.db`**  
   **`/data/data/com.samsung.android.app.sharelive/databases/privacy_library_database.db`**

## References

2026-10: <https://www.gmdsoft.com/blog/gmdsoft-tech-letter-vol-22-quick-share-history-analysis-amid-expanding-device-and-os-support/>

## Tools

*No content yet.*
