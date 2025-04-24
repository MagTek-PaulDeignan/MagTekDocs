---
title: Property 2.3.1.1.2.2 Tamper Sensors Activated
layout: home
parent: Configuration
nav_order: 226
---

## Property 2.3.1.1.2.2 Tamper Sensors Activated

---

- [Property 2.3.1.1.2.2 Tamper Sensors Activated](#property-231122-tamper-sensors-activated)

---


Table 1175 - Property 2.3.1.1.2.2 Tamper Sensors Activated

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.3.1.1.2.2 / 0x020301010202</td>
</tr>
<tr>
<td>Name</td>
<td>Tamper Sensors Activated</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to report whether its tamper sensors
have been activated using <strong>Command 0xF016 - Activate Device
Security (MAGTEK INTERNAL ONLY)</strong>. A device that is operating
normally should always have its tamper sensors activated.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Tamper Sensors Not Activated</p>
<p>0x01 = Tamper Sensors Activated</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1176 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010102 8902 C100 |

Table 1177 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010102 8903 C101 01 |

##