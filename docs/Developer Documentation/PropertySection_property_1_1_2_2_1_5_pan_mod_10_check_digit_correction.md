---
title: Property 1.1.2.2.1.5 PAN MOD 10 Check Digit Correction
layout: home
parent: Configuration
nav_order: 39
---

## Property 1.1.2.2.1.5 PAN MOD 10 Check Digit Correction

Table 523 - Property 1.1.2.2.1.5 PAN MOD 10 Check Digit Correction

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
<td>1.1.2.2.1.5 / 0x010102020105</td>
</tr>
<tr>
<td>Name</td>
<td>PAN MOD 10 Check Digit Correction</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine whether it should modify
one of the masked PAN digits such that the masked PAN passes the Luhn
MOD-10 algorithm check. If this property is enabled, the device uses
masking character ‘0’ to mask the PAN, regardless of the setting in
<strong>Property 1.1.2.2.1.2 ISO/ABA Masking Character</strong>, and
masks the remainder of the track data with the configured masking
character.</td>
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
<td>0x01</td>
</tr>
</tbody>
</table>

Table 524 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1A D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E2 04 E1 02 C5 00 |

Table 525 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 1A D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C5 01 01 |

Table 526 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 12 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C5 01 01 |

Table 527 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 12 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C5 01 01 |

##