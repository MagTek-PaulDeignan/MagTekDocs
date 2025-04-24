---
title: Property 2.1.2.2.2.2 Main Firmware Version
layout: home
parent: Configuration
nav_order: 151
---

## Property 2.1.2.2.2.2 Main Firmware Version

Table 991 - Property 2.1.2.2.2.2 Main Firmware Version

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
<td>2.1.2.2.2.2 / 0x020102020202</td>
</tr>
<tr>
<td>Name</td>
<td>Main Firmware Version</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its main firmware version
number in the form <strong>PartNumber-Version-PCI</strong>, padded with
null characters.</p>
<p>Example: 1000007183-A0-PCI</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>19</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>19</td>
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

Table 992 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 08 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E2 04 E2 02 C2 00 |

Table 993 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 08 D1 01 82 04 00 00 00 00 84 82 00 2D D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1D E1 1B E2 19 E2 17 E2 15 C2 13 31 30 30 30 30 30 37 31 38 33 2D 41 31 2D 50 43 49 00 00 |

##