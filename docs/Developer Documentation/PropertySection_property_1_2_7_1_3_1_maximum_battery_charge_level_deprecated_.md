---
title: Property 1.2.7.1.3.1 Maximum Battery Charge Level (Deprecated)
layout: home
parent: Configuration
nav_order: 136
---

## Property 1.2.7.1.3.1 Maximum Battery Charge Level (Deprecated)

Table 960 - Property 1.2.7.1.3.1 Maximum Battery Charge Level
(Deprecated)

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
<td>1.2.7.1.3.1 / 0x010207010301</td>
</tr>
<tr>
<td>Name</td>
<td>Maximum Battery Charge Level</td>
</tr>
<tr>
<td>Description</td>
<td><p>This OID has been deprecated. The OID can be written or read but
it will have no effect of the device’s behavior.</p>
<p>The host can use this property to control the maximum charge level
for the battery. All charge percentages reported or displayed will use
this percentage as 100% charged.</p>
<p>Setting this value to lower than 0x64 (100%) will increase the life
of the battery but reduce the run time when running from the
battery.</p>
<p>The Maximum Battery Charge Level takes effect immediately after the
host changes it.</p></td>
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
<td>0x0A..0x64</td>
</tr>
<tr>
<td>Default</td>
<td><p>0x64 (100%) if WLAN device</p>
<p>0x50 (80%) for all other devices</p></td>
</tr>
</tbody>
</table>

Table 961 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02070103 8902 C100 |

Table 962 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D101 8204 00000000 84820010 D101 8501 01 8704 02070103 8903 C101 50 |

Table 963 - Set Request Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA00 81040155D111 8410 D111 8501 01 8704 02070103 8903 C101 50 |

Table 8.3‑222 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D111 8204 00000000 84820010 D111 8501 01 8704 02070103 8903 C101 50 |

##