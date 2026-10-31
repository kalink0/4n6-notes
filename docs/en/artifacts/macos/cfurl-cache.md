---
title: "CFURL Cache"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [web-activity]
---

# CFURL Cache

## Meaning

Programs that retrieve data via the standard macOS network interfaces store the servers' responses in a cache. This way, repeated requests can be answered faster and without a new transfer. Each program has its own database (Cache.db) with the retrieved URL, the time and the stored requests and responses; larger responses are stored as individual files in the folder fsCachedData.

From a digital forensics perspective, an entry shows that the program retrieved the URL at the stored time. It does not show that the retrieval was triggered by the user or that the content was displayed to the user.

## Key facts

1. The retrieving program follows from the folder name (bundle ID) of the cache
2. Whether a response is stored as a file in fsCachedData is shown in Cache.db by the column `isDataOnFS` of the table `cfurl_cache_response`
3. Stored requests and responses can contain headers with session cookies and tokens
4. Timestamps of the database in UTC; the timestamp in the stored response object sometimes differs from it
5. The cache size is limited; programs can delete entries themselves or set a different location
6. Location:  
   **`/Users/{USER}/Library/Caches/{BUNDLE_ID}/Cache.db`**  
   **`/Users/{USER}/Library/Caches/{BUNDLE_ID}/fsCachedData/`**  
   Sandboxed programs: **`/Users/{USER}/Library/Containers/{BUNDLE_ID}/Data/Library/Caches/{BUNDLE_ID}/`**

## References

2026-10 (accessed): <https://developer.apple.com/documentation/foundation/urlcache>

2022-12: <https://trustedsec.com/blog/looting-ios-apps-cache-db>

2008-10: <https://dreness.com/blog/archives/73>

## Tools

DLEAPP (parser: App URL Cache) - <https://github.com/abrignoni/DLEAPP>

mac_apt (plugin: CFURLCACHE) - <https://github.com/ydkhatri/mac_apt>

Velociraptor (artifact: MacOS.Applications.Cache) - <https://docs.velociraptor.app/exchange/artifacts/pages/macos.applications.cache>
