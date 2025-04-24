---
title: Property 1.1.1.1.2.6 Tip Mode Enable Submit on Amount Button Press
layout: home
parent: Configuration
nav_order: 28
---

## Property 1.1.1.1.2.6 Tip Mode Enable Submit on Amount Button Press

---

- [Property 1.1.1.1.2.6 Tip Mode Enable Submit on Amount Button Press](#property-111126-tip-mode-enable-submit-on-amount-button-press)

---


Table 471 - Property 1.1.1.1.2.6 Tip Mode Enable Submit on Amount Button
Press

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
<td>1.1.1.1.2.6 / 0x010101010206</td>
</tr>
<tr>
<td>Name</td>
<td>Tip Mode Enable Submit on Amount Button Press</td>
</tr>
<tr>
<td>Description</td>
<td>When enabled, pressing an amount, percent, or ‘no tip’ button on the
tip entry page will proceed immediately without requiring a subsequent
tap of the ‘Submit’ button.</td>
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
<td><p>0x00 – Disabled: Require submit button tap</p>
<p>0x01 – Enabled: Don’t require submit button tap</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00 - Disabled</td>
</tr>
</tbody>
</table>

Table 472 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101028902C600 |

Table 473 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704010101028903C60101 |

Table 474 - Set Request Example

| Example (Hex)                                        |
|------------------------------------------------------|
| AA0081040155D1118410D1118501018704010101028903C60101 |

Table 475 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704010101028903C60101 |

##