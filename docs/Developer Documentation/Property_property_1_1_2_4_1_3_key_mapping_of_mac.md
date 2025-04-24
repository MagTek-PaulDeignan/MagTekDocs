---
title: Property 1.1.2.4.1.3 Key Mapping of MAC
layout: home
parent: Configuration
nav_order: 43
---

## Property 1.1.2.4.1.3 Key Mapping of MAC

---

- [Property 1.1.2.4.1.3 Key Mapping of MAC](#property-112413-key-mapping-of-mac)

---


Table 543 - Property 1.1.2.4.1.3 Key Mapping of MACKey Mapping of MAC

| Property Description |  |
|----|----|
| Property OID | 1.1.2.4.1.3 / 0x010102040103 |
| Name | Key Mapping of MAC |
| Description | The device uses this property to determine which DUKPT Key Set and Variant/Usage shall be used for MAC. |
| Securing Key | None |
| Min. Len (b) | 0x03 |
| Max. Len (b) | 0x03 |
| Data Type | Binary |
| Valid Values | See DUKPT Key Mapping for detail information. |
| Default | 0x20, 0x07, 0x02 |

Table 544 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040159D101 841AD101 81072B06010401F609 850101 890AE108E206E404E102C300 |

Table 545 - Get Response Example

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
<p>890DE10BE209E407E105C3 03200702</p></td>
</tr>
</tbody>
</table>

Table 546 - Set Request Example

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
890DE10BE209E407E105C3</p>
<p>03200702</p></td>
</tr>
</tbody>
</table>

Table 547 - Set Response Example

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
<p>890DE10BE209E407E105C3 03200702</p></td>
</tr>
</tbody>
</table>

##