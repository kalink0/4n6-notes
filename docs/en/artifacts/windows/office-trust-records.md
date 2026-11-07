---
title: "Office Trust Records"
status: reviewed
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: human
translation_of: de
reviewers: [dugeonlady]
reviewed: 2026-11-07
topics: [file-access]
---

# Office Trust Records

## Meaning

Microsoft Office opens documents that come from the internet or from another untrusted source in the so-called *Protected View*. This view ensures that malicious functions in the document cannot be executed automatically.

In order to edit the document, the user is actively asked whether the *Protected View* should be left. In a second step, they're asked whether any present macros should be enabled. If the user confirms this, a so-called *Trust Record* is created.

From a digital forensics perspective, the existence of a *Trust Record* shows that the user actively enabled the editing view of a document and possibly enabled macros. It is stored using the documents file path and file name as key. The data value contains information about the chosen trusted action.

## Key facts

1. Availability: the security feature has existed starting with MS Office 2010
2. Prerequisites: Trust Records are only set if the default settings require active consent from the user.
3. Format and structure: meaning of the last 4 bytes in the data value:  
   01 00 00 00 = "Enable Editing" was clicked by the user account  
   ff ff ff 7f = "Enable Content" was clicked by the user account (macros enabled)
4. Timestamps: meaning of the first 8 bytes in the data value: timestamp of the creation of the document
5. Location:  
   **`HKCU\Software\Microsoft\Office\{VERSION}\{APPNAME}\Security\Trusted Documents\TrustRecords`**

## References

2020-03: <https://www.bleepingcomputer.com/news/security/windows-registry-helps-find-malicious-docs-behind-infections/>

2016-02: <https://az4n6.blogspot.com/2016/02/more-on-trust-records-macros-and.html>

## Tools

RegRipper (msoffice) - <https://github.com/keydet89/RegRipper4.0>
