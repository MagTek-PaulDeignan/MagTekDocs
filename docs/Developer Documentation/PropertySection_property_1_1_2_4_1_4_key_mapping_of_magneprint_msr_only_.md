---
title: Property 1.1.2.4.1.4 Key Mapping of Magneprint (MSR Only)
layout: home
parent: Configuration
nav_order: 44
---

## Property 1.1.2.4.1.4 Key Mapping of Magneprint (MSR Only)

Table 548 - Property 1.1.2.4.1.4 Key Mapping of Magneprint (MSR Only)Key
Mapping of Magneprint

| Property Description |  |
|----|----|
| Property OID | 1.1.2.4.1.4 / 0x010102040104 |
| Name | Key Mapping of Magneprint |
| Description | The device uses this property to determine which DUKPT Key Set and Variant/Usage shall be used for Magneprint. |
| Securing Key | None |
| Min. Len (b) | 0x03 |
| Max. Len (b) | 0x03 |
| Data Type | Binary |
| Valid Values | See DUKPT Key Mapping for detail information. |
| Default | 0x20, 0x07, 0x04 |

Table 549 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040159D101 841AD101 81072B06010401F609 850101 890AE108E206E404E102C400 |

Table 550 - Get Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 81048259D101 820400000000 8482001DD101 81072B06010401F609
850101</p>
<p>890DE10BE209E407E105C4 03200704</p></td>
</tr>
</tbody>
</table>

Table 551 - Set Request Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104015AD111 841DD111 81072B06010401F609 850101
890DE10BE209E407E105C4</p>
<p>03200704</p></td>
</tr>
</tbody>
</table>

Table 552 - Set Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104825AD111 820400000000 8482001DD111 81072B06010401F609
850101</p>
<p>890DE10BE209E407E105C4 03200704</p></td>
</tr>
</tbody>
</table>

##