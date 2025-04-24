---
title: Property 2.1.2.7.1.1 Bluetooth® LE Firmware Version
layout: home
parent: Configuration
nav_order: 206
---

## Property 2.1.2.7.1.1 Bluetooth® LE Firmware Version

Table 1133 - Property 2.1.2.7.1.1 Bluetooth® LE Firmware Version

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
<td>2.1.2.7.1.1 / 0x020102070101</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Firmware Version</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its BLE firmware version
number in the form <strong>PartNumber-Version-PCI</strong>, padded with
null characters.</p>
<p>Example: 1000009327-A0-PCI</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>18</td>
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
<td>None</td>
</tr>
</tbody>
</table>

Table 1134 - Get Request Example

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA0081040108D101841AD10181072B06010401F609850102890AE108E206E704E102C100 |

Table 1135 - Get Response Example

| Example (Hex) |
|----|
| AA0081048208D1018204000000008482002CD10181072B06010401F609850102891CE11AE218E716E114C112313030303030393332372D41302D50434900 |

##