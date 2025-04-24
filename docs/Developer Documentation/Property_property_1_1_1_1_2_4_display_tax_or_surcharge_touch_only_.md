---
title: Property 1.1.1.1.2.4 Display Tax or Surcharge (Touch Only)
layout: home
parent: Configuration
nav_order: 26
---

## Property 1.1.1.1.2.4 Display Tax or Surcharge (Touch Only)

---

- [Property 1.1.1.1.2.4 Display Tax or Surcharge (Touch Only)](#property-111124-display-tax-or-surcharge-touch-only)

---


Table 461 - Property 1.1.1.1.2.4 Display Tax or Surcharge (Touch Only)

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
<td>1.1.1.1.2.4 / 0x010101010204</td>
</tr>
<tr>
<td>Name</td>
<td>Display Tax or Surcharge Control</td>
</tr>
<tr>
<td>Description</td>
<td>The device will check this property to determine to display Tax or
Surcharge label.</td>
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
<td><p>0x00 – Display Tax</p>
<p>0x01 – Display Surcharge</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00 – Display Tax</td>
</tr>
</tbody>
</table>

Table 462 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101028902C400 |

Table 463 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704010101028903C40100 |

Table 464 - Set Request Example

| Example (Hex)                                        |
|------------------------------------------------------|
| AA0081040155D1118410D1118501018704010101028903C40100 |

Table 465 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704010101028903C40100 |

##