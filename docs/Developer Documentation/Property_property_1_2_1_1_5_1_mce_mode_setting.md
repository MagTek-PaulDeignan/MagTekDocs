---
title: Property 1.2.1.1.5.1 MCE Mode Setting
layout: home
parent: Configuration
nav_order: 71
---

## Property 1.2.1.1.5.1 MCE Mode Setting

---

- [Property 1.2.1.1.5.1 MCE Mode Setting](#property-121151-mce-mode-setting)

---


Table 663 - Property 1.2.1.1.5.1 MCE Mode Setting

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
<td>1.2.1.1.5.1 / 0x0102010100501</td>
</tr>
<tr>
<td>Name</td>
<td>MCE Mode Setting (MCE: Manual Card Entry)</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine how to present a sequence
of pages to the host, prompting the cardholder or operator to enter the
specified sequence of values.</td>
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
<td><p>0x00 = Card Number, Expiration Date, CVV/CVC/Card ID</p>
<p>0x01 = Card Number, Expiration Date</p>
<p>0x02 = Card Number, CVV/CVC/Card ID</p>
<p>0x03 = Card Number</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 664 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E5 02 C1 00 |

Table 665 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E5 03 C1 01 03 |

Table 666 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E5 03 C1 01 03 |

Table 667 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E5 03 C1 01 03 |

#