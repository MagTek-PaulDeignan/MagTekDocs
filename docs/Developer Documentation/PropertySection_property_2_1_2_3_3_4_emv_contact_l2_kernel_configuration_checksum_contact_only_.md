---
title: Property 2.1.2.3.3.4 EMV Contact L2 Kernel Configuration Checksum (Contact Only)
layout: home
parent: Configuration
nav_order: 162
---

## Property 2.1.2.3.3.4 EMV Contact L2 Kernel Configuration Checksum (Contact Only)

Table 1015 - Property 2.1.2.3.3.4 EMV Contact L2 Kernel Configuration
Checksum (Contact Only)

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
<td>2.1.2.3.3.4/ 0x020102030304</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contact L2 Kernel Configuration Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contact L2 Kernel
Configuration Checksum as string, no padding.</p>
<p>Example: 17AC3C4A</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>8</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>8</td>
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

Table 1016 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1F D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E3 02 C4 00 |

Table 1017 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 1F D1 01 82 04 00 00 00 00 84 82 00 1E D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0E E1 0C E2 0A E3 08 E3 06 C4 04 17 AC 3C 4A |

##