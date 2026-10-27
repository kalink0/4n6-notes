---
title: "MAC Address"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# MAC Address

The MAC address (Media Access Control) is the hardware address of a network interface, used to address devices within a local network.

It is 48 bits long and is usually written as six hexadecimal bytes (e.g. 00:1A:2B:3C:4D:5E). The first three bytes (OUI, Organizationally Unique Identifier) identify the manufacturer of the network interface. The MAC address is only transmitted within the local network and is not passed on across routers to the internet.

From a digital forensics perspective, a MAC address, e.g. from the logs of a router, can be attributed to a device. The OUI can also potentially be used to determine the manufacturer of the network interface or the device. However, the MAC address can be changed by software. In addition, iOS and Android use randomly generated MAC addresses per Wi-Fi network by default, so the address seen in a network does not necessarily match the hardware address of the device.
