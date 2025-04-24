---
title: Property 2.3.1.2.1.3 External Power Supplied
layout: home
parent: Configuration
nav_order: 232
---

## Property 2.3.1.2.1.3 External Power Supplied

---

- [Property 2.3.1.2.1.3 External Power Supplied](#property-231213-external-power-supplied)

---


Table 1190 - Property 2.3.1.2.1.3 External Power Supplied

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
<td>2.3.1.2.1.3 / 0x020301020103</td>
</tr>
<tr>
<td>Name</td>
<td>External Power Supplied</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to report the status of external
power.</td>
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
<td><p>0x00 = No external power supplied</p>
<p>0x01 = Power supplied by USB port</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1191 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010201 8902 C300 |

Table 8‑200 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010201 8903 C301 01 |

##