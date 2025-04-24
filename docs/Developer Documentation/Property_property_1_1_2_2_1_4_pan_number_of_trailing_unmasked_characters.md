---
title: Property 1.1.2.2.1.4 PAN Number of Trailing Unmasked Characters
layout: home
parent: Configuration
nav_order: 38
---

## Property 1.1.2.2.1.4 PAN Number of Trailing Unmasked Characters

---

- [Property 1.1.2.2.1.4 PAN Number of Trailing Unmasked Characters](#property-112214-pan-number-of-trailing-unmasked-characters)

---


Table 518 - Property 1.1.2.2.1.4 PAN Number of Trailing Unmasked
Characters

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
<td>1.1.2.2.1.4 / 0x010102020104</td>
</tr>
<tr>
<td>Name</td>
<td>PAN Number of Trailing Unmasked Characters</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine how many of the trailing
characters of the PAN the device sends unmasked in <strong>Masked Track
x Data</strong> in ISO/ABA account information For details about ISO/ABA
track masking, see <strong>Property 1.1.2.2.1.2 ISO/ABA Masking
Character</strong>.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Min 0x00</p>
<p>Max 0x04</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x04</td>
</tr>
</tbody>
</table>

Table 519 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 19 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E2 04 E1 02 C4 00 |

Table 520 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 19 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C4 01 04 |

Table 521 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 11 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C4 01 04 |

Table 522 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 11 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C4 01 04 |

##