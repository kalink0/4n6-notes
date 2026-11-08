---
title: "Office MRU"
status: reviewed
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: human
translation_of: de
reviewers: [dugeonlady]
reviewed: 2026-11-06
topics: [file-access]
---

# Office MRU

## Meaning

To enhance usability, Microsoft Office stores the recently opened files and the recently used folders in which the files were located.

From a digital forensics perspective, entries in the Office MRU show that certain files (according to the file name) were opened under a specific file path by the user account in Microsoft Office. The stored timestamp corresponds to the time the document was last opened.

## Key facts

1. Format and structure: File MRU = recently opened files. Place MRU = recently opened/used folders for opening/saving files
2. Particularities and pitfalls: if ACCOUNT = LiveID_xxxx -> Microsoft account, if ACCOUNT = ADAL -> Azure Active Directory (today Microsoft Entra ID); ACCOUNT = AD_xxxx also occurs
3. Location:  
   **`HKCU\SOFTWARE\Microsoft\Office\{VERSION}\{APPNAME}\User MRU\{ACCOUNT}\File MRU`**  
   **`HKCU\SOFTWARE\Microsoft\Office\{VERSION}\{APPNAME}\User MRU\{ACCOUNT}\Place MRU`**  
   **`HKCU\SOFTWARE\Microsoft\Office\{VERSION}\{APPNAME}\File MRU`**  
   **`HKCU\SOFTWARE\Microsoft\Office\{VERSION}\{APPNAME}\Place MRU`**

## References

2024-02: <https://nk0.gitbook.io/dfir/windows/forensics/evidence-of-execution/office-apps-forensics/file-mru>

2023-05: <https://www.cyberengage.org/post/registry-user-activity-tracking-recently-opened-files-in-microsoft-office-a-forensic-guide>

## Tools

### Core tools

DLEAPP (parser: Office File and Place MRU) - <https://github.com/abrignoni/DLEAPP>

Dissect (plugin: mru.msoffice) - <https://docs.dissect.tools/>

Velociraptor (artifact: Windows.Office.MRU) - <https://docs.velociraptor.app/>

Registry Explorer (plugin: OfficeMRU) - <https://ericzimmerman.github.io/>

### Other tools

juntei (parse-registry office) - <https://github.com/Yamato-Security/juntei>

Plaso (parser: microsoft_office_mru) - <https://github.com/log2timeline/plaso>

RegRipper (msoffice) - <https://github.com/keydet89/RegRipper4.0>
