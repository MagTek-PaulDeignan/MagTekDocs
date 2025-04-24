---
title: Property 1.2.3.2.1.1 System Volume Control
layout: home
parent: Configuration
nav_order: 124
---

## Property 1.2.3.2.1.1 System Volume Control

---

- [Property 1.2.3.2.1.1 System Volume Control](#property-123211-system-volume-control)

---


Table 911- Property 1.2.3.2.1.1 System Volume Control

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
<td>1.2.3.2.1.1 / 0x010203020101</td>
</tr>
<tr>
<td>Name</td>
<td>System Volume Control</td>
</tr>
<tr>
<td>Description</td>
<td><p>This property sets the output volume for all sounds the device
produces after startup, expressed as a percentage range from 0% (no
sound) to 100%. The volume setting takes effect immediately after the
host changes it.</p>
<p>Note that devices with limited volume control hardware allocate
ranges of numbers to represent the same physical volume level (for
example, 1..49 = Low, 50..100 = High).</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00..0x64</td>
</tr>
<tr>
<td>Default</td>
<td>0x32 (50%)</td>
</tr>
</tbody>
</table>

Table 912 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E3 06 E2 04 E1 02 C1 00 |

Table 913 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5E D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E2 05 E1 03 C1 01 32 |

Table 914 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5D D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E2 05 E1 03 C1 01 01 |

Table 915 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5D D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E2 05 E1 03 C1 01 01 |

#