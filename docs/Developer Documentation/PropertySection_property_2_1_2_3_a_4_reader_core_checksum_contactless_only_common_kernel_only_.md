---
title: Property 2.1.2.3.A.4 Reader Core Checksum (Contactless Only) (Common Kernel Only)
layout: home
parent: Configuration
nav_order: 183
---

## Property 2.1.2.3.A.4 Reader Core Checksum (Contactless Only) (Common Kernel Only)

Table 1078 - Property 2.1.2.3.A.4 Reader Core Checksum (Contactless
Only) (Common Kernel Only)

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
<td>2.1.2.3.A.4/ 0x020102030A04</td>
</tr>
<tr>
<td>Name</td>
<td>Reader Core Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Reader Core Checksum
as string, no padding.</p>
<p>Example: 371835cedcd7f8a3e4cf8b32cc03803dfdc1f507</p></td>
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

Table 1079 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 11 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EA 02 C4 00 |

Table 1080 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 42 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 32 E1 30 E2 2E E3 2C EA 2A C4 28 33 37 31 38 33 35 63 65 64 63 64 37 66 38 61 33 65 34 63 66 38 62 33 32 63 63 30 33 38 30 33 64 66 64 63 31 66 35 30 37 |

##