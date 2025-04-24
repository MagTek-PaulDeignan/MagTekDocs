---
title: Property 2.1.2.3.3.2 EMV Contact L2 Kernel Firmware Part Number(Contact Only)
layout: home
parent: Configuration
nav_order: 160
---

## Property 2.1.2.3.3.2 EMV Contact L2 Kernel Firmware Part Number(Contact Only)

Table 1009 - Property 2.1.2.3.3.2 EMV Contact L2 Kernel Firmware Part
Number(Contact Only)

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
<td>2.1.2.3.3.2 / 0x020102030302</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contact L2 Kernel Firmware Part Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contact L2 Kernel
Part Number as string, padded with null characters.</p>
<p>Example: 1000008878 Ver A DynaFlex PED L2 Kernel</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>40</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>40</td>
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

Table 1010 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1A D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E3 02 C2 00 |

Table 1011 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 1A D1 01 82 04 00 00 00 00 84 82 00 42 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 32 E1 30 E2 2E E3 2C E3 2A C2 28 31 30 30 30 30 30 38 38 37 38 20 56 65 72 20 41 20 44 79 6E 61 46 6C 65 78 20 50 45 44 20 4C 32 20 4B 65 72 6E 65 6C 00 |

##