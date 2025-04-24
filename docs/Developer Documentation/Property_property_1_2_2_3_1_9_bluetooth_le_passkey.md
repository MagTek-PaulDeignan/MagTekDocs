---
title: Property 1.2.2.3.1.9 Bluetooth® LE Passkey
layout: home
parent: Configuration
nav_order: 112
---

## Property 1.2.2.3.1.9 Bluetooth® LE Passkey

---

- [Property 1.2.2.3.1.9 Bluetooth® LE Passkey](#property-122319-bluetooth®-le-passkey)

---


Table 856 - Property 1.2.2.3.1.9 Bluetooth® LE Passkey

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
<td>1.2.2.3.1.9 / 0x010202030109</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Passkey</td>
</tr>
<tr>
<td>Description</td>
<td><p>This six-byte property contains the device’s Bluetooth® passkey
as a six-character with valid value for each character between ‘0’ and
‘9’</p>
<p>After the host changes this property, the device must be reset before
the changes will take effect.</p>
<p>For security, the Get request for this property will always return a
length of zero and no value, so you can only set the passkey and not get
it.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>6</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>6</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>'000000' - '999999'</td>
</tr>
<tr>
<td>Default</td>
<td>'000000'</td>
</tr>
</tbody>
</table>

Table 857 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102C900 |

Table 858 - Get Response Example

| Example (Hex) |
|----|
| AA0081048232D1018204000000008482001AD10181072B06010401F609850101890AE208E206E304E102C900 |

Table 859 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D1118420D11181072B06010401F6098501018910E20EE20CE30AE108C906303132333435 |

Table 860 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D11182040000000084820020D11181072B06010401F6098501018910E20EE20CE30AE108C906303132333435 |

##