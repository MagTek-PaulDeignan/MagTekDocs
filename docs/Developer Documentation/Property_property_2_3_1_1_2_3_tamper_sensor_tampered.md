---
title: Property 2.3.1.1.2.3 Tamper Sensor Tampered
layout: home
parent: Configuration
nav_order: 227
---

## Property 2.3.1.1.2.3 Tamper Sensor Tampered

---

- [Property 2.3.1.1.2.3 Tamper Sensor Tampered](#property-231123-tamper-sensor-tampered)

---


Table 1178 - Property 2.3.1.1.2.3 Tamper Sensor Tampered

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
<td>2.3.1.1.2.3 / 0x020301010203</td>
</tr>
<tr>
<td>Name</td>
<td>Tamper Sensor Tampered</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to report whether a tamper sensor has
tampered. A device that is operating normally should not reported that
it has been tampered with. To examine the device’s tamper history to
determine the cause, use <strong>Command 0xF014 - Read Log (MAGTEK
INTERNAL ONLY)</strong> or <strong>Command 0xF015 - Read Log &amp; Clear
Tamper (MAGTEK INTERNAL ONLY)</strong>.</td>
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
<td><p>0x00 = Not Tampered</p>
<p>0x01 = Tampered</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1179 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010102 8902 C300 |

Table 1180 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010102 8903 C301 00 |

##