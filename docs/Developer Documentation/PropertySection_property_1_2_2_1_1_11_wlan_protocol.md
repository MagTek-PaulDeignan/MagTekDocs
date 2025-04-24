---
title: Property 1.2.2.1.1.11 WLAN Protocol
layout: home
parent: Configuration
nav_order: 89
---

## Property 1.2.2.1.1.11 WLAN Protocol

<table>
<caption><p>Table 747 - Property 1.2.2.1.2.11 WLAN
Protocol</p></caption>
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
<td>1.2.2.1.1.11 / 0x010202010111</td>
</tr>
<tr>
<td>Name</td>
<td>WLAN Protocol</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set the WLAN Protocol.</p>
<p>0x00 = MQTT</p>
<p>0x01 = RFU</p>
<p>0x02 = WebSocket Server</p></td>
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
<td>0x00 – 0x02</td>
</tr>
<tr>
<td>Default</td>
<td>0x02</td>
</tr>
</tbody>
</table>

| Example (Hex)                                              |
|------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 870402020101 8902 D100 |

Table 748 - Get Request Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020201018903D10102 |

Table 749 - Get Response Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870402020101 8903 D101 02 |

Table 750 - Set Request Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020201018903D10102 |

Table 751 -Set Response Example

##