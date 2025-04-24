---
title: Property 1.2.2.1.1.A Maximum Client Connections
layout: home
parent: Configuration
nav_order: 82
---

## Property 1.2.2.1.1.A Maximum Client Connections

---

- [Property 1.2.2.1.1.A Maximum Client Connections](#property-12211a-maximum-client-connections)

---


Table 713 - Property 1.2.2.1.1.A Maximum Client Connections

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
<td>1.2.2.1.1.A / 0x01020201010A</td>
</tr>
<tr>
<td>Name</td>
<td>Maximum Client Connections</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine how many clients it
will allow to connect to its WLAN WebSocket server at one time. Most use
cases will only want to allow one client at a time. If more than one
client is connected, all outgoing data from the device will be sent to
all clients. For example, all notifications and all command responses
will be sent to all clients. If more than one client is connected, any
client can send a command to the device at any time. Since having more
than one client send commands to the device at the same time can result
in command collisions and unexpected device behavior, it is recommended
that only one client be in charge of sending commands and that other
clients only listen to outgoing messages. A use case for allowing more
than once client may be to have a second client for diagnostic or
monitoring purposes.</p>
<p><strong>Property 2.1.2.5.6.4 Active Client Connections</strong> is
related.</p></td>
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
<td>0x01 – 0x04</td>
</tr>
<tr>
<td>Default</td>
<td>0x01</td>
</tr>
</tbody>
</table>

Table 714 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020101 8902 CA00 |

Table 715 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020201018903CA0101 |

Table 716 - Set Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 8704 02020101 8903 CA0101 |

Table 717 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020201018903CA0101 |

##