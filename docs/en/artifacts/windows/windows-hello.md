---
title: "Windows Hello"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [accounts]
---

# Windows Hello

## Meaning

Windows Hello is the biometric or PIN-based sign-in method of Windows (since Windows 10) as an alternative to the classic password – supported methods include facial recognition, fingerprint and PIN.

From a digital forensics perspective, existing Windows Hello data allows the statement which sign-in method(s) are set up for a user account and – via associated sign-in events – when a successful or failed sign-in/unlock took place. A Windows Hello sign-in with biometric features can usually be used to attribute a sign-in/sign-in attempt to a person.

## Key facts

1. Introduced with Windows 10 (2015)
2. Biometric templates are stored per sensor/method as a separate, encrypted `.DAT` file – not reversible to the original image
3. With sensors supporting "Enhanced Sign-in Security" (ESS), the matching takes place directly on the sensor module – there may then be no analysable templates in the system
4. Log channel: `Microsoft-Windows-Biometrics/Operational` – including event IDs 1004/1005 (recognition successful/failed, with user and sensor), 1019 (sensor used) and 1605 (authorisation confirmed, without method); failed facial recognition may not be logged; Security log without any indication of Windows Hello
5. To be distinguished from **Windows Hello for Business** (domain/enterprise environment): key-based there instead of template-based, keys bound to the TPM, possibly synchronised with Active Directory/Entra ID (`msDS-KeyCredentialLink`) – a separate forensic question in the domain context
6. Location:  
   **`C:\Windows\System32\WinBioDatabase\`** (system-wide, not per user profile – one `.DAT` per sensor/method)  
   **`C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc\`** (keys for PIN/Windows Hello)

## References

2026-03: <https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/how-it-works>

2026-02: <https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/windows-hello-enhanced-sign-in-security>

2025-07: <https://insinuator.net/2025/07/windows-hello-for-business-the-face-swap/>

2025-02: <https://www.hecfblog.com/2025/02/daily-blog-745-solving-windows-hello.html>

2024-08: <https://media.defcon.org/DEF%20CON%2032/DEF%20CON%2032%20presentations/DEF%20CON%2032%20-%20Ceri%20Coburn%20Dirk-jan%20Mollema%20-%20Abusing%20Windows%20Hello%20Without%20a%20Severed%20Hand.pdf>

2018-11: <https://learn.microsoft.com/en-us/archive/msdn-technet-forums/7f2c39db-c4ea-48f5-a399-2df17f1edaad>

## Tools

EvtxECmd (Eric Zimmerman) - <https://github.com/EricZimmerman/evtx>

Chainsaw - <https://github.com/WithSecureLabs/chainsaw>

Hayabusa - <https://github.com/Yamato-Security/hayabusa>
