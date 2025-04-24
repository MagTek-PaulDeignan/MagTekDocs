---
title: 8.4.1.1 Property 2.1.1.1.1.1 API Feature Set
layout: home
parent: Configuration
nav_order: 142
---

## 8.4.1.1 Property 2.1.1.1.1.1 API Feature Set

Table 973 - 8.4.1.1 Property 2.1.1.1.1.1 API Feature Set

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
<td>2.1.1.1.1.1 / 0x020101010101</td>
</tr>
<tr>
<td>Name</td>
<td>Main App Firmware API Feature Set</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report which API features are
active:</p>
<p>Bit 0: Banking Features</p>
<p>Bit 1 🡪 15: RFU</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Bit Mapped</td>
</tr>
<tr>
<td>Default</td>
<td>0x0000</td>
</tr>
</tbody>
</table>

Table 974 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 05 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E1 06 E1 04 E1 02 C1 00 |

Table 975 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 05 D1 01 82 04 00 00 00 00 84 82 00 1C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0C E1 0A E1 08 E1 06 E1 04 C1 02 01 00 |