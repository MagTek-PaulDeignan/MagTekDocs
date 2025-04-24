---
title: Property 2.1.2.3.3.1 EMV Contact L2 Kernel ID (Contact Only)
layout: home
parent: Configuration
nav_order: 159
---

## Property 2.1.2.3.3.1 EMV Contact L2 Kernel ID (Contact Only)

Table 1006 - Property 2.1.2.3.3.1 EMV Contact L2 Kernel ID (Contact
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
<td>2.1.2.3.3.1 / 0x020102030301</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contact L2 Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contact L2 Kernel
ID as string, padded with null characters.</p>
<p>Example: CT L2 4.3K</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>11</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>11</td>
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

Table 1007 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 15 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E3 02 C1 00 |

Table 1008 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 16 D1 01 82 04 00 00 00 00 84 82 00 25 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 15 E1 13 E2 11 E3 0F E3 0D C1 0B 43 54 20 4C 32 20 34 2E 33 4B 00 |

##