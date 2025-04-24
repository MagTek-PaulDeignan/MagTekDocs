---
title: Property 2.1.2.3.3.3 EMV Contact L2 Kernel Checksum (Contact Only)
layout: home
parent: Configuration
nav_order: 161
---

## Property 2.1.2.3.3.3 EMV Contact L2 Kernel Checksum (Contact Only)

Table 1012 - Property 2.1.2.3.3.3 EMV Contact L2 Kernel Checksum
(Contact Only)

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
<td>2.1.2.3.3.3/ 0x020102030303</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contact L2 Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contact L2 Kernel
Checksum as string, no padding.</p>
<p>Example: vxxCAAgnos33_17
b54f31bcb61a26fc823bce9ab8989b31ab90f9a4</p></td>
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

Table 1013 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1B D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E3 02 C3 00 |

Table 1014 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 1B D1 01 82 04 00 00 00 00 84 82 00 52 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 42 E1 40 E2 3E E3 3C E3 3A C3 38 76 78 78 43 41 41 67 6E 6F 73 33 33 5F 31 37 20 62 35 34 66 33 31 62 63 62 36 31 61 32 36 66 63 38 32 33 62 63 65 39 61 62 38 39 38 39 62 33 31 61 62 39 30 66 39 61 34 |

##