---
title: Property 1.1.2.4.1.1 Key Mapping of PIN-TDES (Touch Only)
layout: home
parent: Configuration
nav_order: 41
---

## Property 1.1.2.4.1.1 Key Mapping of PIN-TDES (Touch Only)

Table 533 - Property 1.1.2.4.1.1 Key Mapping of PIN-TDES (Touch Only)Key
Mapping of PIN-TDES

| Property Description |  |
|----|----|
| Property OID | 1.1.2.4.1.1 / 0x010102040101 |
| Name | Key Mapping of PIN-TDES |
| Description | The device uses this property to determine which DUKPT Key Set and Variant shall be used for PIN-TDES. |
| Securing Key | None |
| Min. Len (b) | 0x03 |
| Max. Len (b) | 0x03 |
| Data Type | Binary |
| Valid Values | See DUKPT Key Mapping for detail information. |
| Default | 0x00, 0x00, 0x01 |

Table 534 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040159D101 841AD101 81072B06010401F609 850101 890AE108E206E404E102C100 |

Table 535 - Get Response Example

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
<p>890DE10BE209E407E105C1 03200701</p></td>
</tr>
</tbody>
</table>

Table 536 - Set Request Example

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
890DE10BE209E407E105C1</p>
<p>03200701</p></td>
</tr>
</tbody>
</table>

Table 537 - Set Response Example

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
<p>890DE10BE209E407E105C1 03200701</p></td>
</tr>
</tbody>
</table>

##