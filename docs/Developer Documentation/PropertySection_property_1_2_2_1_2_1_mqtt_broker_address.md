---
title: Property 1.2.2.1.2.1 MQTT Broker Address
layout: home
parent: Configuration
nav_order: 90
---

## Property 1.2.2.1.2.1 MQTT Broker Address

<table>
<caption><p>Table 752 - Property 1.2.2.1.2.1 MQTT Broker
Address</p></caption>
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
<td>1.2.2.1.2.1 / 0x010202010201</td>
</tr>
<tr>
<td>Name</td>
<td>MQTT Broker Address</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to connect to broker on network.
Address can be an URL or IP address.</td>
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
<td>64</td>
</tr>
<tr>
<td>Data Type</td>
<td>ASCII String with no spaces</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Any string</p>
<p>Example: test.mosquitto.org</p></td>
</tr>
<tr>
<td>Default</td>
<td>test.mosquitto.org</td>
</tr>
</tbody>
</table>

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 8704 02020102 8902 C100 |

Table 753 -Get Request Example

<table>
<caption><p>Table 754 -Get Response Example</p></caption>
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
<td><p>AA0081048255D1018204000000008482004FD1018501018704020201028942C140</p>
<p>746573742E6D6F7371756974746F2E6F726700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

| Example (Hex) |
|----|
| AA00 81040155D111 844F D111 850101 870402020102 8942 C140 746573742E6D6F7371756974746F2E6F 72670000000000000000000000000000 00000000000000000000000000000000 00000000000000000000000000000000 |

Table 755 -Set Request Example

<table>
<caption><p>Table 756 -Set Response Example</p></caption>
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
<td><p>AA0081048255D1118204000000008482004FD1118501018704020201028942C140</p>
<p>746573742E6D6F7371756974746F2E6F726700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

##