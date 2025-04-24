---
title: Property 1.2.2.1.1.E Web App Enabled (MAGTEK INTERNAL ONLY FOR NOW)
layout: home
parent: Configuration
nav_order: 86
---

## Property 1.2.2.1.1.E Web App Enabled (MAGTEK INTERNAL ONLY FOR NOW)

Table 733 - Property 1.2.2.1.1.E Web App Enabled (MAGTEK INTERNAL ONLY
FOR NOW)

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
<td>1.2.2.1.1.E / 0x01020201010E</td>
</tr>
<tr>
<td>Name</td>
<td>Web App Enabled</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if its web application
is enabled. The web app can be used to send commands to the device over
the WLAN interface using a web browser. The web app appears as a web
page on a browser.</p>
<p>The URL and port used to access the web page depend on how the device
is configured. The default port is 26 (not 80 or 443). See
<strong>Property 1.2.2.1.1.F Web App Port</strong> for changing the web
app port. The security required to access the web page depends on if the
device has been configured to use TLS or not.</p>
<p>https://df-b62b3aa.lan:26 and https://192.168.86.31:26 are examples
of how to access the web page on a device that has TLS enabled.
http://df-b62b3aa.lan:26 and http://192.168.86.31:26 are examples of how
to access the web page on a device that does not have TLS enabled.</p>
<p>If this property is changed, the device must be or power cycled or
reset before the change will take effect.</p></td>
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
<td>0x00 (not enabled), 0x01 (enabled)</td>
</tr>
<tr>
<td>Default</td>
<td>0x00 (not enabled)</td>
</tr>
</tbody>
</table>

Table 734 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020101 8902 CE00 |

Table 735 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020201018903CE0101 |

Table 736 - Set Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 8704 02020101 8903 CE0101 |

Table 737 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020201018903CE0101 |

##