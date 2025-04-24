---
title: Property 2.1.2.7.2.4 Bluetooth® LE MTU Size
layout: home
parent: Configuration
nav_order: 211
---

## Property 2.1.2.7.2.4 Bluetooth® LE MTU Size

Table 1148 – Bluetooth® LE MTU Size

| Property Description |  |
|----|----|
| Property OID | 2.1.2.7.2.4 / 0x020102070204 |
| Name | Bluetooth® LE MTU Size |
| Description | The device uses this two-byte property, in most significant byte order, to report its Bluetooth® LE MTU size. The maximum transmission unit (MTU) is agreed upon between the host and the device during a connection. For DynaFlex, the value will be between 23 and 247 depending on the size the host supports. If the device is not in a connection, it will report 23. |
| Securing Key | None |
| Min. Len (b) | 2 |
| Max. Len (b) | 2 |
| Data Type | Binary |
| Valid Values | 23 - 247 |
| Default | None |

Table 1149 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020702 8902 C400 |

Table 1150 - Get Response Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D10182040000000084820011D1018501028704010207028904C40200F7 |

#