---
title: Property 1.2.2.2.1.2 USB Configuration Type
layout: home
parent: Configuration
nav_order: 102
---

## Property 1.2.2.2.1.2 USB Configuration Type

Table 807 - Property 1.2.2.2.1.2 USB Configuration Type

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
<td>1.2.2.2.1.2 / 0x010202020102</td>
</tr>
<tr>
<td>Name</td>
<td>USB Configuration Type</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if it should behave as
a USB HID device or an USB iAP2 device. USB HID devices can communicate
with most hosts except for Apple hosts. USB iAP2 devices can communicate
to Apple hosts like iPads and iPhones. The behavior affects USB
enumeration and communications.</p>
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
<td><p>0x00 = HID only</p>
<p>0x01 = iAP2 only</p>
<p>0x02 = autodetect (iAP2 with HID fallback)</p>
<p>The autodetect option can allow a device to work with iAP2 hosts and
HID hosts. With this option, every time the device is attached to a USB
host it will first enumerate as an iAP2 device, if the device does not
receive an iAP2 initialization sequence response from the host within 2
seconds the device will perform a soft USB detach from the host and then
a soft USB attach and next enumerate as a USB HID device.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x02</td>
</tr>
</tbody>
</table>

Table 808 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020201 8902 C200 |

Table 809 - Get Response Example (HID only)

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020202018903C20100 |

Table 810 - Set Request Example (HID only)

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 8704 02020201 8903 C20100 |

Table 811 - Set Response Example (HID only)

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020202018903C20100 |

Table 812 - Set Request Example (iAP2 only)

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 8704 02020201 8903 C20101 |

Table 813 - Set Response Example (iAP2 only)

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020202018903C20101 |

Table 814 - Set Request Example (autodetect (iAP2 with HID fallback))

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 8704 02020201 8903 C20102 |

Table 815 - Set Response Example (autodetect (iAP2 with HID fallback))

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020202018903C20102 |

#