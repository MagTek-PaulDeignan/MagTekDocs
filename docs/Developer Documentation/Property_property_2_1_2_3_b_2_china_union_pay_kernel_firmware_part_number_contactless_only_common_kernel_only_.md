---
title: Property 2.1.2.3.B.2 China Union Pay Kernel Firmware Part Number (Contactless Only) (Common Kernel Only)
layout: home
parent: Configuration
nav_order: 186
---

## Property 2.1.2.3.B.2 China Union Pay Kernel Firmware Part Number (Contactless Only) (Common Kernel Only)

---

- [Property 2.1.2.3.B.2 China Union Pay Kernel Firmware Part Number (Contactless Only) (Common Kernel Only)](#property-2123b2-china-union-pay-kernel-firmware-part-number-contactless-only-common-kernel-only)

---


Table 1087 – Property 2.1.2.3.B.2 China Union Pay Kernel Firmware Part
Number (Contactless Only) (Common Kernel Only)

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
<td>2.1.2.3.B.2 / 0x020102030B02</td>
</tr>
<tr>
<td>Name</td>
<td>China Union Pay Firmware Part Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the China Union Pay Part
Number as string, padded with null characters.</p>
<p>Example: 1000009651 Ver AA0</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>18</td>
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

Table 1088 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0F D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EB 02 C2 00 |

Table 1089 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 2D D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1D E1 1B E2 19 E3 17 EB 15 C2 13 31 30 30 30 30 30 39 36 35 31 20 56 65 72 20 41 41 30 00 |

##