---
title: Property 2.1.2.3.6.2 Visa payWave Kernel Firmware Part Number (Contactless Only)
layout: home
parent: Configuration
nav_order: 170
---

## Property 2.1.2.3.6.2 Visa payWave Kernel Firmware Part Number (Contactless Only)

Table 1039 - Property 2.1.2.3.6.2 Visa payWave Kernel Firmware Part
Number (Contactless Only)

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
<td>2.1.2.3.6.2 / 0x020102030602</td>
</tr>
<tr>
<td>Name</td>
<td>Visa payWave Firmware Part Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Visa payWave Kernel
Part Number as string, padded with null characters.</p>
<p>Example: 1000007180 Ver A1</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1040 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 05 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E6 02 C2 00 |

Table 1041 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 05 D1 01 82 04 00 00 00 00 84 82 00 2C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1C E1 1A E2 18 E3 16 E6 14 C2 12 31 30 30 30 30 30 37 31 38 30 20 56 65 72 20 41 31 00 |

##