---
title: Property 1.2.3.1.2.2 Display Backlight Intensity (Display Only)
layout: home
parent: Configuration
nav_order: 123
---

## Property 1.2.3.1.2.2 Display Backlight Intensity (Display Only)

Table 906- Property 1.2.3.1.2.2 Display Backlight Intensity (Display
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
<td>1.2.3.1.2.2 / 0x010203010202</td>
</tr>
<tr>
<td>Name</td>
<td>Display Backlight Intensity</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set the intensity of the
display’s backlight, expressed as a percentage range from 1% to
100%.</p>
<p>The backlight setting takes effect immediately after the host changes
it.</p></td>
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
<td>0x01..0x64</td>
</tr>
<tr>
<td>Default</td>
<td>0x5A (90%)</td>
</tr>
</tbody>
</table>

Table 907 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 01 84 0F D1 01 85 01 01 87 04 02 03 01 02 89 02 C2 00 |

Table 908 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 10 D1 01 85 01 01 87 04 02 03 01 02 89 03 C2 01 5A |

Table 909 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 10 D1 11 85 01 01 87 04 02 03 01 02 89 03 C2 0164 |

Table 910 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 02 03 01 02 89 03 C2 01 64 |

##