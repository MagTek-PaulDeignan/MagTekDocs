---
title: Property 1.2.2.1.2.4 MQTT Subscribe Topic
layout: home
parent: Configuration
nav_order: 93
---

## Property 1.2.2.1.2.4 MQTT Subscribe Topic

<table>
<caption><p>Table 767 -Property 1.2.2.1.2.4 MQTT Subscribe
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
<td>1.2.2.1.2.4 / 0x010202010204</td>
</tr>
<tr>
<td>Name</td>
<td>MQTT Subscribe Topic</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to set the MQTT Subscribe Topic for
receiving MMS message payloads</td>
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
<p>Example: <strong>MagTek/Device/DynaFlexIIPED/B62B3C6</strong><em>[MMS
Message Payload]</em></p></td>
</tr>
<tr>
<td>Default</td>
<td><p>MagTek/Device/[DevModelName]/[DevSN]</p>
<p>[DevModelName] = DynaFlexIIPED, Device Model Name with no spaces.</p>
<p>[DevSN] = Device Serial #</p></td>
</tr>
</tbody>
</table>

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 8704 02020102 8902 C400 |

Table 768 -Get Request Example

<table>
<caption><p>Table 769 -Get Response Example</p></caption>
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
<td><p>AA0081048255D1018204000000008482004FD1018501018704020201028942C440</p>
<p>4D616754656B2F4465766963652F44796E61466C657849495045442F423632423343360000000000000000000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

| Example (Hex) |
|----|
| AA00 81040155D111 844F D111 850101 870402020102 8942 C440 4D616754656B2F4465766963652F4479 6E61466C657849495045442F42363242 33433600000000000000000000000000 00000000000000000000000000000000 |

Table 770 -Set Request Example

<table>
<caption><p>Table 771 - Set Response Example</p></caption>
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
<td><p>AA0081048255D1118204000000008482004FD1118501018704020201028942C440</p>
<p>4D616754656B2F4465766963652F44796E61466C657849495045442F423632423343360000000000000000000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

##