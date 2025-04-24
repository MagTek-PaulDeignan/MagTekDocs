---
title: Property 2.1.2.3.C.3 Interact Flash Kernel Checksum (Contactless Only) (Common Kernel Only)
layout: home
parent: Configuration
nav_order: 190
---

## Property 2.1.2.3.C.3 Interact Flash Kernel Checksum (Contactless Only) (Common Kernel Only)

Table 1099 - Property 2.1.2.3.C.3 Interact Flash Kernel Checksum
(Contactless Only) (Common Kernel Only)

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
<td>2.1.2.3.C.3/ 0x020102030C03</td>
</tr>
<tr>
<td>Name</td>
<td>Interact Flash Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Interact Flash Kernel
Checksum as string, no padding.</p>
<p>Example: Flash 1.9 -&gt; v1.3.41
[394e45aed865e276e4f6737de26aa84c6eb1b174]</p></td>
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

Table 1100 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 11 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EC 02 C3 00 |

Table 1101 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 59 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 49 E1 47 E2 45 E3 43 EC 41 C3 3F 46 6C 61 73 68 20 31 2E 39 20 2D 3E 20 76 31 2E 33 2E 34 31 20 5B 33 39 34 65 34 35 61 65 64 38 36 35 65 32 37 36 65 34 66 36 37 33 37 64 65 32 36 61 61 38 34 63 36 65 62 31 62 31 37 34 5D |

#