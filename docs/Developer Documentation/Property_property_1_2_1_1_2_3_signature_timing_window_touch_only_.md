---
title: Property 1.2.1.1.2.3 Signature Timing Window (Touch Only)
layout: home
parent: Configuration
nav_order: 59
---

## Property 1.2.1.1.2.3 Signature Timing Window (Touch Only)

---

- [Property 1.2.1.1.2.3 Signature Timing Window (Touch Only)](#property-121123-signature-timing-window-touch-only)

---


Table 603 - Property 1.2.1.1.2.3 Signature Timing Window (Touch Only)

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
<td>1.2.1.1.2.3 / 0x010201010203</td>
</tr>
<tr>
<td>Name</td>
<td>Signature Timing Window</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine how long to wait, in
seconds, for <strong>Command 0x1801 - Request Cardholder
Signature</strong> while running <strong>Command 0x1001 - Start
Transaction</strong>.</td>
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
<td><p>0x00 = No Wait Time. If the device uses this setting, the host
must wait at least one second after receiving <strong>Notification
0x0105 - Transaction Operation Complete</strong> before performing any
other operations.</p>
<p>0x01..0xFF = Wait the Specified Number of Seconds</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x01 (second)</td>
</tr>
</tbody>
</table>

Table 604 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 04 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E2 02 C3 00 |

Table 605 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 04 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C3 01 03 |

Table 606 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 02 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C3 01 01 |

Table 607 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 02 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C3 01 01 |

##