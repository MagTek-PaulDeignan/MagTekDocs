---
title: Property 1.1.1.1.4.2 CA Public Key Configuration Filename
layout: home
parent: Configuration
nav_order: 34
---

## Property 1.1.1.1.4.2 CA Public Key Configuration Filename

---

- [Property 1.1.1.1.4.2 CA Public Key Configuration Filename](#property-111142-ca-public-key-configuration-filename)

---


Table 501 - Property 1.1.1.1.4.2 CA Public Key Configuration Filename

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.4.2 / 0x010101010402 |
| Name | CA Public Key Configuration Filename |
| Description | This string contains the part number and the revision of the CA Public Key Configuration File. |
| Securing Key | None |
| Min. Len (b) | 14 |
| Max. Len (b) | 14 |
| Data Type | ASCII |
| Valid Values | CFG000xxxx-xxx |
| Default | None |

Table 502 - Get Request Example

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA0081040106D101841AD10181072B06010401F609850101890AE108E106E104E402C200 |

Table 503 - Get Response Example

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
<p>8918E116E114E112E410C20E434647303030363831322D323030</p></td>
</tr>
</tbody>
</table>

Table 504 - Set Request Example

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
<td><p>AA0081040106D1118428D11181072B06010401F6098501018918E116E114E112E410C20E</p>
<p>434647303030363831322D323030</p></td>
</tr>
</tbody>
</table>

Table 505 - Set Response Example

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
<p>8918E116E114E112E410C20E434647303030363831322D323030</p></td>
</tr>
</tbody>
</table>

#