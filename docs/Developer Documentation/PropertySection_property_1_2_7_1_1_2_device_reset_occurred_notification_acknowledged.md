---
title: Property 1.2.7.1.1.2 Device Reset Occurred Notification Acknowledged
layout: home
parent: Configuration
nav_order: 131
---

## Property 1.2.7.1.1.2 Device Reset Occurred Notification Acknowledged

Table 936 - Property 1.2.7.1.1.2 Device Reset Occurred Notification
Acknowledged

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
<td>1.2.7.1.1.2 / 0x010207010102</td>
</tr>
<tr>
<td>Name</td>
<td>Device Reset Occurred Notification Acknowledged</td>
</tr>
<tr>
<td>Description</td>
<td><p>The host can use this property to acknowledge it has received the
<strong>Device Reset Occurred</strong> notification in
<strong>Notification 0x1001 - Device Information Update</strong> and to
request that the device stop sending it.</p>
<p>Alternatively, because the device automatically sets the value of
this property to 0x00 on boot, the host can use this property to detect
power cycles or resets using a polling method. To implement this, the
host should read the value on a set schedule (for example, every 2
seconds). If the host finds a value of 0x00, a power cycle or reset has
occurred, and the host should set the value back to 0x01. From that
point until the next power cycle or reset, the value will remain
0x01.</p>
<p>Changes made to this property will not persist after a power cycle or
reset. After a power cycle or reset, this property has a value of 0x00
until the host changes it to 0x01.</p></td>
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
<td><p>0x00 = Not acknowledged. Only the device can set to this
value.</p>
<p>0x01 = Acknowledged. Do not continue to send the
notification.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 937 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02070101 8902 C200 |

Table 938 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D101 8204 00000000 84820010 D101 8501 01 8704 02070101 8903 C201 00 |

Table 939 - Set Request Example

| Example (Hex)                                                 |
|---------------------------------------------------------------|
| AA00 81040155D111 8410 D111 8501 01 8704 02070101 8903 C20101 |

Table 940 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D111 8204 00000000 84820010 D111 8501 01 8704 02070101 8903 C201 01 |

##