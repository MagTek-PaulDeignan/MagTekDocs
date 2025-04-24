---
title: Property 1.2.3.1.2.1 Display Orientation (Display Only)
layout: home
parent: Configuration
nav_order: 120
---

## Property 1.2.3.1.2.1 Display Orientation (Display Only)

Table 891- Property 1.2.3.1.2.1 Display Orientation (Display Only)

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
<td>1.2.3.1.2.1 / 0x010203010201</td>
</tr>
<tr>
<td>Name</td>
<td>Display Orientation</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to set the orientation of the display.
There are four modes: Landscape with magnetic stripe reader (MSR) on the
top, Landscape with MSR on the bottom, Portrait with MSR on the right,
and Portrait with MSR on the left. This property does not take effect
immediately, it takes effect the next time the device transitions to
idle (for example, after a transaction or after power cycle /
reset).</td>
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
<td><p>0x00 = Landscape with MSR on Top</p>
<p>0x01 = Portrait with MSR on Right</p>
<p>0x02 = Portrait with MSR on Left</p>
<p>0x03 = Landscape with MSR on Bottom</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 892 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E3 06 E1 04 E2 02 C1 00 |

Table 893 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5E D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E2 03 C1 01 00 |

Table 894 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5D D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E2 03 C1 01 01 |

Table 895 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5D D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E2 03 C1 01 01 |

##