---
title: Property 1.2.2.3.1.B Bluetooth® LE FCC Test Control (MAGTEK INTERNAL ONLY)
layout: home
parent: Configuration
nav_order: 114
---

## Property 1.2.2.3.1.B Bluetooth® LE FCC Test Control (MAGTEK INTERNAL ONLY)

Table 866 - Property 1.2.2.3.1.B Bluetooth® LE FCC Test Control (MAGTEK
INTERNAL ONLY)

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
<td>1.2.2.3.1.B / 0x01020203010B</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE FCC Test Control</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if Bluetooth® LE FCC
test mode is enabled and to control it. FCC test mode is only used by
MagTek for FCC testing. When it is enabled, the device sends packets
continuously with a fixed interval and all other Bluetooth® LE
communications are disabled.</p>
<p>If the value of this property is set between 0 and 39 (0x27) FCC test
mode is enabled and the value is the transmit channel C. The transmit
frequency is (2C + 2402) Mhz. If the value is greater than 39 (0x27)
then FCC test mode is disabled.</p>
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
<td>0x00 – 0xFF</td>
</tr>
<tr>
<td>Default</td>
<td>0xFF (FCC test disabled)</td>
</tr>
</tbody>
</table>

Table 867 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020301 8902 CB00 |

Table 868 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020203018903CB01FF |

Table 869 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870402020301 8903 CB01FF |

Table 870 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020203018903CB01FF |

##