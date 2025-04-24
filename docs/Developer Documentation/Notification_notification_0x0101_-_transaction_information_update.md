---
title: Notification 0x0101 - Transaction Information Update
layout: home
parent: Notifications
nav_order: 2
---

## Notification 0x0101 - Transaction Information Update

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

#