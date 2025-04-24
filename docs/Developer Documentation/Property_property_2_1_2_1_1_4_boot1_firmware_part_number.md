---
title: Property 2.1.2.1.1.4 Boot1 Firmware Part Number
layout: home
parent: Configuration
nav_order: 146
---

## Property 2.1.2.1.1.4 Boot1 Firmware Part Number

---

- [Property 2.1.2.1.1.4 Boot1 Firmware Part Number](#property-212114-boot1-firmware-part-number)

---


Table 979 - Property 2.1.2.1.1.4 Boot1 Firmware Part Number

| Property Description |  |
|----|----|
| Property OID | 2.1.2.1.1.4 / 0x020102010104 |
| Name | Boot 1 Firmware Part Number |
| Description | The device uses this property to report its bootloader firmware part number as a string, padded with null characters. |
| Securing Key | None |
| Min. Len (b) | 11 |
| Max. Len (b) | 11 |
| Data Type | Alphanumeric |
| Valid Values | Any string |
| Default |  |

Table 980 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 03 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E1 04 E1 02 C4 00 |

Table 981 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 03 D1 01 82 04 00 00 00 00 84 82 00 25 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 15 E1 13 E2 11 E1 0F E1 0D C4 0B 31 30 30 30 30 30 37 35 33 36 00 |

##