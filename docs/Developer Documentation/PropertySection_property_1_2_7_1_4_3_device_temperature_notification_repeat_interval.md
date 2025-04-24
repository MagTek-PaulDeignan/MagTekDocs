---
title: Property 1.2.7.1.4.3 Device Temperature Notification Repeat Interval
layout: home
parent: Configuration
nav_order: 139
---

## Property 1.2.7.1.4.3 Device Temperature Notification Repeat Interval

Table 971 - Property 1.2.7.1.4.3 Device Temperature Notification Repeat
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
<td>1.2.7.1.4.3 / 0x010207010403</td>
</tr>
<tr>
<td>Name</td>
<td>Device Temperature Notification Repeat Interval</td>
</tr>
<tr>
<td>Description</td>
<td><p>While the device’s temperature is outside of the range defined by
Device Low Temperature Notification Level (1.2.7.1.4.1) and Device High
Temperature Notification Level (1.2.7.1.4.2), notifications will be sent
to the host. This property sets the period between notifications.</p>
<p>The Device Temperature Notification Repeat Interval takes effect
immediately after the host changes it.</p></td>
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
<td><p>0x00 Send once. Do not repeat.</p>
<p>0x0F .. 0xFF Repeat period in seconds. Must be multiple of 0x0F
(15).</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x1E (30 seconds)</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table 972 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02070104 8902 C300 |

Table 8.3‑235 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D101 8204 00000000 84820010 D101 8501 01 8704 02070104 8903 C301 1E |

Table 8.36 - Set Request Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA00 81040155D111 8410 D111 8501 01 8704 02070104 8903 C301 1E |

Table 8.3‑237 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D111 8204 00000000 84820010 D111 8501 01 870402070104 8903 C301 1E |