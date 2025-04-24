---
title: Property 1.1.1.1.1.D Apple iAP2 AppBundleID
layout: home
parent: Configuration
nav_order: 15
---

## Property 1.1.1.1.1.D Apple iAP2 AppBundleID

Table 405 - Property 1.1.1.1.1.D Apple iAP2 AppBundleID

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.D / 0x01010101010D |
| Name | Apple iAP2 AppBundleID |
| Description | This setting allows the iOS device to recommend installation of a specific app or set of apps to use with the iOS device when connects to an accessory. |
| Securing Key | None |
| Min. Len (b) | A valid reverse-DNS similar to the Default below |
| Max. Len (b) | 50 |
| Data Type | ASCII |
| Valid Values | ASCII |
| Default | com.magtek.dynaflex2go |

Table 406 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E1 06 E1 04 E1 02 CD 00 |

Table 407 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 4C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 3C E1 3A E1 38 E1 36 E1 34 CD 32 63 6F 6D 2E 6D 61 67 74 65 6B 2E 64 79 6E 61 66 6C 65 78 32 67 6F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |

Table 408 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 07 D1 11 84 4C D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 3C E1 3A E1 38 E1 36 E1 34 CD 32 63 6F 6D 2E 6D 61 67 74 65 6B 2E 64 79 6E 61 66 6C 65 78 32 67 6F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |

Table 409 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 07 D1 11 82 04 00 00 00 00 84 82 00 4C D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 3C E1 3A E1 38 E1 36 E1 34 CD 32 63 6F 6D 2E 6D 61 67 74 65 6B 2E 64 79 6E 61 66 6C 65 78 32 67 6F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |

##