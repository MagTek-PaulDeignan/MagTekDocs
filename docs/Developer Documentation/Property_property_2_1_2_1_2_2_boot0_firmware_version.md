---
title: Property 2.1.2.1.2.2 Boot0 Firmware Version
layout: home
parent: Configuration
nav_order: 147
---

## Property 2.1.2.1.2.2 Boot0 Firmware Version

---

- [Property 2.1.2.1.2.2 Boot0 Firmware Version](#property-212122-boot0-firmware-version)

---


Table 982 - Property 2.1.2.1.2.2 Boot0 Firmware Version

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
<td>2.1.2.1.2.2 / 0x020102010202</td>
</tr>
<tr>
<td>Name</td>
<td>Boot 0 Firmware Version</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its bootloader firmware
version number in the form <strong>PartNumber-Version-PCI</strong>,
padded with null characters.</p>
<p>Example: 1000007535-A0-PCI</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>19</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>19</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 983 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 05 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E1 04 E2 02 C2 00 |

Table 984 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 05 D1 01 82 04 00 00 00 00 84 82 00 2D D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1D E1 1B E2 19 E1 17 E1 15 C2 13 31 30 30 30 30 30 37 35 33 35 2D 41 30 2D 50 43 49 00 00 |

##