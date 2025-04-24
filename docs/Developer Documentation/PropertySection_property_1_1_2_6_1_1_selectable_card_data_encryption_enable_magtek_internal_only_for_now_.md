---
title: Property 1.1.2.6.1.1 Selectable Card Data Encryption Enable (MAGTEK INTERNAL ONLY FOR NOW)
layout: home
parent: Configuration
nav_order: 52
---

## Property 1.1.2.6.1.1 Selectable Card Data Encryption Enable (MAGTEK INTERNAL ONLY FOR NOW)

<table>
<caption><p>Table 578 - Property 1.1.2.6.1.1 Selectable Card Data
Encryption Enable (MAGTEK INTERNAL ONLY FOR NOW)</p></caption>
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
<td>1.1.2.6.1.1 / 0x010102060101</td>
</tr>
<tr>
<td>Name</td>
<td>Selectable Card Data Encryption Enable</td>
</tr>
<tr>
<td>Description</td>
<td>The host can use this property to enable Selectable Card Data
Encryption. Each bit enables a specific card data encryption by setting
that bit to 1. Byte 0 is the first byte, bit 0 is the LSB of each byte.
This is a secured OID, the set request shall be from 0xD112 command. If
the Key DKPTM1F has not been injected, enabling any bits in this OID
will return failure response status 80-02-05-27 (TR31 errors, Key not
present). If the Key DKPTM1F becomes unavailable after this OID has been
enabled, then this OID will be reset to 0 as a status indicator.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>Refer to 0xD112 Command.</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>0x02</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>0x02</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>This OID is bit mapped as follows:</p>
<p>Byte 0</p>
<p>• bit 0: Card Holder Name</p>
<p>• bit 1: Reserved</p>
<p>• bit 2: Expiration Date</p>
<p>• bit 3: Service Code</p>
<p>• bit 4: T1 Discretionary Data</p>
<p>• bit 5: T2 Discretionary Data</p>
<p>• bit 6 - 7: Reserved</p>
<p>Byte 1</p>
<p>• bit 0 - 7: Reserved</p>
<p>The host shall set all the reserved bits to 0.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x0000</td>
</tr>
</tbody>
</table>

Table 579 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E6 04 E1 02 C1 00 |

Table 580 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 1C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0C E1 0A E2 08 E6 06 E1 04 C1 02 3F 00 |

Table 581 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0B D1 12 84 5D EE EE A1 19 81 05 03 03 06 02 08 84 00 85 00 A8 0A 81 02 11 11 82 00 86 00 88 00 A9 00 82 04 BE 00 11 D0 83 08 E7 9F B1 FE 99 9F 8D A2 84 1C D1 12 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0C E1 0A E2 08 E6 06 E1 04 C1 02 3F 00 9E 10 D9 38 F1 6E 7F 8C CE 87 02 35 0F DF 8C C2 75 64 |

Table 582 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0B D1 12 82 04 00 00 00 00 84 82 00 1C D1 12 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0C E1 0A E2 08 E6 06 E1 04 C1 02 3F 00 |