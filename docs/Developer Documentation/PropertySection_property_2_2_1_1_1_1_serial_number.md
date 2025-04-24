---
title: Property 2.2.1.1.1.1 Serial Number
layout: home
parent: Configuration
nav_order: 216
---

## Property 2.2.1.1.1.1 Serial Number

Table 1154 - Property 2.2.1.1.1.1 Serial Number

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
<td>2.2.1.1.1.1 / 0x020201010101</td>
</tr>
<tr>
<td>Name</td>
<td>Device Serial Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its serial number. The
left 3.5 bytes represent the 7 digit serial number, and the remaining
half byte is always 0.</p>
<p>Example: Serial number <strong>B603226</strong> is reported as 0xB6,
0x03, 0x22, 0x60.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Min 0x00000000</p>
<p>Max 0xFFFFFFF0</p></td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1155 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 B5 D1 01 84 18 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 87 04 02 01 01 01 89 02 C1 00 |

Table 1156 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 B5 D1 01 82 04 00 00 00 00 84 82 00 1C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 87 04 02 01 01 01 89 06 C1 04 B6 13 78 A0 |

##