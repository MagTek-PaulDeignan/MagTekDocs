---
title: Property 1.2.2.1.2.3 MQTT QoS Quality of Service
layout: home
parent: Configuration
nav_order: 92
---

## Property 1.2.2.1.2.3 MQTT QoS Quality of Service

---

- [Property 1.2.2.1.2.3 MQTT QoS Quality of Service](#property-122123-mqtt-qos-quality-of-service)

---


<table>
<caption><p>Table 762 -Property 1.2.2.1.2.3 MQTT QoS Quality of
Service</p></caption>
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
<td>1.2.2.1.2.3 / 0x010202010203</td>
</tr>
<tr>
<td>Name</td>
<td>MQTT QoS</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set the MQTT QoS.</p>
<p>0x00 = At most once (Recomnended)</p>
<p>0x01 = At least once</p>
<p>0x02 = Exactly once</p></td>
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
<td>0x00</td>
</tr>
</tbody>
</table>

| Example (Hex)                                              |
|------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 870402020102 8902 C300 |

Table 763 -Get Request Example

| Example (Hex)                                                         |
|-----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020201028903C301 00 |

Table 764 -Get Response Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870402020102 8903C301 00 |

Table 765 -Set Request Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020201028903C30100 |

Table 766 -Set Response Example

##