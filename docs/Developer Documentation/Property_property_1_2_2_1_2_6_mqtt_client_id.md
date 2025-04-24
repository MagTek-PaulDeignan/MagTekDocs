---
title: Property 1.2.2.1.2.6 MQTT Client ID
layout: home
parent: Configuration
nav_order: 95
---

## Property 1.2.2.1.2.6 MQTT Client ID

---

- [Property 1.2.2.1.2.6 MQTT Client ID](#property-122126-mqtt-client-id)

---


<table>
<caption><p>Table 777 -Property 1.2.2.1.2.6 MQTT Client IDClient
ID</p></caption>
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
<td>1.2.2.1.2.6 / 0x010202010206</td>
</tr>
<tr>
<td>Name</td>
<td>MQTT Client ID</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to set the MQTT Client ID.</td>
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
<p>Example: MagTek_Device-B62B3C6</p></td>
</tr>
<tr>
<td>Default</td>
<td><p>MagTek_Device-[DevSN]</p>
<p>[DevSN] = Device Serial #</p></td>
</tr>
</tbody>
</table>

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 8704 02020102 8902 C600 |

Table 778 -Get Request Example

<table>
<caption><p>Table 779 -Get Response Example</p></caption>
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
<td><p>AA0081048255D1018204000000008482002FD1018501018704020201028922C620</p>
<p>4D616754656B5F4465766963652D423632423343360000000000000000000000</p></td>
</tr>
</tbody>
</table>

| Example (Hex) |
|----|
| AA00 81040155D111 842F D111 850101 870402020102 8922 C620 4D616754656B5F4465766963652D4236 32423343360000000000000000000000 |

Table 780 -Set Request Example

<table>
<caption><p>Table 781 - Set Response Example</p></caption>
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
<td><p>AA0081048255D1118204000000008482002FD1118501018704020201028922C620</p>
<p>4D616754656B5F4465766963652D423632423343360000000000000000000000</p></td>
</tr>
</tbody>
</table>

##