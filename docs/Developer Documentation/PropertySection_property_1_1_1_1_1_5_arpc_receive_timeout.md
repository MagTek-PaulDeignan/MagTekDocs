---
title: Property 1.1.1.1.1.5 ARPC Receive Timeout
layout: home
parent: Configuration
nav_order: 7
---

## Property 1.1.1.1.1.5 ARPC Receive Timeout

Table 364 - Property 1.1.1.1.1.5 ARPC Receive Timeout

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
<td>1.1.1.1.1.5 / 0x010101010105</td>
</tr>
<tr>
<td>Name</td>
<td>ARPC Receive Timeout</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine how long to wait for the
host to send <strong>Command 0x1004 - Resume Transaction</strong> with
ARPC data before it times out and continues a transaction the host
started with <strong>Command 0x1001 - Start Transaction</strong>.</td>
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
<td><p>0x00 = Infinite timeout</p>
<p>0x01..0xFE = Timeout in seconds</p>
<p>0xFF = Use Transaction Timeout parameter in <strong>Command 0x1001 -
Start Transaction</strong></p></td>
</tr>
<tr>
<td>Default</td>
<td>0xFF</td>
</tr>
</tbody>
</table>

Table 365 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 C500 |

Table 366 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 10 D1 01 85 01 01 87 04 01 01 01 01 89 03 C5 01 FF |

Table 367 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870401010101 8903 C501FF |

Table 368 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 01 01 01 01 89 03 C5 01 FF |

##