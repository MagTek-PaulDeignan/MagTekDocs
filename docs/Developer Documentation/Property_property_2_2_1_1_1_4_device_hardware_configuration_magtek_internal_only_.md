---
title: Property 2.2.1.1.1.4 Device Hardware Configuration (MAGTEK INTERNAL ONLY)
layout: home
parent: Configuration
nav_order: 219
---

## Property 2.2.1.1.1.4 Device Hardware Configuration (MAGTEK INTERNAL ONLY)

---

- [Property 2.2.1.1.1.4 Device Hardware Configuration (MAGTEK INTERNAL ONLY)](#property-221114-device-hardware-configuration-magtek-internal-only)

---


Table 1163 - Property 2.2.1.1.1.4 Device Hardware Configuration (MAGTEK
INTERNAL ONLY)

| Property Description |  |
|----|----|
| Property OID | 2.2.1.1.1.4 / 0x020201010104 |
| Name | Device Hardware Configuration |
| Description | The device uses this property to report its hardware configuration profile. See the **Hardware Configuration Profile** parameter in **Command 0xF016 - Activate Device Security (MAGTEK INTERNAL ONLY)** for detail. |
| Securing Key | None |
| Min. Len (b) | 10 |
| Max. Len (b) | 256 |
| Data Type | Binary |
| Valid Values | Any number |
| Default |  |

Table 1164 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 E3 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E2 08 E1 06 E1 04 E1 02 C4 00 |

Table 1165 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 08 D1 01 82 04 00 00 00 00 84 82 00 34 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 24 E2 22 E1 20 E1 1E E1 1C C4 1A 01 05 01 02 01 02 00 03 01 01 01 02 01 01 05 01 00 00 00 01 05 01 01 01 01 01 |