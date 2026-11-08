---
title: "OAlerts"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-access]
---

# OAlerts

## Meaning

Microsoft Office logs the dialogs an Office application shows to the user (Office Alerts) in a dedicated event log. An entry contains the application (e.g. Word, Excel, Outlook) and the full text of the dialog, e.g. the question whether changes to a document should be saved, the error message for a wrong password for a protected document or the confirmation prompt when emptying the "Deleted Items" folder in Outlook.

From a digital forensics perspective, an entry shows that the application displayed the dialog at the given time. If the text names a file, it was open in the application at that time or an attempt was made to open it; the save prompt additionally shows that the document had unsaved changes. Which button the user chose in the dialog and under which user account the application ran is not logged.

## Key facts

1. Availability: since Office 2010, for all Office desktop applications
2. Prerequisites: enabled by default; entries are only created when a dialog is shown
3. Retention: as with other event logs, the oldest entries are overwritten when the maximum size is reached; the log can be cleared
4. Format and structure: EVTX log `OAlerts`; all entries have event ID 300, the source names the Office version (e.g. `Microsoft Office 16 Alerts`); the dialog text is in the language of the Office user interface and for files usually contains only the file name, not the path
5. Timestamps: UTC; time at which the dialog was shown
6. Particularities and pitfalls: not every entry goes back to a visible dialog; some are internal messages, e.g. errors when loading add-ins
7. Location:  
   **`C:\Windows\System32\winevt\Logs\OAlerts.evtx`**

## References

2026-11 (retrieved): <https://www.cyberengage.org/post/oalerts-evtx-the-hidden-microsoft-office-evidence-log>

2024-03: <https://dsforensics.com/ds-forensics-inc-articles/windows-event-logs-tracking-file-edits-and-deletions>

2021-02: <https://nasbench.medium.com/finding-forensic-goodness-in-obscure-windows-event-logs-60e978ea45a3>

## Tools

EvtxECmd - <https://ericzimmerman.github.io/>

evtx (evtx_dump) - <https://github.com/omerbenamram/evtx>

DLEAPP (Parser: Office Alerts) - <https://github.com/abrignoni/DLEAPP>

evtx2json (oalerts) - <https://github.com/Silv3rHorn/evtx2json>
