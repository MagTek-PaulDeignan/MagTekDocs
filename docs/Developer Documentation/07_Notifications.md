---
title: Notifications
layout: home
parent: DynaFlex Family Programmer's Manual
nav_order: 7
---
## Notifications

This section provides definitions and practical information about
**Notification Message**s, which follow the format described in section
**3.2.2.3**. To find documentation about a specific notification:

1)  Use the **Notification Source** byte in the message to find the
    Notification Source subsection below. For example, Notification
    Source **0x01 Transaction** leads to subsection **7.1 Notification
    Source 0x01nn - Notifications from Transactions**.

2)  Within that subsection, use the **Notification Source** byte plus
    the **Notification Type** byte in the message to find the
    Notification subsection. For example, Notification Source **0x01
    Transaction** plus Notification Type **0x01 Information Update**
    leads to **Notification 0x0101 - Transaction Information Update**.

3)  Within that subsection, use the four bytes of **Notification Detail
    Code** in the message to look up the notification in the
    **Notification Detail Code** table. For example, **0x07080302**
    leads to a row in **Table 297** that provides practical information
    about what event led to the notification, and how to interpret the
    Notification Payload.

### Notification Source 0x01nn - Notifications from Transactions

#### Notification 0x0101 - Transaction Information Update

This notification reports information about progress and state changes
that occur during a transaction.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 297**, to indicate:

- The **Payment Technology** (PT) involved

- The **Reason** (Rsn) for the notification

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

Table 297 - Notification Detail Codes

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th>PT</th>
<th>Rsn</th>
<th>Det</th>
<th>Ext</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5"><p>Payment Technology <strong>0x07 Manual Card Entry
(MCE)</strong> contains transaction notification detail codes involving
manual card entry (MCE Only).</p>
<ul>
<li><p>Reason 0x01 = Card Event</p></li>
<li><p>Reason 0x08 = Data Update</p></li>
<li><p>Reason 0x10 = State Update</p></li>
</ul></td>
</tr>
<tr>
<td>07</td>
<td>01</td>
<td>01</td>
<td>00</td>
<td>Manual Card Entry, Card Event, Data Entered, Reserved (MCE
Only)</td>
</tr>
<tr>
<td>07</td>
<td>08</td>
<td>02</td>
<td>02</td>
<td><p>Manual Card Entry, Data Update, ARQC Update (Quick Chip), Data
Attached</p>
<p>In this case, the device includes additional data, defined in
<strong>Table 298</strong>, in the <strong>Notification Payload</strong>
portion of the <strong>Notification Message</strong> (MCE
Only).</p></td>
</tr>
<tr>
<td>07</td>
<td>08</td>
<td>03</td>
<td>02</td>
<td><p>Manual Card Entry, Data Update, Batch Data, Data Attached</p>
<p>In this case, the device includes additional data, defined in
<strong>Table 298</strong>, in the <strong>Notification Payload</strong>
portion of the <strong>Notification Message</strong> (MCE
Only).</p></td>
</tr>
<tr>
<td colspan="5"><p>Payment Technology <strong>0x08 Magnetic Stripe
Reader (MSR)</strong> contains transaction notification detail codes
involving magnetic stripe cards (MSR Only).</p>
<ul>
<li><p>Reason 0x01 = Card Event</p></li>
<li><p>Reason 0x08 = Data Update</p></li>
<li><p>Reason 0x10 = State Update</p></li>
</ul></td>
</tr>
<tr>
<td>08</td>
<td>01</td>
<td>01</td>
<td>00</td>
<td>MSR, Card Event, Swiped, Reserved (MSR Only)</td>
</tr>
<tr>
<td>08</td>
<td>01</td>
<td>02</td>
<td>00</td>
<td>MSR, Card Event, Inserted, Reserved (MSR Only)</td>
</tr>
<tr>
<td>08</td>
<td>01</td>
<td>03</td>
<td>00</td>
<td>MSR, Card Event, Removed, Reserved (MSR Only)</td>
</tr>
<tr>
<td>08</td>
<td>01</td>
<td>04</td>
<td>00</td>
<td>MSR, Card Event, Detected, Reserved</td>
</tr>
<tr>
<td>08</td>
<td>08</td>
<td>02</td>
<td>02</td>
<td><p>MSR, Data Update, ARQC Update (Quick Chip), Data Attached</p>
<p>In this case, the device includes additional data, defined in
<strong>Table 298</strong>, in the <strong>Notification Payload</strong>
portion of the <strong>Notification Message</strong> (MSR
Only).</p></td>
</tr>
<tr>
<td>08</td>
<td>08</td>
<td>03</td>
<td>02</td>
<td><p>MSR, Data Update, Batch Data, Data Attached</p>
<p>In this case, the device includes additional data, defined in
<strong>Table 298</strong>, in the <strong>Notification Payload</strong>
portion of the <strong>Notification Message</strong> (MSR
Only).</p></td>
</tr>
<tr>
<td colspan="5"><p>Payment Technology <strong>0x10 EMV Contact</strong>
contains transaction notification detail codes involving contact chip
cards (EMV Contact Only).</p>
<ul>
<li><p>Reason 0x01 = Card Event</p></li>
<li><p>Reason 0x02 = Online PIN Event</p></li>
<li><p>Reason 0x08 = Data Update</p></li>
<li><p>Reason 0x10 = State Update</p></li>
</ul></td>
</tr>
<tr>
<td>10</td>
<td>01</td>
<td>02</td>
<td>00</td>
<td>EMV Contact, Card Event, Inserted, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td>10</td>
<td>01</td>
<td>03</td>
<td>00</td>
<td>EMV Contact, Card Event, Removed, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td>10</td>
<td>01</td>
<td>04</td>
<td>00</td>
<td>EMV Contact, Card Event, Detected, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td>10</td>
<td>02</td>
<td>06</td>
<td>01</td>
<td>EMV Contact, Online PIN Event, PIN Entry, PIN Pad Error (EMV Contact
Only)</td>
</tr>
<tr>
<td>10</td>
<td>02</td>
<td>06</td>
<td>02</td>
<td>EMV Contact, Online PIN Event, PIN Entry, PIN Block Encryption Error
(EMV Contact Only)</td>
</tr>
<tr>
<td>10</td>
<td>08</td>
<td>02</td>
<td>02</td>
<td><p>EMV Contact, Data Update, ARQC Update (Quick Chip), Data
Attached</p>
<p>In this case, the device includes additional data, defined in
<strong>Table 298</strong>, in the <strong>Notification Payload</strong>
portion of the <strong>Notification Message</strong> (EMV Contact
Only).</p></td>
</tr>
<tr>
<td>10</td>
<td>08</td>
<td>03</td>
<td>02</td>
<td><p>EMV Contact, Data Update, Batch Data, Data Attached</p>
<p>In this case, the device includes additional data, defined in
<strong>Table 298</strong>, in the <strong>Notification Payload</strong>
portion of the <strong>Notification Message</strong> (EMV Contact
Only).</p></td>
</tr>
<tr>
<td colspan="5"><p>Payment Technology <strong>0x20 EMV
Contactless</strong> contains transaction notification detail codes
involving contactless cards and contactless payment devices.</p>
<ul>
<li><p>Reason 0x01 = Card Event</p></li>
<li><p>Reason 0x02 = Online PIN Event</p></li>
<li><p>Reason 0x08 = Data Update</p></li>
<li><p>Reason 0x10 = State Update</p></li>
</ul></td>
</tr>
<tr>
<td>00</td>
<td>10</td>
<td>01</td>
<td>00</td>
<td>None, State Update, Transaction Started by Device, Legacy EMV Flow
(Touch Only)</td>
</tr>
<tr>
<td>00</td>
<td>10</td>
<td>01</td>
<td>01</td>
<td>None, State Update, Transaction Started by Device, Quick Chip Flow
(Touch Only)</td>
</tr>
<tr>
<td>00</td>
<td>10</td>
<td>02</td>
<td>00</td>
<td>None, State Update, Transaction Canceled, Reserved (Touch Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>03</td>
<td>00</td>
<td>EMV Contactless, Card Event, Removed, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>04</td>
<td>00</td>
<td>EMV Contactless, Card Event, Detected, EMV (EMV Contactless
Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>04</td>
<td>01</td>
<td>EMV Contactless, Card Event, Detected, NFC/MIFARE Ultralight (EMV
Contactless Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>04</td>
<td>02</td>
<td>EMV Contactless, Card Event, Detected, MIFARE Classic 1K (EMV
Contactless Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>04</td>
<td>03</td>
<td>EMV Contactless, Card Event, Detected, MIFARE Classic 4K (EMV
Contactless Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>04</td>
<td>04</td>
<td>EMV Contactless, Card Event, Detected, MIFARE DESFire Light (EMV
Contactless Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>04</td>
<td>05</td>
<td>EMV Contactless, Card Event, Detected, MIFARE MINI® (EMV Contactless
Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>04</td>
<td>06</td>
<td>EMV Contactless, Card Event, Detected, MIFARE Plus EV1 (EMV
Contactless Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>04</td>
<td>07</td>
<td>EMV Contactless, Card Event, Detected, MIFARE Plus EV2 (EMV
Contactless Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>04</td>
<td>08</td>
<td>EMV Contactless, Card Event, Detected, MIFARE Plus SE (EMV
Contactless Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>04</td>
<td>09</td>
<td>EMV Contactless, Card Event, Detected, MIFARE Plus X (EMV
Contactless Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>04</td>
<td>0A</td>
<td>EMV Contactless, Card Event, Detected, MIFARE DESFire EV1 (EMV
Contactless Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>04</td>
<td>0B</td>
<td>EMV Contactless, Card Event, Detected, MIFARE DESFire EV2 (EMV
Contactless Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>04</td>
<td>0C</td>
<td>EMV Contactless, Card Event, Detected, MIFARE DESFire EV3 (EMV
Contactless Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>05</td>
<td>00</td>
<td>EMV Contactless, Card Event, Collision, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>10</td>
<td>02</td>
<td><p>EMV Contactless, Card Event, Apple VAS Error, Data Attached</p>
<p>In this case, the device includes additional data, defined in
<strong>Table 301</strong> – <strong>VAS Error Report</strong>, in the
<strong>Notification Payload</strong> portion of the
<strong>Notification Message</strong> (Apple VAS Only).</p></td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>20</td>
<td>02</td>
<td><p>EMV Contactless, Card Event, Google Smart Tap Error, Data
Attached</p>
<p>In this case, the device includes additional data, defined in
<strong>Table 301</strong> – <strong>VAS</strong> <strong>Error
Report</strong>, in the <strong>Notification Payload</strong> portion of
the <strong>Notification Message</strong> (Google Smart Tap
Only).</p></td>
</tr>
<tr>
<td>20</td>
<td>02</td>
<td>06</td>
<td>01</td>
<td>EMV Contactless, Online PIN Event, PIN Entry, PIN Pad Error (EMV
Contactless Only)</td>
</tr>
<tr>
<td>20</td>
<td>02</td>
<td>06</td>
<td>02</td>
<td>EMV Contactless, Online PIN Event, PIN Block Encryption Error (EMV
Contactless Only)</td>
</tr>
<tr>
<td>20</td>
<td>08</td>
<td>02</td>
<td>02</td>
<td><p>EMV Contactless, Data Update, ARQC Update (Quick Chip), Data
Attached</p>
<p>In this case, the device includes additional data, defined in
<strong>Table 298</strong>, in the <strong>Notification Payload</strong>
portion of the <strong>Notification Message</strong> (EMV Contactless
Only).</p></td>
</tr>
<tr>
<td>20</td>
<td>08</td>
<td>03</td>
<td>02</td>
<td><p>EMV Contactless, Data Update, Batch data, Data attached</p>
<p>In this case, the device includes additional data, defined in
<strong>Table 298</strong>, in the <strong>Notification Payload</strong>
portion of the <strong>Notification Message</strong> (EMV Contactless
Only)</p></td>
</tr>
<tr>
<td>20</td>
<td>08</td>
<td>04</td>
<td>02</td>
<td><p>EMV Contactless, Data Update, NFC UID data, Data attached</p>
<p>In this case, the device includes additional data, defined in
<strong>Table 298</strong>, in the <strong>Notification Payload</strong>
portion of the <strong>Notification Message</strong> (EMV Contactless
Only)</p></td>
</tr>
<tr>
<td>20</td>
<td>08</td>
<td>07</td>
<td>02</td>
<td><p>EMV Contactless, Data Update, GPO Response, Data Attached</p>
<p>In this case, the device includes additional data, defined in
<strong>Table 298</strong>, in the <strong>Notification Payload</strong>
portion of the <strong>Notification Message</strong> (EMV Contactless
Only)</p></td>
</tr>
<tr>
<td colspan="5"><p>Payment Technology <strong>0x30 Barcode
Reader</strong> contains transaction notification detail codes involving
barcodes (BCR Only).</p>
<ul>
<li><p>Reason 0x01 = Barcode Event</p></li>
</ul></td>
</tr>
<tr>
<td>30</td>
<td>01</td>
<td>01</td>
<td>00</td>
<td><p>(BCR Only)</p>
<p>Barcode Reader, Barcode Event, Read, Reserved</p></td>
</tr>
<tr>
<td>30</td>
<td>08</td>
<td>00</td>
<td>02</td>
<td><p>Barcode Reader, Barcode Update, Type, Data Attached</p>
<ul>
<li><p>Type 0x00 = Unknown</p></li>
<li><p>Type 0x01 = MagTek</p></li>
<li><p>Type 0x02 = EMV</p></li>
</ul>
<p>The barcode reader has successfully read a barcode. In this case, the
device includes barcode data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
If the data is encrypted, the data is in the format described in
<strong>Table 341</strong>. Data that is not encrypted is in the format
described in <strong>Table 342</strong></p>
<p>(BCR Only)</p>
<p>Barcode Reader, Barcode Event, MagTek Blob Type, Data Attached</p>
<p>In this case, the device includes additional data, defined in
<strong>Table 298</strong>, in the <strong>Notification Payload</strong>
portion of the <strong>Notification Message</strong>.</p></td>
</tr>
</tbody>
</table>

**Table 298 - Notification Payload for Data Update, ARQC Update (Quick
Chip), Data Attached**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 5%" />
<col style="width: 60%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
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
<td colspan="6">Beginning of <strong>Notification Message</strong> found
on page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
<tr>
<td colspan="6">0101 = DynaPro Format Transaction Data</td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td>Transaction Data</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(v)</td>
<td><p><strong>EMV ARQC Type</strong> data blob, if the notification is
an ARQC Update (Quick Chip) notification. (MCE Only) If the notification
is for manual card entry, the data blob does not contain Track 3 Data or
MagnePrint Data.</p>
<p><strong>EMV Batch Data Type</strong> data blob, if the notification
is a Batch Data notification. (MCE Only) If the notification is for
manual card entry, the data blob does not contain Track 3 Data or
MagnePrint Data.</p>
<p>Decoded raw barcode data, if the notification is a Barcode event
notification. If the barcode data is Base64 encoded, the device sends
the decoded version in binary format.</p>
<p><strong>NFC UID Type</strong> reports the unique ID from the NFC tag
(EMV Contactless Only)</p>
<p><a href="#gpo-response-type-emv-contactless-only"><strong>GPO
Response Type</strong></a> <strong>reports the card’s GPO Response (EMV
Contactless Only)</strong></p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of <strong>Notification Message</strong> found on
page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
</tbody>
</table>

Table 299 - Notification Payload for Barcode Reader, Barcode Event, Type
(Encrypted Data Attached)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 59%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 11%" />
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
<td colspan="6">Beginning of <strong>Notification Message</strong> found
on page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
<tr>
<td colspan="6">1805 = User Interface Operation Complete</td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td>Notification Payload</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF59</td>
<td>var</td>
<td><p>Encrypted Data Primitive</p>
<p>Decrypt the value of this TLV data object using the algorithm and
variant specified in the <strong>Encrypted Data KSN</strong> parameter
and the <strong>Encrypted Data Encryption Type</strong> parameter to
read its contents. The format of the decrypted data is shown in
<strong>Table 300</strong>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF50</td>
<td>var</td>
<td>Encrypted Data KSN</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF51</td>
<td>01</td>
<td><p>Encrypted Data Encryption Type</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of <strong>Notification Message</strong> found on
page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
</tbody>
</table>

Table 300 - Notification Payload for Barcode Reader, Barcode Event,
Type, Data Attached (Unencrypted Data)

| Tag   | Len | Value / Description    | Typ | Req | Default |
|-------|-----|------------------------|-----|-----|---------|
| FC    | var | Barcode Data Container | T   | R   |         |
| /DF74 | var | Barcode Data           | B   | O   |         |

Table 301 – VAS Error Report

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 5%" />
<col style="width: 57%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
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
<td>FC</td>
<td>var</td>
<td>VAS Error Container</td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF25</td>
<td>var</td>
<td>Device Serial Number (IFD Serial Number)</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DF75</td>
<td>var</td>
<td><p>VAS Error Report</p>
<p>Byte 1 = SW1 returned by the Apple or Android device</p>
<p>Byte 2 = SW2 returned by the Apple or Android device</p>
<p>Byte 3 = Slot Number</p>
<p>Byte 4 = Where in the VAS command sequence the error occurred.</p>
<ul>
<li><p>0x00 = Select OSE Error</p></li>
<li><p>0x01 = Get VAS Data Error (Apple only)</p></li>
<li><p>0x02 = Select Smart Tap Error (Google only)</p></li>
<li><p>0x03 = Negotiate Secure Session Error (Google only)</p></li>
<li><p>0x04 = Get Select Smart Tap Error (Google only)</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
</tbody>
</table>

Table 302 - Notification Example

| Example (Hex) |
|----|
| AA 00 81 04 83 00 01 01 82 04 10 08 02 02 84 82 01 F8 01 01 84 82 01 F2 01 E9 F9 82 01 E5 DF DF 54 0A 00 00 00 00 00 00 00 00 00 00 DF DF 55 01 82 DF DF 25 0F 42 34 44 42 38 31 37 31 31 31 39 31 39 41 41 FA 82 01 BB 70 82 01 B7 DF DF 53 01 00 5F 20 12 47 55 53 54 49 4E 2F 53 54 45 50 48 41 4E 49 45 20 4D 5F 30 02 02 01 DF DF 4D 25 3B 35 33 32 32 30 30 30 30 36 30 30 30 31 36 37 34 3D 31 38 30 39 32 30 31 30 30 30 30 30 30 30 30 30 30 30 3F DF DF 52 01 05 F8 82 01 66 DF DF 59 82 01 48 36 69 98 57 4C 81 08 66 28 B6 1F DD 69 B1 C3 43 F7 BA 98 B2 5A 92 53 5F DA 63 6D DA 44 95 F1 15 2D 01 07 9A 4C EB 28 0B 30 5C 21 B2 39 ED E7 EE B6 1A 79 43 56 2E 26 1E C9 87 86 19 68 FA EB 4A 2B BD F5 5D 54 6F C4 67 97 FF 42 2C D6 CF 36 03 48 58 A4 23 9B 51 03 5C 32 0B DC 5E 4E E5 95 1B B5 C5 18 E7 33 0B D2 FE 8D E8 5C 47 4D 3C 16 79 42 48 1D CD 83 D5 58 64 48 23 17 F3 29 A7 F1 F1 75 F4 B9 C6 45 F3 02 28 1C 90 C7 83 B9 49 AF 56 BD 76 73 E7 45 7D 25 C5 77 3F C7 9A 1B ED 52 0A 05 54 15 B7 9A 2A 59 C1 67 6D E2 8C 02 8B 97 64 96 5D 4C F8 31 A2 20 75 12 8D 99 C1 A2 DF AB 55 0A 62 24 79 CF A8 51 3D AE 84 91 A5 80 19 9F BC 75 B0 F9 56 5E BA 57 A3 B1 61 AA 84 43 F0 D8 E6 44 C1 FA 51 0E 0A B0 F7 F2 61 57 5B 86 7E AB DC 49 00 87 A0 3B 69 5F C1 45 C4 10 9A A8 5F B6 30 59 2C 25 FA 15 A5 44 83 24 96 3D 5A 03 50 36 02 EC 6B 15 7C 8D CC 66 BF B7 F4 CF 4C 6D 67 75 87 B9 4E D4 08 76 25 F8 B8 EF BF A8 A0 72 F9 81 AB FF 49 84 E7 BC 8F C5 DD A0 86 B2 74 DD 59 8A B2 83 5D DD CC 0C 30 01 96 DF DF 56 0A 90 10 01 0B 4D B8 17 00 00 03 DF DF 57 01 80 DF DF 58 01 05 00 00 00 00 00 00 00 |

#### Notification 0x0103 - Transaction Host Action Request (MAGTEK INTERNAL ONLY FOR NOW)

This notification requests the host take action to support a transaction
in progress.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 303**, to indicate:

- The **Payment Technology**, which is always set to 0x00.

- The **Reason** (Rsn) for the notification

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

Table 303 - Notification Detail Codes

| PT | Rsn | Det | Ext | Meaning |
|----|----|----|----|----|
| Payment Technology **0x00 All** contains all transaction host request detail codes. |  |  |  |  |
|  |  |  |  |  |

**Notification Payload** described in section **3.2.2.3 Notification
Message** is only included in some cases, described in **Table 297**.
When a Notification Payload is included, it follows the structure shown
in **Table 304**.

Table 304 - Notification Payload for Transaction Host Action Request

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |
| 0103 = **Notification 0x0103 - Transaction Host Action Request (MAGTEK INTERNAL ONLY FOR NOW)** |  |  |  |  |  |
|  |  |  |  |  |  |
| End of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |

Table 305 - Notification Example for Display Message Request
Notifications (No Display Only)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Display Message Request to show PROCESSING</p>
<p>AA 00</p>
<p>81 04 83 00 01 03 // Notification source/type = 0x0103</p>
<p>82 04</p>
<p>00</p>
<p>01 // 0x01=Display Message Request</p>
<p>01 // 0x01=Data Attached</p>
<p>00</p>
<p>84 82 00 12 // Payload, 18 bytes (using two-byte Length)</p>
<p>81 01 01 // Clear Screen is enabled</p>
<p>82 82 00 0B // Messages, 11 bytes (using two-byte Length)</p>
<p>50 52 4F 43 45 53 53 49 4E 47 00 // “PROCESSING” (line terminator is
0x00)</p></td>
</tr>
</tbody>
</table>

Table 306 - Notification Example for Cardholder Selection Request (No
Display Only)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Cardholder Selection Request to show:</p>
<p>APPLICATION SELECT</p>
<p>1 - VISA CREDIT</p>
<p>2 - VISA DEBIT</p>
<p>3 - VISA ELECTRON</p>
<p>AA 00</p>
<p>81 04 83 00 01 03 // Notification source/type = 0x0103</p>
<p>82 04</p>
<p>00</p>
<p>02 // 0x02=Cardholder Selection Request</p>
<p>00</p>
<p>00 // Timeout, TT=0x00</p>
<p>84 82 00 4B // Payload, 75 bytes (using two-byte Length)</p>
<p>81 01 01 // Clear Display</p>
<p>82 82 00 44 // Messages, 68 bytes (using two-byte Length)</p>
<p>41 50 50 4C 49 43 41 54 49 4F 4E 20 53 45 4C 45 43 54 0A</p>
<p>31 20 2D 20 56 49 53 41 20 43 52 45 44 49 54 0A</p>
<p>32 20 2D 20 56 49 53 41 20 44 45 42 49 54 0A</p>
<p>33 20 2D 20 56 49 53 41 20 45 4C 45 43 54 52 4F 4E 00</p></td>
</tr>
</tbody>
</table>

Table 307 - Notification Example for Online PIN Request (MAGTEK INTERNAL
ONLY FOR NOW, No Display Only)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>(MAGTEK INTERNAL ONLY FOR NOW)</p>
<p>Online PIN Request to show:</p>
<p>VISA DEBIT</p>
<p>100.00</p>
<p>AA 00 81 04 83 00 01 05 82 04 00 03 00 00 84 16 9F 12 0A 56 49 53 41
20 44 45 42 49 54 9F 02 06 00 00 00 01 00 00</p></td>
</tr>
</tbody>
</table>

#### Notification 0x0104 - Transaction Callback (MAGTEK INTERNAL ONLY FOR NOW)

This notification fulfills callback subscriptions the host has
requested.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 308**, to indicate:

- The …

- The …

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

Table 308 - Notification Detail Codes

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th>??</th>
<th>??</th>
<th>Det</th>
<th>Ext</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5"><p>xxx <strong>0x00 None</strong> contains transaction
notification detail codes xxx</p>
<ul>
<li><p>xxx 0x01 = xxx</p></li>
</ul></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="5"><p>xxx <strong>0x00 None</strong> contains transaction
notification detail codes xxx</p>
<ul>
<li><p>xxx 0x01 = xxx</p></li>
</ul></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="5"><p>xxx <strong>0x00 None</strong> contains transaction
notification detail codes xxx</p>
<ul>
<li><p>xxx 0x01 = xxx</p></li>
</ul></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

**Notification Payload** described in section **3.2.2.3 Notification
Message** is only included in some cases, described in **Table 297**.
When a Notification Payload is included, it follows the structure shown
in **Table 309**.

Table 309 - Notification Payload

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |
| 0103 = **Notification 0x0104 - Transaction Callback (MAGTEK INTERNAL ONLY FOR NOW)** |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
| End of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |

Table 310 - Notification Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 83 00 01 05 82 04 20 00 00 00 |

#### Notification 0x0105 - Transaction Operation Complete

This notification reports the final result of a transaction the host
initiated using **Command 0x1001 - Start Transaction**.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 311**, to indicate:

- The **Payment Technology** (PT) involved

- The **Reason** (Rsn) for the notification

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

Table 311 - Notification Detail Codes

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 1%" />
<col style="width: 4%" />
<col style="width: 1%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr>
<th colspan="2">PT</th>
<th colspan="2">Res</th>
<th>Det</th>
<th>Ext</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="7"><p>Payment Technology <strong>0x00 None</strong>
contains transaction notification detail codes that are not specific to
a particular payment technology.</p>
<ul>
<li><p>0x00 = Reserved</p></li>
<li><p>0x01 = Timeout/No Cards Detected</p></li>
<li><p>0x02 = Kernel Outcome</p></li>
<li><p>0x03 = Transaction Terminated</p></li>
<li><p>0x04 = Transaction Completed</p></li>
</ul></td>
</tr>
<tr>
<td>00</td>
<td colspan="2">01</td>
<td colspan="2">00</td>
<td>00</td>
<td>None, Timeout/No Cards Detected, Transaction Timed Out,
Reserved</td>
</tr>
<tr>
<td>00</td>
<td colspan="2">03</td>
<td colspan="2">01</td>
<td>00</td>
<td>None, Transaction Terminated, Transaction Canceled by Host,
Reserved</td>
</tr>
<tr>
<td>00</td>
<td colspan="2">03</td>
<td colspan="2">02</td>
<td>00</td>
<td>None, Transaction Terminated, Transaction Canceled by User, Reserved
(Display Only)</td>
</tr>
<tr>
<td colspan="7"><p>Payment Technology <strong>0x07 Manual Card
Entry</strong> contains transaction notification detail codes involving
manual card entry (MCE Only).</p>
<ul>
<li><p>0x00 = Reserved</p></li>
<li><p>0x01 = Timeout/No Cards Detected</p></li>
<li><p>0x02 = Kernel Outcome</p></li>
<li><p>0x03 = Transaction Terminated</p></li>
<li><p>0x04 = Transaction Completed</p></li>
</ul></td>
</tr>
<tr>
<td>07</td>
<td colspan="2">03</td>
<td colspan="2">05</td>
<td>00</td>
<td>MCE, Transaction Terminated, Transaction Canceled due to entry
error, Reserved (MCE Only)</td>
</tr>
<tr>
<td>07</td>
<td colspan="2">04</td>
<td colspan="2">00</td>
<td>00</td>
<td>MCE, Transaction Completed, Reserved, Reserved (MCE Only)</td>
</tr>
<tr>
<td colspan="7"><p>Payment Technology <strong>0x08 Magnetic Stripe
Reader (MSR)</strong> contains transaction notification detail codes
involving magnetic stripe cards (MSR Only).</p>
<ul>
<li><p>0x00 = Reserved</p></li>
<li><p>0x01 = Timeout/No Cards Detected</p></li>
<li><p>0x02 = Kernel Outcome</p></li>
<li><p>0x03 = Transaction Terminated</p></li>
<li><p>0x04 = Transaction Completed</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">03</td>
<td>05</td>
<td>00</td>
<td>MSR, Transaction Terminated, Transaction Canceled Due to Card Read
Error, Reserved (MSR Only)</td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>06</td>
<td>00</td>
<td>MSR, Outcome, Approved, Reserved (MSR Only)</td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>06</td>
<td>01</td>
<td><p>MSR, Outcome, Approved, Signature Capture Requested (MSR
Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>06</td>
<td>04</td>
<td>MSR, Outcome, Approved, Signature Capture Available (MSR Only)
(MAGTEK INTERNAL ONLY FOR NOW, not yet implemented)</td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>06</td>
<td>05</td>
<td><p>MSR, Outcome, Approved, Signature Capture Success (MSR Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>06</td>
<td>06</td>
<td><p>MSR, Outcome, Approved, Signature Capture Fail (MSR Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>07</td>
<td>00</td>
<td>MSR, Outcome, Quick Chip Deferred, Reserved (MSR Only)</td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>07</td>
<td>01</td>
<td><p>MSR, Outcome, Quick Chip Deferred, Signature Capture Requested
(MSR Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>07</td>
<td>04</td>
<td>MSR, Outcome, Quick Chip Deferred, Signature Capture Available (MSR
Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet implemented)</td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>07</td>
<td>05</td>
<td><p>MSR, Outcome, Quick Chip Deferred, Signature Capture Success (MSR
Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>07</td>
<td>06</td>
<td><p>MSR, Outcome, Quick Chip Deferred, Signature Capture Fail (MSR
Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>80</td>
<td>00</td>
<td>MSR, Outcome, Declined, Reserved (MSR Only)</td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>80</td>
<td>01</td>
<td><p>MSR, Outcome, Declined, Signature Capture Requested (MSR
Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>80</td>
<td>04</td>
<td>MSR, Outcome, Declined, Signature Capture Available (MSR Only)
(MAGTEK INTERNAL ONLY FOR NOW, not yet implemented)</td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>80</td>
<td>05</td>
<td><p>MSR, Outcome, Declined, Signature Capture Success (MSR Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>80</td>
<td>06</td>
<td><p>MSR, Outcome, Declined, Signature Capture Fail (MSR Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="7"><p>Payment Technology <strong>0x10 EMV Contact</strong>
(“ICC”) contains transaction notification detail codes involving contact
chip cards (EMV Contact Only).</p>
<ul>
<li><p>0x00 = Reserved</p></li>
<li><p>0x01 = Timeout, no cards detected</p></li>
<li><p>0x02 = Kernel Outcome</p></li>
<li><p>0x03 = Transaction Terminated</p></li>
<li><p>0x04 = Transaction Completed</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>08</td>
<td>03</td>
<td>ICC, Kernel Outcome, Failed, MSR Fallback (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>09</td>
<td>03</td>
<td>ICC, Kernel Outcome, Empty Candidate List, MSR Fallback (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>00</td>
<td>00</td>
<td>ICC, Kernel Outcome, None, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>00</td>
<td>02</td>
<td>ICC, Kernel Outcome, None, Technical Fallback (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>0F</td>
<td>02</td>
<td>ICC, Kernel Outcome, End Application, Technical Fallback (EMV
Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>01</td>
<td>00</td>
<td>ICC, Kernel Outcome, Try Another Interface, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>02</td>
<td>00</td>
<td>ICC, Kernel Outcome, Offline Approved, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>02</td>
<td>01</td>
<td><p>ICC, Kernel Outcome, Offline Approved, Signature Capture
Requested (EMV Contact Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>02</td>
<td>04</td>
<td>ICC, Kernel Outcome, Offline Approved, Signature Capture Available
(EMV Contact Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet
implemented)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>02</td>
<td>05</td>
<td><p>ICC, Kernel Outcome, Offline Approved, Signature Capture Success
(EMV Contact Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>02</td>
<td>06</td>
<td><p>ICC, Kernel Outcome, Offline Approved, Signature Capture Fail
(EMV Contact Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>03</td>
<td>00</td>
<td>ICC, Kernel Outcome, Offline Declined, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>04</td>
<td>00</td>
<td>ICC, Kernel Outcome, Offline Failed, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>05</td>
<td>00</td>
<td>ICC, Kernel Outcome, Offline Not Accepted, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>06</td>
<td>00</td>
<td>ICC, Kernel Outcome, Approved, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>06</td>
<td>01</td>
<td><p>ICC, Kernel Outcome, Approved, Signature Capture Requested (EMV
Contact Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>06</td>
<td>04</td>
<td>ICC, Kernel Outcome, Approved, Signature Capture Available (EMV
Contact Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet implemented)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>06</td>
<td>05</td>
<td><p>ICC, Kernel Outcome, Approved, Signature Capture Success (EMV
Contact Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>06</td>
<td>06</td>
<td><p>ICC, Kernel Outcome, Approved, Signature Capture Fail (EMV
Contact Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>07</td>
<td>00</td>
<td>ICC, Kernel Outcome, Quick Chip Deferred, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>07</td>
<td>01</td>
<td><p>ICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Requested (EMV Contact Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>07</td>
<td>04</td>
<td>ICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Available (EMV Contact Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet
implemented)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>07</td>
<td>05</td>
<td><p>ICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Success (EMV Contact Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>07</td>
<td>06</td>
<td><p>ICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Failed (EMV Contact Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>08</td>
<td>00</td>
<td>ICC, Kernel Outcome, Failed, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>09</td>
<td>00</td>
<td>ICC, Kernel Outcome, Not Accepted, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>0A</td>
<td>00</td>
<td>ICC, Kernel Outcome, Transaction Canceled, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>0B</td>
<td>00</td>
<td>ICC, Kernel Outcome, Select Next Not Accepted, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>0C</td>
<td>00</td>
<td>ICC, Kernel Outcome, Select Next Retry, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>0D</td>
<td>00</td>
<td>ICC, Kernel Outcome, Try Again, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>0E</td>
<td>00</td>
<td>ICC, Kernel Outcome, Online Request, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>0F</td>
<td>00</td>
<td>ICC, Kernel Outcome, End Application, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>10</td>
<td>00</td>
<td>ICC, Kernel Outcome, Not EMV Card Pooled, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>80</td>
<td>00</td>
<td>ICC, Kernel Outcome, Declined, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>80</td>
<td>01</td>
<td><p>ICC, Kernel Outcome, Declined, Signature Capture Requested (EMV
Contact Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>80</td>
<td>04</td>
<td>ICC, Kernel Outcome, Declined, Signature Capture Available (EMV
Contact Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet implemented)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>80</td>
<td>05</td>
<td><p>ICC, Kernel Outcome, Declined, Signature Capture Success (EMV
Contact Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>80</td>
<td>06</td>
<td><p>ICC, Kernel Outcome, Declined, Signature Capture Failed (EMV
Contact Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">04</td>
<td>07</td>
<td>00</td>
<td>ICC, Transaction Completed, Declined, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="7"><p>Payment Technology <strong>0x20 EMV
Contactless</strong> (“PICC”) contains transaction notification detail
codes involving contactless cards and contactless payment devices (EMV
Contactless Only).</p>
<ul>
<li><p>0x00 = Reserved</p></li>
<li><p>0x01 = Timeout, no cards detected</p></li>
<li><p>0x02 = Kernel Outcome</p></li>
<li><p>0x03 = Transaction Terminated</p></li>
<li><p>0x04 = Transaction Completed</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>00</td>
<td>00</td>
<td>PICC, Kernel Outcome, None, Reserved (EMV Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>01</td>
<td>00</td>
<td>PICC, Kernel Outcome, Try Another Interface, Reserved (EMV
Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>02</td>
<td>00</td>
<td>PICC, Kernel Outcome, Offline Approved, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>02</td>
<td>01</td>
<td><p>PICC, Kernel Outcome, Offline Approved, Signature Capture
Requested (EMV Contactless Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>02</td>
<td>04</td>
<td>PICC, Kernel Outcome, Offline Approved, Signature Capture Available
(EMV Contactless Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet
implemented)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>02</td>
<td>05</td>
<td><p>PICC, Kernel Outcome, Offline Approved, Signature Capture Success
(EMV Contactless Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>02</td>
<td>06</td>
<td><p>PICC, Kernel Outcome, Offline Approved, Signature Capture Fail
(EMV Contactless Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>03</td>
<td>00</td>
<td>PICC, Kernel Outcome, Offline Declined, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>04</td>
<td>00</td>
<td>PICC, Kernel Outcome, Offline Failed, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>05</td>
<td>00</td>
<td>PICC, Kernel Outcome, Offline Not Accepted, Reserved (EMV
Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>06</td>
<td>00</td>
<td>PICC, Kernel Outcome, Approved, Reserved (EMV Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>06</td>
<td>01</td>
<td><p>PICC, Kernel Outcome, Approved, Signature Capture Requested (EMV
Contactless Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>06</td>
<td>04</td>
<td>PICC, Kernel Outcome, Approved, Signature Capture Available (EMV
Contactless Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet
implemented)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>06</td>
<td>05</td>
<td><p>PICC, Kernel Outcome, Approved, Signature Capture Success (EMV
Contactless Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>06</td>
<td>06</td>
<td><p>PICC, Kernel Outcome, Approved, Signature Capture Fail (EMV
Contactless Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>07</td>
<td>00</td>
<td>PICC, Kernel Outcome, Quick Chip Deferred, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>07</td>
<td>01</td>
<td><p>PICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Requested (EMV Contactless Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>07</td>
<td>04</td>
<td>PICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Available (EMV Contactless Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet
implemented)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>07</td>
<td>05</td>
<td><p>PICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Success (EMV Contactless Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>07</td>
<td>06</td>
<td><p>PICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Failed (EMV Contactless Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>08</td>
<td>00</td>
<td>PICC, Kernel Outcome, Failed, Reserved (EMV Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>09</td>
<td>00</td>
<td>PICC, Kernel Outcome, Not Accepted, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>0A</td>
<td>00</td>
<td>PICC, Kernel Outcome, Transaction Canceled, Reserved (EMV
Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>0B</td>
<td>00</td>
<td>PICC, Kernel Outcome, Select Next Not Accepted, Reserved (EMV
Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>0C</td>
<td>00</td>
<td>PICC, Kernel Outcome, Select Next Retry, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>0D</td>
<td>00</td>
<td>PICC, Kernel Outcome, Try Again, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>0E</td>
<td>00</td>
<td>PICC, Kernel Outcome, Online Request, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>0F</td>
<td>00</td>
<td>PICC, Kernel Outcome, End Application, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>10</td>
<td>00</td>
<td>PICC, Kernel Outcome, Not EMV Card Pooled, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>80</td>
<td>00</td>
<td>PICC, Kernel Outcome, Declined, Reserved (EMV Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>80</td>
<td>01</td>
<td><p>PICC, Kernel Outcome, Declined, Signature Capture Requested (EMV
Contactless Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>80</td>
<td>04</td>
<td>PICC, Kernel Outcome, Declined, Signature Capture Available (EMV
Contactless Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet
implemented)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>80</td>
<td>05</td>
<td><p>PICC, Kernel Outcome, Declined, Signature Capture Success (EMV
Contactless Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>80</td>
<td>06</td>
<td><p>PICC, Kernel Outcome, Declined, Signature Capture Failed (EMV
Contactless Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">04</td>
<td>07</td>
<td>00</td>
<td>PICC, Transaction Completed, Declined, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">05</td>
<td>00</td>
<td>00</td>
<td>PICC, NFC TAG, Tag Removed, Reserved (EMV Contactless Only)</td>
</tr>
</tbody>
</table>

Table 312 - Notification Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 83 00 01 05 82 04 20 00 00 00 |

### Notification Source 0x02nn - Notifications from Banking Functions (Banking Functions Only)

#### Notification 0x0201 - Banking Functions Information Update

This notification reports information about progress and state changes
involving the device’s Banking Functions modules.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 313 - Notification Detail Codes**, to indicate:

- The **Payment Technology** (PT) involved

- The **Reason** (Rsn) for the notification

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

Table 313 - Notification Detail Codes

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th>PT</th>
<th>Rsn</th>
<th>Det</th>
<th>Ext</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5"><p>Payment Technology <strong>0x07 Manual Card Entry
(MCE)</strong> contains transaction notification detail codes involving
manual card entry (MCE Only).</p>
<ul>
<li><p>Reason 0x01 = Card Event</p></li>
<li><p>Reason 0x08 = Data Update</p></li>
<li><p>Reason 0x10 = State Update</p></li>
</ul></td>
</tr>
<tr>
<td>07</td>
<td>01</td>
<td>01</td>
<td>00</td>
<td>Manual Card Entry, Card Event, Data Entered, Reserved</td>
</tr>
<tr>
<td colspan="5"><p>Payment Technology <strong>0x08 Magnetic Stripe
Reader (MSR)</strong> contains transaction notification detail codes
involving magnetic stripe cards (MSR Only).</p>
<ul>
<li><p>Reason 0x01 = Card Event</p></li>
<li><p>Reason 0x08 = Data Update</p></li>
<li><p>Reason 0x10 = State Update</p></li>
</ul></td>
</tr>
<tr>
<td>08</td>
<td>01</td>
<td>01</td>
<td>00</td>
<td>MSR, Card Event, Swiped, Reserved (MSR Only)</td>
</tr>
<tr>
<td>08</td>
<td>01</td>
<td>02</td>
<td>00</td>
<td>MSR, Card Event, Inserted, Reserved (MSR Only)</td>
</tr>
<tr>
<td>08</td>
<td>01</td>
<td>03</td>
<td>00</td>
<td>MSR, Card Event, Removed, Reserved (MSR Only)</td>
</tr>
<tr>
<td>08</td>
<td>01</td>
<td>04</td>
<td>00</td>
<td>MSR, Card Event, Detected, Reserved (MSR Only)</td>
</tr>
<tr>
<td colspan="5"><p>Payment Technology <strong>0x10 EMV Contact</strong>
contains transaction notification detail codes involving contact chip
cards (EMV Contact Only).</p>
<ul>
<li><p>Reason 0x01 = Card Event</p></li>
<li><p>Reason 0x08 = Data Update</p></li>
<li><p>Reason 0x10 = State Update</p></li>
</ul></td>
</tr>
<tr>
<td>10</td>
<td>01</td>
<td>02</td>
<td>00</td>
<td>EMV Contact, Card Event, Inserted, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td>10</td>
<td>01</td>
<td>03</td>
<td>00</td>
<td>EMV Contact, Card Event, Removed, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td>10</td>
<td>01</td>
<td>04</td>
<td>00</td>
<td>EMV Contact, Card Event, Detected, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="5"><p>Payment Technology <strong>0x20 EMV
Contactless</strong> contains transaction notification detail codes
involving contactless cards and contactless payment devices. (EMV
Contactless Only)</p>
<ul>
<li><p>Reason 0x01 = Card Event</p></li>
<li><p>Reason 0x08 = Data Update</p></li>
<li><p>Reason 0x10 = State Update</p></li>
</ul></td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>03</td>
<td>00</td>
<td>EMV Contactless, Card Event, Removed, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>04</td>
<td>00</td>
<td>EMV Contactless, Card Event, Detected, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>05</td>
<td>00</td>
<td>EMV Contactless, Card Event, Collision, Reserved (EMV Contactless
Only)</td>
</tr>
</tbody>
</table>

#### Notification 0x0203 - Banking Functions Host Action Request(MAGTEK INTERNAL ONLY FOR NOW)

This notification requests that the host take action during operations
involving the device’s Banking Functions modules.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 334**, to indicate:

- The **User Interface Module** (UI) involved

- The **Reason** (Rsn) for the notification (UI Event)

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

#### Notification 0x0205 - Banking Functions Operation Complete

This notification reports information about progress and state changes
that occur during interaction with the Banking Functions modules.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 339**, to indicate:

- The **User Interface Module** (UI) involved

- The **Reason** (Rsn) for the notification (UI Event)

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

Table 314 - Notification Detail Codes

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th>UI</th>
<th>Rsn</th>
<th>Det</th>
<th>Ext</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5"><p>Module <strong>0x01 Touchscreen</strong> contains UI
notification detail codes that are specific to the touchscreen module
(Touch Only)</p>
<ul>
<li><p>Reason 0x01 = Signature Capture</p></li>
<li><p>Reason 0x02 = PIN Entry (Banking Functions Only)</p></li>
</ul></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>01</td>
<td>01</td>
<td><p>(Banking Functions Only)</p>
<p>Touchscreen, PIN Entry, Success, Data Attached</p>
<p>In this case, the device includes additional data defined in
<strong>Table 315</strong>, or in <strong>Table 316</strong> if the
device is including account data with PIN data.</p></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>02</td>
<td>01</td>
<td><p>(Banking Functions Only)</p>
<p>Touchscreen, PIN Entry, Operation Failed, Timeout</p></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>02</td>
<td>02</td>
<td><p>(Banking Functions Only)</p>
<p>Touchscreen, PIN Entry, Operation Failed, Hardware Not
Available</p></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>02</td>
<td>03</td>
<td><p>(Banking Functions Only)</p>
<p>Touchscreen, PIN Entry, Operation Failed, Canceled</p></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>02</td>
<td>04</td>
<td><p>(Banking Functions Only)</p>
<p>Touchscreen, PIN Entry, Operation Failed, Error</p></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>02</td>
<td>05</td>
<td><p>(Banking Functions Only)</p>
<p>Touchscreen, PIN Entry, Operation Failed, PIN Verify Failed</p></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>02</td>
<td>06</td>
<td><p>(Banking Functions Only)</p>
<p>Touchscreen, PIN Entry, Operation Failed, Account Data Capture
Failed</p></td>
</tr>
</tbody>
</table>

Table 315 - Notification Payload for Touchscreen, PIN Entry, Success,
Data Attached without Account Data (Banking Functions Only)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 59%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 11%" />
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
<td colspan="6">Beginning of <strong>Notification Message</strong> found
on page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
<tr>
<td colspan="6">0205 = User Interface Operation Complete</td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td>Notification Payload</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/F5</td>
<td>var</td>
<td>Container for Encrypted PIN Data</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//DF71</td>
<td>01</td>
<td><p>PIN Block Format</p>
<ul>
<li><p>0x00 = ISO Format 0</p></li>
<li><p>0x01 = ISO Format 1</p></li>
<li><p>0x03 = ISO Format 3</p></li>
<li><p>0x04 = ISO Format 4</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//99</td>
<td>var</td>
<td><p>Encrypted PIN Block</p>
<p>ISO Formats 0, 1, and 3 are 8 bytes</p>
<p>ISO Format 4 is 16 bytes</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//DFDF41</td>
<td>var</td>
<td>PIN Key Serial Number (KSN)</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//DFDF42</td>
<td>01</td>
<td><p>PIN Encryption Type</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of <strong>Notification Message</strong> found on
page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
</tbody>
</table>

Table 316 - Notification Payload for Touchscreen, PIN Entry, Success,
Data Attached with Account Data (Banking Functions Only)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 59%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 11%" />
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
<td colspan="6">Beginning of <strong>Notification Message</strong> found
on page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
<tr>
<td colspan="6">0205 = User Interface Operation Complete</td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td>Notification Payload</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF59</td>
<td>var</td>
<td><p>Encrypted Data Primitive</p>
<p>Decrypt the value of this TLV data object using the algorithm and
variant specified in the <strong>Encrypted Data KSN</strong> parameter
and the <strong>Encrypted Data Encryption Type</strong> parameter to
read its contents. The format of the decrypted data is shown in
<strong>Table 317</strong>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF56</td>
<td>var</td>
<td>Encrypted Data KSN</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF57</td>
<td>01</td>
<td><p>Encrypted Data Encryption Type</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/F5</td>
<td>var</td>
<td>Container for Encrypted PIN Data</td>
<td>TC</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//DF71</td>
<td>01</td>
<td><p>PIN Block Format</p>
<ul>
<li><p>0x00 = ISO Format 0</p></li>
<li><p>0x01 = ISO Format 1</p></li>
<li><p>0x03 = ISO Format 3</p></li>
<li><p>0x04 = ISO Format 4</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//99</td>
<td>var</td>
<td><p>Encrypted PIN Block</p>
<p>ISO Formats 0, 1, and 3 are 8 bytes</p>
<p>ISO Format 4 is 16 bytes</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//DFDF41</td>
<td>var</td>
<td>PIN KSN</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//DFDF42</td>
<td>01</td>
<td><p>PIN Encryption Type</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of <strong>Notification Message</strong> found on
page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
</tbody>
</table>

Table 317 - Account Data DFDF59 Decrypted Contents (Banking Functions
Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| FC | var | Decrypted Data Container | T | R |  |
| /DF42 | var | MSR Track 2 Clear Text Data | B | O |  |
| /57 | var | Track 2 Equivalent Data | B | O |  |
| /5A | var | Primary Account Number | B | O |  |
| Padding to force DFDF59 plus padding to be a multiple of 8 bytes |  |  |  |  |  |

### Notification Source 0x09nn - Notifications from Firmware Updates

#### Notification 0x0905 - Firmware Update Successful

This notification reports the successful completion of firmware update
operations the host initiated using **Command 0xD801 - Load Firmware
File** and **Command 0xD901 - Commit Firmware from File**. The
**Notification Detail** for those two commands are shown in the table
below.

Table 318 - Notification Detail Codes

| B1  | B2  | B3  | B4  | Meaning                                     |
|-----|-----|-----|-----|---------------------------------------------|
| 08  | 01  | 0A  | 03  | Commit Firmware from File Complete, Success |
| 08  | 01  | 09  | 03  | Load Firmware File Complete, Success        |

#### Notification 0x0906 - Firmware Update Failed

This notification reports the failure of a Firmware Update command the
host initiated using **Command 0xD801 - Load Firmware File** and
**Command 0xD901 - Commit Firmware from File**. The **Notification
Detail** for those two commands are shown in the table below.

Table 319 - Notification Detail Codes

| B1  | B2  | B3  | B4  | Meaning                                    |
|-----|-----|-----|-----|--------------------------------------------|
| 08  | 01  | 0A  | 04  | Commit Firmware from File Complete, Failed |
| 08  | 01  | 09  | 04  | Load Firmware File Complete, Failed        |

####  Notification 0x0907 - Firmware is Up to Date

This notification reports Firmware is up to date for host initiated
**Command 0xD801 - Load Firmware File**. The **Notification Detail** for
this command is shown in the table below.

Table 7.3‑3 - Notification Detail Codes

| B1  | B2  | B3  | B4  | Meaning                               |
|-----|-----|-----|-----|---------------------------------------|
| 08  | 01  | 09  | 03  | Load Firmware File Complete, Complete |

### Notification Source 0x10nn - Notifications from Device

#### Notification 0x1001 - Device Information Update

This notification reports information about general state changes that
occur within the device, outside the context of specific operations like
transactions (**Notification Source 0x01nn - Notifications from
Transactions**), requests the host receives from the firmware’s
integrated display interface (**Notification Source 0x18nn -
Notifications from User Interface**), and so on.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 320** **below**, to indicate:

- The **Category** (Cat) of notification (for example, the subsystem the
  notification is originating from)

- The **Reason** (Rsn) for the notification (Device Event)

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

The other optional message parameters in the **Notification Message**
depend on which combination of four bytes is included in **Notification
Detail**, and are described in **Table 320**.

Table 320 - Notification Detail Codes

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr>
<th>Cat</th>
<th>Rsn</th>
<th>Det</th>
<th>Ext</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5"><p>Category <strong>0x00 Power / Reset</strong> contains
notification detail codes involving the device’s power and reset
functionality. Each possible notification has a unique
<strong>Reason</strong> value:</p>
<ul>
<li><p>Reason 0x00 = Device Reset Occurred</p></li>
<li><p>Reason 0x01 = Device Reset Will Occur Soon</p></li>
<li><p>Reason 0x02 = Low Battery</p></li>
<li><p>Reason 0x03 = Key Management</p></li>
<li><p>Reason 0x04 = Temperature</p></li>
</ul></td>
</tr>
<tr>
<td>00</td>
<td>00</td>
<td>00</td>
<td>00</td>
<td><p>Power/Reset, Device Reset Occurred, Reserved, Reserved</p>
<p>The device sends and repeats this notification after the device power
cycles or resets, depending on the setting in <strong>Property
1.2.7.1.1.1 Device Reset Occurred Notification Control</strong>. If it
is set to repeat, it does so until the host acknowledges it using
<strong>Property 1.2.7.1.1.2 Device Reset Occurred Notification
Acknowledged</strong>.</p>
<p>These notifications always include the <strong>Notification
Payload</strong> parameter in the <strong>Notification Message</strong>,
as shown in <strong>Table 334</strong>.</p></td>
</tr>
<tr>
<td>00</td>
<td>01</td>
<td>00</td>
<td>00</td>
<td><p>Power/Reset, Device Reset Will Occur Soon, Reserved, Reserved</p>
<p>The device sends this notification before it automatically resets to
conform to PCI’s 24 hour Self-Test requirement, and behaves according to
the setting in <a
href="#property-1.2.7.1.1.3-device-reset-will-occur-soon-notification-control"><strong>Property
1.2.7.1.1.3 Device Reset Will Occur Soon Notification
Control</strong></a>.</p>
<p>See <strong>24 Hour Automatic Reset PCI Requirement</strong> for more
information.</p>
<p>These notifications always include the <strong>Notification
Payload</strong> parameter in the <strong>Notification Message</strong>,
which directly contains one byte indicating the number of minutes (0x01
to 0xFF) until the device will perform the reset.</p></td>
</tr>
<tr>
<td>00</td>
<td>02</td>
<td>00</td>
<td>00</td>
<td><p>Power/Reset, Battery, Low Battery Warning, Percent</p>
<p>The device sends this notification when the battery charge reaches 15
percent. If a device is powered on with a charge that is already 15
percent or below, this notification is sent shortly after power up and
includes the current battery charge percentage. Percent indicates the
percent of battery charge remaining.</p></td>
</tr>
<tr>
<td>00</td>
<td>02</td>
<td>01</td>
<td>00</td>
<td><p>Power/Reset, Battery, Power Down Imminent, Reserved</p>
<p>The device sends this notification one minute before it automatically
powers down the device because the battery charge has reached 0
percent.</p></td>
</tr>
<tr>
<td>00</td>
<td>02</td>
<td>02</td>
<td>00</td>
<td><p>Power/Reset, Battery, Battery Charge Complete, Reserved</p>
<p>The device sends this notification when the battery charger detects
that the battery is fully charged.</p></td>
</tr>
<tr>
<td>00</td>
<td>03</td>
<td>00</td>
<td>00</td>
<td><p>Power/Reset, Device reset per Command 0x1F01.</p>
<p>The device sends this notification to notify the host when Device
executes Reset Command 0x1F01.</p></td>
</tr>
<tr>
<td colspan="5"><p>Category <strong>0x01 User Event</strong> contains
notification detail codes involving events triggered by user actions.
Each possible notification has a unique <strong>Reason</strong>
value:</p>
<ul>
<li><p>Reason 0x00 = Contactless Card Presented (EMV Contactless
Only)</p></li>
<li><p>Reason 0x01 = Contactless Card Removed (EMV Contactless
Only)</p></li>
<li><p>Reason 0x02 = Card Seated in Slot (EMV Contact Only)</p></li>
<li><p>Reason 0x03 = Card Unseated from Slot (EMV Contact Only)</p></li>
<li><p>Reason 0x04 = Card Swiped (MSR Only)</p></li>
<li><p>Reason 0x05 = Touch Sensor Press On Display (Touch Only)</p></li>
<li><p>Reason 0x06 = Touch Sensor Release On Display (Touch
Only)</p></li>
<li><p>Reason 0x07 = Barcode Read (BCR Only)</p></li>
</ul>
<p>The host can use <strong>Property 1.2.7.1.2.1 User Event Notification
Controls</strong> Enable to enable these notification reasons
individually.</p>
<p>The host may choose to use these notifications to determine when to
send additional commands. For example, it may send <strong>Command
0x1001 - Start Transaction</strong>. The host should do this as quickly
as possible to minimize the response time between when the cardholder
presents a card and when the device provides feedback via a visible or
audible state change or attempts to read a chip card. Note there are
cases where the device may send a notification with
<strong>Reason</strong> = <strong>Contactless Card Presented</strong>
while the cardholder is inserting or swiping a card, so the host should
start transactions with all supported card interfaces enabled to
maximize the chances of a successful card read.</p></td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>00</td>
<td>00</td>
<td>User Event, Contactless Card Presented, EMV, Reserved (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>00</td>
<td>00</td>
<td>User Event, Contactless Card Removed, EMV, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>01</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, NTag/MIFARE Ultralite,
Reserved (EMV Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>01</td>
<td>00</td>
<td>User Event, Contactless Card Removed, NTag/MIFARE Ultralite,
Reserved (EMV Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>02</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE Classic, 1K (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>02</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE Classic, 1K (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>03</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE Classic, 4K (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>03</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE Classic, 4K (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>04</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE DESFire Light (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>04</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE DESFire Light (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>05</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE MINI® (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>05</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE MINI® (EMV Contactless
Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>06</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE Plus EV1 (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read an NFC tag. In this
case, the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>06</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE Plus EV1 (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>07</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE Plus EV2 (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read an NFC tag. In this
case, the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID.</strong></p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>07</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE Plus EV2 (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>08</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE Plus SE (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read an NFC tag. In this
case, the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>08</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE Plus SE (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>09</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE Plus X (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read an NFC tag. In this
case, the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>09</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE Plus X (EMV Contactless
Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>0A</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE DESFire EV1 (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>0A</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE DESFire EV1 (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>0B</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE DESFire EV2 (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>0B</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE DESFire EV2 (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>0C</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE DESFire EV3 (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>0C</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE DESFire EV3 (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>00</td>
<td>00</td>
<td>User Event, Card Seated in Slot, Reserved, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td>01</td>
<td>03</td>
<td>00</td>
<td>00</td>
<td>User Event, Card Unseated from Slot, Reserved, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td>01</td>
<td>04</td>
<td>00</td>
<td>00</td>
<td><p>User Event, Card Swiped, Reserved, Reserved (MSR Only)</p>
<p>When the host receives this notification, it should call
<strong>Command 0x1001 - Start Transaction</strong> before the timeout
configured in <strong>Property 1.2.7.1.2.2 User Event Notification MSR
Data Timeout (MSR Only)</strong> to process the MSR swipe data the
device is temporarily storing in memory.</p></td>
</tr>
<tr>
<td>01</td>
<td>05</td>
<td>00</td>
<td>00</td>
<td><p>User Event, Touch Sensor Press On Display, Reserved, Reserved
(Touch Only)</p>
<p>These notifications always include the <strong>Notification
Payload</strong> parameter in the <strong>Notification Message</strong>,
as shown in <strong>Table 326</strong>.</p></td>
</tr>
<tr>
<td>01</td>
<td>06</td>
<td>00</td>
<td>00</td>
<td><p>User Event, Touch Sensor Release On Display, Reserved, Reserved
(Touch Only)</p>
<p>These notifications always include the <strong>Notification
Payload</strong> parameter in the <strong>Notification Message</strong>,
as shown in <strong>Table 326</strong>.</p></td>
</tr>
<tr>
<td>01</td>
<td>07</td>
<td>00</td>
<td>00</td>
<td><p>Barcode Reader, Read Barcode Result, Type, Reserved (BCR
Only)</p>
<ul>
<li><p>Type 0x00 = Unknown</p></li>
<li><p>Type 0x01 = MagTek</p></li>
<li><p>Type 0x02 = EMV</p></li>
</ul>
<p>The barcode reader has successfully read a barcode. In this case, the
device includes barcode data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
If the data is encrypted, the data is in the format described in
<strong>Table 341</strong>. Data that is not encrypted is in the format
described in <strong>Table 342</strong>.</p></td>
</tr>
<tr>
<td colspan="5"><p>Category <strong>0x02 Session Management</strong>
contains notification detail codes involving session management
functionality (Session Management Only). Each possible notification has
a unique <strong>Reason</strong> value:</p>
<ul>
<li><p>Reason 0x00 = Session Expiring Soon</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">02</td>
<td style="text-align: center;">00</td>
<td>00</td>
<td>00</td>
<td><p>Session Management, Session Expiring Soon, Reserved, Reserved</p>
<p>The device sends this notification 5 minutes before a session expires
and every minute after that until the session is extended or the
connection is closed. The host can optionally extend the session with
<strong>Command 0x1F03 - Extend Session</strong> or by sending any
command request.</p>
<p>These notifications always include the <strong>Notification
Payload</strong> parameter in the <strong>Notification Message</strong>,
as shown in <strong>Table 328</strong>.</p></td>
</tr>
<tr>
<td colspan="5"><p>Category <strong>0x03 Key Management</strong>
contains notification detail codes involving key management
functionality (WLAN Only). Each possible notification has a unique
<strong>Reason</strong> value:</p>
<ul>
<li><p>Reason 0x00 = CSR keys generated Reason</p></li>
<li><p>0x01 = Certificate Expiring Soon</p></li>
</ul></td>
</tr>
<tr>
<td>03</td>
<td>00</td>
<td>00</td>
<td>00</td>
<td><p>Key management, CSR keys generated, Reserved, Reserved</p>
<p>This notification does not include a Notification Payload. See
<strong>Command 0xEF02 – Generate CSR keys (WLAN Only)</strong> for more
information.</p></td>
</tr>
<tr>
<td>03</td>
<td>01</td>
<td>00</td>
<td>00</td>
<td><p>Key management, Certificate Expiring Soon, Reserved, Reserved</p>
<p>See <strong>Property 1.2.2.1.1.B Certificate Expiring Soon
Notification Threshold</strong> for more information.</p>
<p>These notifications always include the <strong>Notification
Payload</strong> parameter in the <strong>Notification Message</strong>,
as shown in <strong>Table 330 - Notification Payload for Key management,
Certificate Expiring Soon</strong>.</p></td>
</tr>
<tr>
<td colspan="5"><p>Category <strong>0x04 Temperature</strong> contains
notification detail codes involving temperature reporting. Each possible
notification has a unique <strong>Reason</strong> value:</p>
<ul>
<li><p>Reason 0x00 = Temperature out of range</p></li>
</ul></td>
</tr>
<tr>
<td>04</td>
<td>00</td>
<td>00</td>
<td>00</td>
<td><p>Temperature, Out of Range, Low Warning, Temperature</p>
<p>The device sends this notification when the device’s temperature
falls below the temperature set in Low Temperature Notification Level
(1.2.7.1.4.1). The temperature reported is in Celsius.</p></td>
</tr>
<tr>
<td>04</td>
<td>00</td>
<td>01</td>
<td>00</td>
<td><p>Temperature, Out of Range, High Warning, Temperature</p>
<p>The device sends this notification when the device’s temperature
rises above the temperature set in High Temperature Notification Level
(1.2.7.1.4.2). The temperature reported is in Celsius.</p></td>
</tr>
</tbody>
</table>

##### Notification 0x1001 – Low Battery Warning

The device sends this notification when the battery charge reaches 15
percent. If a device is powered on with a charge that is already 15
percent or below, this notification is sent shortly after power up and
includes the current battery charge percentage. Percent indicates the
percent of battery charge remaining. It is recommended that the device
is charged using a USB power source soon after receiving this
notification. See **Table 13 - Notification Message Format** and **Table
321 Low Battery Notification Example**.

| Example (Hex)                          |
|----------------------------------------|
| AA 00 81 04 83 00 10 01 82 00 02 00 0D |

Table 321 Low Battery Notification Example

##### Notification 0x1001 - Low Battery Shutdown

The device sends this notification one minute before it automatically
powers down the device. This occurs when the battery charge has reached
0 percent. Shutdown can be prevented by connecting the device to a USB
power source. See **Table 13 - Notification Message Format** and **Table
322 Low Battery Shutdown Response Example**.

**Table 322 Low Battery Shutdown Response Example**

| Example (Hex)                          |
|----------------------------------------|
| AA 00 81 04 83 00 10 01 82 00 02 01 00 |

##### Notification 0x1001 - Battery Charged

The device sends this notification when the battery charger detects that
the battery is fully charged. This only occurs when the device is
powered by a USB power source. See **Table 13 - Notification Message
Format** and **Table 323 - Battery Charged Notification Example**.

Table 323 - Battery Charged Notification Example

| Example (Hex)                          |
|----------------------------------------|
| AA 00 81 04 83 00 10 01 82 00 02 02 00 |

Table 324 - Notification Payload for Device Reset Occurred

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |
| 1001 = Device Information Update |  |  |  |  |  |
| 81 | var | This parameter has the same length and value described by **Property 2.3.1.2.1.1 Device Operational Status**. | B | R |  |
| 82 | var | This parameter has the same length and value described by **Property 2.3.1.2.1.2 Offline Status Detail**. | B | R |  |
| xx | var | More data objects may be added in future firmware revisions. |  |  |  |
| End of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |

Table 325 - Notification Example for Device Reset Occurred

| Example (Hex)                                                   |
|-----------------------------------------------------------------|
| AA00 81 04 83001001 82 04 00000000 84 08 1001 81 01 02 82 01 00 |

Table 326 - Notification Payload for Touch Sensor Press or Release On
Display (Touch Only)

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 5%" />
<col style="width: 60%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
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
<td colspan="6">Beginning of <strong>Notification Message</strong> found
on page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
<tr>
<td colspan="6">1001 = Device Information Update</td>
</tr>
<tr>
<td>81</td>
<td>04</td>
<td><p>Press / Release Coordinates</p>
<p>Coordinates of the press / release from origin 0,0 at the top left
corner of the display, automatically adjusted to match the device’s
orientation as configured by Property 1.2.3.1.1.2 Custom Idle Page Image
Device Locked (Display Only).</p>
<p>Bytes 1..2 X Coordinate</p>
<p>X coordinate of press / release, in big endian order.</p>
<p>Bytes 3..4 Y Coordinate</p>
<p>Y Coordinate of press / release, in big endian order.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of <strong>Notification Message</strong> found on
page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
</tbody>
</table>

Table 327 - Notification Example for Touch Sensor Press or Release On
Display (Touch Only)

| Example (Hex)                                                   |
|-----------------------------------------------------------------|
| AA00 81 04 83001001 82 04 00000000 84 08 1001 81 04 00 80 00 80 |

Table 328 - Notification Payload for Session Expiring Soon (Session
Management Only)

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 5%" />
<col style="width: 60%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
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
<td colspan="6">Beginning of <strong>Notification Message</strong> found
on page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
<tr>
<td colspan="6">1001 = Device Information Update</td>
</tr>
<tr>
<td>81</td>
<td>1</td>
<td><p>Interface</p>
<p>0x00 = WLAN</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>1</td>
<td><p>Connection</p>
<p>0x00 = Connection 0, Interfaces that only support one connection will
use connection 0. WLAN will always set this to 0 even if the device is
configured to support more than one connection with <strong>Property
1.2.2.1.1.A Maximum Client Connections</strong> since there is only a
single session for all clients. See <strong>Command 0x1F03 - Extend
Session (Session Management Only)</strong> for more information on this
scenario.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>1</td>
<td><p>Expiration Time</p>
<p>The time in minutes until the session expires.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>xx</td>
<td>var</td>
<td>More data objects may be added in future firmware revisions.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="6">End of <strong>Notification Message</strong> found on
page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
</tbody>
</table>

Table 329 - Notification Example for Session Expiring Soon (Session
Management Only)

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA00 81 04 83001001 82 04 00000000 84 0B 1001 81 01 00 82 01 00 83 01 05 |

Table 330 - Notification Payload for Key management, Certificate
Expiring Soon (Session Management Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |
| 1001 = Device Information Update |  |  |  |  |  |
| 81 | 1 | This parameter has the same length and value described by **Property 1.2.2.1.1.B Certificate Expiring Soon Notification Threshold**. | B | R |  |
| 82 | 1 | This parameter contains the certificate identifier. See the certificate file type section (File Type 0x03) from ­Table 196 to identify this certificate by locating the certificate that has a File Subtype that matches this certificate identifier. | B | R |  |
| 83 | 1 | The number of days the certificate is still valid. | B | R |  |
| End of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |

Table 331 - Notification Example for Key management, Certificate
Expiring Soon (Session Management Only)

| Example (Hex)                                                   |
|-----------------------------------------------------------------|
| AA00 81 04 83001001 82 04 00000000 84 08 1001 81 01 02 82 01 00 |

Table 332 - Notification Payload for UID

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |
| 1001 = Device Information Update |  |  |  |  |  |
| 84 | var | NFC Payload | B | R |  |
| /DF79 | var | NFC UID | B | R |  |
| End of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |

Table 333 – Notification Payload for UID Example

| Example (Hex) |
|----|
| AA 00 81 04 83 00 10 01 82 04 01 00 01 00 84 0E 10 01 84 0A DF 79 07 04 37 1F 71 BF 61 80 |

### Notification Source 0x18nn - Notifications from User Interface

#### Notification 0x1801 - User Interface Information Update (MAGTEK INTERNAL ONLY FOR NOW)

This notification reports information about progress and state changes
involving the device’s User Interface modules.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, to indicate:

- The **Payment Technology** (PT) involved

- The **Reason** (Rsn) for the notification

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

#### Notification 0x1803 - User Interface Host Action Request

This notification requests that the host take action during operations
involving the device’s User Interface modules.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 334**, to indicate:

- The **User Interface Module** (UI) involved

- The **Reason** (Rsn) for the notification (UI Event)

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

Table 334 - Notification Detail Codes

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th>UI</th>
<th>Rsn</th>
<th>Det</th>
<th>Ext</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5">Module <strong>0x00 Miscellaneous</strong> contains UI
notification detail codes that are not specific to a particular UI
module.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="5"><p>Module <strong>0x01 Touchscreen</strong> contains UI
notification detail codes that are specific to the touchscreen module
(Touch Only).</p>
<ul>
<li><p>Reason 0x01 = Signature Capture</p></li>
<li><p>Reason 0x02 = Functional button selected</p></li>
<li><p>Reason 0x03 = Button text string selected</p></li>
<li><p>Reason 0x04 = Button $Amount selected</p></li>
<li><p>Reason 0x05 = Present card functional button Right is
selected</p></li>
</ul></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>01</td>
<td>00</td>
<td>Touchscreen, Functional button Left selected</td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>02</td>
<td>00</td>
<td>Touchscreen, Functional button Middle selected</td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>03</td>
<td>00</td>
<td>Touchscreen, Functional button Right selected</td>
</tr>
<tr>
<td>01</td>
<td>03</td>
<td>01</td>
<td>00</td>
<td>Touchscreen, Text string button 1 selected</td>
</tr>
<tr>
<td>01</td>
<td>03</td>
<td>02</td>
<td>00</td>
<td>Touchscreen, Text string button 2 selected</td>
</tr>
<tr>
<td>01</td>
<td>03</td>
<td>03</td>
<td>00</td>
<td>Touchscreen, Text string button 3 selected</td>
</tr>
<tr>
<td>01</td>
<td>03</td>
<td>04</td>
<td>00</td>
<td>Touchscreen, Text string button 4 selected</td>
</tr>
<tr>
<td>01</td>
<td>03</td>
<td>05</td>
<td>00</td>
<td>Touchscreen, Text string button 5 selected</td>
</tr>
<tr>
<td>01</td>
<td>03</td>
<td>06</td>
<td>00</td>
<td>Touchscreen, Text string button 6 selected</td>
</tr>
<tr>
<td>01</td>
<td>04</td>
<td>00</td>
<td>00</td>
<td>Touchscreen, $Amount button selected, Data Attached contain the
amount selected as described in <strong>Table 336 - Notification Payload
for $ Amount button selected, Data Attached</strong></td>
</tr>
<tr>
<td>01</td>
<td>05</td>
<td>00</td>
<td>00</td>
<td>Touchscreen, Present card functional button Right selected</td>
</tr>
<tr>
<td colspan="5"><p>Module <strong>0x02 Display</strong> contains UI
notification detail codes that are specific to the display module. The
device primarily uses these notifications to request that the host stand
in as a display to interact with cardholders / operators when the device
does not have a display of its own (No Display Only).</p>
<ul>
<li><p>Reason 0x01 = Display Message Request</p></li>
<li><p>Reason 0x02 = Cardholder Selection Request</p></li>
<li><p>Reason 0x03 = Online PIN Request (MAGTEK INTERNAL ONLY FOR
NOW)</p></li>
</ul></td>
</tr>
<tr>
<td>02</td>
<td>01</td>
<td>00</td>
<td>00</td>
<td><p>Display, Display Message, No Data Attached, Clear Display.</p>
<p>The host should clear any existing messages it is currently
displaying (No Display Only).</p></td>
</tr>
<tr>
<td>02</td>
<td>01</td>
<td>01</td>
<td>00</td>
<td><p>Display, Display Message, Data Attached, No Cancel Function (No
Display Only)</p>
<p>In this case, the notification includes additional data and display
control, defined in <strong>Table 335</strong>, in the
<strong>Notification Payload</strong> portion of the
<strong>Notification Message</strong>.</p>
<p>This notification is for simple messages. The host should show the
requested message until another notification arrives or until the host
needs to use the display for its own purposes. For example, during a
transaction, this notification will pass along the simple messages in
the transaction sequence like <strong>CARD READ OK - REMOVE
CARD</strong>, <strong>THANK YOU</strong>, and
<strong>WELCOME</strong>.</p></td>
</tr>
<tr>
<td>02</td>
<td>01</td>
<td>02</td>
<td>00</td>
<td><p>Display, Display Message, Data Attached, Include Cancel Function
(No Display Only)</p>
<p>In this case, the notification includes additional data and display
control, defined in <strong>Table 335</strong>, in the
<strong>Notification Payload</strong> portion of the
<strong>Notification Message</strong>.</p>
<p>The host should show the requested message and should allow the
request to be canceled by a cardholder or operator. For example, during
a transaction, this notification will pass along the simple messages in
the transaction sequence like “TAP, INSERT, or SWIPE CARD,” where
cancelation is appropriate. If the cancel button involves canceling the
whole transaction, the host should send <strong>Command 0x1008 - Cancel
Transaction</strong>.</p></td>
</tr>
<tr>
<td>02</td>
<td>02</td>
<td>00</td>
<td>00</td>
<td><p>Display, Cardholder Selection, Data Attached, Reserved (No
Display Only)</p>
<p>In this case, the notification includes additional data and display
control, defined in <strong>Table 337</strong>, in the
<strong>Notification Payload</strong> portion of the
<strong>Notification Message</strong>.</p>
<p>The host should show the requested selection, then send
<strong>Command 0x1802 - Report Cardholder Selection</strong> to device
to return the cardholder’s selection to the device.</p></td>
</tr>
<tr>
<td>02</td>
<td>03</td>
<td>00</td>
<td>00</td>
<td><p>(MAGTEK INTERNAL ONLY FOR NOW, No Display Only)</p>
<p>Display, Online PIN Request, Application ID / Amount, Data Attached,
Reserved.</p>
<p>In this case, the notification includes additional data, defined in
<strong>Table 338</strong>, in the <strong>Notification Payload</strong>
portion of the <strong>Notification Message</strong>.</p>
<p>The host must send Command TBD to the device to indicate PIN Capture
data and result.</p></td>
</tr>
</tbody>
</table>

Table 335 - Notification Payload for Display Message Request
Notifications (No Display Only)

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 5%" />
<col style="width: 60%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
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
<td colspan="6">Beginning of <strong>Notification Message</strong> found
on page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
<tr>
<td colspan="6">1803 = <strong>Notification 0x1803 - User Interface Host
Action Request</strong></td>
</tr>
<tr>
<td>/81</td>
<td>01</td>
<td><p>Reserved for time functions.</p>
<p>0x00</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>01</td>
<td><p>Append or Clear Display</p>
<ul>
<li><p>0x00 = Append the message(s) on the next available row.</p></li>
<li><p>0x01 = Clear the display first and display the requested message
on the first row.</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>var</td>
<td><p>Message</p>
<p>This parameter is a set of one or more ASCII strings the host should
show, with each string terminated by any one of the following
characters. MagTek recommends proceeding to the next row on receiving
any of these characters:</p>
<ul>
<li><p>Null (0x00)</p></li>
<li><p>LF (0x0A)</p></li>
<li><p>The end of the Message parameter.</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/85</td>
<td>var</td>
<td><p>Enhanced Application Select Message</p>
<p>For Contactless, this parameter will return the PPSE response
starting from tag BF0C</p>
<p>BF0C &lt;LEN&gt;&lt;VALUE&gt;</p>
<p>For Contact, this parameter will return all available AID returned
from the PSE or List Of AIDs, from tag 70</p>
<p>70 &lt;len&gt;</p>
<p>61 &lt;len&gt;</p>
<p>4F&lt;len&gt;&lt;value of AID&gt;</p>
<p>50&lt;len&gt;&lt;value of Application Label&gt;</p>
<p>87&lt;len&gt;&lt;value of Application Priority Indicator&gt;</p>
<p>61 &lt;len&gt;</p>
<p>4F&lt;len&gt;&lt;value of AID&gt;</p>
<p>50&lt;len&gt;&lt;value of Application Label&gt;</p>
<p>87&lt;len&gt;&lt;value of Application Priority Indicator,
optional&gt;</p>
<p>If the GPO Response returns a <strong>Notification 0x0101 -
Transaction Information Update of</strong>’69 85’, the response will be
sent first by the device and this Enhanced Application Select Message
will be sent again.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of <strong>Notification Message</strong> found on
page <strong><a href="#notification-message">30</a>.</strong></td>
</tr>
</tbody>
</table>

**Table 336 - Notification Payload for \$ Amount button selected, Data
Attached**

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page **[30](#notification-message).** |  |  |  |  |  |
| 1803 = **Command 0x1803 - Display Message (Display Only)** |  |  |  |  |  |
| 84 | 9 | Amount selected payload | B | R |  |
| /9F02 | 6 | Dollar and cents amount selected in BCD format | B | R |  |
| End of **Notification Message** found on page **[30](#notification-message).** |  |  |  |  |  |

Table 337 - Notification Payload for Cardholder Selection Notifications
(No Display Only)

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 5%" />
<col style="width: 60%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
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
<td colspan="6">Beginning of <strong>Notification Message</strong> found
on page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
<tr>
<td colspan="6">1803 = <strong>Notification 0x1803 - User Interface Host
Action Request</strong></td>
</tr>
<tr>
<td>/81</td>
<td>01</td>
<td>Time in seconds the device will wait for host to respond with
<strong>Command 0x1802 - Report Cardholder Selection</strong>.</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>01</td>
<td><p>Append or Clear Display</p>
<ul>
<li><p>0x00 = Append, display the messages on the next line.</p></li>
<li><p>0x01 = Clear, clear the display first and display the requested
message on the first line.</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>var</td>
<td><p>Message</p>
<p>This parameter is a set of one or more ASCII strings the host should
show, with each string terminated by any one of the following
characters. MagTek recommends proceeding to the next row on receiving
any of these characters:</p>
<ul>
<li><p>Null (0x00)</p></li>
<li><p>LF (0x0A)</p></li>
<li><p>The end of the Message parameter.</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of <strong>Notification Message</strong> found on
page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
</tbody>
</table>

Table 338 - Notification Payload for Display Online PIN Request
Notifications (MAGTEK INTERNAL ONLY FOR NOW, No Display Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |
| 1803 = **Notification 0x1803 - User Interface Host Action Request** |  |  |  |  |  |
| /9F12 | var | This contains AID Preferred Name (Tag 9F12) if it is provided by the card. | B | O |  |
| /9F06 | var | This contains the AID (Tag) if Tag 9F12 is not provided by the card. | B | O |  |
| /9F02 | 06 | This contains the Amount (Tag 9F02) if it should be displayed. For example, the device excludes this when using a provisional amount for a Quick Chip transaction. | B | O |  |
| End of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |

#### Notification 0x1805 - User Interface Operation Complete

This notification reports information about progress and state changes
that occur during interaction with the User Interface modules.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 339**, to indicate:

- The **User Interface Module** (UI) involved

- The **Reason** (Rsn) for the notification (UI Event)

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

Table 339 - Notification Detail Codes

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th>UI</th>
<th>Rsn</th>
<th>Det</th>
<th>Ext</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5"><p>Module <strong>0x01 Touchscreen</strong> contains UI
notification detail codes that are specific to the touchscreen module
(Touch Only)</p>
<ul>
<li><p>Reason 0x01 = Signature Capture</p></li>
<li></li>
</ul></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>01</td>
<td>01</td>
<td><p>Touchscreen, Signature Capture, Success, Data Available (Touch
Only)</p>
<p>In this case, the device includes the File ID as defined in
<strong>Table 340</strong> in the <strong>Additional Detail</strong>
portion of the <strong>Notification Message</strong>. The host should
use this File ID and call <a href="#_Command_0xD821_-"><strong>Command
0xD825 – Start Get File from Device</strong></a>.</p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>02</td>
<td>01</td>
<td>Touchscreen, Signature Capture, Operation Failed, Timeout (Touch
Only)</td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>02</td>
<td>02</td>
<td>Touchscreen, Signature Capture, Operation Failed, Hardware Not
Available (Touch Only)</td>
</tr>
<tr>
<td colspan="5"><p>Module <strong>0x02 Display</strong> contains UI
notification detail codes that are specific to the display module
(Display Only).</p>
<ul>
<li><p>Reason 0x01 = Display Message Request</p></li>
<li><p>Reason 0x02 = Cardholder Selection Request</p></li>
<li><p>Reason 0x03 = Online PIN Request (MAGTEK INTERNAL ONLY FOR
NOW)</p></li>
</ul></td>
</tr>
<tr>
<td>02</td>
<td>01</td>
<td>00</td>
<td>00</td>
<td><p>Display, Display Message, Timed Out, Reserved</p>
<p>The device has finished displaying a message requested by the host
using <strong>Command 0x1803 - Display Message</strong>.</p></td>
</tr>
<tr>
<td colspan="5"><p>Module <strong>0x04 Barcode Reader</strong> contains
notification detail codes that are specific to the barcode reader
module.</p>
<ul>
<li><p>Reason 0x03 = Read Barcode Result</p></li>
</ul></td>
</tr>
<tr>
<td>04</td>
<td>03</td>
<td>01</td>
<td>00</td>
<td><p>Barcode Reader, Read Barcode Result, Success, Unidentified
Type</p>
<p>The barcode reader has successfully read a barcode. In this case, the
device includes barcode data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
If the data is encrypted, the data is in the format described in
<strong>Table 341</strong>. Data that is not encrypted is in the format
described in <strong>Table 342</strong>.</p></td>
</tr>
<tr>
<td>04</td>
<td>03</td>
<td>01</td>
<td>01</td>
<td><p>Barcode Reader, Read Barcode Result, Success, MagTek Blob
Type</p>
<p>The barcode reader has successfully read a barcode. In this case, the
device includes barcode data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
MagTek Blob data is always encrypted. The data is in the format
described in <strong>Table 341</strong>.</p></td>
</tr>
<tr>
<td>04</td>
<td>03</td>
<td>01</td>
<td>02</td>
<td><p>Barcode Reader, Read Barcode Result, Success, EMV Type</p>
<p>The barcode reader has successfully read a barcode. In this case, the
device includes barcode data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
EMV barcode data is always encrypted. The data is in the format
described in <strong>Table 341.</strong></p></td>
</tr>
<tr>
<td>04</td>
<td>03</td>
<td>02</td>
<td>01</td>
<td>Barcode Reader, Read Barcode Result, Operation Failed, Timeout</td>
</tr>
<tr>
<td colspan="5"><p>Module <strong>0x05 Buzzer</strong> contains
notification detail codes that are specific to the buzzer module.</p>
<ul>
<li><p>Reason 0x04 = Buzzer Result</p></li>
</ul></td>
</tr>
<tr>
<td>05</td>
<td>04</td>
<td>01</td>
<td>00</td>
<td>Buzzer, Buzzer Result, Operation Success, Reserve</td>
</tr>
<tr>
<td>05</td>
<td>04</td>
<td>02</td>
<td>00</td>
<td>Buzzer, Buzzer Result, Operation Fail, Reserve</td>
</tr>
<tr>
<td colspan="5"><p>Module <strong>0x06 Card Emulation</strong> contains
notification detail codes that are specific to card emulation.</p>
<ul>
<li><p>Reason 0x05 = Card Emulation Result</p></li>
</ul></td>
</tr>
<tr>
<td>06</td>
<td>05</td>
<td>01</td>
<td>00</td>
<td>Card Emulation, Card Emulation Result, Operation Success,
Reserve</td>
</tr>
<tr>
<td>06</td>
<td>05</td>
<td>02</td>
<td>01</td>
<td>Card Emulation, Card Emulation Result, Operation Fail, Timeout</td>
</tr>
<tr>
<td>06</td>
<td>05</td>
<td>02</td>
<td>03</td>
<td>Card Emulation, Card Emulation Result, Operation Fail, Cancel</td>
</tr>
<tr>
<td>06</td>
<td>05</td>
<td>02</td>
<td>04</td>
<td>Card Emulation, Card Emulation Result, Operation Fail, Error</td>
</tr>
</tbody>
</table>

Table 340 - Additional Detail for Touchscreen, Signature Capture,
Success, Data Available (Touch Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |
| 83 | 04 | File ID from ­Table 196 | B | R |  |
| End of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |

Table 341 - Notification Payload for Barcode Reader, Read Barcode
Result, Success (Encrypted Data Attached)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 59%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 11%" />
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
<td colspan="6">Beginning of <strong>Notification Message</strong> found
on page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
<tr>
<td colspan="6">1805 = User Interface Operation Complete</td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td>Notification Payload</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF59</td>
<td>var</td>
<td><p>Encrypted Data Primitive</p>
<p>Decrypt the value of this TLV data object using the algorithm and
variant specified in the <strong>Encrypted Data KSN</strong> parameter
and the <strong>Encrypted Data Encryption Type</strong> parameter to
read its contents. The format of the decrypted data is shown in
<strong>Table 342</strong>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF50</td>
<td>var</td>
<td>Encrypted Data KSN</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF51</td>
<td>01</td>
<td><p>Encrypted Data Encryption Type</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of <strong>Notification Message</strong> found on
page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
</tbody>
</table>

Table 342 - Notification Payload for Barcode Reader, Read Barcode
Result, Success (Unencrypted Data)

| Tag   | Len | Value / Description    | Typ | Req | Default |
|-------|-----|------------------------|-----|-----|---------|
| FC    | var | Barcode Data Container | T   | R   |         |
| /DF74 | var | Barcode Data           | B   | O   |         |

**Table 343 – Default User Interface String IDs and Strings**

| Display String ID | Display String               |
|-------------------|------------------------------|
| 0x0000            | “ ”                          |
| 0x0001            | “Thank You”                  |
| 0x0002            | “Hello”                      |
| 0x0003            | “Please Select”              |
| 0x0004            | “Touch Screen To Continue”   |
| 0x0005            | “Cancel”                     |
| 0x0006            | “Select a Transaction”       |
| 0x0007            | “Deposit”                    |
| 0x0008            | “Withdrawal”                 |
| 0x0009            | “Choose PIN”                 |
| 0x000A            | “Change PIN”                 |
| 0x000B            | “Balance”                    |
| 0x000C            | “Cash Advance”               |
| 0x000D            | “Authenticate Me”            |
| 0x000E            | “Transfer”                   |
| 0x000F            | “Make Payment”               |
| 0x0010            | “On Sale”                    |
| 0x0011            | “Discount”                   |
| 0x0012            | “Clearance”                  |
| 0x0013            | “\$5.00 /5 Mins.”            |
| 0x0014            | “\$6.00 /7 Mins.”            |
| 0x0015            | “\$7.00 /9 Mins.”            |
| 0x0016            | “\$8.00 /15 Mins.”           |
| 0x0017            | “Call Attendant”             |
| 0x0018            | “Print Receipt”              |
| 0x0019            | “Email Receipt”              |
| 0x001A            | “Text Receipt”               |
| 0x001B            | “Please Select An Amount”    |
| 0x001C            | “Please Select A Tip Amount” |
| 0x001D            | “Menu Selection 1”           |
| 0x001E            | “Menu Selection 2”           |
| 0x001F            | “Menu Selection 3”           |
| 0x0020            | “Menu Selection 4”           |
| 0x0021            | “Service Request”            |
| 0x0022            | “Show More”                  |
| 0x0023            | “Options”                    |
| 0x0024            | “What is the issue?”         |
| 0x0025            | “Exit”                       |
| 0x0026            | “No Hot Water”               |
| 0x0027            | “Doesn't Spin”               |
| 0x0028            | “Water Leakage”              |
| 0x0029            | “No Heat”                    |
| 0x002A            | “Please select a Machine”    |
| 0x002B            | “Pump 1”                     |
| 0x002C            | “Pump 2”                     |
| 0x002D            | “Pump 3”                     |
| 0x002E            | “Pump 4”                     |
| 0x002F            | “A1”                         |
| 0x0030            | “A2”                         |
| 0x0031            | “A3”                         |
| 0x0032            | “A4”                         |
| 0x0033            | “B1”                         |
| 0x0034            | “B2”                         |
| 0x0035            | “B3”                         |
| 0x0036            | “B4”                         |
| 0x0037            | “C1”                         |
| 0x0038            | “C2”                         |
| 0x0039            | “C3”                         |
| 0x003A            | “C4”                         |
| 0x003B            | “\$5.50 – Cake”              |
| 0x003C            | “\$5.00 – Muffin”            |
| 0x003D            | “\$6.50 – Croissant”         |
| 0x003E            | “\$4.50 – Danish”            |
| 0x003F            | “Req. QR Code”               |
| 0x0040            | “Scan QR Code”               |
| 0x0041            | “Scan NFC”                   |
| 0x0042            | “Call Server”                |
| 0x0043            | “Request Bill”               |
| 0x0044            | “Approve”                    |
| 0x0045            | “Reject”                     |
| 0x0046            | “Verify SMS”                 |
| 0x0047            | “Verify Email”               |
| 0x0048            | “English”                    |
| 0x0049            | “Spanish”                    |
| 0x0080            | “Hola”                       |
| 0x0081            | “Por Favor Seleccione”       |
| 0x0082            | “Toca Para Continuar”        |
| 0x0083            | “Cancelar”                   |
| 0x0084            | “Seleccione Una Transaccion” |
| 0x0085            | “Deposito”                   |
| 0x0086            | “Retiro”                     |
| 0x0087            | “Elija PIN”                  |
| 0x0088            | “Cambiar PIN”                |
| 0x0089            | “Adelanto En Efectivo”       |
| 0x008A            | “Autenticarme”               |
| 0x008B            | “Verificar SMS”              |
| 0x008C            | “Confirmar”                  |
| 0x008D            | “Mostrar Mas”                |
| 0x008E            | “Opciones”                   |
| 0x008F            | “Salida”                     |
| 0x0090            | “Transferir”                 |
| 0x0091            | “Realizar Pago”              |
| 0x0092            | “En Venta”                   |
| 0x0093            | “Descuento”                  |
| 0x0094            | “Autorizacion”               |
| 0x0095            | “Operador De Llamada”        |
| 0x0096            | “Imprimir Recibo”            |
| 0x0097            | “Correo Electronico”         |
| 0x0098            | “Recibo De Texto”            |
| 0x0099            | “Seleccione Una Cantidad”    |
| 0x009A            | “Anadir Un Consejo”          |
| 0x009B            | “Requerido Codigo QR”        |
| 0x009C            | “Escanear Codigo QR”         |
| 0x009D            | “Escanear NFC”               |
| 0x009E            | “Servidor De Llamadas”       |
| 0x009F            | “Solicitar Factura”          |
| 0x00A0            | “Aprobar”                    |
| 0x00A1            | “Rechazar”                   |
| 0x00A2            | “Gracias”                    |
| 0x00A3            | “Ingles”                     |
| 0x00A4            | “Espanol”                    |

String ID value can be from 0x0000 to 0x012B, and String length maximum
is 30 characters. This default configured Strings can be changed and
uploaded to the device. See **4.29 UI Configuration File Type**