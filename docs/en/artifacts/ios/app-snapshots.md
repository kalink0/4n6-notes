---
title: "App Snapshots"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution]
---

# App Snapshots

## Meaning

iOS creates app snapshots when an app moves to the background. They capture the displayed screen state and serve, among other things, as a preview in the app switcher.

From a digital forensics perspective, the snapshots show the last content of the app displayed on the screen before it was last moved to the background by the user or the system.

## Key facts

1. First observed on iOS 10
2. Snapshot metadata is stored in `applicationState.db` under the key `XBApplicationSnapshotManifest` (key=2, table=kvs). The related information is stored in bplists. The snapshot images are in KTX format or, on current iOS versions, PNG
3. The `creationDate` corresponds to the creation of the file. The exact meaning of `lastUsedDate` has not been conclusively clarified
4. The content can be hidden if the app was declared as sensitive by the app developer and/or the user - the snapshot is then black
5. Locations:  
   **`/private/var/mobile/Library/FrontBoard/applicationState.db`**  
   **`/private/var/mobile/Library/SplashBoard/Snapshots/`**  
   **`/private/var/mobile/Containers/Data/Application/{UUID}/Library/SplashBoard/Snapshots`**  
   **`/private/var/mobile/Containers/Data/Application/{UUID}/Library/Caches/Snapshots/`**

## References

2026-08: <https://leapps.org/blog-post?post=2026-08-10-ios-app-snapshots-seven-years-later>

2025-05: <https://www.magnetforensics.com/blog/that-one-artifact-snapshot-to-justice/>

2019-09: <https://abrignoni.blogspot.com/2019/09/ios-snapshots-triage-parser-working.html>

2019-09: <https://gforce4n6.blogspot.com/2019/09/a-quick-look-into-ios-snapshots.html>

## Tools

iLEAPP (App Snapshots) - <https://github.com/abrignoni/iLEAPP>
