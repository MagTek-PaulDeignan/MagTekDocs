---
title: Property 2.3.1.2.1.5 Battery Charger Status
layout: home
parent: Configuration
nav_order: 234
---

## Property 2.3.1.2.1.5 Battery Charger Status

---

- [Property 2.3.1.2.1.5 Battery Charger Status](#property-231215-battery-charger-status)

---


Table 8‑204 - Property 2.3.1.2.1.5 Battery Charger Status

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
<td>2.3.1.2.1.5 / 0x020301020105</td>
</tr>
<tr>
<td>Name</td>
<td>Battery Charger Status</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to report the status of the battery
charger.</td>
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
<td><p>0x00 = Precharge</p>
<p>0x01 = Fast charge – constant current</p>
<p>0x02 = Fast charge – constant voltage</p>
<p>0x03 = End of charge</p>
<p>0x04 = Charge complete</p>
<p>0x08 = No external power supplied</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 8‑205 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010201 8902 C500 |

Table 8‑206 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010201 8903 C501 04 |

##