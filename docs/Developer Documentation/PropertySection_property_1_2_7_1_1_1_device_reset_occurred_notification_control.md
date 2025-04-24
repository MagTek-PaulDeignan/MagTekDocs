---
title: Property 1.2.7.1.1.1 Device Reset Occurred Notification Control
layout: home
parent: Configuration
nav_order: 130
---

## Property 1.2.7.1.1.1 Device Reset Occurred Notification Control

Table 931 - Property 1.2.7.1.1.1 Device Reset Occurred Notification
Control

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
<td>1.2.7.1.1.1 / 0x010207010101</td>
</tr>
<tr>
<td>Name</td>
<td>Device Reset Occurred Notification Control</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to control behavior of the
<strong>Device Reset Occurred</strong> notification in
<strong>Notification 0x1001 - Device Information Update</strong>.</p>
<p>Changes to this property do not take effect until the device is power
cycled or reset.</p></td>
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
<td><p>0x00 = Never send this notification.</p>
<p>0x01..0xFE = The frequency in seconds the device should repeat
sending the notification until the host requests that it stop with
<strong>Property 1.2.7.1.1.2 Device Reset Occurred Notification
Acknowledged</strong>.</p>
<p>0xFF = Only send this notification once.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 932 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 01 84 0F D1 01 85 01 01 87 04 02 07 01 01 89 02 C1 00 |

Table 933 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 10 D1 01 85 01 01 87 04 02 07 01 01 89 03 C1 01 00 |

Table 934 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 10 D1 11 85 01 01 87 04 02 07 01 01 89 03 C1 01 05 |

Table 935 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 02 07 01 01 89 03 C1 01 05 |

##