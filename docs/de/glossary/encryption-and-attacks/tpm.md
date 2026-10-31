---
title: "Trusted Platform Module (TPM)"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Trusted Platform Module (TPM)

Ein Trusted Platform Module (TPM) ist ein Sicherheitsbaustein in PCs und Notebooks, der kryptografische Schlüssel geschützt speichert und nur unter festgelegten Bedingungen freigibt.

Das TPM kann ein eigener Chip auf der Hauptplatine sein oder als Firmware-TPM im Prozessor umgesetzt werden (z. B. Intel PTT, AMD fTPM). Beim Systemstart misst es die einzelnen Stufen des Bootvorgangs (Firmware, Bootloader, Konfiguration). Ein Schlüssel kann an diese Messwerte gebunden werden und wird nur freigegeben, wenn die Bootkette unverändert ist. Zusätzlich kann die Freigabe an eine PIN gekoppelt werden; nach mehreren Fehlversuchen sperrt sich das TPM vorübergehend. Windows 11 setzt ein TPM 2.0 voraus, die Festplattenverschlüsselung von Windows (BitLocker) nutzt es standardmäßig. Unter Linux kann z. B. ein mit LUKS verschlüsselter Datenträger über das TPM entsperrt werden.

Aus digitalforensischer Sicht ist ein mit TPM geschützter Datenträger an das Gerät gebunden: Wird er ausgebaut und an einem anderen System gesichert, liegen die Daten nur verschlüsselt vor und lassen sich nur mit dem beim Einrichten erzeugten Wiederherstellungsschlüssel (Recovery Key) entschlüsseln. Auch Änderungen an der Bootkette, z. B. das Starten von einem anderen Medium oder geänderte Firmware-Einstellungen, führen dazu, dass das TPM den Schlüssel nicht freigibt. Ohne zusätzliche PIN entsperrt das TPM das Volume beim Start automatisch, die Daten sind dann im Wesentlichen nur noch durch die Anmeldung am Betriebssystem geschützt. Bei separaten TPM-Chips ist es in diesem Fall bereits gelungen, den Schlüssel auf der Verbindung zwischen TPM und Prozessor mitzulesen.
