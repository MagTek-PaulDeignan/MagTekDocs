---
title: Property 1.1.1.1.1.1 EMV Terminal Identification
layout: home
parent: Configuration
nav_order: 3
---

## Property 1.1.1.1.1.1 EMV Terminal Identification

Table 344 - Property 1.1.1.1.1.1 EMV Terminal Identification

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.1 / 0x010101010101 |
| Name | EMV Terminal Identification |
| Description | The device uses this property to report its Terminal ID / Terminal Identification in tag **9F1C** in all EMV-related communication. Merchants usually configure each device with a different terminal ID per their own proprietary system standards to help identify the source of a transaction. |
| Securing Key | None |
| Min. Len (b) | 8 |
| Max. Len (b) | 8 |
| Data Type | Alphanumeric |
| Valid Values | Any string |
| Default | “00000000” (0x3030303030303030) |

Table 345 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 04 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E1 06 E1 04 E1 02 C1 00 |

Table 346 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 04 D1 01 82 04 00 00 00 00 84 82 00 22 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 12 E1 10 E1 0E E1 0C E1 0A C1 08 30 30 30 30 30 30 30 30 |

Table 347 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 3E D1 11 84 22 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 12 E1 10 E1 0E E1 0C E1 0A C1 08 31 31 31 31 31 31 31 31 |

Table 348 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 3E D1 11 82 04 00 00 00 00 84 82 00 22 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 12 E1 10 E1 0E E1 0C E1 0A C1 08 31 31 31 31 31 31 31 31 |

##