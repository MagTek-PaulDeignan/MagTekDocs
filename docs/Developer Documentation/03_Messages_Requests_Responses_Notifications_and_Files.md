---
title: Messages (Requests, Responses, Notifications, and Files)
layout: home
parent: DynaFlex Family Programmer's Manual
nav_order: 3
---
## Messages (Requests, Responses, Notifications, and Files)

This section describes the general format of messages exchanged between
hosts and devices that are using the common MMS message framework.

Documentation about the specific messages supported by a given device is
provided in section **6 Commands**.

### About Messages

The host and the device communicate with each other by exchanging blocks
of data called **Messages**, which are standardized wrappers containing
a **payload** that is either a command **Request**, a command
**Response**, an unsolicited **Notification**, or a **File**. For
example, the host may send a command **request** message to the device
to change a configuration setting, and the device may send a command
**response** message to indicate the command was successful; when a
cardholder inserts a card, the device may send a **notification**
message to the host that a cardholder has initiated a transaction; the
host may send the device a **file** message to load firmware.

Messages can be nested. For example, a top-level secure wrapper request
from the host to the device may contain an encrypted or signed command
request for the device to unpack, validate, and execute.

**Requests and Responses.** Requests and responses are two of the
message payload types the host and device exchange inside messages. The
combination of a message that contains a **request** payload and a
message that contains the corresponding **response** payload is referred
to generally in this document as a **Command**. The device can only
service one command request at a time, and sends each command response
within a pre-determined finite amount of time after receiving the
request. After sending a command request, the host must wait until the
device returns a response before sending another request, or until the
request is unanswered after a reasonable host-defined timeout period
passes.

**Notifications.** Notifications are a message payload type the host and
device exchange inside messages. The device sends notification messages
to the host if the device’s state changes or if an external event
occurs, such as a cardholder inserting a card. The device can send a
notification at any time, and does not expect a response or any specific
action from the host. By default, the device sends all notifications to
the USB interface. To configure the device to send notifications on
additional connections, use **Command 0x1F02 - Set Notification
Subscriptions**.

**Data Files**. Data Files are a message payload type the host and
device exchange inside messages. The device handles them as a stream, in
that it begins storing the payload of the message before it has received
the final packet of the message, allowing for much larger payloads than
standard requests. This is made possible by restricting the function of
the message to just transferring a file, which means restricting the
message payload to primitive data only; it cannot contain composed TLV
data objects.

Regardless of connection type, all MMS devices use the same schema for
sending and receiving messages, which is documented in section **3.2
Message Format**. For information about transmitting and receiving
messages using specific connection types, which involves following
connection-specific rules for breaking messages down into transmittable
**Message Streams**, see section **2 Connection Types**.

### Message Format

#### Tag-Length-Value (TLV) Encoding

##### About TLV Encoding

All messages exchanged between the host and the device are formatted
using the tag-length-value **Distinguished Encoding Rules** (DER)
defined in ***ITU-T X.680\|ISO/IEC 8824-1*** and ***ITU-T X.690\|ISO/IEC
8825-1***. A subset of these standards is also used in ***EMV Integrated
Circuit Card Specifications for Payment Systems 4.3, Part IV, Annex B
Rules for BER-TLV Data Objects***, so the latter can serve as a useful
point of reference, especially for developers who are familiar with
systems that exchange blocks of EMV data.

Summarizing those specifications, each TLV data object follows these
basic rules:

- The DER standard designates the least significant bit of a byte as
  **bit 1**, and the most significant bit of a byte as **bit 8**. This
  is different from the remainder of the MMS standard, which indexes bit
  numbers starting at 0 to be consistent with each bit position number
  representing that bit’s power of 2.

- The **Tag** or **Identifier** portion of a TLV data object identifies
  the TLV data object. This standard assigns the **tag** (identifier)
  portion of TLV data objects according to the DER format as follows:

  - Bits 8 and 7 specify whether the TLV data object is universal,
    application-defined, context-specific, or private. Most messages in
    this standard contain **context-specific** tags (bits 8 and 7 =
    **10**), meaning different messages reuse the same tags, and the
    tags represent sequentially numbered parameters passed in any
    message. The contents of each context-specific tag (parameter) are
    described for each message in section **6 Commands**.

  - Bit 6 specifies whether the tag is **primitive** (bit 6=**0**),
    meaning it contains its values directly, or **constructed** (bit
    6=**1**), meaning the TLV data object contains more TLV data
    objects.

  - Bits 5 to 1 specify a unique tag number, with 11111 reserved to
    mean:

    - The tag is not a single byte long

    - Bits 7 to 1 of subsequent bytes with bit 8 set to 1 are also part
      of the tag identifier with the most significant of the whole tag
      number in bit 7

    - Bits 7 to 1 of the final byte with bit 8 set to 0 is also part of
      the tag identifier

<!-- -->

- The **Length** portion is calculated as the total length of the Data
  portion that follows it: Lengths can be either short form or long
  form:

  - **Short form** means the length is one byte long in the range 0x00
    to 0x7F.

  - **Long form** means the length is multiple bytes long, starting with
    one-byte 0x80 or greater, where the lower 7 bits specify how many
    subsequent bytes are used to indicate the length. For example, in
    the case of length 8201C3, 0x82 is greater than 0x7F, and the lower
    7 bits equal 0x02, so the next 2 bytes 0x01C3 give the total length
    of the data block, 451 bytes.

  - DER format stipulates all TLV data objects should be encoded using
    the smallest length required to fit the data.

- The **Value** or **Data** portion is the actual payload of the TLV
  data object.

This document provides message definitions in hexadecimal format; when
the host constructs or interprets a message, if no additional encode /
decode filtering or translation is in place at the platform layer, it
should expect each hexadecimal value shown in this document to be
represented as binary bytes in the message stream, not as string
literals. For example, FF is a single byte with all bits set to 1, not
the two-byte string literal “FF.”

##### TLV Example

Below is a brief example of a TLV-encoded request and response for
**Command 0xDF01 - Echo**, wrapped in the standard message format
documented in section **3.2.2 Message Structure**.

The host sends the device a binary byte stream
AA0081040101DF018407DF018103010203, which breaks down as follows:

- AA00 = Standard **Start of Message** / **API Framework Version** (not
  TLV)

- 81, 04, 0101DF01

  - Tag 81 = Request Message Parameter 1, **Message Information**

  - Length 04

  - Value 0101DF01

    - 01 = Request from host to device

    - 01 = Message reference number

    - DF01 = **Command 0xDF01 - Echo**

- 84, 07, DF018103010203

  - Tag 84 = Request Message Parameter 4, **Request Payload**

  - Length 07

  - Value DF018103010203

    - DF01 = Payload format is for Request **Command 0xDF01 - Echo**
      (not TLV)

    - Tag 81 = Payload Parameter 1, **Value to Echo**

    - Length 03

    - Value 010203 = Value to Echo 010203

In response, the device sends the host a binary byte stream
AA0081048201DF018204000000008407DF018103010203, which breaks down as
follows:

- AA00 = Standard **Start of Message** / **API Framework Version** (not
  TLV)

- 81, 04, 8201DF01

  - Tag 81 = Response Message Parameter 1, **Message Information**

  - Length 04

  - Value 8201DF01

    - 82 = Response from device to host

    - 01 = Message reference number

    - DF01 = **Command 0xDF01 - Echo**

- 82, 04, 00000000

  - Tag 82 = Response Message Parameter 2, **Response Status** (one byte
    **Operation Status Summary**, three bytes **Operation Status
    Detail**)

  - Length 04

  - Value 00, 000000 = OK / Done, General / All Good / Requested
    operation was successful

- 84, 07, DF018103010203

  - Tag 84 = Response Message Parameter 4 for **Response Payload**

  - Length 07

  - Value DF018103010203

    - DF01 = Payload format is for Response **Command 0xDF01 - Echo**
      (not TLV)

    - Tag 81 = Payload Parameter 1, **Value to Echo**

    - Length 03

    - Value 010203 = Value to Echo 010203

##### How to Read TLV Tables

Throughout this document, tables that show TLV data objects use some
number of slashes in front of the **Tag** identifier to indicate that
object’s *relative* level of nesting / containment within other TLV data
objects *in the same table*. These levels should not be assumed to be
absolute levels, because a given TLV data object may be nested within
other TLV data objects at any level. The slash notation saves table
space compared to whitespace indenting and is easier to read than a
separate “Nesting Level” column, which can be difficult to notice.

For example:

- **Earth** contains

- **/North America**, which contains

- **//United States**, which contains

- **///California**.

Although **Earth** is a *relative* root within the context of the
objects above, it is not an *absolute* root, because the nested objects
starting with the **Earth** relative root could be wrapped inside
another object representing **Sol Solar System**, and that could be
wrapped in **Milky Way Galaxy**, and so on.

In tables that show TLV data objects, a Length of **var** means the
length is variable, and the device or host must calculate it based on
whatever is nested inside the TLV data object.

See **Table 9 below** for an example.

Table 9 - TLV Table Example

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| A1 | var | TLV data object **A1** contains four directly nested TLV data objects: 81, 82, A3, and 84 for short, or more precisely A1/81, A1/82, A1/A3, and A1/84. A1/82 is optional (Req = **O**), so the length of A1 will vary depending on whether or not A1/82 is included (Len = **var**) or excluded / left implicit. | T | R |  |
| /81 | 01 | TLV data object A1/81 contains one byte and is required. It has no default value because it must be explicitly included. | B | R |  |
| /82 | 03 | TLV data object A1/82 contains three bytes but is optional. If it is not included in this object, the device (or host) assumes the default value 0x4D6F6D. | B | O | 0x4D6F6D |
| /A3 | 08 | TLV data object A1/A3 contains two TLV data objects: 81 and 82, or more precisely, A1/A3/81 and A1/A3/82. Its length is the combined length of its two nested objects: 5 bytes for 81 (tag **81**, length **03**, value **xx xx xx**) and 3 bytes for 82 (tag **82**, length **01**, value **xx**). | T | R |  |
| //81 | 03 | TLV data object A1/A3/81 contains three bytes and is required. | B | R |  |
| //82 | 01 | TLV data object A1/A3/82 contains one byte and is required. | B | R |  |
| /84 | 03 | TLV data object A1/84 contains three bytes that represent distinct values, but to save space, they are length-delimited directly inside A1/84, instead of being assigned their own individual nested TLV data objects. The length of A1/84 is simply the combination of three single bytes. | B | R |  |
| //null | \(1\) | This is just a raw byte inside 84. As a simple byte, it has no tag-length-value structure of its own, so its Tag is shown here as **/null**, and its length is in parentheses to indicate it is not encoded as a TLV data object, it is simply a byte count that can be used to “slice apart” the contents of 84 into separate values. | B | R |  |
| //null | \(1\) | This is another byte contained by 84. | B | R |  |
| //null | \(1\) | This is another byte contained by 84. | B | R |  |

#### Message Structure

Each message type follow a specific structure, detailed in the
subsections below.

##### Request Message

Table 10 - Request Message Format

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 6%" />
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
<td colspan="6"><p>One byte standard <strong>Start of Message</strong>
constant, not in TLV format.</p>
<ul>
<li><p>0xAA = Standard start of message byte</p></li>
</ul></td>
</tr>
<tr>
<td colspan="6"><p>One-byte standard <strong>API Framework
Version</strong> constant, not in TLV format, used for tracking version
compatibility. Devices that implement higher (newer) versions of the API
framework are designed to be reasonably compatible with current and
previous (lower) versions:</p>
<ul>
<li><p>0x00 = Pre-production development (limited breaking changes). At
minimum, every device MagTek ever produces using the MMS framework will
accept this value.</p></li>
<li><p>0x01 = First Production release (no breaking changes)</p></li>
<li><p>0x02 = Second Production release</p></li>
<li><p>Etc.</p></li>
</ul></td>
</tr>
<tr>
<td>81</td>
<td>var</td>
<td>Message Information</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Message Type &amp; Direction</p>
<ul>
<li><p>0x01 = Request from host to device</p></li>
<li><p>0x81 = Request from device to host (Reserved)</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Message Reference Number</p>
<p>The host can use any value in this byte to help match responses with
their corresponding requests. The device includes the same number in the
corresponding response(s). MagTek recommends using a simple incrementing
counter per request the host sends during a session.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(2)</td>
<td><p>Command ID</p>
<p>The fully qualified Command number as defined in section <strong>6
Commands</strong>. The first byte is the Command Group number, which
groups functionally related requests, and the second byte is the Command
number within that group. If the <strong>Request Payload</strong> in the
message contains wrappers, the host should specify the command it is
invoking at the core of the request after all wrappers have been
removed. This value is included primarily for performance and key
conservation; the device simply uses it to make sure it is in a mode
where it is capable of processing the desired command before it begins
processing the <strong>Request Payload</strong>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(var)</td>
<td>Reserved</td>
<td></td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td><p>Request Payload</p>
<p>As documented in the message’s Request table in section <strong>6
Commands</strong>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>9E</td>
<td>var</td>
<td>Reserved</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
</tbody>
</table>

##### Response Message

Table 11 - Response Message Format

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 6%" />
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
<td colspan="6"><p>One byte standard <strong>Start of Message</strong>
constant, not in TLV format.</p>
<ul>
<li><p>0xAA = Standard start of message byte</p></li>
</ul></td>
</tr>
<tr>
<td colspan="6"><p>One-byte standard <strong>API Framework
Version</strong> constant, not in TLV format, used for tracking version
compatibility. Devices that implement higher (newer) versions of the API
framework are designed to be reasonably compatible with current and
previous (lower) versions:</p>
<ul>
<li><p>0x00 = Pre-production development (limited breaking changes). At
minimum, every device MagTek ever produces using the MMS framework will
accept this value.</p></li>
<li><p>0x01 = First Production release (no breaking changes)</p></li>
<li><p>0x02 = Second Production release</p></li>
<li><p>Etc.</p></li>
</ul></td>
</tr>
<tr>
<td>81</td>
<td style="text-align: center;">4</td>
<td>Message Information</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Message Type &amp; Direction</p>
<ul>
<li><p>0x02 = Response from host to device (Reserved)</p></li>
<li><p>0x82 = Response from device to host</p></li>
</ul></td>
<td></td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Message Reference Number</p>
<p>The device echoes back whatever value the host populated in the
Message Reference Number when it made the corresponding request. The
host can use this value to match responses with their corresponding
requests.</p></td>
<td></td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(2)</td>
<td><p>Response ID</p>
<p>Matches the fully qualified Command number from the corresponding
Command Request message, as defined in section <strong>6.1 Command Group
0x10nn - Transactions</strong>.</p>
<ul>
<li><p>0x1001 – Start Transaction</p></li>
</ul></td>
<td></td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(var)</td>
<td>Reserved</td>
<td></td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>04</td>
<td>Response Status</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Operation Status Summary</p>
<ul>
<li><p>0x00 = OK, Done</p></li>
<li><p>0x01 = OK, Started / Running</p></li>
<li><p>0x40 = OK, Done with Warnings</p></li>
<li><p>0x41 = OK, Started / Running with Warnings</p></li>
<li><p>0x80 = Failed to start operation (missing parameters,
etc.)</p></li>
<li><p>0x81 = Failed during operation</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Operation Status Detail (Group)</p>
<p>Operation Status Detail <strong>Group</strong>,
<strong>Subgroup</strong>, and <strong>Status Code</strong> combine to
provide a more detailed report than the Operation Status Summary. See
<strong>Table 12 - Operation Status Detail Codes</strong> on page <a
href="#_Ref133388469"><strong>26</strong></a>.</p>
<ul>
<li><p>0x02 = Security / Permission Problems</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Operation Status Detail (Subgroup)</p>
<p>Operation Status Detail <strong>Group</strong>,
<strong>Subgroup</strong>, and <strong>Status Code</strong> combine to
provide a more detailed report than the Operation Status Summary. See
<strong>Table 12 - Operation Status Detail Codes</strong> on page <a
href="#_Ref133388469"><strong>26</strong></a>.</p>
<ul>
<li><p>0x03 = Device State Issue</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Operation Status Detail (Status Code)</p>
<p>Operation Status Detail <strong>Group</strong>,
<strong>Subgroup</strong>, and <strong>Status Code</strong> combine to
provide a more detailed report than the Operation Status Summary. See
<strong>Table 12 - Operation Status Detail Codes</strong> on page <a
href="#_Ref133388469"><strong>26</strong></a>.</p>
<ul>
<li><p>0x16 = Low Battery (5% or less)</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>var</td>
<td><p>Additional Details</p>
<p>If provided, use this value to help isolate the problem such as the
specific parameter number or EMV tag. See the Command definition in
section <strong>6 Commands</strong> for command-specific Additional
Details.</p></td>
<td></td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td><p>Response Payload</p>
<p>As documented in the message’s Response table in section <strong>6
Commands</strong>.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>9E</td>
<td>var</td>
<td>Reserved</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Ref133388469" class="anchor"></span>Table 12 - Operation
Status Detail Codes

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 5%" />
<col style="width: 13%" />
<col style="width: 5%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr>
<th>Source</th>
<th>Grp</th>
<th>Sub</th>
<th>Cde</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5"><p>The <strong>General</strong> group 0x00 contains
operation status detail codes related to the platform that do not
originate from a specific functional module.</p>
<ul>
<li><p>Subgroup 0x00 = General</p></li>
</ul></td>
</tr>
<tr>
<td>General</td>
<td>00</td>
<td>00</td>
<td>00</td>
<td>All good / requested operation was successful.</td>
</tr>
<tr>
<td>General</td>
<td>00</td>
<td>00</td>
<td>02</td>
<td>Requested Operation Failed</td>
</tr>
<tr>
<td>General</td>
<td>00</td>
<td>00</td>
<td>10</td>
<td>Setting up RTC data and time failure</td>
</tr>
<tr>
<td>General</td>
<td>00</td>
<td>00</td>
<td>11</td>
<td>Setting up RTC alarm failure</td>
</tr>
<tr>
<td>General</td>
<td>00</td>
<td>00</td>
<td>12</td>
<td>Key generation failure</td>
</tr>
<tr>
<td>General</td>
<td>00</td>
<td>00</td>
<td>13</td>
<td>Tamper setting is locked, can’t be changed</td>
</tr>
<tr>
<td>General</td>
<td>00</td>
<td>00</td>
<td>14</td>
<td>Tamper setting requires system reset to continue</td>
</tr>
<tr>
<td>General</td>
<td>00</td>
<td>00</td>
<td>15</td>
<td>Tamper status can’t be cleared, failure</td>
</tr>
<tr>
<td>General</td>
<td>00</td>
<td>00</td>
<td>16</td>
<td>Device has been tampered, need attention</td>
</tr>
<tr>
<td>General</td>
<td>00</td>
<td>00</td>
<td>17</td>
<td>Tamper module failed for other cases</td>
</tr>
<tr>
<td>General</td>
<td>00</td>
<td>00</td>
<td>18</td>
<td>Setting WLAN SoftAP password failure</td>
</tr>
<tr>
<td colspan="5"><p>The <strong>Message Handler</strong> group 0x01
contains operation status detail codes related to parsing and validating
messages.</p>
<ul>
<li><p>Subgroup 0x01 = Device issues that prevent Message Processing
(e.g., Critical Battery, Pending Reset, System Failure, System
Busy).</p></li>
</ul></td>
</tr>
<tr>
<td>Message</td>
<td>01</td>
<td>01</td>
<td>01</td>
<td>Generic Failure.</td>
</tr>
<tr>
<td>Message</td>
<td>01</td>
<td>01</td>
<td>02</td>
<td>Bad message parameter. The host has sent a message to the device
that is not constructed properly.</td>
</tr>
<tr>
<td>Message</td>
<td>01</td>
<td>01</td>
<td>09</td>
<td>Device offline, can not process messages. For example, the device
returns this detail code when it does not have keys injected or has
registered a tamper.</td>
</tr>
<tr>
<td>Message</td>
<td>01</td>
<td>01</td>
<td>10</td>
<td>PIN Key Not Mapped.</td>
</tr>
<tr>
<td>Message</td>
<td>01</td>
<td>01</td>
<td>13</td>
<td>Feature Not Available</td>
</tr>
<tr>
<td colspan="5"><p>The <strong>Request Handler</strong> group 0x02
contains operation status detail codes related to starting actual
command requests.</p>
<ul>
<li><p>Subgroup 0x01 = Data issues (bad, missing, unknown…)</p></li>
<li><p>Subgroup 0x02 = Security / permission problems</p></li>
<li><p>Subgroup 0x03 = Device state issues (busy, not permitted,
tampered, low battery)</p></li>
<li><p>Subgroup 0x04 = Device issues (missing hardware or
features)</p></li>
<li><p>Subgroup 0x05 = TR31 Errors</p></li>
</ul></td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>00</td>
<td>00</td>
<td>Reserved</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>01</td>
<td>00</td>
<td>Reserved</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>01</td>
<td>01</td>
<td>Generic Failure</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>01</td>
<td>02</td>
<td>Bad Message Parameter</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>01</td>
<td>03</td>
<td>Response Payload too big</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>01</td>
<td>07</td>
<td>Internal FW Failure</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>01</td>
<td>0A</td>
<td>Image Failure</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>01</td>
<td>19</td>
<td>Key does not exist</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>01</td>
<td>1A</td>
<td>Not Secured</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>01</td>
<td>1B</td>
<td>Passcode validation failed</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>01</td>
<td>1C</td>
<td>Device is locked</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>02</td>
<td>00</td>
<td>Reserved</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>03</td>
<td>04</td>
<td>Failed, device state issue, no transaction.</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>03</td>
<td>05</td>
<td>Failed, device state issue, cannot cancel.</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>03</td>
<td>08</td>
<td>Failed, device state, Transaction in Progress.</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>03</td>
<td>0C</td>
<td>Failed, device state, Signature Not allowed</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>03</td>
<td>0D</td>
<td>Failed, device state, Wrong Transaction State</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>03</td>
<td>0E</td>
<td>Failed, device state, Invalid PIN Entry State</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>03</td>
<td>0F</td>
<td>Failed, device state, PIN Entry in Session.</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>03</td>
<td>11</td>
<td>Failed, device state, Barcode Read in Progress.</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>03</td>
<td>12</td>
<td>Failed, device state, Pass-through command Not Activated.</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>03</td>
<td>14</td>
<td>Failed, device state, UI Settings in Progress.</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>03</td>
<td>15</td>
<td>Failed, device state, Buzzer in Progress</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>03</td>
<td>16</td>
<td>Failed, device state, Low Battery (5% or less)</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>03</td>
<td>17</td>
<td>Attempt to display Flexible UI page while touchscreen UI
notifications enabled</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>03</td>
<td>18</td>
<td>Request is invalid while card emulation is in progress</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>04</td>
<td>13</td>
<td>Failed, BCR hardware not found.</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>01</td>
<td>Invalid TR31parameter</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>02</td>
<td>Invalid AES length</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>03</td>
<td>Invalid 16-Byte Boundary</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>04</td>
<td>Invalid Length in Message</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>05</td>
<td>Invalid number of optional KBH</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>06</td>
<td>Error in conversion of data type</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>07</td>
<td>Invalid KCV algorithm</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>08</td>
<td>Invalid KCV length</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>09</td>
<td>Invalid Optional KBH ID</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>0A</td>
<td>Invalid KBH ID</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>0B</td>
<td>Invalid algorithm used in KBH</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>0C</td>
<td>Invalid KBH usage</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>0D</td>
<td>Invalid KBH length</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>0E</td>
<td>Invalid version ID for key derivation</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>0F</td>
<td>Invalid KBH mode of use</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>10</td>
<td>TR31 engine not installed</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>11</td>
<td>Invalid Cryptographic operation</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>12</td>
<td>MAC Verification Failed</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>13</td>
<td>Error in Decrypting Key data</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>14</td>
<td>Error in computing MAC over entire message</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>15</td>
<td>Invalid MAC length</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>16</td>
<td>KDF Error</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>17</td>
<td>Buffer Insufficient</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>18</td>
<td>Invalid Storage KPM</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>19</td>
<td>Invalid Storage Secure RAM</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>1A</td>
<td>Invalid Key ID specified in option block</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>1B</td>
<td>Unsupported Key ID specified in option block</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>1C</td>
<td>Invalid Key ID Relationship</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>1D</td>
<td>Protection Key ID not loaded</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>1E</td>
<td>Invalid Data Tag MagTek Custom option block</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>1F</td>
<td>Invalid Kcv</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>20</td>
<td>Invalid Data</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>21</td>
<td>Invalid DUKPT key derivation</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>22</td>
<td>Invalid Exportability</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>23</td>
<td>Invalid Key Class</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>24</td>
<td>Invalid DSN</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>25</td>
<td>Invalid Challenge</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>26</td>
<td>Key Undeletable</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>27</td>
<td>Key not present</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>28</td>
<td>Unsupported Keyset ID</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>29</td>
<td>KPM Error</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>2A</td>
<td>Secure RAM Error</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>2B</td>
<td>Duplicated Key</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>2C</td>
<td>Invalid Key Usage Rule</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>2D</td>
<td>Selftest Key Corrupted</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>2E</td>
<td>Selftest System Key Bitmap Corrupted</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>2F</td>
<td>Selftest System Key Missing</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>30</td>
<td>Selftest System Key Not Loaded</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>31</td>
<td>Invalid Key Storage Limit</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>32</td>
<td>Duplicated Key set</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>33</td>
<td>Key Restriction</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>34</td>
<td>Key Transported by Weaker key</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>35</td>
<td>Repeat Key Agreement</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>36</td>
<td>Security not activated</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>37</td>
<td>Selftest key relocated</td>
</tr>
<tr>
<td>Request Handler</td>
<td>02</td>
<td>05</td>
<td>38</td>
<td>Invalid Selftest Scanned Versus Saved Bitmap</td>
</tr>
<tr>
<td colspan="5"><p>(MAGTEK INTERNAL ONLY FOR NOW, not used)</p>
<p>The <strong>EMV Tag Processing</strong> group 0x03 contains operation
status detail codes related to…</p></td>
</tr>
<tr>
<td>EMV Tag Processing</td>
<td>03</td>
<td>00</td>
<td>00</td>
<td>Reserved</td>
</tr>
<tr>
<td colspan="5"><p>(MAGTEK INTERNAL ONLY FOR NOW, not used)</p>
<p>The <strong>Keys / Cryptographic Handler</strong> group 0x04 contains
operation status detail codes related to…</p></td>
</tr>
<tr>
<td>Keys/Crypto Handler</td>
<td>04</td>
<td>00</td>
<td>00</td>
<td>Reserved</td>
</tr>
<tr>
<td colspan="5"><p>(MAGTEK INTERNAL ONLY FOR NOW, not used)</p>
<p>The <strong>Configuration</strong> group 0x05 contains operation
status detail codes related to…</p></td>
</tr>
<tr>
<td>Configuration</td>
<td>05</td>
<td>00</td>
<td>00</td>
<td>Reserved</td>
</tr>
<tr>
<td colspan="5"><p>(MAGTEK INTERNAL ONLY FOR NOW, not used)</p>
<p>The <strong>Kernel Set ‘A’</strong> group 0xF0 contains operation
status detail codes from a subset of vendor-supplied libraries / modules
used by the device’s firmware. These detail codes are not specifically
enumerated here, they simply provide a standard, controlled channel to
report messages controlled by third parties.</p>
<p>Please report occurrences of this type of failure to MagTek Support
Services.</p></td>
</tr>
<tr>
<td colspan="5"><p>(MAGTEK INTERNAL ONLY FOR NOW, not used)</p>
<p>The <strong>Kernel Set ‘I’</strong> group 0xF1 contains operation
status detail codes from a subset of vendor-supplied libraries / modules
used by the device’s firmware. These detail codes are not specifically
enumerated here, they simply provide a standard, controlled channel to
report messages controlled by third parties.</p>
<p>Please report occurrences of this type of failure to MagTek Support
Services.</p></td>
</tr>
</tbody>
</table>

##### Notification Message

Table 13 - Notification Message Format

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 68%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 9%" />
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
<td colspan="6"><p>One-byte standard <strong>Start of Message</strong>
constant, not in TLV format.</p>
<ul>
<li><p>0xAA = Standard start of message byte</p></li>
</ul></td>
</tr>
<tr>
<td colspan="6"><p>One-byte standard <strong>API Framework
Version</strong> constant, not in TLV format, used for tracking version
compatibility. Devices that implement higher (newer) versions of the API
framework are designed to be reasonably compatible with current and
previous (lower) versions:</p>
<ul>
<li><p>0x00 = Pre-production development (limited breaking changes). At
minimum, every device MagTek ever produces using the MMS framework will
accept this value.</p></li>
<li><p>0x01 = First Production release (no breaking changes)</p></li>
<li><p>0x02 = Second Production release</p></li>
<li><p>Etc.</p></li>
</ul></td>
</tr>
<tr>
<td>81</td>
<td style="text-align: center;">4</td>
<td>Message Information</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Message Type &amp; Direction</p>
<ul>
<li><p>0x03 = Notification from host to device (Reserved)</p></li>
<li><p>0x83 = Notification from device to host</p></li>
</ul></td>
<td></td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td>Reserved, set to 0x00</td>
<td></td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Notification Source</p>
<p>This byte and the <strong>Notification Type</strong> form the first
two bytes of a unique six-byte Notification ID. Use this byte to look up
the <strong>Notification Group</strong> subsection in <strong>7
Notifications</strong>.</p>
<ul>
<li><p>0x01 = Transaction</p></li>
<li><p>0x09 = Firmware Update</p></li>
<li><p>0x10 = Device</p></li>
<li><p>0x18 = User Interface</p></li>
</ul></td>
<td></td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Notification Type</p>
<p>Append this byte to <strong>Notification Source</strong> to look up
the <strong>Notification 0xNNNN</strong> subsection in the Notification
Group subsection to find the documentation for the notification.</p>
<ul>
<li><p>0x01 = Information Update</p></li>
<li><p>0x02 = Warning (e.g. low battery, reset soon)</p></li>
<li><p>0x03 = Action Request (device is asking the host to take
action)</p></li>
<li><p>0x04 = Callback (request for action from host, device waits
before continuing the related operation)</p></li>
<li><p>0x05 = Operation Complete (either success or error)</p></li>
</ul></td>
<td></td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(var)</td>
<td>Reserved</td>
<td></td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>(4)</td>
<td><p>Notification Detail Code</p>
<p>These four bytes, when combined with <strong>Notification
Source</strong> and <strong>Notification Type</strong>, form a six-byte
unique ID for the notification. Each six-byte combination has a specific
meaning and represents a different call to action for the host. See
section <strong>7 Notifications</strong> for <strong>Notification Detail
Codes</strong> tables containing information about the
notification.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>1</td>
<td><p>Category</p>
<ul>
<li><p>0x00 = Power/Reset</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>1</td>
<td><p>Reason</p>
<ul>
<li><p>0x02 = Battery</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>1</td>
<td><p>Reason Detail (Subgroup)</p>
<ul>
<li><p>0x01 = Power Down Imminent</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>1</td>
<td>Reserved, set to 0x00</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>var</td>
<td><p>Additional Detail</p>
<p>See the notification definition in section <strong>7
Notifications</strong> for notification-specific Additional
Details.</p></td>
<td></td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td><p>Notification Payload</p>
<p>As documented in the message’s Notification table in section
<strong>7 Notifications</strong>.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>9E</td>
<td>var</td>
<td>Reserved</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
</tbody>
</table>

##### Data File Message

This message type is used exclusively for transferring larger blocks of
data that can overwhelm the standard message queue. The payload data for
each message is always be treated as an individual file. This message is
only valid after a successful invocation of **Command 0xD811 - Start
Send File to Device (Secured)**, **Command 0xD812 - Start Send File to
Device (Unsecured)**, or **Command 0xD821 - Start Get File from
Device**.

Table 14 - Data File Message Format

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 6%" />
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
<td colspan="6"><p>One byte standard <strong>Start of Message</strong>
constant, not in TLV format.</p>
<ul>
<li><p>0xAA = Standard start of message byte</p></li>
</ul></td>
</tr>
<tr>
<td colspan="6"><p>One-byte standard <strong>API Framework
Version</strong> constant, not in TLV format, used for tracking version
compatibility. Devices that implement higher (newer) versions of the API
framework are designed to be reasonably compatible with current and
previous (lower) versions:</p>
<ul>
<li><p>0x00 = Pre-production development (limited breaking changes). At
minimum, every device MagTek ever produces using the MMS framework will
accept this value.</p></li>
<li><p>0x01 = First Production release (no breaking changes)</p></li>
<li><p>0x02 = Second Production release</p></li>
<li><p>Etc.</p></li>
</ul></td>
</tr>
<tr>
<td>81</td>
<td>08</td>
<td>Message Information</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Message Type &amp; Direction</p>
<ul>
<li><p>0x04 = Data file from host to device</p></li>
<li><p>0x84 = Data file from device to host</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Message Reference Number</p>
<p>The host can use any value in this byte to help match responses with
their corresponding requests. The device includes the same number in the
corresponding response(s). MagTek recommends using a simple incrementing
counter per request the host sends during a session.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(2)</td>
<td>Command Number that prompted this message to be sent, as documented
in <strong>Command Group 0xD8nn - File Operations</strong>.</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(4)</td>
<td><p>File Type</p>
<p>The file type as defined in <strong>Command Group 0xD8nn - File
Operations</strong></p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td><p>File Payload</p>
<p>As documented in section <strong>6.7.1 About Files</strong>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
</tbody>
</table>

Table 15 - Data File Message Example

| Example (Hex) |
|----|
| AA 00 81 08 84 08 D8 21 00 00 00 01 84 40 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F 20 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E 2F 30 31 32 33 34 35 36 37 38 39 3A 3B 3C 3D 3E 3F |