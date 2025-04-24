---
title: Property 2.1.2.3.A.3 JCB Kernel Checksum (Contactless Only) (Common Kernel Only)
layout: home
parent: Configuration
nav_order: 182
---

## Property 2.1.2.3.A.3 JCB Kernel Checksum (Contactless Only) (Common Kernel Only)

---

- [Property 2.1.2.3.A.3 JCB Kernel Checksum (Contactless Only) (Common Kernel Only)](#property-2123a3-jcb-kernel-checksum-contactless-only-common-kernel-only)

---


Table 1075 - Property 2.1.2.3.A.3 JCB Kernel Checksum (Contactless Only)
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
<td>2.1.2.3.A.3/ 0x020102030A03</td>
</tr>
<tr>
<td>Name</td>
<td>JCB Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the JCB Kernel Checksum
as string, no padding.</p>
<p>Example: JCB 1.6 -&gt; v1.0.29
[ca44a90cd42d379088fcb8ca8d1fab195546b278]</p></td>
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

Table 1076 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 11 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EA 02 C3 00 |

Table 1077 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 57 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 47 E1 45 E2 43 E3 41 EA 3F C3 3D 4A 43 42 20 31 2E 36 20 2D 3E 20 76 31 2E 30 2E 32 39 20 5B 63 61 34 34 61 39 30 63 64 34 32 64 33 37 39 30 38 38 66 63 62 38 63 61 38 64 31 66 61 62 31 39 35 35 34 36 62 32 37 38 5D |

##