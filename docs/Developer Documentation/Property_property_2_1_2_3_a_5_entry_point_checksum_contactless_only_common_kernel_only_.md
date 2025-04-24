---
title: Property 2.1.2.3.A.5 Entry Point Checksum (Contactless Only) (Common Kernel Only)
layout: home
parent: Configuration
nav_order: 184
---

## Property 2.1.2.3.A.5 Entry Point Checksum (Contactless Only) (Common Kernel Only)

---

- [Property 2.1.2.3.A.5 Entry Point Checksum (Contactless Only) (Common Kernel Only)](#property-2123a5-entry-point-checksum-contactless-only-common-kernel-only)

---


Table 1081 - Property 2.1.2.3.A.5 Entry Point Checksum (Contactless
Only) (Common Kernel Only) (Common Kernel Only)

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
<td>2.1.2.3.A.5/ 0x020102030A05</td>
</tr>
<tr>
<td>Name</td>
<td>Entry Point Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Entry Point Checksum
as string, no padding.</p>
<p>Example: 1B3725A7DBC220805DF369E035E935EF404C4B71</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Variable</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>75</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1082 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EA 02 C5 00 |

Table 1083 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 42 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 32 E1 30 E2 2E E3 2C EA 2A C5 28 31 42 33 37 32 35 41 37 44 42 43 32 32 30 38 30 35 44 46 33 36 39 45 30 33 35 45 39 33 35 45 46 34 30 34 43 34 42 37 31 |

##