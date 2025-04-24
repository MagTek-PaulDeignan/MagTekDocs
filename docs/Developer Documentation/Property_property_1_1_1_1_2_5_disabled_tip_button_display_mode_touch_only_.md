---
title: Property 1.1.1.1.2.5 Disabled Tip Button Display Mode (Touch Only)
layout: home
parent: Configuration
nav_order: 27
---

## Property 1.1.1.1.2.5 Disabled Tip Button Display Mode (Touch Only)

---

- [Property 1.1.1.1.2.5 Disabled Tip Button Display Mode (Touch Only)](#property-111125-disabled-tip-button-display-mode-touch-only)

---


Table 466 - Property 1.1.1.1.2.5 Disabled Tip Button Display Mode (Touch
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
<td>1.1.1.1.2.5 / 0x010101010205</td>
</tr>
<tr>
<td>Name</td>
<td>Disabled Tip Button Display Mode</td>
</tr>
<tr>
<td>Description</td>
<td>The device will check this property to determine how to handle or
display a disabled Tip button.</td>
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
<td><p>0x00 – Display as Blank</p>
<p>0x01 – Display as Disabled (grayed-out)</p>
<p>0x02 - Invisible</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x02 - Invisible</td>
</tr>
</tbody>
</table>

Table 467 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101028902C500 |

Table 468 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704010101028903C50100 |

Table 469 - Set Request Example

| Example (Hex)                                        |
|------------------------------------------------------|
| AA0081040155D1118410D1118501018704010101028903C50100 |

Table 470 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704010101028903C50100 |

##