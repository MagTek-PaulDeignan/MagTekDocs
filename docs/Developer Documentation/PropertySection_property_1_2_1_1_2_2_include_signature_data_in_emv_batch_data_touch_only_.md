---
title: Property 1.2.1.1.2.2 Include Signature Data in EMV Batch Data (Touch Only)
layout: home
parent: Configuration
nav_order: 58
---

## Property 1.2.1.1.2.2 Include Signature Data in EMV Batch Data (Touch Only)

Table 598 - Property 1.2.1.1.2.2 Include Signature Data in EMV Batch
Data (Touch Only)

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
<td>1.2.1.1.2.2 / 0x010201010202</td>
</tr>
<tr>
<td>Name</td>
<td>Include Signature Data in EMV Batch Data</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine whether to include
signature capture coordinate data in TLV data object DFDF3E when it
returns <strong>EMV Batch Data Type</strong> while running
<strong>Command 0x1001 - Start Transaction</strong>.</td>
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
<td><p>0x00 = Include signature data in <strong>EMV Batch Data
Type</strong></p>
<p>0x01 = RESERVED. Make signature data available as file. Use
<strong>Command 0xD821 - Start Get File from Device</strong> to request
file type <strong>Signature Capture File</strong> to retrieve the data
as a <strong>Signature Capture File Type</strong>.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 599 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 04 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E2 02 C2 00 |

Table 600 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 04 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C2 01 01 |

Table 601 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 02 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C2 01 01 |

Table 602 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 02 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C2 01 01 |

##