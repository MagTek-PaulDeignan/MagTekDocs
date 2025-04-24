---
title: Property 2.1.2.3.8.1 American Express Expresspay Kernel ID (Contactless Only)
layout: home
parent: Configuration
nav_order: 176
---

## Property 2.1.2.3.8.1 American Express Expresspay Kernel ID (Contactless Only)

---

- [Property 2.1.2.3.8.1 American Express Expresspay Kernel ID (Contactless Only)](#property-212381-american-express-expresspay-kernel-id-contactless-only)

---


Table 1057 - Property 2.1.2.3.8.1 American Express Expresspay Kernel ID
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
<td>2.1.2.3.8.1 / 0x020102030801</td>
</tr>
<tr>
<td>Name</td>
<td>American Express Expresspay Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the American Express
Expresspay Kernel ID as string, padded with null characters.</p>
<p>Example: AMEX 4.0.2</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>11</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>11</td>
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

Table 1058 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E8 02 C1 00 |

Table 1059 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0E D1 01 82 04 00 00 00 00 84 82 00 25 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 15 E1 13 E2 11 E3 0F E8 0D C1 0B 41 4D 45 58 20 34 2E 30 2E 32 00 |

##