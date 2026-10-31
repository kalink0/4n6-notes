---
title: "Office Trust Records"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-access]
---

# Office Trust Records

## Meaning

Microsoft Office opens documents that come from the internet or from another untrusted source in the so-called *Protected View*. This view ensures that no malicious functions in the document can be executed.

The user is actively asked whether the *Protected View* should be left in order to be able to edit the document and, in a second step, whether any macros present should be enabled. If the user confirms this, a so-called *Trust Record* is created.

From a digital forensics perspective, the existence of a *Trust Record* means that the user actively enabled the editing view of the document with the given file path and file name and possibly enabled macros - this can be read from the data value.

## Key facts

1. Availability: the security feature has existed since MS Office 2010
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
