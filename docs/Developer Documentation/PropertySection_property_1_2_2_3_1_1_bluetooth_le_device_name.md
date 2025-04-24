---
title: Property 1.2.2.3.1.1 Bluetooth® LE Device Name
layout: home
parent: Configuration
nav_order: 104
---

## Property 1.2.2.3.1.1 Bluetooth® LE Device Name

Table 816 - Property 1.2.2.3.1.1 Bluetooth® LE Device Name

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
<td>1.2.2.3.1.1 / 0x010202030101</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Device Name</td>
</tr>
<tr>
<td>Description</td>
<td><p>This property contains the Bluetooth® device name, which is
typically used by the host software to present an operator with a list
of devices to interact with. To avoid ambiguity, if the solution
specifies that more than one device of the same name will be available,
MagTek recommends including a unique identifier in the device name so
the operator can differentiate.</p>
<p>The name should not contain any null string characters (0x00) at the
beginning or in the middle, 0x00 can be used at the end of the name for
padding to a total length of 20 characters. When setting this property,
you can enter 0 to 20 characters. If set to a length of 0, the value
reverts to its original default value described below. After modifying
the Bluetooth® device name, you must reset the Bluetooth® LE module.</p>
<p>When getting this property, device will always return 20 characters
If the name is less than 20 characters long, device will return 0x00 for
the remaining characters.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>0</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>20</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td><p>A prefix, such as “DF II Go-“ for DynaFlex II Go, followed by the
device’s serial number. For example, “DF II Go-B603226”.</p>
<p>Devices are always deployed with the serial number loaded, but prior
to loading the serial number at MagTek, the prefix will be followed by
the second to last and the last least significant bytes of the
Bluetooth® device address converted to ASCII hex. For example, “DF II
Go-97C2”.</p></td>
</tr>
</tbody>
</table>

Table 817 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102C100 |

Table 818 - Get Response Example

| Example (Hex) |
|----|
| AA008104825CD10182040000000084820020D10181072B06010401F6098501028910E10EE20CE70AE208C106943469B297A5 |

Table 819 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D111842ED11181072B06010401F609850101891EE21CE21AE318E116C11444594E41464C4558000000000000000000000000 |

Table 820 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D1118204000000008482002ED11181072B06010401F609850101891EE21CE21AE318E116C11444594E41464C4558000000000000000000000000 |

##