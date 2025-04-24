---
title: Property 2.1.2.5.6.5 Server Certificate Chain Select
layout: home
parent: Configuration
nav_order: 200
---

## Property 2.1.2.5.6.5 Server Certificate Chain Select

Table 1120 - Property 2.1.2.5.6.5 Server Certificate Chain Select

| Property Description |  |
|----|----|
| Property OID | 2.1.2.5.6.5 / 0x020102050605 |
| Name | Server Certificate Chain Select |
| Description | The device uses this property to report the certificate chain used for server certificate. Server Certificate Chain Select is set by loading a Trust Configuration File. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0x00 – 0x01: 0x00=client chain, 0x01=server chain |
| Default | None |

Table 1121 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020506 8902 C500 |

Table 1122 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870401020506 8903 C501 00 |

##