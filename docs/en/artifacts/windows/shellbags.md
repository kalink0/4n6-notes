---
title: "Shellbags"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-access]
---

# Shellbags

## Meaning

Shellbags are used in modern Windows systems (from Windows XP) to store the folder view for folders visited by the user account. The aim is to display the folder structure the way the user account prefers. Data such as folder names and date of access are stored.

From a digital forensics perspective, stored shellbags mean that the user account actively navigated the folder structure via Windows Explorer (including Open/Save dialogs in apps) at the given time. It cannot be said what was/is stored in files or whether they were opened by the user account. It cannot be said by which route a folder was navigated to. It can be said that at the time of navigation the folders matched the data in the shellbags by name.

## Key facts

1. Only folders opened with Windows Explorer (including Open/Save dialogs in apps) end up in the shellbags
2. Shellbags are retained even if the actual file path no longer exists (deletion, removal of external storage)
3. From Windows 11 22H2, archives (ZIP, 7-ZIP, RAR, TAR, GZIP) are also supported
4. Windows Store apps may additionally create shellbags. These are stored in separate User.dat and UserClasses.dat in the respective Windows app directory structure
5. Locations (registry):  
   Up to Windows XP, NTUSER.dat: **`HKCU\Software\Microsoft\Windows\ShellNoRoam\BagMRU`**  
   Up to Windows XP, NTUSER.dat: **`HKCU\Software\Microsoft\Windows\ShellNoRoam\Bags`**  
   Up to Windows XP, NTUSER.dat: **`HKCU\Software\Microsoft\Windows\Shell\BagMRU`**  
   Up to Windows XP, NTUSER.dat: **`HKCU\Software\Microsoft\Windows\Shell\Bags`**  
   From Windows Vista, NTUSER.dat: **`HKCU\Software\Microsoft\Windows\Shell\BagMRU`**  
   From Windows Vista, NTUSER.dat: **`HKCU\Software\Microsoft\Windows\Shell\Bags`**  
   From Windows Vista, UsrClass.dat: **`HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\BagMRU`**  
   From Windows Vista, UsrClass.dat: **`HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\Bags`**  
   Store apps: **`%USERPROFILE%\AppData\Local\Packages\{PACKAGE}\SystemAppData\Helium\User.dat`**  
   Store apps: **`%USERPROFILE%\AppData\Local\Packages\{PACKAGE}\SystemAppData\Helium\UserClasses.dat`**

## References

2026-03: <https://www.cybertriage.com/blog/shellbags-forensic-analysis-2025/>

2025-02: <https://www.ilyakobzar.com/p/revisiting-shellbags-in-windows-11>

2014-08: <https://www.magnetforensics.com/blog/forensic-analysis-of-windows-shellbags/>

2014-04: <https://www.sans.org/white-papers/34545>

## Tools

SBECmd - <https://ericzimmerman.github.io/>

Shellbag Explorer - <https://ericzimmerman.github.io/>

ShellBags View - <https://www.nirsoft.net/utils/shell_bags_view.html>

RegRipper (plugin: shellbags) - <https://github.com/keydet89/RegRipper4.0>

DLEAPP (parser: ShellBags) - <https://github.com/abrignoni/DLEAPP>

Velociraptor (artifact: Windows.Forensics.Shellbags) - <https://docs.velociraptor.app/artifact_references/pages/windows.forensics.shellbags/>

Dissect (plugin: shellbags) - <https://docs.dissect.tools/en/stable/plugins/shellbags.html>
