---
title: Property 2.1.2.3.2.1 EMV Contact L1 Kernel ID (Contact Only)
layout: home
parent: Configuration
nav_order: 157
---

## Property 2.1.2.3.2.1 EMV Contact L1 Kernel ID (Contact Only)

Table 1000 - Property 2.1.2.3.2.1 EMV Contact L1 Kernel ID (Contact
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
<td>2.1.2.3.2.1 / 0x020102030201</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contact L1 Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contact L1 Kernel
ID as string, padded with null characters.</p>
<p>Example: CT L1 EMVCO 4.3C</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>17</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>17</td>
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

Table 1001 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 12 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E2 02 C1 00 |

Table 1002 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 12 D1 01 82 04 00 00 00 00 84 82 00 2B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1B E1 19 E2 17 E3 15 E2 13 C1 11 43 54 20 4C 31 20 45 4D 56 43 4F 20 34 2E 33 43 00 |

##