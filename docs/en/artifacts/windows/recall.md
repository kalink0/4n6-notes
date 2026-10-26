---
title: "Windows Recall"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [program-execution]
---

# Windows Recall

## Meaning

Windows Recall is an AI-supported feature for so-called Copilot+ PCs (Windows 11, from version 24H2, requires corresponding NPU hardware) that takes screenshots of the screen content at periodic intervals. The screenshots are analysed locally via OCR (text recognition) and semantic analysis and made searchable, so that users can find earlier screen content again by keyword or content search.

From a digital forensics perspective, a Recall entry means that the captured window/application was visible on the screen at the logged time – including the content displayed at that time. It does not show, however, that the user perceived the content or interacted with it. Likewise, the absence of content does not show that it was not displayed.

## Key facts

1. Prerequisite: Copilot+ PC hardware (NPU)
2. Disabled by default; activation requires active user interaction (opt-in). Individual applications can additionally exclude themselves from capture
3. Before April 2025 accessible unencrypted (but not widely distributed). Since April 2025 (general availability) encrypted via VBS enclave, decryption only via the user's Windows Hello on a running system
4. Incognito/private browsing is hidden in the screenshot – window title changes are still recorded, however
5. Sensitive content (passwords, ID and credit card numbers) is supposed to be filtered out by default
6. The oldest snapshots are deleted when the storage limit is reached; optional time limit (30–180 days)
7. Central table: `WindowCapture`; window events with timestamp and window title, snapshot events refer to the screenshot
8. Screenshots are stored separately as JPEG (`ImageStore`), referenced from the database; they also contain EXIF data
9. Location:  
   **`%USERPROFILE%\AppData\Local\CoreAIPlatform.00\UKP\{GUID}\`** (containing: ukg.db, SemanticTextStore.sidb, SemanticImageStore.sidb, folder ImageStore)

## References

2026-04: <https://www.windowscentral.com/microsoft/windows-11/why-this-windows-recall-feature-raises-real-security-questions>

2025-12: <https://learn.microsoft.com/en-us/windows/client-management/manage-recall>

2025-10: <https://securelist.com/forensic-artifacts-in-windows-11/117680/>

2024-09: <https://blogs.windows.com/windowsexperience/2024/09/27/update-on-recall-security-and-privacy-architecture/>

2024-09: <https://medium.com/@boutnaru/the-windows-forensic-journey-ukg-db-windows-recall-e2413841ade8>

2024-06: <https://cybercx.com.au/blog/forensic-applications-of-microsoft-recall/>

## Tools

TotalRecall / TotalRecall Reloaded - <https://github.com/xaitax/TotalRecall>

KAPE (target: WindowsCopilotRecall) - <https://github.com/EricZimmerman/KapeFiles/blob/master/Targets/Windows/WindowsCopilotRecall.tkape>

Velociraptor (artifacts: Windows.System.Recall.WindowCaptureEvent, Windows.System.Recall.AllWindowEvents) - <https://docs.velociraptor.app/exchange/artifacts/pages/windows.system.recall.windowcaptureevent/>
