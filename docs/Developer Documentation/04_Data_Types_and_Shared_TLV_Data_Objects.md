---
title: Data Types and Shared TLV Data Objects
layout: home
parent: DynaFlex Family Programmer's Manual
nav_order: 4
---
---

  - [Data Types and Shared TLV Data Objects](#data-types-and-shared-tlv-data-objects)
    - [Primitive Data Types](#primitive-data-types)
    - [About Track Data](#about-track-data)
    - [Display Strings](#display-strings)
    - [Encryption Type](#encryption-type)
    - [EMV ARQC Type](#emv-arqc-type)
    - [EMV ARPC Type](#emv-arpc-type)
    - [EMV Batch Data Type](#emv-batch-data-type)
    - [EMV Terminal Configuration File Type](#emv-terminal-configuration-file-type)
    - [EMV Processing Configuration File Type](#emv-processing-configuration-file-type)
    - [EMV Entry Point Configuration File Type](#emv-entry-point-configuration-file-type)
    - [EMV Configuration CA Public Keys File Type](#emv-configuration-ca-public-keys-file-type)
    - [EMV American Express DRL Configuration File Type (Not Supported on Expresspay 4.x)](#emv-american-express-drl-configuration-file-type-not-supported-on-expresspay-4x)
    - [Signature Capture File Type (Touch Only)](#signature-capture-file-type-touch-only)
    - [Security Operation Type](#security-operation-type)
    - [Security Parameters Type](#security-parameters-type)
    - [Key Information Type](#key-information-type)
    - [NFC UID Type (EMV Contactless Only)](#nfc-uid-type-emv-contactless-only)
    - [GPO Response Type (EMV Contactless Only)](#gpo-response-type-emv-contactless-only)
    - [TR-31 Key Block Type](#tr-31-key-block-type)
    - [Miniature Certificate Type (MAGTEK INTERNAL ONLY)](#miniature-certificate-type-magtek-internal-only)
    - [Firmware File Type (MAGTEK INTERNAL ONLY)](#firmware-file-type-magtek-internal-only)
    - [TrackType Type (MAGTEK INTERNAL ONLY FOR NOW)](#tracktype-type-magtek-internal-only-for-now)
    - [CardData Type (MAGTEK INTERNAL ONLY FOR NOW)](#carddata-type-magtek-internal-only-for-now)
    - [TagsType Type (MAGTEK INTERNAL ONLY FOR NOW)](#tagstype-type-magtek-internal-only-for-now)
    - [TLVType Type (MAGTEK INTERNAL ONLY FOR NOW)](#tlvtype-type-magtek-internal-only-for-now)
    - [Common File Structure](#common-file-structure)
    - [Certificate File Types](#certificate-file-types)
    - [Certificate Signing Request (CSR) File Types](#certificate-signing-request-csr-file-types)
    - [UI Configuration File Type (MAGTEK INTERNAL ONLY)](#ui-configuration-file-type-magtek-internal-only)
    - [Card Emulation](#card-emulation)

---


## Data Types and Shared TLV Data Objects

This section describes the primitive and composed data types referred to
throughout this document.

### Primitive Data Types

TLV data objects use the following primitive data types:

- A = Alphabetic (string, no numbers).

- AN = Alphanumeric (string).

- B = Binary value, which includes bit combinations (“OR” types).

- CN = Compressed numeric, as defined by ***EMV 4.3 Book 3***, section
  ***Data Element Format Conventions***.

- N = Numeric, as defined by ***EMV 4.3 Book 3***, section ***Data
  Element Format Conventions***.

- T = TLV **Constructed** data object (TLV Value contains additional
  layers of TLV-encoded data the parser should continue to process).

### About Track Data

After the host receives and decrypts **EMV ARQC Type** data or
**Merchant Data Container** data from the device, it may need to parse
each track into individual values embedded in the tracks. The device can
read multiple card formats, which vary even between different issuers
and payment brands using the same underlying standards. Describing all
possible formats is beyond the scope of this document, but this section
describes how to parse data from tracks 1, 2, and 3 in a generic ISO/ABA
compliant format as an example.

**Table 16** shows an example of ISO/ABA track data the device sends to
the host, using unmasked placeholder numbers to make it easier to see
the relative positions of the values embedded in the track data. It is
important to note that some cards do not include Track 3 data. Manually
entered data does not include Track 3.

Table 16 - Example Generic ISO/ABA Track Data Format

| Generic ISO/ABA Track Data Format |  |
|----|----|
| Track 1 Data | %75555555555555555^CARDHOLDER NAME/^33338880004444000006? |
| Track 2 Data | ;5555555555555555=33338880004444006? |
| Track 3 Data | ;5555555555555555=333388800044440000006? |

The example track data in **Table 16** can be interpreted as follows:

- The **%**, **?**, and **;** are Sentinels / delimiters, and are taken
  directly from the data on the card.

- The **7** at the beginning of Track 1 data is the card format code.
  For swiped credit / debit cards, this comes from the card and is
  generally **B**. Manually entered data uses **M**.

- The string of **5**s is the Account Number / License Number / PAN.

- The carets **^** are a standard ISO track 1 delimiter surrounding the
  Cardholder Name.

- **CARDHOLDER NAME/** is the Cardholder Name. Manually entered data
  uses string literal **MANUAL ENTRY/**.

- The string of **3**s is the Expiration Date (YYMM).

- The string of **8**s is the Service Code. For swiped credit / debit
  cards, this comes from the card. Manually entered data uses **000**.

- The remaining characters (**0**s, **4**s, and **6**) are Discretionary
  Data. For swiped debit / credit cards this data is of varying length
  and content and comes from the card, and must be interpreted according
  to the standards established by issuers, payment brands, and so on.
  Manually entered track data uses a MagTek standard for Discretionary
  Data as follows:

  - The string of **4**s is the CVV2 a cardholder or operator entered on
    the keypad. This may be 3 or 4 characters long and is not padded, so
    the host software must find it by using the fixed-length padding and
    sentinels that surround it.

  - The strings of **0**s are literals of fixed length: Track 1 has
    three zeroes after the Service Code, and five zeroes after the CVV2;
    Track 2 has three zeroes after the Service Code, and two zeroes
    after CVV2.

  - The **6** contains either a 0 or a 1. This Field Option tells what
    data is included in the track data, where **0 = Acct, Date, CVV**
    and **1 = Name on Card, Acct, Date, CVV**.

### Display Strings

The Display Strings type provides a pre-defined set of messages by
string ID that the host and device use for various user interface
features.

Table 17 - Display String IDs and Strings

| Display String ID | Display String (en-US)               |
|-------------------|--------------------------------------|
| 0x00              | Reserved, do not use.                |
| 0x01              | “AMOUNT”                             |
| 0x02              | “AMOUNT OK?”                         |
| 0x03              | “APPROVED”                           |
| 0x04              | “CALL YOUR BANK”                     |
| 0x05              | “CANCEL OR ENTER”                    |
| 0x06              | “CARD ERROR”                         |
| 0x07              | “DECLINED”                           |
| 0x08              | “ENTER AMOUNT”                       |
| 0x09              | Reserved, do not use.                |
| 0x0A              | Reserved, do not use.                |
| 0x0B              | “INSERT CARD”                        |
| 0x0C              | “NOT ACCEPTED”                       |
| 0x0D              | Reserved, do not use.                |
| 0x0E              | “PLEASE WAIT”                        |
| 0x0F              | “PROCESSING ERROR”                   |
| 0x10              | “REMOVE CARD”                        |
| 0x11              | “USE CHIP READER”                    |
| 0x12              | “USE MAGSTRIPE”                      |
| 0x13              | “TRY AGAIN”                          |
| 0x14              | “WELCOME”                            |
| 0x15              | “PRESENT CARD”                       |
| 0x16              | “PROCESSING”                         |
| 0x17              | “CARD READ OK - REMOVE CARD”         |
| 0x18              | “INSERT OR SWIPE CARD”               |
| 0x19              | “PRESENT ONE CARD ONLY”              |
| 0x1A              | “APPROVED PLEASE SIGN”               |
| 0x1B              | “AUTHORIZING PLEASE WAIT”            |
| 0x1C              | “INSERT, SWIPE, OR TRY ANOTHER CARD” |
| 0x1D              | “PLEASE INSERT CARD”                 |
| 0x1E              | Null prompt (empty screen)           |
| 0x1F              | Reserved, do not use.                |
| 0x20              | “SEE PHONE”                          |
| 0x21              | “PRESENT CARD AGAIN”                 |
| 0x22              | “INSERT/SWIPE/TRY OTHER CARD”        |
| 0x23              | “TAP or SWIPE CARD”                  |
| 0x24              | “TAP or INSERT CARD”                 |
| 0x25              | “TAP, INSERT or SWIPE CARD”          |
| 0x26              | “TAP CARD”                           |
| 0x27              | “TIMEOUT”                            |
| 0x28              | “TRANSACTION TERMINATED”             |
| 0x29              | “USE CHIP READER or MAGSTRIPE”       |
| 0x2A              | “SCAN BARCODE”                       |
| 0x2B              | “BARCODE READ SUCCESSFULLY”          |
| 0x2C              | “CANCELED”                           |
| 0x2D              | “SWIPE CARD or SCAN BARCODE”         |
| 0x2E              | “INSERT CARD or SCAN BARCODE”        |
| 0x2F              | “INSERT, SWIPE or SCAN BARCODE”      |
| 0x30              | “TAP CARD or SCAN BARCODE”           |
| 0x31              | “TAP, SWIPE or SCAN BARCODE”         |
| 0x32              | “TAP, INSERT or SCAN BARCODE”        |
| 0x33              | “TAP, INSERT, SWIPE or SCAN BARCODE” |
| 0x34              | “TRY ANOTHER INTERFACE”              |
| 0x35              | “NFC TAG DETECTED”                   |
| 0x36              | “ERROR REMOVE CARD”                  |
| 0x37              | “MIFARE CLASSIC 1K DETECTED”         |
| 0x38              | “MIFARE CLASSIC 4K DETECTED”         |
| 0x39              | “MIFARE DESFIRE DETECTED”            |

### Encryption Type

The Encryption Type provides the key type, variant, and other
information the host can use to decrypt encrypted data included in
various payloads. The possible values are an ORed bitmask using the
following elements:

- 0xxx xxxx = Fixed Key (Not used)

- 1xxx xxxx = DUKPT Key

- xx00 xxxx = TDES

- xx01 xxxx = AES128

- xx10 xxxx = AES256

- xxxx 0000 = Data Encrypt/Decrypt Variant

- xxxx 0001 = PIN Variant

- xxxx 0010 = MAC Variant

- xxxx 0011 = Data, Encrypt Variant

- xxxx 0100 = MAC Verify Variant

- xxxx 0101 = RESERVED

- xxxx 0110 = RESERVED

- xxxx 0111 = AES PIN Encrypt

- xxxx 1000 = AES MAC Generate

- xxxx 1001 = AES MAC Verify

- xxxx 1010 = AES MAC Generate/Verify

- xxxx 1011 = AES Data Encrypt

- xxxx 1100 = AES Data Decrypt

- xxxx 1101 = AES Data Encrypt/Decrypt

- xxxx 1110 = RESERVED

- xxxx 1111 = RESERVED

### EMV ARQC Type

The device formats ARQC messages as shown in **Table 18**. The default
is an EMV standard list of ARQC message tags. The host may also
customize the contents of ARQC messages by setting **Property
1.1.1.1.1.2 EMV ARQC Message Tag List**.

#### EMV ARQC (DynaPro Format) Type

Table 18 - EMV ARQC (DynaPro Format) Type

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
<td colspan="6">2-byte MSB message length excluding padding and
CBC-MAC</td>
</tr>
<tr>
<td>F9</td>
<td>var</td>
<td>Container for MAC structure and generic data</td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF54</td>
<td>var</td>
<td>MAC KSN</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF55</td>
<td>01</td>
<td><p>MAC Encryption Type</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
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
<td>/FA</td>
<td>var</td>
<td>Container for generic data</td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//70</td>
<td>var</td>
<td>Container for ARQC</td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>///82</td>
<td>02</td>
<td><p>Application Interchange Profile</p>
<p>Available on:</p>
<p>DynaProx FW Ver A8 or newer</p>
<p>DynaFlex II FW Ver A6 or newer</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///9F6E</td>
<td>var</td>
<td><p>Third Party Data</p>
<p>Available on:</p>
<p>DynaProx FW Ver A8 or newer</p>
<p>DynaFlex II FW Ver A6 or newer</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///DFDF53</td>
<td>01</td>
<td><p>Fallback Indicator</p>
<ul>
<li><p>0x00 = No Fallback</p></li>
<li><p>0x01 = Technical Fallback</p></li>
<li><p>0x81 = MSR Fallback</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>///DFDF33</td>
<td>var</td>
<td><p>Masked Track 2 MSR Data</p>
<p>If the payment method presented by the cardholder provides
it</p></td>
<td>AN</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///DFDF4D</td>
<td>var</td>
<td><p>Masked Track 2 ICC Data</p>
<p>If the payment method presented by the cardholder provides
it</p></td>
<td>AN</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///DFDF52</td>
<td>01</td>
<td><p>Card Type</p>
<ul>
<li><p>0x00 = Other</p></li>
<li><p>0x01 = Magnetic Stripe ISO/ABA Financial (MSR)</p></li>
<li><p>0x02 = Magnetic Stripe AAMVA (MSR)</p></li>
<li><p>0x03 = Manual Entry</p></li>
<li><p>0x04 = Unknown</p></li>
<li><p>0x05 = Contact Chip Card (ICC)</p></li>
<li><p>0x06 = Contactless Chip Card (PICC), EMV</p></li>
<li><p>0x07 = MSR Financial and Contact Chip Card (ICC)</p></li>
<li><p>0x08 = Contactless PICC, Magnetic Stripe Data (MSD)</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>///FF42</td>
<td>var</td>
<td><p>Container for Selectable Encrypted Card Data</p>
<p>Set up OID 1.1.2.6.1.1 to enable this container.</p></td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>////DFDFDF37</td>
<td>var</td>
<td><p>Selectable Encrypted Data Primitive</p>
<p>Decrypt the value of this TLV data object using the algorithm and
variant specified in the <strong>Selectable Encrypted Data KSN</strong>
parameter and the <strong>Selectable Encrypted Data Encryption
Type</strong> parameter. See <strong>Table 20 - EMV ARQC (DynaPro
Format) DFDFDF37 Decrypted Contents</strong> for the data structure as
it should appear after decryption.</p>
<p>(This item will be present if 0xFF42 is enabled)</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>////DFDFDF38</td>
<td>0C</td>
<td><p>Selectable Encrypted Data KSN</p>
<p>(This item will be present if 0xFF42 is enabled)</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>////DFDFDF39</td>
<td>01</td>
<td><p>Selectable Encrypted Data Encryption Type</p>
<p>(This item will be present if 0xFF42 is enabled)</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///DF2A</td>
<td>06</td>
<td>Tip Mode Sale Amount Entered</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///DF2B</td>
<td>06</td>
<td>Tip Mode Total Amount</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///DF5D</td>
<td>06</td>
<td>Tip Amount</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///DF5E</td>
<td>06</td>
<td>Tax Amount</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///F8</td>
<td>var</td>
<td>Container for Encrypted Data</td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>////DFDF59</td>
<td>var</td>
<td><p>Encrypted Data Primitive</p>
<p>Decrypt the value of this TLV data object using the algorithm and
variant specified in the <strong>Encrypted Transaction Data KSN</strong>
parameter and the <strong>Encrypted Transaction Data Encryption
Type</strong> parameter to read its contents. See <strong>Table
19</strong> on page <a href="#_Ref36484046"><strong>39</strong></a> for
the data structure as it should appear after decryption.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>////DFDF56</td>
<td>var</td>
<td>Encrypted Transaction Data KSN</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>////DFDF57</td>
<td>01</td>
<td><p>Encrypted Transaction Data Encryption Type</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>////DFDF58</td>
<td>01</td>
<td><p>Number of Padding Bytes</p>
<p>Number of bytes added to DFDF59 value to force its length to a
multiple of 8 bytes for TDES, or 16 bytes for AES.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/FE</td>
<td>Var</td>
<td><p>VAS Data Container</p>
<p>See <strong>Table 24 – VAS Data Container Payload</strong></p></td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/FF40</td>
<td>Var</td>
<td><p>Fleet Data Container (Common Kernel Only)</p>
<p>See <a href="#OLE_LINK1"><strong>Table 4.5 9 – Fleet Data Container
Payload</strong></a></p></td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td colspan="6">Padding to ensure the length of data, starting with the
message length at the very beginning, and ending with any additional
padding, is a multiple of 8 bytes for TDES, or 16 bytes for AES. This is
a requirement of using the CBC-MAC algorithm.</td>
</tr>
<tr>
<td colspan="6">Four-byte CBC-MAC. The host should calculate the CBC-MAC
and verify that it matches. For details about calculating a CBC-MAC, see
<strong>About Message Authentication Codes (MAC)</strong>.</td>
</tr>
</tbody>
</table>

The device encrypts the value inside the **Encrypted Data Primitive**
container using the **Encrypted Transaction Data Encryption Type**
parameter and working key associated with the keyset number currently
active in the device’s configuration. As a requirement for using DUKPT
encryption algorithms, the device pads it so the length of its value is
a multiple of 8 bytes for TDES, or 16 bytes for AES. The device uses
container DFDF58 to report how many bytes of data object DFDF59 are
padding. Data object DFDF59 itself is formatted like **Table 19** after
the host decrypts it.

<span id="_Ref36484046" class="anchor"></span>Table 19 - EMV ARQC
(DynaPro Format) DFDF59 Decrypted Contents

<table style="width:100%;">
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
<td><p>Decrypted Data Container</p>
<p>Inside this container, the device inserts all EMV TLV data objects
specified by the setting in <strong>Property 1.1.1.1.1.2 EMV ARQC
Message Tag List</strong>. The remainder of this table shows the basic
structure and content of MagTek custom tags. For definitions of all
other standard EMV tags that can be included directly under container
FC, see <em><strong>EMV 4.3 Book 3</strong></em>.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DF29</td>
<td>08</td>
<td><p>Only if tag DF29 is included in <strong>Property 1.1.1.1.1.2 EMV
ARQC Message Tag List</strong>.</p>
<p>Outcome Parameter Set</p>
<p>Byte 1 - Outcome</p>
<p>0x10 = Approved</p>
<p>0x20 = Declined</p>
<p>0x30 = Online Request</p>
<p>0x40 = End Application</p>
<p>0x50 = Select Next Application</p>
<p>0x60 = Try Another Interface</p>
<p>0x70 = Try Again</p>
<p>0xF0 = N/A</p>
<p>Byte 2 – Entry Point Start</p>
<p>0x00 = Start A</p>
<p>0x10 = Start B</p>
<p>0x20 = Start C</p>
<p>0x30 = Start D</p>
<p>0xF0 = N/A</p>
<p>Byte 3 – Entry Point Online Response</p>
<p>0x00 = EMV Data</p>
<p>0x10 = Any</p>
<p>0xF0 = N/A</p>
<p>Byte 4 – CVM</p>
<p>0x00 = No CVM</p>
<p>0x10 = Obtain Signature</p>
<p>0x20 = Online PIN</p>
<p>0x30 = Confirmation Code Verified</p>
<p>0xF0 = N/A</p>
<p>Byte 5 – UI/Data/Receipt</p>
<p>0x80 = UI Request on Outcome Present</p>
<p>0x40 = UI Request on Restart Present</p>
<p>0x20 = Data Record Present</p>
<p>0x10 = Discretionary Data Present</p>
<p>0x08 = Provide Receipt</p>
<p>Byte 6 – Alternate Interface Preference</p>
<p>0x10 = Contact</p>
<p>0x20 = MSR</p>
<p>0xF0 = N/A</p>
<p>Byte 7 – Field Off Request</p>
<p>FF = N/A</p>
<p>Byte 8 – Removal Timeout</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/F4</td>
<td>var</td>
<td>Container for encrypted MSR data (MSR Only)</td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF36</td>
<td>01</td>
<td><p>Encrypted Track 1 Status (MSR Only)</p>
<ul>
<li><p>0x00 = OK</p></li>
<li><p>0x01 = Empty</p></li>
<li><p>0x02 = Error</p></li>
<li><p>0x03 = Disabled</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF37</td>
<td>var</td>
<td>Encrypted Track 1 Data (MSR Only)</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF38</td>
<td>01</td>
<td><p>Encrypted Track 2 Status (MSR Only)</p>
<ul>
<li><p>0x00 = OK</p></li>
<li><p>0x01 = Empty</p></li>
<li><p>0x02 = Error</p></li>
<li><p>0x03 = Disabled</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF39</td>
<td>var</td>
<td>Encrypted Track 2 Data (MSR Only)</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF3A</td>
<td>01</td>
<td><p>Encrypted Track 3 Status (MSR Only)</p>
<ul>
<li><p>0x00 = OK</p></li>
<li><p>0x01 = Empty</p></li>
<li><p>0x02 = Error</p></li>
<li><p>0x03 = Disabled</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF3B</td>
<td>var</td>
<td>Encrypted Track 3 Data (MSR Only)</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF3C</td>
<td>var</td>
<td><p>Encrypted MagnePrint Data (MSR Only)</p>
<p>Only included for MSR swipe transactions and when Track Data and
Magneprint are using the same KSN.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF43</td>
<td>04</td>
<td><p>MagnePrint Status Data (MSR Only)</p>
<p>Only included for MSR swipe transactions and when Track Data and
Magneprint are using the same KSN.</p>
<ul>
<li><p>Bit 0 = MagnePrint Capable Flag</p>
<ul>
<li><p>0 = Device is not MagnePrint capable</p></li>
<li><p>1 = Device is MagnePrint capable</p></li>
</ul></li>
<li><p>Bits 1 through 3 = Mode</p>
<ul>
<li><p>0 = Standard MagnePrint</p></li>
<li><p>1 = Extended MagnePrint</p></li>
</ul></li>
<li><p>Bits 4 through 15 = ASIC Revision</p></li>
<li><p>Bit 16 = Reserved</p></li>
<li><p>Bit 17 = Reserved</p></li>
<li><p>Bit 18 = Swipe too slow</p></li>
<li><p>Bit 19 = Swipe too fast</p></li>
<li><p>Bit 20 = Reserved</p></li>
<li><p>Bit 21 = Card swipe direction</p>
<ul>
<li><p>0 = Forward</p></li>
<li><p>1 = Reverse</p></li>
</ul></li>
</ul>
<p>Bits 22..31 = Reserved</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF50</td>
<td>var</td>
<td><p>MSR KSN Data (MSR Only)</p>
<p>Key Serial Number for the key the host should use to decrypt
<strong>Encrypted Track 1 Data</strong>, <strong>Encrypted Track 2
Data</strong>, <strong>Encrypted Track 3 Data</strong> and
<strong>Encrypted MagnePrint Data</strong>.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF51</td>
<td>01</td>
<td><p>MSR Encryption Type (MSR Only)</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/FF73</td>
<td>var</td>
<td><p>Container for Encrypted MagnePrint Data (MSR Only)</p>
<p>Only included when Track Data and MagnePrint encryption keys are
using different KSN</p></td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF3C</td>
<td>var</td>
<td><p>Encrypted MagnePrint Data (MSR Only)</p>
<p>Only included for MSR swipe transactions.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF43</td>
<td>04</td>
<td><p>MagnePrint Status Data (MSR Only)</p>
<p>Only included for MSR swipe transactions.</p>
<ul>
<li><p>Bit 0 = MagnePrint Capable Flag</p>
<ul>
<li><p>0 = Device is not MagnePrint capable</p></li>
<li><p>1 = Device is MagnePrint capable</p></li>
</ul></li>
<li><p>Bits 1 through 3 = Mode</p>
<ul>
<li><p>0 = Standard MagnePrint</p></li>
<li><p>1 = Extended MagnePrint</p></li>
</ul></li>
<li><p>Bits 4 through 15 = ASIC Revision</p></li>
<li><p>Bit 16 = Reserved</p></li>
<li><p>Bit 17 = Reserved</p></li>
<li><p>Bit 18 = Swipe too slow</p></li>
<li><p>Bit 19 = Swipe too fast</p></li>
<li><p>Bit 20 = Reserved</p></li>
<li><p>Bit 21 = Card swipe direction</p>
<ul>
<li><p>0 = Forward</p></li>
<li><p>1 = Reverse</p></li>
</ul></li>
</ul>
<p>Bits 22..31 = Reserved</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF50</td>
<td>var</td>
<td><p>MSR KSN Data (MSR Only)</p>
<p>Key Serial Number for the key the host should use to decrypt
<strong>Encrypted MagnePrint Data</strong>.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF51</td>
<td>01</td>
<td><p>MSR Encryption Type (MSR Only)</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/F5</td>
<td>var</td>
<td><p>Container for Encrypted PIN Data (Touch Only)</p>
<p>Contains ISO PIN Block formatted data in the nested <strong>Encrypted
PIN Data</strong> object, plus supporting information to decrypt it. The
host should use the current PIN DUKPT working key specified in the
supporting information.</p></td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DF71</td>
<td>01</td>
<td><p>PIN Block Format (Touch Only)</p>
<ul>
<li><p>0x00 = ISO Format 0</p></li>
<li><p>0x01 = ISO Format 1</p></li>
<li><p>0x03 = ISO Format 3</p></li>
<li><p>0x04 = ISO Format 4</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//99</td>
<td>08</td>
<td>Encrypted PIN Data (Touch Only)</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF41</td>
<td>var</td>
<td>PIN KSN Data (Touch Only)</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF42</td>
<td>01</td>
<td><p>PIN Encryption Type (Touch Only)</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td colspan="6">Padding to force DFDF59 plus padding to be a multiple of
8 bytes</td>
</tr>
</tbody>
</table>

**Table 20 - EMV ARQC (DynaPro Format) DFDFDF37 Decrypted Contents**

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
<td><p>Decrypted Data Container</p>
<p>Inside this container, the device inserts EMV TLV data objects
specified by the setting in Property 1.1.1.1.1.2 EMV ARQC Message Tag
List. If the data is not available for a given selected card data, the
tag will still get transmitted with a length of ‘1’ and value =
‘*’.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/5F20</td>
<td>var</td>
<td><p>Only if Byte 0 – Bit 0 is set in Property 1.1.2.6.1.1 Selectable
Card Data Encryption Enable.</p>
<p>Cardholder Name</p></td>
<td>an</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/5F24</td>
<td><p>02/</p>
<p>03</p></td>
<td><p>Only if Byte 0 – Bit 2 is set in Property 1.1.2.6.1.1 Selectable
Card Data Encryption Enable.</p>
<p>Expiration Date, YYMM or YYMMDD</p></td>
<td><p>n4/</p>
<p>n6</p></td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/5F30</td>
<td>02</td>
<td><p>Only if Byte 0 – Bit 3 is set in Property 1.1.2.6.1.1 Selectable
Card Data Encryption Enable.</p>
<p>Service Code</p></td>
<td>n3</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/9F1F</td>
<td>var</td>
<td><p>Only if Byte 0 – Bit 4 is set in Property 1.1.2.6.1.1 Selectable
Card Data Encryption Enable.</p>
<p>T1 Discretionary Data</p></td>
<td>an</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/9F20</td>
<td>var</td>
<td><p>Only if Byte 0 – Bit 5 is set in Property 1.1.2.6.1.1 Selectable
Card Data Encryption Enable.</p>
<p>T2 Discretionary Data</p></td>
<td>cn</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td colspan="6">Padding to force DFDFDF37 plus padding to be a multiple
of 16 bytes for AES encryption.</td>
</tr>
</tbody>
</table>

Table 21 – EMV ARQC Enhanced DFDF59 Decrypted Contents for EMV Data

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 5%" />
<col style="width: 0%" />
<col style="width: 57%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th colspan="2">Len</th>
<th>Value / Description</th>
<th>Typ</th>
<th>Req</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td>FC</td>
<td colspan="2">var</td>
<td><p>Decrypted Data Container</p>
<p>This contains all EMV TLV data objects specified in <strong>Property
1.1.1.1.1.2 EMV ARQC Message Tag List</strong>.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/FE</td>
<td>Var</td>
<td colspan="2"><p>VAS Data Container</p>
<p>See <strong>Table 24 – VAS Data Container Payload</strong></p></td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td colspan="7">Padding to ensure the length of data, starting with the
message length at the very beginning, and ending with any additional
padding, is a multiple of 8 bytes for TDES, or 16 bytes for AES. This is
a requirement of using the CBC-MAC algorithm.</td>
</tr>
</tbody>
</table>

Table 22 – EMV ARQC Enhanced DFDF59 Decrypted Contents for MSR and
MagnePrint Data

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 5%" />
<col style="width: 0%" />
<col style="width: 57%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th colspan="2">Len</th>
<th>Value / Description</th>
<th>Typ</th>
<th>Req</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td>FC</td>
<td colspan="2">var</td>
<td><p>Decrypted Data Container</p>
<p>Inside this container, the device inserts all EMV TLV data objects
specified by the setting in <strong>Property 1.1.1.1.1.2 EMV ARQC
Message Tag List</strong>. The remainder of this table shows the basic
structure and content of MagTek custom tags. For definitions of all
other standard EMV tags that can be included directly under container
FC, see <em><strong>EMV 4.3 Book 3</strong></em>.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/9F41</td>
<td colspan="2">04</td>
<td><p>Transaction Counter</p>
<p>Starts at 00000000 each time the device powers up or resets,
increments for each transaction.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF36</td>
<td colspan="2">01</td>
<td><p>MSR Track 1 Status</p>
<ul>
<li><p>0x00 = OK</p></li>
<li><p>0x01 = Empty</p></li>
<li><p>0x02 = Error</p></li>
<li><p>0x03 = Disabled</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/DF41</td>
<td colspan="2">var</td>
<td>MSR Track 1 Clear Text</td>
<td>AN</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/DFDF38</td>
<td colspan="2">01</td>
<td><p>MSR Track 2 Status</p>
<ul>
<li><p>0x00 = OK</p></li>
<li><p>0x01 = Empty</p></li>
<li><p>0x02 = Error</p></li>
<li><p>0x03 = Disabled</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/DF42</td>
<td colspan="2">var</td>
<td>MSR Track 2 Clear Text</td>
<td>AN</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/DFDF3A</td>
<td colspan="2">01</td>
<td><p>MSR Track 3 Status</p>
<ul>
<li><p>0x00 = OK</p></li>
<li><p>0x01 = Empty</p></li>
<li><p>0x02 = Error</p></li>
<li><p>0x03 = Disabled</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/DF43</td>
<td colspan="2">var</td>
<td>MSR Track 3 Clear Text</td>
<td>AN</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/DFDF43</td>
<td colspan="2">04</td>
<td><p>MagnePrint Status</p>
<p>The device only includes this if MSR and MagnePrint data are both
included in the transaction and the device is configured to encrypt them
using the same key, to avoid consuming two DUKPT keys encrypting
separate containers. If the device is configured to encrypt MSR and
MagnePrint data using different keys, it provides MagnePrint data in the
<strong>Container for Encrypted MagnePrint Data</strong> instead.</p>
<ul>
<li><p>Bit 0 = MagnePrint Capable Flag</p>
<ul>
<li><p>0 = Device is not MagnePrint capable</p></li>
<li><p>1 = Device is MagnePrint capable</p></li>
</ul></li>
<li><p>Bits 1 through 3 = Mode</p>
<ul>
<li><p>0 = Standard MagnePrint</p></li>
<li><p>1 = Extended MagnePrint</p></li>
</ul></li>
<li><p>Bits 4 through 15 = ASIC Revision</p></li>
<li><p>Bit 16 = Reserved</p></li>
<li><p>Bit 17 = Reserved</p></li>
<li><p>Bit 18 = Swipe too slow</p></li>
<li><p>Bit 19 = Swipe too fast</p></li>
<li><p>Bit 20 = Reserved</p></li>
<li><p>Bit 21 = Card swipe direction</p>
<ul>
<li><p>0 = Forward</p></li>
<li><p>1 = Reverse</p></li>
</ul></li>
<li><p>Bits 22..31 = Reserved</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/DF44</td>
<td colspan="2">var</td>
<td><p>MagnePrint Data</p>
<p>The device only includes this if MSR and MagnePrint data are both
included in the transaction and the device is configured to encrypt them
using the same key. The host can use this data in conjunction with
Magensa services to determine whether the swiped card is
authentic.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/FE</td>
<td>Var</td>
<td colspan="2"><p>VAS Data Container</p>
<p>See <strong>Table 24 – VAS Data Container Payload</strong></p></td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td colspan="7">Padding to ensure the length of data, starting with the
message length at the very beginning, and ending with any additional
padding, is a multiple of 8 bytes for TDES, or 16 bytes for AES. This is
a requirement of using the CBC-MAC algorithm.</td>
</tr>
</tbody>
</table>

Table 23 – EMV ARQC Enhanced DFDF59 Decrypted Contents for MagnePrint
Data

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 5%" />
<col style="width: 0%" />
<col style="width: 57%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th colspan="2">Len</th>
<th>Value / Description</th>
<th>Typ</th>
<th>Req</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td>FC</td>
<td colspan="2">var</td>
<td>Decrypted Data Container</td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF43</td>
<td colspan="2">var</td>
<td><p>MagnePrint Status</p>
<p>The device only includes this when MSR and MagnePrint data are
included in the transaction, but the device is configured to encrypt
them using a different key.</p>
<ul>
<li><p>Bit 0 = MagnePrint Capable Flag</p>
<ul>
<li><p>0 = Device is not MagnePrint capable</p></li>
<li><p>1 = Device is MagnePrint capable</p></li>
</ul></li>
<li><p>Bits 1..15 = Product revision &amp; mode</p></li>
<li><p>Bit 16 = Reserved</p></li>
<li><p>Bit 17 = Reserved for noise measurement</p></li>
<li><p>Bit 18 = Swipe too slow</p></li>
<li><p>Bit 19 = Swipe too fast</p></li>
<li><p>Bit 20 = Reserved</p></li>
<li><p>Bit 21 = Card swipe direction</p>
<ul>
<li><p>0 = Forward</p></li>
<li><p>1 = Reverse</p></li>
</ul></li>
<li><p>Bits 22..31 = Reserved</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DF44</td>
<td colspan="2">var</td>
<td><p>MagnePrint Data</p>
<p>The host can use this data in conjunction with Magensa services to
determine whether the swiped card is authentic.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DF4B</td>
<td colspan="2">var</td>
<td>MSR PAN</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/FE</td>
<td>Var</td>
<td colspan="2"><p>VAS Data Container</p>
<p>See <strong>Table 24 – VAS Data Container Payload</strong></p></td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td colspan="7">Padding to ensure the length of data, starting with the
message length at the very beginning, and ending with any additional
padding, is a multiple of 8 bytes for TDES, or 16 bytes for AES. This is
a requirement of using the CBC-MAC algorithm.</td>
</tr>
</tbody>
</table>

Table 24 – VAS Data Container Payload

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 6%" />
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
<td>/FE</td>
<td>var</td>
<td>VAS Data Container</td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//FF01</td>
<td>var</td>
<td>Apple VAS Container Slot 1 Container</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///9F27</td>
<td>var</td>
<td><p>VAS Data</p>
<p>Up to 128 bytes.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///9F2A</td>
<td>var</td>
<td><p>Mobile Token</p>
<p>Up to 36 bytes.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//FF02</td>
<td>var</td>
<td>Apple VAS Container Slot 2 Container</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///9F27</td>
<td>var</td>
<td><p>VAS Data</p>
<p>Up to 128 bytes.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///9F2A</td>
<td>var</td>
<td><p>Mobile Token</p>
<p>Up to 36 bytes.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//FF03</td>
<td>var</td>
<td>Apple VAS Container Slot 3 Container</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///9F27</td>
<td>var</td>
<td><p>VAS Data</p>
<p>Up to 128 bytes.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///9F2A</td>
<td>var</td>
<td><p>Mobile Token</p>
<p>Up to 36 bytes.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//FF04</td>
<td>var</td>
<td>Apple VAS Container Slot 4 Container</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///9F27</td>
<td>var</td>
<td><p>VAS Data</p>
<p>Up to 128 bytes.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///9F2A</td>
<td>var</td>
<td><p>Mobile Token</p>
<p>Up to 36 bytes.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//FF05</td>
<td>var</td>
<td>Apple VAS Container Slot 5 Container</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///9F27</td>
<td>var</td>
<td><p>VAS Data</p>
<p>Up to 128 bytes.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///9F2A</td>
<td>var</td>
<td><p>Mobile Token</p>
<p>Up to 36 bytes.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//FF06</td>
<td>var</td>
<td>Apple VAS Container Slot 6 Container</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///9F27</td>
<td>var</td>
<td><p>VAS Data</p>
<p>Up to 128 bytes.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///9F2A</td>
<td>var</td>
<td><p>Mobile Token</p>
<p>Up to 36 bytes.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//FF41</td>
<td>var</td>
<td>Google Smart Tap Container</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///FF01</td>
<td>var</td>
<td>Collector ID Slot 1 Container</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>////DF7B</td>
<td>var</td>
<td>Service Response NDEF Record</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///FF02</td>
<td>var</td>
<td>Collector ID Slot 2 Container</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>////DF7B</td>
<td>var</td>
<td>Service Response NDEF Record</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///FF03</td>
<td>var</td>
<td>Collector ID Slot 3 Container</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>////DF7B</td>
<td>var</td>
<td>Service Response NDEF Record</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///FF04</td>
<td>var</td>
<td>Collector ID Slot 4 Container</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>////DF7B</td>
<td>var</td>
<td>Service Response NDEF Record</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///FF05</td>
<td>var</td>
<td>Collector ID Slot 5 Container</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>////DF7B</td>
<td>var</td>
<td>Service Response NDEF Record</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///FF06</td>
<td>var</td>
<td>Collector ID Slot 6 Container</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>////DF7B</td>
<td>var</td>
<td>Service Response NDEF Record</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
</tbody>
</table>

<span id="OLE_LINK1" class="anchor"></span>Table 25 – Fleet Data
Container Payload (Common Kernel Only)

| Tag |  | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|----|
| /FF40 |  | var | Fleet Data Container | T | O |  |
| //DF30 |  | var | Prompting | B | O |  |
| //DF32 |  | var | Purchase Restrictions | B | O |  |
| //DF33 |  | var |  | B | O |  |
| //DF34 |  | var | Chip Offline purchase Restrictions for Fuel | B | O |  |
| //DF35 |  | var | Chip Offline purchase Restrictions for Non-fuel | B | O |  |
| //DF36 |  | var | Relationship Codes | B | O |  |
| //DF37 |  | var | 3<sup>rd</sup> Party Reference Data Generation 2 | B | O |  |
| //DF38 |  | var | Loyalty ID | B | O |  |
| //DF39 |  | var | Purchase Device Sequence Number | B | O |  |
| //DF40 |  | var | Generic Tag | B | O |  |
| //DF41 |  | var | Vehicle/Trailer Number | B | O |  |
| //DF42 |  | var | Vehicle Tag | B | O |  |
| //DF43 |  | var | Driver ID | B | O |  |
| //DF44 |  | var | Driver’s License Number | B | O |  |
| //DF45 |  | var | Driver’s License State/Province Abbreviation | B | O |  |
| //DF46 |  | var | Driver’s License Name Abbreviation | B | O |  |
| //DF47 |  | var | Date of Birth | B | O |  |
| //DF48 |  | var | Zip/Postal Code | B | O |  |
| //DF49 – //DF51 |  | var | IFSR Reserved for Future Use | B | O |  |
| //DF52 |  | var | Trailer Number | B | O |  |
| //DF53 |  | var | Employee Number | B | O |  |
| //DF54 |  | var | Work Order / Purchase Order Number | B | O |  |
| //DF55 |  | var | Additional Prompted Data 1 | B | O |  |
| //DF56 |  | var | Additional Prompted Data 2 | B | O |  |
| //DF57 |  | var | Proprietary Data | B | O |  |
| //9F5A |  | var |  | B | O |  |
| //9F0A |  | var | ASRPD | B | O |  |
| //9F6E |  | var | M/C Fleet | B | O |  |
| //9FD4 |  | var |  | B | O |  |
| //9F50 |  | var |  | B | O |  |

### EMV ARPC Type

Table 26 – EMV ARPC Data

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
<td>FF74</td>
<td>var</td>
<td>Container for non-MAC ARPC</td>
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
<td>/FA</td>
<td>var</td>
<td>Container for generic data</td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//70</td>
<td>var</td>
<td>Container for ARPC</td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>///8A</td>
<td>02</td>
<td><p>Authorization Response Code</p>
<ul>
<li><p>‘00’ = Approved</p></li>
<li><p>‘01’ = Issuer Referral</p></li>
<li><p>‘05’ = Declined</p></li>
<li><p>‘12’ = Switch Interface</p></li>
<li><p>‘13’ = Request Online PIN</p></li>
</ul></td>
<td>AN</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>///91</td>
<td>var</td>
<td><p>Issuer Authentication Data</p>
<p>As defined in <em><strong>EMV Integrated Circuit Card Specifications
for Payment Systems 4.3</strong></em></p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///71</td>
<td>var</td>
<td><p>Issuer Script Template 1</p>
<p>As defined in <em><strong>EMV Integrated Circuit Card Specifications
for Payment Systems 4.3</strong></em>. <em><strong>The host may include
as many instances of this parameter as needed, up to a maximum length of
128 bytes including Tags and Lengths.</strong></em></p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>///72</td>
<td>var</td>
<td><p>Issuer Script Template 2</p>
<p>As defined in <em><strong>EMV Integrated Circuit Card Specifications
for Payment Systems 4.3</strong></em>. <em><strong>The host may include
as many instances of this parameter as needed, up to a maximum length of
128 bytes including Tags and Lengths.</strong></em></p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
</tbody>
</table>

### EMV Batch Data Type

The device formats EMV batch data, such as merchant data and pre-defined
EMV batch data tags, using the format shown in **Table 27**. The default
is an EMV standard list of batch data message tags. The host may also
customize the contents of batch data messages by setting **Property
1.1.1.1.1.3 EMV Batch Data Tag List**.

(EMV Contact Only) For unsuccessful transactions, this data object can
contain additional pre-defined reversal data. It is normally used by the
host for data capture. The default is an EMV standard list of reversal
data message tags. The host may also customize the contents of reversal
data messages by setting **Property 1.1.1.1.1.4 EMV Reversal Data Tag
List**.

As part of successful completion of **Command 0x1001 - Start
Transaction**, this data structure contains the results of the
transaction. The set of tags used during a given EMV transaction is a
combination of the tags defined in the EMV specification and the tags
that are specific to the kernel being used for the transaction.

#### EMV Batch Data (DynaPro Format) Type

Table 27 – EMV Batch Data (DynaPro Format) Type

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 47%" />
<col style="width: 8%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th>Len</th>
<th>Value / Description</th>
<th>Typ</th>
<th colspan="2">Req</th>
<th colspan="2">Default</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="8">2-byte MSB message length excluding padding and
CBC-MAC</td>
</tr>
<tr>
<td>F9</td>
<td>var</td>
<td>Container for MAC structure and generic data</td>
<td>T</td>
<td colspan="2">R</td>
<td colspan="2"></td>
</tr>
<tr>
<td>/DFDF54</td>
<td>var</td>
<td>MAC KSN</td>
<td>B</td>
<td colspan="2">R</td>
<td colspan="2"></td>
</tr>
<tr>
<td>/DFDF55</td>
<td>01</td>
<td><p>MAC Encryption Type</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td colspan="2">R</td>
<td colspan="2"></td>
</tr>
<tr>
<td>/DFDF25</td>
<td>var</td>
<td>Device Serial Number (IFD Serial Number)</td>
<td>B</td>
<td colspan="2">R</td>
<td colspan="2"></td>
</tr>
<tr>
<td>/FA</td>
<td>var</td>
<td>Container for Generic Data</td>
<td>T</td>
<td colspan="2">R</td>
<td colspan="2"></td>
</tr>
<tr>
<td>//F0</td>
<td>var</td>
<td>Transaction Results</td>
<td>T</td>
<td colspan="2">R</td>
<td colspan="2"></td>
</tr>
<tr>
<td>///F1</td>
<td>var</td>
<td>Container for Status Data</td>
<td>T</td>
<td colspan="2">R</td>
<td colspan="2"></td>
</tr>
<tr>
<td>////DFDF1A</td>
<td>01</td>
<td><p>Transaction Status</p>
<ul>
<li><p>0x00 = Accept</p></li>
<li><p>0x01 = Decline</p></li>
<li><p>0x02 = Error</p></li>
</ul></td>
<td>B</td>
<td colspan="2">R</td>
<td colspan="2"></td>
</tr>
<tr>
<td>////DFDF1B</td>
<td>01</td>
<td><p>Additional Transaction Information</p>
<p>0x00</p>
<p>(MAGTEK INTERNAL ONLY FOR NOW)</p>
<ul>
<li><p>0x00 = No additional information</p></li>
<li><p>0x31 = EMV Application not selected</p></li>
<li><p>0x32 = Error transaction in progress</p></li>
<li><p>0x33 = Error invalid PSE format</p></li>
<li><p>0x34 = EMV Terminal application list is empty</p></li>
<li><p>0x35 = Candidate list is empty</p></li>
<li><p>0x36 = No transaction</p></li>
<li><p>0x37 = No common EMV applications</p></li>
<li><p>0x38 = Transaction canceled</p></li>
<li><p>0x39 = Aid parse error</p></li>
<li><p>0x3A = Code table index not found</p></li>
<li><p>0x3B = Error no more record</p></li>
<li><p>0x3C = EMV e overflow [sic.]</p></li>
</ul></td>
<td>B</td>
<td colspan="2">R</td>
<td colspan="2"></td>
</tr>
<tr>
<td>///F8</td>
<td>var</td>
<td>Container for Encrypted Data</td>
<td>T</td>
<td colspan="2">R</td>
<td colspan="2"></td>
</tr>
<tr>
<td>////DFDF59</td>
<td>var</td>
<td><p>Encrypted Data Primitive</p>
<p>Decrypt the value of this TLV data object according to the
<strong>Encrypted Transaction Data KSN</strong> parameter and the
<strong>Encrypted Transaction Data Encryption Type</strong> parameter to
read its contents. See <strong>Table 28</strong> on page <a
href="#_Ref36482891"><strong>51</strong></a> for the data structure as
it should appear after decryption.</p>
<p>Use the data variant of the current MSR DUKPT working key used in the
relevant transaction.</p></td>
<td>B</td>
<td colspan="2">R</td>
<td colspan="2"></td>
</tr>
<tr>
<td>////DFDF56</td>
<td>var</td>
<td>Encrypted Transaction Data KSN</td>
<td>B</td>
<td colspan="2">R</td>
<td colspan="2"></td>
</tr>
<tr>
<td>////DFDF57</td>
<td>01</td>
<td><p>Encrypted Transaction Data Encryption Type</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td colspan="2">R</td>
<td colspan="2"></td>
</tr>
<tr>
<td>////DFDF58</td>
<td>01</td>
<td>Number of padding bytes added to DFDF59 value to force length to a
multiple of 8 bytes</td>
<td>B</td>
<td colspan="2">R</td>
<td colspan="2"></td>
</tr>
<tr>
<td>///F7</td>
<td>var</td>
<td><p>Merchant Data</p>
<p>This contains an instance of <strong>Merchant Data
Container</strong>.</p></td>
<td>T</td>
<td colspan="2">R</td>
<td colspan="2"></td>
</tr>
<tr>
<td>/FE</td>
<td>Var</td>
<td><p>VAS Data Container</p>
<p>See <strong>Table 24 – VAS Data Container Payload</strong></p></td>
<td colspan="2">T</td>
<td colspan="2">O</td>
<td></td>
</tr>
<tr>
<td colspan="8">Padding to ensure the length of data, starting with the
message length at the very beginning, and ending with any additional
padding, is a multiple of 8 bytes for TDES, or 16 bytes for AES. This is
a requirement of using the CBC-MAC algorithm.</td>
</tr>
<tr>
<td colspan="8">Four-byte CBC-MAC. The host should calculate the CBC-MAC
and verify that it matches. For details about calculating a CBC-MAC, see
<strong>About Message Authentication Codes (MAC)</strong>.</td>
</tr>
</tbody>
</table>

<span id="_Ref36482891" class="anchor"></span>Table 28 – EMV Batch Data
(DynaPro Format) DFDF59 Decrypted Contents

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
<td>Decrypted Data Container</td>
<td>T</td>
<td></td>
<td></td>
</tr>
<tr>
<td>/F2</td>
<td>var</td>
<td><p>Container for Batch Data</p>
<p>This data object contains the set of EMV TLV data objects specified
in <strong>Property 1.1.1.1.1.3 EMV Batch Data Tag
List</strong>.</p></td>
<td>T</td>
<td></td>
<td></td>
</tr>
<tr>
<td>//DF29</td>
<td>08</td>
<td><p>Only if tag DF29 is included in <strong>Property 1.1.1.1.1.3 EMV
Batch Data Tag List</strong></p>
<p>Outcome Parameter Set</p>
<p>Byte 1 - Outcome</p>
<p>0x10 = Approved</p>
<p>0x20 = Declined</p>
<p>0x30 = Online Request</p>
<p>0x40 = End Application</p>
<p>0x50 = Select Next Application</p>
<p>0x60 = Try Another Interface</p>
<p>0x70 = Try Again</p>
<p>0xF0 = N/A</p>
<p>Byte 2 – Entry Point Start</p>
<p>0x00 = Start A</p>
<p>0x10 = Start B</p>
<p>0x20 = Start C</p>
<p>0x30 = Start D</p>
<p>0xF0 = N/A</p>
<p>Byte 3 – Entry Point Online Response</p>
<p>0x00 = EMV Data</p>
<p>0x10 = Any</p>
<p>0xF0 = N/A</p>
<p>Byte 4 – CVM</p>
<p>0x00 = No CVM</p>
<p>0x10 = Obtain Signature</p>
<p>0x20 = Online PIN</p>
<p>0x30 = Confirmation Code Verified</p>
<p>0xF0 = N/A</p>
<p>Byte 5 – UI/Data/Receipt</p>
<p>0x80 = UI Request on Outcome Present</p>
<p>0x40 = UI Request on Restart Present</p>
<p>0x20 = Data Record Present</p>
<p>0x10 = Discretionary Data Present</p>
<p>0x08 = Provide Receipt</p>
<p>Byte 6 – Alternate Interface Preference</p>
<p>0x10 = Contact</p>
<p>0x20 = MSR</p>
<p>0xF0 = N/A</p>
<p>Byte 7 – Field Off Request</p>
<p>FF = N/A</p>
<p>Byte 8 – Removal Timeout</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/F3</td>
<td>var</td>
<td><p>(EMV Contact Only)</p>
<p>Container for Reversal Data, if any</p>
<p>This data object contains the set of EMV TLV data objects specified
in <strong>Property 1.1.1.1.1.4 EMV Reversal Data Tag
List</strong>.</p></td>
<td>T</td>
<td>O</td>
<td>null</td>
</tr>
<tr>
<td>/F4</td>
<td>var</td>
<td>Container for encrypted MSR data (MSR Only)</td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF36</td>
<td>01</td>
<td><p>Encrypted Track 1 Status (MSR Only)</p>
<ul>
<li><p>0x00 = OK</p></li>
<li><p>0x01 = Empty</p></li>
<li><p>0x02 = Error</p></li>
<li><p>0x03 = Disabled [<strong>Property 1.1.2.5.1.2 Track 1 Enable (MSR
Only)</strong> set to <strong>Disabled</strong>]</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF37</td>
<td>var</td>
<td>Encrypted Track 1 Data (MSR Only)</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF38</td>
<td>01</td>
<td><p>Encrypted Track 2 Status (MSR Only)</p>
<ul>
<li><p>0x00 = OK</p></li>
<li><p>0x01 = Empty</p></li>
<li><p>0x02 = Error</p></li>
<li><p>0x03 = Disabled [<strong>Property 1.1.2.5.1.3 Track 2 Enable (MSR
Only)</strong> set to <strong>Disabled</strong>]</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF39</td>
<td>var</td>
<td>Encrypted Track 2 Data (MSR Only)</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF3A</td>
<td>01</td>
<td><p>Encrypted Track 3 Status (MSR Only)</p>
<ul>
<li><p>0x00 = OK</p></li>
<li><p>0x01 = Empty</p></li>
<li><p>0x02 = Error</p></li>
<li><p>0x03 = Disabled [<strong>Property 1.1.2.5.1.4 Track 3 Enable (MSR
Only)</strong> set to <strong>Disabled</strong>]</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF3B</td>
<td>var</td>
<td>Encrypted Track 3 Data (MSR Only)</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF3C</td>
<td>var</td>
<td><p>Encrypted MagnePrint Data (MSR Only)</p>
<p>Only included for MSR swipe transactions and when Track Data and
Magneprint are using the same KSN.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF43</td>
<td>04</td>
<td><p>MagnePrint Status Data (MSR Only)</p>
<p>Only included for MSR swipe transactions and when Track Data and
Magneprint are using the same KSN.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF50</td>
<td>var</td>
<td>MSR KSN Data (MSR Only)</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF51</td>
<td>01</td>
<td><p>MSR Encryption Type (MSR Only)</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/FF73</td>
<td>var</td>
<td><p>Container for Encrypted MagnePrint Data (MSR Only)</p>
<p>Only included when Track Data and MagnePrint encryption keys are
using different KSN</p></td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF3C</td>
<td>var</td>
<td><p>Encrypted MagnePrint Data (MSR Only)</p>
<p>Only included for MSR swipe transactions.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF43</td>
<td>04</td>
<td><p>MagnePrint Status Data (MSR Only)</p>
<p>Only included for MSR swipe transactions.</p>
<ul>
<li><p>Bit 0 = MagnePrint Capable Flag</p>
<ul>
<li><p>0 = Device is not MagnePrint capable</p></li>
<li><p>1 = Device is MagnePrint capable</p></li>
</ul></li>
<li><p>Bits 1 through 3 = Mode</p>
<ul>
<li><p>0 = Standard MagnePrint</p></li>
<li><p>1 = Extended MagnePrint</p></li>
</ul></li>
<li><p>Bits 4 through 15 = ASIC Revision</p></li>
<li><p>Bit 16 = Reserved</p></li>
<li><p>Bit 17 = Reserved</p></li>
<li><p>Bit 18 = Swipe too slow</p></li>
<li><p>Bit 19 = Swipe too fast</p></li>
<li><p>Bit 20 = Reserved</p></li>
<li><p>Bit 21 = Card swipe direction</p>
<ul>
<li><p>0 = Forward</p></li>
<li><p>1 = Reverse</p></li>
</ul></li>
</ul>
<p>Bits 22..31 = Reserved</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF50</td>
<td>var</td>
<td><p>MSR KSN Data (MSR Only)</p>
<p>Key Serial Number for the key the host should use to decrypt
<strong>Encrypted MagnePrint Data</strong>.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF51</td>
<td>01</td>
<td><p>MSR Encryption Type (MSR Only)</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/F5</td>
<td>00</td>
<td>Container for Encrypted PIN Data (Touch Only)</td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DF71</td>
<td>00</td>
<td><p>PIN Block Format (Touch Only)</p>
<ul>
<li><p>0x00 = ISO Format 0</p></li>
<li><p>0x01 = ISO Format 1</p></li>
<li><p>0x03 = ISO Format 3</p></li>
<li><p>0x04 = ISO Format 4</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//99</td>
<td>00</td>
<td>Encrypted PIN Data (Touch Only)</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF41</td>
<td>00</td>
<td>PIN KSN Data (Touch Only)</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>//DFDF42</td>
<td>00</td>
<td><p>PIN Encryption Type (Touch Only)</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>null</td>
<td>(var)</td>
<td>Padding to force DFDF59 plus padding to be a multiple of 8
bytes</td>
<td>B</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table 29 - EMV Batch Data (DynaPro Format) DFDF59 Decrypted Contents

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
<td>Decrypted Data Container</td>
<td>T</td>
<td></td>
<td></td>
</tr>
<tr>
<td>/F2</td>
<td>var</td>
<td><p>Container for Batch Data</p>
<p>This data object contains the set of EMV TLV data objects specified
in <strong>Property 1.1.1.1.1.3 EMV Batch Data Tag
List</strong>.</p></td>
<td>T</td>
<td></td>
<td></td>
</tr>
<tr>
<td>/F3</td>
<td>var</td>
<td><p>Container for Reversal Data, if any</p>
<p>This data object contains the set of EMV TLV data objects specified
in <strong>Property 1.1.1.1.1.4 EMV Reversal Data Tag
List</strong>.</p></td>
<td>T</td>
<td>O</td>
<td>null</td>
</tr>
<tr>
<td>null</td>
<td>(var)</td>
<td>Padding to force DFDF59 plus padding to be a multiple of 8 bytes or
16 bytes depending on the cipher block size of the algorithm being
used.</td>
<td>B</td>
<td></td>
<td></td>
</tr>
<tr>
<td>/FE</td>
<td>Var</td>
<td><p>VAS Data Container</p>
<p>See <strong>Table 24 – VAS Data Container Payload</strong></p></td>
<td>T</td>
<td>O</td>
<td>/FE</td>
</tr>
</tbody>
</table>

#### Merchant Data Container

Merchant Data is normally used by the host for receipt printing. The
contents of this container are not customizable.

Table 30 - Merchant Data Container

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 41%" />
<col style="width: 11%" />
<col style="width: 15%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th>Description</th>
<th>Source</th>
<th>Format</th>
<th>Length</th>
</tr>
</thead>
<tbody>
<tr>
<td>DFDF30</td>
<td><p>Masked Track 1 Status (MSR Only)</p>
<ul>
<li><p>0x00 = OK</p></li>
<li><p>0x01 = Empty</p></li>
<li><p>0x02 = Error</p></li>
<li><p>0x03 = Disabled</p></li>
</ul></td>
<td>Device</td>
<td>b</td>
<td>1</td>
</tr>
<tr>
<td>DFDF31</td>
<td>Masked Track 1 Data (MSR Only)</td>
<td>Device</td>
<td>b</td>
<td>var</td>
</tr>
<tr>
<td>DFDF32</td>
<td><p>Masked Track 2 Status (MSR Only)</p>
<ul>
<li><p>0x00 = OK</p></li>
<li><p>0x01 = Empty</p></li>
<li><p>0x02 = Error</p></li>
<li><p>0x03 = Disabled</p></li>
</ul></td>
<td>Device</td>
<td>b</td>
<td>1</td>
</tr>
<tr>
<td>DFDF33</td>
<td>Masked Track 2 Data (MSR Only)</td>
<td>Device</td>
<td>b</td>
<td>var</td>
</tr>
<tr>
<td>DFDF34</td>
<td><p>Masked Track 3 Status (MSR Only)</p>
<ul>
<li><p>0x00 = OK</p></li>
<li><p>0x01 = Empty</p></li>
<li><p>0x02 = Error</p></li>
<li><p>0x03 = Disabled</p></li>
</ul></td>
<td>Device</td>
<td>b</td>
<td>1</td>
</tr>
<tr>
<td>DFDF35</td>
<td>Masked Track 3 Data (MSR Only)</td>
<td>Device</td>
<td>b</td>
<td>var</td>
</tr>
<tr>
<td>DFDF40</td>
<td><p>Signature Status</p>
<ul>
<li><p>0x00 = Signature Not Required</p></li>
<li><p>0x01 = Signature Required</p></li>
<li><p>0x02 = Signature Available</p></li>
<li><p>0x03 = Signature Succeeded</p></li>
<li><p>0x04 = Signature Failed</p></li>
</ul></td>
<td>Device</td>
<td>b</td>
<td>1</td>
</tr>
<tr>
<td>DFDF3E</td>
<td><p>Signature Capture Data (Touch Only)</p>
<p>This is a blob that consists of a raw list of point coordinates
representing the signature. Each coordinate is 2 bytes long, where the
first byte is the X coordinate of that point, and the second byte is the
Y coordinate of that point.</p></td>
<td>Device</td>
<td>b</td>
<td>0..2000</td>
</tr>
<tr>
<td>5F25</td>
<td>EMV Application Effective Date</td>
<td>Card</td>
<td>n6</td>
<td>3</td>
</tr>
<tr>
<td>5F24</td>
<td>EMV Application Expiration Date</td>
<td>Card</td>
<td>n6</td>
<td>3</td>
</tr>
<tr>
<td>89</td>
<td>Authorization Code</td>
<td>Device</td>
<td>b</td>
<td>6</td>
</tr>
<tr>
<td>5F2A</td>
<td>Transaction Currency Code</td>
<td>Card</td>
<td>n3</td>
<td>2</td>
</tr>
<tr>
<td>9F02</td>
<td>Amount, authorized</td>
<td>Device</td>
<td>n12</td>
<td>6</td>
</tr>
<tr>
<td>9F03</td>
<td>Amount, other</td>
<td>Device</td>
<td>n12</td>
<td>6</td>
</tr>
<tr>
<td>9F06</td>
<td>AID - terminal</td>
<td>Device</td>
<td>b</td>
<td>5..16</td>
</tr>
<tr>
<td>9F12</td>
<td>EMV Application Preferred Name</td>
<td>Card</td>
<td>ans</td>
<td>1..16</td>
</tr>
<tr>
<td>9F1C</td>
<td>Terminal ID</td>
<td>Device</td>
<td>an 8</td>
<td>8</td>
</tr>
<tr>
<td>9F39</td>
<td>POS Entry Mode</td>
<td>Device</td>
<td>n2</td>
<td>1</td>
</tr>
<tr>
<td>9C</td>
<td>Transaction Type</td>
<td>Device</td>
<td>n2</td>
<td>1</td>
</tr>
<tr>
<td>9F34</td>
<td>Indicates the results of the last CVM performed</td>
<td>Device</td>
<td>b</td>
<td>3</td>
</tr>
<tr>
<td>5F57</td>
<td>Account Type</td>
<td>Device</td>
<td>n2</td>
<td>1</td>
</tr>
<tr>
<td>5F34</td>
<td>PAN Sequence Number</td>
<td>Card</td>
<td>n2</td>
<td>1</td>
</tr>
<tr>
<td>DFDF4D</td>
<td>Masked ICC Track 2 Data</td>
<td>Card</td>
<td>ans</td>
<td>30..38</td>
</tr>
</tbody>
</table>

### EMV Terminal Configuration File Type 

The host uses **Command 0xD812 - Start Send File to Device (Unsecured)**
to load this file type to control the behavior of the device’s EMV
contact kernel. The configuration loaded using this file type must be
designed to work together with all instances of **EMV Processing
Configuration File Type** and **EMV Entry Point Configuration File
Type** the host loads into the device.

MagTek provides tools that allow these settings to be loaded using a
Microsoft Excel spreadsheet for more convenient authoring, review, and
change tracking. For a reference sample spreadsheet that contains EMVCo
approved configurations, contact MagTek Support Services.

This document shows one example of the available Contact Level 2
certified configurations (***DynaFlex C01, Merchant, Attended, ODA***).
To see which configurations are supported on the devices you are using,
see the list of **Vendor Config IDs** in the device’s ***Letter of
Approval for Contact Level 2*** posted in the list of ***Approved /
Evaluated*** products on the EMVCo web site. For detailed descriptions
of the tags included in this file type, including possible valid values
and their effects on device behavior, see ***EMV Integrated Circuit Card
Specifications for Payment Systems v4.3***.

Table 31 - EMV Configuration Terminal File Type

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
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6"><p>File Type Version</p>
<p>One byte indicating the version of the file type format being
used.</p>
<ul>
<li><p>0xAA</p></li>
</ul></td>
</tr>
<tr>
<td colspan="6"><p>SHA-1 Hash</p>
<p>20-byte hash of all values that follow.</p></td>
</tr>
<tr>
<td>9F1A</td>
<td>02</td>
<td>Terminal Country Code</td>
<td>B</td>
<td>R</td>
<td>08 40</td>
</tr>
<tr>
<td>DF79</td>
<td>01</td>
<td>Cardholder Confirmation</td>
<td>B</td>
<td>R</td>
<td>01</td>
</tr>
<tr>
<td>9F35</td>
<td>01</td>
<td>Terminal Type</td>
<td>B</td>
<td>R</td>
<td>21</td>
</tr>
<tr>
<td>DF0A</td>
<td>01</td>
<td>EMV Contact Supported</td>
<td>B</td>
<td>R</td>
<td>01</td>
</tr>
<tr>
<td>9F33</td>
<td>03</td>
<td>Terminal Capabilities</td>
<td>B</td>
<td>R</td>
<td>E0 28 C8</td>
</tr>
<tr>
<td>9F40</td>
<td>05</td>
<td>Additional Terminal Capabilities</td>
<td>B</td>
<td>R</td>
<td>EF 80 F0 A0 01</td>
</tr>
<tr>
<td>DF55</td>
<td>01</td>
<td>EMV Contactless Supported</td>
<td>B</td>
<td>R</td>
<td>01</td>
</tr>
<tr>
<td>DF0B</td>
<td>01</td>
<td>Magnetic Stripe Supported</td>
<td>B</td>
<td>R</td>
<td>01</td>
</tr>
<tr>
<td>DF27</td>
<td>01</td>
<td>Time allocated to enter a PIN</td>
<td>B</td>
<td>R</td>
<td>0A</td>
</tr>
<tr>
<td>DF06</td>
<td>01</td>
<td>Batch / Online Data Capture managed</td>
<td>B</td>
<td>R</td>
<td>01</td>
</tr>
<tr>
<td>DF08</td>
<td>00</td>
<td>Advice Managed</td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>DF7A</td>
<td>01</td>
<td>PSE Supported</td>
<td>B</td>
<td>R</td>
<td>01</td>
</tr>
<tr>
<td>DF0D</td>
<td>00</td>
<td>AutoRun Mode</td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>DF10</td>
<td>03</td>
<td>Predefined amount for AutoRun mode</td>
<td>B</td>
<td>R</td>
<td>00 00 00</td>
</tr>
<tr>
<td>DF7B</td>
<td>01</td>
<td>PIN Bypass Supported</td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>DF07</td>
<td>01</td>
<td>Referral Managed</td>
<td>B</td>
<td>R</td>
<td>01</td>
</tr>
<tr>
<td>DF09</td>
<td>01</td>
<td>Default TAC supported when regular TACs are not present</td>
<td>B</td>
<td>R</td>
<td>01</td>
</tr>
<tr>
<td>DF73</td>
<td>05</td>
<td>Default TAC default</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>DF74</td>
<td>05</td>
<td>Default TAC denial</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>DF75</td>
<td>05</td>
<td>Default TAC online</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>DF53</td>
<td>01</td>
<td>Random Transaction Selection not supported</td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>DF54</td>
<td>01</td>
<td>Velocity Checking not supported</td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>DF7C</td>
<td>01</td>
<td>CDA Mode</td>
<td>B</td>
<td>R</td>
<td>01</td>
</tr>
</tbody>
</table>

### EMV Processing Configuration File Type 

The host uses **Command 0xD812 - Start Send File to Device (Unsecured)**
to load this file type to control the behavior of the device’s EMV
kernels. The host must compile a single instance of this file type
containing multiple instances of the **AID Delimiter Container**, one
for each contact or contactless AID the device should support. For each
instance of the **AID Delimiter Container** where tag 9F01 is set to a
contactless AID, the host must load a corresponding instance of an Entry
Point Table when it loads the **EMV Entry Point Configuration File
Type** .

Table 32 - EMV Configuration Processing File Type

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
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6"><p>File Type Version</p>
<p>One byte indicating the version of the file type format being
used.</p>
<ul>
<li><p>0xAA</p></li>
</ul></td>
</tr>
<tr>
<td colspan="6"><p>SHA-1 Hash</p>
<p>20-byte hash of all values that follow.</p></td>
</tr>
<tr>
<td>FF33</td>
<td>var</td>
<td><p>AID Delimiter Container</p>
<p>There can be multiple instances of this in sequence. The contents of
the first instance are loaded into Processing Table Slot 1, the contents
of the second are loaded into Processing Table Slot 2, etc.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/9F01</td>
<td>06</td>
<td><p>Payment Brand Identifier</p>
<p>This serves as supporting information to clarify whether this
instance of the AID Delimiter Container is for Contact or
Contactless.</p>
<p>Byte 1 upper nibble must be set to a value flagging that it
corresponds to a Contactless AID, generally by using 0xC0 or 0xF0. For
Contact AID, the value of Byte 1 is 00.</p>
<p>Byte 1 lower nibble:</p>
<ul>
<li><p>0 = Contact</p></li>
<li><p>1 = Interac (Common Kernel Only)</p></li>
<li><p>2 = Mastercard Contactless</p></li>
<li><p>3 = Visa payWave</p></li>
<li><p>4 = Expresspay</p></li>
<li><p>5 = JCB (Common Kernel Only)</p></li>
<li><p>6 = Discover D-PAS</p></li>
<li><p>7 = China UnionPay (Common Kernel Only)</p></li>
</ul>
<p>Bytes 2..5</p>
<p>Reserved for future use</p></td>
<td>B</td>
<td>R</td>
<td>F2 00 00 00 00 00</td>
</tr>
<tr>
<td>/4F</td>
<td>0..16</td>
<td>Application Identifier (AID)</td>
<td>B</td>
<td>R</td>
<td>A0 00 00 00 04 10 10</td>
</tr>
<tr>
<td>/DF7E</td>
<td>01</td>
<td>ASI</td>
<td>B</td>
<td>R</td>
<td>01</td>
</tr>
<tr>
<td>/9F09</td>
<td>02</td>
<td><p>Application Version</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00 00</td>
</tr>
<tr>
<td>/DF11</td>
<td>01</td>
<td><p>Skip TAC/IAC default supported</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>/DF12</td>
<td>01</td>
<td><p>Random transaction selection supported</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>/DF13</td>
<td>01</td>
<td><p>Velocity checking supported</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>/DF14</td>
<td>01</td>
<td><p>Floor limit checking supported</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>/DF15</td>
<td>01</td>
<td><p>TAC supported</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>/DF20</td>
<td>05</td>
<td><p>TAC default</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>/DF21</td>
<td>05</td>
<td><p>TAC denial</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>/DF22</td>
<td>05</td>
<td><p>TAC online</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>/9F1B</td>
<td>04</td>
<td><p>Floor limit</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00 00 00 00</td>
</tr>
<tr>
<td>/DF70</td>
<td>01</td>
<td><p>Target percentage</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>/DF6E</td>
<td>03</td>
<td><p>Threshold value</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00 00 00</td>
</tr>
<tr>
<td>/DF6F</td>
<td>01</td>
<td><p>Maximum target percentage</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>/DF01</td>
<td>01</td>
<td><p>Default DDOL supported</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>/DF71</td>
<td><p>0..</p>
<p>FC</p></td>
<td><p>DDOL</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DF02</td>
<td>01</td>
<td><p>Default TDOL supported</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>/DF72</td>
<td><p>0..</p>
<p>252</p></td>
<td><p>TDOL</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/5F2A</td>
<td>02</td>
<td><p>Currency Code</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00 00</td>
</tr>
<tr>
<td>/5F36</td>
<td>01</td>
<td><p>Transaction currency exponent</p>
<p>Only applies when Payment Brand Identifier indicates
Contact.</p></td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td colspan="6">Additional instances of the <strong>AID Delimiter
Container</strong> parameter, one per Application Identifier (AID) the
device should support.</td>
</tr>
</tbody>
</table>

### EMV Entry Point Configuration File Type 

The host uses **Command 0xD812 - Start Send File to Device (Unsecured)**
to load this file type to control the behavior of the device’s EMV
kernels.

Table 33 - EMV Entry Point Configuration File Type Header

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 25%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th>Value (hex)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>File Type Version</p>
<p>One byte indicating the version of the file type format being
used.</p>
<ul>
<li><p>0xAA</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3"><p>SHA-1 Hash</p>
<p>20-byte hash of all values that follow</p></td>
</tr>
<tr>
<td colspan="3"><p>One or more instances of the following:</p>
<ul>
<li><p><strong>4.10.1 Mastercard MCL Entry Point</strong> Table</p></li>
<li><p><strong>4.10.2 Visa payWave Entry Point</strong> Table</p></li>
<li></li>
<li><p><strong><br />
4.10.3 American Express Expresspay Entry</strong> Point Table</p></li>
<li><p><strong>4.10.4 Discover D-PAS Entry Point</strong> Table</p></li>
<li><p><strong>4.10.5 China Unionpay Entry Point Table (Common
Kernel</strong> Only)</p></li>
<li><p><strong>4.10.6 JCB Entry Point Table (Common Kernel</strong>
Only)</p></li>
<li><p><strong>4.10.7 Interac Flash Entry Point Table (Common
Kernel</strong> Only)</p></li>
</ul>
<p>The host should include an Entry Point Table for each transaction
type to be supported by each contactless payment brand Application
Identifier (AID) listed in the loaded <strong>EMV Processing
Configuration File Type</strong> . For example, if the device should
support three transaction types across each of four payment brands, it
would combine 12 total Entry Point Tables into a single file instance
before loading.</p></td>
</tr>
</tbody>
</table>

#### 4.10.1 Mastercard MCL Entry Point Table

Table 34 - Mastercard MCL Entry Point Table

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
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>FF35</td>
<td>var</td>
<td><p>AID Delimiter Container</p>
<p>There can be multiple instances of this in sequence. The contents of
the first instance are loaded into Entry Point Table Slot 1, the
contents of the second are loaded into Entry Point Table Slot 2,
etc.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DF0E</td>
<td>03</td>
<td><p>Kernel ID, Processing Slot, Transaction Type</p>
<p>Byte 1 Kernel ID</p>
<ul>
<li><p>0x02 = MasterCard Contactless (MCL)</p></li>
</ul>
<p>Byte 2 Processing Slot to Use</p>
<p>See the <strong>AID Delimiter Container</strong> parameter in
<strong>EMV Processing Configuration File Type</strong> for information
about how to identify slots.</p>
<p>Byte 3 Transaction Type</p>
<ul>
<li><p>0x00 = Purchase</p></li>
<li><p>0x01 = Cash</p></li>
<li><p>0x02 = Purchase with cashback</p></li>
<li><p>0x03 = Refund</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>02 01 00</td>
</tr>
<tr>
<td>/DF0F</td>
<td>var</td>
<td><p>Payload Delimiter Container</p>
<p>Include only one of these containers inside each <strong>AID
Delimiter Container</strong>.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//9F1A</td>
<td>02</td>
<td>Terminal Country Code</td>
<td>B</td>
<td>R</td>
<td>08 40</td>
</tr>
<tr>
<td>//9F35</td>
<td>01</td>
<td>Terminal Type</td>
<td>B</td>
<td>R</td>
<td>21</td>
</tr>
<tr>
<td>//9F40</td>
<td>05</td>
<td>Additional Terminal Capabilities</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>//9F7E</td>
<td>01</td>
<td>Mobile Support Indicator</td>
<td>B</td>
<td>R</td>
<td>01</td>
</tr>
<tr>
<td>//DF0C</td>
<td>01</td>
<td>Kernel ID</td>
<td>B</td>
<td>R</td>
<td>02</td>
</tr>
<tr>
<td>//DF1B</td>
<td>01</td>
<td><p>Kernel Configuration</p>
<ul>
<li><p>Bit 8 = MSD Mode Not Supported ( Not Used, kernel does not
support MSD, always set to 0)</p></li>
<li><p>Bit 7 = EMV Mode contactless transaction not supported (Always
set to 0)</p></li>
<li><p>Bit 6 = On-Device-CVM Supported</p></li>
<li><p>Bit 5 = Relay Resistance Protocol Supported</p></li>
<li><p>Bit 4..1 = Reserved for future use</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>20</td>
</tr>
<tr>
<td>//DF2D</td>
<td>03</td>
<td>Message Hold Time (100 of ms)</td>
<td>B</td>
<td>R</td>
<td>00 00 0D</td>
</tr>
<tr>
<td>//9F6D</td>
<td>02</td>
<td><p>Magnetic Stripe Application Version Number</p>
<p>This value only applies when the Kernel Configuration parameter is
set to support MSD. The device ignores this value.</p></td>
<td>B</td>
<td>R</td>
<td>00 01</td>
</tr>
<tr>
<td>//DF1A</td>
<td>03</td>
<td><p>Magnetic Stripe Default UDOL</p>
<p>This value only applies when the Kernel Configuration parameter is
set to support MSD. The device ignores this value.</p></td>
<td>B</td>
<td>R</td>
<td>9F 6A 04</td>
</tr>
<tr>
<td>//DF1E</td>
<td>01</td>
<td><p>CVM Capability - CVM Required</p>
<p>This value only applies when the Kernel Configuration parameter is
set to support MSD. The device ignores this value.</p>
<ul>
<li><p>Bits 8..5:</p>
<ul>
<li><p>0000 = No CVM</p></li>
<li><p>0001 = Obtain Signature</p></li>
<li><p>0010 = Online PIN</p></li>
<li><p>Others = Reserved for future use</p></li>
</ul></li>
<li><p>Bits 4..1 = Reserved for future use</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>//DF2C</td>
<td>01</td>
<td><p>CVM Capability - No CVM Required</p>
<p>This value only applies when the Kernel Configuration parameter is
set to support MSD. The device ignores this value.</p>
<ul>
<li><p>Bits 8..5:</p>
<ul>
<li><p>0000 = No CVM</p></li>
<li><p>0001 = Obtain Signature</p></li>
<li><p>0010 = Online PIN</p></li>
<li><p>Others = Reserved for future use</p></li>
</ul></li>
<li><p>Bits 4..1 = Reserved for future use</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>//9F09</td>
<td>02</td>
<td>EMV Application Version Number</td>
<td>B</td>
<td>R</td>
<td>00 02</td>
</tr>
<tr>
<td>//DF03</td>
<td>01</td>
<td><p>Security Capabilities</p>
<ul>
<li><p>Bit 8 = SDA</p></li>
<li><p>Bit 7 = DDA</p></li>
<li><p>Bit 6 = Card Capture</p></li>
<li><p>Bit 5 = Reserved for future use</p></li>
<li><p>Bit 4 = CDA</p></li>
<li><p>Bits 3..1 = Reserved for future use</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>08</td>
</tr>
<tr>
<td>//DF17</td>
<td>01</td>
<td><p>Card Data Input Capabilities</p>
<ul>
<li><p>Bit 8 = Manual Key Entry</p></li>
<li><p>Bit 7 = MSR</p></li>
<li><p>Bit 6 = ICC</p></li>
<li><p>Bits 5..1 = Reserved for future use</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>60</td>
</tr>
<tr>
<td>//DF18</td>
<td>01</td>
<td><p>CVM Capability - CVM Required</p>
<ul>
<li><p>Bit 8 = Offline Plaintext PIN</p></li>
<li><p>Bit 7 = Enciphered Online PIN</p></li>
<li><p>Bit 6 = Signature</p></li>
<li><p>Bit 5 = Enciphered Offline PIN</p></li>
<li><p>Bit 4 = No CVM</p></li>
<li><p>Bits 3..1 = Reserved for future use</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>28</td>
</tr>
<tr>
<td>//DF19</td>
<td>01</td>
<td><p>CVM Capability - No CVM Required</p>
<ul>
<li><p>Bit 8 = Offline Plaintext PIN</p></li>
<li><p>Bit 7 = Enciphered Online PIN</p></li>
<li><p>Bit 6 = Signature</p></li>
<li><p>Bit 5 = Enciphered Offline PIN</p></li>
<li><p>Bit 4 = No CVM</p></li>
<li><p>Bits 3..1 = Reserved for future use</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>08</td>
</tr>
<tr>
<td>//DF1C</td>
<td>02</td>
<td>Max Lifetime Torn Transaction(s)</td>
<td>B</td>
<td>R</td>
<td>01 2C</td>
</tr>
<tr>
<td>//DF1D</td>
<td>01</td>
<td>Max Number Torn Transaction</td>
<td>B</td>
<td>R</td>
<td>00</td>
</tr>
<tr>
<td>//DF20</td>
<td>05</td>
<td>Terminal Action Code - Default</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>//DF21</td>
<td>05</td>
<td>Terminal Action Code - Denial</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>//DF22</td>
<td>05</td>
<td>Terminal Action Code - Online</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>//DF04</td>
<td>0</td>
<td>Balance Read Before GenAC</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//DF05</td>
<td>0</td>
<td>Balance Read After GenAC</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//DF23</td>
<td>06</td>
<td>Reader Contactless Floor Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 01 00 00</td>
</tr>
<tr>
<td>//DF24</td>
<td>06</td>
<td>Reader Contactless Transaction Limit (No On-Device CVM)</td>
<td>B</td>
<td>R</td>
<td>00 00 00 03 00 00</td>
</tr>
<tr>
<td>//DF25</td>
<td>06</td>
<td>Reader Contactless Transaction Limit (On-Device CVM)</td>
<td>B</td>
<td>R</td>
<td>00 00 00 05 00 00</td>
</tr>
<tr>
<td>//DF26</td>
<td>06</td>
<td>Reader CVM Required Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 10 00</td>
</tr>
<tr>
<td>//DF27</td>
<td>02</td>
<td>Timeout Value (ms)</td>
<td>B</td>
<td>R</td>
<td>13 88</td>
</tr>
<tr>
<td>//DF30</td>
<td>01</td>
<td>Hold time value before field off (100 of ms)</td>
<td>B</td>
<td>R</td>
<td>0D</td>
</tr>
<tr>
<td>//DF32</td>
<td>02</td>
<td>Minimum Relay Resistance Grace Period (100 of micro sec)</td>
<td>B</td>
<td>R</td>
<td>00 14</td>
</tr>
<tr>
<td>//DF33</td>
<td>02</td>
<td>Maximum Relay Resistance Grace Period (100 of micro seconds)</td>
<td>B</td>
<td>R</td>
<td>00 32</td>
</tr>
<tr>
<td>//DF34</td>
<td>02</td>
<td>Terminal Expected Transmission Time for Relay Resistance C-APDU (100
of micro seconds)</td>
<td>B</td>
<td>R</td>
<td>00 12</td>
</tr>
<tr>
<td>//DF35</td>
<td>02</td>
<td>Terminal Expected Transmission Time for Relay Resistance R-APDU (100
of micro seconds)</td>
<td>B</td>
<td>R</td>
<td>00 18</td>
</tr>
<tr>
<td>//DF36</td>
<td>02</td>
<td>Relay Resistance Accuracy Threshold (100 of micro seconds)</td>
<td>B</td>
<td>R</td>
<td>01 2C</td>
</tr>
<tr>
<td>//DF37</td>
<td>01</td>
<td>Relay Resistance Transmission Time Mismatch Threshold (%)</td>
<td>B</td>
<td>R</td>
<td>32</td>
</tr>
</tbody>
</table>

#### 4.10.2 Visa payWave Entry Point Table

Table 35 - Visa payWave Entry Point Table

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
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>FF35</td>
<td>var</td>
<td><p>AID Delimiter Container</p>
<p>There can be multiple instances of this in sequence. The contents of
the first instance are loaded into Entry Point Table Slot 1, the
contents of the second are loaded into Entry Point Table Slot 2,
etc.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DF0E</td>
<td>03</td>
<td><p>Kernel ID, Processing Slot, Transaction Type</p>
<p>Byte 1 Kernel ID</p>
<ul>
<li><p>0x03 = Visa payWave</p></li>
</ul>
<p>Byte 2 Processing Slot to Use</p>
<p>See the <strong>AID Delimiter Container</strong> parameter in
<strong>EMV Processing Configuration File Type</strong> for information
about how to identify slots.</p>
<p>Byte 3 Transaction Type</p>
<ul>
<li><p>0x00 = Purchase</p></li>
<li><p>0x01 = Cash</p></li>
<li><p>0x02 = Purchase with cashback</p></li>
<li><p>0x03 = Refund</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>03 05 00</td>
</tr>
<tr>
<td>/DF0F</td>
<td>var</td>
<td><p>Payload Delimiter Container</p>
<p>Include only one of these containers inside each <strong>AID
Delimiter Container</strong>.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//9F35</td>
<td>01</td>
<td>Terminal Type</td>
<td>B</td>
<td>R</td>
<td>21</td>
</tr>
<tr>
<td>//9F1A</td>
<td>02</td>
<td>Terminal Country Code</td>
<td>B</td>
<td>R</td>
<td>08 40</td>
</tr>
<tr>
<td>//9F33</td>
<td>03</td>
<td>Terminal Capabilities</td>
<td>B</td>
<td>R</td>
<td>00 00 00</td>
</tr>
<tr>
<td>//9F40</td>
<td>05</td>
<td>Additional Terminal Capabilities</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>//9F66</td>
<td>04</td>
<td>Terminal Transaction Qualifier</td>
<td>B</td>
<td>R</td>
<td>22 00 40 00</td>
</tr>
<tr>
<td>//DF1B</td>
<td>03</td>
<td><p>Kernel Configuration</p>
<p>Byte 1</p>
<ul>
<li><p>Bit 8 = CVN17 fallback to MSD legacy (Not supported)</p></li>
<li><p>Bit 7 = Enable MSD and CVN17 (Not supported)</p></li>
<li><p>Bit 6 = MSD Formatting Track 2 Data (Not supported)</p></li>
<li><p>Bit 5 = MSD Formatting Track 1 Data (Not supported)</p></li>
<li><p>Bits 4..3 = Reserved for future use</p></li>
<li><p>Bit 2 = Force Online if Online Only terminal and with cash back
transaction</p></li>
<li><p>Bit 1 = UL2 #23 Errata S.79/5.80 Performed</p></li>
</ul>
<p>Byte 2</p>
<ul>
<li><p>Bit 8 = DRL Set</p></li>
<li><p>Bit 7 = TVR not reset</p></li>
<li><p>Bit 6 = TSI not reset</p></li>
<li><p>Bits 5..1 = Reserved for future use</p></li>
</ul>
<p>Byte 3</p>
<p>Reserved for future use</p></td>
<td>B</td>
<td>R</td>
<td>00 00 06</td>
</tr>
<tr>
<td>//DF2D</td>
<td>03</td>
<td>Message Hold Time (100 of ms)</td>
<td>B</td>
<td>R</td>
<td>00 00 0F</td>
</tr>
<tr>
<td>//9F09</td>
<td>02</td>
<td>EMV Application Version Number</td>
<td>B</td>
<td>R</td>
<td>00 01</td>
</tr>
<tr>
<td>//DF30</td>
<td>01</td>
<td><p>Bitmap Entry Point</p>
<ul>
<li><p>Bit 8 = Status Check Support Flag</p></li>
<li><p>Bit 7= Zero Amount Allowed Flag</p></li>
<li><p>Bit 6= Reader Contactless Transaction Limit</p></li>
<li><p>Bit 5 = Reader Contactless Floor Limit</p></li>
<li><p>Bit 4 = Reader CVM Required Limit</p></li>
<li><p>Bits 3..1 = Reserved for future use</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>F8</td>
</tr>
<tr>
<td>//DF32</td>
<td>01</td>
<td><p>Status Zero Amount Allowed Flag</p>
<ul>
<li><p>0x01 = Option 1, Online Cryptogram Request</p></li>
<li><p>0x02 = Option 2, Not Allowed</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>02</td>
</tr>
<tr>
<td>//9F1B</td>
<td>04</td>
<td>Terminal Floor Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00</td>
</tr>
<tr>
<td>//DF23</td>
<td>06</td>
<td>Reader Contactless Floor Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 20 00</td>
</tr>
<tr>
<td>//DF24</td>
<td>06</td>
<td>Reader Contactless Transaction Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 50 00</td>
</tr>
<tr>
<td>//DF26</td>
<td>06</td>
<td>Reader CVM Required Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 10 00</td>
</tr>
</tbody>
</table>

####  

#### 4.10.3 American Express Expresspay Entry Point Table

Table 36 - American Express Expresspay Entry Point Table

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
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>FF35</td>
<td>var</td>
<td><p>AID Delimiter Container</p>
<p>There can be multiple instances of this in sequence. The contents of
the first instance are loaded into Entry Point Table Slot 1, the
contents of the second are loaded into Entry Point Table Slot 2,
etc.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DF0E</td>
<td>03</td>
<td><p>Kernel ID, Processing Slot, Transaction Type</p>
<p>Byte 1 Kernel ID</p>
<ul>
<li><p>0x04 = Expresspay</p></li>
</ul>
<p>Byte 2 Processing Slot to Use</p>
<p>See the <strong>AID Delimiter Container</strong> parameter in
<strong>EMV Processing Configuration File Type</strong> for information
about how to identify slots.</p>
<p>Byte 3 Transaction Type</p>
<ul>
<li><p>0x00 = Purchase</p></li>
<li><p>0x01 = Cash</p></li>
<li><p>0x02 = Purchase with cashback</p></li>
<li><p>0x03 = Refund</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>04 04 00</td>
</tr>
<tr>
<td>/DF0F</td>
<td>var</td>
<td><p>Payload Delimiter Container</p>
<p>Include only one of these containers inside each <strong>AID
Delimiter Container</strong>.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//9F09</td>
<td>02</td>
<td>EMV Application Version Number</td>
<td>B</td>
<td>R</td>
<td>00 01</td>
</tr>
<tr>
<td>//9F1A</td>
<td>02</td>
<td>Terminal Country Code</td>
<td>B</td>
<td>R</td>
<td>08 40</td>
</tr>
<tr>
<td>//9F33</td>
<td>03</td>
<td>Terminal Capabilities</td>
<td>B</td>
<td>R</td>
<td>60 28 00</td>
</tr>
<tr>
<td>//9F35</td>
<td>01</td>
<td>Terminal Type</td>
<td>B</td>
<td>R</td>
<td>21</td>
</tr>
<tr>
<td>//9F40</td>
<td>05</td>
<td>Additional Terminal Capabilities</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>//9F6D</td>
<td>01</td>
<td><p>Contactless Reader Capability</p>
<p>Bits 8..7</p>
<ul>
<li><p>00 = Expresspay 1.0</p></li>
<li><p>01 = Expresspay 2.0 and Expresspay &gt;= 3.x (MSD)</p></li>
<li><p>11 = Expresspay &gt;= 3.x(MSD)</p></li>
</ul>
<p>Bits 6..1 = 0 (Reserved, not to be configured)</p></td>
<td>B</td>
<td>R</td>
<td>C0</td>
</tr>
<tr>
<td>//DF1B</td>
<td>06</td>
<td><p>Kernel Configuration</p>
<p>Byte 1 Seed for UN for MSD mode</p>
<p>Byte 2</p>
<ul>
<li><p>Bit 8 = DRL Set</p></li>
<li><p>Bit 7 = EMVCo Entry Point</p></li>
<li><p>Bit 6 = Use TAC and IAC</p></li>
<li><p>Bit 5 = Not EMV Consistency Check</p></li>
<li><p>Bit 4 = Patch ODA Applied</p></li>
<li><p>Bit 3 = Consistency Check as per EMV</p></li>
<li><p>Bit 2 = Delay authorization</p></li>
<li><p>Bit 1 = Unable to go online support</p></li>
</ul>
<p>Byte 3</p>
<p>Hold Time for ‘See Phone’ cases</p>
<p>Byte 4</p>
<p>No holding time on Approve and Decline</p>
<p>Byte 5</p>
<ul>
<li><p>Bit 8 = XP 3.0 activated</p></li>
<li><p>Bit 7 = Start D managed in EMV Mode</p></li>
<li><p>Bit 6 = Disable Discretionary Data</p></li>
<li><p>Bit 5 = Display delayed message</p></li>
<li><p>Bit 4 = Check CDOL2 Presence</p></li>
<li><p>Bit 3 = CVM Mobile Supported</p></li>
<li><p>Bit 2 = Terminal exempt of No CVM checks</p></li>
<li><p>Bit 1 = Transit Terminal</p></li>
</ul>
<p>Byte 6</p>
<ul>
<li><p>Bit 8 = Display PROCESSING Message</p></li>
<li><p>Bit 7 = Only EMV Mode</p></li>
<li><p>Bits 6..4 = Reserved for future use</p></li>
<li><p>Bits 3..1 = C-4 Kernel Version</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>31 01 00 00 00 00</td>
</tr>
<tr>
<td>//DF27</td>
<td>01</td>
<td>Timeout, Field off request (100 of ms)</td>
<td>B</td>
<td>R</td>
<td>20</td>
</tr>
<tr>
<td>//DF2D</td>
<td>03</td>
<td>Message Hold Time (100 of ms)</td>
<td>B</td>
<td>R</td>
<td>00 00 0F</td>
</tr>
<tr>
<td>//DF30</td>
<td>01</td>
<td><p>Bitmap Entry Point</p>
<ul>
<li><p>Bit 8 = Status Check Support Flag</p></li>
<li><p>Bit 7= Zero Amount Allowed Flag</p></li>
<li><p>Bit 6= Reader Contactless Transaction Limit</p></li>
<li><p>Bit 5 = Reader Contactless Floor Limit</p></li>
<li><p>Bit 4 = Reader CVM Required Limit</p></li>
<li><p>Bits 3..1 = Reserved for future use</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>F8</td>
</tr>
<tr>
<td>//DF32</td>
<td>01</td>
<td><p>Status Zero Amount Allowed</p>
<ul>
<li><p>0x01 = Option 1, Online Cryptogram Request</p></li>
<li><p>0x02 = Option 2, Not Allowed</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>01</td>
</tr>
<tr>
<td>//DF20</td>
<td>05</td>
<td>Terminal Action Code - Default</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>//DF21</td>
<td>05</td>
<td>Terminal Action Code - Denial</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>//DF22</td>
<td>05</td>
<td>Terminal Action Code - Online</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>//DF23</td>
<td>06</td>
<td>Reader Contactless Floor Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 20 00</td>
</tr>
<tr>
<td>//DF24</td>
<td>06</td>
<td>Reader Contactless Transaction Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 01 00 00</td>
</tr>
<tr>
<td>//DF26</td>
<td>06</td>
<td>Reader CVM Required Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 01 00 00</td>
</tr>
</tbody>
</table>

#### 4.10.4 Discover D-PAS Entry Point Table

Table 37 - Discover D-PAS Entry Point Table

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
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>FF35</td>
<td>var</td>
<td><p>AID Delimiter Container</p>
<p>There can be multiple instances of this in sequence. The contents of
the first instance are loaded into Entry Point Table Slot 1, the
contents of the second are loaded into Entry Point Table Slot 2,
etc.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DF0E</td>
<td>03</td>
<td><p>Kernel ID, Processing Slot, Transaction Type</p>
<p>Byte 1 Kernel ID</p>
<ul>
<li><p>0x06 = Discover D-PAS</p></li>
</ul>
<p>Byte 2 Processing Slot to Use</p>
<p>See the <strong>AID Delimiter Container</strong> parameter in
<strong>EMV Processing Configuration File Type</strong> for information
about how to identify slots.</p>
<p>Byte 3 Transaction Type</p>
<ul>
<li><p>0x00 = Purchase</p></li>
<li><p>0x01 = Cash</p></li>
<li><p>0x02 = Purchase with cashback</p></li>
<li><p>0x03 = Refund</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>06 06 00</td>
</tr>
<tr>
<td>/DF0F</td>
<td>var</td>
<td><p>Payload Delimiter Container</p>
<p>Include only one of these containers inside each <strong>AID
Delimiter Container</strong>.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//9F09</td>
<td>02</td>
<td>EMV Application Version Number</td>
<td>B</td>
<td>R</td>
<td>00 01</td>
</tr>
<tr>
<td>//9F1A</td>
<td>02</td>
<td>Terminal Country Code</td>
<td>B</td>
<td>R</td>
<td>08 40</td>
</tr>
<tr>
<td>//9F33</td>
<td>03</td>
<td>Terminal Capabilities</td>
<td>B</td>
<td>R</td>
<td>00 00 00</td>
</tr>
<tr>
<td>//9F35</td>
<td>01</td>
<td>Terminal Type</td>
<td>B</td>
<td>R</td>
<td>21</td>
</tr>
<tr>
<td>//9F66</td>
<td>04</td>
<td>Terminal Transaction Qualifier</td>
<td>B</td>
<td>R</td>
<td>B6 00 C0 00</td>
</tr>
<tr>
<td>//DF1B</td>
<td>01</td>
<td><p>Kernel Configuration</p>
<ul>
<li><p>Bit 8 = Exception List Supported</p></li>
<li><p>Bit 7 = Check PID Limit</p></li>
<li><p>Bit 6 = Extended Selection Support</p></li>
<li><p>Bit 5 = RFU</p></li>
<li><p>Bit 4 = Kernel Supports Do Not Fix Track</p></li>
<li><p>Bit 3 = Online PIN allowed after going online</p></li>
<li><p>Bits 2..1 = Reserved for future use</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>60</td>
</tr>
<tr>
<td>//DF1B</td>
<td>02</td>
<td><p>Kernel Configuration (Common Kernel Only)</p>
<p>Byte 1</p>
<ul>
<li><p>Bit 8 = Exception List Supported</p></li>
<li><p>Bit 7 = Check PID Limit</p></li>
<li><p>Bit 6 = Extended Selection Support</p></li>
<li><p>Bit 5 = RFU</p></li>
<li><p>Bit 4 = Kernel Supports Do Not Fix Track</p></li>
<li><p>Bit 3 = Online PIN allowed after going online</p></li>
<li><p>Bits 2..1 = Reserved for future use</p></li>
</ul>
<p>Byte 2</p>
<ul>
<li><p>Bit 8 = RFU</p></li>
<li><p>Bit 7 = RFU</p></li>
<li><p>Bit 6 = RFU</p></li>
<li><p>Bit 5 = Deferred Authorization</p></li>
<li><p>Bit 4 = Data Storage Supported (MAGTEK INTERNAL ONLY FOR
NOW)</p></li>
<li><p>Bit 3 = Torn Transaction Supported (MAGTEK INTERNAL ONLY FOR
NOW)</p></li>
<li><p>Bit 2 = Extended Logging Supported (MAGTEK INTERNAL ONLY FOR
NOW)</p></li>
<li><p>Bit 1 = Do Not Display Processing Message (MAGTEK INTERNAL ONLY
FOR NOW)</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>60 00</td>
</tr>
<tr>
<td>//DF30</td>
<td>02</td>
<td><p>Bitmap Entry Point</p>
<ul>
<li><p>Bit 8 = Status Check Support Flag</p></li>
<li><p>Bit 7= Zero Amount Allowed Flag</p></li>
<li><p>Bit 6= Reader Contactless Transaction Limit</p></li>
<li><p>Bit 5 = Reader Contactless Floor Limit</p></li>
<li><p>Bit 4 = Reader CVM Required Limit</p></li>
<li><p>Bits 3..1 = Reserved for future use</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>F8</td>
</tr>
<tr>
<td>//DF32</td>
<td>01</td>
<td><p>Status Zero Amount Allowed Flag</p>
<ul>
<li><p>0x01 = Option 1, Online Cryptogram Request</p></li>
<li><p>0x02 = Option 2, Not Allowed</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>01</td>
</tr>
<tr>
<td>//9F1B</td>
<td>06</td>
<td>Terminal Floor Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00</td>
</tr>
<tr>
<td>//DF23</td>
<td>06</td>
<td>Reader Contactless Floor Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 01 50 00</td>
</tr>
<tr>
<td>//DF24</td>
<td>06</td>
<td>Reader Contactless Transaction Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 03 00 00</td>
</tr>
<tr>
<td>//DF26</td>
<td>06</td>
<td>Reader CVM Required Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 20 00</td>
</tr>
</tbody>
</table>

#### 4.10.5 China Unionpay Entry Point Table (Common Kernel Only)

Table 38 – China Unionpay Entry Point Table

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
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>FF35</td>
<td>var</td>
<td><p>AID Delimiter Container</p>
<p>There can be multiple instances of this in sequence. The contents of
the first instance are loaded into Entry Point Table Slot 1, the
contents of the second are loaded into Entry Point Table Slot 2,
etc.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DF0E</td>
<td>03</td>
<td><p>Kernel ID, Processing Slot, Transaction Type</p>
<p>Byte 1 Kernel ID</p>
<ul>
<li><p>0x07 = China Unionpay</p></li>
</ul>
<p>Byte 2 Processing Slot to Use</p>
<p>See the <strong>AID Delimiter Container</strong> parameter in
<strong>EMV Processing Configuration File Type</strong> for information
about how to identify slots.</p>
<p>Byte 3 Transaction Type</p>
<ul>
<li><p>0x00 = Purchase</p></li>
<li><p>0x01 = Cash</p></li>
<li><p>0x02 = Purchase with cashback</p></li>
<li><p>0x03 = Refund</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>07 05 00</td>
</tr>
<tr>
<td>/DF0F</td>
<td>var</td>
<td><p>Payload Delimiter Container</p>
<p>Include only one of these containers inside each <strong>AID
Delimiter Container</strong>.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//9F09</td>
<td>02</td>
<td>EMV Application Version Number</td>
<td>B</td>
<td>R</td>
<td>00 30</td>
</tr>
<tr>
<td>//9F1A</td>
<td>02</td>
<td>Terminal Country Code</td>
<td>B</td>
<td>R</td>
<td>01 56</td>
</tr>
<tr>
<td>//9F33</td>
<td>03</td>
<td>Terminal Capabilities</td>
<td>B</td>
<td>R</td>
<td>60 08 00</td>
</tr>
<tr>
<td>//9F35</td>
<td>01</td>
<td>Terminal Type</td>
<td>B</td>
<td>R</td>
<td>21</td>
</tr>
<tr>
<td>//9F66</td>
<td>04</td>
<td>Terminal Transaction Qualifier</td>
<td>B</td>
<td>R</td>
<td>36 00 00 80</td>
</tr>
<tr>
<td>//DF1B</td>
<td>02</td>
<td><p>Kernel Configuration</p>
<p>Byte1:</p>
<ul>
<li><p>→ b8..b2: RFU</p></li>
<li><p>→ b1: Display PROCESSING Message</p></li>
</ul>
<p>Byte2:</p>
<ul>
<li><p>→ b8: C7 Outcome</p></li>
<li><p>→ b7: TVR Not Reset</p></li>
<li><p>→ b6: 9F27 Always Raised</p></li>
<li><p>→ b5: Not Forced Online</p></li>
<li><p>→ b4: Standard UICS DT/CT Application Flow Supported</p></li>
<li><p>→ b3: Always DD</p></li>
<li><p>→ b2: Not Decline On Transit Debit AID ONLINE PIN Case</p></li>
<li><p>→ b1: Transit Terminal</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>00 00</td>
</tr>
<tr>
<td>//DF20</td>
<td>05</td>
<td>Terminal Action Code - Default</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>//DF21</td>
<td>05</td>
<td>Terminal Action Code - Denial</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>//DF22</td>
<td>05</td>
<td>Terminal Action Code - Online</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>//DF23</td>
<td>06</td>
<td>Reader Contactless Floor Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 01 50 00</td>
</tr>
<tr>
<td>//DF24</td>
<td>06</td>
<td>Reader Contactless Transaction Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 03 00 00</td>
</tr>
<tr>
<td>//DF26</td>
<td>06</td>
<td>Reader CVM Required Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 01 20 00</td>
</tr>
<tr>
<td>//DF30</td>
<td>01</td>
<td><p>Bitmap Entry Point</p>
<ul>
<li><p>Bit 8 = Status Check Support Flag</p></li>
<li><p>Bit 7= Zero Amount Allowed Flag</p></li>
<li><p>Bit 6= Reader Contactless Transaction Limit</p></li>
<li><p>Bit 5 = Reader Contactless Floor Limit</p></li>
<li><p>Bit 4 = Reader CVM Required Limit</p></li>
</ul>
<p>Bits 3..1 = Reserved for future use</p></td>
<td>B</td>
<td>R</td>
<td>78</td>
</tr>
<tr>
<td>9F1B</td>
<td>04</td>
<td>Terminal Floor Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 3a 98</td>
</tr>
</tbody>
</table>

#### 4.10.6 JCB Entry Point Table (Common Kernel Only)

Table 39 - JCB Entry Point Table

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
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>FF35</td>
<td>var</td>
<td><p>AID Delimiter Container</p>
<p>There can be multiple instances of this in sequence. The contents of
the first instance are loaded into Entry Point Table Slot 1, the
contents of the second are loaded into Entry Point Table Slot 2,
etc.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DF0E</td>
<td>03</td>
<td><p>Kernel ID, Processing Slot, Transaction Type</p>
<p>Byte 1 Kernel ID</p>
<ul>
<li><p>0x05 = JCB</p></li>
</ul>
<p>Byte 2 Processing Slot to Use</p>
<p>See the <strong>AID Delimiter Container</strong> parameter in
<strong>EMV Processing Configuration File Type</strong> for information
about how to identify slots.</p>
<p>Byte 3 Transaction Type</p>
<ul>
<li><p>0x00 = Purchase</p></li>
<li><p>0x01 = Cash</p></li>
<li><p>0x02 = Purchase with cashback</p></li>
<li><p>0x03 = Refund</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>05 06 00</td>
</tr>
<tr>
<td>/DF0F</td>
<td>var</td>
<td><p>Payload Delimiter Container</p>
<p>Include only one of these containers inside each <strong>AID
Delimiter Container</strong>.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//9F01</td>
<td>06</td>
<td>Acquirer Identifier</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00 01</td>
</tr>
<tr>
<td>//9F15</td>
<td>02</td>
<td>Merchant Category Code</td>
<td>B</td>
<td>R</td>
<td>70 32</td>
</tr>
<tr>
<td>//9F09</td>
<td>02</td>
<td>EMV Application Version Number</td>
<td>B</td>
<td>R</td>
<td>00 01</td>
</tr>
<tr>
<td>//9F1A</td>
<td>02</td>
<td>Terminal Country Code</td>
<td>B</td>
<td>R</td>
<td>03 92</td>
</tr>
<tr>
<td>//9F33</td>
<td>03</td>
<td>Terminal Capability</td>
<td>B</td>
<td>R</td>
<td>60 68 08</td>
</tr>
<tr>
<td>//9F35</td>
<td>01</td>
<td>Terminal Type</td>
<td>B</td>
<td>R</td>
<td>21</td>
</tr>
<tr>
<td>//9F4E</td>
<td>var</td>
<td>Merchant Name and Location</td>
<td>B</td>
<td>R</td>
<td>5858204D45524348414E54205959204C4F434154494F4E</td>
</tr>
<tr>
<td>//DF1B</td>
<td>03</td>
<td><p>Kernel Configuration</p>
<p>Byte1 (reflects Combination Options):</p>
<ul>
<li><p>→ b8: RFU</p></li>
<li><p>→ b7: Status Check Supported</p></li>
<li><p>→ b6: ODA Supported</p></li>
<li><p>→ b5: Exception File Supported</p></li>
<li><p>→ b4: Random Transaction Selection Supported</p></li>
<li><p>→ b3: MagStripe Mode Supported (see here)</p></li>
<li><p>→ b2: EMV Mode Supported (see here)</p></li>
<li><p>→ b1: Legacy Mode Supported (see here)</p></li>
</ul>
<p>Byte2 (reflects Combination Options):</p>
<ul>
<li><p>→ b8..b1: RFU</p></li>
<li><p>Byte3:</p></li>
<li><p>→ b8: On Device CVM</p></li>
<li><p>→ b7: Transit Reader Supported</p></li>
<li><p>→ b6: Issuer Update Supported</p></li>
<li><p>→ b5..b3: RFU</p></li>
<li><p>→ b2: Do Not Display PROCESSING message</p></li>
<li><p>→ b1: TVR with Online Pin for Legacy</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>7B 00 80</td>
</tr>
<tr>
<td>//DF20</td>
<td>05</td>
<td>Terminal Action Code - Default</td>
<td>B</td>
<td>R</td>
<td>90 40 20 80 20</td>
</tr>
<tr>
<td>//DF21</td>
<td>05</td>
<td>Terminal Action Code - Denial</td>
<td>B</td>
<td>R</td>
<td>04 10 20 20 20</td>
</tr>
<tr>
<td>//DF22</td>
<td>05</td>
<td>Terminal Action Code - Online</td>
<td>B</td>
<td>R</td>
<td>90 60 20 90 20</td>
</tr>
<tr>
<td>//DF23</td>
<td>06</td>
<td>Reader Contactless Floor Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 01 50 00</td>
</tr>
<tr>
<td>//DF24</td>
<td>06</td>
<td>Reader Contactless Transaction Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 03 00 00</td>
</tr>
<tr>
<td>//DF25</td>
<td>06</td>
<td>On Device CVM Contactless Transaction Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 02 50 00</td>
</tr>
<tr>
<td>//DF26</td>
<td>06</td>
<td>Reader CVM Required Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 01 20 00</td>
</tr>
<tr>
<td>//9F1B</td>
<td>04</td>
<td>Terminal Floor Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 3a 98</td>
</tr>
</tbody>
</table>

#### 4.10.7 Interac Flash Entry Point Table (Common Kernel Only)

Table 40 – Interac Flash Entry Point Table

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
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>FF35</td>
<td>var</td>
<td><p>AID Delimiter Container</p>
<p>There can be multiple instances of this in sequence. The contents of
the first instance are loaded into Entry Point Table Slot 1, the
contents of the second are loaded into Entry Point Table Slot 2,
etc.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DF0E</td>
<td>03</td>
<td><p>Kernel ID, Processing Slot, Transaction Type</p>
<p>Byte 1 Kernel ID</p>
<ul>
<li><p>0x41 = Interac Flash</p></li>
</ul>
<p>Byte 2 Processing Slot to Use</p>
<p>See the <strong>AID Delimiter Container</strong> parameter in
<strong>EMV Processing Configuration File Type</strong> for information
about how to identify slots.</p>
<p>Byte 3 Transaction Type</p>
<ul>
<li><p>0x00 = Purchase</p></li>
<li><p>0x01 = Cash</p></li>
<li><p>0x02 = Purchase with cashback</p></li>
<li><p>0x03 = Refund</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>41 05 00</td>
</tr>
<tr>
<td>/DF0F</td>
<td>var</td>
<td><p>Payload Delimiter Container</p>
<p>Include only one of these containers inside each <strong>AID
Delimiter Container</strong>.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//9F09</td>
<td>02</td>
<td>EMV Application Version Number</td>
<td>B</td>
<td>R</td>
<td>00 02</td>
</tr>
<tr>
<td>//9F1A</td>
<td>02</td>
<td>Terminal Country Code</td>
<td>B</td>
<td>R</td>
<td>01 24</td>
</tr>
<tr>
<td>//9F33</td>
<td>03</td>
<td>Terminal Capabilities</td>
<td>B</td>
<td>R</td>
<td>60 68 08</td>
</tr>
<tr>
<td>//9F35</td>
<td>01</td>
<td>Terminal Type</td>
<td>B</td>
<td>R</td>
<td>21</td>
</tr>
<tr>
<td>//9F40</td>
<td>05</td>
<td>Additional Terminal Capabilities</td>
<td>B</td>
<td>R</td>
<td>E0 00 E0 F0 01</td>
</tr>
<tr>
<td>//9F58</td>
<td>01</td>
<td>Merchant Type Indicator</td>
<td>B</td>
<td>R</td>
<td>03</td>
</tr>
<tr>
<td>//9F5D</td>
<td>06</td>
<td>Receipt Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 50 00</td>
</tr>
<tr>
<td>//9F5E</td>
<td>02</td>
<td><p>Terminal Option Status</p>
<p>Byte1:</p>
<ul>
<li><p>→ b8: Use Interface If Different Currency</p></li>
<li><p>→ b7: Use Interface If Different Country Code</p></li>
<li><p>→ b6: Use Interface If Domestic Transaction With Different
Currency</p></li>
<li><p>→ b5..b1: RFU</p></li>
</ul>
<p>Byte2:</p>
<ul>
<li><p>→ b8..b1: RFU</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>E0 00</td>
</tr>
<tr>
<td>//9F5F</td>
<td>06</td>
<td>Reader Contactless Floor Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 01 00 00</td>
</tr>
<tr>
<td>//DF1B</td>
<td>02</td>
<td><p>Kernel Configuration</p>
<p>Byte1:</p>
<ul>
<li><p>Max Retry</p></li>
</ul>
<p>Byte2:</p>
<ul>
<li><p>→ b8: Interac Contact</p></li>
<li><p>→ b7: Interac on Other Terminal</p></li>
<li><p>→ b6: Mobile NFC</p></li>
<li><p>→ b5: Contactless Card</p></li>
<li><p>→ b4: Legacy Floor Limit</p></li>
<li><p>→ b3: Always DD</p></li>
<li><p>→ b2: Terminal v1.4</p></li>
<li><p>→ b1: Processing Message Disabled</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>02 34</td>
</tr>
<tr>
<td>//DF20</td>
<td>05</td>
<td>Terminal Action Code - Default</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>//DF21</td>
<td>05</td>
<td>Terminal Action Code - Denial</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>//DF22</td>
<td>05</td>
<td>Terminal Action Code - Online</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 00</td>
</tr>
<tr>
<td>//9F1B</td>
<td>04</td>
<td>Terminal Floor Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 1F 40</td>
</tr>
</tbody>
</table>

### EMV Configuration CA Public Keys File Type 

The host can load this file type to control the behavior of the device’s
EMV contact and contactless kernels when the device should support
Offline Data Authentication (ODA). Populate all values from information
provided by each payment brand that should be supported by the device.
The host can load this file using **Command 0xD812 - Start Send File to
Device (Unsecured)**.

MagTek provides tools that allow these settings to be loaded using a
Microsoft Excel spreadsheet in xlsx format for more convenient
authoring, review, and change tracking. For a reference sample
spreadsheet, contact MagTek Support Services. The MagTek tools expect
the spreadsheet to be formatted format as shown in **Table 41**. Each CA
Key to be supported is defined in a tab of the Excel file.

Table 41 - EMV Configuration CA Keys File Type

| Tag | Len | Value / Description | Typ | Req | Example |
|----|----|----|----|----|----|
| DFDF79 | 05 | Registered Application ID (RID) | B | R | A0 00 00 00 04 |
| DFDF7A | 01 | CA Public Key Index | B | R | 05 |
| DFDF7B | var | CA Public key Modulus | B | R | B8 04 8A … D5 97 |
| DFDF7C | 01 or 03 | CA Public Key Exponent | B | R | 03 |
| DFDF7D | 14 | CA Public Key Checksum | B | R | EB FA 0D 5D 06 D8 CE 70 2D A3 EA E8 90 70 1D 45 E2 74 C8 45 |

The MagTek tool converts the spreadsheet data into the format shown in
**Table 42**.

Table 42 - CA Keys Raw Format

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>CA Keys Raw Format</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>RID (5 Bytes)</p>
<p>As defined by the payment brand.</p></td>
</tr>
<tr>
<td><p>Index (1 Byte)</p>
<p>As defined by the payment brand.</p></td>
</tr>
<tr>
<td><p>Exponent Length (1 Byte)</p>
<ul>
<li><p>0x01</p></li>
<li><p>0x03</p></li>
</ul></td>
</tr>
<tr>
<td>Key Length (1 Byte), Max of 248 bytes per EMVCo specifications</td>
</tr>
<tr>
<td><p>Exponent (1 or 3 Bytes)</p>
<ul>
<li><p>0x03</p></li>
<li><p>0x010001</p></li>
</ul></td>
</tr>
<tr>
<td><p>Modulus</p>
<p>As defined by the payment brand.</p></td>
</tr>
<tr>
<td>Additional CA Keys, repeating from RID through Modulus, as
needed.</td>
</tr>
<tr>
<td>SHA-1 hash of all data in the file</td>
</tr>
</tbody>
</table>

### EMV American Express DRL Configuration File Type (Not Supported on Expresspay 4.x) 

The host can load this file type to control the behavior of the device’s
American Express contactless kernel when the card sends tag 9F70 and one
or more DRL is defined.

The host can load it using **Command 0xD812 - Start Send File to Device
(Unsecured)**. See the ***Expresspay 4.0.2*** specification for
functional details.

MagTek provides tools that allow these settings to be loaded using a
Microsoft Excel spreadsheet in xlsx format for more convenient
authoring, review, and change tracking. For a reference sample
spreadsheet, contact MagTek Support Services. The MagTek tools expect
the spreadsheet to be formatted as shown in **Table 43**. Each DRL to be
supported is defined in a tab of the Excel file.

Table 43 - EMV Configuration American Express DRL Set File Type

| Tag  | Len | Value / Description                  | Typ | Req | Example           |
|------|-----|--------------------------------------|-----|-----|-------------------|
| DF23 | 06  | Reader Contactless Floor Limit       | B   | R   | 00 00 00 00 15 00 |
| DF24 | 06  | Reader Contactless Transaction Limit | B   | R   | 00 00 00 00 05 00 |
| DF26 | 06  | Reader CVM Required Limit            | B   | R   | 00 00 00 00 10 00 |

The MagTek tool converts the spreadsheet data into the raw format shown
in **Table 44**:

Table 44 -Raw EMV Configuration American Express DRL Set File Type

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
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6"><p>File Type Version</p>
<p>One byte indicating the version of the file type format being
used.</p>
<ul>
<li><p>0xAA</p></li>
</ul></td>
</tr>
<tr>
<td colspan="6"><p>SHA-1 Hash</p>
<p>20 byte hash of all values that follow</p></td>
</tr>
<tr>
<td>FF37</td>
<td>var</td>
<td>DRL Configuration Container</td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/FF36</td>
<td>var</td>
<td>DRL Set Container</td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//DF23</td>
<td>06</td>
<td>Reader Contactless Floor Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 15 00</td>
</tr>
<tr>
<td>//DF24</td>
<td>06</td>
<td>Reader Contactless Transaction Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 05 00</td>
</tr>
<tr>
<td>//DF26</td>
<td>06</td>
<td>Reader CVM Required Limit</td>
<td>B</td>
<td>R</td>
<td>00 00 00 00 10 00</td>
</tr>
<tr>
<td colspan="6">Additional instances of DRL Set Container as needed</td>
</tr>
</tbody>
</table>

### Signature Capture File Type (Touch Only)

The signature capture file type produced when the host invokes **Command
0x1801 - Request Cardholder Signature (Touch Only)** is a TLV data
object in the format below.

Table 45 - Signature Capture File Type

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 61%" />
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
<td>81</td>
<td>08</td>
<td><p>Signature Window Width and Height</p>
<p>Bytes 0..1 = Left edge (minimum value of all X coordinates)</p>
<p>Bytes 2..3 = Right edge (maximum value of all Y coordinates)</p>
<p>Bytes 4..5 = Top edge (minimum value of all Y coordinates)</p>
<p>Bytes 6..7 = Bottom edge (maximum value of all Y
coordinates)</p></td>
<td>B</td>
<td>R</td>
<td><p>0000 00FD 0000 0078 (landscape)</p>
<p>0000 00C8</p>
<p>0000 00B9</p>
<p>(portrait)</p></td>
</tr>
<tr>
<td>82</td>
<td>var</td>
<td><p>Signature Coordinate Values List</p>
<p>This is a blob that consists of a raw list of point coordinates
representing the signature. Each coordinate is 4 bytes long, where the
first 2 bytes are the X coordinate of that point and the second 2 bytes
are the Y coordinate of that point.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
</tbody>
</table>

### Security Operation Type

This non-TLV data structure consists of four or five bytes that
describes a security operation, including the algorithms and methods to
be used in that operation.

Table 46 - Security Operation Type

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 62%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th>Offset</th>
<th>Description</th>
<th>Typ</th>
<th>Req</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td><p>Operation Type</p>
<ul>
<li><p>0x01 = Key Agreement</p></li>
<li><p>0x02 = Command Authorization Using Signature</p></li>
<li><p>0x03 = Command Authorization Using MAC</p></li>
<li><p>0x05 = Data Authentication Using MAC</p></li>
<li><p>0x07 = Data Encryption</p></li>
<li><p>0x10 = Data Signature</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>1</td>
<td><p>Operation Algorithm</p>
<p>If <strong>Operation Type</strong> is Key Agreement type:</p>
<ul>
<li><p>0x01 = ECDHE</p></li>
</ul>
<p>If <strong>Operation Type</strong> is a Signature type:</p>
<ul>
<li><p>0x01 = ECDSA (indeterministic)</p></li>
</ul>
<p>If <strong>Operation Type</strong> is a MAC type:</p>
<ul>
<li><p>0x01 = HMAC</p></li>
<li><p>0x02 = CBC-MAC</p></li>
<li><p>0x03 = CMAC</p></li>
</ul>
<p>If <strong>Operation Type</strong> is an Encryption type:</p>
<ul>
<li><p>0x01 = DEA</p></li>
<li><p>0x02 = 2TDEA</p></li>
<li><p>0x03 = 3TDEA</p></li>
<li><p>0x04 = AES-128</p></li>
<li><p>0x05 = AES-192</p></li>
<li><p>0x06 = AES-256</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td><p>Operation Curve/Mode/Hash/Cipher</p>
<p>If <strong>Operation Type</strong> is a Key Agreement type, this
specifies the Curve:</p>
<ul>
<li><p>0x01 = P192</p></li>
<li><p>0x02 = P224</p></li>
<li><p>0x03 = P256</p></li>
<li><p>0x04 = P384</p></li>
<li><p>0x05 = P521</p></li>
</ul>
<p>If <strong>Operation Type</strong> is a Signature type, this
specifies the Hash:</p>
<ul>
<li><p>0x01 = MD5</p></li>
<li><p>0x02 = SHA-1</p></li>
<li><p>0x03 = SHA-224</p></li>
<li><p>0x04 = SHA-256</p></li>
<li><p>0x05 = SHA-384</p></li>
<li><p>0x06 = SHA-512</p></li>
<li><p>0x07 = SHA-512/224</p></li>
<li><p>0x08 = SHA-512/256</p></li>
<li><p>0x09 = SHA3-224</p></li>
<li><p>0x0A = SHA3-256</p></li>
<li><p>0x0B = SHA3-384</p></li>
<li><p>0x0C = SHA3-512</p></li>
</ul>
<p>If <strong>Operation Type</strong> is a MAC type, this specifies the
Encryption Algorithm:</p>
<ul>
<li><p>0x01 = DEA</p></li>
<li><p>0x02 = 2TDEA</p></li>
<li><p>0x03 = 3TDEA</p></li>
<li><p>0x04 = AES-128</p></li>
<li><p>0x05 = AES-192</p></li>
<li><p>0x06 = AES-256</p></li>
</ul>
<p>If <strong>Operation Type</strong> is an Encryption type, this
specifies the Mode:</p>
<ul>
<li><p>0x01 = ECB (Block)</p></li>
<li><p>0x02 = CBC (Block)</p></li>
<li><p>0x03 = CFB (Stream)</p></li>
<li><p>0x04 = OFB (Stream)</p></li>
<li><p>0x05 = CTR (Stream)</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td><p>KDF/Curve/Padding</p>
<p>If <strong>Operation Type</strong> is a Key Agreement type, this
specifies the KDF:</p>
<ul>
<li><p>0x01 = SP800-56A / X9.63</p></li>
</ul>
<p>If <strong>Operation Type</strong> is a Signature type, this
specifies the Curve:</p>
<ul>
<li><p>0x01 = P192</p></li>
<li><p>0x02 = P224</p></li>
<li><p>0x03 = P256</p></li>
<li><p>0x04 = P384</p></li>
<li><p>0x05 = P521</p></li>
</ul>
<p>If <strong>Operation Type</strong> is a MAC type, this specifies the
Padding:</p>
<ul>
<li><p>0x00 = None (for streaming modes)</p></li>
<li><p>0x01 = Zeros (ISO 9797 Padding Method 1)</p></li>
<li><p>0x02 = One and zeros (ISO 9797 Method 2)</p></li>
<li><p>0x03 = Length + zeros (ISO 9797 Method 3)</p></li>
<li><p>0x10 = PKCS7 (pad # = pad length)</p></li>
<li><p>0x11 = X9.23 (random + pad length)</p></li>
<li><p>0x20 = Random (when length is known)</p></li>
</ul>
<p>If <strong>Operation Type</strong> is an Encryption type, this
specifies the Padding:</p>
<ul>
<li><p>0x00 = None (for streaming modes)</p></li>
<li><p>0x01 = Zeros (ISO 9797 Padding Method 1)</p></li>
<li><p>0x02 = One and zeros (ISO 9797 Method 2)</p></li>
<li><p>0x03 = Length + zeros (ISO 9797 Method 3)</p></li>
<li><p>0x10 = PKCS7 (pad # = pad length)</p></li>
<li><p>0x11 = X9.23 (random + pad length)</p></li>
<li><p>0x20 = Random (when length is known)</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td><p>MAC Block Size</p>
<p>If <strong>Operation Type</strong> is a MAC type, this specifies the
data to be MACed must be padded to a multiple of this many bytes.</p>
<p>For all other Operation Types, do not include this byte.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
</tbody>
</table>

### Security Parameters Type

Table 47 - Security Parameters Type

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 61%" />
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
<td>81</td>
<td>var</td>
<td><p>Operation</p>
<p>This contains an instance of a <strong>Security Operation
Type</strong> structure specifying the operation to be
performed.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td><p>Data</p>
<p>Reserved for future use. Do not include this parameter. It is
reserved for Initialization Vector or nonce, if needed.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>85</td>
<td>var</td>
<td><p>Extra Data Item</p>
<p>Reserved for future use. Do not include.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>A8</td>
<td>var</td>
<td><p>Key Information</p>
<p>This specifies the key used in the operation. Populate with a
<strong>Key Information Type</strong> TLV data object. For ECDSA
operations, do not include this parameter.</p></td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>A9</td>
<td>var</td>
<td><p>Second Key Information (Reserved, do not include)</p>
<p>This specifies a second key used in the operation. If needed,
populate with a <strong>Key Information Type</strong> TLV data
object.</p></td>
<td>T</td>
<td>O</td>
<td></td>
</tr>
</tbody>
</table>

### Key Information Type

Table 48 - Key Information Type

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 61%" />
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
<td>81</td>
<td>02</td>
<td><p>Key Slot ID</p>
<p>Identifies the key being used for operation. See <strong>Table 56 -
Key Slot IDs</strong>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>var</td>
<td><p>Key Label</p>
<p>The label that indicates the key type. For example,
<strong>DEVTK</strong>.</p></td>
<td>AN</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>86</td>
<td>var</td>
<td><p>Key Derivation Details</p>
<p>Use Key Serial Number (KSN) in requests, Key Derivation Information
in responses.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>88</td>
<td>var</td>
<td><p>Additional Information</p>
<p>Reserved for future use. Do not include.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
</tbody>
</table>

### NFC UID Type (EMV Contactless Only)

Table 49 – NFC UID Type

| Tag  | Len | Value / Description | Typ | Req | Default |
|------|-----|---------------------|-----|-----|---------|
| DF79 | var | NFC UID             | B   | R   |         |

### GPO Response Type (EMV Contactless Only)

Table 50 – NFC UID Type

| Tag | Len | Value / Description | Typ | Req | Default |
|-----|-----|---------------------|-----|-----|---------|
| 81  | var | GPO Response        | B   | R   |         |

### TR-31 Key Block Type

A ***TR-31*** (***X9.143***) key block consists of three parts:

The **Key Block Header** (KBH) which contains attribute information
about the key and the key block and is not encrypted. It is always
treated as ASCII.

- The first section is 16 bytes with a fixed format defined below.

- The second section is optional within the standard, but required for
  current products.

The **Confidential Data**, which is encrypted and always binary.

- Two bytes indicating the key length (in bits, AES-128 is 128 bits, so
  length will be 0080).

- The secret key and/or sensitive data.

- Padding as required (random bytes 0x00 to 0xFF).

The **MAC**, which is of varying length as follows:

- 64 bits if the TDEA key derivation method is used (typically not used
  for this device).

- 128 bits if the AES key derivation method is used.

| Header | Header (optional) | Key Length |    Key    | Key Padding | Block Padding | MAC |
|--------|-------------------|------------|:---------:|-------------|---------------|-----|
|        |                   |            | Encrypted |             |               |     |
|        |                   | MAC        |           |             |               |     |

Symmetric keys are padded with **Block Padding** to the maximum length
for the algorithm, 192 bits for TDEA or 256 bits for AES, to hide the
true length of short keys.

The data to be encrypted and the MAC are always binary for calculation
purposes. The encrypted data and the MAC are converted to ASCII hex as
the last step.

Date and time strings specified within the TR-31 block are represented
according to the rules described in ***ISO 8601*** and ***TR-31***. Year
is 4 digits. Time uses UTC 24 hour clock. Some functions like
‘toISOString()’ will produce a string of format
**yyyy-mm-ddThh:mm:ss.fffZ** where fff is a decimal fraction of a
second, Z is UTC time zone. The device ignores ‘Z’ and ‘.fff’ if they
are present. Seconds ‘:ss’ are optional. Date, hours, and minutes are
required. For example, March 23, 2020 4:19PM is encoded as
**2020-03-23T16:19** at minimum, but could also be
**2020-03-23T16:19:00.000Z**.

Table 51 - TR-31 Block Fixed Header

| Offset | Name | Fixed Value | Variable |
|----|----|----|----|
| 0 | Key Block V ID | ‘D’ |  |
| 1..4 | Key Block Length |  | Calculated (in decimal, e.g. 138 bytes shown as ‘0138’ |
| 5..6 | Usage |  | Look up the desired **Key Type** in **Table 52 below** and select this value from the **Usage** column. |
| 7 | Algorithm |  | Look up the desired **Key Type** in **Table 52 below** and select this value from the **Algorithm** column. |
| 8 | Mode of Use |  | Look up the desired **Key Type** in **Table 52 below** and select this value from the **Mode of Use** column. |
| 9..10 | Key Version \# | ‘00’ | Always ‘00’ |
| 11 | Exportability | ‘N’ | Always no export allowed |
| 12..13 | \# option blocks |  | Calculated |
| 14..15 | Reserved | ‘00’ |  |

Table 52 - TR-31 Key Type Table - Usage/Algorithm/Mode

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 9%" />
<col style="width: 31%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr>
<th>Key Type</th>
<th>Usage</th>
<th>Algorithm AES/TDEA</th>
<th><p>Mode of Use</p>
<p>(Both, To, From)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Transport (KBPK)</td>
<td>‘K1’</td>
<td>‘A’ / ‘T’</td>
<td>‘D’</td>
</tr>
<tr>
<td>Initial DUKPT Key</td>
<td>‘B1’</td>
<td>‘A’ / ‘T’</td>
<td>‘X’</td>
</tr>
<tr>
<td>Fixed MAC (CMAC)</td>
<td>‘M6’</td>
<td>‘A’ / ‘T’</td>
<td>(‘C’, ’G’, ’V’)</td>
</tr>
<tr>
<td>Fixed Encrypt</td>
<td>‘D0’</td>
<td>‘A’ / ‘T’</td>
<td>(‘B’, ‘E’, ‘D’)</td>
</tr>
</tbody>
</table>

Table 53 - TR-31 Optional Blocks

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr>
<th>ID</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>‘IK’</td>
<td>DUKPT KSID</td>
</tr>
<tr>
<td>‘KS’</td>
<td>Key Set Identifier (e.g. data used by host to find and/or derive
this key).</td>
</tr>
<tr>
<td>‘KC’</td>
<td>Key Check Value (KCV) (Legacy or CMAC)</td>
</tr>
<tr>
<td>‘PB’</td>
<td>Padding Field</td>
</tr>
<tr>
<td>‘TS’</td>
<td>Current Time Stamp (optional) see description in previous
section.</td>
</tr>
<tr>
<td>‘KP’</td>
<td>KCV of KBPK that created this Key Block (optional-preferred)</td>
</tr>
<tr>
<td>‘21’</td>
<td><p>MagTek Additional Key Info</p>
<p>From <strong>Table 54 - MagTek Custom TR-31 Small Optional
Block</strong></p></td>
</tr>
</tbody>
</table>

Table 54 - MagTek Custom TR-31 Small Optional Block

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 19%" />
<col style="width: 14%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr>
<th>Offset</th>
<th>Name</th>
<th>Value</th>
<th>Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td>0..1</td>
<td>Block ID</td>
<td>‘21’</td>
<td>MagTek Added Key Info Block</td>
</tr>
<tr>
<td>2..3</td>
<td>Block Length</td>
<td>var</td>
<td>ASCII Hex (Length 01-FF from offset 0)</td>
</tr>
<tr>
<td>4..7</td>
<td>Owner Tag</td>
<td>‘MGTK’</td>
<td>Avoid collision with others using Block ID ‘21’</td>
</tr>
<tr>
<td>8..9</td>
<td>Data Tag</td>
<td>‘10’</td>
<td>Field ID</td>
</tr>
<tr>
<td>10..11</td>
<td>Data Len</td>
<td>‘01’</td>
<td>Field Length (ASCII Hex 00-FF)</td>
</tr>
<tr>
<td>12</td>
<td>Data</td>
<td>‘T’,’P’, or ‘0’</td>
<td><p>Field Data for Key Environment</p>
<ul>
<li><p>T = Test</p></li>
<li><p>P = Production</p></li>
<li><p>0 = Erase Key</p></li>
</ul></td>
</tr>
<tr>
<td>13…</td>
<td>Added elements</td>
<td></td>
<td>More Fields (Tags, Lengths, and Data)</td>
</tr>
</tbody>
</table>

Table 55 - MagTek Custom Key Data Fields

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 12%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr>
<th>Field ID</th>
<th>Length</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>‘10’</td>
<td>‘01’</td>
<td><p>Key Environment</p>
<ul>
<li><p>T = Test</p></li>
<li><p>P = Production</p></li>
<li><p>0 = Erase Key</p></li>
</ul></td>
</tr>
<tr>
<td>‘11’</td>
<td>‘04’</td>
<td><p>Key Slot ID</p>
<p>See <strong>Table 56 - Key Slot ID</strong>.</p></td>
</tr>
<tr>
<td>‘12’</td>
<td>‘04’</td>
<td>Key Slot ID of Transport Key</td>
</tr>
<tr>
<td>‘20’</td>
<td>--</td>
<td>Reserved</td>
</tr>
<tr>
<td>‘21’</td>
<td>‘04’</td>
<td><p>DUKPT Data Type Restriction Bitmask</p>
<p>This is for Transport Keys and DUKPT keys. Default to 0.</p></td>
</tr>
<tr>
<td>‘31’</td>
<td>‘07’</td>
<td>Device Serial Number</td>
</tr>
<tr>
<td>‘32’</td>
<td>‘10’</td>
<td><p>Challenge Token</p>
<p>10h = 16 characters</p></td>
</tr>
<tr>
<td>‘33’</td>
<td>‘10’ ..‘18’</td>
<td><p>Expiration Date/Time</p>
<p>This is in UTC format, use short form if possible. Reserved.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref49929758" class="anchor"></span>Table 56 - Key Slot IDs

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 13%" />
<col style="width: 38%" />
<col style="width: 24%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th>ID</th>
<th>Label</th>
<th>Description</th>
<th>Load Transport Key</th>
<th>TR31-F</th>
</tr>
</thead>
<tbody>
<tr>
<td>10xx</td>
<td></td>
<td>Transport Keys (KBPK)</td>
<td></td>
<td></td>
</tr>
<tr>
<td>1000</td>
<td>TMPTK</td>
<td>Temporary KBPK</td>
<td>Key agreement process from <strong>Command 0xF017 - Establish
Ephemeral KBPK</strong></td>
<td>N/A</td>
</tr>
<tr>
<td>1001</td>
<td>MTK</td>
<td>Master Transport Key</td>
<td>TMPTK</td>
<td>K1AD</td>
</tr>
<tr>
<td>1002</td>
<td>DEVTK</td>
<td>Device Master Transport Key</td>
<td>MTK</td>
<td>K1AD</td>
</tr>
<tr>
<td>1003</td>
<td>FINTK</td>
<td>Financial Master Transport Key</td>
<td>MTK</td>
<td>K1AD</td>
</tr>
<tr>
<td>1021</td>
<td>PRODTK</td>
<td><p>(MAGTEK INTERNAL ONLY)</p>
<p>Production Transport Key</p></td>
<td>DEVTK</td>
<td>K1AD</td>
</tr>
<tr>
<td>1022</td>
<td>MFGTK</td>
<td><p>(MAGTEK INTERNAL ONLY)</p>
<p>Manufacturing Transport Key</p></td>
<td>DEVTK</td>
<td>K1AD</td>
</tr>
<tr>
<td>1081</td>
<td>MKIFTK</td>
<td>MagTek KIF Financial Transport Keys</td>
<td>FINTK</td>
<td>K1AD</td>
</tr>
<tr>
<td>1101</td>
<td>FREQMK</td>
<td>Factory Request MAC Key</td>
<td>PRODTK</td>
<td>M6AV</td>
</tr>
<tr>
<td>1102</td>
<td>MREQMK</td>
<td>Manufacturer Device Request MAC Key</td>
<td>MFGTK</td>
<td>M6AV</td>
</tr>
<tr>
<td>1111</td>
<td>MFRQMK</td>
<td>Manufacturer Financial Request MAC (Configuration) Key</td>
<td>MKIFTK</td>
<td>M6AV</td>
</tr>
<tr>
<td>0x2000 to 0x201F</td>
<td>DKPTM0 to DKPTM1F</td>
<td>DUKPT Initial Keys,</td>
<td>MKIFTK</td>
<td>B1TX</td>
</tr>
</tbody>
</table>

#### DUKPT Key Mapping

##### Terms and Definitions

DUKPT – Derived Unique Key Per Transaction

OID – Object Identifier

SRED - Secure Reading and Exchange of Data

There are 7 new OIDs defined for these 7 SRED Data IDs.

Each OID value contains a two-byte DUKPT slot ID and a one-byte
transformation ID.

| **SRED Data ID** | **OID** | **OID Size** |
|----|----|:--:|
| 0: Not assigned | N/A | N/A |
| 1: PIN-TDES (supported on PED devices Only) | 0x010102040101 | 3 |
| 2: Account Data | 0x010102040102 | 3 |
| 3: MAC | 0x010102040103 | 3 |
| 4: Magneprint (supported on devices with MSR Only) | 0x010102040104 | 3 |
| 5: MagTek Token | 0x010102040105 | 3 |
| 6: User Data 1 | 0x010102040106 | 3 |
| 7: PIN-AES (supported on PED devices Only) | 0x010102040107 | 3 |

Table 57 - SRED Data IDs and OIDs

###### DUKPT Slot IDs

The existing TR31 Module supports 32 MagTek DUKPT Slot IDs, from 0x2000
to 0x201F.

The Key Injection Software Tool shall inject DUKPT keys through these
DUKPT Slot IDs.

###### Transformation IDs

This is the list of DUKPT transformations defined in both the Legacy and
AES specifications.

#### Restrictions of a DUKPT Slot ID

Table 58 - Transformation IDs for DUKPT Legacy and AES

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><p><strong>Transformation</strong></p>
<p><strong>ID #</strong></p></th>
<th><strong>Usage Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Data for calculation</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">0</td>
<td>Reserved</td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td>PIN Encryption</td>
<td>Legacy</td>
<td>00 00 00 00 00 00 00 FF</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td>MAC Generate/Verify</td>
<td>Legacy</td>
<td>00 00 00 00 00 00 FF 00</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td>MAC Verify</td>
<td>Legacy</td>
<td>00 00 00 00 FF 00 00 00</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td>Data Enc/Decryption</td>
<td>Legacy</td>
<td>00 00 00 00 00 FF 00 00</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td>Data Encryption</td>
<td>Legacy</td>
<td>00 00 00 FF 00 00 00 00</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td>Reserved</td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td>PIN Encryption</td>
<td>AES</td>
<td>0x1000</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td>MAC Generate</td>
<td>AES</td>
<td>0x2000</td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td>MAC Verify</td>
<td>AES</td>
<td>0x2001</td>
</tr>
<tr>
<td style="text-align: center;">A</td>
<td>MAC Generate/Verify</td>
<td>AES</td>
<td>0x2002</td>
</tr>
<tr>
<td style="text-align: center;">B</td>
<td>Data Encryption</td>
<td>AES</td>
<td>0x3000</td>
</tr>
<tr>
<td style="text-align: center;">C</td>
<td>Data Decryption</td>
<td>AES</td>
<td>0x3001</td>
</tr>
<tr>
<td style="text-align: center;">D</td>
<td>Data Enc/Decryption</td>
<td>AES</td>
<td>0x3002</td>
</tr>
</tbody>
</table>

<table>
<caption><p>Table 59 - The definition of Restriction bit
map</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Bit #</strong></th>
<th style="text-align: center;"><strong>5</strong></th>
<th style="text-align: center;"><strong>4</strong></th>
<th style="text-align: center;"><strong>3</strong></th>
<th style="text-align: center;"><strong>2</strong></th>
<th style="text-align: center;"><strong>1</strong></th>
<th style="text-align: center;"><strong>0</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Data Type</strong></td>
<td style="text-align: center;"><p>User Data</p>
<p>(RFU)</p></td>
<td style="text-align: center;"><p>Token</p>
<p>(RFU)</p></td>
<td style="text-align: center;">Magneprint</td>
<td style="text-align: center;">MAC</td>
<td style="text-align: center;">Account Data</td>
<td style="text-align: center;">PIN</td>
</tr>
</tbody>
</table>

During TR31 Key Injection, each DUKPT Slot ID contains a parameter
indicates the purpose of a Key Set.

Example 1: The restriction value is 0x3F

This Key Set can be used for all purposes.

Example 2: The restriction value is 0x3E

This Key Set can be used for all purposes, except PIN Encryption.

Example 3: The restriction value is 0x01

This Key Set can be used for PIN Encryption only.

#### The Rules of Key Mapping

SRED Data ID map configuration values (Slot ID and Transformation ID)
must be checked and rejected if they don’t meet the following
conditions.

a). The DUKPT Slot ID must be loaded. (**Table 60**)

b). The loaded DUKPT Slot ID must allows this type of SRED Data ID.
(Table 59**)**

c). The transformation must be allowed by **Table 61**.

#### The settings of DUKPT Slot IDs injected through TR31

Here is the list of parameters of 4 DUKPT Slot IDs based on the existing
Key Injection Tool.

| DUKPT Slot ID | Key Type | Restrictions |
|---------------|----------|--------------|
| DKPTM0-2000   | TDES     | 0x3E         |
| DKPTM2-2002   | AES-128  | 0x3F         |
| DKPTM3-2003   | AES-256  | 0x3F         |
| DKPTM7-2007   | TDES     | 0x3F         |

Table 60 - Settings of Injected DUKPT Slot IDs

#### The Allowed Key Mapping Table

<table>
<caption><p>Table 61 - Allowed Key Mapping Table</p></caption>
<colgroup>
<col style="width: 9%" />
<col style="width: 55%" />
<col style="width: 18%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr>
<th><p>SRED</p>
<p>Data ID</p></th>
<th><p>Data Type</p>
<p>(Working Key Purpose)</p></th>
<th><p>Allowed Legacy</p>
<p>DUKPT</p>
<p>Transforms</p></th>
<th><p>Allowed AES</p>
<p>DUKPT</p>
<p>Transforms</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>Not assigned</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>1</td>
<td>PIN-TDES (supported on PED devices Only)</td>
<td>01</td>
<td>Not allowed</td>
</tr>
<tr>
<td>2</td>
<td>Account Data</td>
<td>01, 04, 05</td>
<td>0B, 0D</td>
</tr>
<tr>
<td>3</td>
<td>Transaction MAC</td>
<td>02</td>
<td>08, 0A</td>
</tr>
<tr>
<td>4</td>
<td>MagnePrint (supported on devices with MSR Only)</td>
<td>01, 04, 05</td>
<td>0B, 0D</td>
</tr>
<tr>
<td>5</td>
<td>MagTek Token (RFU)</td>
<td>RFU</td>
<td>RFU</td>
</tr>
<tr>
<td>6</td>
<td>User Data #1 (RFU)</td>
<td>RFU</td>
<td>RFU</td>
</tr>
<tr>
<td>7</td>
<td>PIN-AES (supported on PED devices Only)</td>
<td>Not allowed</td>
<td>07</td>
</tr>
<tr>
<td>…</td>
<td>RFU</td>
<td>-</td>
<td>-</td>
</tr>
</tbody>
</table>

Note: If SRED Data ID 2 and 4 are mapped to the same Key Set, then they
must have the same Transformation ID.

If the Transformation ID of the latest key mapping request is different,
then the original OID setting of the other SRED Data ID will be forced
to match the latest OID setting. For example, SRED Data ID 2 has been
mapped to 0x2007 0x04, user wants to map SRED Data ID 4 to 0x2007 0x05,
then the OID setting of SRED Data ID 2 will be forced to 0x2007 0x05.

#####  Examples of Key Mapping

The following OID Values indicate that:

1)  200701: Map PIN-TDES to DKPTM7-2007 PIN Encryption Variant.

2)  20020B: Map Account Data to DKPTM2-2002 Data Encryption Usage.

3)  200702: Map MAC to DKPTM7-2007 MAC Generate/Verify Variant.

4)  20030B: Map MangePrint to DKPTM3-2003 Data Encryption Usage.

5)  000004: MagTek Token is RFU, 0000 ID does not exist (this is default
    value).

6)  000004: User Data is RFU, 0000 ID does not exist (this is default
    value).

7)  200207: Map PIN-AES to DKPTM2-2002 PIN Encryption Usage.

<figure>
<img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image1.png"
style="width:5.23264in;height:2.34861in"
alt="Graphical user interface, text, application, email Description automatically generated" />
<figcaption><p>Figure 1 - Configuration Usage Values</p></figcaption>
</figure>

### Miniature Certificate Type (MAGTEK INTERNAL ONLY)

Table 62 - Miniature Certificate Type

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 61%" />
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
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6"><strong>FF01</strong> = Start Of Miniature Certificate
Marker</td>
</tr>
<tr>
<td>81</td>
<td>08</td>
<td>Miniature Certificate Info and ID</td>
<td>B</td>
<td>R</td>
<td>81 08 50 01 01 00 C2 C2 C2 C2</td>
</tr>
<tr>
<td>83</td>
<td>02</td>
<td>Public Key Info</td>
<td>B</td>
<td>R</td>
<td>83 02 10 04</td>
</tr>
<tr>
<td>84</td>
<td>40</td>
<td>Public Key, 64 bytes for ECDSA Curve P-256</td>
<td>B</td>
<td>R</td>
<td>84 40 then 64 bytes</td>
</tr>
<tr>
<td>86</td>
<td>00</td>
<td>Reserved for RSA cipher</td>
<td>B</td>
<td>O</td>
<td>86 00</td>
</tr>
<tr>
<td>90</td>
<td>04</td>
<td><p>Signing Miniature Certificate ID</p>
<p>Signed by Base Miniature Certificate</p></td>
<td>B</td>
<td>R</td>
<td>90 04 CA CA CA CA</td>
</tr>
<tr>
<td>91</td>
<td>01</td>
<td><p>Signing Algorithm</p>
<p>SHA-256, ECDSA Curve P-256</p></td>
<td>B</td>
<td>R</td>
<td>91 01 01</td>
</tr>
<tr>
<td>9E</td>
<td>40</td>
<td><p>Signature</p>
<p>(64 bytes for ECDSA P-256)</p></td>
<td>B</td>
<td>R</td>
<td>9E 40 then 64 bytes</td>
</tr>
<tr>
<td colspan="6"><p>Padding</p>
<p>Pad with 0xCA to make the total length of the data object 512
bytes.</p></td>
</tr>
</tbody>
</table>

### Firmware File Type (MAGTEK INTERNAL ONLY)

Please refer to ***D100006342 DYNAFLEX, DYNAPROX, DYNAFLEX II GO FAMILY
EMV CONTACTLESS/NFC CARD READER AND WRITER DEVICE FIRMWARE UPDATE
PROCESS,*** for more information on Firmware File Types.

### TrackType Type (MAGTEK INTERNAL ONLY FOR NOW)

The **TrackType** TLV data object is used to define magnetic stripe data
and variations thereof.

Table 63 - Response Track Type

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 61%" />
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
<td>81</td>
<td>04</td>
<td>Track Data Descriptor</td>
<td></td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Track ID</p>
<ul>
<li><p>0x00 = Reserved</p></li>
<li><p>0x01 = Track 1</p></li>
<li><p>0x02 = Track 2</p></li>
<li><p>0x03 = Track 3</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Track Status</p>
<ul>
<li><p>0x00 = OK</p></li>
<li><p>0x01 = Empty</p></li>
<li><p>0x02 = Disabled</p></li>
<li><p>0x81 = No Start Sentinel</p></li>
<li><p>0x82 = No End Sentinel</p></li>
<li><p>0x83 = Bad Parity</p></li>
<li><p>0x84 = Bad LRC</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Track Encoding</p>
<ul>
<li><p>0x05 = 5-bit Encoding</p></li>
<li><p>0x07 = 7-bit Encoding</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Track Data Format (ORed bits)</p>
<ul>
<li><p>OR 0b00000001 = No Start Sentinel</p></li>
<li><p>OR 0b00000010 = No End Sentinel</p></li>
<li><p>OR 0b00000100 = No LRC</p></li>
<li><p>OR 0b00001000 = No Masking</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td><p>Track Data</p>
<p>ASCII characters, no null at end</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
</tbody>
</table>

### CardData Type (MAGTEK INTERNAL ONLY FOR NOW)

The **CardData** TLV data object is used to contain all available
information about non-EMV cards.

Table 64 - Response Card Data Type (wip)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 63%" />
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
<td>81</td>
<td>04</td>
<td>Card Data Descriptor</td>
<td></td>
<td>R</td>
<td>See below.</td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Status</p>
<ul>
<li><p>0x00 = OK</p></li>
<li><p>0x80 = No Data (occurs when send track errors needed)</p></li>
</ul></td>
<td></td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Source</p>
<ul>
<li><p>0x01 = Swipe</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Card Type</p>
<ul>
<li><p>0x00 = Unknown</p></li>
<li><p>0x01 = ISO</p></li>
<li><p>0x02 = AAMVA</p></li>
<li><p>0x03 = Other</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td>Reserved, set to 0x00</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>A4</td>
<td></td>
<td>List of Track Types</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/A0</td>
<td></td>
<td>Track x</td>
<td>*</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/A0</td>
<td></td>
<td>Track y</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/A0</td>
<td></td>
<td>Track z</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>A6</td>
<td></td>
<td>List of Encrypted Block Types - SRED + TBD</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/80</td>
<td></td>
<td>Enc Block 1</td>
<td>*</td>
<td></td>
<td></td>
</tr>
<tr>
<td>/80</td>
<td></td>
<td>Enc Block ..n</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

P5 List of Encrypted Blocks

- List elements are each tagged with P0.

- The assumption is that data using the same crypto info would exist in
  one block.

- An example of multiple blocks encrypted under different keys would be
  track data vs MagnePrint.

EncryptedBlockType - tbd

- P1 - Encrypt Info

  - P1 - Algorithm

  - P2 - Padding method (default to PKCS7)

  - P3 - KSN or Key ID

  - P4 - IV

- P2 - List of encrypted elements

  - IV?

  - Unencrypted Length

  - Data elements ID

  - Encrypted Data

### TagsType Type (MAGTEK INTERNAL ONLY FOR NOW)

The **TagsType** TLV data object is used to contain unstructured lists
of tag/value pairs, for example, for reading or writing the contents of
tag databases used to configure EMV terminal and application settings.

### TLVType Type (MAGTEK INTERNAL ONLY FOR NOW)

The **TLVType** data object is used to contain structured TLV objects,
for example, for conveying the data used in processing EMV transactions.

### Common File Structure

Some files types conform to the common file structure format that
follows.

The following is a list of file types that conform to this format.

1)  EMV file types

2)  **Certificate File Types**

3)  **Certificate Signing Request (CSR) File Types**

<table>
<caption><p>Table 65 - Common File Structure</p></caption>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 61%" />
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
<td colspan="6"><strong>MGTKAP10</strong> = Start Of File Marker</td>
</tr>
<tr>
<td>C1</td>
<td>4</td>
<td><p>File Type</p>
<p>See ­Table 196</p></td>
<td>B</td>
<td>R</td>
<td>N/A</td>
</tr>
<tr>
<td>CE</td>
<td>var</td>
<td><p>File Payload</p>
<p>See the “File Type” subsections of section <strong>4 Data Types and
Shared TLV Data Objects</strong>.</p></td>
<td>B</td>
<td>R</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### Certificate File Types

These file types are listed in ­Table 196.

These file types conform to the **Common File Structure** format.

The File Payload of these files contain a certificate in PEM format.

Certificates must be loaded into the device in the order of trust
starting with the root CA, next intermediate CA(s) and ending with the
leaf (server or client for example) so that the device can verify the
signature of each certificate. If the certificates are not loaded in
order, they will be rejected.

When loading a server cert, the associated key pair must already exist
in the device as the CSR keys or as the existing server or client cert
and will be used to verify that the public key contained in the
certificate is correct. If the keys don’t match the certificate will be
rejected. If the certificate is associated with the CSR keys, the CSR
keys will be associated with the certificate and will no longer be
available for other certificates until re-generated.

Initial server or client certificates can not be loaded until the
respective CSR keys and CSR is generated.

To generate a CSR see **Command 0xEF03 – Generate CSR (WLAN Only)**.

### Certificate Signing Request (CSR) File Types

These file types are listed in ­Table 196.

These file types conform to the **Common File Structure** format.

The File Payload of these files contain a certificate signing request in
PEM format.

To generate a CSR see **Command 0xEF03 – Generate CSR (WLAN Only)**.

The device will erase the CSR file from volatile memory after the host
fetches it with **Command 0xD821 - Start Get File from Device**. After
fetching the CSR, the keys used to generate the CSR will still exist in
non-volatile memory associated with a CSR and can be used to generate a
new CSR if needed.

### UI Configuration File Type (MAGTEK INTERNAL ONLY)

The UI configuration file will be in the following 3 file format during
it’s life time:

1)  Text or .csv file.

2)  TLV binary file.

3)  Signed UI configuration file.

The UI Configuration file may contain maximum 300 items (valid String
IDs from 0x0000 to 0x012B, and maximum String length is 30 characters).

The MagTek software tool will convert the “Text or .csv file” to the
“TLV binary file”, and then sign the “TLV binary file” into “Signed UI
configuration file”.

An example of a Text file displayed in ASCII format. (file name:
CFG0006869-100.xxx)

DISPLAY STRING ID, DISPLAY STRING

0000,

0000,Thank You

0002,See You!

0003,Hello!

0004,Please Select

0005,Please Select An Amount

0006,Please Select A Tip Amount

0007,Touch Screen To Continue

0008,Cancel

0009,Service Request

000A,Show More

000B,Options

000C,What is the issue?

000D,Exit

000E,No hot water

000F,Doesn’t spin

0010,Water leakage

0011,Request

The Text file below is displayed in Hex format.

<img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image2.png"
style="width:4.5974in;height:3.12795in"
alt="A screenshot of a computer Description automatically generated" />

The MagTek software tool will convert the above Text file into “TLV
binary file”.

This Text file has 18 items, each item contains a two-byte Tag, one-byte
Length, and variable-length of Value.

For example, the first TLV item is 00 00 01 20.

00 00 01 20 00 01 09 54 68 61 6e 6b 20 59 6f 75

00 02 08 53 65 65 20 59 6f 75 21 00 03 06 48 65

6c 6c 6f 21 00 04 0d 50 6c 65 61 73 65 20 53 65

6c 65 63 74 00 05 17 50 6c 65 61 73 65 20 53 65

6c 65 63 74 20 41 6e 20 41 6d 6f 75 6e 74 00 06

1a 50 6c 65 61 73 65 20 53 65 6c 65 63 74 20 41

20 54 69 70 20 41 6d 6f 75 6e 74 00 07 18 54 6f

75 63 68 20 53 63 72 65 65 6e 20 54 6f 20 43 6f

6e 74 69 6e 75 65 00 08 06 43 61 6e 63 65 6c 00

09 0f 53 65 72 76 69 63 65 20 52 65 71 75 65 73

74 00 0a 09 53 68 6f 77 20 4d 6f 72 65 00 0b 07

4f 70 74 69 6f 6e 73 00 0c 12 57 68 61 74 20 69

73 20 74 68 65 20 69 73 73 75 65 3f 00 0d 04 45

78 69 74 00 0e 0c 4e 6f 20 68 6f 74 20 77 61 74

65 72 00 0f 0c 44 6f 65 73 6e 27 74 20 73 70 69

6e 00 10 0d 57 61 74 65 72 20 6c 65 61 6b 61 67

65 00 11 07 52 65 71 75 65 73 74

The MagTek software tool will generate a secure header and sign the “TLV
binary file” (the payload) into the

“Signed UI configuration file”. The format of the “Signed UI
configuration file” is shown in Table 66 - Format of a Signed UI
Configuration File.

#### Process UI Configuration File

##### Step 1: Convert Text File Into a Binary File

| THE LEFT HAND SIDE DISPLAYS THE CONTENTS | THE RIGHT HAND SIDE DISPLAYS THE HEX VALUES OF THE TEXT FILE GENERATED BY EDIT. |
|----|----|
| <img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image3.png"
style="width:2.03889in;height:2.825in"
alt="A screenshot of a computer screen Description automatically generated" /> | <img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image2.png"
style="width:4.10417in;height:2.79236in"
alt="A screenshot of a computer Description automatically generated" /> |
| Note: Please be aware of the fact that Item ID 0000 has the content of 0x20 (space) |  |

###### Example \#1

Text Input (ASCII): 0001,Thank You

Text Input (Binary): 30303031215468616E6B20596F750D0A

Binary Output: 0001095468616E6B20596F75

09 is the number of bytes in the message string.

5468616E6B20596F75 is the ASCII code of Thank You.

###### Example \#2:

Text Input (ASCII): 0002,See You!

Text Input (Binary): 303030322153656520596F75210D0A

Binary Output: 00020853656520596F7521

08 is the number of bytes in the message string.

53656520596F7521 is the ASCII code of See You!.

###### Example \#3:

Text Input (ASCII): 0001,Thank You

0002,See You!

Binary Output: 0001095468616E6B20596F7500020853656520596F7521

If the text file only contains 2 items, then the above Binary Output is
the payload for signing.

A UI Configuration file may contain maximum 300 items.

**Note**: For each iteam, ID has 2 bytes, Length has 1 byte, Message
String has \<= 30 bytes.

Test file in Hex values:

30 30 30 30 2c 20 0d 0a

30 30 30 31 2c 54 68 61 6e 6b 20 59 6f 75 0d 0a

30 30 30 32 2c 53 65 65 20 59 6f 75 21 0d 0a

30 30 30 33 2c 48 65 6c 6c 6f 21 0d 0a

30 30 30 34 2c 50 6c 65 61 73 65 20 53 65 6c 65 63 74 0d 0a

30 30 30 35 2c 50 6c 65 61 73 65 20 53 65 6c 65 63 74 20 41 6e 20 41 6d
6f 75 6e 74 0d 0a

30 30 30 36 2c 50 6c 65 61 73 65 20 53 65 6c 65 63 74 20 41 20 54 69 70
20 41 6d 6f 75 6e 74 0d 0a

30 30 30 37 2c 54 6f 75 63 68 20 53 63 72 65 65 6e 20 54 6f 20 43 6f 6e
74 69 6e 75 65 0d 0a

30 30 30 38 2c 43 61 6e 63 65 6c 0d 0a

30 30 30 39 2c 53 65 72 76 69 63 65 20 52 65 71 75 65 73 74 0d 0a

30 30 30 41 2c 53 68 6f 77 20 4d 6f 72 65 0d 0a

30 30 30 42 2c 4f 70 74 69 6f 6e 73 0d 0a

30 30 30 43 2c 57 68 61 74 20 69 73 20 74 68 65 20 69 73 73 75 65 3f 0d
0a

30 30 30 44 2c 45 78 69 74 0d 0a

30 30 30 45 2c 4e 6f 20 68 6f 74 20 77 61 74 65 72 0d 0a

30 30 30 46 2c 44 6f 65 73 6e 27 74 20 73 70 69 6e 0d 0a

30 30 31 30 2c 57 61 74 65 72 20 6c 65 61 6b 61 67 65 0d 0a

30 30 31 31 2c 52 65 71 75 65 73 74

The Text file has been converted into binary file: (.bin):

00 00 01 20 00 01 09 54 68 61 6e 6b 20 59 6f 75

00 02 08 53 65 65 20 59 6f 75 21 00 03 06 48 65

6c 6c 6f 21 00 04 0d 50 6c 65 61 73 65 20 53 65

6c 65 63 74 00 05 17 50 6c 65 61 73 65 20 53 65

6c 65 63 74 20 41 6e 20 41 6d 6f 75 6e 74 00 06

1a 50 6c 65 61 73 65 20 53 65 6c 65 63 74 20 41

20 54 69 70 20 41 6d 6f 75 6e 74 00 07 18 54 6f

75 63 68 20 53 63 72 65 65 6e 20 54 6f 20 43 6f

6e 74 69 6e 75 65 00 08 06 43 61 6e 63 65 6c 00

09 0f 53 65 72 76 69 63 65 20 52 65 71 75 65 73

74 00 0a 09 53 68 6f 77 20 4d 6f 72 65 00 0b 07

4f 70 74 69 6f 6e 73 00 0c 12 57 68 61 74 20 69

73 20 74 68 65 20 69 73 73 75 65 3f 00 0d 04 45

78 69 74 00 0e 0c 4e 6f 20 68 6f 74 20 77 61 74

65 72 00 0f 0c 44 6f 65 73 6e 27 74 20 73 70 69

6e 00 10 0d 57 61 74 65 72 20 6c 65 61 6b 61 67

65 00 11 07 52 65 71 75 65 73 74

##### Step 2: Sign the Binary Output File

This signing process is very similar to the Image Signing process.

Assume the Text file name is CFG0006869-100.xxx, then CFG0006869-100 (in
ASCII format) will be placed in the Required String 1. And, CFG0006869
is the part number, 100 is the revision number.

The Host App may retrieve this information (CFG0006869-100) from OID
0x020102080101.

<table>
<caption><p>Table 66 - Format of a Signed UI Configuration
File</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 31%" />
<col style="width: 19%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th>Len</th>
<th>Description</th>
<th style="text-align: center;">Value (example)</th>
<th style="text-align: center;">Offset</th>
</tr>
</thead>
<tbody>
<tr>
<td>N/A</td>
<td>8</td>
<td><p>Apollo File Marker:</p>
<p>‘MGTKAP10’</p></td>
<td style="text-align: center;"><p>4D 47 54 4B</p>
<p>41 50 31 30</p></td>
<td style="text-align: center;">0000 - 0007</td>
</tr>
<tr>
<td>C1</td>
<td>4</td>
<td>File ID</td>
<td style="text-align: center;"><p>C1 04</p>
<p>06 00 00 00</p></td>
<td style="text-align: center;">0008 – 000D</td>
</tr>
<tr>
<td>E3</td>
<td><p>sum</p>
<p> </p></td>
<td><p>File Description Strings</p>
<p>Required String 1: CFG0006869-100</p>
<p>Optional String 2</p>
<p>Optional String 3</p></td>
<td style="text-align: center;"><p>E3 14</p>
<p>81 0E 14bytes</p>
<p>82 00</p>
<p>83 00</p></td>
<td style="text-align: center;">000E – 0023</td>
</tr>
<tr>
<td>E5</td>
<td>sum</td>
<td>File Manifest</td>
<td style="text-align: center;">E5 1A</td>
<td style="text-align: center;">0024 – 0025</td>
</tr>
<tr>
<td>81</td>
<td>4</td>
<td><p>Product/Module Type</p>
<p>00 00: UI Config File</p>
<p>02 00: Main App</p></td>
<td style="text-align: center;"><p>81 04</p>
<p>00 00</p>
<p>02 00</p></td>
<td style="text-align: center;">0026 – 002B</td>
</tr>
<tr>
<td>82</td>
<td>2</td>
<td><p>Payload Type</p>
<p>0000: uncompressed</p></td>
<td style="text-align: center;"><p>82 02</p>
<p>00 00</p></td>
<td style="text-align: center;">002C – 002F</td>
</tr>
<tr>
<td>83</td>
<td>4</td>
<td><p>Payload Offset</p>
<p>Offset is 0x00000200</p></td>
<td style="text-align: center;"><p>83 04</p>
<p>00 00 02 00</p></td>
<td style="text-align: center;">0030 - 0035</td>
</tr>
<tr>
<td>86</td>
<td>4</td>
<td>Customer ID</td>
<td style="text-align: center;"><p>86 04</p>
<p>00 00 00 00</p></td>
<td style="text-align: center;">0036 – 003B</td>
</tr>
<tr>
<td>A8</td>
<td>v</td>
<td>Constraints</td>
<td style="text-align: center;">A8 00</td>
<td style="text-align: center;">003C – 003D</td>
</tr>
<tr>
<td>A9</td>
<td>v</td>
<td>Extra Operations</td>
<td style="text-align: center;">A9 00</td>
<td style="text-align: center;">003E – 003F</td>
</tr>
<tr>
<td>E7</td>
<td>sum</td>
<td>File Security</td>
<td style="text-align: center;">E7 81 DF</td>
<td style="text-align: center;">0040 – 0042</td>
</tr>
<tr>
<td>81</td>
<td>4</td>
<td><p>Sequence Number</p>
<p># = 0xnm</p></td>
<td style="text-align: center;"><p>81 04</p>
<p>00 00 00 nm</p></td>
<td style="text-align: center;">0043 – 0048</td>
</tr>
<tr>
<td>82</td>
<td>4</td>
<td>Time Stamp</td>
<td style="text-align: center;"><p>82 04</p>
<p>5f 18 88 10</p></td>
<td style="text-align: center;">0049 – 004E</td>
</tr>
<tr>
<td>84</td>
<td>1</td>
<td><p>Hash Algorithm</p>
<p>0x04 = SHA-256</p></td>
<td style="text-align: center;"><p>84 01</p>
<p>04</p></td>
<td style="text-align: center;">004F - 0051</td>
</tr>
<tr>
<td>85</td>
<td>4</td>
<td>Payload Length</td>
<td style="text-align: center;"><p>85 04</p>
<p>00 00 WX YZ</p></td>
<td style="text-align: center;">0052 - 0057</td>
</tr>
<tr>
<td>86</td>
<td>32</td>
<td><p>Payload Hash Checksum</p>
<p>(Note 1)</p></td>
<td style="text-align: center;"><p>86 20</p>
<p>plus 32 bytes</p></td>
<td style="text-align: center;">0058 – 0079</td>
</tr>
<tr>
<td>88</td>
<td>159</td>
<td><p>Signing mini-cert</p>
<p>159 bytes of Certificate, see 4.20 Miniature Certificate
Type.</p></td>
<td style="text-align: center;"><p>88 81 9F</p>
<p>plus 159 bytes</p></td>
<td style="text-align: center;">007A – 011B</td>
</tr>
<tr>
<td>89</td>
<td>4</td>
<td><p>Signature OP,</p>
<p>Data Sig + ECDSA + P256 + SHA256 (Note 2)</p></td>
<td style="text-align: center;"><p>89 04</p>
<p>10 01 03 04</p></td>
<td style="text-align: center;">011C - 0121</td>
</tr>
<tr>
<td>CC</td>
<td>64</td>
<td><p>Signature</p>
<p>64 bytes of signature</p></td>
<td style="text-align: center;"><p>CC 40</p>
<p>plus 64 bytes</p></td>
<td style="text-align: center;">0122 – 0163</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>512-byte Alignment</td>
<td style="text-align: center;">File up 0xFF</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td> </td>
<td> </td>
<td><p>Payload</p>
<p>(TLV binary file)</p></td>
<td style="text-align: center;">0xWXYZ bytes</td>
<td style="text-align: center;">0200 – End of File</td>
</tr>
<tr>
<td colspan="5"><p><strong>Note 1</strong>: “Payload Hash Checksum”
include all the bytes of the “TLV binary file”.</p>
<p><strong>Note 2</strong>: Hash Checksum for the signature include the
bytes starts from 0x0000 to 0x121.</p></td>
</tr>
</tbody>
</table>

Host application sends the “Signed UI configuration file” to the device
with 0xD812 command

File ID for UI Configuration File is 0x06000000.

<table>
<caption><p>Table 67 - Format of an UI Configuration File Signing
Mini-cert Signed by the Base Mini-cert</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 28%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th>Len</th>
<th>Description</th>
<th style="text-align: center;">Value (example)</th>
<th style="text-align: center;">Offset</th>
</tr>
</thead>
<tbody>
<tr>
<td>FF01</td>
<td>N/A</td>
<td>Mini-cert Marker</td>
<td style="text-align: center;">FF,91</td>
<td style="text-align: center;">0000 - 0001</td>
</tr>
<tr>
<td>81</td>
<td>8</td>
<td>Mini-cert Info and ID</td>
<td style="text-align: center;"><p>81,08,</p>
<p>50,01,01,00</p>
<p>C2,C2,C2,C2</p></td>
<td style="text-align: center;">0002 – 000B</td>
</tr>
<tr>
<td>83</td>
<td>2</td>
<td>Public Key Info</td>
<td style="text-align: center;">83,02,10,04</td>
<td style="text-align: center;">000C – 000F</td>
</tr>
<tr>
<td>84</td>
<td>64</td>
<td>Public Key, 64 bytes for ECDSA Curve P-256</td>
<td style="text-align: center;"><p>84,40,</p>
<p>64 bytes</p></td>
<td style="text-align: center;">0010 – 0051</td>
</tr>
<tr>
<td>86</td>
<td>0</td>
<td>Reserved for RSA cipher</td>
<td style="text-align: center;">86,00</td>
<td style="text-align: center;">0052 – 0053</td>
</tr>
<tr>
<td>90</td>
<td>4</td>
<td><p>Signing Mini-cert ID</p>
<p>(signed by Base mini-cert)</p></td>
<td style="text-align: center;"><p>90,04,</p>
<p>CA,CA,CA,CA</p></td>
<td style="text-align: center;">0054 – 0059</td>
</tr>
<tr>
<td>91</td>
<td>1</td>
<td><p>Signing Algorithm</p>
<p>SHA-256, ECDSA Curve P-256</p></td>
<td style="text-align: center;"><p>91,01,</p>
<p>01</p></td>
<td style="text-align: center;">005A – 005C</td>
</tr>
<tr>
<td>9E</td>
<td>64</td>
<td><p>Signature</p>
<p>(64 bytes for ECDSA P-256)</p></td>
<td style="text-align: center;"><p>9E,40,</p>
<p>64 bytes</p></td>
<td style="text-align: center;">005D – 009E</td>
</tr>
</tbody>
</table>

##### Step 3: Send the Signed UI Configuration File to the Device with 0xd812 Command

File ID for UI Configuration File is 0x06000000.

Send the signed UI Configuration File to the device with MagTek DTE App.

#### Authenticate and Save the signed UI configuration file

**The Device Will Verify the Mini cert in the Signed UI Configuration
File as Follows:**

- Step \#1: Fetch the Base mini-cert Public Key from the Base mini-cert
  resides in the Boot-0 image.

- Step \#2: Hash the Signing mini-cert (exclude the Signature TLV) into
  sha_cksum\[32\], it is a 32-byte array holds the result of SHA-256
  operation. These Hash operation parameters are derived from the
  Signing mini-cert in the secure header of the signed UI configuration
  file.

- Step \#3: Initialize ECDSA context.

- Step \#4: Load NIST EC Curve P-256 parameters into ECDSA context.

- Step \#5: Load Base mini-cert Public Key fetched in Step \#1 into
  ECDSA context.

- Step \#6: Load sha_cksum\[32\] and signature into ECDSA context. These
  signature validation parameters are derived from the Signing mini-cert
  in the secure header of the signed UI configuration file.

- Step \#7: Validate the signature per SECG – SEC1 Elliptic Curve
  Cryptography, Version 2.0, Section 4.1.4. (SECG = Standards for
  Efficient Cryptography Group)

**Verify the Signature of the Signed UI Configuration File:**

- Step \#1: Hash the payload into sha_cksum\[32\], it is a 32-byte array
  holds the result of SHA-256 operation on the payload. These Hash
  operation parameters are derived from the secure header of the signed
  UI configuration file, such as Signature Algorithm, Payload Offset,
  Payload Size, and the Payload.

- Step \#2: Verify the contents of sha_cksum\[32\] from Step \#1 match
  the contents of Payload Hash Checksum in the secure header.

- Step \#3: Hash the secure header (exclude the signature TLV) into
  sha_cksum\[32\].

- Step \#4: Initialize ECDSA context.

- Step \#5: Load NIST EC Curve P-256 parameters into ECDSA context.

- Step \#6: Get the UI configuration file Authentication Public Key from
  the Signing mini-cert in the secure header, load this Key into ECDSA
  context.

- Step \#7: Get the signature from the secure header, load
  sha_cksum\[32\] and signature into ECDSA context. These signature
  validation parameters are derived from the secure header of the signed
  UI configuration file, such as Signature Algorithm, Signature Offset,
  Signature Size, and the Signature.

- Step \#8: Validate the signature per SECG – SEC1 Elliptic Curve
  Cryptography, Version 2.0, Section 4.1.4. (SECG = Standards for
  Efficient Cryptography Group)

Save the signed UI configuration file and the Part Number and Revision
to the file system.

#### Self-Authenticate the Saved UI Configuration File 

During power-up, the device will retrieve and authenticate the saved UI
configuration file. The device will read the signed UI configuration
file, and then authenticate the file the same way as described **Step 3:
Send the Signed UI Configuration File to the Device with 0xd812
Command.**

### Card Emulation

#### Card Emulation Overview

Card emulation enables a DynaFlex/DynaProx device to simulate a Type 4
smart card. The emulated card has the following characteristics:

- Compliance: Card emulation conforms to ISO/IEC 14443 Type-A and NFC
  Forum Type 4 standards.

- Passive Operation: The emulated card functions in passive mode. The
  phone is responsible for generating the magnetic field required to
  activate the simulated card.

- Read-Only: The emulated card is read-only and does not support
  writing.

- Supported Data Type: Supports the URI (URL) data type.

#### Device Compatibility 

- iPhone Support: NFC card reading was introduced on Apple iPhones
  starting with the iPhone 7.

- Android Support: Android added NFC support in 2012; however,
  compatibility depends on the specific phone model and hardware
  capabilities. Most Android phones released since 2016 support NFC.
  Verify with the phone’s manufacturer to confirm compatibility.

- Google Pay Indicator: If a phone supports Google Pay, it is likely
  capable of reading NFC tags.