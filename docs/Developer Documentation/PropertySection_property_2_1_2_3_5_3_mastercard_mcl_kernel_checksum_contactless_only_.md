---
title: Property 2.1.2.3.5.3 Mastercard MCL Kernel Checksum (Contactless Only)
layout: home
parent: Configuration
nav_order: 168
---

## Property 2.1.2.3.5.3 Mastercard MCL Kernel Checksum (Contactless Only)

Table 1033 - Property 2.1.2.3.5.3 Mastercard MCL Kernel Checksum
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
<td>2.1.2.3.5.3/ 0x020102030503</td>
</tr>
<tr>
<td>Name</td>
<td>Mastercard MCL Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Mastercard MCL Kernel
Checksum as string, no padding.</p>
<p>Example: C2.2.8 -&gt; v1.0.2
[ade94c13b0c6a31f1be682b12536528264b1efc0]</p></td>
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

Table 1034 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 2A D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E5 02 C3 00 |

Table 1035 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 2A D1 01 82 04 00 00 00 00 84 82 00 55 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 45 E1 43 E2 41 E3 3F E5 3D C3 3B 43 32 2E 32 2E 38 20 2D 3E 20 76 31 2E 30 2E 32 20 5B 61 64 65 39 34 63 31 33 62 30 63 36 61 33 31 66 31 62 65 36 38 32 62 31 32 35 33 36 35 32 38 32 36 34 62 31 65 66 63 30 5D |

##