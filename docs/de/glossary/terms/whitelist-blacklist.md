---
title: "Whitelist / Blacklist"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
---

# Whitelist / Blacklist

Eine Whitelist bzw. Blacklist ist eine Liste von Einträgen, z. B. Dateien, IP-Adressen, Internetseiten oder Ports, die als zulässig bzw. unbedenklich (Whitelist) oder als unzulässig bzw. relevant (Blacklist) eingestuft sind.

Whitelists und Blacklists werden z. B. in Firewalls, Proxys oder E-Mail-Filtern eingesetzt, um Verbindungen oder Inhalte zuzulassen bzw. zu blockieren. Die Listen werden auch als Allowlist/Blocklist oder Known-Good/Known-Bad bezeichnet.

Im digitalforensischen Kontext werden vor allem Listen von Hash-Werten verwendet, mit denen Dateien abgeglichen werden. Eine Whitelist (z. B. die NSRL des NIST mit Dateien von Betriebssystemen und Standardsoftware) reduziert die zu sichtende Datenmenge, da bekannte unbedenkliche Dateien ausgeblendet werden können. Eine Blacklist (z. B. bekannte Schadsoftware oder bereits bekanntes inkriminiertes Material) ermöglicht das schnelle Auffinden bekannter Dateien. Bereits eine minimale Änderung einer Datei führt zu einem anderen Hash-Wert, sodass veränderte Dateien nicht erkannt werden.
