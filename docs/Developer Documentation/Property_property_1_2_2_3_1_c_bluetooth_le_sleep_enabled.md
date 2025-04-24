---
title: Property 1.2.2.3.1.C Bluetooth® LE Sleep Enabled
layout: home
parent: Configuration
nav_order: 115
---

## Property 1.2.2.3.1.C Bluetooth® LE Sleep Enabled

---

- [Property 1.2.2.3.1.C Bluetooth® LE Sleep Enabled](#property-12231c-bluetooth®-le-sleep-enabled)

---


Table 871 - Property 1.2.2.3.1.C Bluetooth® LE Sleep Enabled

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
<td>1.2.2.3.1.C / 0x01020203010C</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Sleep Enabled</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if Bluetooth® LE Sleep
is enabled. When it is enabled, the device will conserve battery power
when USB power is not present and the device is not in a secure
Bluetooth® LE connection with notifications enabled (not able to
exchange messages with a host). The device will conserve battery power
by turning off various hardware features and by going into low power
modes.</p>
<p>The battery life when the device is idle can be increased by about 3
times for DynaFlex II Go when the host application takes advantage of
this feature.</p>
<p>Here is an example of how the host application can be written to take
advantage of this feature and extend battery life.</p>
<p>1) Establish a BLE connection with the device only when the host
needs to perform a transaction or other operation.</p>
<p>2) Perform the transaction or other operation.</p>
<p>3) Close the BLE connection.</p>
<p>4) The device will sleep at this point and use less power.</p>
<p>Some operations in addition to connecting USB power or establishing a
BLE connection will wake the device from sleep mode temporarily. The
following are examples of these operations.</p>
<p>1) Pressing the button.</p>
<p>2) Putting the device into pairing mode.</p>
<p>When the device is sleeping, all LEDs will go off so the device will
look similar to when it is off.</p>
<p>If the value of this property is set to 0, sleep is disabled. If it
is set to 1, sleep is enabled.</p>
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
<td>0x00 – 0x01</td>
</tr>
<tr>
<td>Default</td>
<td>0x01 (Bluetooth® LE Sleep enabled)</td>
</tr>
</tbody>
</table>

Table 872 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020301 8902 CC00 |

Table 873 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020203018903CC0100 |

Table 874 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870402020301 8903 CC0100 |

Table 875 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020203018903CC0100 |

##