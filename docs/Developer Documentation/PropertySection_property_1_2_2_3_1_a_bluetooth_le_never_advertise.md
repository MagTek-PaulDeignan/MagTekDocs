---
title: Property 1.2.2.3.1.A Bluetooth® LE Never Advertise
layout: home
parent: Configuration
nav_order: 113
---

## Property 1.2.2.3.1.A Bluetooth® LE Never Advertise

Table 861 - Property 1.2.2.3.1.A Bluetooth® LE Never Advertise

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
<td>1.2.2.3.1.A / 0x01020203010A</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Never Advertise</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if the Bluetooth® LE
Never Advertise is enabled. When it is enabled, the device never
advertises. This mode may be useful for operators who only want to use
the USB interface and don’t want the device to advertise.</p>
<p>After the host changes this property, the device must be reset before
the changes will take effect.</p></td>
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
<td><p>0x00 (Disabled)</p>
<p>0x01 (Enabled)</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00 (Disabled)</td>
</tr>
</tbody>
</table>

Table 862 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102CA00 |

Table 863 - Get Response Example

| Example (Hex) |
|----|
| AA0081048232D1018204000000008482001BD10181072B06010401F609850101890BE209E207E305E103CA0100 |

Table 864 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D111841BD11181072B06010401F609850101890BE209E207E305E103CA0100 |

Table 865 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D1118204000000008482001BD11181072B06010401F609850101890BE209E207E305E103CA0100 |

##