---
title: Property 1.1.1.1.1.B Apple VAS Merchant ID and URL Slot 5
layout: home
parent: Configuration
nav_order: 13
---

## Property 1.1.1.1.1.B Apple VAS Merchant ID and URL Slot 5

---

- [Property 1.1.1.1.1.B Apple VAS Merchant ID and URL Slot 5](#property-11111b-apple-vas-merchant-id-and-url-slot-5)

---


Table 395 - Property 1.1.1.1.1.B Apple VAS Merchant ID and URL Slot 5

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.B / 0x01010101010B |
| Name | Apple VAS Merchant ID and URL Slot 5 |
| Description | The device uses this property for Apple VAS processing to configure the device’s supported Merchant ID and URL. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 102 |
| Data Type | Binary |
| Valid Values | 00 or see **Table 375 - VAS Merchant ID and URL Type** |
| Default | 0x00 |

Table 396 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 CB00 |

Table 397 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 49 D1 01 85 01 01 87 04 01 01 01 01 89 3C CB 3A 9F 25 20 3E 22 54 3A AF 0A C5 E4 AC FC 25 67 1A 6E BF 6E DE 5A C1 96 74 6C 55 F3 D4 37 08 19 FF F9 22 C3 9F 29 14 77 77 77 2E 65 78 61 6D 70 6C 65 2D 75 72 6C 2E 63 6F 6D |

Table 398 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870401010101 8903 CB0100 |

Table 399 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 01 01 01 01 89 03 CB 01 00 |

##