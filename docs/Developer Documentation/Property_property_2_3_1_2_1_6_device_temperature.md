---
title: Property 2.3.1.2.1.6 Device Temperature
layout: home
parent: Configuration
nav_order: 235
---

## Property 2.3.1.2.1.6 Device Temperature

---

- [Property 2.3.1.2.1.6 Device Temperature](#property-231216-device-temperature)

---


Table 8‑207 - Property 2.3.1.2.1.6 Device Temperature

| Property Description |  |
|----|----|
| Property OID | 2.3.1.2.1.6 / 0x020301020106 |
| Name | Device Temperature |
| Description | The device uses this property to report the temperature in Celsius |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Signed Binary |
| Valid Values | 0x80 .. 0x7F (-128 .. 127) |
| Default | None |

Table 8‑208 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010201 8902 C600 |

Table 8‑209 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010201 8903 C601 26 |