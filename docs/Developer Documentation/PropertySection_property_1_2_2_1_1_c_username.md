---
title: Property 1.2.2.1.1.C Username
layout: home
parent: Configuration
nav_order: 84
---

## Property 1.2.2.1.1.C Username

Table 723 - Property 1.2.2.1.1.C Username

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
<td>1.2.2.1.1.C / 0x01020201010C</td>
</tr>
<tr>
<td>Name</td>
<td>Username</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set up the Username for EAP-PEAP
authentication method which is used to connect to an WiFi Access Point.
Username is not used by</p>
<p>PSK authentication method.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>N/A</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>32</td>
</tr>
<tr>
<td>Data Type</td>
<td>ASCII String</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Example: joe@MagTek.com</td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 724 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104010DD101 841AD101 81072B06010401F609 850101 890AE208E206E104E102CC00 |

Table 725 - Get Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104820DD101 820400000000 8482003AD101 81072B06010401F609
850101</p>
<p>892AE228E226E124E122CC
206A6F65406D616774656B2E636F6D00000000000000</p>
<p>0000000000000000000000</p></td>
</tr>
</tbody>
</table>

Table 726 - Set Request Example

| Example (Hex) |
|----|
| AA00 8104010ED111 843AD111 81072B06010401F609 850101 892AE228E226E124E122CC 206A6F65406D616774656B2E636F6D000000000000000000 |

Table 727 - Set Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104820ED111 820400000000 8482003AD111 81072B06010401F609
850101</p>
<p>892AE228E226E124E122CC 206A6F65406D616774656B2E636F6D</p>
<p>000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

##