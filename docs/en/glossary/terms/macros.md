---
title: "Macros"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Macros

A macro is a sequence of commands that is stored in a document or an application and is executed automatically or on demand.

Best known are macros in Microsoft Office documents, which are written in the programming language Visual Basic for Applications (VBA). They can, for example, start when a document is opened and access files, the network and the operating system. Documents with macros have their own file extensions in the current Office formats (e.g. `.docm`, `.xlsm`); with the older formats (`.doc`, `.xls`), the file name does not show whether a macro is included. There are also older Excel 4.0 macros (XLM) and macros in other office suites such as LibreOffice.

From a digital forensics perspective, macros are a common way to bring malware onto a system via email attachments or downloads. Since 2022, Microsoft Office blocks macros in files from the internet by default; Windows recognises the origin by a marker that is stored in an additional data stream of the file during download (Mark of the Web, alternate data stream `Zone.Identifier`). Whether a macro was executed cannot be seen from the document itself, only from traces on the system, e.g. entries for documents for which the user enabled the content (registry key `TrustRecords`), started processes or downloaded files. The macro code can be extracted from documents with tools such as olevba (oletools) without executing it.
