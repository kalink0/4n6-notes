---
title: "Radio cell"
status: complete
completed: 2026-10-31
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# Radio cell

A radio cell is the area served by one antenna of a mobile network base station.

A base station usually has several antennas, each covering one sector (often three sectors of 120° each); each sector is a separate radio cell. The size of a cell ranges from a few hundred metres in cities to several kilometres in rural areas. A mobile device that is switched on is always registered with one cell (serving cell). Which cell that is depends on signal strength and load; it does not have to be the nearest one.

Each radio cell has a globally unique identifier (CGI, Cell Global Identity; ECGI for LTE, NCGI for 5G):

- **MCC (Mobile Country Code, 3 digits):** country (e.g. 262 = Germany)
- **MNC (Mobile Network Code, 2–3 digits):** mobile network (e.g. 01 = Telekom)
- **LAC or TAC (Location Area Code for 2G/3G, Tracking Area Code for 4G/5G):** area made up of several radio cells
- **Cell ID:** radio cell within the network; the length depends on the mobile standard (for LTE 28 bits, made up of the identifier of the base station and of the cell)

From a digital forensics perspective, an entry with a cell identifier shows that the device was connected to this cell. The device's location can only be narrowed down to the coverage area of the cell.
