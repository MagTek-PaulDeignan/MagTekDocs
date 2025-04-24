---
title: Command Group 0x11nn - NFC/MIFARE Pass Through Commands (Contactless Only)
layout: home
parent: Commands
nav_order: 2
---

## Command Group 0x11nn - NFC/MIFARE Pass Through Commands (Contactless Only)

---

- [Command Group 0x11nn - NFC/MIFARE Pass Through Commands (Contactless Only)](#command-group-0x11nn---nfcmifare-pass-through-commands-contactless-only)
    - [Command 0x1100 – Pass Through Command For NTag/MIFARE Ultralight, Type 2](#command-0x1100-–-pass-through-command-for-ntagmifare-ultralight,-type-2)
      - [Encrypted Data Format](#encrypted-data-format)
    - [Command 0x1101 – Pass Through Command for MIFARE Classic/MINI®/Plus SL1 (Security Level 1), Type 2](#command-0x1101-–-pass-through-command-for-mifare-classicmini®plus-sl1-security-level-1,-type-2)
      - [Encrypted Data Format](#encrypted-data-format)
    - [Command 0x1102 – Pass Through Command for MIFARE DESFire, Type 4](#command-0x1102-–-pass-through-command-for-mifare-desfire,-type-4)
      - [Encrypted Data Format](#encrypted-data-format)
    - [Command 0x1103 – Pass Through Command for MIFARE Plus, Type 2](#command-0x1103-–-pass-through-command-for-mifare-plus,-type-2)
      - [Encrypted Data Format](#encrypted-data-format)

---


#### Command 0x1100 – Pass Through Command For NTag/MIFARE Ultralight, Type 2

After an NTag/MIFARE Ultralight is activated, the host uses this command
to send commands and receive responses to and from a Ntag/MIFARE
Ultralight. Do not change the address 0x00 for read protection of
Ultralight C/AES card because the device will fail to access the card if
the address 0x00 is read protected.

Table 82 - Request Data for Command 0x1100 – Pass Through Command For
NTag/MIFARE Ultralight, Type 2.

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
<td colspan="6">Beginning of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message">23</a></td>
</tr>
<tr>
<td colspan="6">1100 = <strong>Command 0x1100 – Pass Through Command For
NTag/MIFARE Ultralight, Type</strong> 2</td>
</tr>
<tr>
<td>81</td>
<td>var</td>
<td><p>Command to Send.</p>
<p>See <strong>Table 83 – NTag Commands</strong></p>
<p>See <strong>Table 84 – MIFARE Ultralight EV1 Commands</strong></p>
<p>See <strong>Table 85 – MIFARE Ultralight C Commands</strong></p>
<p>See <strong>Table 86 – MIFARE Ultralight AES
Commands</strong></p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>01</td>
<td><p>00 – No Encrypt</p>
<p>01 - Encrypt</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>01</td>
<td><p>00 – Expect More Commands</p>
<p>01 – FF (Last Command)</p>
<p>If the pass-through command is the last successful command, the
device will end the transaction with a single beep, indicating success.
If an error arises, the device will end the transaction but will sound
two beeps to indicate the error. The user should then remove the
card.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including Request
Message found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 83 – NTag Commands

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 13%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr>
<th>Command</th>
<th>Length</th>
<th>Field Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Get Version</td>
<td>1</td>
<td><p>The GET_VERSION command is used to retrieve information on the
NTAG family, the product version, storage size and other product data
required to identify the specific NTAG21x.</p>
<p>Byte 0 = 0x60</p></td>
</tr>
<tr>
<td>Read</td>
<td>2-3</td>
<td><p>The READ command requires a start page address, and returns the
16 bytes of four NTAG21x pages. For example, if address is 03h then
pages 03h, 04h, 05h, 06h are returned. Special conditions apply if the
READ command address is near the end of the accessible memory area. The
special conditions also apply if at least part of the addressed pages is
within a password protected area.</p>
<p>The READ command with an option of end page address returns the all
n*4 bytes of the addressed pages. For example if the start address is
03h and the end address is 07h then pages 03h, 04h, 05h, 06h and 07h are
returned.</p>
<p>Byte 0 = 0x30</p>
<p>Byte 1 = Start Page Address</p>
<p>Byte 2 = (optional) End Page Address</p></td>
</tr>
<tr>
<td>Fast Read</td>
<td>3</td>
<td><p>The FAST_READ command requires a start page address and an end
page address and returns the all n*4 bytes of the addressed pages. For
example, if the start address is 03h and the end address is 07h then
pages 03h, 04h, 05h, 06h and 07h are returned.</p>
<p>Byte 0 = 0x3A</p>
<p>Byte 2 = Start Page Address</p>
<p>Byte 3 = End Page Address</p></td>
</tr>
<tr>
<td>Write</td>
<td>6</td>
<td><p>The WRITE command requires a block address, and writes 4 bytes of
data into the addressed NTAG21x page.</p>
<p>Byte 0 = 0xA2</p>
<p>Byte 1 = Address to Write</p>
<p>Byte 2 to 5 = 4 Bytes of Data to Write</p></td>
</tr>
<tr>
<td><p>Compatibility</p>
<p>Write</p></td>
<td>18</td>
<td><p>The COMPATIBILITY_WRITE command is implemented to guarantee
interoperability with the established MIFARE Classic PCD infrastructure,
in case of coexistence of ticketing and NFC applications. Even though 16
bytes are transferred to NTAG21x, only the least significant 4 bytes
(bytes 0 to 3) are written to the specified address. Set all the
remaining bytes, 04h to 0Fh, to logic 00h.</p>
<p>Byte 0 = 0xA0</p>
<p>Byte 1 = Address to Write</p>
<p>Byte 2 to 17 = 16 Bytes of Data to Write (only least significant 4
bytes are written)</p>
<p>Note: This command is sent in 2 steps, which the Firmware will
handle</p>
<ol type="1">
<li><p>&lt;CMD&gt;&lt;Address to
Write&gt;&lt;CRCH&gt;&lt;CRCL&gt;</p></li>
<li><p>&lt;16 Bytes of Data to
Write&gt;&lt;CRCH&gt;&lt;CRCL&gt;</p></li>
</ol></td>
</tr>
<tr>
<td>READ_CNT</td>
<td>2</td>
<td><p>The READ_CNT command is used to read out the current value of the
NFC one-way counter of the NTAG213, NTAG215 and NTAG216. The command has
a single argument specifying the counter number and returns the 24-bit
counter value of the corresponding counter. If the NFC_CNT_PWD_PROT bit
is set to 1b the counter is password protected and can only be read with
the READ_CNT command after a previous valid password authentication</p>
<p>Byte 0 = 0x39</p>
<p>Byte 1 = 0x02 (NFC Counter Address)</p></td>
</tr>
<tr>
<td>PWD_AUTH</td>
<td>5</td>
<td><p>A protected memory area can be accessed only after a successful
password verification using the PWD_AUTH command. The AUTH0
configuration byte defines the protected area. It specifies the first
page that the password mechanism protects. The level of protection can
be configured using the PROT bit either for write protection or
read/write protection. The PWD_AUTH command takes the password as
parameter and, if successful, returns the password authentication
acknowledge, PACK. By setting the AUTHLIM configuration bits to a value
larger than 000b, the number of unsuccessful password verifications can
be limited. Each unsuccessful authentication is then counted in a
counter featuring anti-tearing support. After reaching the limit of
unsuccessful attempts, the memory access specified in PROT, is no longer
possible.</p>
<p>Byte 0 = 0x1B</p>
<p>Byte 1..4 = password (4 bytes)</p></td>
</tr>
<tr>
<td>READ_SIG</td>
<td>2</td>
<td><p>The READ_SIG command returns an IC specific, 32-byte ECC
signature, to verify NXP Semiconductors as the silicon vendor. The
signature is programmed at chip production and cannot be changed
afterwards.</p>
<p>Byte 0 = 0x3C</p>
<p>Byte 1 = 0x00, RFU</p></td>
</tr>
</tbody>
</table>

Table 84 – MIFARE Ultralight EV1 Commands

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 11%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr>
<th>Command</th>
<th>Length</th>
<th>Field Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Get Version</td>
<td>1</td>
<td><p>The GET_VERSION command is used to retrieve information on the
MIFARE family, product version, storage size and other product data
required to identify the MF0ULx1.</p>
<p>Byte 0 = 0x60</p></td>
</tr>
<tr>
<td>Read</td>
<td>2-3</td>
<td><p>The READ command requires a start page address, and returns the
16 bytes of four MIFARE Ultralight pages. For example if address (Addr)
is 03h then pages 03h, 04h, 05h, 06h are returned. A rollover mechanism
is implemented if the READ command address is near the end of the
accessible memory area. This rollover mechanism is also used when at
least part of the addressed pages is within a password protected
area.</p>
<p>The READ command with an option of end page address returns the all
n*4 bytes of the addressed pages. For example if the start address is
03h and the end address is 07h then pages 03h, 04h, 05h, 06h and 07h are
returned.</p>
<p>Byte 0 = 0x30</p>
<p>Byte 1 = Start Page Address</p>
<p>Byte 2 = (optional) End Page Address</p></td>
</tr>
<tr>
<td>Fast Read</td>
<td>3</td>
<td><p>The FAST_READ command requires a start page address and an end
page address and returns the all n*4 bytes of the addressed pages. For
example if the start address is 03h and the end address is 07h then
pages 03h, 04h, 05h, 06h and 07h are returned.</p>
<p>Byte 0 = 0x3A</p>
<p>Byte 2 = Start Page Address</p>
<p>Byte 3 = End Page Address</p></td>
</tr>
<tr>
<td>Write</td>
<td>6</td>
<td><p>The WRITE command requires a block address, and writes 4 bytes of
data into the addressed MIFARE Ultralight EV1 page.</p>
<p>Byte 0 = 0xA2</p>
<p>Byte 1 = Address to Write</p>
<p>Byte 2 to 5 = 4 Bytes of Data to Write</p></td>
</tr>
<tr>
<td><p>Compatibility</p>
<p>Write</p></td>
<td>18</td>
<td><p>The COMPATIBILITY_WRITE command is implemented to accommodate the
established MIFARE Classic PCD infrastructure. Even though 16 bytes are
transferred to the MF0ULx1, only the least significant 4 bytes (bytes 0
to 3) are written to the specified address. Set all the remaining bytes,
04h to 0Fh, to logic 00h</p>
<p>Byte 0 = 0xA0</p>
<p>Byte 1 = Address to Write</p>
<p>Byte 2 to 17 = 16 Bytes of Data to Write (only least significant 4
bytes are written)</p>
<p>Note: This command is sent in 2 steps, which the Firmware will
handle</p>
<ol type="1">
<li><p>&lt;CMD&gt;&lt;Address to
Write&gt;&lt;CRCH&gt;&lt;CRCL&gt;</p></li>
<li><p>&lt;16 Bytes of Data to
Write&gt;&lt;CRCH&gt;&lt;CRCL&gt;</p></li>
</ol></td>
</tr>
<tr>
<td>READ_CNT</td>
<td>2</td>
<td><p>The READ_CNT command is used to read out the current value of one
of the 3 one-way counters of the MF0ULx1. The command has a single
argument specifying the counter number and returns the 24-bit counter
value of the corresponding counter. The counters are always readable,
independent on the password protection settings.</p>
<p>Byte 0 = 0x39</p>
<p>Byte 1 = 0x00..0x02 (counter number from 0x00 to 0x02)</p></td>
</tr>
<tr>
<td>INCR_CNT</td>
<td>6</td>
<td><p>The INCR_CNT command is used to increment one of the 3 one-way
counters of the MF0ULx1. The two arguments are the counter number and
the increment value.</p>
<p>Byte 0 = 0xA5</p>
<p>Byte 1 = 0x00..0x02 (counter number from 0x00 to 0x02)</p>
<p>Byte 2 to 5 = 4 bytes increment value (only the 3 least significant
bytes are relevant)</p></td>
</tr>
<tr>
<td>PWD_AUTH</td>
<td>5</td>
<td><p>A protected memory area can be accessed only after a successful
password verification using the PWD_AUTH command. The AUTH0
configuration byte defines the protected area. It specifies the first
page that the password mechanism protects. The level of protection can
be configured using the PROT bit either for write protection or read/
write protection. The PWD_AUTH command takes the password as parameter
and, if successful, returns the password authentication acknowledge,
PACK. By setting the AUTHLIM configuration bits to a value larger than
000b, the number of unsuccessful password verifications can be limited.
Each unsuccessful authentication is then counted in a counter featuring
anti-tearing support. After reaching the limit of unsuccessful attempts,
the memory access specified in PROT, is no longer possible.</p>
<p>Byte 0 = 0x1B</p>
<p>Byte 1..4 = password (4 bytes)</p></td>
</tr>
<tr>
<td>READ_SIG</td>
<td>2</td>
<td><p>The READ_SIG command returns an IC specific, 32-byte ECC
signature, to verify NXP Semiconductors as the silicon vendor. The
signature is programmed at chip production and cannot be changed
afterwards.</p>
<p>Byte 0 = 0x3C</p>
<p>Byte 1 = 0x00, RFU</p></td>
</tr>
<tr>
<td><p>CHECK</p>
<p>TEARING_EVENT</p></td>
<td>2</td>
<td><p>The CHECK_TEARING_EVENT command enables the application to
identify if a tearing event happened on a specified counter element. It
takes the counter number as single argument and returns a specified
valid flag for this counter. If the returned valid flag is not equal to
the predefined value, a tearing event happened. Note, although a tearing
event might have happened on the counter, a valid value corresponding to
the last valid counter status is still available using the READ_CNT
command.</p>
<p>Byte 0 = 0x3E</p>
<p>Byte 1 = 0x00..0x02 (counter number from 0x00 to 0x02)</p></td>
</tr>
<tr>
<td>VCSL</td>
<td>21</td>
<td><p>The VCSL command is used to enable a unique identification and
selection process across different MIFARE product-based cards and card
implementations on mobile devices. The command requires a 16-byte
installation identifier IID and a 4-byte PCD capability value as
parameters. The parameters are present to support compatibility to other
MIFARE product-based devices but are not used or checked inside the
MF0ULx1. Nevertheless, the number of bytes is checked for correctness.
The answer to the VCSL command is the virtual card type identifier
VCTID. This identifier indicates the type of card or ticket. Using this
information, the reader can decide whether the ticket belongs to the
installation or not.</p>
<p>Byte 0 = 0x4B</p>
<p>Byte 1 to 16 = 16-byte IID (installation identifier, can be any
number)</p>
<p>Byte 17 to 20 = 4-byte PCDCAPS (PCD capabilities, can be any
number)</p></td>
</tr>
</tbody>
</table>

Table 85 – MIFARE Ultralight C Commands

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr>
<th>Command</th>
<th>Length</th>
<th>Field Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Read</td>
<td>2-3</td>
<td><p>The READ command takes the page address as a parameter. Only
addresses 00h to 2Bh are decoded. For higher addresses the MF0ICU2
returns a NAK. The MF0ICU2 responds to the READ command by sending 16
bytes starting from the page address defined in the command (e.g. if ADR
is 03h, pages 03h, 04h, 05h, 06h are returned)</p>
<p>A roll-over mechanism is implemented to continue reading from page
00h once the end of the accessible memory is reached. For example,
reading from address 29h on a MF0ICU2 results in pages 29h, 2Ah, 2Bh and
00h being returned.</p>
<p>The following conditions apply if part of the memory is protected by
the 3DES authentication for read access:</p>
<p>• if the MF0ICU2 is in the ACTIVE state – addressing a page which is
equal or higher than AUTH0 results in a NAK response – addressing a page
lower than AUTH0 results in data being returned with the roll-over
mechanism occurring just before the AUTH0 defined page</p>
<p>• if the MF0ICU2 is in the AUTHENTICATED state – the READ command
behaves like on a MF0ICU2 without access protection.</p>
<p>The READ command with an option of end page address returns the all
n*4 bytes of the addressed pages. For example if the start address is
03h and the end address is 07h then pages 03h, 04h, 05h, 06h and 07h are
returned.</p>
<p>Byte 0 = 0x30</p>
<p>Byte 1 = Start Page Address</p>
<p>Byte 2 = (optional) End Page Address</p></td>
</tr>
<tr>
<td>Write</td>
<td>6</td>
<td><p>The WRITE command is used to program the lock bytes in page 02h,
the OTP bytes in page 03h, data bytes in pages 04h to 27h, configuration
data from page 28h to 2B and keys from page 2Ch to 2Fh. A WRITE command
is performed page-wise, programming 4 bytes in a page.</p>
<p>Byte 0 = 0xA2</p>
<p>Byte 1 = Address to Write</p>
<p>Byte 2 to 5 = 4 Bytes of Data to Write</p></td>
</tr>
<tr>
<td><p>Compatibility</p>
<p>Write</p></td>
<td>18</td>
<td><p>The COMPATIBILITY WRITE command was implemented to accommodate
the established MIFARE PCD infrastructure. Even though 16 bytes are
transferred to the MF0ICU2, only the least significant 4 bytes (bytes 0
to 3) will be written to the specified address. It is recommended to set
the remaining bytes 4 to 15 to all 0.</p>
<p>Byte 0 = 0xA0</p>
<p>Byte 1 = Address to Write</p>
<p>Byte 2 to 17 = 16 Bytes of Data to Write (only least significant 4
bytes are written)</p>
<p>Note: This command is sent in 2 steps, which the Firmware will
handle</p>
<ol type="1">
<li><p>&lt;CMD&gt;&lt;Address to
Write&gt;&lt;CRCH&gt;&lt;CRCL&gt;</p></li>
<li><p>&lt;16 Bytes of Data to
Write&gt;&lt;CRCH&gt;&lt;CRCL&gt;</p></li>
</ol></td>
</tr>
<tr>
<td>AUTHENTICATE</td>
<td>2</td>
<td><p>The AUTHENTICATE command is used to authenticate the MF0ICU2
using 2 keys 3DES encryption in Cipher-Block Chaining (CBC) mode as
described in ISO/IEC 10116.</p>
<ul>
<li><p>The 16-byte of the 2keys 3DES are programmed to card memory pages
from 2Ch to 2Fh. The key itself can be written during personalization or
at any later stage using the WRITE or COMPATIBILITY WRITE with Byte 0 is
always sent first.</p></li>
</ul>
<blockquote>
<p>On example of Key1 = 0001020304050607h and Key2 = 08090A0B0C0D0E0Fh,
the command sequence needed for key programming with WRITE command
is:</p>
<p>• A2 2C 07 06 05 04</p>
<p>• A2 2D 03 02 01 00</p>
<p>• A2 2E 0F 0E 0D 0C</p>
<p>• A2 2F 0B 0A 09 08</p>
</blockquote>
<ul>
<li><p>The 16-byte of the same 2keys 3DES are programed to the Device
using <strong>Property 1.2.1.1.4.1 MIFARE Ultralight C
2keys3DES</strong></p></li>
</ul>
<p>Byte 0 = 0x1A</p>
<p>Byte 1 = 0x00</p></td>
</tr>
</tbody>
</table>

Table 86 – MIFARE Ultralight AES Commands

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr>
<th>Command</th>
<th>Length</th>
<th>Field Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Get Version</td>
<td>1</td>
<td><p>The GET_VERSION command is used to retrieve information on the
MIFARE family, product version, storage size and other product data
required to identify the MIFARE Ultralight AES.</p>
<p>Byte 0 = 0x60</p></td>
</tr>
<tr>
<td>Read</td>
<td>2-3</td>
<td><p>The READ command requires a start page address, and returns the
16 bytes of four pages. For example, if address (Addr) is 03h then pages
03h, 04h, 05h, 06h are returned. So called roll-over mechanism
(described later) applies if the READ command address is near the end of
the accessible memory area. Same mechanism applies if at least part of
the addressed pages is within an authentication protected area</p>
<p>In the default state of MIFARE Ultralight AES, all memory pages in
the range from 00h to 3Bh are allowed as Addr parameter to the READ
command. Addressing a memory page above the limit results in a NAK
response. A roll-over mechanism is implemented to continue reading from
page 00h once the end of the accessible memory is reached if at least
first addressed page is within allowed limit.</p>
<p><strong>Remark</strong>: AES key values can never be directly read
out of the memory. When reading from the pages holding key values, all
00h bytes are returned.</p>
<p>The READ command with an option of end page address returns the all
n*4 bytes of the addressed pages. For example if the start address is
03h and the end address is 07h then pages 03h, 04h, 05h, 06h and 07h are
returned.</p>
<p>Byte 0 = 0x30</p>
<p>Byte 1 = Start Page Address</p>
<p>Byte 2 = (optional) End Page Address</p></td>
</tr>
<tr>
<td>Fast Read</td>
<td>3</td>
<td><p>The FAST_READ command requires a start page address and an end
page address and returns bytes of addressed pages. For example if the
start address is 03h and the end address is 07h then pages 03h, 04h,
05h, 06h, and 07h are returned. If either start or end address is
outside accessible area, then MIFARE Ultralight AES replies with a
NAK.</p>
<p>Byte 0 = 0x3A</p>
<p>Byte 2 = Start Page Address</p>
<p>Byte 3 = End Page Address</p></td>
</tr>
<tr>
<td>Write</td>
<td>6</td>
<td><p>The WRITE command requires a block address, and writes 4 bytes of
data into the addressed MIFARE Ultralight AES page.</p>
<p>Byte 0 = 0xA2</p>
<p>Byte 1 = Address to Write</p>
<p>Byte 2 to 5 = 4 Bytes of Data to Write</p></td>
</tr>
<tr>
<td>READ_CNT</td>
<td>2</td>
<td><p>The READ_CNT command is used to read out the current value of one
of the 3 one-way counters of MIFARE Ultralight AES. The command has a
single argument specifying the counter number and returns the 24-bit
counter value of the corresponding counter. Counters are always
readable, except in case of the counter "0x02" with the optional AES
authentication protection enabled. In that case, the counter 0x02 is
readable only in the AUTHENTICATE state.</p>
<p>Byte 0 = 0x39</p>
<p>Byte 1 = 0x00..0x02 (counter number from 0x00 to 0x02)</p></td>
</tr>
<tr>
<td>INCR_CNT</td>
<td>6</td>
<td><p>The INCR_CNT command is used to increment one of the 3x one-way
counters of the MIFARE Ultralight AES. Two arguments are the counter
number and the increment value. Counters are always incrementable,
except in case of the counter "0x02" with the optional AES
authentication protection enabled. In that case, the counter 0x02 can be
incremented only in the AUTHENTICATE state.</p>
<p>Byte 0 = 0xA5</p>
<p>Byte 1 = 0x00..0x02 (counter number from 0x00 to 0x02)</p>
<p>Byte 2 to 5 = 4 bytes increment value (only the 3 least significant
bytes are relevant)</p></td>
</tr>
<tr>
<td>READ_SIG</td>
<td>2</td>
<td><p>The READ_SIG command returns an IC-specific, 48-byte ECC
signature. The originality signature can be changed if it has been
unlocked with the LOCK_SIG command.</p>
<p>Byte 0 = 0x3C</p>
<p>Byte 1 = 0x00, RFU</p></td>
</tr>
<tr>
<td>WRITE_SIG</td>
<td>6</td>
<td><p>The WRITE_SIG command allows the writing of a customized
originality signature into the dedicated originality signature memory.
The WRITE_SIG command requires an originality signature block address,
and writes 4 bytes of data into the addressed originality signature
block.</p>
<p>In the initial state of MIFARE Ultralight AES, the following
originality signature blocks 00h to 0Bh are valid Addr parameters to the
WRITE_SIG command. Addressing a memory block beyond the limits above
results in a NAK response from MIFARE Ultralight AES.</p>
<p>If the originality signature is locked or permanently locked, a
WRITE_SIG command results in a NAK response from the MIFARE Ultralight
AES.</p>
<p>Byte 0 = 0xA9</p>
<p>Byte 1 = signature block address</p>
<p>Byte 2 to 5 = signature bytes to be written</p></td>
</tr>
<tr>
<td>LOCK_SIG</td>
<td>2</td>
<td><p>The LOCK_SIG command allows the user to unlock, lock or
permanently lock the dedicated originality signature memory.</p>
<p>The originality signature can only be unlocked, if the originality
signature is not permanently locked.</p>
<p>There is no command to unlock the originality signature, if the
originality signature is permanently locked.</p>
<p>Byte 0 = 0xAC</p>
<p>Byte 1 = lock option</p>
<ul>
<li><p>0x00 = unlock</p></li>
<li><p>0x01 = lock</p></li>
<li><p>0x02 = permanently lock</p></li>
</ul></td>
</tr>
<tr>
<td>VCSL</td>
<td>21</td>
<td><p>The VCSL command is used to enable a unique identification and
selection process across different physical MIFARE product-based cards
and virtual MIFARE implementations. The command requires a 16-byte
installation identifier IID and a 4-byte PCD capability value as
parameters. The parameters are present to support compatibility to other
MIFARE product-based devices, but are not used or checked inside the
MIFARE Ultralight AES. Nevertheless, the number of bytes is checked for
correctness. The answer to the VCSL command is the VCTID value stored in
the user configuration segment. This identifier indicates the type of
card or ticket. Using this information, the contactless reader can
decide whether the ticket belongs to the installation or not.</p>
<p>Byte 0 = 0x4B</p>
<p>Byte 1 to 16 = 16-byte IID (installation identifier, can be any
number)</p>
<p>Byte 17 to 20 = 4-byte PCDCAPS (PCD capabilities, can be any
number)</p></td>
</tr>
<tr>
<td>AUTHENTICATE</td>
<td>2</td>
<td><p>The AUTHENTICATE command is used to authenticate with a 3-pass
mutual authentication the MIFARE Ultralight AES and PCD. The
cryptographic method is based on AES in Cipher-Block chaining (CBC) mode
according to NIST Special Publication 800-38A. The used key is a 128-bit
AES Key. Remark: To reduce the risk on card-only side channel attack to
the AES keys, a failed authentication limit (AUTH_LIM) can be set.</p>
<ul>
<li><p>The 16 bytes of the AES [DataProtKey] are programmed to memory
pages from 30h to 33h. Keys themselves can be written during
personalization or at any later stage in a secure environment, as long
as the key is not locked for update in the user configuration segment.
AES [UIDRetrKey] is stored in memory addresses from 34h until 37h. In
case keys are not locked, MIFARE Ultralight AES allows to change
AES-keys without authentication as long as AUTH0 is not set to a page
address before or at page address where keys bytes are stored. Otherwise
MIFARE Ultralight AES requires to be in the AUTHENTICATED state to allow
to write AES keys.</p></li>
</ul>
<blockquote>
<p>The key itself can be written using the WRITE with Byte 0 is always
sent first.</p>
<p>On example of AES [DataProtKey] = 000102030405060708090A0B0C0D0E0Fh,
the command sequence needed for key programming with WRITE command
is:</p>
<p>• A2 30 0F 0E 0D 0C</p>
<p>• A2 31 0B 0A 09 08</p>
<p>• A2 32 07 06 05 04</p>
<p>• A2 33 03 02 01 00</p>
<p>On example of AES [UIDRetrKey] = 000102030405060708090A0B0C0D0E0Fh,
the command sequence needed for key programming with WRITE command
is:</p>
<p>• A2 34 0F 0E 0D 0C</p>
<p>• A2 35 0B 0A 09 08</p>
<p>• A2 36 07 06 05 04</p>
<p>• A2 37 03 02 01 00</p>
</blockquote>
<ul>
<li><p>The 16-byte of the same AES [DataProtKey] are programed to the
Device using <strong>Property 1.2.1.1.4.2 MIFARE Ultralight AES
DataProtKey</strong>.</p></li>
<li><p>The 16-byte of the same AES [UIDRetrKey] are programed to the
Device using <strong>Property 1.2.1.1.4.3 MIFARE Ultralight AES
UIDRetrKey</strong>.</p></li>
<li><p>The 16-byte of the AES [OriginalityKey] are programed to the
Device using <strong>Property 1.2.1.1.4.4 MIFARE Ultralight AES
OriginalityKey.</strong> This key value is only known by NXP.</p></li>
</ul>
<p>Byte 0 = 0x1A</p>
<p>Byte 1 = Key option</p>
<p>0x00 = DataProtKey</p>
<p>0x01 = UIDRetrKey</p>
<p>0x02 = OriginalityKey</p></td>
</tr>
</tbody>
</table>

Table 87 - Response Data for Command 0x1100 – Pass Through Command For
NTag/MIFARE Ultralight, Type 2

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
<td colspan="6">Beginning of any wrappers, at minimum including Response
Message found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
<tr>
<td colspan="6">1100 = Command 0x1100 – Pass Through Command For
NTag/MIFARE Ultralight, Type 2 Command For NFC Tag</td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Tag Response Code</p>
<p>0x00 = Success</p>
<p>0x01 = Failed</p></td>
<td>B</td>
<td>R</td>
<td>N/A</td>
</tr>
<tr>
<td>82</td>
<td>var</td>
<td><p>Encryption Control</p>
<p>If encrypted, see Table 90 - Payload for Encrypted NFC/MIFARE
Data</p>
<p>If unencrypted see Table 91 – Unencrypted NFC/MIFARE Data</p></td>
<td>B</td>
<td>O</td>
<td>N/A</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including Response
Message found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
</tbody>
</table>

If the request started successfully, the Request Status in the message
wrapper is **OK, Started / Running, All good / requested operation was
successful**.

Table 88 - Request Example (Get Version)

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA 00 81 04 01 39 11 00 84 0B 11 00 81 01 60 82 01 00 83 01 00 |

Table 89 - Response Example (Get Version)

| Example (Hex) |
|----|
| AA 00 81 04 82 39 11 00 82 04 01 00 00 00 84 14 11 00 81 01 00 82 0D FC 0B DF 7A 08 01 02 03 04 05 06 07 08 |

##### Encrypted Data Format

Table 90 - Payload for Encrypted NFC/MIFARE Data

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
<td>/DFDF59</td>
<td>var</td>
<td><p>Encrypted Data Primitive</p>
<p>Decrypt the value of this TLV data object using the algorithm and
variant specified in the <strong>Encrypted Data KSN</strong> parameter
and the <strong>Encrypted Data Encryption Type</strong> parameter to
read its contents. The format of the decrypted data is shown in
<strong>Table 91 – Unencrypted NFC/MIFARE</strong> Data.</p></td>
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
<p>See section 4.4 Encryption Type for a list of valid values.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of Notification Message found on page <a
href="#notification-message"><strong>30</strong></a></td>
</tr>
</tbody>
</table>

Table 91 – Unencrypted NFC/MIFARE Data

| Tag   | Len | Value / Description | Typ | Req | Default |
|-------|-----|---------------------|-----|-----|---------|
| FC    | var | NFC Data Container  | T   | R   |         |
| /DF7A | var | NFC Data            | B   | O   |         |

#### Command 0x1101 – Pass Through Command for MIFARE Classic/MINI®/Plus SL1 (Security Level 1), Type 2

After a MIFARE Tag is activated, the host uses this command to send
commands and receive responses to and from a MIFARE tag.

For MIFARE Plus EV1/EV2/SE/X at SL1 (Security Level 1), the tag is
discovered as MIFARE Classic, and can use the same functionality as
MIFARE Classic 1K/4K commands in **Table 93 – MIFARE Classic/MINI**®
Commands**.** Furthermore, an additional optional AES authentication is
available in this level without affecting the MIFARE Classic 1K/4K
functionality. The authenticity of the card can be proven using strong
cryptographic means with this additional functionality. In addition to
the backwards compatibility mode, MIFARE Plus card can be switched to
higher security levels. After MIFARE Plus is authenticated with AES
Security Level 1 Key, the Device doesn’t auto detect an error from the
MIFARE Tag has been removed to end the pass-through session. To end the
pass-through session, the Host application can send the last command,
CANCEL command (0xFF), or receive error response from the MIFARE Tag.

Table 92 - Request Data for Command 0x1101 - Pass Through Command for
MIFARE Classic/MINI®/Plus SL1 (Security Level 1)

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
<td colspan="6">Beginning of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message">23</a></td>
</tr>
<tr>
<td colspan="6">1101 = <strong>Command 0x1101 – Pass Through Command for
MIFARE Classic/MINI®/Plus SL1 (Security Level 1), Type 2</strong></td>
</tr>
<tr>
<td>81</td>
<td>var</td>
<td><p>Command to Send.</p>
<p>See <strong>Table 93 – MIFARE Classic/MINI</strong>® Commands</p>
<p>See <strong>Table 94 – MIFARE Plus EV1/EV2/SE/X SL1 (Security Level
1)</strong> Commands</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>01</td>
<td><p>00 – No Encrypt</p>
<p>01 - Encrypt</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>01</td>
<td><p>00 – Expect More Commands</p>
<p>01 – FF (Last Command)</p>
<p>If last command, Device will provide a single beep after receiving a
successful response from tag, otherwise, device will provide a double
beep</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including Request
Message found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 93 – MIFARE Classic/MINI® Commands

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 13%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr>
<th>Command</th>
<th>Length</th>
<th>Field Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>MIFARE Read</td>
<td></td>
<td><p>Byte 0 – 0x30 – Read Command</p>
<p>Byte 1- Sector Number to Read</p>
<p>Byte 2 – Start Block Number</p>
<p>Byte 3 – End Block Number</p>
<p>Byte 4 – Key Type, 0 = A, 1 = B</p>
<p>Byte 5 to 10 = 6 Byte Key</p></td>
</tr>
<tr>
<td>MIFARE Write</td>
<td></td>
<td><p>Byte 0 – 0xA0 – Write Command</p>
<p>Byte 1- Sector Number to Write</p>
<p>Byte 2 – Start Block Number</p>
<p>Byte 3 – End Block Number</p>
<p>Byte 4 – Key Type 0 = A, 1 = B</p>
<p>Byte 5 to 10 = 6 Byte Key</p>
<p>Byte 11 to x = Variable length Byte Data (16 bytes per
block)</p></td>
</tr>
<tr>
<td>MIFARE Increment</td>
<td></td>
<td><p>Byte 0 – 0xC1 – Increment Command</p>
<p>Byte 1 – Source Sector Number</p>
<p>Byte 2- Source Block number</p>
<p>Byte 3 – Key Type 0 = A, 1 = B</p>
<p>Byte 4 to 9 = 6 Byte Key</p>
<p>Byte 10 to 13 = 4 Byte Operand</p></td>
</tr>
<tr>
<td>MIFARE Decrement</td>
<td></td>
<td><p>Byte 0 – 0xC0 – Decrement Command</p>
<p>Byte 1 – Source Sector Number</p>
<p>Byte 2- Source Block number</p>
<p>Byte 3 – Key Type 0 = A, 1 = B</p>
<p>Byte 4 to 9 = 6 Byte Key</p>
<p>Byte 10 to 13 = 4 Byte Operand</p></td>
</tr>
<tr>
<td>MIFARE Restore</td>
<td></td>
<td><p>Byte 0 – 0xC2 – Restore Command</p>
<p>Byte 1 – Source Sector Number</p>
<p>Byte 2 - Source Block number</p>
<p>Byte 3 – Key Type 0 = A, 1 = B</p>
<p>Byte 4 to 9 = 6 Byte Key</p></td>
</tr>
<tr>
<td>MIFARE Transfer</td>
<td></td>
<td><p>Byte 0 – 0xB0 – Write the value from the Transfer Buffer into
destination block number</p>
<p>Byte 1 – Destination Sector Number</p>
<p>Byte 2 - Destination Block number</p>
<p>Byte 3 – Key Type 0 = A, 1 = B</p>
<p>Byte 4 to 9 = 6 Byte Key</p></td>
</tr>
</tbody>
</table>

Table 94 – MIFARE Plus EV1/EV2/SE/X SL1 (Security Level 1) Commands

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 7%" />
<col style="width: 54%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr>
<th>Command</th>
<th>Length</th>
<th>Field Value</th>
<th>EV1</th>
<th>EV2</th>
<th>SE</th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr>
<td>First Authenticate (part1 and part2)</td>
<td>3</td>
<td><p>First Authenticate. Use this command to switch to higher security
levels. This command is behaved as the last command. Device will provide
a single beep after receiving a successful response from a card,
otherwise, device will provide a double beep.</p>
<p>Byte 0 = 0x70</p>
<p>Byte 1-2 = Level 2 Switch Key (MIFARE Plus X only), or Level 3 Switch
Key. See NXP doc ds206234, table 113.</p>
<p>Byte 3 = MIFARE Plus AES_Key#</p>
<ul>
<li><p>0x01 = AES_Key1 = 16 bytes value stored in <strong>Property
1.2.1.1.4.5 MIFARE Plus AES_Key1.</strong></p></li>
<li><p>0x02 = AES_Key2 = 16 bytes value stored in <strong>Property
1.2.1.1.4.6 MIFARE Plus AES_Key2.</strong></p></li>
<li><p>0x03 = AES_Key3 = 16 bytes value stored in <strong>Property
1.2.1.1.4.7 MIFARE Plus AES_Key3.</strong></p></li>
<li><p>0x04 = AES_Key4 = 16 bytes values stored in <strong>Property
1.2.1.1.4.8 MIFARE Plus AES_Key4.</strong></p></li>
<li><p>0x05 = AES_Key5 = 16 bytes values stored in <strong>Property
1.2.1.1.4.9 MIFARE Plus AES_Key5.</strong></p></li>
<li><p>0x06 = AES_Key6 = 16 bytes values stored in <strong>Property
1.2.1.1.4.A MIFARE Plus AES_Key6.</strong></p></li>
</ul></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td><p>Following Authenticate</p>
<p>(part1 and part2)</p></td>
<td>3</td>
<td><p>Following Authenticate. Use this command for an option to put the
NFC tag in Security Level 1 AES Authenticated before sending MIFARE
Classic commands.</p>
<p>Byte 0 = 0x76</p>
<p>Byte 1-2 = Security Level 1 Card Authentication Key. See NXP doc
ds206234, table 113.</p>
<p>Byte 3 = MIFARE Plus AES_Key#</p>
<ul>
<li><p>0x01 = AES_Key1 = 16 bytes value stored in <strong>Property
1.2.1.1.4.5 MIFARE Plus AES_Key1.</strong></p></li>
<li><p>0x02 = AES_Key2 = 16 bytes value stored in <strong>Property
1.2.1.1.4.6 MIFARE Plus AES_Key2.</strong></p></li>
<li><p>0x03 = AES_Key3 = 16 bytes value stored in <strong>Property
1.2.1.1.4.7 MIFARE Plus AES_Key3.</strong></p></li>
<li><p>0x04 = AES_Key4 = 16 bytes values stored in <strong>Property
1.2.1.1.4.8 MIFARE Plus AES_Key4.</strong></p></li>
<li><p>0x05 = AES_Key5 = 16 bytes values stored in <strong>Property
1.2.1.1.4.9 MIFARE Plus AES_Key5.</strong></p></li>
<li><p>0x06 = AES_Key6 = 16 bytes values stored in <strong>Property
1.2.1.1.4.A MIFARE Plus AES_Key6.</strong></p></li>
</ul></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>READ_SIG</td>
<td>2</td>
<td><p>The READ_SIG command returns an IC-specific, 48-byte ECC
originality check signature.</p>
<p>Byte 0 = 0x3C</p>
<p>Byte 1 = 0x00, RFU</p></td>
<td>Y</td>
<td>Y</td>
<td>N</td>
<td>N</td>
</tr>
<tr>
<td>Personalize UID</td>
<td>2</td>
<td><p>Set anti-collision, selection and authentication behavior.</p>
<p>The execution of this command requires an authentication to MF
Classic sector 0. Once this command has been issued and accepted by the
PICC, the configuration is automatically locked. A subsequently issued
‘Personalize UID Usage’ command is not executed and fails.</p>
<p>Byte 0 = 0x40</p>
<p>Byte 1 = Encoded type of UID usage:</p>
<p>0x00 = UIDF0 = anti-collision and selection with the double size UID
(7-byte) according to ISO/IEC14443-3</p>
<p>0x40 = UIDF1 = anti-collision and selection with the double size UID
(7-byte) according to ISO/IEC 14443-3 and optional usage of a selection
process shortcut</p>
<p>0x20 = UIDF2 = anti-collision and selection with a single size random
ID (4-byte) according to ISO/IEC14443-3. After the card is configured
with random ID, it won’t be able perform any MF Classic authentication
since MF Classic authentication requires UID.</p>
<p>0x60 = UIDF3 = anti-collision and selection with a single size NUID
(4-byte) according to ISO/IEC14443-3 where the NUID is calculated out of
the 7-byte UID</p></td>
<td>Y</td>
<td>Y</td>
<td>N</td>
<td>N</td>
</tr>
<tr>
<td>CANCEL</td>
<td>1</td>
<td><p>This command is used to terminate the pass-through command
session.</p>
<p>Byte 0 = 0xFF</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
</tbody>
</table>

Table 95 - Response Data for Command 0x1101 – Pass Through Command for
MIFARE Classic/MINI®/Plus SL1 (Security Level 1), Type 2

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
<td colspan="6">Beginning of any wrappers, at minimum including Response
Message found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
<tr>
<td colspan="6">1101 = <strong>Command 0x1101 – Pass Through Command for
MIFARE Classic/MINI®/Plus SL1 (Security Level 1), Type 2</strong></td>
</tr>
<tr>
<td>81</td>
<td>var</td>
<td><p>Tag Response Code</p>
<p>Byte 0 = 0x00 = Success</p>
<p>Byte 0 = 0x01 = I/O Failed</p>
<p>Byte 0 = 0x02 Authentication Failed</p>
<p>Byte 1 = 0x01 = Block that Failed (optional)</p></td>
<td>B</td>
<td>R</td>
<td>N/A</td>
</tr>
<tr>
<td>82</td>
<td>var</td>
<td><p>Encryption Control</p>
<p>If encrypted, see <strong>Table 90 - Payload for Encrypted
NFC/MIFARE</strong> Data</p>
<p>If unencrypted see <strong>Table 91 – Unencrypted NFC/MIFARE</strong>
Data</p></td>
<td>B</td>
<td>O</td>
<td>N/A</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including Response
Message found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
</tbody>
</table>

If the request started successfully, the Request Status in the message
wrapper is **OK, Started / Running, All good / requested operation was
successful**.

Table 96 - Request Example (Read Sector 0, Block Number Start 0 - End 0,
KeyType A, Key = FFFFFFFFFFFF)

| Example (Hex) |
|----|
| AA 00 81 04 01 19 11 01 84 15 11 01 81 0B 30 00 00 00 00 FF FF FF FF FF FF 82 01 00 83 01 00 |

Table 97 - Response Example (Read Sector 0, Block Number Start 0 - End
0, KeyType A, Key = FFFFFFFFFFFF)

| Example (Hex) |
|----|
| AA 00 81 04 82 19 11 01 82 04 01 00 00 00 84 1C 11 01 81 01 00 82 15 FC 13 DF 7A 10 A4 FB 0D 3E 6C 08 04 00 03 0D C0 90 EE BF BB 1D |

##### Encrypted Data Format

Table 98 - Payload for Encrypted NFC/MIFARE Data

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
<p>See section 4.4 Encryption Type for a list of valid values.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including Response
Message found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
</tbody>
</table>

Table 99 – Unencrypted NFC/MIFARE Data

| Tag   | Len | Value / Description       | Typ | Req | Default |
|-------|-----|---------------------------|-----|-----|---------|
| FC    | var | NFC/MIFARE Data Container | T   | R   |         |
| /DF7A | var | NFC/MIFARE Data           | B   | O   |         |

#### Command 0x1102 – Pass Through Command for MIFARE DESFire, Type 4

After a MIFARE DESFire Light/EV1/EV2/EV3 Tag is activated, the host uses
this command to send commands and receive responses to and from a MIFARE
DESFire Tag.

There will be a fixed 30 second timeout for commands that require
multiple command/responses.

Table 100 - Request Data for Command 0x1102 – Pass Through Command for
MIFARE DESFire, Type 4

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
<td colspan="6">Beginning of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message">23</a></td>
</tr>
<tr>
<td colspan="6">1102 <strong>=</strong> <strong>Command 0x1102 – Pass
Through Command for MIFARE DESFire, Type 4</strong></td>
</tr>
<tr>
<td>81</td>
<td>var</td>
<td><p>Command to Send.</p>
<p>See DESFire Data Sheet (MF2DLHX0)</p>
<p>Should follow ISO 7816-4 APDU format</p>
<ul>
<li><p>C-APDU</p></li>
</ul>
<ul>
<li><p>CLA INS P1 P2 Lc Data Le</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>01</td>
<td><p>00 – No Encrypt</p>
<p>01 - Encrypt</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>01</td>
<td><p>00 – Expect More Commands</p>
<p>01 – FF (Last Command)</p>
<p>If last command, Device will provide a single beep after receiving a
successful response from tag, otherwise, device will provide a double
beep</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including Request
Message found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 101 - Response Data for Command 0x1102 – Pass Through Command for
MIFARE DESFire, Type 4

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
<td colspan="6">Beginning of any wrappers, at minimum including Response
Message found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
<tr>
<td colspan="6">1102 = <strong>Command 0x1102 – Pass Through Command for
MIFARE DESFire, Type 4</strong></td>
</tr>
<tr>
<td>81</td>
<td>02</td>
<td><p>Tag Response (SW1 SW2)</p>
<p>See DESFire Data Sheet (MF2DLHX0)</p>
<p>Should follow ISO 7816-4 APDU format</p>
<ul>
<li><p>SW1 and SW2 of R-APDU</p></li>
</ul>
<p>If card is not able to respond:</p>
<ul>
<li><p>SW1 = 0x64, SW2 = 0x00</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>N/A</td>
</tr>
<tr>
<td>82</td>
<td>var</td>
<td><p>Tag Data</p>
<ul>
<li><p>Data of R-APDU</p></li>
</ul>
<p>Encryption Control</p>
<p>If encrypted, see <strong>Table 90 - Payload for Encrypted
NFC/MIFARE</strong> Data</p>
<p>If unencrypted see <strong>Table 91 – Unencrypted NFC/MIFARE</strong>
Data</p></td>
<td>B</td>
<td>O</td>
<td>N/A</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including Response
Message found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
</tbody>
</table>

If the request started successfully, the Request Status in the message
wrapper is **OK, Started / Running, All good / requested operation was
successful**.

Table 102 - Request Example (Get Version Part 1)

| Example (Hex) |
|----|
| AA 00 81 04 01 13 11 02 84 0F 11 02 81 05 90 60 00 00 00 82 01 00 83 01 00 |

Table 103 - Response Example (Get Version Part 1)

| Example (Hex) |
|----|
| AA 00 81 04 82 13 11 02 82 04 01 00 00 00 84 14 11 02 81 02 91 AF 82 0C FC 0A DF 7A 07 04 08 01 30 00 13 05 |

##### Encrypted Data Format

Table 104 - Payload for Encrypted NFC/MIFARE Data

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
<td colspan="6">End of Notification Message found on page <a
href="#notification-message"><strong>30</strong></a></td>
</tr>
</tbody>
</table>

Table 105 – Unencrypted NFC/MIFARE Data

| Tag   | Len | Value / Description       | Typ | Req | Default |
|-------|-----|---------------------------|-----|-----|---------|
| FC    | var | NFC/MIFARE Data Container | T   | R   |         |
| /DF7A | var | NFC/MIFARE Data           | B   | O   |         |

#### Command 0x1103 – Pass Through Command for MIFARE Plus, Type 2

After a MIFARE Plus EV1/EV2/SE/X Tag is activated, the Host uses this
command to send commands and receive responses to and from a MIFARE Plus
tag.

For MIFARE Plus SE/X, the Device will not auto detect an error from the
MIFARE Tag that has been removed to end the pass-through session. To end
the pass-through session, the Host application can send the last
command, CANCEL command (0xFF), or receive error response from the
MIFARE Tag.

After the card is configured to successfully switch to Security Level 1,
the card will be discovered as MIFARE Classic 1K/4K and can use the same
functionality as MIFARE Classic 1K/4K commands.

For more details, please refer to NXP NDA documentation ds206234-Product
data sheet MIFARE Plus Functionality of implementations on smart card
controllers (3.4)

Table 106 - Command 0x1103 – Pass Through Command for MIFARE Plus, Type
2

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
<td colspan="6">Beginning of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message">23</a></td>
</tr>
<tr>
<td colspan="6"><strong>1103 = Command 0x1103 – Pass Through Command for
MIFARE Plus, Type 2</strong></td>
</tr>
<tr>
<td>81</td>
<td>var</td>
<td><p>Command to Send.</p>
<p>See <strong>Table 107 - MIFARE Plus EV1/EV2/SE/X SL0 (Security Level
0) Commands</strong></p>
<p>See <strong>Table 108 – MIFARE Plus EV1/EV2/SE/X SL3 (Security Level
3) Commands</strong></p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>01</td>
<td><p>00 – No Encrypt</p>
<p>01 - Encrypt</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>01</td>
<td><p>00 – Expect More Commands</p>
<p>01 – FF (Last Command)</p>
<p>If this is the last command, the Device will provide a single beep
after receiving a successful response from the tag, otherwise, the
device will provide a double beep</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including Request
Message found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 107 - MIFARE Plus EV1/EV2/SE/X SL0 (Security Level 0) Commands

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 8%" />
<col style="width: 54%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr>
<th>Command</th>
<th>Length</th>
<th>Field Value</th>
<th>EV1</th>
<th>EV2</th>
<th>SE</th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr>
<td>GET_VERSION</td>
<td>1</td>
<td><p>The GET_VERSION command is used to retrieve manufacturing related
data of the MIFARE Plus EV1/EV2 cards</p>
<p>Byte 0 = 0x60</p></td>
<td>Y</td>
<td>Y</td>
<td>N</td>
<td>N</td>
</tr>
<tr>
<td>READ_SIG</td>
<td>2</td>
<td><p>The READ_SIG command returns an IC-specific, 48-byte ECC
originality check signature of MIFARE Plus EV1/EV2 cards.</p>
<p>Byte 0 = 0x3C</p>
<p>Byte 1 = 0x00, RFU</p></td>
<td>Y</td>
<td>Y</td>
<td>N</td>
<td>N</td>
</tr>
<tr>
<td>WRITE_PERSO</td>
<td>19</td>
<td><p>The WRITE_PERSO command is used to pre-personalize AES keys and
data from the initial delivery configuration to a customer specific
value.</p>
<p>Byte 0 = 0xA8</p>
<p>Byte 1-2 = Number of Block or Key to be written to (MSB first). See
NXP doc ds206234, table 113.</p>
<p>Byte 3 to 18 = 16 bytes value of the key or data which shall be
written (in plain)</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>COMMIT_PERSO</td>
<td>2</td>
<td><p>The COMMIT_PERSO command is used to finalize the personalization
and switch up to security level 1 or security level 3.</p>
<p>For MIFARE Plus EV1/EV2, the following mandatory AES keys must be
written using the WRITE_PERSO command before it can be switched to
security level 1 or security level 3.</p>
<ul>
<li><p>Card Configuration Key</p></li>
<li><p>Card Master Key</p></li>
<li><p>Level 2 Switch Key</p></li>
<li><p>Level 3 Switch Key</p></li>
</ul>
<p>For MIFARE Plus SE, the following mandatory AES keys must be written
using the WRITE_PERSO command before it can be switched to security
level 1 (for L1 card) or security level 3 (for L3 card).</p>
<ul>
<li><p>Card Configuration Key</p></li>
<li><p>Card Master Key</p></li>
<li><p>Level 3 Switch Key</p></li>
</ul>
<p>For MIFARE Plus X, the following mandatory AES keys must be written
using the WRITE_PERSO command before it can be switched to security
level 1 (for L1 card) or security level 3 (for L3 card).</p>
<ul>
<li><p>Card Configuration Key</p></li>
<li><p>Card Master Key</p></li>
<li><p>Level 2 Switch Key (for L1 card)</p></li>
<li><p>Level 3 Switch Key (for L1 card)</p></li>
</ul>
<p>Byte 0 = 0xAA</p>
<p>Byte 1 = Security Level Option for EV1 and EV2 cards</p>
<ul>
<li><p>0x01 = Security Level 1</p></li>
<li><p>0x03 = Security Level 3</p></li>
<li><p>Other values = Invalid. Device will return error.</p></li>
</ul>
<p>Byte 1 = 0x00 for SE and X cards. The Device will return error for
other values.</p>
<p>It is also highly recommended to change all sector AES keys as well
as the data within this security level in a secure environment.</p>
<p>This command is behaved as the last command. The Device will provide
a single beep after receiving a successful response from a card,
otherwise, device will provide a double beep.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>CANCEL</td>
<td>1</td>
<td><p>This command is used to terminate the pass-through command
session.</p>
<p>Byte 0 = 0xFF</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
</tbody>
</table>

Table 108 – MIFARE Plus EV1/EV2/SE/X SL3 (Security Level 3) Commands

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 7%" />
<col style="width: 54%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr>
<th>Command</th>
<th>Length</th>
<th>Field Value</th>
<th>EV1</th>
<th>EV2</th>
<th>SE</th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>MIFARE Plus Authenticate commands</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>First Authenticate (part1 and part2)</td>
<td>3</td>
<td><p>First Authenticate</p>
<p>Byte 0 = 0x70</p>
<p>Byte 1-2 = Key Number of the key to be authenticated (MSB first). See
NXP doc ds206234, table 113.</p>
<p>Byte 3 = MIFARE Plus AES_Key#</p>
<ul>
<li><p>0x01 = AES_Key1 = 16 bytes value stored in <strong>Property
1.2.1.1.4.5 MIFARE Plus AES_Key1.</strong></p></li>
<li><p>0x02 = AES_Key2 = 16 bytes value stored in <strong>Property
1.2.1.1.4.6 MIFARE Plus AES_Key2.</strong></p></li>
<li><p>0x03 = AES_Key3 = 16 bytes value stored in <strong>Property
1.2.1.1.4.7 MIFARE Plus AES_Key3.</strong></p></li>
<li><p>0x04 = AES_Key4 = 16 bytes values stored in <strong>Property
1.2.1.1.4.8 MIFARE Plus AES_Key4.</strong></p></li>
<li><p>0x05 = AES_Key5 = 16 bytes values stored in <strong>Property
1.2.1.1.4.9 MIFARE Plus AES_Key5.</strong></p></li>
<li><p>0x06 = AES_Key6 = 16 bytes values stored in <strong>Property
1.2.1.1.4.A MIFARE Plus AES_Key6.</strong></p></li>
</ul></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td><p>Following Authenticate</p>
<p>(part1 and part2)</p></td>
<td>3</td>
<td><p>Following Authenticate</p>
<p>Byte 0 = 0x76</p>
<p>Byte 1-2 = Key Number of the key to be authenticated (MSB first). See
NXP doc ds206234, table 113.</p>
<p>Byte 3 = MIFARE Plus AES_Key#</p>
<ul>
<li><p>0x01 = AES_Key1 = 16 bytes value stored in <strong>Property
1.2.1.1.4.5 MIFARE Plus AES_Key1.</strong></p></li>
<li><p>0x02 = AES_Key2 = 16 bytes value stored in <strong>Property
1.2.1.1.4.6 MIFARE Plus AES_Key2.</strong></p></li>
<li><p>0x03 = AES_Key3 = 16 bytes value stored in <strong>Property
1.2.1.1.4.7 MIFARE Plus AES_Key3.</strong></p></li>
<li><p>0x04 = AES_Key4 = 16 bytes values stored in <strong>Property
1.2.1.1.4.8 MIFARE Plus AES_Key4.</strong></p></li>
<li><p>0x05 = AES_Key5 = 16 bytes values stored in <strong>Property
1.2.1.1.4.9 MIFARE Plus AES_Key5.</strong></p></li>
<li><p>0x06 = AES_Key6 = 16 bytes values stored in <strong>Property
1.2.1.1.4.A MIFARE Plus AES_Key6.</strong></p></li>
</ul></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>ResetAuth</td>
<td>1</td>
<td><p>Reset the authentication</p>
<p>Byte 0 = 0x78</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td><strong>READ commands</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Read</td>
<td>4</td>
<td><p>Reading encrypted, no MAC on response, MAC</p>
<p>on command.</p>
<p>This command offers the possibility to read the data from</p>
<p>one or multiple blocks in an encrypted way. A MAC is only used on the
command sent to the PICC, no MAC is attached to the response.</p>
<p>Byte 0 = 0x30</p>
<p>Byte 1-2 = Block number of the 1<sup>st</sup> block to be read (MSB
first). See NXP doc ds206234, table 113.</p>
<p>Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers
do not count if Byte 3 &gt; 1. Use Byte 3 = 1 for reading Sector
Trailer.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Read MACed</td>
<td>4</td>
<td><p>Reading encrypted, MAC on response, MAC on</p>
<p>Command.</p>
<p>This command offers the possibility to read the data from</p>
<p>one or multiple blocks in an encrypted way. A MAC is used on the
command sent to the PICC and on the response</p>
<p>received.</p>
<p>Byte 0 = 0x31</p>
<p>Byte 1-2 = Block number of the 1<sup>st</sup> block to be read (MSB
first). See NXP doc ds206234, table 113.</p>
<p>Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers
do not count if Byte 3 &gt; 1. Use Byte 3 = 1 for reading Sector
Trailer.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Read Plain</td>
<td>4</td>
<td><p>Reading in plain, no MAC on response, MAC on command.</p>
<p>This command offers the possibility to read the data in plain from
one or multiple blocks. A MAC is used on the command and not on the
response.</p>
<p>Byte 0 = 0x32</p>
<p>Byte 1-2 = Block number of the 1<sup>st</sup> block to be read (MSB
first). See NXP doc ds206234, table 113.</p>
<p>Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers
do not count if Byte 3 &gt; 1. Use Byte 3 = 1 for reading Sector
Trailer.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Read Plain MACed</td>
<td>4</td>
<td><p>Reading in plain, MAC on response, MAC on command.</p>
<p>This command offers the possibility to read the data in plain from
one or multiple blocks. A MAC is used on the command and the
response.</p>
<p>Byte 0 = 0x33</p>
<p>Byte 1-2 = Block number of the 1<sup>st</sup> block to be read (MSB
first). See NXP doc ds206234, table 113.</p>
<p>Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers
do not count if Byte 3 &gt; 1. Use Byte 3 = 1 for reading Sector
Trailer.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Read UnMACed</td>
<td>4</td>
<td><p>Reading encrypted, no MAC on response, no</p>
<p>MAC on command</p>
<p>This command offers the possibility to read the data from</p>
<p>one or multiple blocks in an encrypted way.</p>
<p>By default, Read with MAC on command is required. To Read with no MAC
on command, needs to modify the card MFP Configuration Block.</p>
<p>Byte 0 = 0x34</p>
<p>Byte 1-2 = Block number of the 1<sup>st</sup> block to be read (MSB
first). See NXP doc ds206234, table 113.</p>
<p>Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers
do not count if Byte 3 &gt; 1. Use Byte 3 = 1 for reading Sector
Trailer.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Read UnMACed, Response MACed</td>
<td>4</td>
<td><p>Reading encrypted, MAC on response, no MAC on command</p>
<p>This command offers the possibility to read the data from</p>
<p>one or multiple blocks in an encrypted way. A MAC is used only on the
response received.</p>
<p>By default, Read with MAC on command is required. To Read with no MAC
on command, needs to modify the card MFP Configuration Block.</p>
<p>Byte 0 = 0x35</p>
<p>Byte 1-2 = Block number of the 1<sup>st</sup> block to be read (MSB
first). See NXP doc ds206234, table 113.</p>
<p>Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers
do not count if Byte 3 &gt; 1. Use Byte 3 = 1 for reading Sector
Trailer.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Read Plain UnMACed</td>
<td>4</td>
<td><p>Reading in plain, no MAC on response, no MAC on command.</p>
<p>This command offers the possibility to read the data in plain from
one or multiple blocks. AMAC is not used on the response and not on the
command.</p>
<p>By default, Read with MAC on command is required. To Read with no MAC
on command, needs to modify the card MFP Configuration Block.</p>
<p>Byte 0 = 0x36</p>
<p>Byte 1-2 = Block number of the 1<sup>st</sup> block to be read (MSB
first). See NXP doc ds206234, table 113.</p>
<p>Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers
do not count if Byte 3 &gt; 1. Use Byte 3 = 1 for reading Sector
Trailer.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Read Plain UnMACed, Response MACed</td>
<td>4</td>
<td><p>Reading in plain, MAC on response, no MAC on command</p>
<p>This command offers the possibility to read the data in plain from
one or multiple blocks. A MAC is used on the response and not on the
command.</p>
<p>By default, Read with MAC on command is required. To Read with no MAC
on command, needs to modify the card MFP Configuration Block.</p>
<p>Byte 0 = 0x37</p>
<p>Byte 1-2 = Block number of the 1<sup>st</sup> block to be read (MSB
first). See NXP doc ds206234, table 113.</p>
<p>Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers
do not count if Byte 3 &gt; 1. Use Byte 3 = 1 for reading Sector
Trailer.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td><strong>WRITE commands</strong></td>
<td></td>
<td></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Write</td>
<td>20/36/52</td>
<td><p>Writing encrypted, no MAC on response, MAC on Command.</p>
<p>This command offers the possibility to write the data to up to three
blocks in an encrypted way. MAC is only used on the command sent to the
PICC.</p>
<p>Byte 0 = 0xA0</p>
<p>Byte 1-2 = Block number of the 1<sup>st</sup> to be written block
(MSB first). See NXP doc ds206234, table 113.</p>
<p>Byte 3 = 0x01/0x02/0x03 = number of blocks (16 byte) of the data to
be written</p>
<p>Byte 4 – n = Data to be written, equal to number of blocks *
16.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Write MACed</td>
<td>20/36/52</td>
<td><p>Writing encrypted, MAC on response, MAC on command.</p>
<p>This command offers the possibility to write the data to up to three
blocks in an encrypted way. A MAC is used on the command sent to the
PICC and on the response received from the PICC.</p>
<p>Byte 0 = 0xA1</p>
<p>Byte 1-2 = Block number of the 1<sup>st</sup> to be written block
(MSB first). See NXP doc ds206234, table 113.</p>
<p>Byte 3 = 0x01/0x02/0x03 = number of blocks (16 byte) of the data to
be written</p>
<p>Byte 4 – n = Data to be written, equal to number of blocks *
16.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Write Plain</td>
<td>20/36/52</td>
<td><p>Writing in plain, no MAC on response, MAC on command</p>
<p>This command offers the possibility to write the data to up to three
blocks in plain. A MAC is only used on the command sent to the PICC.</p>
<p>Byte 0 = 0xA2</p>
<p>Byte 1-2 = Block number of the 1<sup>st</sup> to be written block
(MSB first). See NXP doc ds206234, table 113.</p>
<p>Byte 3 = 0x01/0x02/0x03 = number of blocks (16 byte) of the data to
be written</p>
<p>Byte 4 – n = Data to be written, equal to number of blocks *
16.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Write Plain MACed</td>
<td>20/36/52</td>
<td><p>Writing in plain, MAC on response, MAC on command.</p>
<p>This command offers the possibility to write the data to up to three
blocks in plain. A MAC is used on the command sent to the PICC as well
as on the response from the PICC</p>
<p>Byte 0 = 0xA3</p>
<p>Byte 1-2 = Block number of the 1<sup>st</sup> to be written block
(MSB first). See NXP doc ds206234, table 113.</p>
<p>Byte 3 = 0x01/0x02/0x03 = number of blocks (16 byte) of the data to
be written</p>
<p>Byte 4 – n = Data to be written, equal to number of blocks *
16.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td><strong>VALUE operations</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Increment</td>
<td>7</td>
<td><p>Increment encrypted, no MAC on response, MAC on command</p>
<p>This command offers the possibility to increment a value block where
the command is secured by a MAC calculated, but not on the response.</p>
<p>Byte 0 = 0xB0</p>
<p>Byte 1-2 = Source Block number. Block Number of the block to be
incremented (MSB first). See NXP doc ds206234, table 113.</p>
<p>Byte 3-6 = The 4 bytes value to be incremented in LSB order. For
example, if the value to be incremented by 1, then the value will be
0x01 00 00 00</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Increment MACed</td>
<td>7</td>
<td><p>Increment encrypted, MAC on response, MAC on command.</p>
<p>This command offers the possibility to increment a value block where
the command is secured by a MAC calculated, but not on the response.</p>
<p>Byte 0 = 0xB1</p>
<p>Byte 1-2 = Source Block number. Block Number of the block to be
incremented (MSB first). See NXP doc ds206234, table 113.</p>
<p>Byte 3-6 = The 4 bytes value to be incremented in LSB order. For
example, if the value to be incremented by 1, then the value will be
0x01 00 00 00</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Decrement</td>
<td>7</td>
<td><p>Decrement encrypted, no MAC on response, MAC on command.</p>
<p>This command offers the possibility to decrement a value block where
the command is secured by a MAC calculated, but not on the response.</p>
<p>Byte 0 = 0xB2</p>
<p>Byte 1-2 = Source Block number. Block Number of the block to be
decremented (MSB first). See NXP doc ds206234, table 113.</p>
<p>Byte 3-6 = The 4 bytes value to be decremented in LSB order. For
example, if the value to be decremented by 1, then the value will be
0x01 00 00 00</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Decrement MACed</td>
<td>7</td>
<td><p>Decrement encrypted, MAC on response, MAC on command</p>
<p>This command offers the possibility to decrement a value block where
the command is secured by a MAC calculated, as well as on the
response.</p>
<p>Byte 0 = 0xB3</p>
<p>Byte 1-2 = Source Block number. Block Number of the block to be
decremented (MSB first). See NXP doc ds206234, table 113.</p>
<p>Byte 3-6 = The 4 bytes value to be decremented in LSB order. For
example, if the value to be decremented by 1, then the value will be
0x01 00 00 00</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Transfer</td>
<td>3</td>
<td><p>Transfer, no MAC on response, MAC on command.</p>
<p>The Transfer command stores the content of the Transfer Buffer to the
specified address.</p>
<p>The Transfer command can be applied to any block. The Transfer
command can only be executed after an Increment, Decrement,
IncrementTransfer, DecrementTransfer or</p>
<p>Restore command has been successfully executed since the latest
authentication. The command is secured by a MAC on a command. No MAC is
calculated on the response.</p>
<p>Byte 0 = 0xB4</p>
<p>Byte 1-2 = Destination Block number, whose content is to be replaced
by the content of the Transfer Buffer (MSB first). See NXP doc ds206234,
table 113.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Transfer MACed</td>
<td>3</td>
<td><p>Transfer, MAC on response, MAC on command.</p>
<p>The Transfer command stores the content of the Transfer Buffer to the
specified address.</p>
<p>The Transfer command can be applied to any block. The Transfer
command can only be executed after an Increment, Decrement,
IncrementTransfer, DecrementTransfer or</p>
<p>Restore command has been successfully executed since the latest
authentication. The command is secured by a MAC on a command. A MAC is
calculated on the response.</p>
<p>Byte 0 = 0xB5</p>
<p>Byte 1-2 = Destination Block number, whose content is to be replaced
by the content of the Transfer Buffer (MSB first). See NXP doc ds206234,
table 113.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Increment Transfer</td>
<td>9</td>
<td><p>Increment Transfer encrypted, no MAC on response, MAC on</p>
<p>Command.</p>
<p>This command offers the possibility to make a combined increment and
transfer within one command on a value block where the command is
secured by a MAC calculated, no MAC on the response.</p>
<p>The command updates the Transfer Buffer in the same way as if a
separate Increment and Transfer commands were given</p>
<p>Byte 0 = 0xB6</p>
<p>Byte 1-2 = Source Block number. Block Number of the block to be
incremented.</p>
<p>Byte 3-4 = Destination Block number, whose content is to be replaced
by the content of the Transfer Buffer.</p>
<p>Byte 5-8 = The 4 bytes value to be incremented in LSB order.</p>
<p>For example, if the value to be incremented by 1, then the value will
be 0x01 00 00 00</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Increment Transfer MACed</td>
<td>9</td>
<td><p>Increment Transfer encrypted, MAC on response, MAC on
command.</p>
<p>This command offers the possibility to make a combined increment and
transfer within one command on a value block where the command is
secured by a MAC calculated, and as well as a MAC on the response.</p>
<p>The command updates the Transfer Buffer in the same way as if a
separate Increment and Transfer commands were given.</p>
<p>Byte 0 = 0xB7</p>
<p>Byte 1-2 = Source Block number. Block Number of the block to be
incremented (MSB first).</p>
<p>Byte 3-4 = Destination Block number, whose content is to be replaced
by the content of the Transfer Buffer (MSB first).</p>
<p>Byte 5-8 = The 4 bytes value to be incremented in LSB order.</p>
<p>For example, if the value to be incremented by 1, then the value will
be 0x01 00 00 00.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Decrement Transfer</td>
<td>9</td>
<td><p>Decrement Transfer encrypted, no MAC on response, MAC on
command</p>
<p>This command offers the possibility to make a combined decrement and
transfer within one command on a value block where the command is
secured by a MAC, but no MAC on the response. The command updates the
Transfer Buffer in the same way as if a separate Decrement and Transfer
commands were given.</p>
<p>Byte 0 = 0xB8</p>
<p>Byte 1-2 = Source Block number. Block Number of the block to be
decremented (MSB first).</p>
<p>Byte 3-4 = Destination Block number, whose content is to be replaced
by the content of the Transfer Buffer (MSB first).</p>
<p>Byte 5-8 = The 4 bytes value to be incremented in LSB order.</p>
<p>For example, if the value to be decremented by 1, then the value will
be 0x01 00 00 00.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Decrement Transfer MACed</td>
<td>9</td>
<td><p>Decrement Transfer encrypted, MAC on response, MAC on</p>
<p>Command</p>
<p>This command offers the possibility to make a combined decrement and
transfer within one command on a value block where both the command and
the response are secured by a MAC.</p>
<p>The command updates the Transfer Buffer in the same way as if a
separate Decrement and Transfer commands were given.</p>
<p>Byte 0 = 0xB9</p>
<p>Byte 1-2 = Source Block number. Block Number of the block to be
decremented (MSB first).</p>
<p>Byte 3-4 = Destination Block number, whose content is to be replaced
by the content of the Transfer Buffer (MSB first).</p>
<p>Byte 5-8 = The 4 bytes value to be incremented in LSB order.</p>
<p>For example, if the value to be decremented by 1, then the value will
be 0x01 00 00 00.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Restore</td>
<td>3</td>
<td><p>Restore encrypted, no MAC on response, MAC on command</p>
<p>The Restore command copies the Content found in the Value Block at
the given address to the Transfer Buffer. The Restore command can only
be applied to value blocks. The command is secured by a MAC on a
command, no MAC is calculated on the response.</p>
<p>Byte 0 = 0xC2</p>
<p>Byte 1-2 = Source Block number. Block Number of the block which
content is to be copied to the Transfer Buffer.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>Restore MACed</td>
<td>3</td>
<td><p>Restore encrypted, MAC on response, MAC on command.</p>
<p>The Restore command copies the Content found in the Value Block at
the given address to the Transfer Buffer. The Restore command can only
be performed to value blocks. The command is secured by a MAC on a
command and a MAC is</p>
<p>calculated on the response.</p>
<p>Byte 0 = 0xC3</p>
<p>Byte 1-2 = Source Block number. Block Number of the block which
content is to be copied to the Transfer Buffer.</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td><strong>Others</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>GET_VERSION</td>
<td>1</td>
<td><p>The GET_VERSION command is used to retrieve manufacturing related
data of the MIFARE Plus EV1/EV2 cards</p>
<p>Byte 0 = 0x60</p></td>
<td>Y</td>
<td>Y</td>
<td>N</td>
<td>N</td>
</tr>
<tr>
<td>READ_SIG</td>
<td>2</td>
<td><p>The READ_SIG command returns an IC-specific, 48-byte ECC
originality check signature of MIFARE Plus EV1/EV2 cards.</p>
<p>Byte 0 = 0x3C</p>
<p>Byte 1 = 0x00, RFU</p></td>
<td>Y</td>
<td>Y</td>
<td>N</td>
<td>N</td>
</tr>
<tr>
<td>CANCEL</td>
<td>1</td>
<td><p>This command is used to terminate the pass-through command
session.</p>
<p>Byte 0 = 0xFF</p></td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
</tbody>
</table>

Table 109 - Response Data for Command 0x1103 – Pass Through Command for
MIFARE Plus, Type 2

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
<td colspan="6">Beginning of any wrappers, at minimum including Response
Message found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
<tr>
<td colspan="6">1103 = <strong>Command 0x1103 – Pass Through Command for
MIFARE Plus, Type 2</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Tag Response Code</p>
<p>0x00 = Success</p>
<p>0x01 = Failed</p></td>
<td>B</td>
<td>R</td>
<td>N/A</td>
</tr>
<tr>
<td>82</td>
<td>Var</td>
<td><p>Encryption Control</p>
<p>If encrypted, see <strong>Table 90 - Payload for Encrypted
NFC/MIFARE</strong> Data</p>
<p>If unencrypted see <strong>Table 91 – Unencrypted NFC/MIFARE</strong>
Data</p></td>
<td>B</td>
<td>O</td>
<td>N/A</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including Response
Message found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
</tbody>
</table>

If the request started successfully, the Request Status in the message
wrapper is **OK, Started / Running, All good / requested operation was
successful**.

Table 110 - Request Example (Get Version)

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA 00 81 04 01 DA 11 03 84 0B 11 03 81 01 60 82 01 00 83 01 00 |

Table 111 - Response Example (Get Version)

| Example (Hex) |
|----|
| AA 00 81 04 82 DA 11 03 82 04 01 00 00 00 84 28 11 03 81 01 00 82 21 FC 1F DF 7A 1C 04 02 01 11 00 16 04 04 02 01 01 01 16 04 04 4D 59 5A 3E 18 90 CF 8D 15 61 51 21 23 |

##### Encrypted Data Format

Table 112 - Payload for Encrypted NFC/MIFARE Data

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
<td colspan="6">End of Notification Message found on page <a
href="#notification-message"><strong>30</strong></a></td>
</tr>
</tbody>
</table>

Table 113 – Unencrypted NFC/MIFARE Data

| Tag   | Len | Value / Description       | Typ | Req | Default |
|-------|-----|---------------------------|-----|-----|---------|
| FC    | var | NFC/MIFARE Data Container | T   | R   |         |
| /DF7A | var | NFC/MIFARE Data           | B   | O   |         |