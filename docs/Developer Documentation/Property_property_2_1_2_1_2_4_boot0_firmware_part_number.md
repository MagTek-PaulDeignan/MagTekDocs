---
title: Property 2.1.2.1.2.4 Boot0 Firmware Part Number
layout: home
parent: Configuration
nav_order: 148
---

## Property 2.1.2.1.2.4 Boot0 Firmware Part Number

---

- [Property 2.1.2.1.2.4 Boot0 Firmware Part Number](#property-212124-boot0-firmware-part-number)

---


| Property Description |  |
|----|----|
| Property OID | 2.1.2.1.2.4 / 0x020102010204 |
| Name | Boot 0 Firmware Part Number |
| Description | The device uses this property to report its bootloader firmware part number as a string, padded with null characters. |
| Securing Key | None |
| Min. Len (b) | 11 |
| Max. Len (b) | 11 |
| Data Type | Alphanumeric |
| Valid Values | Any string |
| Default |  |

Table 985 - Property 2.1.2.1.2.4 Boot0 Firmware Part Number

| Example (Hex) |
|----|
| AA 00 81 04 01 0A D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E1 04 E2 02 C4 00 |

Table 986 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0A D1 01 82 04 00 00 00 00 84 82 00 25 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 15 E1 13 E2 11 E1 0F E2 0D C4 0B 31 30 30 30 30 30 37 35 33 35 00 |

Table 987 - Get Response Example

#