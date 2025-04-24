---
title: Property 2.1.2.3.A.1 JCB Kernel ID (Contactless Only) (Common Kernel Only)
layout: home
parent: Configuration
nav_order: 180
---

## Property 2.1.2.3.A.1 JCB Kernel ID (Contactless Only) (Common Kernel Only)

---

- [Property 2.1.2.3.A.1 JCB Kernel ID (Contactless Only) (Common Kernel Only)](#property-2123a1-jcb-kernel-id-contactless-only-common-kernel-only)

---


Table 1069 - Property 2.1.2.3.A.1 JCB Kernel ID (Contactless Only)
(Common Kernel Only)

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
<td>2.1.2.3.A.1 / 0x020102030A01</td>
</tr>
<tr>
<td>Name</td>
<td>JCB Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the JCB Kernel ID as
string, padded with null characters.</p>
<p>Example: JCB 1.6</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>11</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>11</td>
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

Table 1070 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EA 02 C1 00 |

Table 1071 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 22 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 12 E1 10 E2 0E E3 0C EA 0A C1 08 4A 43 42 20 31 2E 36 00 |

##