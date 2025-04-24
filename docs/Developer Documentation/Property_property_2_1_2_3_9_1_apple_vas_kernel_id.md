---
title: Property 2.1.2.3.9.1 Apple VAS Kernel ID
layout: home
parent: Configuration
nav_order: 179
---

## Property 2.1.2.3.9.1 Apple VAS Kernel ID

---

- [Property 2.1.2.3.9.1 Apple VAS Kernel ID](#property-212391-apple-vas-kernel-id)

---


Table 1066 - Property 2.1.2.3.9.1 Apple VAS Kernel ID

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
<td>2.1.2.3.9.1 / 0x020102030901</td>
</tr>
<tr>
<td>Name</td>
<td>Apple VAS Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Apple VAS Kernel ID
as a string, padded with null characters.</p>
<p>Example: APPLE VAS 1.0.0</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16</td>
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

Table 1067 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E9 02 C1 00 |

Table 1068 - Get Response Example

| Example (Hex) |
|----|
| AA008104820ED1018204000000008482002AD10181072B06010401F609850102891AE118E216E314E912C1104150504C452056415320312E302E3000 |

##