---
title: Property 1.2.2.1.1.5 Use DHCP
layout: home
parent: Configuration
nav_order: 77
---

## Property 1.2.2.1.1.5 Use DHCP

---

- [Property 1.2.2.1.1.5 Use DHCP](#property-122115-use-dhcp)

---


Table 688 - Property 1.2.2.1.1.5 Use DHCP

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
<td>1.2.2.1.1.5 / 0x010202010105</td>
</tr>
<tr>
<td>Name</td>
<td>Use_DHCP</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if it gets its IP from
a DHCP server or uses a static IP.</p>
<p>0000—use static IP address;</p>
<p>othervalue—get IP address from DHCP server</p></td>
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
<td>0000 to FFFF</td>
</tr>
<tr>
<td>Default</td>
<td>0001</td>
</tr>
</tbody>
</table>

Table 689 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040117D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C500 |

Table 690 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048217D101 820400000000 8482001ED101 81072B06010401F609 850101 890EE20CE20AE108E106C50400000001 |

Table 691 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040116D111 841ED111 81072B06010401F609 850101 890EE20CE20AE108E106C50400000001 |

Table 692 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048216D111 820400000000 8482001ED111 81072B06010401F609 850101 890EE20CE20AE108E106C50400000001 |

##