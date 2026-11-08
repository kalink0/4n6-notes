---
title: "Scheduled tasks"
status: complete
completed: 2026-11-08
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [persistence, program-execution]
---

# Scheduled tasks

## Meaning

The Windows Task Scheduler starts programs, scripts or commands at defined times or on certain events, e.g. at logon, at system startup or when idle. Tasks are created by Windows itself, by installed programs (e.g. for updates), by administrators and by users, through the Task Scheduler, `schtasks` or the programming interface. Each task is stored as an XML file containing, among other things, author, creation date, triggers, the actions to run and the user account it runs under. In addition, the Task Scheduler registers each task in the registry. The service actually loads the tasks from the registry; it also records there when a task was registered and when it last ran.

From a digital forensics perspective, a task shows that the named program or command is to be started automatically under the given conditions, with the rights of the given account. The last run time in the registry shows that the task's action was started at that time. If a task exists only in the registry but not as an XML file, or if the two differ, the task was modified or hidden outside the Task Scheduler.

## Key facts

1. Availability: XML format since Windows Vista; up to Windows XP binary files in `.job` format, which still occur later, e.g. for tasks created with `at.exe`
2. Prerequisites: the Task Scheduler is enabled by default; the history (log `Microsoft-Windows-TaskScheduler/Operational`) is disabled by default on Windows 10 and 11; the security events 4698 (created), 4699 (deleted), 4700 (enabled), 4701 (disabled) and 4702 (updated) are only generated with the audit policy "Audit Other Object Access Events"
3. Retention: when deleted through the Task Scheduler, the XML file and the registry entries are removed; if only the XML file is deleted, the task stays registered and keeps running
4. Format and structure: XML in UTF-16 without file extension, the subfolders correspond to the folders in the Task Scheduler; in the registry, per task one key under `Tree` with identifier and security descriptor (`SD`) and one key under `Tasks\{GUID}` with path, actions, triggers and runtime information as undocumented binary data
5. Timestamps: the creation date in the XML file is set by the creating program, can be chosen freely and is often in local time without time zone; in the registry (`DynamicInfo`) as FILETIME (UTC) the time of registration and of the last run, in newer Windows versions also of the last successful run
6. Particularities and pitfalls: if a task's `SD` value is missing or invalid, Task Scheduler and `schtasks` do not show the task, but it keeps running (known since 2022 from the Tarrask malware); removing it requires SYSTEM rights; tasks written directly to the registry generate no creation events; event IDs in the history: 106 (registered), 140 (updated), 141 (deleted), 100 (task started), 200 (action started), 201 (action completed)
7. Location:  
   XML: **`C:\Windows\System32\Tasks`**  
   Registry: **`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache`**  
   `.job`: **`C:\Windows\Tasks`**  
   History: **`C:\Windows\System32\winevt\Logs\Microsoft-Windows-TaskScheduler%4Operational.evtx`**

## References

2026-05: <https://forenza.io/persistence-task-cache/>

2024-02: <https://www.cybertriage.com/blog/windows-scheduled-tasks-for-dfir-investigations/>

2022-04: <https://www.microsoft.com/en-us/security/blog/2022/04/12/tarrask-malware-uses-scheduled-tasks-for-defense-evasion/>

## Tools

RegRipper (tasks, hiddentasks) - <https://github.com/keydet89/RegRipper4.0>

Autoruns - <https://learn.microsoft.com/sysinternals/downloads/autoruns>

EvtxECmd - <https://ericzimmerman.github.io/>

DLEAPP (Parser: Scheduled Tasks, Scheduled Task Cache (TaskCache), Task Scheduler Task Registrations, Task Scheduler Task Actions) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (Artifacts: Windows.System.TaskScheduler, Windows.Registry.TaskCache, Windows.EventLogs.ScheduledTasks) - <https://docs.velociraptor.app/>

Dissect (Plugin: tasks) - <https://docs.dissect.tools/>

Plaso (Parser: winjob, windows_task_cache) - <https://github.com/log2timeline/plaso>

TaskSchedulerView - <https://www.nirsoft.net/utils/task_scheduler_view.html>

juntei (parse-registry taskcache, persistence-hunter) - <https://github.com/Yamato-Security/juntei>

Windows-Scheduled-Task-Parser - <https://github.com/gajos112/Windows-Scheduled-Task-Parser>

PersistenceSniper (Get-ScheduledTasks) - <https://github.com/last-byte/PersistenceSniper>

Registry Explorer (plugin: TaskCache) - <https://ericzimmerman.github.io/>
