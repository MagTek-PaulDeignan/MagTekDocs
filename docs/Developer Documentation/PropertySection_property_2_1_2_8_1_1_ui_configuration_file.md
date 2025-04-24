---
title: Property 2.1.2.8.1.1 UI Configuration File
layout: home
parent: Configuration
nav_order: 213
---

## Property 2.1.2.8.1.1 UI Configuration File

Table 1151 - Property 2.1.2.8.1.1 UI Configuration File

| Property Description |  |
|----|----|
| Property OID | 2.1.2.8.1.1 / 0x020102080101 |
| Name | UI Configuration Filename |
| Description | This string contains the part number and the revision of the UI Configuration File. |
| Securing Key | None |
| Min. Len (b) | 14 |
| Max. Len (b) | 14 |
| Data Type | ASCII |
| Valid Values | CFG000xxxx-xxx |
| Default | None |

Table 1152 - Get Request Example

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA0081040106D101841AD10181072B06010401F609850102890AE108E206E804E102C100 |

Table 1153 - Get Response Example

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
<td><p>AA0081048206D10182040000000084820028D10181072B06010401F609850102</p>
<p>8918E116E214E812E110C10E434647303030363831322D323030</p></td>
</tr>
</tbody>
</table>