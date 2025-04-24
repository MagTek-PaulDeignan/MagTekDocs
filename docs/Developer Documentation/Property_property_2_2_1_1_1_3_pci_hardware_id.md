---
title: Property 2.2.1.1.1.3 PCI Hardware ID
layout: home
parent: Configuration
nav_order: 218
---

## Property 2.2.1.1.1.3 PCI Hardware ID

---

- [Property 2.2.1.1.1.3 PCI Hardware ID](#property-221113-pci-hardware-id)

---


Table 1160 - Property 2.2.1.1.1.3 PCI Hardware ID

| Property Description |  |
|----|----|
| Property OID | 2.2.1.1.1.3 / 0x020201010103 |
| Name | PCI Hardware ID |
| Description | The device uses this property to report its PCI Hardware ID. Customers can use this value to compare against the device’s certification records on the PCI web site. |
| Securing Key | None |
| Min. Len (b) | 10 |
| Max. Len (b) | 256 |
| Data Type | Alphanumeric |
| Valid Values | Any string |
| Default |  |

Table 1161 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 E3 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E2 08 E1 06 E1 04 E1 02 C3 00 |

Table 1162 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 E3 D1 01 82 04 00 00 00 00 84 82 00 24 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 14 E2 12 E1 10 E1 0E E1 0C C3 0A 33 36 50 43 49 34 35 30 41 30 |

##