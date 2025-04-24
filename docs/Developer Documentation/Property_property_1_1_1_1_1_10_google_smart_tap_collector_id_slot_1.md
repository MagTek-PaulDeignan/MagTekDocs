---
title: Property 1.1.1.1.1.10 Google Smart Tap Collector ID Slot 1
layout: home
parent: Configuration
nav_order: 16
---

## Property 1.1.1.1.1.10 Google Smart Tap Collector ID Slot 1

---

- [Property 1.1.1.1.1.10 Google Smart Tap Collector ID Slot 1](#property-1111110-google-smart-tap-collector-id-slot-1)

---


| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.10 / 0x010101010110 |
| Name | Google Smart Tap Collector ID Slot 1 |
| Description | The device uses this property for Google Smart Tap processing to configure the device’s supported Collector ID and Service Types. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 25 |
| Data Type | Binary |
| Valid Values | 00 or see **Table 375 - VAS Merchant ID and URL Types** |
| Default | 0x00 |

Table 410 - Property 1.1.1.1.1.10 Google Smart Tap Collector ID Slot 1

Table 411 - Google Smart Tap Collector ID and Service Types

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 29%" />
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th>Len</th>
<th>Value / Description</th>
<th>Typ</th>
<th>Req</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td>DF7C</td>
<td>0x08</td>
<td>GWST Collector ID</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>DF7D</td>
<td>Var up to 0x0E</td>
<td><p>GWST Service Types</p>
<p>0x00 = All services</p>
<p>0x01 = All services except PPSE</p>
<p>0x02 = PPSE</p>
<p>0x03 = Loyalty</p>
<p>0x04 = Offer</p>
<p>0x05 = Gift card</p>
<p>0x06 = Private label card</p>
<p>0x07 = Event ticket</p>
<p>0x08 = Flight</p>
<p>0x09 = Transit</p>
<p>0x10 = Cloud-based wallet</p>
<p>0x11 = Mobil marketing platform</p>
<p>0x12 = Generic</p>
<p>0x13 = Generic private pass</p>
<p>0x40 = Wallet customer</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
</tbody>
</table>

Table 412 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 D000 |

Table 413 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 1E D1 01 85 01 01 87 04 01 01 01 01 89 11 D0 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

Table 414 - Set Request Example

| Example (Hex) |
|----|
| AA00 81048255D111 8427 D111 8107 2B06010401F609 8501 01 8704 01010101 8911 D00F DF7C083230313830363038DF7D0100 |

Table 415 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 2 7D 11 18 10 7 2B 06 01 04 01 F6 09 85 01 01 87 04 01 01 01 01 89 11 D0 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

##