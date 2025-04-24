---
title: Property 2.1.2.3.7.2 Discover D-PAS Kernel Firmware Part Number (Contactless Only)
layout: home
parent: Configuration
nav_order: 174
---

## Property 2.1.2.3.7.2 Discover D-PAS Kernel Firmware Part Number (Contactless Only)

---

- [Property 2.1.2.3.7.2 Discover D-PAS Kernel Firmware Part Number (Contactless Only)](#property-212372-discover-d-pas-kernel-firmware-part-number-contactless-only)

---


Table 1051 – Property 2.1.2.3.7.2 Discover D-PAS Kernel Firmware Part
Number (Contactless Only)

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
<td>2.1.2.3.7.2 / 0x020102030702</td>
</tr>
<tr>
<td>Name</td>
<td>Discover D-PAS Firmware Part Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Discover D-PAS Kernel
Part Number as string, padded with null characters.</p>
<p>Example: 1000007181 Ver A0</p></td>
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

Table 1052 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 09 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E7 02 C2 00 |

Table 1053 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 09 D1 01 82 04 00 00 00 00 84 82 00 2C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1C E1 1A E2 18 E3 16 E7 14 C2 12 31 30 30 30 30 30 37 31 38 31 20 56 65 72 20 41 30 00 |

##