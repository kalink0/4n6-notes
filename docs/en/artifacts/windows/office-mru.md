---
title: "Office MRU"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-access]
---

# Office MRU

## Meaning

Microsoft Office stores the recently opened files and the recently used folders in which the files were located, to make operation more convenient for the user.

From a digital forensics perspective, entries in the Office MRU mean that the given files (according to the file name) were opened under the given file path by the user account in Microsoft Office. The given timestamp corresponds to the time the document was last opened.

## Key facts

1. Format and structure: File MRU = recently opened files. Place MRU = recently opened/used folders for opening/saving files
2. Special features and pitfalls: if ACCOUNT = LiveID_xxxx -> Microsoft account, if ACCOUNT = ADAL -> Azure Active Directory (today Microsoft Entra ID); ACCOUNT = AD_xxxx also occurs
3. Location:  
   **`HKCU\SOFTWARE\Microsoft\Office\{VERSION}\{APPNAME}\User MRU\{ACCOUNT}\File MRU`**  
   **`HKCU\SOFTWARE\Microsoft\Office\{VERSION}\{APPNAME}\User MRU\{ACCOUNT}\Place MRU`**  
   **`HKCU\SOFTWARE\Microsoft\Office\{VERSION}\{APPNAME}\File MRU`**  
   **`HKCU\SOFTWARE\Microsoft\Office\{VERSION}\{APPNAME}\Place MRU`**

## References

2024-02: <https://nk0.gitbook.io/dfir/windows/forensics/evidence-of-execution/office-apps-forensics/file-mru>

2023-05: <https://www.cyberengage.org/post/registry-user-activity-tracking-recently-opened-files-in-microsoft-office-a-forensic-guide>

## Tools

RegRipper (msoffice) - <https://github.com/keydet89/RegRipper4.0>
