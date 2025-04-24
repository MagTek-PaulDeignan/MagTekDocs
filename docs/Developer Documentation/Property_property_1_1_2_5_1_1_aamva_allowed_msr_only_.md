---
title: Property 1.1.2.5.1.1 AAMVA Allowed (MSR Only)
layout: home
parent: Configuration
nav_order: 48
---

## Property 1.1.2.5.1.1 AAMVA Allowed (MSR Only)

---

- [Property 1.1.2.5.1.1 AAMVA Allowed (MSR Only)](#property-112511-aamva-allowed-msr-only)

---


Table 558 - Property 1.1.2.5.1.1 AAMVA Allowed (MSR Only)

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
<td>1.1.2.5.1.1 / 0x010102 050101</td>
</tr>
<tr>
<td>Name</td>
<td>AAMVA Allowed</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine whether it should accept
AAMVA (driver’s license) and other permutations of ISO encoded cards in
addition to ISO/ABA financial cards. If this is disabled, the
<strong>EMV ARQC Type</strong> the device returns to the host includes
Track Status = <strong>Error</strong> for any track that exists but does
not comply with ISO/ABA financial card format.</td>
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

Table 559 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1B D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E5 04 E1 02 C1 00 |

Table 560 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 1B D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C1 01 01 |

Table 561 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 14 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C1 01 01 |

Table 562 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 14 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C1 01 01s |

##