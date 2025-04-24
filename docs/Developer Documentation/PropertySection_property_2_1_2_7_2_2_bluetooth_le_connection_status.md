---
title: Property 2.1.2.7.2.2 Bluetooth® LE Connection Status
layout: home
parent: Configuration
nav_order: 209
---

## Property 2.1.2.7.2.2 Bluetooth® LE Connection Status

Table 1142 – Bluetooth® LE Connection Status

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
<td>2.1.2.7.2.2 / 0x020102070202</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Connection Status</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to report its Bluetooth® LE Connection
Status.</td>
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
<td><p>One byte value where each bit of the byte indicates a particular
status. Bit 0 is the least significant bit.<br />
<br />
Bit 0 is the advertising status. If set to 1 the device is advertising,
otherwise 0.</p>
<p>Bit 1 is the connection status. If set to 1 the device is in a
connection, otherwise 0.</p>
<p>Bit 2 is the secure connection status. If set to 1 the device is in a
secure connection, otherwise 0.</p>
<p>Bit 3 is the notification status. If set to 1 notifications are
enabled, otherwise 0.</p>
<p>Bits 4 to 7 are reserved and will be set to zero for now.</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1143 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020702 8902 C200 |

Table 1144 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501028704010207028903C20101 |

##