---
title: Property 1.1.1.1.1.3 EMV Batch Data Tag List
layout: home
parent: Configuration
nav_order: 5
---

## Property 1.1.1.1.1.3 EMV Batch Data Tag List

Table 354 - Property 1.1.1.1.1.3 EMV Batch Data Tag List

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.3 / 0x010101010103 |
| Name | EMV Batch Data Tag List |
| Description | The device uses this property when it generates an **EMV Batch Data Type** data object to contain **transaction result data**, to determine what tags to include in the data object. It serves the same purpose that MagTek custom tag DFDF17 serves on some other MagTek devices. |
| Securing Key | None |
| Min. Len (b) | 0 |
| Max. Len (b) | 255 |
| Data Type | Binary |
| Valid Values | List of any valid standard EMV message tags and device custom tags |
| Default | 50 57 5A 82 84 8E 95 9A 9C F4 5F 20 5F 24 5F 25 5F 28 5F 2A 5F 2D 5F 34 9F 02 9F 03 9F 07 9F 09 9F 0B 9F 0D 9F 0E 9F 0F 9F 10 9F 11 9F 12 9F 15 9F 16 9F 1A 9F 1C 9F 1E 9F 21 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 DF DF 25 |

Table 355 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 15 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E1 06 E1 04 E1 02 C3 00 |

Table 356 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 15 D1 01 82 04 00 00 00 00 84 82 00 66 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 56 E1 54 E1 52 E1 50 E1 4E C3 4C 50 57 5A 82 84 8E 95 9A 9C 5F 20 5F 24 5F 25 5F 28 5F 2A 5F 2D 5F 34 9F 02 9F 03 9F 07 9F 09 9F 0B 9F 0D 9F 0E 9F 0F 9F 10 9F 11 9F 12 9F 15 9F 16 9F 1A 9F 1C 9F 1E 9F 21 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 DF DF 25 |

Table 357 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0B D1 11 84 66 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 56 E1 54 E1 52 E1 50 E1 4E C3 4C 50 57 5A 82 84 8E 95 9A 9C 5F 20 5F 24 5F 25 5F 28 5F 2A 5F 2D 5F 34 9F 02 9F 03 9F 07 9F 09 9F 0B 9F 0D 9F 0E 9F 0F 9F 10 9F 11 9F 12 9F 15 9F 16 9F 1A 9F 1C 9F 1E 9F 21 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 DF DF 25 |

Table 358 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0B D1 11 82 04 00 00 00 00 84 82 00 66 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 56 E1 54 E1 52 E1 50 E1 4E C3 4C 50 57 5A 82 84 8E 95 9A 9C 5F 20 5F 24 5F 25 5F 28 5F 2A 5F 2D 5F 34 9F 02 9F 03 9F 07 9F 09 9F 0B 9F 0D 9F 0E 9F 0F 9F 10 9F 11 9F 12 9F 15 9F 16 9F 1A 9F 1C 9F 1E 9F 21 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 DF DF 25 |

##