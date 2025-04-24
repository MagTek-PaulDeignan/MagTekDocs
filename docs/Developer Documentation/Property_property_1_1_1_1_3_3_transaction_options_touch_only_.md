---
title: Property 1.1.1.1.3.3 Transaction Options (Touch Only)
layout: home
parent: Configuration
nav_order: 31
---

## Property 1.1.1.1.3.3 Transaction Options (Touch Only)

---

- [Property 1.1.1.1.3.3 Transaction Options (Touch Only)](#property-111133-transaction-options-touch-only)

---


Table 486 - Property 1.1.1.1.3.3 Transaction Options (Touch Only)

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
<td>1.1.1.1.3.3 / 0x010101010303</td>
</tr>
<tr>
<td>Name</td>
<td>Transaction Options</td>
</tr>
<tr>
<td>Description</td>
<td>Sets various device behaviors that change the transaction flow or
the way the device reports transaction results</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>20</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td><p>84020007</p>
<p>Apple VAS Disabled</p>
<p>Quickchip</p>
<p>Skip MSR signature capture if service code is chip card</p>
<p>Do not display amount in Quickchip</p></td>
</tr>
</tbody>
</table>

Table 487 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101038902C300 |

Table 488 - Get Response Example

| Example (Hex) |
|----|
| AA0081048255D10182040000000084820023D1018501018704010101038916C3148402000700000000000000000000000000000000 |

Table 489 - Set Request Example

| Example (Hex)                                              |
|------------------------------------------------------------|
| AA0081040155D1118413D1118501018704010101038906C30484020007 |

Table 490 - Set Response Example

| Example (Hex) |
|----|
| AA0081048255D11182040000000084820013D1118501018704010101038906C30484020007 |

##