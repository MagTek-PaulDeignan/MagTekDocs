---
title: Property 1.1.1.1.2.3 Tax Rate (Touch Only)
layout: home
parent: Configuration
nav_order: 25
---

## Property 1.1.1.1.2.3 Tax Rate (Touch Only)

---

- [Property 1.1.1.1.2.3 Tax Rate (Touch Only)](#property-111123-tax-rate-touch-only)

---


Table 456 - Property 1.1.1.1.2.3 Tax Rate (Touch Only)

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
<td>1.1.1.1.2.3/ 0x010101010203</td>
</tr>
<tr>
<td>Name</td>
<td>Tax Rate</td>
</tr>
<tr>
<td>Description</td>
<td>Tax Rate that is used when in Event Driven Mode</td>
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
<td>3</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x000000 – Tax Display and Calculation Disabled</p>
<p>0x000001 thru 0x999999- Tax Rate (0.0001% thru 99.9999%)</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x000000 - Tax Display and Calculation Disabled</td>
</tr>
</tbody>
</table>

Table 457 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101028902C300 |

Table 458 - Get Response Example

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA0081048255D10182040000000084820012D1018501018704010101028905C303000000 |

Table 459 - Set Request Example

| Example (Hex)                                            |
|----------------------------------------------------------|
| AA0081040155D1118412D1118501018704010101028905C303108725 |

Table 460 - Set Response Example

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA0081048255D11182040000000084820012D1118501018704010101028905C303108725 |

##