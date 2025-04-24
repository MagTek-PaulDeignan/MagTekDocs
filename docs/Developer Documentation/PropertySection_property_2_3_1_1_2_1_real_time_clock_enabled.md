---
title: Property 2.3.1.1.2.1 Real Time Clock Enabled
layout: home
parent: Configuration
nav_order: 225
---

## Property 2.3.1.1.2.1 Real Time Clock Enabled

Table 1172 - Property 2.3.1.1.2.1 Real Time Clock Enabled

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
<td>2.3.1.1.2.1 / 0x020301010201</td>
</tr>
<tr>
<td>Name</td>
<td>Real Time Clock Enabled</td>
</tr>
<tr>
<td>Description</td>
<td>The device maps this property to its internal register that enables
its internal real-time clock. Because the device ensures that register
is enabled every time it powers up, this property should always report
Real Time Clock Enabled.</td>
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
<td><p>0x00 = Real Time Clock Not Enabled</p>
<p>0x01 = Real Time Clock Enabled</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1173 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010102 8902 C100 |

Table 1174 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010102 8903 C101 01 |

##