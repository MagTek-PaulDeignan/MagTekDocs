---
title: Property 2.3.1.1.1.1 Device Key Status
layout: home
parent: Configuration
nav_order: 222
---

## Property 2.3.1.1.1.1 Device Key Status

Table 1166 - Property 2.3.1.1.1.1 Device Key Status

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
<td>2.3.1.1.1.1 / 0x020301010101</td>
</tr>
<tr>
<td>Name</td>
<td>Device Key Status</td>
</tr>
<tr>
<td>Description</td>
<td>This OID contains a 32-bit bitmap. Each bit indicates the status of
a device key. A bit value of 1 indicates the corresponding key has been
injected.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Bit 0: TMPTK_1000</p>
<p>Bit 1: MTK_1001</p>
<p>Bit 2: DEVTK_1002</p>
<p>Bit 3: FINTK_1003</p>
<p>Bit 4: PRODTK_1021</p>
<p>Bit 5: MFGTK_1022</p>
<p>Bit 6: MFIFTK_1081</p>
<p>Bit 7: AKIFTK_1091</p>
<p>Bit 8: FREQMK_1101</p>
<p>Bit 9: MREQMK_1102</p>
<p>Bit 10: MFRQMK_1111</p>
<p>Bit 11: ARQ1MK_1121</p>
<p>Bit 12: ARQ2MK_1122</p>
<p>Bit 13 – 31: Reserved</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1167 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104010ED101 841AD101 81072B06010401F609 850102 890AE308E106E104E102C100 |

Table 1168 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104820ED101 820400000000 8482001E D101 81072B06010401F609 850102 890EE30CE10AE108E106C1040000077E |

##