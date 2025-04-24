---
title: Property 1.2.2.1.1.F Web App Port (MAGTEK INTERNAL ONLY FOR NOW)
layout: home
parent: Configuration
nav_order: 87
---

## Property 1.2.2.1.1.F Web App Port (MAGTEK INTERNAL ONLY FOR NOW)

Table 738 - Property 1.2.2.1.1.F Web App Port (MAGTEK INTERNAL ONLY FOR
NOW)

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
<td>1.2.2.1.1.F / 0x01020201010F</td>
</tr>
<tr>
<td>Name</td>
<td>Web App Port</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine which port the web app
can be accessed on. See <strong>Web App Enabled</strong> for more
details about the web app.</p>
<p>The device does not support having both WLAN web socket and the web
app accessible on the same port. By default, the device will use port
443 for the WLAN web socket port when TLS is enabled and port 80 when
TLS is not enabled. If the web app port is set to the same port
configured for the WLAN web socket port, then the web app will not be
accessible.</p>
<p>If this property is changed, the device must be power cycled or reset
before the change will take effect.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 0x00 (0) - 0xFF 0xFF (65535) MSB first</td>
</tr>
<tr>
<td>Default</td>
<td>0x00 0x1A (26)</td>
</tr>
</tbody>
</table>

Table 739 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020101 8902 CF00 |

Table 740 - Get Response Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D10182040000000084820011D1018501018704020201018904CF02001A |

Table 741 - Set Request Example

| Example (Hex)                                                 |
|---------------------------------------------------------------|
| AA00 81040155D111 8411 D111 850101 870402020101 8904 CF02001A |

Table 742 - Set Response Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D11182040000000084820011D1118501018704020201018904CF02001A |

##