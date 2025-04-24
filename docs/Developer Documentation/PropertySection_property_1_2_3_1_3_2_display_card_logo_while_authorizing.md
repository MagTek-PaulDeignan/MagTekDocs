---
title: Property 1.2.3.1.3.2 Display Card Logo While Authorizing
layout: home
parent: Configuration
nav_order: 122
---

## Property 1.2.3.1.3.2 Display Card Logo While Authorizing

Table 901- Property 1.2.3.1.3.2 Display Card Logo While Authorizing

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
<td>1.2.3.1.3.2 / 0x010203010302</td>
</tr>
<tr>
<td>Name</td>
<td>Display Card Logo While Authorizing</td>
</tr>
<tr>
<td>Description</td>
<td>Enable display of logo for card brand used in transaction</td>
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
<td><p>0x00 = Disable Logo</p>
<p>0x01 = Enable Logo</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 902 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E3 06 E1 04 E3 02 C2 00 |

Table 903 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5E D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E3 03 C2 01 00 |

Table 904 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5D D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E3 03 C2 01 01 |

Table 905 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5D D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E3 03 C2 01 01 |

##