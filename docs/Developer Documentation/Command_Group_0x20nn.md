---
title: Command Group 0x20nn - Banking Functions (Touch/Display Only)
layout: home
parent: Commands
nav_order: 5
---

## Command Group 0x20nn - Banking Functions (Touch/Display Only)

---

- [Command Group 0x20nn - Banking Functions (Touch/Display Only)](#command-group-0x20nn---banking-functions-touchdisplay-only)
    - [Command 0x2001 - Request PIN with Host Supplied Account Data (Banking Functions Only)](#command-0x2001---request-pin-with-host-supplied-account-data-banking-functions-only)
    - [Command 0x2002 - Request PIN with Card Supplied Account Data (Banking Functions Only)](#command-0x2002---request-pin-with-card-supplied-account-data-banking-functions-only)

---


#### Command 0x2001 - Request PIN with Host Supplied Account Data (Banking Functions Only)

This command directs the device to prompt the cardholder to enter a PIN
when a card is not present or is not presented. The host is aware of the
account information and the device is not. To prompt the cardholder to
present a card before prompting for a PIN, use **Command 0x2002 -
Request PIN with Card Supplied Account Data (Banking Functions Only)**
instead.

When the host calls this command, the device enters **PIN Entry Mode**,
meaning it starts a “PIN Entry session.” While in PIN Entry Mode:

- The device ignores most other commands from the host, similar to the
  way it behaves while **Command 0x1001 - Start Transaction** is
  running: Only essential commands and those that are relevant to the
  current PIN entry session are allowed.

- When the device is waiting for the host to take action, it resets the
  timeout clock and shows an interstitial **PLEASE WAIT** page until one
  of the following occurs:

  - The host calls the same PIN entry command again to show another UI
    sequence or to end the PIN entry session, or

  - The host calls another allowed command (ending the PIN entry
    session), or

  - The device has shown **PLEASE WAIT** until the **Timeout** the host
    specified in the command has expired (ending the PIN entry session).

- The host can call this command again and again as needed, to invoke
  any number and any combination of available PIN Entry User Interface
  Sequences. This allows the host to determine the number of retries,
  and to exercise flexible fine-grained control over the end to end
  “sequence of sequences.”

- The host may cancel the PIN entry session by calling this command
  again with **User Interface Sequence = Cancel PIN Session**. In
  response, the device shows an interstitial page **PIN Entry Canceled**
  for 2 seconds, then returns to idle.

The usual sequence is as follows:

1)  The host invokes this command using the format in **Table 172**.

2)  If an error occurs, the device returns a command response message as
    shown in **Table 173** with Response Status, Operation Status
    Summary byte set to 0x80 (Failed to start operation), and terminates
    the command.

3)  If no error occurs, the device returns a command response message as
    shown in **Table 173** with Response Status, Operation Status
    Summary byte set to 0x01 (OK, Started / Running), and enters PIN
    Entry Mode.

4)  The device shows one of the predefined messages specified by the
    **User Interface Sequence** parameter and waits up to the specified
    **Timeout** for the cardholder to enter a PIN.

5)  If the host has specified **User Interface Sequence** = **Enter PIN
    / Enter PIN Again**, the device automatically prompts the cardholder
    to enter the PIN a second time.

6)  When the command completes (PIN entry done, cardholder or operator
    canceled, or **Wait Time** timeout), the device sends **Notification
    0x0205 - Banking Functions Operation Complete** to report
    **Touchscreen** / **PIN Entry**. If PIN entry is successful, the
    report also contains a payload as shown in **Table 315**. The EPB
    format the device uses depends on the parameters the host specified
    in the command:

    1)  If the host provided the **Account Number** data in the command,
        the device creates the EPB using the **PIN Block Format** the
        host specified in the command.

    2)  If the host did not provide the **Account Number** data in the
        command, the device creates the EPB using ISO format 1.

7)  If the host is performing a PIN Verification function (such as
    **User Interface Sequence** = **Enter PIN**), the host software uses
    the financial institution’s backend systems to compare the EPB to
    the account information on file, receives a result as to whether the
    entered PIN was correct, and reports the results to the teller and
    to the device.

    1)  If the PIN is correct, the host calls the same command again
        with parameter **User Interface Sequence = PIN Entry
        Successful** to indicate success and exit PIN Entry Mode. The
        device responds by showing an interstitial page **PIN Entry
        Successful** for 2 seconds, then returns to idle mode. The
        device sounds the EMV success tone to audibly report the result
        and call the cardholder’s attention to the display.

    2)  If the PIN is incorrect, depending on host-driven retry rules
        and the history of the session:

        1)  The host may call the same command again with parameter
            **User Interface Sequence = PIN Incorrect, Try Again** to
            show the **PIN Incorrect, Try Again** prompt. The device
            sounds the EMV failure tone to audibly report the result and
            call the cardholder’s attention to the display.

        2)  The host may call the same command again with other **User
            Interface Sequences** as desired.

        3)  The host must eventually finalize by calling the same
            command again with parameters to end the PIN entry session.
            If the host calls the command with **User Interface Sequence
            = PIN Entry Failed** to trigger final failure (as opposed to
            final success described above), the device shows an
            interstitial page **PIN Entry Failed** for 2 seconds, then
            returns to idle. The device also sounds the EMV failure tone
            to audibly report the result and call the cardholder’s
            attention to the display.

8)  If the host is performing a PIN Entry / Re-PIN function (such as
    **User Interface Sequence** = **Enter PIN / Enter PIN Again**),
    after the cardholder enters the PIN a second time:

    1)  If the PINs match:

        1)  The device sends the Encrypted PIN block to the host by
            sending **Notification 0x0205 - Banking Functions Operation
            Complete** to report **Touchscreen / PIN Entry / Success /
            Data Attached**. The host may pass this PIN block to backend
            systems for processing and storage.

        2)  The host calls the same command again with parameter **User
            Interface Sequence = PIN Entry Successful** to indicate
            success and exit PIN Entry Mode. The device responds by
            showing an interstitial page **PIN Entry Successful** for 2
            seconds, then returns to idle mode. The device also sounds
            the EMV success tone to audibly report the result and call
            the cardholder’s attention to the display.

    2)  If the PINs do not match, the device sends **Notification
        0x0205 - Banking Functions Operation Complete** to report
        **Touchscreen** / **PIN Entry / Operation Failed / PIN Verify
        Failed**. Depending on host-driven retry rules and the history
        of the session:

        1)  The host may call the same command again with parameter
            **User Interface Sequence = Enter PIN /Enter PIN Again** to
            prompt the cardholder to enter a PIN twice again.

        2)  The host must eventually finalize by calling the same
            command again with parameters to end the PIN entry session.
            If the host calls the command with **User Interface Sequence
            = PIN Entry Failed** to trigger final failure (as opposed to
            final success described above), the device shows an
            interstitial page **PIN Entry Failed** for 2 seconds, then
            returns to idle. The device also sounds the EMV failure tone
            to audibly report the result and call the cardholder’s
            attention to the display.

Table 172 - Request Data for Command 0x2001 - Request PIN with Host
Supplied Account Data (Banking Functions Only)

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
<td colspan="6">2001 = <strong>Command 0x2001 - Request PIN with Host
Supplied Account Data (Banking Functions Only)</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Timeout</p>
<p>Timeout in seconds that the device should wait for the cardholder to
enter PIN and confirm completion.</p>
<ul>
<li><p>0x00 = Reserved, Not Allowed</p></li>
<li><p>0x01 to 0xFF = 1 to 255 seconds</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>01</td>
<td><p>User Interface Sequence</p>
<ul>
<li><p>0x00 = Enter PIN (start session)</p></li>
<li><p>0x02 = PIN Incorrect, Try Again (continue session)</p></li>
<li><p>0x03 = Enter PIN / Enter PIN Again (start session)</p></li>
<li><p>0x05 = Enter PIN Again (continue session)</p></li>
<li><p>0xFD = Cancel PIN Session (end session)</p></li>
<li><p>0xFE = PIN Entry Failed (end session)</p></li>
<li><p>0xFF = PIN Entry Successful (end session)</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>02</td>
<td><p>PIN Length Limits</p>
<p>Byte 1 Maximum PIN Length (&lt;= 0x0C)</p>
<p>Byte 2 Minimum PIN Length (&gt;=0x04)</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>A1</td>
<td>var</td>
<td>Account Number Options</td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>01</td>
<td><p>Account Number Length</p>
<p>When host specifies <strong>PIN Block Format</strong> parameter =
<strong>ISO Format 1</strong> the Account Number length must be 0</p>
<p>When host specifies <strong>PIN Block Format</strong> parameter =
<strong>ISO Format 0 or 3</strong> the Account Number length must be
12</p>
<p>When host specifies <strong>PIN Block Format</strong> parameter =
<strong>ISO Format 4</strong> the Account Number length must be between
12 and 19 , if this length is not an even number, the device ignores the
rightmost nibble, which the host should generally set to zero.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>var</td>
<td><p>Account Number</p>
<p>If the host does provide an account number, it must provide it in
Compressed Numeric (CN) format as defined by <em><strong>EMV 4.3 Book
3</strong></em>, section <em><strong>Data Element Format
Conventions</strong></em></p></td>
<td>CN</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>85</td>
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
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 173 - Response Data for Command 0x2001 - Request PIN with Host
Supplied Account Data (Banking Functions Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 2001 = **Command 0x2001 - Request PIN with Host Supplied Account Data (Banking Functions Only)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

If the request started successfully, the Response Status in the message
wrapper is **OK, Started/Running**.

Table 174 - Request Example for Command 0x2001 - Request PIN with Host
Supplied Account Data (Banking Functions Only)

| Example (Hex) |
|----|
| AA 00 81 04 01 09 20 01 84 1C 20 01 81 01 3C 82 01 00 83 02 08 04 85 01 00 A1 0B 81 01 0C 82 06 12 34 56 78 90 12 |

Table 175 - Response Example Command 0x2001 - Request PIN with Host
Supplied Account Data (Banking Functions Only)

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 09 20 01 82 04 01 00 00 00 |

#### Command 0x2002 - Request PIN with Card Supplied Account Data (Banking Functions Only)

This command directs the device to prompt the cardholder to present
their card by swiping, dipping or tapping, and to enter a PIN. To prompt
the cardholder for a PIN without presenting a card when the host knows
the account number already, use **Command 0x2001 - Request PIN with Host
Supplied Account Data (Banking Functions Only)** instead.

When the host calls this command, the device enters **PIN Entry Mode**,
meaning it starts a “PIN Entry session.” While in PIN Entry Mode:

- The device ignores most other commands from the host, similar to the
  way it behaves while **Command 0x1001 - Start Transaction** is
  running: Only essential commands and those that are relevant to the
  current PIN Entry session are allowed.

- When the device is waiting for the host to take action, it resets the
  timeout clock and shows an interstitial **PLEASE WAIT** page until one
  of the following occurs:

  - The host calls the same PIN entry command again to show another UI
    sequence or to end the PIN entry session, or

  - The host calls another allowed command (ending the PIN entry
    session), or

  - The device has shown **PLEASE WAIT** until the **Timeout** the host
    specified in the command has expired (ending the PIN entry session).

- The host can call this command again and again as needed, to invoke
  any number and any combination of available PIN Entry User Interface
  Sequences. This allows the host to determine number of retries, and to
  exercise flexible fine-grained control over the end to end “sequence
  of sequences.”

- The host may cancel the PIN entry session by calling this command
  again with **User Interface Sequence = Cancel PIN Session**. In
  response, the device shows an interstitial page **PIN Entry Canceled**
  for 2 seconds, then returns to idle.

The usual sequence is as follows:

1)  The host invokes this command using the format in **Table 176**.

2)  If an error occurs, the device returns a command response message as
    shown in **Table 177** with Response Status, Operation Status
    Summary byte set to 0x80 (Failed to start operation), and terminates
    the command.

3)  If no error occurs, the device returns a command response message as
    shown in **Table 177** with Response Status, Operation Status
    Summary byte set to 0x01 (OK, Started / Running), and enters PIN
    Entry Mode.

4)  The device shows a prompt requesting the cardholder present one of
    the payment technologies specified in the **Reader Options**
    parameter, and waits up to the specified **Timeout** for the
    cardholder to respond.

5)  After the cardholder presents a card, the device sends
    **Notification 0x0201 - Banking Functions Information Update** to
    report the payment technology being used / Card Event / Detected.

6)  If the cardholder swiped a magnetic stripe card, the device reads
    Track 2 data.

7)  If cardholder inserts an ICC or taps a PICC, the device reads
    records from the card and attempts to retrieve tags 57 (Track 2
    Equivalent Data) and 5A (Primary Account number). It then powers off
    the card without performing the first Generate Application
    Cryptogram, so the card does not increment its transaction counters.

8)  If an error occurs, the device terminates the command and PIN entry
    session and sends **Notification 0x0205 - Banking Functions
    Operation Complete** to report Touchscreen / PIN Entry / Operation
    Failed / Account Data Capture Failed.

9)  The device shows one of the predefined messages specified by the
    **User Interface Sequence** parameter, and waits up to the specified
    **Timeout** for the cardholder to enter a PIN.

10) If the host has specified **User Interface Sequence** = **Enter PIN
    / Enter PIN Again**, the device automatically prompts the cardholder
    to enter the PIN a second time.

11) When the command completes (PIN entry done, cardholder or operator
    canceled, or **Wait Time** timeout), the device sends a
    **Notification 0x0205 - Banking Functions Operation Complete** to
    report **Touchscreen** **PIN Entry**. If PIN entry is successful,
    the report also contains a payload as shown in **Table 316**. The
    device creates the EPB using the **PIN Block Format** the host
    specified in the command.

12) If the host is performing a PIN Verification function (such as
    **User Interface Sequence** = **Enter PIN**), the host software uses
    the financial institution’s backend systems to compare the EPB to
    the account information on file, receives a result as to whether the
    entered PIN was correct, and reports the results to the teller and
    to the device.

    1)  If the PIN is correct, the host calls the same command again
        with parameter **User Interface Sequence = PIN Entry
        Successful** to indicate success and exit PIN Entry Mode. The
        device responds by showing an interstitial page **PIN Entry
        Successful** for 2 seconds, then returns to idle mode. The
        device sounds the EMV success tone to audibly report the result
        and call the cardholder’s attention to the display.

    2)  If the PIN is incorrect, depending on host-driven retry rules
        and the history of the session:

        1)  The host may call the same command again with parameter
            **User Interface Sequence = PIN Incorrect, Try Again** to
            show the **PIN Incorrect, Try Again** prompt. The device
            sounds the EMV failure tone to audibly report the result and
            call the cardholder’s attention to the display.

        2)  The host may call the same command again with other **User
            Interface Sequences** as desired.

        3)  The host must eventually finalize by calling the same
            command again with parameters to end the PIN entry session.
            If the host calls the command with **User Interface Sequence
            = PIN Entry Failed** to trigger final failure (as opposed to
            final success described above), the device shows an
            interstitial page **PIN Entry Failed** for 2 seconds, then
            returns to idle. The device also sounds the EMV failure tone
            to audibly report the result and call the cardholder’s
            attention to the display.

13) If the host is performing a PIN Entry / Re-PIN function (such as
    **User Interface Sequence** = **Enter PIN / Enter PIN Again**),
    after the cardholder enters the PIN a second time:

    1)  If the PINs match:

        1)  The device sends the Encrypted PIN block to the host by
            sending **Notification 0x0205 - Banking Functions Operation
            Complete** to report **Touchscreen / PIN Entry / Success /
            Data Attached**. The host may pass this PIN block to backend
            systems for processing and storage.

        2)  The host calls the same command again with parameter **User
            Interface Sequence = PIN Entry Successful** to indicate
            success and exit PIN Entry Mode. The device responds by
            showing an interstitial page **PIN Entry Successful** for 2
            seconds, then returns to idle mode. The device also sounds
            the EMV success tone to audibly report the result and call
            the cardholder’s attention to the display.

    2)  If the PINs do not match, the device sends **Notification
        0x0205 - Banking Functions Operation Complete** to report
        **Touchscreen** / **PIN Entry / Operation Failed / PIN Verify
        Failed**. Depending on host-driven retry rules and the history
        of the session:

        1)  The host may call the same command again with parameter
            **User Interface Sequence = Enter PIN /Enter PIN Again** to
            prompt the cardholder to enter a PIN twice again.

        2)  The host must eventually finalize by calling the same
            command again with parameters to end the PIN entry session.
            If the host calls the command with **User Interface Sequence
            = PIN Entry Failed** to trigger final failure (as opposed to
            final success described above), the device shows an
            interstitial page **PIN Entry Failed** for 2 seconds, then
            returns to idle. The device also sounds the EMV failure tone
            to audibly report the result and call the cardholder’s
            attention to the display.

Table 176 - Request Data for Command 0x2002 - Request PIN with Card
Supplied Account Data (Banking Functions Only)

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
<td colspan="6">2002 = <strong>Command 0x2002 - Request PIN with Card
Supplied Account Data (Banking Functions Only)</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Timeout</p>
<p>Timeout in seconds that the device should wait for the cardholder to
present card, enter PIN and confirm completion.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>A3</td>
<td>09</td>
<td><p>Reader Options</p>
<p>The parameters inside this TLV data object allow the host to enable
and disable the various payment method interfaces</p></td>
<td>TC</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>01</td>
<td><p>Magnetic Stripe Reader Mode</p>
<ul>
<li><p>0x00 = Disabled</p></li>
<li><p>0x01 = Enabled</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>01</td>
<td><p>Contact Reader Mode</p>
<ul>
<li><p>0x00 = Disabled</p></li>
<li><p>0x01 = Enabled</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>01</td>
<td><p>Contactless Reader Mode</p>
<ul>
<li><p>0x00 = Disabled</p></li>
<li><p>0x01 = Enabled</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>A4</td>
<td>0A</td>
<td>PIN Entry Options</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>01</td>
<td><p>User Interface Sequence</p>
<ul>
<li><p>0x00 = Reserved</p></li>
<li><p>0x01 = Present Card / Enter PIN (start session)</p></li>
<li><p>0x02 = PIN Incorrect, Try Again (continue session)</p></li>
<li><p>0x03 = Enter PIN / Enter PIN Again (continue session)</p></li>
<li><p>0x04 = Present Card / Enter PIN / Enter PIN Again (start
session)</p></li>
<li><p>0xFD = Cancel PIN Session (end session)</p></li>
<li><p>0xFE = PIN Entry Failed (end session)</p></li>
<li><p>0xFF = PIN Entry Successful (end session)</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>02</td>
<td><p>PIN Length Limits (Only when PIN is requested)</p>
<p>Byte 1 Maximum PIN Length (&lt;= 0x0C)</p>
<p>Byte 2 Minimum PIN Length (&gt;=0x04)</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/85</td>
<td>01</td>
<td><p>PIN Block Format (Only when PIN is requested)</p>
<ul>
<li><p>0x00 = ISO Format 0</p></li>
<li><p>0x01 = Reserved / Invalid</p></li>
<li><p>0x03 = ISO Format 3</p></li>
<li><p>0x04 = ISO Format 4.</p></li>
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

Table 177 - Response Data for Command 0x2002 - Request PIN with Card
Supplied Account Data (Banking Functions Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| 2002 = **Command 0x2002 - Request PIN with Card Supplied Account Data (Banking Functions Only)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

If the request started successfully, the Request Status in the message
wrapper is **OK / Operation Started**.

Table 178 - Request Example Command 0x2002 - Request PIN with Card
Supplied Account Data (Banking Functions Only)

| Example (Hex) |
|----|
| AA 00 81 04 01 0C 20 02 84 1C 20 02 81 01 3C A3 09 81 01 01 82 01 01 83 01 01 A4 0A 82 01 01 83 02 08 04 85 01 00 |

Table 179 - Response Example Command 0x2002 - Request PIN with Card
Supplied Account Data (Banking Functions Only)

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 0C 20 02 82 04 01 00 00 00 |