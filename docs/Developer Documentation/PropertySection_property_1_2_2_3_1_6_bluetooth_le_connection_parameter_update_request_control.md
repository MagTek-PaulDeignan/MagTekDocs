---
title: Property 1.2.2.3.1.6 Bluetooth® LE Connection Parameter Update Request Control
layout: home
parent: Configuration
nav_order: 109
---

## Property 1.2.2.3.1.6 Bluetooth® LE Connection Parameter Update Request Control

Table 841 - Property 1.2.2.3.1.6 Bluetooth® LE Connection Parameter
Update Request Control

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
<td>1.2.2.3.1.6 / 0x010202030106</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Connection Parameter Update Request Control</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if the Bluetooth® LE
connection parameter update request control is enabled. When it is
enabled, the device sends a connection parameter update request once
after each Bluetooth® LE connection.</p>
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
<td>0x01 (Enabled)</td>
</tr>
</tbody>
</table>

Table 842 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102C600 |

Table 843 - Get Response Example

| Example (Hex) |
|----|
| AA0081048232D1018204000000008482001BD10181072B06010401F609850101890BE209E207E305E103C60100 |

Table 844 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D111841BD11181072B06010401F609850101890BE209E207E305E103C60100 |

Table 845 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D1118204000000008482001BD11181072B06010401F609850101890BE209E207E305E103C60100 |

##