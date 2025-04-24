---
title: Property 1.1.1.1.3.2 Reader Options (Touch Only)
layout: home
parent: Configuration
nav_order: 30
---

## Property 1.1.1.1.3.2 Reader Options (Touch Only)

Table 481 - Property 1.1.1.1.3.2 Reader Options (Touch Only)

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
<td>1.1.1.1.3.2 / 0x010101010302</td>
</tr>
<tr>
<td>Name</td>
<td>Reader Options</td>
</tr>
<tr>
<td>Description</td>
<td>Configures which payment method interface is enabled, PIN Block
format</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>9</td>
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
<td><p>810101 820101 830101 85020101 860100</p>
<p>MSR Enabled</p>
<p>Contact Enabled</p>
<p>Contactless Enabled</p>
<p>BCR Enabled and Encrypt Non-EMV</p>
<p>PIN Block Format 0</p></td>
</tr>
</tbody>
</table>

Table 482 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101038902C200 |

Table 483 - Get Response Example

| Example (Hex) |
|----|
| AA0081048255D10182040000000084820023D1018501018704010101038916C2148101018201018301018400000085020101860100 |

Table 484 - Set Request Example

| Example (Hex) |
|----|
| AA0081040155D111841FD1118501018704010101038912C21081010182010183010185020101860100 |

Table 485 - Set Response Example

| Example (Hex) |
|----|
| AA0081048255D1118204000000008482001FD1118501018704010101038912C21081010182010183010185020101860100 |

##