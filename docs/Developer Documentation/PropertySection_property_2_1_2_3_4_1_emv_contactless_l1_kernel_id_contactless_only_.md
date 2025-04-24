---
title: Property 2.1.2.3.4.1 EMV Contactless L1 Kernel ID (Contactless Only)
layout: home
parent: Configuration
nav_order: 163
---

## Property 2.1.2.3.4.1 EMV Contactless L1 Kernel ID (Contactless Only)

Table 1018 - Property 2.1.2.3.4.1 EMV Contactless L1 Kernel ID
(Contactless Only)

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
<td>2.1.2.3.4.1 / 0x020102030401</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contactless L1 Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contactless L1
Kernel ID as string, padded with null characters.</p>
<p>Example: CL L1 EMVCO 3.0</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16</td>
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

Table 1019 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 21 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E4 02 C1 00 |

Table 1020 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 21 D1 01 82 04 00 00 00 00 84 82 00 2A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1A E1 18 E2 16 E3 14 E4 12 C1 10 43 4C 20 4C 31 20 45 4D 56 43 4F 20 33 2E 30 00 |

##