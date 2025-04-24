---
title: Property 1.2.2.3.1.7 Bluetooth® LE Minimum Advertising Interval
layout: home
parent: Configuration
nav_order: 110
---

## Property 1.2.2.3.1.7 Bluetooth® LE Minimum Advertising Interval

Table 846 - Property 1.2.2.3.1.7 Bluetooth® LE Minimum Advertising
Interval

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
<td>1.2.2.3.1.7 / 0x010202030107</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Minimum Advertising Interval</td>
</tr>
<tr>
<td>Description</td>
<td><p>This two property, in most significant byte order, contains the
device’s minimum Bluetooth® LE advertising interval in 625 microsecond
increments. This property, combined with <strong>Property 1.2.2.3.1.8
Bluetooth® LE Maximum Advertising Interval,</strong> specifies the
Bluetooth® LE advertising interval the device uses. Smaller advertising
intervals cause the device to consume more power when advertising, which
may be a concern when running on battery power.</p>
<p>Only values between 32 (20ms) and 65535 (40.96s) are valid. The host
may need to adjust the maximum advertising interval property when
changing this property; if the maximum advertising interval is less than
the minimum, the device may behave unpredictably.</p>
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
<td>0x00 0x20 (32) - 0xFF 0xFF (65535) MSB first</td>
</tr>
<tr>
<td>Default</td>
<td>0x00 0xA0 = 160 (100 milliseconds)</td>
</tr>
</tbody>
</table>

Table 847 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102C700 |

Table 848 - Get Response Example

| Example (Hex) |
|----|
| AA0081048232D1018204000000008482001CD10181072B06010401F609850101890CE20AE208E306E104C70200A0 |

Table 849 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D111841CD11181072B06010401F609850101890CE20AE208E306E104C70200B0 |

Table 850 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D1118204000000008482001CD11181072B06010401F609850101890CE20AE208E306E104C70200B0 |

##