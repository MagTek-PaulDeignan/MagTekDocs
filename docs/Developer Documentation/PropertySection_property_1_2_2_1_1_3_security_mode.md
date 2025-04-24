---
title: Property 1.2.2.1.1.3 Security Mode
layout: home
parent: Configuration
nav_order: 75
---

## Property 1.2.2.1.1.3 Security Mode

Table 678 - Property 1.2.2.1.1.3 Security Mode

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
<td>1.2.2.1.1.3 / 0x010202010103</td>
</tr>
<tr>
<td>Name</td>
<td>Security Mode</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine the authentication method
to be used to connect to an WiFi Access Point.</td>
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
<td><p>0x00 = PSK (Personal) Mode, requires <strong>Property 1.2.2.1.1.2
Password</strong></p>
<p>0x01 = EAP-PEAP (Enterprise) Mode, requires <strong>Property
1.2.2.1.1.2 Password</strong>, <strong>Property 1.2.2.1.1.C
Username</strong></p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 679 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040103D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C300 |

Table 680 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048203D101 820400000000 8482001BD101 81072B06010401F609 850101 890BE209E207E105E103C30100 |

Table 681 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040104D111 841BD111 81072B06010401F609 850101 890BE209E207E105E103C30101 |

Table 682 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048204D111 820400000000 8482001BD111 81072B06010401F609 850101 890BE209E207E105E103C30101 |

##