---
title: Property 1.2.2.3.1.2 Bluetooth® LE Desired Minimum Connection Interval
layout: home
parent: Configuration
nav_order: 105
---

## Property 1.2.2.3.1.2 Bluetooth® LE Desired Minimum Connection Interval

Table 821 - Property 1.2.2.3.1.2 Bluetooth® LE Desired Minimum
Connection Interval

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
<td>1.2.2.3.1.2 / 0x010202030102</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Desired Minimum Connection Interval</td>
</tr>
<tr>
<td>Description</td>
<td><p>This two-byte property, in most significant byte order, contains
the Interval Min value in 1.25 millisecond units that the device sends
to a Bluetooth® LE host in a CONNECTION PARAMETER UPDATE REQUEST. See
the Core Bluetooth® Specification for details. Only values between 6 and
3200 are valid.</p>
<p>After the host changes this property, the device must be reset before
the changes will take effect.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 0x06 (6) - 0x0C 0x80 (3200) MSB first</td>
</tr>
<tr>
<td>Default</td>
<td>0x00 0x0C (15.0 milliseconds)</td>
</tr>
</tbody>
</table>

Table 822 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102C200 |

Table 823 - Get Response Example

| Example (Hex) |
|----|
| AA0081048232D1018204000000008482001CD10181072B06010401F609850101890CE20AE208E306E104C202000C |

Table 824 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D111841CD11181072B06010401F609850101890CE20AE208E306E104C2020010 |

Table 825 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D1118204000000008482001CD11181072B06010401F609850101890CE20AE208E306E104C2020010 |

##