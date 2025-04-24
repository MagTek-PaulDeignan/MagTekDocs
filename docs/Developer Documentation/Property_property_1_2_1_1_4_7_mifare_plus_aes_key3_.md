---
title: Property 1.2.1.1.4.7 MIFARE Plus AES_Key3.
layout: home
parent: Configuration
nav_order: 67
---

## Property 1.2.1.1.4.7 MIFARE Plus AES_Key3.

---

- [Property 1.2.1.1.4.7 MIFARE Plus AES_Key3.](#property-121147-mifare-plus-aes_key3)

---


Table 643 - Property 1.2.1.1.4.7 MIFARE Plus AES_Key3.

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
<td>1.2.1.1.4.7 / 0x0102010100407</td>
</tr>
<tr>
<td>Name</td>
<td>MIFARE Plus AES_Key3.</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set 16-byte of the AES_Key3 for
MIFARE Plus.</p>
<p>On example of the ASE Key = 000102030405060708090A0B0C0D0E0Fh, the
setting should be 000102030405060708090A0B0C0D0E0F</p>
<p>For security, the Get request for this property will always return
4-MSB of KCV.</p>
<p>This key will be encrypted and stored in KPM.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16</td>
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
<td>00000000 00000000 00000000 00000000</td>
</tr>
</tbody>
</table>

Table 644 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 C7 00 |

Table 645 - Get Response Example

| Example (Hex) |
|----|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406C704763CBCDE |

Table 646 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C7 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

Table 647 - Set Response Example

| Example (Hex) |
|----|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412C710000102030405060708090A0B0C0D0E0F |

##