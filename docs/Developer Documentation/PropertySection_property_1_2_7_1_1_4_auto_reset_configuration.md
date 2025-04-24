---
title: Property 1.2.7.1.1.4 Auto Reset Configuration
layout: home
parent: Configuration
nav_order: 133
---

## Property 1.2.7.1.1.4 Auto Reset Configuration

Table 945 - Property 1.2.7.1.1.4 Auto Reset Configuration

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
<td>1.2.7.1.1.4 / 0x010207010104</td>
</tr>
<tr>
<td>Name</td>
<td>Auto Reset Configuration</td>
</tr>
<tr>
<td>Description</td>
<td><p>This property controls the device’s auto reset feature. The auto
reset feature can be configured such that the device automatically
resets 23 hours after booting up or at a specific time of day. The
auto-reset feature cannot be disabled.</p>
<p>See <strong>24 Hour Automatic Reset PCI Requirement</strong> for more
information.</p>
<p>Changes to this property do not take effect until the device is power
cycled or reset.</p></td>
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
<td><p>First byte 0 - 23 hours and second byte 0 - 59 minutes = Reset at
the time of day specified. The time of day specified should be 24-hour
Universal Time Coordinated (UTC). For example, values of 0 0 would be
12:00am UTC and values of 23 59 (0x17 0x3B) would be 11:59pm UTC.</p>
<p>First byte 0xFF and second byte 0xFF = Auto reset 23 hours after
booting up.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0xFF 0xFF</td>
</tr>
</tbody>
</table>

Table 946 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02070101 8902 C400 |

Table 947 - Get Response Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D10182040000000084820011D1018501018704020701018904C402FFFF |

Table 948 - Set Request Example

| Example (Hex)                                                    |
|------------------------------------------------------------------|
| AA00 81040155D111 8411 D111 8501 01 8704 02070101 8904 C402 FFFF |

Table 949 - Set Response Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D11182040000000084820011D1118501018704020701018904C402FFFF |

##