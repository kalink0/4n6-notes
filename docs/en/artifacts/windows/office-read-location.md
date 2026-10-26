---
title: "Office Read Location"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-access]
---

# Office Read Location

## Meaning

Microsoft Word stores the last position at which a user account last read or viewed a document ("Reading Locations" feature, also known as "Pick up where you left off"). This allows the user account to be navigated to this position when the document is opened again – also across devices, if signed in with a Microsoft account.

From a digital forensics perspective, the data allows the statement that the given document was opened by the user account and was closed at the given time. The last displayed position in the document (character position of the top visible line from the start of the document) can also be determined from the data.

## Key facts

1. Availability: exists since **Word 2013** (version 15.0).
2. Retention: the data of the **last 50 documents read** is stored.
3. Format and structure: a subkey `Document n` is created per document, with the values `File Path` (path of the document) and `Datetime` (time of last closing, **local system time**, format without seconds, e.g. `2025-08-23T14:39`). The value `Position` consists of **two numbers separated by a space**: the first corresponds to the `w14:paraId` of the last viewed paragraph (from the internal `document.xml`), the second to the **character position from the start of the document**
4. Timestamps: cross-validation: after conversion to UTC, the `Datetime` value (local time) should match the **last write time of the respective** `Document n` **subkey**
5. Special features and pitfalls: PDFs and documents opened via Outlook are also recorded; their path then points to the temporary Outlook cache. Documents on network drives are also recorded.
6. Location:  
   **`HKCU\Software\Microsoft\Office\{VERSION}\Word\Reading Locations`**

## References

2026-10 (accessed): <https://renenyffenegger.ch/notes/Windows/registry/tree/HKEY_CURRENT_USER/Software/Microsoft/Office/application_version/Word/Reading-Locations/index>

2025-08: <https://isc.sans.edu/diary/32224>

2025-02: <https://www.cyberengage.org/post/registry-user-activity-tracking-recently-opened-files-in-microsoft-office-a-forensic-guide>

2022-10: <https://office-watch.com/2014/how-do-they-know-where-you-left-off/>

2019-02: <https://thinkdfir.com/2019/02/11/microsoft-office-reading-locations-part-1/>

## Tools

RegRipper (msoffice) - <https://github.com/keydet89/RegRipper4.0>
