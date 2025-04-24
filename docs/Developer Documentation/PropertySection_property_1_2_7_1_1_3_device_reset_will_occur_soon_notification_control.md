---
title: Property 1.2.7.1.1.3 Device Reset Will Occur Soon Notification Control
layout: home
parent: Configuration
nav_order: 132
---

## Property 1.2.7.1.1.3 Device Reset Will Occur Soon Notification Control

Table 941 - Property 1.2.7.1.1.3 Device Reset Will Occur Soon
Notification Control

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
<td>1.2.7.1.1.3 / 0x010207010103</td>
</tr>
<tr>
<td>Name</td>
<td>Device Reset Will Occur Soon Notification Control</td>
</tr>
<tr>
<td>Description</td>
<td><p>The host can use this property to control behavior of the
<strong>Device Reset Will Occur Soon</strong> notification in
<strong>Notification 0x1001 - Device Information Update</strong>.</p>
<p>See <strong>24 Hour Automatic Reset PCI Requirement</strong> for more
information.</p>
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
<p>0x01..0xFF = Number of minutes before a reset to send the
notification message.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x03</td>
</tr>
</tbody>
</table>

Table 942 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 01 84 0F D1 01 85 01 01 87 04 02 07 01 01 89 02 C3 00 |

Table 943 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 10 D1 01 85 01 01 87 04 02 07 01 01 89 03 C3 01 05 |

Table 944 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 10 D1 11 85 01 01 87 04 02 07 01 01 89 03 C1 01 05 |

Table 8‑115 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 02 07 01 01 89 03 C1 01 05 |

##