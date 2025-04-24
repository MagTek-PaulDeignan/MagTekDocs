---
title: Property 1.1.2.2.1.6 PAN MOD 10 Check Digit Validation (MCE Only)
layout: home
parent: Configuration
nav_order: 40
---

## Property 1.1.2.2.1.6 PAN MOD 10 Check Digit Validation (MCE Only)

---

- [Property 1.1.2.2.1.6 PAN MOD 10 Check Digit Validation (MCE Only)](#property-112216-pan-mod-10-check-digit-validation-mce-only)

---


Table 528 - Property 1.1.2.2.1.6 PAN MOD 10 Check Digit Validation (MCE
Only)

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
<td>1.1.2.2.1.6 / 0x010102020106</td>
</tr>
<tr>
<td>Name</td>
<td>PAN MOD 10 Check Digit Validation</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine whether to use the Luhn
MOD-10 algorithm to validate card number (PAN) digits a cardholder or
operator enters in manual card entry mode during <strong>Command 0x1001
- Start Transaction</strong>. If validation is enabled, the device
checks the PAN digits during entry, and until the PAN passes the check,
the device disables the ENTER key, sounds an error tone when the Enter
key is pressed (if the command has audio feedback enabled), and stays at
the Card Number prompt until the cardholder or operator presses the
Cancel button or corrects the PAN.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Disabled</p>
<p>0x01 = Enabled</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 529 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1A D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E2 04 E1 02 C6 00 |

Table 530 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 1A D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C6 01 00 |

Table 531 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 12 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C6 01 01 |

Table 532 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 12 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C6 01 01 |

##