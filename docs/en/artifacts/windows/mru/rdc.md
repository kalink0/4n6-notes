---
title: "MRU - Remote Desktop Connection"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [network]
---

# MRU - Remote Desktop Connection

## Meaning

The Windows operating system keeps several so-called MRU (Most Recently Used) lists. Per user account, these generally store recently opened or saved files, recently executed commands and recently opened folders.

The purpose of the MRU lists is to give users a smoother experience, for example by offering the user their recently opened files.

The list is written by the Windows Remote Desktop Connection client (mstsc.exe).

From a digital forensics perspective, entries in the MRU list for RDC mean that the user account attempted to establish a remote connection to the listed host names/IP addresses. The order in the MRU corresponds to the order of the respective last connection attempts to the host names/IP addresses.

## Key facts

1. There is only one entry per IP/host name in the MRU list
2. Values MRU0 to MRU9, MRU0 is the newest entry
3. The last write time of the key Default only belongs to MRU0
4. The subkey Servers contains a separate key per target with UsernameHint (user name used) and is not limited to ten entries
5. With mstsc /public, neither MRU nor Servers are written
6. Locations:  
   **`HKCU\Software\Microsoft\Terminal Server Client\Default`**  
   **`HKCU\Software\Microsoft\Terminal Server Client\Servers\{HOST}`**

## References

2026-02: <https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/remove-entries-from-remote-desktop-connection-computer>

2025-03: <https://devolutions.net/blog/using-rdp-without-leaving-traces-the-mstsc-public-mode/>

## Tools

DLEAPP (windowsRdpClientServers) - <https://github.com/abrignoni/DLEAPP>

RegRipper (tsclient) - <https://github.com/keydet89/RegRipper4.0>

Velociraptor (Windows.Registry.RDP) - <https://docs.velociraptor.app/>
