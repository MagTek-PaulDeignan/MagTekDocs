---
title: Property 2.1.2.3.7.1 Discover D-PAS Kernel ID (Contactless Only)
layout: home
parent: Configuration
nav_order: 173
---

## Property 2.1.2.3.7.1 Discover D-PAS Kernel ID (Contactless Only)

Table 1048 - Property 2.1.2.3.7.1 Discover D-PAS Kernel ID (Contactless
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
<td>2.1.2.3.7.1 / 0x020102030701</td>
</tr>
<tr>
<td>Name</td>
<td>Discover D-PAS Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Discover D-PAS Kernel
ID as string, padded with null characters.</p>
<p>Example: DPAS 1.0</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>9</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>9</td>
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

Table 1049 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 07 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E7 02 C1 00 |

Table 1050 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 07 D1 01 82 04 00 00 00 00 84 82 00 23 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 13 E1 11 E2 0F E3 0D E7 0B C1 09 44 50 41 53 20 31 2E 30 00 |

##