---
title: Property 1.2.1.1.2.1 Signature Capture Control
layout: home
parent: Configuration
nav_order: 57
---

## Property 1.2.1.1.2.1 Signature Capture Control

---

- [Property 1.2.1.1.2.1 Signature Capture Control](#property-121121-signature-capture-control)

---


Table 593 - Property 1.2.1.1.2.1 Signature Capture Control

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
<td>1.2.1.1.2.1 / 0x010201010201</td>
</tr>
<tr>
<td>Name</td>
<td>Signature Capture Control</td>
</tr>
<tr>
<td>Description</td>
<td>The host can use this property to change whether the device
automatically prompts the cardholder for a signature when running
<strong>Command 0x1001 - Start Transaction</strong>, or leaves the
triggering of signature capture prompts to the host.</td>
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
<td><p>0x00 = Device-driven Signature Capture</p>
<p>0x01 = Host-driven Signature Capture</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 594 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 04 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E2 02 C1 00 |

Table 595 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 04 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C1 01 01 |

Table 596 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 02 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C1 01 01 |

Table 597 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 02 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C1 01 01 |

##