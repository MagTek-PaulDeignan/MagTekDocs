---
title: Property 2.1.2.3.4.3 EMV Contactless L1 Kernel Checksum (Contactless Only)
layout: home
parent: Configuration
nav_order: 165
---

## Property 2.1.2.3.4.3 EMV Contactless L1 Kernel Checksum (Contactless Only)

Table 1024 - Property 2.1.2.3.4.3 EMV Contactless L1 Kernel Checksum
(Contactless Only)

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
<td>2.1.2.3.4.3/ 0x020102030403</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contactless L1 Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contactless L1
Kernel Checksum as string, no padding.</p>
<p>Example: d3c5d413334178d1d5929a752b8d29adc1e5829c</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Variable</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>75</td>
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

Table 1025 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 26 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E4 02 C3 00 |

Table 1026 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 26 D1 01 82 04 00 00 00 00 84 82 00 42 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 32 E1 30 E2 2E E3 2C E4 2A C3 28 64 33 63 35 64 34 31 33 33 33 34 31 37 38 64 31 64 35 39 32 39 61 37 35 32 62 38 64 32 39 61 64 63 31 65 35 38 32 39 63 |

##