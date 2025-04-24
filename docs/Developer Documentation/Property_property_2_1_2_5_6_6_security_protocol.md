---
title: Property 2.1.2.5.6.6 Security Protocol
layout: home
parent: Configuration
nav_order: 201
---

## Property 2.1.2.5.6.6 Security Protocol

---

- [Property 2.1.2.5.6.6 Security Protocol](#property-212566-security-protocol)

---


Table 1123 - Property 2.1.2.5.6.6 Security Protocol

| Property Description |  |
|----|----|
| Property OID | 2.1.2.5.6.6 / 0x020102050606 |
| Name | Security Protocol |
| Description | The device uses this property to report the security protocol. Security Protocol is set by loading a Trust Configuration File. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0x00 – 0x02: 0x00=mTLS, 0x01=TLS, 02=None |
| Default | None |

Table 1124 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020506 8902 C600 |

Table 1125 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870401020506 8903 C601 00 |

##