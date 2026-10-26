---
title: "UAL - User Access Logging"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [accounts, network]
---

# UAL - User Access Logging

## Meaning

The UAL (User Access Logging) service logs access to services of the local server. Administrators can use it to determine how many users use a service. This makes it possible for administrators to see whether there are enough licences for the use of a service.

From a digital forensics perspective, entries mean that the user account accessed the corresponding service from the logged IP address. The number of accesses per day is listed, with the first access of the year and the last access of the year additionally shown including the time.

## Key facts

1. Enabled by default on Windows Server versions, from Windows Server 2012
2. Logins of the last 2-3 years available
3. Timestamps in UTC
4. Location:  
   **`C:\Windows\System32\LogFiles\Sum`**  
   Current.mdb: current year  
   {GUID}.mdb: copy of Current.mdb (updated every 24 hours) as well as one file each for the two previous years  
   SystemIdentity.mdb: server roles and mapping of RoleGuid to role name

## References

2026-02: <https://learn.microsoft.com/en-us/windows-server/security/windows-services/security-guidelines-for-disabling-system-services-in-windows-server#user-access-logging-service>

2024-05: <https://www.thedfirspot.com/post/sum-ual-investigating-server-access-with-user-access-logging>

2021-06: <https://www.crowdstrike.com/en-us/blog/user-access-logging-ual-overview>

2021-02: <https://svch0st.medium.com/windows-user-access-logs-ual-9580f1100635>

## Tools

SumECmd - <https://ericzimmerman.github.io/>

KStrike - <https://github.com/brimorlabs/KStrike>

DLEAPP (parser: User Access Logging) - <https://github.com/abrignoni/DLEAPP>

Dissect (plugin: ual) - <https://docs.dissect.tools/en/stable/plugins/ual.html>
