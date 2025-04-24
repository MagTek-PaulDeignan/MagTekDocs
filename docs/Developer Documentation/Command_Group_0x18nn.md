---
title: Command Group 0x18nn - User Interface
layout: home
parent: Commands
nav_order: 3
---

## Command Group 0x18nn - User Interface

---

- [Command Group 0x18nn - User Interface](#command-group-0x18nn---user-interface)
    - [Command 0x1801 - Request Cardholder Signature (Touch Only)](#command-0x1801---request-cardholder-signature-touch-only)
    - [Command 0x1802 - Report Cardholder Selection](#command-0x1802---report-cardholder-selection)
    - [Command 0x1803 - Display Message (Display Only)](#command-0x1803---display-message-display-only)
    - [Command 0x1804 - Read Barcode (BCR Only)](#command-0x1804---read-barcode-bcr-only)
    - [Command 0x1805 - Buzzer](#command-0x1805---buzzer)
    - [Command 0x1821 - Show Image (Display Only)](#command-0x1821---show-image-display-only)
    - [Command 0x1822 - Show QR Code (Display Only)](#command-0x1822---show-qr-code-display-only)
    - [Command 0x1823 - Show Bitmap Image (Display Only)](#command-0x1823---show-bitmap-image-display-only)
    - [Command 0x1830 - Display Flexible UI Pages (Display Only)](#command-0x1830---display-flexible-ui-pages-display-only)
      - [UI Page Option 0x00 Layout](#ui-page-option-0x00-layout)
      - [UI Page Option 0x01 and 0x02 Layout](#ui-page-option-0x01-and-0x02-layout)
      - [UI Page Option 0x03 Layout](#ui-page-option-0x03-layout)
    - [Command 0x1840 – Card Emulation](#command-0x1840-–-card-emulation)

---


#### Command 0x1801 - Request Cardholder Signature (Touch Only)

The host uses this command to prompt a cardholder for a signature.

The sequence of events is as follows:

1)  The device completes a transaction after the host invokes **Command
    0x1001 - Start Transaction**. At the end of the transaction, the
    device has provided data to the host in **Notification 0x0105 -
    Transaction Operation Complete**.

2)  The host decides whether to request a signature from the cardholder.
    For example:

    1)  If the Notification Detail in **Notification 0x0105 -
        Transaction Operation Complete** indicates Signature Capture
        Requested.

    2)  If an application-specific rule requires requesting a signature.

3)  If the host determines it should request a signature, it composes a
    command request in the format below.

4)  The device presents a signature capture interface to the cardholder
    on the display.

5)  The device sends **Notification 0x1805 - User Interface Operation
    Complete** to the host to report data available, timeout, or
    hardware failure.

6)  If the device reported data available, the host uses **Command
    0xD821 - Start Get File from Device** to request file type
    **Signature Capture File** to retrieve the data as a **Signature
    Capture File Type**.

Table 114 - Request Data for Command 0x1801 - Request Cardholder
Signature (Touch Only)

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
href="#request-message"><strong>23</strong></a></td>
</tr>
<tr>
<td colspan="6">1801 = <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Timeout</p>
<p>Timeout in seconds that the device should wait for the cardholder to
sign and confirm completion.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 115 - Response Data for Command 0x1801 - Request Cardholder
Signature (Touch Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1801 = **Command 0x1801 - Request Cardholder Signature (Touch Only)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

If the request started successfully, the Request Status in the message
wrapper is **OK, Started / Running, All good / requested operation was
successful**.

Table 116 - Request Example

| Example (Hex)                                |
|----------------------------------------------|
| AA 00 81 04 01 00 18 01 84 05 18 01 81 01 1E |

Table 117 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 00 18 01 82 04 01 00 00 00 |

#### Command 0x1802 - Report Cardholder Selection

The host uses this command to provide a cardholder selection to the
device when the device itself does not have a display or inputs to
prompt the cardholder for a selection.

The sequence of events is as follows:

1)  The host has already invoked **Command 0x1001 - Start Transaction**
    and the transaction is still in process.

2)  During the transaction, if the device does not have a display or
    touchscreen but needs to show information to the cardholder or needs
    the cardholder to make a selection, it sends the host **Notification
    0x1803 - User Interface Host Action Request** to report Display /
    Cardholder Selection and supporting information.

3)  The host uses its user interface to request a selection from the
    cardholder based on the information and selectable items provided by
    the notification message.

4)  The host sends the user selection to the device by sending the
    command in the format below.

Table 118 - Request Data for Command 0x1802 - Report Cardholder
Selection

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
href="#request-message"><strong>23</strong></a></td>
</tr>
<tr>
<td colspan="6">1802 = <strong>Command 0x1802 - Report Cardholder
Selection</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Cardholder Selection Request Status</p>
<ul>
<li><p>0x00 = Cardholder Selection Request completed, see Selection
Result parameter.</p></li>
<li><p>0x01 = Cardholder Selection Request canceled by cardholder,
Transaction Aborted.</p></li>
<li><p>0x02 = Cardholder Selection Request timed out, Transaction
Aborted.</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>01</td>
<td><p>Selection Result</p>
<p>Menu item index the cardholder selected. If the cardholder made no
selection or the operation terminated abnormally, the device does not
include this parameter.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 119 - Response Data for Command 0x1802 - Report Cardholder
Selection

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1802 = **Command 0x1802 - Report Cardholder Selection** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

If the request started successfully, the Request Status in the message
wrapper is **OK, Started / Running, All good / requested operation was
successful**.

Table 120 - Request Example

| Example (Hex)                                         |
|-------------------------------------------------------|
| AA 00 81 04 01 00 18 02 84 08 18 02 81 01 00 82 01 00 |

Table 121 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 00 18 02 82 04 01 00 00 00 |

#### Command 0x1803 - Display Message (Display Only)

The host uses this command to request that the device display a message
for the cardholder.

The sequence of events is as follows:

1)  The host ensures the device is not currently running another
    command, for example, that it is not running a transaction using
    **Command 0x1001 - Start Transaction**.

2)  The host selects the message it wants to display from the list of
    available pre-determined strings.

3)  The host composes a command request in the format below, and sends
    it to the device.

4)  The device displays the requested message.

    1)  If the Timeout parameter is set to Infinite, the device returns
        a command response message with Response Status, Operation
        Status Summary byte set to 0x00 (OK, Done) after which the host
        is free to send further commands.

    2)  If the timeout parameter is not set to Infinite:

        1)  The device returns a command response message with its
            Response Status, Operation Status Summary byte set to 0x01
            (OK, Started / Running).

        2)  While the host is waiting for the timeout to expire, it
            should not send any commands to the device, because the
            device is busy processing the current command.

        3)  After the timeout period expires, the device blanks the
            display and sends **Notification 0x1805 - User Interface
            Operation Complete** to inform the host.

Table 122 - Request Data for Command 0x1803 - Display Message (Display
Only)

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
href="#request-message"><strong>23</strong></a></td>
</tr>
<tr>
<td colspan="6">1803 = <strong>Command 0x1803 - Display Message (Display
Only)</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Timeout</p>
<ul>
<li><p>0x00 = Infinite. Device leaves the requested message on the
display until the host initiates a change.</p></li>
<li><p>All other values = Timeout in seconds for the device to display
the message.</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0x00</td>
</tr>
<tr>
<td>82</td>
<td>01</td>
<td><p>Message ID</p>
<p>Specify a Display String ID from section <strong>4.3 Display
Strings</strong>.</p></td>
<td>B</td>
<td>O</td>
<td>0x14</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 123 - Response Data for Command 0x1803 - Display Message (Display
Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1803 = **Command 0x1803 - Display Message (Display Only)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 124 - Request Example

| Example (Hex)                             |
|-------------------------------------------|
| AA00 810401551803 8408 1803 810102 820116 |

Table 125 - Response Example

| Example (Hex)                           |
|-----------------------------------------|
| AA00 810482551803 820401000000 84021803 |

#### Command 0x1804 - Read Barcode (BCR Only)

The host uses this command to direct the device to arm or disarm the
barcode reader for reading a barcode outside the scope of a transaction.
This is an immediate directive. To read barcodes within the scope of a
transaction, use **Command 0x1001 - Start Transaction** and its barcode
reader parameters instead.

The sequence of events is as follows:

1)  The host ensures the device is not currently running another
    command, for example, that it is not running a transaction using
    **Command 0x1001 - Start Transaction**.

2)  The host composes a command request in the format below and sends it
    to the device.

3)  If the device has a display, it shows a prompt **SCAN BARCODE**.

4)  The device enables the barcode reader.

    1)  If the **Timeout** parameter is set to **Infinite**:

        1)  The device returns a command response message with Response
            Status, Operation Status Summary byte set to 0x00 (OK, Done)
            after which the host is free to send further commands.

        2)  The host may end the barcode reading session by calling this
            command again with the **Enable** parameter set to
            **Disable**.

    2)  If the **Timeout** parameter is set to a value other than
        **Infinite**:

        1)  The device returns a command response message with its
            Response Status, Operation Status Summary byte set to 0x01
            (OK, Started / Running).

        2)  While the host is waiting for the timeout to expire, it
            should not send any commands to the device, because the
            device is busy processing the current command.

        3)  After the device reads a barcode or the timeout period
            expires, the device sends **Notification 0x1805 - User
            Interface Operation Complete** to report Barcode Reader /
            Read Barcode Result and additional supporting information.

Table 126 - Request Data for Command 0x1804 - Read Barcode (BCR Only)

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
href="#request-message"><strong>23</strong></a></td>
</tr>
<tr>
<td colspan="6">1804 = <strong>Command 0x1804 - Read Barcode (BCR
Only)</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Enable</p>
<ul>
<li><p>0x00 = Disable. The device disables the barcode reader. In this
case, the device ignores all other parameters.</p></li>
<li><p>0x01 = Enable. The device enables the barcode reader.</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td>0x00</td>
</tr>
<tr>
<td>82</td>
<td>01</td>
<td><p>Timeout</p>
<ul>
<li><p>0x00 = Infinite. The device leaves the barcode reader enabled
until it reads a barcode, or until the host sends this command again to
disable the barcode reader.</p></li>
<li><p>All other values = Timeout in seconds for the device to leave the
barcode reader enabled without reading a barcode.</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0x00</td>
</tr>
<tr>
<td>83</td>
<td>01</td>
<td><p>Encrypt Barcode Data</p>
<ul>
<li><p>0x00 = Do Not Encrypt. The device does not encrypt the barcode
data when it sends <strong>Notification 0x1805 - User Interface
Operation Complete</strong>.</p></li>
<li><p>0x01 = Encrypt. The device encrypts the barcode data when it
sends <strong>Notification 0x1805 - User Interface Operation
Complete</strong>.</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0x00</td>
</tr>
<tr>
<td>99</td>
<td>var</td>
<td><p>(MAGTEK INTERNAL ONLY)</p>
<p>Send Command to Barcode Reader</p>
<p>The device sends the command to the barcode reader. The host can use
these commands to change the reader’s internal configuration. See
<em><strong>UM10089_NLS-N1_User_Guide</strong></em> for command
details.</p>
<p>If tag 0x99 is included in the command, the device ignores all other
tags.</p>
<p><strong>Do not change communication settings with this feature.
Changes may result is loss of communications with the
reader.</strong></p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 127 - Response Data for Command 0x1804 - Read Barcode (BCR Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1804 = **Command 0x1804 - Read Barcode (BCR Only)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 128 - Request Example

| Example (Hex)                                    |
|--------------------------------------------------|
| AA00 810401031804 840B 1804 810101 82010F 830101 |

Table 129 - Response Example

| Example (Hex)                  |
|--------------------------------|
| AA00 810482031804 820401000000 |

#### Command 0x1805 - Buzzer

The host uses this command to start a buzzer for playing a sequence of
tones. Each sequence can have a minimum of 1 to maximum of 10 tones.

The sequence of events is as follows:

1)  The host ensures the device is not currently running another
    command, for example, that it is not running a transaction using
    **Command 0x1001 - Start Transaction**.

2)  The host composes a command request in the format below and sends it
    to the device.

3)  The device plays a specific tone sequence as the command specified.
    After finish, the device sends **Notification 0x1805 - User
    Interface Operation Complete** to report Buzzer/Buzzer Result.

> The host should wait for **Notification 0x1805 - User Interface
> Operation Complete** before sending another command.
>
> If the buzzer is current playing a sequence of tones and any
> transaction that uses the buzzer to make a sound is started, the
> device will stop the buzzer for that transaction to take over.

Table 130 - Request Data for Command 0x1805 - Buzzer

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
href="#request-message"><strong>23</strong></a></td>
</tr>
<tr>
<td colspan="6">1805 = <strong>Command 0x1805 - Buzzer</strong></td>
</tr>
<tr>
<td>81</td>
<td>N*4</td>
<td><p>N = Number of tones</p>
<ul>
<li><p>0x01 – Min (1 tone)</p></li>
<li><p>0x0A – Max (10 tones)</p></li>
</ul>
<p>4 = 4 bytes data parameter for each tone in the sequence</p>
<p>Byte0-Byte1 – Frequency in units of 1 Hz</p>
<ul>
<li><p>0x0000..0x0031 (&lt; 50 Hz, Silent)</p></li>
<li><p>0x0032 - Min (50 Hz)</p></li>
<li><p>0x0FA0 - Max (4000 Hz)</p></li>
<li><p>0x0FA1..0xFFFF (&gt; 4000 Hz, Error)</p></li>
</ul>
<p>Byte 2-Byte3 – Duration of tone in units of 1 millisecond</p>
<ul>
<li><p>0x0001 – Min (1 ms)</p></li>
<li><p>0xFFFF – Max (65535 ms)</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 131 - Response Data for Command 0x1805 - Buzzer

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1805 = **Command 0x1805 - Buzzer** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 132 - Request Example for a sequence of 5 tones

| Example (Hex) |
|----|
| AA00 810401031805 8418 1805 8114 00C8 01F4 0190 01F4 0258 01F4 0190 01F4 00C8 01F4 |

Table 133 - Response Example

| Example (Hex)                  |
|--------------------------------|
| AA00 810482031805 820401000000 |

#### Command 0x1821 - Show Image (Display Only)

The host uses this command to trigger the device to immediately show a
pre-loaded image on the display, provided the device is not in a mode
that has exclusive use of the display (such as during a transaction).
This is an immediate and temporary directive. For a solution that
affects the device’s idle page behavior on a more permanent basis, see
**Property 1.2.3.1.1.1 Custom Idle Page Image**. This command is
different from **Command 0x1823 - Show Bitmap Image** in that the
bitmaps are pre-loaded and persistently stored in the device and can not
be composited with each other.

The sequence of events is as follows:

1)  The host makes sure it has loaded the image into at least one of the
    device’s Custom Idle Page Image slots using **Command 0xD812 - Start
    Send File to Device (Unsecured)**.

2)  The host makes sure the device is in Active/Idle state (meaning the
    display is fully powered on and is not in a mode that has exclusive
    use of the display, such as processing a transaction).

3)  The host calls this command to show the image loaded into the
    desired slot number.

4)  The device shows the specified image on the display until the device
    is no longer in Active/Idle.

Table 134 - Request Data for Command 0x1821 - Show Image (Display Only)

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
href="#request-message"><strong>23</strong></a></td>
</tr>
<tr>
<td colspan="6">1821 = <strong>Command 0x1821 - Show Image (Display
Only)</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Custom Idle Page Image Number</p>
<ul>
<li><p>0x01 = Show custom image 1</p></li>
<li><p>0x02 = Show custom image 2</p></li>
<li><p>0x03 = Show custom image 3</p></li>
<li><p>0x04 = Show custom image 4</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>01</td>
<td><p>Display Option</p>
<ul>
<li><p>0x00 = Default to cover/uncover the top status bar depends on the
current status of the display. If the current display shows the top
status bar, the Show Image command won’t cover the top status bar. If
the current display doesn’t show the top status bar, the Show Image
command will cover the top status bar.</p></li>
<li><p>0x01 = Cover the top status bar regardless of the current status
of the display.</p></li>
<li><p>0x02 = Not cover the top status bar regardless of the current
status of the display.</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0</td>
</tr>
<tr>
<td>83</td>
<td>01</td>
<td><p>Display Time</p>
<ul>
<li><p>0x00 = Show image until device changes state</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 135 - Response Data for Command 0x1821 - Show Image (Display Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1821 = **Command 0x1821 - Show Image (Display Only)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

If the request started successfully, the Request Status in the message
wrapper is **All Good, Requested Operation Was Successful**.

Table 136 - Request Example

| Example (Hex)                                         |
|-------------------------------------------------------|
| AA 00 81 04 01 2C 18 21 84 08 18 21 81 01 03 83 01 00 |

Table 137 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 2C 18 21 82 04 00 00 00 00 |

#### Command 0x1822 - Show QR Code (Display Only)

The host uses this command to direct the device to immediately show a QR
code on the display, provided the device is not in a mode that has
exclusive use of the display (such as during a transaction).

The sequence of events is as follows:

1)  The host ensures the device is not currently running another
    command, for example, that it is not running a transaction using
    **Command 0x1001 - Start Transaction**.

2)  The host selects the data for the QR code it wants to display.

3)  The host composes a command request in the format below and sends it
    to the device.

4)  The device generates and displays the QR code.

    1)  If the **Display Time** parameter is set to **Indefinite**, the
        device returns a command response message with Response Status,
        Operation Status Summary byte set to 0x00 (OK, Done) after which
        the host is free to send further commands.

    2)  If the **Display Time** parameter is set to a number of seconds:

        1)  The device returns a command response message with its
            Response Status, Operation Status Summary byte set to 0x01
            (OK, Started / Running).

        2)  While the host is waiting for the timeout to expire, it
            should not send any commands to the device, because the
            device is busy processing the current command.

        3)  After the timeout period expires, the device unlocks to
            allow other commands and sends **Notification 0x1805 - User
            Interface Operation Complete** to report **Display** /
            **Display Message** / **Timed Out** / **Reserved**.

Table 138 - Request Data for Command 0x1822 - Show QR Code (Display
Only)

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
href="#request-message"><strong>23</strong></a></td>
</tr>
<tr>
<td colspan="6">1822 = Command 0x1822 - Show QR Code (Display Only)</td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Display Time</p>
<ul>
<li><p>0x00 = Indefinite</p></li>
<li><p>0x01 to 0xFF = 1 to 255 seconds</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0x00</td>
</tr>
<tr>
<td>82</td>
<td>var</td>
<td><p>Data to Encode</p>
<p>See <em><strong>ISO/IEC 18004:2015</strong></em></p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>01</td>
<td><p>Error Correction</p>
<ul>
<li><p>0x00 = Low</p></li>
<li><p>0x01 = Medium</p></li>
<li><p>0x02 = Quartile</p></li>
<li><p>0x03 = High</p></li>
</ul>
<p>See <em><strong>ISO/IEC 18004:2015</strong></em></p></td>
<td>B</td>
<td>O</td>
<td>0x00</td>
</tr>
<tr>
<td>84</td>
<td>01</td>
<td><p>Mask Pattern</p>
<ul>
<li><p>0x00 to 0x07 = Mask Pattern</p></li>
<li><p>0xFF = Device Select Optimal Mask Pattern</p></li>
</ul>
<p>See <em><strong>ISO/IEC 18004:2015</strong></em></p></td>
<td>B</td>
<td>O</td>
<td>0xFF</td>
</tr>
<tr>
<td>85</td>
<td>01</td>
<td><p>Minimum Version</p>
<p>Must be less than or equal to Maximum Version</p>
<ul>
<li><p>0x01 to 0x28 = Version 1 to Version 40</p></li>
</ul>
<p>See <em><strong>ISO/IEC 18004:2015</strong></em></p></td>
<td>B</td>
<td>O</td>
<td>0x01</td>
</tr>
<tr>
<td>86</td>
<td>01</td>
<td><p>Maximum Version</p>
<p>Must be greater than or equal to Minimum Version</p>
<ul>
<li><p>0x01 to 0x28 = Version 1 to Version 40</p></li>
</ul>
<p>See <em><strong>ISO/IEC 18004:2015</strong></em></p></td>
<td>B</td>
<td>O</td>
<td>0x28</td>
</tr>
<tr>
<td>87</td>
<td>03</td>
<td><p>Block Color</p>
<p>Use RRGGBB format.</p></td>
<td>B</td>
<td>O</td>
<td><p>0x000000</p>
<p>(Black)</p></td>
</tr>
<tr>
<td>88</td>
<td>03</td>
<td><p>Background Color</p>
<p>Use RRGGBB format.</p></td>
<td>B</td>
<td>O</td>
<td><p>0xFFFFFF</p>
<p>(White)</p></td>
</tr>
<tr>
<td>89</td>
<td>var</td>
<td><p>Prompt</p>
<p>Text for the device to display below the QR code. Because the device
shows the Prompt using a proportional font, the maximum length that fits
the display depends on the text and the device’s orientation set by
Property 1.2.3.1.1.2 Custom Idle Page Image Device Locked (Display
Only)<strong>.</strong> In Landscape orientation, the upper limit is
approximately 30 characters. In Portrait orientation, the limit is
approximately 22 characters.</p></td>
<td>B</td>
<td>O</td>
<td>No prompt</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 139 - Response Data for Command 0x1822 - Show QR Code (Display
Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1822 = **Command 0x1822 - Show QR Code (Display Only)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

If the request started successfully, the Request Status in the message
wrapper is **All Good, Requested Operation Was Successful**.

Table 140 - Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 05 18 22 84 41 18 22 81 01 3C 82 0F 54 68 69 73 20 69 73 20 61 20 74 65 73 74 21 83 01 00 84 01 FF 85 01 01 86 01 28 87 03 00 00 00 88 03 FF FF FF 89 13 50 6c 65 61 73 65 20 73 63 61 6e 20 51 52 20 63 6f 64 65 |

Table 6‑29 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 2C 18 22 82 04 00 00 00 00 |

Table 6‑30 - Notification Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 83 00 18 05 82 04 02 01 00 00 |

#### Command 0x1823 - Show Bitmap Image (Display Only)

The host uses this command to trigger the device to immediately show a
bitmap file the host includes as a parameter, provided the device is not
in a mode that has exclusive use of the display (such as during a
transaction).

This is an immediate and temporary directive. For a solution that
affects the device’s idle page behavior on a more permanent basis, see
**Property 1.2.3.1.1.1 Custom Idle Page Image**. This command is
different from **Command 0x1821 - Show Image (Display Only)** in that
the host sends bitmaps as parameters instead of pre-loading them, and
the host can call this command multiple times without clearing the
display to show multiple bitmaps on the display at the same time.

The sequence of events is as follows:

1)  The host ensures the device is not currently running another
    command, for example, that it is not running a transaction using
    **Command 0x1001 - Start Transaction**.

2)  The host selects a bitmap file it wants to display.

3)  The host composes a command request in the format below and sends it
    to the device.

4)  If the host includes the **Background Color** parameter, the device
    clears the display using the specified color. If the host does not
    include that parameter, the device does not clear the display.

5)  The device shows the bitmap with the upper left corner at the
    specified **X Position** and **Y Position**. If the host omits
    either parameter, the device centers the bitmap along the
    unspecified axis.

    1)  If the **Display Time** parameter is **Indefinite** or is not
        included, the device returns a command response message with
        Response Status, Operation Status Summary byte set to 0x00 (OK,
        Done) after which the host is free to send further commands.

    2)  If the timeout parameter is set to a specific number of seconds:

        1)  The device returns a command response message with its
            Response Status, Operation Status Summary byte set to 0x01
            (OK, Started / Running).

        2)  While the host is waiting for the timeout to expire, it
            should not send any commands to the device, because the
            device is busy processing the current command.

        3)  After the timeout period expires, the device unlocks to
            allow other commands and sends **Notification 0x1805 - User
            Interface Operation Complete** to inform the host.

Table 141 - Request Data for Command 0x1823 - Show Bitmap Image (Display
Only)

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
href="#request-message"><strong>23</strong></a></td>
</tr>
<tr>
<td colspan="6">1823 = <strong>Command 0x1823 - Show Bitmap Image
(Display Only)</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Display Time</p>
<ul>
<li><p>0x00 = Indefinite</p></li>
<li><p>0x01 to 0xFF = 1 to 255 seconds</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0x00</td>
</tr>
<tr>
<td>82</td>
<td>03</td>
<td><p>Background Color</p>
<p>Use RRGGBB format.</p></td>
<td>B</td>
<td>O</td>
<td>N/A</td>
</tr>
<tr>
<td>83</td>
<td>02</td>
<td><p>X Position</p>
<p>The device places the left edge of the image at this pixel position
relative to the left edge of the display, which is position 0x0000. This
parameter plus the pixel width of the image must be less than the pixel
width of the display. The display’s pixel width depends on the device’s
orientation set by Property 1.2.3.1.1.2 Custom Idle Page Image Device
Locked (Display Only)For information about the resolution of the
display, see the specifications in the device’s <em><strong>Installation
and Operation Manual</strong></em>.</p></td>
<td>B</td>
<td>O</td>
<td>Centered</td>
</tr>
<tr>
<td>84</td>
<td>02</td>
<td><p>Y Position</p>
<p>The device places the top edge of the image at this pixel position
relative to the top edge of the display, which is position 0x0000. This
parameter plus the pixel height of the image must be less than the pixel
height of the display. The display’s pixel height depends on the
device’s orientation set by Property 1.2.3.1.1.2 Custom Idle Page Image
Device Locked (Display Only). For information about the resolution of
the display, see the specifications in the device’s
<em><strong>Installation and Operation Manual</strong></em>.</p></td>
<td>B</td>
<td>O</td>
<td>Centered</td>
</tr>
<tr>
<td>85</td>
<td>var</td>
<td><p>Bitmap</p>
<p>Image encoded in full BMP file format as defined by Microsoft (e.g.,
starting with “BM”)</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>86</td>
<td>01</td>
<td><p>Display Option</p>
<ul>
<li><p>0x00 = Default to cover/uncover the top status bar depends on the
current status of the display. If the current display shows the top
status bar, the Show Bitmap Image command won’t cover the top status
bar. If the current display doesn’t show the top status bar, the Show
Bitmap Image command will cover the top status bar.</p></li>
<li><p>0x01 = Cover the top status bar regardless of the current status
of the display.</p></li>
<li><p>0x02 = Not cover the top status bar regardless of the current
status of the display.</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>0</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including Request
Message found on page <a href="#request-message">23</a></td>
</tr>
</tbody>
</table>

Table 142 - Response Data for Command 0x1823 - Show Bitmap Image
(Display Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1823 = **Command 0x1823 - Show Bitmap Image (Display Only)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

If the request started successfully, the Request Status in the message
wrapper is **All Good, Requested Operation Was Successful**.

Table 143 - Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 05 18 22 84 41 18 22 81 01 3C 82 0F 54 68 69 73 20 69 73 20 61 20 74 65 73 74 21 83 01 00 84 01 FF 85 01 01 86 01 28 87 03 00 00 00 88 03 FF FF FF 89 13 50 6c 65 61 73 65 20 73 63 61 6e 20 51 52 20 63 6f 64 65 |

Table 6‑29 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 2C 18 22 82 04 00 00 00 00 |

Table 6‑30 - Notification Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 83 00 18 05 82 04 02 01 00 00 |

#### Command 0x1830 - Display Flexible UI Pages (Display Only)

**DF II PED Operation Flow Proposal with Flexible UI Framework**

<img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image7.png"
style="width:6.5in;height:5.22361in"
alt="A diagram of a device Description automatically generated" />

<img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image8.png"
style="width:6.42361in;height:2.275in"
alt="A screenshot of a document Description automatically generated" />

<img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image9.png"
style="width:6.5in;height:4.21806in"
alt="A screenshot of a diagram Description automatically generated" />

<img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image10.png"
style="width:6.5in;height:3.425in"
alt="A screenshot of a computer program Description automatically generated" />

The host uses this command to display Flexible UI pages in the following
layout:

##### UI Page Option 0x00 Layout

The host uses this option to display a maximum of 5 lines of host
provided text, and 1 optional green functional button, Middle – label
with a String ID that associates it with a configured String message.
See

**Table 343 – Default User Interface String IDs and Strings**. When the
user presses this button, the device sends a notification to the host to
indicate this button is pressed. See **Notification 0x1803 - User
Interface Host Action Request.** After that, the host will decide what
to do next.

Recommend maximum number of characters setting for this page:

- Landscape Screen Orientation:

> Each text line can fit about 18 Upper case wide size characters like
> “WM”, 23 Upper case regular size characters such as “ABC”, 21 lower
> case wide size characters like “wm”, or 30 lower case regular size
> characters like “abc”.
>
> Button text can fit about 5 Upper case wide size characters like “WM”,
> 8 Upper case regular size characters like “ABC”, 6 lower case wide
> size characters like “wm”, or 9 lower case regular size characters
> like “abc”.

- Portrait Screen Orientation:

> Each text line can fit about 13 Upper case wide size characters like
> “WM”, 17 Upper case regular size characters like “ABC”, 14 lower case
> wide size characters like “wm”, or 20 lower case regular size
> characters like abc.
>
> Button text can fit about 4 Upper case wide size characters like “WM”,
> 6 Upper case regular size characters like “ABC”, 5 lower case wide
> size characters like “wm”, or 7 lower case regular size characters
> like “abc”.

<img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image11.png"
style="width:3.38542in;height:2.54167in"
alt="A screenshot of a computer program Description automatically generated" /><img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image12.png"
style="width:2.54167in;height:3.375in"
alt="A screenshot of a computer Description automatically generated" />

##### UI Page Option 0x01 and 0x02 Layout

The host uses UI Page Option **0x01** to display a page with a title, a
maximum of 6 data buttons (2 rows and 3 columns in Landscape Screen
Orientation, 3 rows and 2 columns in Portrait Screen Orientation) with
text, and maximum 3 functional buttons with a color option of red,
green, or yellow.

The host uses UI Page Option **0x01** to display a page with a title,
maximum of 4 data buttons (2 rows and 2 columns in Landscape Screen
Orientation, 2 rows and 2 columns in Portrait Screen Orientation) with
text, and maximum 3 functional buttons with a color option of red,
green, or yellow.

The host uses UI Page Option **0x02** to display a page with a title,
maximum of 6 data buttons (2 rows and 3 columns in Landscape Screen
Orientation, 3 rows and 2 columns in Portrait Screen Orientation) with
\$Amount, and maximum 3 functional buttons with a color option of red,
green, or yellow.

The host uses UI Page Option **0x02** to display a page with a title,
maximum of 4 data buttons (2 rows and 2 columns in Landscape Screen
Orientation, 2 rows and 2 columns in Portrait Screen Orientation) with
\$Amount, and maximum 3 functional buttons with a color option of red,
green, or yellow.

The button with **\$** Amount value is host provided. The title, data
buttons text, and functional buttons are labeled with String IDs
associated with configured String messages. See

**Table 343 – Default User Interface String IDs and Strings**. When the
user presses any button, the device sends a notification to the host to
indicate the corresponding button is pressed. See **Notification
0x1803 - User Interface Host Action Request.** After that, the host will
decide what to do next.

Recommend maximum number of character settings for this page:

- Landscape Screen Orientation:

  - The title text can fit about 18 Upper case wide size characters like
    “WM”, 23 Upper case regular size characters like “ABC”, 21 lower
    case wide size characters like “wm”, or 30 lower case regular size
    characters like “abc”.

  - The 3 columns data button’s text can fit about 5 Upper case wide
    size characters like “WM”, 8 Upper case regular size characters like
    “ABC”, 6 lower case wide size characters like “wm”, or 9 lower case
    regular size characters like “abc”.

  - The 2 columns data button’s text can fit about 9 Upper case wide
    size characters like “WM”, 13 Upper case regular size characters
    like “ABC”, 9 lower case wide size characters like “wm”, or 15 lower
    case regular size characters like “abc”.

  - The Functional button’s text can fit about 5 Upper case wide size
    characters like “WM”, 8 Upper case regular size characters like
    “ABC”, 6 lower case wide size characters like “wm”, or 9 lower case
    regular size characters like “abc”.

- Portrait Screen Orientation:

  - The title text can fit about 13 Upper case wide size characters like
    “WM”, 17 Upper case regular size characters like “ABC”, 14 lower
    case wide size characters like “wm”, or 20 lower case regular size
    characters like “abc”.

  - The 2 columns data button’s text can fit about 6 Upper case wide
    size characters like “WM”, 10 Upper case regular size characters
    like “ABC”, 7 lower case wide size characters like “wm”, or 11 lower
    case regular size characters like “abc”.

  - The functional button’s text can fit about 4 Upper case wide size
    characters like “WM”, 6 Upper case regular size characters like
    “ABC”, 5 lower case wide size characters like “wm”, or 7 lower case
    regular size characters like “abc”.

**The Layout for a page with a title, a maximum of 4 data buttons with
text/\$Amount, and a maximum of 3 functional buttons:**

<img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image13.png"
style="width:3.38542in;height:2.55208in"
alt="A screenshot of a computer program Description automatically generated" />
<img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image14.png"
style="width:2.5625in;height:3.38542in"
alt="A screenshot of a phone Description automatically generated" />

**The Layout for a page with a title, 5 to 6 data buttons with a
text/\$Amount, and maximum of 3 functional buttons:**

<img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image15.png"
style="width:3.375in;height:2.54167in"
alt="A screenshot of a computer program Description automatically generated" />
<img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image16.png"
style="width:2.5625in;height:3.39583in"
alt="A screenshot of a computer Description automatically generated" />

##### UI Page Option 0x03 Layout

The host uses this option to display a page with the following elements:
a title, a section for uploading a custom image, an option at the
bottom-left corner to display either the Device Serial Number or
host-provided text, and a maximum of one functional green button
positioned on the right.

The title and functional button are labeled with String IDs associated
with configured String message. See

**Table 343 – Default User Interface String IDs and Strings**. When the
user presses this button, the device sends a notification to the host to
indicate the corresponding button is pressed. See **Notification
0x1803 - User Interface Host Action Request.** After that, the host will
decide what to do next.

Recommend maximum number of characters and bitmap image setting for this
page:

- Landscape Screen Orientation:

  - Title text can fit about 18 Upper case wide size characters like
    “WM”, 23 Upper case regular size characters like “ABC”, 21 lower
    case wide size characters like “wm”, or 30 lower case regular size
    characters like “abc”.

  - Bottom left corner text can fit about 8 Upper case wide size
    characters like “WM”, 12 Upper case regular size characters like
    “ABC”, 9 lower case wide size characters like “wm”, or 15 lower case
    regular size characters like “abc”.

  - Functional button text can fit about 5 Upper case wide size
    characters like “WM”, 8 Upper case regular size characters like
    “ABC”, 6 lower case wide size characters like “wm”, or 9 lower case
    regular size characters like “abc”.

  - Bitmap image maximum width is 320px, height is 140px. Color depth
    can be 24-bit (True Color, RGB), 16-bit (5:5:5:1, RGB Hi Color),
    8-bit (256 Color), 4-bit (16 Color), or 1-bit (monochrome)

- Portrait Screen Orientation:

  - Title text can fit about 13 Upper case wide size characters like
    “WM”, 17 Upper case regular size characters like “ABC”, 14 lower
    case wide size characters like “wm”, or20 lower case regular size
    characters like “abc”.

  - Bottom left corner text can fit about 8 Upper case wide size
    characters like “WM”, 12 Upper case regular size characters like
    “ABC”, 9 lower case wide size characters like “wm”, or 15 lower case
    regular size characters like “abc”.

  - Functional button text can fit about 4 Upper case wide size
    characters like “WM”, 6 Upper case regular size characters like
    “ABC”, 5 lower case wide size characters like “wm”, or 7 lower case
    regular size characters like “abc”.

  - Bitmap image maximum width is 240px, height is 220px. Color depth
    can be 24-bit (True Color, RGB), 16-bit (5:5:5:1, RGB Hi Color),
    8-bit (256 Color), 4-bit (16 Color), or 1-bit (monochrome)

<img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image17.png"
style="width:3.38542in;height:2.55208in"
alt="A screenshot of a computer error Description automatically generated" />
<img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image18.png"
style="width:2.54167in;height:3.375in"
alt="A screenshot of a computer Description automatically generated" />

Table 144 – Request Data for Command 0x1830

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
<strong>Response Message</strong> found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
<tr>
<td colspan="6">1830 = <strong>Command 0x1830 - Display Flexible UI
Pages (Display Only)</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Display Time</p>
<ul>
<li><p>0x00 – Infinitive. Device leaves the requested page on the
display until the host initiates a change.</p></li>
<li><p>0x01 to 0xFF = RFU</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>01</td>
<td><p>UI page option</p>
<ul>
<li><p>0x00 – Page with up to 5 lines of text and up to 1 functional
button Middle. See Tag A1.</p></li>
<li><p>0x01 – Page with a title, up to 6 buttons with text, and up to 3
functional buttons. See Tag 83, A2 and A4.</p></li>
<li><p>0x02 – Page with a title, up to 6 buttons with $Amount, and up to
3 functional buttons. See Tag 83, A3 and A4.</p></li>
<li><p>0x03 – Page with a title, a custom image, an optional bottom left
corner with SN or Text, and up to 1 functional button Right. See Tag 83
and A5.</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>02</td>
<td><p>Text String ID for a tile of UI page option: 0x01, 0x02, 0x03</p>
<p>See</p>
<p><strong>Table 343 – Default User Interface String IDs and
Strings</strong></p>
<p>If host wants to disable this title, do not include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>A1</td>
<td>var</td>
<td><p>Text string parameters for UI page option: 0x00</p>
<p>The parameter in this TLV data object allow the host to enable and
disable the data base for UI page option 0x00</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>var</td>
<td><p>Text string (&lt;= 30 characters) for line 1, end with NULL
char.</p>
<p>If host wants to disable this line, do not include this tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>var</td>
<td><p>Text string (&lt;= 30 characters) for line 2, end with NULL
char.</p>
<p>If host wants to disable this line, do not include this tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>var</td>
<td><p>Text string (&lt;= 30 characters) for line 3, end with NULL
char.</p>
<p>If host wants to disable this line, do not include this tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/84</td>
<td>var</td>
<td><p>Text string (&lt;= 30 characters) for line 4, end with NULL
char.</p>
<p>If host wants to disable this line, do not include this tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/85</td>
<td>var</td>
<td><p>Text string (&lt;= 30 characters) for line 5, end with NULL
char.</p>
<p>If host wants to disable this line, do not include this tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/86</td>
<td>02</td>
<td><p>Function button Middle option.</p>
<p>String ID = Enable functional button Middle with a String ID
associates with a configured String message. See</p>
<p><strong>Table 343 – Default User Interface String IDs and
Strings</strong></p>
<p>When user presses this button, device sends notification to the host
to indicate the functional button Middle is pressed. See
<strong>Notification 0x1803 - User Interface Host Action
Request</strong></p>
<p>If host wants to disable this button, do not include this
tag</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>A2</td>
<td>var</td>
<td><p>Button text String ID parameters for UI page option: 0x01 and
0x02. The parameter in this TLV data object allows the host to enable
and disable the data base.</p>
<p>When user presses any button, device sends notification to the host
to indicate which button is pressed. See <strong>Notification 0x1803 -
User Interface Host Action Request</strong></p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>02</td>
<td><p>Text String ID for button 1. See</p>
<p><strong>Table 343 – Default User Interface String IDs and
Strings</strong>.</p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>02</td>
<td><p>Text String ID for button 2. See</p>
<p><strong>Table 343 – Default User Interface String IDs and
Strings</strong>.</p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>02</td>
<td><p>Text String ID for button 3. See</p>
<p><strong>Table 343 – Default User Interface String IDs and
Strings</strong>.</p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/84</td>
<td>02</td>
<td><p>Text String ID for button 4. See</p>
<p><strong>Table 343 – Default User Interface String IDs and
Strings</strong> .</p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/85</td>
<td>02</td>
<td><p>Text String ID for button 5. See</p>
<p><strong>Table 343 – Default User Interface String IDs and
Strings</strong> .</p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/86</td>
<td>02</td>
<td><p>Text String ID for button 6. See</p>
<p><strong>Table 343 – Default User Interface String IDs and
Strings</strong> .</p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>A3</td>
<td>var</td>
<td><p>Button $Amount parameters for UI page option: 0x01, 0x02</p>
<p>The parameter in this TLV data object allows the host to enable and
disable the data base for UI page option 0x01 and 0x02</p>
<p>When user presses any button, device sends notification to the host
to indicate which amount button is pressed. See <strong>Notification
0x1803 - User Interface Host Action Request</strong></p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>04</td>
<td><p>Value $Amount for button 1.</p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>04</td>
<td><p>Value $Amount for button 2.</p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>04</td>
<td><p>Value $Amount for button 3.</p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/84</td>
<td>04</td>
<td><p>Value $Amount for button 4.</p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/85</td>
<td>04</td>
<td><p>Value $Amount for button 5.</p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/86</td>
<td>04</td>
<td><p>Value $Amount for button 6.</p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>A4</td>
<td>var</td>
<td><p>Functional buttons parameters for UI page option: 0x01 and 0x02.
The parameter in this TLV data object allows the host to enable and
disable the data base.</p>
<p>When user presses any button, the device sends notification to the
host to indicate which functional button is pressed. See
<strong>Notification 0x1803 - User Interface Host Action
Request</strong></p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>03</td>
<td><p>Text String ID and color option for functional button Left.
See</p>
<p><strong>Table 343 – Default User Interface String IDs and
Strings</strong>.</p>
<p>Byte 0-1: String ID</p>
<p>Byte 2: color option</p>
<p>0x00 = red</p>
<p>0x01 = green</p>
<p>0x02 = yellow</p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>03</td>
<td><p>Text String ID and color option for functional button Middle.
See</p>
<p><strong>Table 343 – Default User Interface String IDs and
Strings</strong> .</p>
<p>Byte 0-1: String ID</p>
<p>Byte 2: color option</p>
<p>0x00 = red</p>
<p>0x01 = green</p>
<p>0x02 = yellow</p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>03</td>
<td><p>Text String ID and color option for functional button Right.
See</p>
<p><strong>Table 343 – Default User Interface String IDs and
Strings</strong> .</p>
<p>Byte 0-1: String ID</p>
<p>Byte 2: color option</p>
<p>0x00 = red</p>
<p>0x01 = green</p>
<p>0x02 = yellow</p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>A5</td>
<td>var</td>
<td><p>Parameters for UI page option 0x03</p>
<p>The parameter in this TLV data object allow the host to enable and
disable the data base</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>02</td>
<td><p>Text String ID for green functional button Right. See</p>
<p><strong>Table 343 – Default User Interface String IDs and
Strings</strong> .</p>
<p>When user presses this button, device sends notification to the host
to indicate the functional button Right is pressed. See
<strong>Notification 0x1803 - User Interface Host Action
Request</strong></p>
<p>If host wants to disable this button, don’t include this
tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>02</td>
<td><p>X Position.</p>
<p>If host wants device to display the image in the center of the
loading image area, don’t include this tag.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>02</td>
<td><p>Y Position.</p>
<p>If host want device to display the image in the center of the loading
image area, don’t include this tag</p>
<p>Note:</p>
<p>Y pos &gt; = 50px</p>
<p>Y pos + Image Height &lt;= 190px Landscape Screen Orientation</p>
<p>Y pos + Image Height &lt;= 270px Portrait Screen Orientation</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/84</td>
<td>var</td>
<td><p>Bitmap</p>
<p>Image encoded in full BMP file format as defined by Microsoft (e.g,
starting with “BM”)</p>
<p>Image Width Max = 320px Landscape Screen Orientation</p>
<p>Image Height Max = 140px Landscape Screen Orientation</p>
<p>Image Width Max = 240px Portrait Screen Orientation</p>
<p>Image Height Max = 220px Portrait Screen Orientation</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/85</td>
<td>var</td>
<td><p>Bottom left corner option</p>
<p>Byte 0 = option</p>
<ul>
<li><p>0x00 = Disable</p></li>
<li><p>0x01 = show Device Serial Number</p></li>
<li><p>0x02 = show text</p></li>
<li><p>0x03..0x0F = invalid</p></li>
</ul>
<p>Byte 1 = length of the text, should be less than 16 characters.</p>
<p>Byte 2..N = text string value.</p></td>
<td>B</td>
<td>0</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum <strong>Response
Message</strong> found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
</tbody>
</table>

Table 145 - Response Data for Command 0x1830 - Display Flexible UI Pages
(Display Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 1830 = **Command 0x1830 - Display Flexible UI Pages (Display Only)** |  |  |  |  |  |
| No parameters |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

If the request started successfully, the Request Status in the message
wrapper is **All good / requested operation was successful**.

Table 146 - Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 2C 18 30 84 1A 18 30 81 01 00 82 01 00 83 02 00 05 A1 0C 83 0A 54 48 41 4E 4B 20 59 4F 55 00 |

Table 147 - Response Example

| Example (Hex)                |
|------------------------------|
| AA008104822C1830820400000000 |

#### Command 0x1840 – Card Emulation

Card emulation is initiated by receiving a 0x1840 command from the host.
The device will prepare card emulation with the parameters provided in
the command and start card emulation.

The sequence of events is as follows:

1)  The host ensures the device is not currently running another
    command, for example, that it is not running a transaction or PIN
    entry.

2)  The host composes a command request in the format below and sends it
    to the device.

3)  The device receives the command and verifies that the parameters are
    valid and the device is in a state that allows the execution of card
    emulation.

4)  If the device has a display, a prompt will be displayed asking the
    customer to tap their phone to the device.

5)  If the timeout parameter is not included or set to 0x00, then there
    is no timeout. Or, if the timeout parameter is set to a specific
    number of seconds, the device returns a command response message
    with its Operation Status Summary byte set to 0x01 (OK, Started /
    Running).

6)  The host may issue a 0x1840 command with Tag 0x81 set to 0x00 to
    cancel the execution of card emulation.

7)  After the timeout expires, host cancel or the card is read, the
    device sends a 0x1805 notification to inform the host.

<table>
<caption><p>Table 148 - Request Data for Command 0x1840 – Card
Emulation</p></caption>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 65%" />
<col style="width: 6%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th>Len</th>
<th>Value / Description</th>
<th>Req</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td>/81</td>
<td>01</td>
<td><p>Start/Cancel</p>
<ul>
<li><p>0x00 = Cancel (See the example of 0x1840 cancel</p></li>
</ul>
<blockquote>
<p>command below)</p>
</blockquote>
<ul>
<li><p>0x01 = Start</p></li>
</ul></td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>01</td>
<td><p>Timeout in seconds</p>
<ul>
<li><p>0x00 = No timeout</p></li>
<li><p>0x01 to 0xFF = 1 to 255 seconds</p></li>
</ul></td>
<td>O</td>
<td>0x00</td>
</tr>
<tr>
<td>/83</td>
<td><p>&lt;=</p>
<p>254</p></td>
<td><p>URL</p>
<p>URL to use as card data. Required when starting card emulation.
Optional and ignored if canceling emulation.</p>
<p>Example: <a
href="https://www.magtek.com/">https://www.magtek.com/</a></p></td>
<td>O/R</td>
<td></td>
</tr>
</tbody>
</table>

| Example (Hex) |
|----|
| AA 00 81 04 01 01 18 40 84 21 18 40 81 01 01 82 01 00 83 17 68 74 74 70 73 3A 2F 2F 77 77 77 2E 6D 61 67 74 65 6B 2E 63 6F 6D 2F |

Table 149 - Request Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 01 18 40 82 04 01 00 00 00 |

Table 150 - Response Example

| Example (Hex)                                |
|----------------------------------------------|
| AA 00 81 04 01 01 18 40 84 05 18 40 81 01 00 |

Table 151 - Example of 0x1840 Cancel Command