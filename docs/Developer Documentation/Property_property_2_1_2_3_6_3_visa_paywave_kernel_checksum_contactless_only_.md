---
title: Property 2.1.2.3.6.3 Visa payWave Kernel Checksum (Contactless Only)
layout: home
parent: Configuration
nav_order: 171
---

## Property 2.1.2.3.6.3 Visa payWave Kernel Checksum (Contactless Only)

---

- [Property 2.1.2.3.6.3 Visa payWave Kernel Checksum (Contactless Only)](#property-212363-visa-paywave-kernel-checksum-contactless-only)

---


Table 1042 - Property 2.1.2.3.6.3 Visa payWave Kernel Checksum
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
<td>2.1.2.3.6.3/ 0x020102030603</td>
</tr>
<tr>
<td>Name</td>
<td>Visa payWave Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Visa payWave Kernel
Checksum as string, no padding.</p>
<p>Example: VCPS 2.2x [00000000]-&gt; v1.5.6
[F1CBB8A23E00984E9E753EF4884C33EA368E570C]</p></td>
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

Table 1043 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E6 02 C3 00 |

Table 1044 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 62 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 52 E1 50 E2 4E E3 4C E6 4A C3 48 56 43 50 53 20 32 2E 32 78 20 5B 30 30 30 30 30 30 30 30 5D 2D 3E 20 76 31 2E 35 2E 36 20 5B 46 31 43 42 42 38 41 32 33 45 30 30 39 38 34 45 39 45 37 35 33 45 46 34 38 38 34 43 33 33 45 41 33 36 38 45 35 37 30 43 5D |

##