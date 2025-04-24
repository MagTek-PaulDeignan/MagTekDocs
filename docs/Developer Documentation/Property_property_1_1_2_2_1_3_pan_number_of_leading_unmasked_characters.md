---
title: Property 1.1.2.2.1.3 PAN Number of Leading Unmasked Characters
layout: home
parent: Configuration
nav_order: 37
---

## Property 1.1.2.2.1.3 PAN Number of Leading Unmasked Characters

---

- [Property 1.1.2.2.1.3 PAN Number of Leading Unmasked Characters](#property-112213-pan-number-of-leading-unmasked-characters)

---


Table 513 - Property 1.1.2.2.1.3 PAN Number of Leading Unmasked
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
<td>1.1.2.2.1.3 / 0x010102020103</td>
</tr>
<tr>
<td>Name</td>
<td>PAN Number of Leading Unmasked Characters</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine how many of the leading
characters of the PAN the device sends unmasked in <strong>Masked Track
x Data</strong> in ISO/ABA account information For details about ISO/ABA
track masking, see <strong>Property 1.1.2.2.1.2 ISO/ABA</strong> Masking
Character.</td>
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
<p>Max 0x08, if PAN length is less than 16, the number of unmasked
characters will be limited to 6.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x04</td>
</tr>
</tbody>
</table>

Table 514 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 18 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E2 04 E1 02 C3 00 |

Table 515 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 18 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C3 01 04 |

Table 516 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 10 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C3 01 04 |

Table 517 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 10 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C3 01 04 |

##