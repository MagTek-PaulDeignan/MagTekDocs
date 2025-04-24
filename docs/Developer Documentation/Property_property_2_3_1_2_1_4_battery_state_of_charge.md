---
title: Property 2.3.1.2.1.4 Battery State of Charge
layout: home
parent: Configuration
nav_order: 233
---

## Property 2.3.1.2.1.4 Battery State of Charge

---

- [Property 2.3.1.2.1.4 Battery State of Charge](#property-231214-battery-state-of-charge)

---


Table 8‑201 - Property 2.3.1.2.1.4 Battery State of Charge

| Property Description |  |
|----|----|
| Property OID | 2.3.1.2.1.4 / 0x020301020104 |
| Name | Battery State of Charge |
| Description | The device uses this property to report the charge status of the internal battery. The charge status is reported as a percentage of full charge. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0x00..0x64 |
| Default | None |

Table 8‑202 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010201 8902 C400 |

Table 8‑203 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010201 8903 C401 64 |

##