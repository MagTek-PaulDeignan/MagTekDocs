---
title: Property 1.2.1.1.1.2 Application Selection Behavior (Contactless Only)
layout: home
parent: Configuration
nav_order: 56
---

## Property 1.2.1.1.1.2 Application Selection Behavior (Contactless Only)

---

- [Property 1.2.1.1.1.2 Application Selection Behavior (Contactless Only)](#property-121112-application-selection-behavior-contactless-only)

---


Table 588 - Property 1.2.1.1.1.2 Application Selection Behavior
(Contactless Only)Application Selection Behavior

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
<td>1.2.1.1.1.2 / 0x010201010102</td>
</tr>
<tr>
<td>Name</td>
<td>Application Selection Behavior</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to set the device’s application
selection behavior for payment brand selection.</td>
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
<td><p>0x00 –Card Preference.</p>
<p>The device automatically chooses the application that is mutually
supported by the card and the terminal, based on the priority order
specified by the card. This is the default and is standard EMV
transaction flow behavior.</p>
<p>0x01 – Reserved</p>
<p>0x02 – Reserved</p>
<p>0x03 – Enhanced Prompt Cardholder.</p>
<p>The device sends the host <strong>Notification 0x1803 – 02 02 00
00</strong> (Display Cardholder, Data Attached, Reserved) to request
that the cardholder select from a list of available applications. Each
application may include additional tags such as - priority indicator,
Issuer Country Code and Issuer Identification Number. After the
cardholder selects an application, the host passes the selection to the
device using <strong>Command 0x1802 - Report Cardholder
Selection</strong> to device to return the cardholder’s selection to the
device.</p>
<p>Note that if the device is configured to use this option, the
cardholder must hold the card or contactless payment device in contact
with the device for until cardholder application selection is complete,
otherwise the device will report the transaction failed. For this
reason, MagTek does not recommend using this setting.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00 – Card Preference</td>
</tr>
</tbody>
</table>

Table 589 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02010101 8902 C200 |

Table 590 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 10 D1 01 85 01 01 87 04 02 01 01 01 89 03 C2 01 00 |

Table 591 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870402010101 8903 C20103 |

Table 592 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 02 01 01 01 89 03 C2 01 03 |

##