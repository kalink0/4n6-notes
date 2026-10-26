---
title: "UserAssist"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution]
---

# UserAssist

## Meaning

The Windows operating system comes with the "UserAssist" feature. Based on the programs executed by the user account, this feature serves to display the most recently executed programs in the operating system's Start menu. It thus serves the usability of the operating system.

From a digital forensics perspective, entries in UserAssist provide information about when an application was last used by the referenced user account, where possible how often in total, and for how long. In addition, it can be said how an application was executed. The application must have been available on the system at the time of execution.

## Key facts

1. Entries are ROT-13 encoded
2. Only records programs started via the Windows interface (Start menu/search, desktop, Explorer, taskbar, Run); starts via the command line usually not
3. Can be disabled per user via the privacy setting "Track app launches"
4. Location (registry):  
   **`HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{GUID}\Count`**

## References

2026-03: <https://www.cybertriage.com/blog/userassist-forensics-2025/>

2025-09: <https://www.magnetforensics.com/blog/artifact-profile-userassist/>

2013-08: <https://www.hecfblog.com/2013/08/daily-blog-45-understanding-artifacts.html>

2013-05: <https://www.4n6k.com/2013/05/userassist-forensics-timelines.html>

## Tools

UserAssistView - <https://www.nirsoft.net/utils/userassist_view.html>

RegRipper (plugin: userassist) - <https://github.com/keydet89/RegRipper4.0>

Registry Explorer (bookmark: UserAssist) - <https://ericzimmerman.github.io/>

DLEAPP (parser: UserAssist) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (artifact: Windows.Registry.UserAssist) - <https://docs.velociraptor.app/artifact_references/pages/windows.registry.userassist/>

Dissect (plugin: userassist) - <https://docs.dissect.tools/en/stable/plugins/userassist.html>
