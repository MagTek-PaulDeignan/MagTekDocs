---
title: Property 2.1.2.3.8.3 American Express Expresspay Kernel Checksum (Contactless Only)
layout: home
parent: Configuration
nav_order: 178
---

## Property 2.1.2.3.8.3 American Express Expresspay Kernel Checksum (Contactless Only)

Table 1063 - Property 2.1.2.3.8.3 American Express Expresspay Kernel
Checksum (Contactless Only)

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
<td>2.1.2.3.8.3/ 0x020102030803</td>
</tr>
<tr>
<td>Name</td>
<td>American Express Expresspay Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the American Express
Expresspay Kernel Checksum as string, no padding.</p>
<p>Example: C4.2.7 -&gt; v1.0.6
[5D5CC3073F64FE7F14F5454D62026EDB9E202930]</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Variable</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>75</td>
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

Table 1064 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 11 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E8 02 C3 00 |

Table 1065 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 11 D1 01 82 04 00 00 00 00 84 82 00 55 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 45 E1 43 E2 41 E3 3F E8 3D C3 3B 43 34 2E 32 2E 37 20 2D 3E 20 76 31 2E 30 2E 36 20 5B 35 44 35 43 43 33 30 37 33 46 36 34 46 45 37 46 31 34 46 35 34 35 34 44 36 32 30 32 36 45 44 42 39 45 32 30 32 39 33 30 5D |

##