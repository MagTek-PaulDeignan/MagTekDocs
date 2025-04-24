---
title: Property 1.1.1.1.3.4 Other TLV (Touch Only)
layout: home
parent: Configuration
nav_order: 32
---

## Property 1.1.1.1.3.4 Other TLV (Touch Only)

Table 491 - Property 1.1.1.1.3.4 Other TLV (Touch Only)

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
<td>1.1.1.1.3.4 / 0x010101010304</td>
</tr>
<tr>
<td>Name</td>
<td>Other TLV</td>
</tr>
<tr>
<td>Description</td>
<td>This is a list of self-contained TLV data objects that defines the
basic parameters for the transaction.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>3</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>100</td>
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
<td><p>9C0100 9F0206000000000100 9F0306000000000000 5F2A020840
5F360102</p>
<p>Transaction Type = Purchase</p>
<p>Default Amount for Quickchip = $1.00</p>
<p>Amount, Other = 0</p>
<p>Transaction Currency Code = US Dollar</p>
<p>Transaction Currency Exponent = 2</p></td>
</tr>
</tbody>
</table>

Table 492 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101038902C400 |

Table 493 - Get Response Example

| Example (Hex) |
|----|
| AA0081048255D1018204000000008482002DD1018501018704010101038920C41E9C01009F02060000000001009F03060000000000005F2A0208405F360102 |

Table 494 - Set Request Example

| Example (Hex) |
|----|
| AA0081040155D111842DD1118501018704010101038920C41E9C01009F02060000000001009F03060000000000005F2A0208405F360102 |

Table 495 - Set Response Example

| Example (Hex) |
|----|
| AA0081048255D1118204000000008482002DD1118501018704010101038920C41E9C01009F02060000000001009F03060000000000005F2A0208405F360102 |

##