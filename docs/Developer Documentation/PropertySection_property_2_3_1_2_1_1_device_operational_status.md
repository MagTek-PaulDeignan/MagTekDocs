---
title: Property 2.3.1.2.1.1 Device Operational Status
layout: home
parent: Configuration
nav_order: 230
---

## Property 2.3.1.2.1.1 Device Operational Status

Table 1184 - Property 2.3.1.2.1.1 Device Operational Status

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
<td>2.3.1.2.1.1 / 0x020301020101</td>
</tr>
<tr>
<td>Name</td>
<td>Device Operational Status</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its operational
status.</p>
<p><strong>Online</strong> is the status the manufacturer populates in
this property before shipping, and is the result of the device going
through processes that configure its security subsystems and features.
In this state, the device is fully functional and can perform
transactions.</p>
<p><strong>Offline</strong> means the device is no longer fully
functional and can no longer perform transactions. The device
automatically transitions to this state if it detects a problem with
security or any of the subsystems it checks. For example, trying to open
the device triggers a tamper response, which causes the device to change
its operational status to Offline. To retrieve more information about
the cause of an Offline status, the host can retrieve <strong>Property
2.3.1.2.1.2 Offline Status Detail</strong>.</p></td>
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
<td><p>0x01 = Offline</p>
<p>0x02 = Online</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1185 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010201 8902 C100 |

Table 1186 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010201 8903 C101 02 |

##