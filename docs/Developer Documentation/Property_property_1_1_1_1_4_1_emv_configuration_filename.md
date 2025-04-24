---
title: Property 1.1.1.1.4.1 EMV Configuration Filename
layout: home
parent: Configuration
nav_order: 33
---

## Property 1.1.1.1.4.1 EMV Configuration Filename

---

- [Property 1.1.1.1.4.1 EMV Configuration Filename](#property-111141-emv-configuration-filename)

---


Table 496 - Property 1.1.1.1.4.1 EMV Configuration Filename

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.4.1 / 0x010101010401 |
| Name | EMV Configuration Filename |
| Description | This string contains the part number and the revision of the EMV Configuration File. |
| Securing Key | None |
| Min. Len (b) | 14 |
| Max. Len (b) | 14 |
| Data Type | ASCII |
| Valid Values | CFG000xxxx-xxx |
| Default | None |

Table 497 - Get Request Example

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA0081040106D101841AD10181072B06010401F609850101890AE108E106E104E402C100 |

Table 498 - Get Response Example

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
<td><p>AA0081048206D10182040000000084820028D10181072B06010401F609850101</p>
<p>8918E116E114E112E410C10E434647303030363831322D323030</p></td>
</tr>
</tbody>
</table>

Table 499 - Set Request Example

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
<td><p>AA0081040106D1118428D11181072B06010401F6098501018918E116E114E112E410C10E</p>
<p>434647303030363831322D323030</p></td>
</tr>
</tbody>
</table>

Table 500 - Set Response Example

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
<td><p>AA0081048206D11182040000000084820028D11181072B06010401F609850101</p>
<p>8918E116E114E112E410C10E434647303030363831322D323030</p></td>
</tr>
</tbody>
</table>

##