---
title: Property 1.1.1.1.2.1 Start Transaction on Touchscreen Event Control(Touch Only)
layout: home
parent: Configuration
nav_order: 23
---

## Property 1.1.1.1.2.1 Start Transaction on Touchscreen Event Control(Touch Only)

---

- [Property 1.1.1.1.2.1 Start Transaction on Touchscreen Event Control(Touch Only)](#property-111121-start-transaction-on-touchscreen-event-controltouch-only)

---


Table 446 - Property 1.1.1.1.2.1 Start Transaction on Touchscreen Event
Control(Touch Only)

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
<td>1.1.1.1.2.1 / 0x010101010201</td>
</tr>
<tr>
<td>Name</td>
<td>Start Transaction on Touchscreen Event Control</td>
</tr>
<tr>
<td>Description</td>
<td>The device use this property to determine if a transaction operation
is to be started when a Touchscreen event is detected.</td>
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
<td><p>0x00 – Do not start Transaction on Touchscreen event</p>
<p>0x01 – Start Transaction on Touchscreen Event</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00 - Do not start Transaction on Touchscreen event s</td>
</tr>
</tbody>
</table>

Table 447 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101028902C100 |

Table 448 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704010101028903C10100 |

Table 449 - Set Request Example

| Example (Hex)                                        |
|------------------------------------------------------|
| AA0081040155D1118410D1118501018704010101028903C10100 |

Table 450 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704010101028903C10100 |

##