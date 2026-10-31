---
title: "FSCachedData"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [web-activity]
---

# FSCachedData

## Meaning

Apps that make network requests via the standard iOS interfaces store the servers' responses in a cache. The metadata of the requests and part of the responses are stored in a database; further responses are stored by iOS as individual files in the folder fsCachedData. Depending on the app, these are e.g. JSON data with chat messages, images or other media.

From a digital forensics perspective, a file in fsCachedData shows that the associated app retrieved this content from a server. It does not show, however, that the content was displayed to the user.

## Key facts

1. One folder per app in the cache directory; developers can also create it elsewhere in the app container
2. File names are UUID-like; the file type can only be recognised by the content
3. Whether a response is stored in fsCachedData is shown in Cache.db by the column `isDataOnFS` of the table `cfurl_cache_response`
4. Location:  
   **`/private/var/mobile/Containers/Data/Application/{UUID}/Library/Caches/{BUNDLE_ID}/fsCachedData/`**

## References

2018-08: <https://abrignoni.blogspot.com/2018/08/finding-discord-chats-in-ios.html>

## Tools

iLEAPP (fsCachedData) - <https://github.com/abrignoni/iLEAPP>
