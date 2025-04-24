---
title: Property 1.1.2.4.1.2 Key Mapping of Account Data
layout: home
parent: Configuration
nav_order: 42
---

## Property 1.1.2.4.1.2 Key Mapping of Account Data

Table 538 - Property 1.1.2.4.1.2 Key Mapping of Account DataKey Mapping
of Account Data

| Property Description |  |
|----|----|
| Property OID | 1.1.2.4.1.2 / 0x010102040102 |
| Name | Key Mapping of Account Data |
| Description | The device uses this property to determine which DUKPT Key Set and Variant/Usage shall be used for Account Data. |
| Securing Key | None |
| Min. Len (b) | 0x03 |
| Max. Len (b) | 0x03 |
| Data Type | Binary |
| Valid Values | See DUKPT Key Mapping for detail information. |
| Default | 0x20, 0x07, 0x04 |

Table 539 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040159D101 841AD101 81072B06010401F609 850101 890AE108E206E404E102C200 |

Table 540 - Get Response Example

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
<p>890DE10BE209E407E105C2 03200704</p></td>
</tr>
</tbody>
</table>

Table 541 - Set Request Example

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
890DE10BE209E407E105C2</p>
<p>03200704</p></td>
</tr>
</tbody>
</table>

Table 542 - Set Response Example

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
<p>890DE10BE209E407E105C2 03200704</p></td>
</tr>
</tbody>
</table>

##