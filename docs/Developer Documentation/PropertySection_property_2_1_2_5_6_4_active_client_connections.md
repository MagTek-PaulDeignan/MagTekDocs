---
title: Property 2.1.2.5.6.4 Active Client Connections
layout: home
parent: Configuration
nav_order: 199
---

## Property 2.1.2.5.6.4 Active Client Connections

Table 1117 - Property 2.1.2.5.6.4 Active Client Connections

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
<td>2.1.2.5.6.4 / 0x020102050604</td>
</tr>
<tr>
<td>Name</td>
<td>Active Client Connections</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its number of active
client connections.</p>
<p><strong>Property 1.2.2.1.1.A Maximum Client Connections</strong> is
related.</p></td>
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
<td>0x00 – 0x04</td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1118 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020506 8902 C400 |

Table 1119 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870401020506 8903 C401 01 |

##