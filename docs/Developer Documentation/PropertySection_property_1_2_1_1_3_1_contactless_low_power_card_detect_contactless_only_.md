---
title: Property 1.2.1.1.3.1 Contactless Low Power Card Detect (Contactless Only)
layout: home
parent: Configuration
nav_order: 60
---

## Property 1.2.1.1.3.1 Contactless Low Power Card Detect (Contactless Only)

Table 608 - Property 1.2.1.1.3.1 Contactless Low Power Card Detect
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
<td>1.2.1.1.3.1 / 0x0102010100301</td>
</tr>
<tr>
<td>Name</td>
<td>Contactless Low Power Card Detect</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to enable/disable contactless low
power card detect (Proximity Detection Mode). When disabled, device will
read a contactless card as soon as the card is detected. If enabled,
device will track and delay reading a contactless card, allowing user to
use Contact or MSR card slots.</td>
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
<td><p>0x00 = Disable</p>
<p>0x01 = Enable</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00 - Disabled</td>
</tr>
</tbody>
</table>

Table 609 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 01 84 0F D1 01 85 01 01 87 04 02 01 01 03 89 02 C1 00 |

Table 610 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 10 D1 01 85 01 01 87 04 02 01 01 03 89 03 C1 01 00 |

Table 611 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 10 D1 11 85 01 01 87 04 02 01 01 03 89 03 C1 01 00 |

Table 612 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 02 01 01 03 89 03 C1 01 00 |

##