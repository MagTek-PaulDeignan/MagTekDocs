---
title: Property 1.2.2.3.1.D Bluetooth® LE Debug Mode Enabled
layout: home
parent: Configuration
nav_order: 116
---

## Property 1.2.2.3.1.D Bluetooth® LE Debug Mode Enabled

---

- [Property 1.2.2.3.1.D Bluetooth® LE Debug Mode Enabled](#property-12231d-bluetooth®-le-debug-mode-enabled)

---


Table 876 - Property 1.2.2.3.1.D Bluetooth® LE Debug Mode Enabled

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
<td>1.2.2.3.1.D / 0x01020203010D</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Debug Mode Enabled</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if Bluetooth® LE Debug
Mode is enabled. When it is enabled, the secure connections bonding uses
known debug keys, so that the encrypted packet can be opened by a
Bluetooth® protocol analyzer. Bondings made in debug mode are unsecure.
This mode should only be enabled for debugging for development purposes
and not for regular device use.</p>
<p>Prior to enabling or disabling Debug Mode, the following should be
done. Erase all of the device's bonds with <strong>Command 0x1F05 –
Erase All Bluetooth® LE Bonds (Bluetooth® LE Only)</strong>. Forget the
device on all hosts that have paired with it by using the host's
Bluetooth® settings application. Reboot all of those hosts.</p>
<p>Some hosts like Windows 10 will not pair with devices that use known
debug keys.</p>
<p>If the value of this property is set to 0, Debug Mode is disabled. If
it is set to 1, Debug Mode is enabled.</p>
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
<td>0x00 (Bluetooth® LE Debug Mode disabled)</td>
</tr>
</tbody>
</table>

Table 877 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020301 8902 CD00 |

Table 878 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020203018903CD0100 |

Table 879 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870402020301 8903 CD0100 |

Table 880 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020203018903CD0100 |

#