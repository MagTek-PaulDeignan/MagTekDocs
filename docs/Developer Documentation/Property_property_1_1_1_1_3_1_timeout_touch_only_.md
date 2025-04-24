---
title: Property 1.1.1.1.3.1 Timeout (Touch Only)
layout: home
parent: Configuration
nav_order: 29
---

## Property 1.1.1.1.3.1 Timeout (Touch Only)

---

- [Property 1.1.1.1.3.1 Timeout (Touch Only)](#property-111131-timeout-touch-only)

---


Table 476 - Property 1.1.1.1.3.1 Timeout (Touch Only)

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
<td>1.1.1.1.3.1 / 0x010101010301</td>
</tr>
<tr>
<td>Name</td>
<td>Timeout</td>
</tr>
<tr>
<td>Description</td>
<td>Transaction Timeout in seconds</td>
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
<td><p>0x00 – No Timeout</p>
<p>0x01 – 0xFF (1 to 255 Seconds)</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x78 – 120 seconds</td>
</tr>
</tbody>
</table>

Table 477 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101038902C100 |

Table 478 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704010101038903C10178 |

Table 479 - Set Request Example

| Example (Hex)                                        |
|------------------------------------------------------|
| AA0081040155D1118410D1118501018704010101038903C10150 |

Table 480 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704010101038903C10150 |

##