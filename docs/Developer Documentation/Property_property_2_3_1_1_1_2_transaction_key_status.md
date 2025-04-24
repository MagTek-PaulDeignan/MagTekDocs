---
title: Property 2.3.1.1.1.2 Transaction Key Status
layout: home
parent: Configuration
nav_order: 223
---

## Property 2.3.1.1.1.2 Transaction Key Status

---

- [Property 2.3.1.1.1.2 Transaction Key Status](#property-231112-transaction-key-status)

---


Table 1169 - Property 2.3.1.1.1.2 Transaction Key Status

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
<td>2.3.1.1.1.2 / 0x020301010102</td>
</tr>
<tr>
<td>Name</td>
<td>Transaction Key Status</td>
</tr>
<tr>
<td>Description</td>
<td>This OID contains a 32-bit bitmap. Each bit indicates the status of
a transaction key. A bit value of 1 indicates the corresponding key has
been injected.</td>
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
<td><p>Bit 0: DKPTM0_2000 Bit 16: DKPTM10_2010</p>
<p>Bit 1: DKPTM1_2001 Bit 17: DKPTM11_2011</p>
<p>Bit 2: DKPTM2_2002 Bit 18: DKPTM12_2012</p>
<p>Bit 3: DKPTM3_2003 Bit 19: DKPTM13_2013</p>
<p>Bit 4: DKPTM4_2004 Bit 20: DKPTM14_2014</p>
<p>Bit 5: DKPTM5_2005 Bit 21: DKPTM15_2015</p>
<p>Bit 6: DKPTM6_2006 Bit 22: DKPTM16_2016</p>
<p>Bit 7: DKPTM7_2007 Bit 23: DKPTM17_2017</p>
<p>Bit 8: DKPTM8_2008 Bit 24: DKPTM18_2018</p>
<p>Bit 9: DKPTM9_2009 Bit 25: DKPTM19_2019</p>
<p>Bit 10: DKPTMA_200A Bit 26: DKPTM1A_201A</p>
<p>Bit 11: DKPTMB_200B Bit 27: DKPTM1B_201B</p>
<p>Bit 12: DKPTMC_200C Bit 28: DKPTM1C_201C</p>
<p>Bit 13: DKPTMD_200D Bit 29: DKPTM1D_201D</p>
<p>Bit 14: DKPTME_200E Bit 30: DKPTM1E_201E</p>
<p>Bit 15: DKPTMF_200F Bit 31: DKPTM1F_201F</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1170 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104010FD101 841AD101 81072B06010401F609 850102 890AE308E106E104E102C200 |

Table 1171 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104820FD101 820400000000 8482001ED101 81072B06010401F609 850102 890EE30CE10AE108E106C20400000081 |

#