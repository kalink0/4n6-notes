---
title: "Screen Sharing"
status: complete
completed: 2026-11-07
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [data-transfer, network, accounts]
---

# Screen Sharing

## Meaning

With Screen Sharing, a user views and controls the screen of another Mac over the network and copies files between the two computers. The connection has two sides, each leaving its own traces:

- **Connecting Mac:** The Screen Sharing app stores in its preferences file the connections from its connection list (address, display name, user name, groups, time of the last connection) and a list of file transfers (remote computer, file name, source and destination path, byte counters, direction and state as numeric values). The app logs the sessions in the Unified Logs.
- **Sharing Mac:** Sharing is off by default and is turned on in System Settings under "Sharing" or by command. macOS then changes the service's launch configuration and creates a preferences file; if access for VNC viewers with a password is allowed, also a file containing this password. The screensharingd service logs every login attempt in the Unified Logs.

From a digital forensics perspective, a saved connection shows that the app was used from this user account to connect to the given computer, most recently at the stored time; earlier connections to the same computer are not recorded individually. A transfer entry shows that a file was to be copied via the app between this Mac and the named computer, with source and destination path on both sides; it has no timestamp. On the sharing Mac, a login entry shows the time, the user name used, the IP address of the connecting computer and whether the login succeeded. The configuration files show that sharing was set up, but not a connection.

| Entry type | Shows | Relevant fields |
| --- | --- | --- |
| `com.apple.ScreenSharing.plist`, `connectionsStore` (connecting Mac) | Connection from this user account to the given computer, most recently at the stored time | `address`, `username`, `displayName`, `lastConnectedDate` |
| `com.apple.ScreenSharing.plist`, `FileTransferHistory` (connecting Mac) | File transfer between this Mac and the named computer | `remoteComputerName`, `sourcePath`, `destinationPath`, `bytesCopied`, `bytesToCopy` |
| Unified Logs, process `Screen Sharing` (connecting Mac) | Outgoing session at the time of the entry | |
| Unified Logs, process `screensharingd`, message `Authentication:` (sharing Mac) | Login attempt with user name, IP address of the connecting computer and result | `User Name`, `Viewer Address`, `SUCCEEDED` / `FAILED` |
| `disabled.plist`, key `com.apple.screensharing` (sharing Mac) | Sharing is turned on or off | |
| `com.apple.RemoteManagement.plist` (sharing Mac) | Screen Sharing or Remote Management was set up | |
| `com.apple.VNCSettings.txt` (sharing Mac) | Access for VNC viewers with a password was allowed | |

## Key facts

1. File transfers so far only examined on macOS 27
2. Sharing is turned off by default; the user can edit and delete saved connections in the app
3. The Unified Logs entries are rotated by size and age and can be overwritten after a short time on a heavily used Mac
4. `com.apple.ScreenSharing.plist` is a binary plist; `connectionsStore` is an embedded binary plist within it that must be decoded separately, `FileTransferHistory` an array in the outer plist
5. `lastConnectedDate` in UTC, only the last connection per computer; transfer entries without timestamp
6. The numeric values for direction (`direction`) and state (`state`) of the transfers are not documented; which path is on which computer can only be determined from the paths themselves
7. `com.apple.VNCSettings.txt` contains the VNC password, only obfuscated with a fixed key
8. `com.apple.RemoteManagement.plist` and the `screensharingd` entries are also created for connections via Apple Remote Desktop
9. Location:  
   Connecting Mac: **`/Users/{USER}/Library/Containers/com.apple.ScreenSharing/Data/Library/Preferences/com.apple.ScreenSharing.plist`**  
   Sharing Mac: **`/private/var/db/com.apple.xpc.launchd/disabled.plist`**  
   Sharing Mac: **`/Library/Preferences/com.apple.RemoteManagement.plist`**  
   Sharing Mac: **`/Library/Preferences/com.apple.VNCSettings.txt`**  
   Both: **`/private/var/db/diagnostics/`** (Unified Logs)

## References

2026-11: <https://doi.org/10.5281/zenodo.23876165>

2025-04: <https://www.cyberengage.org/post/macos-system-artifacts-macos-finder-gui-configurations-time-changes-bluetooth-printing-and-sha>

2020-04: <http://www.mac4n6.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins>

## Tools

mac_apt (Plugin: SCREENSHARING) - <https://github.com/ydkhatri/mac_apt>

macOS Screen Sharing FileTransferHistory Parser - <https://github.com/Forensic-IT/macos-screensharing-filetransferhistory>
