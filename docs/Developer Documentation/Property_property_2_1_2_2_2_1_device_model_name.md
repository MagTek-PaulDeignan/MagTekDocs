---
title: Property 2.1.2.2.2.1 Device Model Name
layout: home
parent: Configuration
nav_order: 150
---

## Property 2.1.2.2.2.1 Device Model Name

---

- [Property 2.1.2.2.2.1 Device Model Name](#property-212221-device-model-name)

---


Table 988 - Property 2.1.2.2.2.1 Device Model Name

| Property Description |  |
|----|----|
| Property OID | 2.1.2.2.2.1 / 0x020102020201 |
| Name | Device Model Name |
| Description | The device uses this property to report its model name as string, padded with null characters. |
| Securing Key | None |
| Min. Len (b) | 10 |
| Max. Len (b) | 20 |
| Data Type | Alphanumeric |
| Valid Values | Any string |
| Default |  |

Table 989 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E2 04 E2 02 C1 00 |

Table 990 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 27 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 17 E1 15 E2 13 E2 11 E2 0F C1 0D 44 79 6E 61 46 6C 65 78 20 50 72 6F 00 |

##