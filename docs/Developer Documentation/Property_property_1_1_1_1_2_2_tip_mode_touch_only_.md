---
title: Property 1.1.1.1.2.2 Tip Mode(Touch Only)
layout: home
parent: Configuration
nav_order: 24
---

## Property 1.1.1.1.2.2 Tip Mode(Touch Only)

---

- [Property 1.1.1.1.2.2 Tip Mode(Touch Only)](#property-111122-tip-modetouch-only)

---


Table 451 - Property 1.1.1.1.2.2 Tip Mode(Touch Only)

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
<td>1.1.1.1.2.2 / 0x010101010202</td>
</tr>
<tr>
<td>Name</td>
<td>Tip Mode</td>
</tr>
<tr>
<td>Description</td>
<td>The Tip Mode to use when in Event Driven mode</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1F</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1F</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Byte 1 Tip Mode</p>
<p>0x00 – Disable Tip Mode</p>
<p>0x01 – Show Tip GUI immediately using % value</p>
<p>0x02 – Show Tip GUI immediately using $ amount</p>
<p>Byte 2, Display Mode for Button1</p>
<p>0 - % or Amount</p>
<p>1 – Display Custom</p>
<p>2 – Display NO TIP</p>
<p>3 – Disabled (An OID controls whether the button is blank, grayed out
or not showing)</p>
<p>Bytes 3 to 6 Value in % or Amount for Button 1, if applicable</p>
<p>Byte 7, Display Mode for Button 2 (See Byte 2 for Details)</p>
<p>Bytes 8 to 11 Value in % or Amount for Button 2, if applicable</p>
<p>Byte 12, Display Mode for Button 3 (See Byte 2 for Details)</p>
<p>Bytes 13 to 16 Value in % or Amount for Button 3, if applicable</p>
<p>Byte 17, Display Mode for Button 4 (See Byte 2 for Details)</p>
<p>Bytes 18 to 21 Value in % or Amount for Button 4, if applicable</p>
<p>Byte 22, Display Mode for Button 5 (See Byte 2 for Details)</p>
<p>Bytes 23 to 26 Value in % or Amount for Button 5, if applicable</p>
<p>Byte 27, Display Mode for Button 6 (See Byte 2 for Details)</p>
<p>Bytes 28 to 31 Value in % or Amount for Button 6, if
applicable</p></td>
</tr>
<tr>
<td>Default</td>
<td><p>0x1, // show tip GUI using %</p>
<p>0x0, 0x0, 0x0, 0x0, 0x15, // button 1, %, value 15</p>
<p>0x0, 0x0, 0x0, 0x0, 0x20, // button 2, %, value 20</p>
<p>0x0, 0x0, 0x0, 0x0, 0x25, // button 3, %, value 25</p>
<p>0x2, 0x0, 0x0, 0x0, 0x0, // button 4 'no tip'</p>
<p>0x1, 0x0, 0x0, 0x0, 0x0, // button 5 'custom'</p>
<p>0x3, 0x0, 0x0, 0x0, 0x0, // button 6 disabled</p></td>
</tr>
</tbody>
</table>

Table 452 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010102 8902 C200 |

Table 453 - Get Response Example

| Example (Hex) |
|----|
| AA0081048255D1018204000000008482002ED1018501018704010101028921C21F00000000001500000000200000000025020000000001000000000300000000 |

Table 454 - Set Request Example

| Example (Hex) |
|----|
| AA0081040155D111842ED1118501018704010101028921C21F00000000001500000000200000000025020000000001000000000300000000 |

Table 455 - Set Response Example

| Example (Hex) |
|----|
| AA0081048255D1118204000000008482002ED1118501018704010101028921C21F00000000001500000000200000000025020000000001000000000300000000 |

##