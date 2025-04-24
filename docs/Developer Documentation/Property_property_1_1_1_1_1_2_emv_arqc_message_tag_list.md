---
title: Property 1.1.1.1.1.2 EMV ARQC Message Tag List
layout: home
parent: Configuration
nav_order: 4
---

## Property 1.1.1.1.1.2 EMV ARQC Message Tag List

---

- [Property 1.1.1.1.1.2 EMV ARQC Message Tag List](#property-111112-emv-arqc-message-tag-list)

---


Table 349 - Property 1.1.1.1.1.2 EMV ARQC Message Tag List

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.2 / 0x010101010102 |
| Name | EMV ARQC Message Tag List |
| Description | The device uses this property when it generates an **EMV ARQC Type** data object, to determine what tags to include in the data object. It serves the same purpose that MagTek custom tag DFDF02 serves on some other MagTek devices. |
| Securing Key | None |
| Min. Len (b) | 0 |
| Max. Len (b) | 255 |
| Data Type | Binary |
| Valid Values | List of any valid standard EMV message tags and device custom tags |
| Default | 50 5A 57 82 84 95 9A 9B 9C F4 5F 1A 5F 20 5F 24 5F 2A 5F 30 5F 34 9F 02 9F 03 9F 06 9F 09 9F 10 9F 15 9F 1A 9F 1D 9F 1E 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 9F 39 9F 41 9F 45 9F 4C 9F 4E 9F 5D 9F 66 9F 6E 9F 7C |

Table 350 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 08 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E1 06 E1 04 E1 02 C2 00 |

Table 351 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 08 D1 01 82 04 00 00 00 00 84 82 00 64 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 54 E1 52 E1 50 E1 4E E1 4C C2 4A 50 5A 57 82 84 95 9A 9B 9C F4 5F 1A 5F 20 5F 24 5F 2A 5F 30 5F 34 9F 02 9F 03 9F 06 9F 09 9F 10 9F 15 9F 1A 9F 1D 9F 1E 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 9F 39 9F 41 9F 45 9F 4C 9F 4E 9F 5D 9F 66 9F 6E 9F 7C |

Table 352 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 09 D1 11 84 64 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 54 E1 52 E1 50 E1 4E E1 4C C2 4A 50 5A 57 82 84 95 9A 9B 9C F4 5F 1A 5F 20 5F 24 5F 2A 5F 30 5F 34 9F 02 9F 03 9F 06 9F 09 9F 10 9F 15 9F 1A 9F 1D 9F 1E 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 9F 39 9F 41 9F 45 9F 4C 9F 4E 9F 5D 9F 66 9F 6E 9F 7C |

Table 353 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 09 D1 11 82 04 00 00 00 00 84 82 00 64 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 54 E1 52 E1 50 E1 4E E1 4C C2 4A 50 5A 57 82 84 95 9A 9B 9C F4 5F 1A 5F 20 5F 24 5F 2A 5F 30 5F 34 9F 02 9F 03 9F 06 9F 09 9F 10 9F 15 9F 1A 9F 1D 9F 1E 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 9F 39 9F 41 9F 45 9F 4C 9F 4E 9F 5D 9F 66 9F 6E 9F 7C |

##