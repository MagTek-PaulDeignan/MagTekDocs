---
title: Property 1.2.2.1.1.10 Firmware Authentication Hash (MAGTEK INTERNAL ONLY)
layout: home
parent: Configuration
nav_order: 88
---

## Property 1.2.2.1.1.10 Firmware Authentication Hash (MAGTEK INTERNAL ONLY)

---

- [Property 1.2.2.1.1.10 Firmware Authentication Hash (MAGTEK INTERNAL ONLY)](#property-1221110-firmware-authentication-hash-magtek-internal-only)

---


Table 743 - Property 1.2.2.1.1.10 Firmware Authentication Hash (MAGTEK
INTERNAL ONLY)

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.10 / 0x010202010110 |
| Name | Firmware Authentication Hash |
| Description | The device uses this property to get and set the WLAN firmware hash. Only required when WLAN firmware is preloaded using JTAG during production. Allows MFG CFG to validate WLAN firmware is loaded properly. |
| Securing Key | None |
| Min. Len (b) | 44 |
| Max. Len (b) | 44 |
| Data Type | Binary |
| Valid Values | FW_adr\[4\], FW_len\[4\], hash_len\[4\], hash\[32\] |
| Default | None |

Table 744 - Get Request Example

| Example (Hex)                                          |
|--------------------------------------------------------|
| AA00 81040155D101 840FD101 850101870402020101 8902D000 |

Table 745 - Get Response Example

| Example (Hex) |
|----|
| AA0081048255D1018204000000008482003BD101850101870402020101892ED02C0000C000000F40000000002013160562C59F77F9EAC8EEA603BCC6C7E0DCED13B640C14BF550AB8520FAF758 |

Table 746 - Set Request Example

| Example (Hex) |
|----|
| AA0081040155D111843BD111850101870402020101892ED02C0000C000000F4000000000201F1E1D1C1B1A191817161514131211100F0E0D0C0B0A09080706050403020100 |

Table 8.3‑75 - Set Response Example

| Example (Hex) |
|----|
| AA0081048255D1118204000000008482003BD111850101870402020101892ED02C0000C000000F4000000000201F1E1D1C1B1A191817161514131211100F0E0D0C0B0A09080706050403020100 |

##