---
title: Property 1.1.1.1.1.4 EMV Reversal Data Tag List (EMV Contact Only)
layout: home
parent: Configuration
nav_order: 6
---

## Property 1.1.1.1.1.4 EMV Reversal Data Tag List (EMV Contact Only)

---

- [Property 1.1.1.1.1.4 EMV Reversal Data Tag List (EMV Contact Only)](#property-111114-emv-reversal-data-tag-list-emv-contact-only)

---


Table 359 - Property 1.1.1.1.1.4 EMV Reversal Data Tag List (EMV Contact
Only)

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.4 / 0x010101010104 |
| Name | EMV Reversal Data Tag List |
| Description | The device uses this property when it generates an **EMV Batch Data Type** data object to contain **reversal data**, to determine what tags to include in the data object. It serves the same purpose that MagTek custom tag DFDF05 serves on some other MagTek devices. |
| Securing Key | None |
| Min. Len (b) | 0 |
| Max. Len (b) | 255 |
| Data Type | Binary |
| Valid Values | List of any valid standard EMV message tags and device custom tags |
| Default | 57 5A 82 8A 95 9A 9C 5F 24 5F 2A 5F 34 9F 01 9F 02 9F 10 9F 15 9F 16 9F 1A 9F 1C 9F 21 9F 33 9F 35 9F 36 9F 39 9F 5B DF DF 25 |

Table 360 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 16 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E1 06 E1 04 E1 02 C4 00 |

Table 361 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 16 D1 01 82 04 00 00 00 00 84 82 00 44 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 34 E1 32 E1 30 E1 2E E1 2C C4 2A 57 5A 82 8A 95 9A 9C 5F 24 5F 2A 5F 34 9F 01 9F 02 9F 10 9F 15 9F 16 9F 1A 9F 1C 9F 21 9F 33 9F 35 9F 36 9F 39 9F 5B DF DF 25 |

Table 362 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0D D1 11 84 44 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 34 E1 32 E1 30 E1 2E E1 2C C4 2A 57 5A 82 8A 95 9A 9C 5F 24 5F 2A 5F 34 9F 01 9F 02 9F 10 9F 15 9F 16 9F 1A 9F 1C 9F 21 9F 33 9F 35 9F 36 9F 39 9F 5B DF DF 25 |

Table 363 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0D D1 11 82 04 00 00 00 00 84 82 00 44 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 34 E1 32 E1 30 E1 2E E1 2C C4 2A 57 5A 82 8A 95 9A 9C 5F 24 5F 2A 5F 34 9F 01 9F 02 9F 10 9F 15 9F 16 9F 1A 9F 1C 9F 21 9F 33 9F 35 9F 36 9F 39 9F 5B DF DF 25 |

##