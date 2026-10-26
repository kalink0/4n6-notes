---
title: "Tails Linux"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Tails Linux

Tails is a portable operating system that is started from a USB stick and has special security mechanisms to protect against surveillance.

By default, each time the system is shut down, all changes made during operation are discarded and the operating system is reset to its original state. This applies both to changes made by the user and to changes made by the system or programs. In particular, all log files created by the use of software are also deleted. Only a separate storage area ("Persistent Storage") can be used to store user data permanently and is not overwritten. However, no system files at all are stored in this area.

The Persistent Storage is encrypted with LUKS; the user password is required to extract any data stored there.
