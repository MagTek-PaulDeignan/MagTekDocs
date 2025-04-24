---
title: Property 2.3.1.2.1.2 Offline Status Detail
layout: home
parent: Configuration
nav_order: 231
---

## Property 2.3.1.2.1.2 Offline Status Detail

Table 1187 - Property 2.3.1.2.1.2 Offline Status Detail

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
<td>2.3.1.2.1.2 / 0x020301020102</td>
</tr>
<tr>
<td>Name</td>
<td>Offline Status Detail</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the status of every
subsystem that can cause the device’s operation status to be set to
<strong>Offline</strong> in <strong>Property 2.3.1.2.1.1 Device
Operational</strong> Status.</p>
<p>The property consists of a sequence of bytes where each bit in each
byte represents the status of a subsystem. If a bit is set to one, then
there is a problem with the subsystem, otherwise no problem was
detected.</p>
<p>Some subsystems provide other properties or commands that can be used
to get more information about the subsystem’s status. For example,
<strong>Property 2.3.1.1.2.2 Tamper Sensors Activated</strong> and
<strong>Property 2.3.1.1.2.3 Tamper Sensor Tampered</strong>.</p></td>
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
<td>16 (reserved for future expansion)</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Byte 0</p>
<ul>
<li><p>Bit 0 = Tamper problem present</p></li>
<li><p>Bit 1 = Master Key problem present</p></li>
<li><p>Bit 2 = Keys and Certificates problem present</p></li>
<li><p>Bit 3 = Real Time Clock problem present</p></li>
<li><p>Bit 4 = Random Number Generator problem present</p></li>
<li><p>Bit 5 = Cryptography Engine problem present</p></li>
<li><p>Bit 6 = Magnetic Stripe Reader Hardware problem present</p></li>
<li><p>Bit 7 = Reserved</p></li>
</ul></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1188 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010201 8902 C200 |

Table 1189 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010201 8903 C201 00 |

##