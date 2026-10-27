---
title: "IP Address"
status: complete
completed: 2026-10-27
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# IP Address

An IP address is an address through which a device can be reached in a network based on the Internet Protocol (IP).

There are two versions: IPv4 addresses are 32 bits long (e.g. 192.0.2.10), IPv6 addresses 128 bits (e.g. 2001:db8::10). Private address ranges (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) are only used in local networks and cannot be reached from the internet. Public IP addresses are assigned by the internet service provider, often dynamically, i.e. an address is assigned to different subscriber lines one after another.

From a digital forensics perspective, a public IP address together with an exact timestamp including time zone can be used to attribute the subscriber line or the device via the provider. If several subscriber lines share one public address (carrier-grade NAT), the source port is needed as well.
