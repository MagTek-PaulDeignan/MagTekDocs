---
title: Property 1.2.1.1.1.1 Device-Driven Fallback Behavior (MSR Only)
layout: home
parent: Configuration
nav_order: 55
---

## Property 1.2.1.1.1.1 Device-Driven Fallback Behavior (MSR Only)

Table 583 - Property 1.2.1.1.1.1 Device-Driven Fallback Behavior (MSR
Only)

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
<td>1.2.1.1.1.1 / 0x010201010101</td>
</tr>
<tr>
<td>Name</td>
<td>Device-Driven Fallback Behavior</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine whether it should
automatically implement payment brand fallback rules without host
intervention when running <strong>Command 0x1001 - Start
Transaction</strong>.</td>
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
<td><p>0x00 = No device-driven fallback</p>
<p>0x01 = Device-driven fallback enabled</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x01</td>
</tr>
</tbody>
</table>

Table 584 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 04 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E1 02 C1 00 |

Table 585 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 04 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E1 03 C1 01 01 |

Table 586 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 02 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E1 03 C1 01 01 |

Table 587 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 02 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E1 03 C1 01 01 |

##