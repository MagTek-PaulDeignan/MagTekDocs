---
title: Property 1.2.2.1.1.2 Password
layout: home
parent: Configuration
nav_order: 74
---

## Property 1.2.2.1.1.2 Password

---

- [Property 1.2.2.1.1.2 Password](#property-122112-password)

---


Table 673 - Property 1.2.2.1.1.2 Password

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
<td>1.2.2.1.1.2 / 0x010202010102</td>
</tr>
<tr>
<td>Name</td>
<td>Password</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set password for WLAN settings.
If the password is shorter than 63 bytes, all remaining bytes after the
password should be set to zeros.</p>
<p>For EAP-PEAP authentication, the maximum length of password is 32
bytes. The real password has to be &lt;= 32 bytes, all bytes after the
desired password must be set to zeroes.</p>
<p>For security, the Get request for this property will always return a
value with 63 zeroes, so you can only set the password and not get
it.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>63</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>63</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 674 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040110D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C200 |

Table 675 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104820CD101 820400000000 84820059D101 81072B06010401F609 850101 8949E247E245E143E141C23F00000000 |

Table 676 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040112D111 8459D111 81072B06010401F609 850101 8949E247E245E143E141C23F546F744031386342 |

Table 677 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048212D111 820400000000 84820059D111 81072B06010401F609 850101 8949E247E245E143E141C23F546F744031386342 |

##