---
title: Property 2.1.2.3.5.1 Mastercard MCL Kernel ID (Contactless Only)
layout: home
parent: Configuration
nav_order: 166
---

## Property 2.1.2.3.5.1 Mastercard MCL Kernel ID (Contactless Only)

Table 1027 - Property 2.1.2.3.5.1 Mastercard MCL Kernel ID (Contactless
Only)

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
<td>2.1.2.3.5.1 / 0x020102030501</td>
</tr>
<tr>
<td>Name</td>
<td>Mastercard MCL Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Mastercard MCL Kernel
ID as string, padded with null characters.</p>
<p>Example: MCL 3.1.3</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>10</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>10</td>
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

Table 1028 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 28 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E5 02 C1 00 |

Table 1029 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 28 D1 01 82 04 00 00 00 00 84 82 00 24 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 14 E1 12 E2 10 E3 0E E5 0C C1 0A 4D 43 4C 20 33 2E 31 2E 33 00 |

##