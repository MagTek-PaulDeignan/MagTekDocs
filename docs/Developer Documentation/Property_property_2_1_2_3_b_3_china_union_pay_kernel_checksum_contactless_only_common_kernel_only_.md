---
title: Property 2.1.2.3.B.3 China Union Pay Kernel Checksum (Contactless Only) (Common Kernel Only)
layout: home
parent: Configuration
nav_order: 187
---

## Property 2.1.2.3.B.3 China Union Pay Kernel Checksum (Contactless Only) (Common Kernel Only)

---

- [Property 2.1.2.3.B.3 China Union Pay Kernel Checksum (Contactless Only) (Common Kernel Only)](#property-2123b3-china-union-pay-kernel-checksum-contactless-only-common-kernel-only)

---


Table 1090 - Property 2.1.2.3.B.3 China Union Pay Kernel Checksum
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
<td>2.1.2.3.B.3/ 0x020102030B03</td>
</tr>
<tr>
<td>Name</td>
<td>China Union Pay Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the China Union Pay
Kernel Checksum as string, no padding.</p>
<p>Example: CUP v1.0.2 -&gt; v1.3.40
[23e9bc82b4ecbf422c2054c91914848017e0ed0f]</p></td>
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

Table 1091 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 11 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EB 02 C3 00 |

Table 1092 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 5A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 4A E1 48 E2 46 E3 44 EB 42 C3 40 43 55 50 20 76 31 2E 30 2E 32 20 2D 3E 20 76 31 2E 33 2E 34 30 20 5B 32 33 65 39 62 63 38 32 62 34 65 63 62 66 34 32 32 63 32 30 35 34 63 39 31 39 31 34 38 34 38 30 31 37 65 30 65 64 30 66 5D |

##