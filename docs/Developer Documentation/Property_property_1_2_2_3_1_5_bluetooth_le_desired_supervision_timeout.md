---
title: Property 1.2.2.3.1.5 Bluetooth® LE Desired Supervision Timeout
layout: home
parent: Configuration
nav_order: 108
---

## Property 1.2.2.3.1.5 Bluetooth® LE Desired Supervision Timeout

---

- [Property 1.2.2.3.1.5 Bluetooth® LE Desired Supervision Timeout](#property-122315-bluetooth®-le-desired-supervision-timeout)

---


Table 836 - Property 1.2.2.3.1.5 Bluetooth® LE Desired Supervision
Timeout

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
<td>1.2.2.3.1.5 / 0x010202030105</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Desired Supervision Timeout</td>
</tr>
<tr>
<td>Description</td>
<td><p>This two-byte property, in most significant byte order, contains
the value of the Timeout Multiplier sent in 10 millisecond units that
the device sends to a Bluetooth® LE host in a CONNECTION PARAMETER
UPDATE REQUEST. See the Core Bluetooth® Specification for details. Only
values between 10 and 3200 are valid.</p>
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
<td>0x00 0x0A (10) - 0x0C 0x80 (3200) MSB first</td>
</tr>
<tr>
<td>Default</td>
<td>0x01 0xF4 (5000 milliseconds)</td>
</tr>
</tbody>
</table>

Table 837 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102C500 |

Table 838 - Get Response Example

| Example (Hex) |
|----|
| AA0081048232D1018204000000008482001CD10181072B06010401F609850101890CE20AE208E306E104C50201F4 |

Table 839 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D111841CD11181072B06010401F609850101890CE20AE208E306E104C50201F4 |

Table 840 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D1118204000000008482001CD11181072B06010401F609850101890CE20AE208E306E104C50201F4 |

##