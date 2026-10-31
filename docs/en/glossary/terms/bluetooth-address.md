---
title: "Bluetooth address (BD_ADDR)"
status: complete
completed: 2026-10-31
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Bluetooth address (BD_ADDR)

The Bluetooth address (BD_ADDR, Bluetooth Device Address) is the 48-bit hardware address of a Bluetooth interface.

Like a MAC address, it is written as six hexadecimal bytes (e.g. 00:1A:2B:3C:4D:5E); for a fixed (public) address, the first three bytes identify the manufacturer (OUI). Classic Bluetooth uses this fixed address. With Bluetooth Low Energy (BLE), devices often use random addresses that change regularly; paired devices can still resolve them using a key exchanged during pairing.

From a digital forensics perspective, devices store paired Bluetooth devices with their address, e.g. headphones or vehicles. If two devices each have stored the address of the other, this shows that they were paired with each other.
