---
title: Property 2.1.2.3.7.3 Discover D-PAS Kernel Checksum (Contactless Only)
layout: home
parent: Configuration
nav_order: 175
---

## Property 2.1.2.3.7.3 Discover D-PAS Kernel Checksum (Contactless Only)

---

- [Property 2.1.2.3.7.3 Discover D-PAS Kernel Checksum (Contactless Only)](#property-212373-discover-d-pas-kernel-checksum-contactless-only)

---


Table 1054 - Property 2.1.2.3.7.3 Discover D-PAS Kernel Checksum
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
<td>2.1.2.3.7.3/ 0x020102030703</td>
</tr>
<tr>
<td>Name</td>
<td>Discover D-PAS Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Discover D-PAS Kernel
Checksum as string, no padding.</p>
<p>Example: DPAS 1.0 + TAS 00x -&gt; v1.3.42
[e28bf053de947cf6ad456a2a7c71059a2c5ac61e]</p></td>
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

Table 1055 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0C D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E7 02 C3 00 |

Table 1056 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0C D1 01 82 04 00 00 00 00 84 82 00 62 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 52 E1 50 E2 4E E3 4C E7 4A C3 48 44 50 41 53 20 31 2E 30 20 2B 20 54 41 53 20 30 30 78 20 2D 3E 20 76 31 2E 33 2E 34 32 20 5B 65 32 38 62 66 30 35 33 64 65 39 34 37 63 66 36 61 64 34 35 36 61 32 61 37 63 37 31 30 35 39 61 32 63 35 61 63 36 31 65 5D |

##