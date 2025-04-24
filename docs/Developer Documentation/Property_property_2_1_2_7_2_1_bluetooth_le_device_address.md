---
title: Property 2.1.2.7.2.1 Bluetooth® LE Device Address
layout: home
parent: Configuration
nav_order: 208
---

## Property 2.1.2.7.2.1 Bluetooth® LE Device Address

---

- [Property 2.1.2.7.2.1 Bluetooth® LE Device Address](#property-212721-bluetooth®-le-device-address)

---


Table 1139 – Bluetooth® LE Device Address

| Property Description |  |
|----|----|
| Property OID | 2.1.2.7.2.1 / 0x020102070201 |
| Name | Bluetooth® LE Device Address |
| Description | The device uses this property to report its Bluetooth® LE Device address in most significant byte order. |
| Securing Key | None |
| Min. Len (b) | 6 |
| Max. Len (b) | 6 |
| Data Type | Binary |
| Valid Values | IEEE 802 EUI-48 |
| Default | None |

Table 1140 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104010ED101 841AD101 81072B06010401F609 850102 890AE108E206E704E202C100 |

Table 1141 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104820ED101 820400000000 84820020D101 81072B06010401F609 850102 8910E10EE20CE70AE208C1 06943469B297A5 |

##