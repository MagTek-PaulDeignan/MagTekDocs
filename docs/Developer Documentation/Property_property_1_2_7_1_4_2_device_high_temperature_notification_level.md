---
title: Property 1.2.7.1.4.2 Device High Temperature Notification Level
layout: home
parent: Configuration
nav_order: 138
---

## Property 1.2.7.1.4.2 Device High Temperature Notification Level

---

- [Property 1.2.7.1.4.2 Device High Temperature Notification Level](#property-127142-device-high-temperature-notification-level)

---


Table 968 - Property 1.2.7.1.4.2 Device High Temperature Notification
Level

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
<td>1.2.7.1.4.2 / 0x010207010402</td>
</tr>
<tr>
<td>Name</td>
<td>Device High Temperature Notification Level</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device will send a high temperature notification when the
device’s temperature rises above this temperature. The temperature is in
degrees Celsius.</p>
<p>The Device High Temperature Notification Level takes effect
immediately after the host changes it.</p></td>
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
<td>Signed Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Temperature in Celsius:<br />
DynaProx: 0xE2 .. 0x55 (-30 .. 85)<br />
DynaProx BCR: 0xEC .. 0x37 (-20 .. 55)<br />
DynaFlex: 0x00 .. 0x2D (0 .. 45)</p>
<p>This value must be greater than that set in 1.2.7.1.4.1.</p></td>
</tr>
<tr>
<td>Default</td>
<td>Temperature in Celsius:<br />
DynaProx: 0x55 (85)<br />
DynaProx BCR: 0x37 (55)<br />
DynaFlex: 0x2D (45)</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table 969 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02070104 8902 C200 |

Table 8.3‑230 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D101 8204 00000000 84820010 D101 8501 01 8704 02070104 8903 C201 2D |

Table 970 - Set Request Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA00 81040155D111 8410 D111 8501 01 8704 02070104 8903 C201 2D |

Table 8.3‑232 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D111 8204 00000000 84820010 D111 8501 01 870402070104 8903 C201 2D |

##