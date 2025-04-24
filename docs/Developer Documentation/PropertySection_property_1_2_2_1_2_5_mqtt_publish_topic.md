---
title: Property 1.2.2.1.2.5 MQTT Publish Topic
layout: home
parent: Configuration
nav_order: 94
---

## Property 1.2.2.1.2.5 MQTT Publish Topic

<table>
<caption><p>Table 772 -Property 1.2.2.1.2.5 MQTT Publish
Topic</p></caption>
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
<td>1.2.2.1.2.5 / 0x010202010205</td>
</tr>
<tr>
<td>Name</td>
<td>MQTT Publish Topic</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set the MQTT Publish Topic for
sending MMS message payloads.</p>
<p>Device will add append the string <em>/MMSMessage</em> to the MQTT
Publish Topic string set in this property.</p></td>
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
<p>Example:
<strong>MagTek/Server/DynaFlexIIPED/B62B3C6</strong><em>/MMSMessage[MMS
Message Payload]</em></p></td>
</tr>
<tr>
<td>Default</td>
<td><p>MagTek/Server/[DevModelName]/[DevSN]</p>
<p>[DevModelName] = DynaFlexIIPED, Device Model Name with no spaces.</p>
<p>[DevSN] = Device Serial #</p></td>
</tr>
</tbody>
</table>

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 8704 02020102 8902 C500 |

Table 773 -Get Request Example

<table>
<caption><p>Table 774 -Get Response Example</p></caption>
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
<td><p>AA0081048255D1018204000000008482004FD1018501018704020201028942C540</p>
<p>4D616754656B2F5365727665722F44796E61466C657849495045442F423632423343360000000000000000000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

| Example (Hex) |
|----|
| AA00 81040155D111 844F D111 850101 870402020102 8942 C540 4D616754656B2F5365727665722F4479 6E61466C657849495045442F42363242 33433600000000000000000000000000 00000000000000000000000000000000 |

Table 775 -Set Request Example

<table>
<caption><p>Table 776 -Set Response Example</p></caption>
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
<td><p>AA0081048255D1118204000000008482004FD1118501018704020201028942C540</p>
<p>4D616754656B2F5365727665722F44796E61466C657849495045442F423632423343360000000000000000000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

##