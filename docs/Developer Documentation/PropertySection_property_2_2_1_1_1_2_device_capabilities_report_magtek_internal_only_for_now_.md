---
title: Property 2.2.1.1.1.2 Device Capabilities Report (MAGTEK INTERNAL ONLY FOR NOW)
layout: home
parent: Configuration
nav_order: 217
---

## Property 2.2.1.1.1.2 Device Capabilities Report (MAGTEK INTERNAL ONLY FOR NOW)

Table 1157 - Property 2.2.1.1.1.2 Device Capabilities Report (MAGTEK
INTERNAL ONLY FOR NOW)

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
<td>2.2.1.1.1.2 / 0x020201010102</td>
</tr>
<tr>
<td>Name</td>
<td>Device Capabilities Report</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its capabilities in
string format padded with null characters.</p>
<p>Example: “V=1,SC=1,SR=1,UDE=0,CE=2,CLE=2,BT=0,WF=0”</p>
<ul>
<li><p>V = Version</p></li>
<li><p>SC = Signature Capture</p></li>
<li><p>SR = SRED</p></li>
<li><p>UDE = Cardholder Data Entry Mode</p></li>
<li><p>CE = Contact EMV Level Supported</p></li>
<li><p>CLE = Contactless Level Supported</p></li>
<li><p>BT = Bluetooth®</p></li>
<li><p>WF = Wireless LAN (WLAN)</p></li>
</ul></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>64</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>64</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1158 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 E0 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E2 08 E1 06 E1 04 E1 02 C2 00 |

Table 1159 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 E0 D1 01 82 04 00 00 00 00 84 82 00 5A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 4A E2 48 E1 46 E1 44 E1 42 C2 40 56 3D 31 2C 53 43 3D 31 2C 53 52 3D 31 2C 55 44 45 3D 30 2C 43 45 3D 32 2C 43 4C 45 3D 32 2C 42 54 3D 30 2C 57 46 3D 30 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |

##