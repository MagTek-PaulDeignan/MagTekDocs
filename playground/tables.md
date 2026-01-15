---
title: Table Demo
layout: home
parent: Playground
nav_order: 4
---
# Tables Documentation



## 2.3 How to Use SLIP Format (SLIP Only)
For connection types that do not include error detection and correction, such as serial protocols, which
provides a means for the host and device to re-synchronize in the case of connection errors by watching
for specifically reserved frame delimiters marking the start and end of a message. The MMS SLIP
wrapper is defined in Table 2.3-1.
All messages start with SLIP’s frame delimiter C0, and must consider SLIP escape sequences that deal
with occurrences of C0 inside the SLIP data frame:
• If an outbound message contains the byte value C0, software should encode it into SLIP as DB DC.
• If an inbound message contains the byte sequence DB DC, software should decode it to C0.
• If an outbound message contains the byte value DB, software should encode it into SLIP as DB DD.
• If an inbound message contains the byte sequence DB DD, software should decode it to DB.
Message Info indicates the direction of the message (such as Direction Host to Device for Commands,
Direction Device to Host for Notifications). If the host has sent the device a command that exceeds the
device’s incoming message buffer capacity, the device responds with a brief message indicating
Hardware Capability Exceeded, and populates Length of MMS Message with the maximum possible
message length the device can process, followed by a zero length MMS Message and the closing SLIP
Frame Delimiter.
For general information about messages, see section 2.4.
For specific messages, see sections 6 Commands and 7 Notifications.



**Table 2.3-1 - MMS SLIP Wrapper**

| Offset| Value |
|:-----------:|:-----------|
| Byte 0 | SLIP Frame Delimiter = 0xC0 |
| Byte 1 | Message Info <br> 0x00 = Direction Host to Device <br> 0x02 = Direction Device to Host <br> 0x03 = Hardware Capability Exceeded |
| Bytes 2..5 |  Length of MMS Message <br>Use big endian order |
| Bytes 6..n | MMS Message |
| Byte n+1 | SLIP Frame Delimiter = 0xC0 |


<table>
    <tr>
        <th>Content</th>
        <th>Example</th>
    </tr>
    <tr>
        <td>List</td>
        <td><ul>
            <li>aaa</li>
            <li>bbb</li>
        </ul></td>
    </tr>
    <tr>
        <td>Code block</td>
        <td>
            <pre><code>
ccc
            </code></pre>
        </td>
    </tr>
    <tr>
        <td>Image</td>
        <td><img src="example.png"></td>
    </tr>
</table>



<table>
<colgroup>
<col width="10%" />
<col width="90%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">First column **fields**</td>
<td markdown="span">Some descriptive text. This is a markdown link to [Google](http://google.com). Or see [some link](mydoc_tags).</td>
</tr>
<tr>
<td markdown="span">Second column **fields**</td>
<td markdown="span">Some more descriptive text.
</td>
</tr>
</tbody>
</table>



<table>
<thead>
<tr class="header">
<th>Tag</th>
<th>Len</th>
<th>Value/Description</th>
<th>Type</th>
<th>Req</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">81</td>
<td markdown="span">01</td>
<td markdown="span">Reserved</td>
<td markdown="span"></td>
<td markdown="span"></td>
<td markdown="span">Default</td>
</tr>

</tbody>
</table>



Beginning of any wrappers, at minimum including **Request Message** found on page **58**

1001 = Command 0x1001 - Start Transaction

| Tag | Len | Value / Description| Typ | Req | Default |
|-----|-----|--------------------|-----|-----|---------|
| 81  | 01  |Reserved            |     | O   |         |
| 82  | 01  |Transaction Timeout, in seconds This parameter defines how long the device waits for the cardholder to take action on any cardholder input, for example, when waiting for the cardholder to present payment after the host starts the transaction. 0x00 = No timeout 0x01 to 0xFF = 1 to 255 seconds                      | B   | R   |         |
| A3  | var | Reader Options The parameters inside this TLV data object allow the host to enable and disable the various payment method interfaces.                      | T   | O   |         |
| /81 | 01  | Magnetic Stripe Reader Mode (MSR Only) 0x00 = Disabled 0x01 = EMV 0x80 = Non-EMV (disables other readers) (MAGTEK INTERNAL ONLY FOR NOW)                                                  | B   | O   | 0x01    |
| /82 | 01  | Contact Reader Mode (EMV Contact Only) 0x00 = Disabled 0x01 = EMV                                          | B   | O   | 0x01    |
| /83 | 01  | Contactless Reader Mode (EMV Contactless Only) 0x00 = Disabled 0x01 = EMV 0x02 = NFC 0x03 = EMV and NFC Enable NFC only when non-payment tags are to be detected.                 | B   | O   | 0x01    |
| /84 | 03  | Manual Entry Mode (Touch Only) Populate this parameter to enable manual card entry. When using this feature, all other Reader Mode parameters must be set to **Disabled**.  Byte 1 Card Number Valid Format 0x00 = PAN min 8, max 21 digits  Byte 2 User Interface Sequence 0x00 = Based on the setting of **Property 1.2.1.1.5.1 MCE Mode Setting**  Byte 3 Beeper Feedback 0x00 = On keypress sound disabled 0x01 = On keypress sound enabled                                              | B   | O   |         |
| /85 | 02  | Barcode Reader Mode (BCR Only) Populate this parameter to enable the device’s barcode reader. This feature can be enabled alongside all other reader modes except Manual Entry Mode.  Byte 1 Barcode Reader Enable 0x00 = Disabled 0x01 = Enabled  Byte 2 Encrypt Non-EMV Barcode Data 0x00 = Disabled 0x01 = Enabled                       | B   | O   | 0x0000  |
| /86 | 01  | PIN Block Format (Touch Only) 0x00 = ISO Format 0 0x03 = ISO Format 3 0x04 = ISO Format 4  | B   | O   | 0x00    |
| A4  | var | Tip and Tax Options                    | B   | O   |         |
| /81 | 1F  | Byte 1 Tip Mode 0x00 – Disable Tip Mode 0x01 – Show Tip GUI immediately using % value 0x02 – Show Tip GUI immediately using \$ amount  0x11 - Enable Read Channel(s), with +Tip Button, %value 0x12 - Enable Read Channel(s), with +Tip Button, \$ Amount  For Tip Modes 0x01 and 0x02, the Tip GUI is shown immediately with selected read channels disabled. They get enabled after the Tip information are entered.  For Tip Modes 0x11 and 0x12, the read channels are enabled and “+Tip” button is shown. If no tip is desired, just present the card. If “+Tip” button is selected, read channels are first disabled, then show the Tip GUI.  Byte 2, Display Mode for Button1 0 - % or Amount 1 – Display Custom 2 – Display NO TIP 3 – Disabled (An OID controls whether the button is blank, grayed out or not showing, see **Property 1.1.1.1.2.5 Disabled Tip Button Display Mode (Touch Only)**)  Bytes 3 to 6 Value in % or Amount for Button 1, if applicable  Byte 7, Display Mode for Button 2 (See Byte 2 for Details) Bytes 8 to 11 Value in % or Amount for Button 2, if applicable  Byte 12, Display Mode for Button 3 (See Byte 2 for Details) Bytes 13 to 16 Value in % or Amount for Button 3, if applicable  Byte 17, Display Mode for Button 4 (See Byte 2 for Details) Bytes 18 to 21 Value in % or Amount for Button 4, if applicable  Byte 22, Display Mode for Button 5 (See Byte 2 for Details) Bytes 23 to 26 Value in % or Amount for Button 5, if applicable  Byte 27, Display Mode for Button 6 (See Byte 2 for Details) Bytes 28 to 31 Value in % or Amount for Button 6, if applicable  **See Property 1.1.1.1.2.2 Tip Mode(Touch Only) for a suggested default value**   | B   | O   |         |
| /82 | 06  | Tax or Surcharge Amount to Display See **Property 1.1.1.1.2.4 Display Tax or Surcharge (Touch Only)** to configure display Tax or Surcharge                                          | B   | O   |         |
| 84  | 02  | Transaction Options This parameter is a bitmask (ORed bits) that sets various device behaviors that change the transaction flow or the way the device reports transaction results, as follows:  Byte 1 Apple VAS Mode (**Apple / Google VAS Only, set to 0 if not supported**)  Bits 0, 1 0x00 = **Apple/Google VAS Support Disabled** 0x01 = **VAS App OR Payment Mode (Single Mode)**. The device reads only Apple/Google VAS data from a tapped smartphone, or reads EMV payment data from a tapped card. When the device sends ARQC to conclude the transaction, it only includes either EMV payment data in container FC for cards, or includes VAS data in container FE for smartphones 0x02 = **VAS App and Payment Mode (Dual Mode)**. The device reads both Apple/Google VAS data and EMV payment data from a tapped smartphone, or reads EMV payment data from a tapped card. When device sends ARQC to the host to conclude the transaction, it includes EMV payment data in container FC and includes VAS data, if available, in container FE 0x03 = **VAS App Only Mode (VAS Mode)**. The device reads only Apple/Google VAS data from a tapped smartphone, and does not read data from a tapped card. If the tapped smartphone does not support VAS, the device does not detect or read from the smartphone. When the device send ARQC to conclude the transaction, it includes VAS data in container FE and does not include EMV payment data in container FC 0x04 = **Payment Only Mode (Payment Mode)**. The device operates the same as EMV mode (01). It reads only EMV payment data from a tapped smartphone or a tapped card. When the device sends ARQC to conclude the transaction, it includes EMV payment data in container FC and does not include VAS data in container FE.   Bits 4, 5, 6 Wallet Mode 4 -Apple 5 - Google 6 - Reserved 0x000 = Wallet Support Disabled 0x001 = Apple VAS Enable  0x002 = Google VAS Enabled  0x003 = –Apple and Google VAS Enabled  Bit 7 Apple VAS Protocol Mode o Value 0 – URL VAS Protocol o Value 1 – FULL VAS Protocol  Byte 2 Transaction Flow Control Bit 0 Transaction Flow Value 1 = Quick Chip Transaction Flow Value 0 = EMV Transaction Flow Bit 1 Response Format Value 1 = DynaPro Response Format. For sending ARQC data and batch data, the device uses **EMV ARQC (DynaPro Format) Type** and **EMV Batch Data (DynaPro Format) Type**. Value 0 = Reserved. Bit 2 Signature Capture Control (MSR Only). Value 1 = Skip Signature Capture On Service Code. The device skips signature capture during an MSR-only transaction if the card’s service code indicates it is a chip card.  Value 0 = Do Not Skip Signature Capture. Bit 3 Display Amount for Quick Chip Transaction Flow Value 1 = Display Amount Value 0 = Do not Display Amount | B   | O   | 0x0003  |
| 86  | var | Transaction TLV This is a list of self-contained TLV data objects that defines the basic parameters for the transaction. It may contain any of the following tags in the formats defined in the **EMV 4.3** specification or payment brand specifications, but at minimum it must contain 9C and 9F02, plus 9F03 if the transaction includes cash back. This parameter is optional for Manual Card Entry; to show a transaction amount when using Manual Card Entry, include 9F02 and 5F2A: 9C Transaction Type 9F02 Amount Authorized. If the **Transaction Flow** parameter specifies **Quick Chip Transaction Flow**, the host must specify a non-zero amount. 9F03 Amount Other 9F7C Merchant Custom Data 5F2A Transaction Currency Code 5F36 Transaction Currency Exponent 9F53 Transaction Category Code 9F15 Merchant Category Code 9F16 Merchant ID    | B   | R/O |         |
| A8  | 00  | (MAGTEK INTERNAL ONLY FOR NOW) Tag Lists | O   |         |
| 8A  |     | (MAGTEK INTERNAL ONLY FOR NOW) Notification Options ?? |     |     |         |
| AC  | var | User Interface Options             | T   | O   | null    |
| /81 | 00  | Suppress Thank You Message By default, devices with a display signal the end of a transaction by briefly showing “THANK YOU,” then “WELCOME.” The host can include this parameter to direct the device to suppress the “THANK YOU” message during this transaction.                                                                                                                                                                                                                            | T   | O   | null    |
| /82 | 01  | Override Final Transaction Message By default, devices with a display signal the end of a transaction by returning to the idle page and showing “WELCOME.” The host can include this parameter to direct the device to show a different message, chosen from the list of available Display String IDs in section **4.3 Display Strings**. This option completely overrides the device’s idle page behavior until the next transaction, power cycle, or other similar state change.             | B   | O   | null    |
| /83 | 02  | Functional button Right option. String ID = Enable the present card page with a green functional button Right – label with a String ID associates with a configured String message. See  **Table 354 – Default User Interface String IDs and Strings.** This button can fit about 15 characters. When user presses this button, device sends notification to the host to indicate the present card functional button Right is pressed. See **Notification 0x1803 - User Interface Host Action Request**  If host wants to disable this button, do not include this tag.
          | B   | O   | null    |

End of any wrappers, at minimum including Request Message found on page 58
