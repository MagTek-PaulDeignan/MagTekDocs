---
title: Property 2.1.2.7.2.3 Bluetooth® LE Number of Bondings
layout: home
parent: Configuration
nav_order: 210
---

## Property 2.1.2.7.2.3 Bluetooth® LE Number of Bondings

---

- [Property 2.1.2.7.2.3 Bluetooth® LE Number of Bondings](#property-212723-bluetooth®-le-number-of-bondings)

---


Table 1145 – Bluetooth® LE Number of Bondings

| Property Description |  |
|----|----|
| Property OID | 2.1.2.7.2.3 / 0x020102070203 |
| Name | Bluetooth® LE Number of Bondings |
| Description | The device uses this property to report its Bluetooth® LE Number of Bondings. The maximum number of bondings is 9. If the device has 9 bondings and another host pairs with it, the new bonding will overwrite the oldest existing bonding. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0 - 9 |
| Default | None |

Table 1146 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020702 8902 C300 |

Table 1147 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501028704010207028903C30101 |

##