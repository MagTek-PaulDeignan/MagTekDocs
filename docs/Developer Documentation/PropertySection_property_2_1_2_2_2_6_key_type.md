---
title: Property 2.1.2.2.2.6 Key Type
layout: home
parent: Configuration
nav_order: 153
---

## Property 2.1.2.2.2.6 Key Type

Table 997 - Property 2.1.2.2.2.6 Key Type

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
<td>2.1.2.2.2.6 / 0x020102020206</td>
</tr>
<tr>
<td>Name</td>
<td>Key Type</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device’s firmware can be compiled to use one of two available
ECDSA P-521 key sets when signing and verifying the signature in
<strong>Command 0xEEEE - Send Secured Command to Device</strong>.</p>
<p>This property indicates which of the two keys the firmware is
configured to expect the host and device to use:</p>
<ul>
<li><p>0xFF00 = Development Key</p></li>
<li><p>Any other value = Production Key</p></li>
</ul></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>2</td>
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

Table 998 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 31 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E2 04 E2 02 C6 00 |

Table 999 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 31 D1 01 82 04 00 00 00 00 84 82 00 1C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0C E1 0A E2 08 E2 06 E2 04 C6 02 FF 00 |

#