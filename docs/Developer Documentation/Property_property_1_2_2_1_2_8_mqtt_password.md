---
title: Property 1.2.2.1.2.8 MQTT Password
layout: home
parent: Configuration
nav_order: 97
---

## Property 1.2.2.1.2.8 MQTT Password

---

- [Property 1.2.2.1.2.8 MQTT Password](#property-122128-mqtt-password)

---


<table>
<caption><p>Table 787 - Property 1.2.2.1.2.8 MQTT
PasswordPassword</p></caption>
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
<td>1.2.2.1.2.8 / 0x010202010208</td>
</tr>
<tr>
<td>Name</td>
<td>MQTT Password</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to set the MQTT Password.</td>
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
<td>ASCII String with no spaces</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Any string</p>
<p>Example: emqx-tST1!</p></td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 8704 02020102 8902 C800 |

Table 788 -Get Request Example

<table>
<caption><p>Table 789 - Get Response Example</p></caption>
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
<td><p>AA0081048255D1018204000000008482002FD1018501018704020201028922C820</p>
<p>656D71782D745354312100000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

| Example (Hex) |
|----|
| AA00 81040155D111 842F D111 850101 870402020102 8922 C820 656d71782d7453543121000000000000 00000000000000000000000000000000 |

Table 790 - Set Request Example

<table>
<caption><p>Table 791 -Set Response Example</p></caption>
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
<td><p>AA0081048255D1118204000000008482002FD1118501018704020201028922C820</p>
<p>656D71782D745354312100000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

##