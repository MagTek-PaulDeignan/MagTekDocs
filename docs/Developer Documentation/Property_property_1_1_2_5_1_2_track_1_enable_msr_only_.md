---
title: Property 1.1.2.5.1.2 Track 1 Enable (MSR Only)
layout: home
parent: Configuration
nav_order: 49
---

## Property 1.1.2.5.1.2 Track 1 Enable (MSR Only)

---

- [Property 1.1.2.5.1.2 Track 1 Enable (MSR Only)](#property-112512-track-1-enable-msr-only)

---


Table 563 - Property 1.1.2.5.1.2 Track 1 Enable (MSR Only)

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
<td>1.1.2.5.1.2 / 0x010102050102</td>
</tr>
<tr>
<td>Name</td>
<td>Track 1 Enable</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine whether it should read
include or suppress Track 1 data when reading and transmitting ISO/ABA
account information from a card’s magnetic stripe.</td>
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
<td><p>0x00 = Disabled</p>
<p>0x01 = Enabled</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x01</td>
</tr>
</tbody>
</table>

Table 564 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1C D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E5 04 E1 02 C2 00 |

Table 565 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 1C D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C2 01 01 |

Table 566 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 17 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C2 01 01 |

Table 567 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 17 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C2 01 01 |

##