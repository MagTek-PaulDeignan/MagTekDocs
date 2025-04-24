---
title: Property 1.2.2.1.1.B Certificate Expiring Soon Notification Threshold
layout: home
parent: Configuration
nav_order: 83
---

## Property 1.2.2.1.1.B Certificate Expiring Soon Notification Threshold

Table 718 - Property 1.2.2.1.1.B Certificate Expiring Soon Notification
Threshold

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
<td>1.2.2.1.1.B / 0x01020201010B</td>
</tr>
<tr>
<td>Name</td>
<td>Certificate Expiring Soon Notification Threshold</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine how many days before a
certificate expires it should start notifying the host that it is about
to expire. If the value is set to 0, the notification will be
disabled.</p>
<p>The notification will only be sent if TLS is enabled, and the
notification will only be sent for they server certificate that the
device is configured to use. The notification will be sent every time
the first client connects to the device shortly after it connects.</p>
<p><strong>Notification 0x1001 - Device Information Update</strong>
category Key management, reason Certificate Expiring Soon is
related.</p></td>
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
<td>0x00 – 0xFF</td>
</tr>
<tr>
<td>Default</td>
<td>0x1E (30 days)</td>
</tr>
</tbody>
</table>

Table 719 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020101 8902 CB00 |

Table 720 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020201018903CB011E |

Table 721 - Set Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 8704 02020101 8903 CB011E |

Table 722 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020201018903CB011E |

##