---
title: "Windows Timeline"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution, file-access]
---

# Windows Timeline

## Meaning

The Windows Timeline is a feature in modern Windows systems (Windows 10, from version 1803) that records the activities of user accounts and, if set up, synchronises them with the cloud and other devices. The Timeline is bound to the user account, but also shows on which device the action was performed.

Data such as running applications or opened documents is recorded.

From a digital forensics perspective, entries in the Windows Timeline mean that the corresponding user account performed the given action on the given device at the given time. An action can be, for example, starting a program, opening a file or bringing an application to the foreground.

## Key facts

1. Available from Windows 10, version 1803, removed in Windows 11
2. Retention 30 days with an online account, approx. 5 days with an offline account
3. Potentially data from other devices (bound to the account, also O365 without Windows; for Microsoft accounts only until July 2021, for Azure AD accounts also afterwards)
4. Location:  
   **`C:\Users\{user}\AppData\Local\ConnectedDevicesPlatform\{userId}\ActivitiesCache.db`**  
   userID can be: local user name, Microsoft account ID, Azure AD account

## References

2025-10: <https://securelist.com/forensic-artifacts-in-windows-11/117680/>

## Tools

WxTCmd - <https://ericzimmerman.github.io/>

WindowsTimeline (kacos2000) - <https://github.com/kacos2000/WindowsTimeline>

DLEAPP (parser: ActivitiesCache) - <https://github.com/abrignoni/DLEAPP>

Dissect (plugin: activitiescache) - <https://docs.dissect.tools/en/stable/plugins/activitiescache.html>
