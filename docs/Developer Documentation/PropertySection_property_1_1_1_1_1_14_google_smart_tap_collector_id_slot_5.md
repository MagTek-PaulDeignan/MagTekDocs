---
title: Property 1.1.1.1.1.14 Google Smart Tap Collector ID Slot 5
layout: home
parent: Configuration
nav_order: 20
---

## Property 1.1.1.1.1.14 Google Smart Tap Collector ID Slot 5

Table 431 - Property 1.1.1.1.1.14 Google Smart Tap Collector ID Slot 5

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.14 / 0x010101010114 |
| Name | Google Smart Tap Collector ID Slot 5 |
| Description | The device uses this property for Google Smart Tap processing to configure the device’s supported Collector ID and Service Types. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 25 |
| Data Type | Binary |
| Valid Values | 00 or see **Table 375 - VAS Merchant ID and URL Types** |
| Default | 0x00 |

Table 432 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 D400 |

Table 433 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 1E D1 01 85 01 01 87 04 01 01 01 01 89 11 D4 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

Table 434 - Set Request Example

| Example (Hex) |
|----|
| AA00 81048255D111 8427 D111 8107 2B06010401F609 8501 01 8704 01010101 8911 D40F DF7C083230313830363038DF7D0100 |

Table 435 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 2 7D 11 18 10 7 2B 06 01 04 01 F6 09 85 01 01 87 04 01 01 01 01 89 11 D4 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

##