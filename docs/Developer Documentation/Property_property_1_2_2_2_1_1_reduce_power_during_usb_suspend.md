---
title: Property 1.2.2.2.1.1 Reduce Power During USB Suspend
layout: home
parent: Configuration
nav_order: 101
---

## Property 1.2.2.2.1.1 Reduce Power During USB Suspend

---

- [Property 1.2.2.2.1.1 Reduce Power During USB Suspend](#property-122211-reduce-power-during-usb-suspend)

---


Table 802 - Property 1.2.2.2.1.1 Reduce Power During USB Suspend

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
<td>1.2.2.2.1.1 / 0x010202020101</td>
</tr>
<tr>
<td>Name</td>
<td>Reduce Power During USB Suspend</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine whether it should
reduce its power consumption when a USB host directs it to suspend. If
this property is set to Disabled, the device will not have a USB
compliant current draw when suspended, which, for example, allows it to
continue to turn on LEDs and the display if present.</p>
<p>To activate changes made to this property, the device must be reset
or power cycled.</p></td>
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
<td><p>0x00 = Disabled</p>
<p>0x01 = Enabled</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x01</td>
</tr>
</tbody>
</table>

Table 803 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020201 8902 C100 |

Table 804 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020202018903C10101 |

Table 805 - Set Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 8704 02020201 8903 C10101 |

Table 806 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020202018903C10101 |

##