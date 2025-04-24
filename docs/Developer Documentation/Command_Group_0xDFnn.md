---
title: Command Group 0xDFnn - Diagnostics and Utilities
layout: home
parent: Commands
nav_order: 9
---

## Command Group 0xDFnn - Diagnostics and Utilities

---

- [Command Group 0xDFnn - Diagnostics and Utilities](#command-group-0xdfnn---diagnostics-and-utilities)
    - [Command 0xDF01 - Echo](#command-0xdf01---echo)
    - [Command 0xDF02 - Convert Binary Tag Data to Text (MAGTEK INTERNAL ONLY FOR NOW)](#command-0xdf02---convert-binary-tag-data-to-text-magtek-internal-only-for-now)
  - [Command Group 0xEnnn - Security](#command-group-0xennn---security)
    - [Command 0xE001 - Get Challenge](#command-0xe001---get-challenge)
    - [Command 0xEEEE - Send Secured Command to Device](#command-0xeeee---send-secured-command-to-device)
    - [Command 0xEF01 - Load Key Using TR-31](#command-0xef01---load-key-using-tr-31)
    - [Command 0xEF02 – Generate CSR keys (WLAN Only)](#command-0xef02-–-generate-csr-keys-wlan-only)
    - [Command 0xEF03 – Generate CSR (WLAN Only)](#command-0xef03-–-generate-csr-wlan-only)
    - [Command 0xEF04 – Load LTPK Protection Key (MAGTEK INTERNAL ONLY FOR NOW)](#command-0xef04-–-load-ltpk-protection-key-magtek-internal-only-for-now)
    - [Command 0xEF05 – Load Encrypted LTPK and Version (MAGTEK INTERNAL ONLY FOR NOW)](#command-0xef05-–-load-encrypted-ltpk-and-version-magtek-internal-only-for-now)
    - [Command 0xEF06 – Change Device Lock State](#command-0xef06-–-change-device-lock-state)
    - [Command 0xEF07 – Change Device Lock Passcode](#command-0xef07-–-change-device-lock-passcode)
    - [Command 0xEF08 – Reset Device Lock Passcode (MAGTEK INTERNAL ONLY FOR NOW)](#command-0xef08-–-reset-device-lock-passcode-magtek-internal-only-for-now)
    - [Command 0xEF11 - Get Key Info](#command-0xef11---get-key-info)
  - [Command Group 0xFnnn - Manufacturing](#command-group-0xfnnn---manufacturing)
    - [Command 0xF012 - Force Tamper (MAGTEK INTERNAL ONLY)](#command-0xf012---force-tamper-magtek-internal-only)
    - [Command 0xF014 - Read Log (MAGTEK INTERNAL ONLY)](#command-0xf014---read-log-magtek-internal-only)
    - [Command 0xF015 - Read Log & Clear Tamper (MAGTEK INTERNAL ONLY)](#command-0xf015---read-log-&-clear-tamper-magtek-internal-only)
    - [Command 0xF016 - Activate Device Security (MAGTEK INTERNAL ONLY)](#command-0xf016---activate-device-security-magtek-internal-only)
    - [Command 0xF017 - Establish Ephemeral KBPK](#command-0xf017---establish-ephemeral-kbpk)

---


#### Command 0xDF01 - Echo

The host uses this command to prompt the device for a response that
contains the same payload it sent.

The sequence of events is as follows:

1)  The host constructs the command request for **Command 0xDF01 -
    Echo** in the format below, populating any of the available
    parameters with any data. The total length of data to be echoed
    across all parameters must not exceed 128 bytes.

2)  The host sends the command request to the device.

3)  The device sends a command response in the format below to the host,
    echoing back the exact parameters the host sent in the command
    request.

Table 227 - Request Data for Command 0xDF01 - Echo

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |
| DF01 = **Command 0xDF01 - Echo** |  |  |  |  |  |
| 81 | var | Data to be echoed | B | O |  |
| 82 | var | Data to be echoed | B | O |  |
| End of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |

Table 228 - Response Data for Command 0xDF01 - Echo

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| DF01 = **Command 0xDF01 - Echo** |  |  |  |  |  |
| 81 | var | Data being echoed | B | O |  |
| 82 | var | Data being echoed | B | O |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 229 - Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA 00 81 04 01 01 DF 01 84 07 DF 01 81 03 01 02 03 |

Table 230 - Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA 00 81 04 82 01 DF 01 82 04 00 00 00 00 84 07 DF 01 81 03 01 02 03 |

#### Command 0xDF02 - Convert Binary Tag Data to Text (MAGTEK INTERNAL ONLY FOR NOW)

Reserved for future use per Dave.

### Command Group 0xEnnn - Security

#### Command 0xE001 - Get Challenge

The host uses this command to request challenge data from the device,
which the host can then use to perform a specific sensitive operation /
modify a specific type of device setting. Information about how the host
should pass the required challenge data to the device is included in the
documentation for all commands that use this security mechanism.

The sequence of events is as follows:

1)  The host already wants to perform a secured operation that requires
    a challenge \[for example **Command 0xEEEE - Send Secured Command to
    Device**\].

2)  The host constructs the command request for **Command 0xE001 - Get
    Challenge** in the format below.

3)  The host sends the command request to the device.

4)  The device generates a random number for the challenge, stores it
    locally, and sends a response in the format below to the host.

5)  The device starts a 5 minute countdown timer during which the
    challenge is valid. If the host takes no action within 5 minutes,
    the timer expires, the device erases the challenge data, and the
    device must retrieve a fresh challenge to perform the operation it
    wants to perform. This binding of the command to a specific time
    period allows the device to detect and reject commands that have
    been captured/intercepted at one point in time and replayed later.

Table 231 - Request Data for Command 0xE001 - Get Challenge

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |
| E001 = **Command 0xE001 - Get Challenge** |  |  |  |  |  |
| 81 | 02 | Request ID to be protected | B | R |  |
| End of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |

Table 232 - Response Data for Command 0xE001 - Get ChallengeGet
Challenge

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
<td colspan="6">E001 = <strong>Command 0xE001 - Get
Challenge</strong></td>
</tr>
<tr>
<td>81</td>
<td>02</td>
<td>Request ID to be protected</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>04</td>
<td>Device Serial Number</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>08</td>
<td><p>Challenge Token</p>
<p>A challenge token includes 8 byte random numbers and must be used
within 5 minutes of being issued. Only one token can be active at a
time. Attempts to use a token for requests other than the one specified
will cause the token to be revoked/erased</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Response Message</strong> found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
</tbody>
</table>

Table 233 - Request Example

| Example (Hex)                                   |
|-------------------------------------------------|
| AA 00 81 04 01 13 E0 01 84 06 E0 01 81 02 F0 12 |

Table 234 - Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 13 E0 01 82 04 00 00 00 00 84 16 A2 14 81 02 E0 01 82 04 B5 03 3D A0 83 08 3B 4F A0 62 69 BB 73 38 |

#### Command 0xEEEE - Send Secured Command to Device

The host uses this command to transmit another command securely. This
“secure wrapper” mechanism provides the device a means to ensure the
wrapped command originated from an authentic, authorized host. In
addition, its implementation includes an operation that starts a
countdown timer, which ensures the command is current and is not an
unauthorized replay of a previously intercepted / stored command. This
command can use multiple authentication methods, including MAC or ECDSA
Signature. The method and parameters to use are specific to the command
being wrapped, and are specified in the documentation for that command.

The sequence of events is as follows:

1)  The host determines what command it wants to call from section **6
    Commands**, determines the command must be secured, and uses the
    Request Data table for that command to compose **Message Payload**.

2)  The host uses **Command 0xE001 - Get Challenge** to retrieve a
    **Challenge Token** and unlock the device for receiving the desired
    command for a limited period of time. When the time expires, the
    device will no longer accept the Challenge Token and the host will
    have to retrieve another one.

3)  The host creates an instance of **Command 0xEEEE - Send Secured
    Command to Device** in the format below, and includes the Message
    Payload and Challenge Token inside it. In the **Request Message**,
    it fills in **Command ID** as the command number of the wrapped
    Message Payload, instead of 0xEEEE. Some parameters are
    command-specific; see the documentation for the command that is
    being wrapped to determine what values to use.

4)  The host sends the resulting composite command request to the
    device.

5)  The device validates the serial number and challenge token, then
    examines the parameters to determine which authentication method is
    being used, and authenticates the command accordingly.

6)  If the device determines the command request is authentic, it will
    start executing the secure command defined by the Message Payload.

7)  The device sends a response to the host reporting success or
    failure. In both cases, the response uses the format that
    corresponds to the command invoked by the Message Payload. See the
    documentation for that command to determine the format of the
    response.

Table 235 - Request Data for Command 0xEEEE - Send Secured Command to
Device

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 60%" />
<col style="width: 6%" />
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
<td colspan="6">EEEE = <strong>Command 0xEEEE - Send Secured Command to
Device</strong></td>
</tr>
<tr>
<td>A1</td>
<td>var</td>
<td><p>Security Parameters</p>
<p>This parameter describes how the Signature parameter in this data
object is calculated, and is a <strong>Security Parameters Type</strong>
TLV data object. To determine which values to use in that TLV data
object, see the documentation for the command being wrapped.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>04</td>
<td>Serial Number</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>08</td>
<td><p>Challenge Token</p>
<p>The token the device returned when the host called <strong>Command
0xE001 - Get Challenge</strong>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td>Message Payload</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>9E</td>
<td>var</td>
<td>MAC or Signature</td>
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

Table 236 - Request Example Using MAC

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
<td><p>This example wraps <strong>Command 0xD811 - Start Send File to
Device (Secured)</strong>.</p>
<p>AA 00 81 04 01 04 D8 11 84 81 8F EE EE A1 19 81 05 03 03 06 02 08 84
00 85 00 A8 0A 81 02 11 02 82 00 86 00 88 00 A9 00 82 04 FF FF FF F0 83
08 C9 65 45 F2 97 69 85 B1 84 4E D8 11 81 04 00 00 03 00 A2 2B 81 04 00
00 02 99 82 01 04 83 20 87 A4 B3 54 61 C5 CB D3 1D DC BA 9D 65 25 5A D4
6A 22 FA 51 5E FD 65 87 AF AC A8 8C 4F AF 80 9B A3 14 38 31 30 38 33 30
33 30 33 30 33 30 33 30 33 33 33 30 33 30 87 01 01 9E 10 7D E4 27 C8 A0
70 72 08 19 0A 1E 0A 3F 48 BB F1</p></td>
</tr>
</tbody>
</table>

Table 237 - Request Example Using ECDSA

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
<td><p>This example wraps <strong>Command 0xF015 - Read Log &amp; Clear
Tamper (MAGTEK INTERNAL ONLY)</strong>:</p>
<p>AA 00 // Marker</p>
<p>81 04 01 0F F0 15 // Message Information</p>
<p>84 81 C8 // Request Payload</p>
<p>EE EE // 0xEEEE, Secure Wrapper</p>
<p>A1 24 // P4-A1, Security Parameters</p>
<p>81 04 02 01 04 05 // 02=Cmd Auth-sign, 01=ECDSA, 04=SHA-256,
05=P-521</p>
<p>84 00 // Data (for IV, nonce, as needed)</p>
<p>85 00 // Extra data item (reserved for future use)</p>
<p>A8 16 // Key Info</p>
<p>81 02 00 00 // Key Slot ID</p>
<p>82 07 45 43 43 53 49 47 4E // Key Label, “ECCSIGN”</p>
<p>86 05 45 43 44 53 41 // KSN or derive info, ECDSA</p>
<p>88 00 // Added Info</p>
<p>A9 00 // 2nd Key Info (reserved for future use)</p>
<p>82 04 B5 03 3D A0 // P4-P2, Device Serial Number</p>
<p>83 08 5B 6B 45 4B 00 5B CE 31 // P4-P3, Challenge Token</p>
<p>84 02 F0 15 // P4-P4, Payload Command 0xF015</p>
<p>9E 81 89 // P4-P30, Signature for Secure Wrapper</p>
<p>30 81 86</p>
<p>02 41 // Sig-&gt;R</p>
<p>52 5B 04 9A C7 CC 56 DE 5A EA 89 62 47 BB B8 0D</p>
<p>93 80 CE C8 AD 6E 16 F7 6E DA 08 42 0B 9C 69 77</p>
<p>61 B0 99 FC 05 7D AE AF 75 79 9C 7B B3 81 72 5C</p>
<p>4E 5B 92 DC F3 B6 85 5E B3 A2 71 0D 1D 93 B5 0D</p>
<p>0C</p>
<p>02 41 // Sig-&gt;S</p>
<p>46 47 0A EF 6F D5 97 ED 4F 41 E8 3C FD 20 A1 CE</p>
<p>7D E5 CA D3 E8 22 3B ED BC 2A 8A A0 BF 73 72 81</p>
<p>35 4F CB 52 B6 A9 07 6F 36 7F 5D 35 D5 29 3D 5D</p>
<p>78 17 0E B2 D6 AA A5 0D B3 4D B9 04 2C 03 6A AC</p>
<p>A5</p></td>
</tr>
</tbody>
</table>

***Note: For additional support, please contact MagTek Support.***

#### Command 0xEF01 - Load Key Using TR-31

The host uses this command to load a key into one of several available
slots in the device’s secure memory.

| **ID** | **Label** | **Description**                   | **Load TK** |
|--------|-----------|-----------------------------------|-------------|
| 1000   | TMPTK     | Temporary KBPK                    | agree       |
| 1001   | MTK       | Master Transport                  | TMPTK       |
| 1002   | DEVTK     | Device Master                     | MTK         |
| 1003   | FINTK     | Financial Master                  | MTK         |
| 1021   | PRODTK    | Production - MagTek Internal Only | DEVTK       |
| 1022   | MFGTK     | MagTek Only Internal/External     | DEVTK       |
| 1081   | MKIFTK    | MagTek KIF Financial Keys         | FINTK       |
| 1101   | FREQMK    | Factory Request MAC               | PRODTK      |
| 1102   | MREQMK    | Mfg Device Request MAC            | MFGTK       |
| 1111   | MFRQMK    | Mfg Financial Request MAC         | MKIFTK      |
| 20xx   | DKPTM0-1F | MagTek DUKPT Initial Key          | MKIFTK      |

Table 238 - Device Key ID / Slot

To inject a specific key in the above table, the corresponding Load TK
shall be injected previously

As shown in the table, MTK injection requires that a TMPTK has been
created. See **Command 0xF017 - Establish Ephemeral KBPK**.

After MTK has been injected successfully, the sequence of injecting
other keys is as follows:

1)  The host uses **Command 0xE001 - Get Challenge** to establish a
    secure session with the device.

2)  The host constructs a TR-31 (X9.143) key block for the key it is
    going to load. (Note that the Load Key must be injected previously.)

3)  The host constructs the command request for **Command 0xEF01 - Load
    Key Using TR-31** in the format below.

4)  The host sends the command request to the device.

5)  The device sends a response in the format below to the host.

Table 239 - Request Data for Command 0xEF01 - Load Key Using TR-31

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
<th><br />
Tag</th>
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
<td colspan="6">EF01 = <strong>Command 0xEF01 - Load Key Using
TR-31</strong></td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td><p>Key Block</p>
<p>This is a populated, secured <strong>TR-31 Key Block
Type</strong>.</p></td>
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

Table 240 - Response Data for Command 0xEF01 - Load Key Using TR-31

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| EF01 = **Command 0xEF01 - Load Key Using TR-31** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 241 - Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1A EF 01 84 82 01 36 EF 01 84 82 01 30 44 30 33 30 34 42 31 54 58 30 30 4E 30 36 30 30 49 4B 31 38 46 46 46 46 39 38 37 36 35 34 33 32 31 30 33 30 30 30 30 30 32 31 35 38 4D 47 54 4B 31 30 30 31 54 31 31 30 34 32 30 30 37 31 32 30 34 31 30 38 31 32 31 30 34 30 30 33 46 33 31 30 37 42 35 30 41 46 44 32 33 32 31 30 43 39 33 36 31 39 44 44 41 41 32 31 33 36 43 37 33 33 31 30 32 30 32 30 31 32 30 34 54 31 37 31 36 33 30 5A 4B 50 30 45 30 31 39 33 36 46 41 33 32 45 4B 43 30 41 30 30 34 35 30 30 54 53 31 34 32 30 32 30 30 39 30 32 54 31 35 35 38 30 32 5A 50 42 30 34 35 37 32 31 37 46 33 34 37 31 34 43 32 42 38 38 46 33 39 35 35 32 32 32 46 46 35 39 41 41 30 35 37 44 39 39 41 46 38 32 41 37 35 37 32 46 39 33 38 46 38 33 38 42 43 36 35 45 45 35 34 46 39 34 37 46 35 39 41 30 36 43 44 34 35 35 31 39 32 32 37 41 32 35 35 43 37 44 35 44 37 43 38 36 37 34 35 30 33 46 41 43 36 46 41 37 31 33 32 43 38 46 41 39 39 36 42 34 45 42 36 41 41 31 31 34 46 45 |

Table 242 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 1A EF 01 82 04 00 00 00 00 |

***Note: For additional support, please contact MagTek Support.***

#### Command 0xEF02 – Generate CSR keys (WLAN Only)

The host uses this command to generate a key pair to be used for a
certificate signing request (CSR). The key pair generated will be 256
bit elliptic-curve (EC) keys. The key pair generated will be saved to
non-volatile memory in the device and will overwrite any existing CSR
key pair. The key pair will persist in non-volatile memory associated
with a CSR until it is either overwritten or until a leaf certificate is
loaded into the device with **Command 0xD811 - Start Send File to Device
(Secured)** that contains a public key that matches the key pair at
which point the key pair will be associated with that certificate
instead of a CSR.

The sequence of events is as follows:

1)  The host constructs the command request in the format below and
    sends it to the device.

2)  The device sends a response in the format below to the host to
    indicate that key pair generation has been started.

3)  Once the device finishes generating the key pair, it will send
    **Notification 0x1001 - Device Information Update** with the
    category set to key management and the reason set to CSR keys
    generated to indicate that the key pair generation process has
    completed. The device typically takes around a second or two to
    generate a 256 bit EC key pair. If this command is extended in the
    future to support 2048 bit RSA keys, then it will take an average of
    30 seconds and sometimes much longer to generate the RSA keys. That
    is why a notification is used to indicate that the key pair has been
    generated instead of a command response that indicates that it is
    complete.

4)  The host will typically send **Command 0xEF03 – Generate CSR (WLAN
    Only)** as the next step. See this command for more detail and more
    potential steps.

Table 243 - Request Data for Command 0xEF02 – Generate CSR keys (WLAN
Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |
| EF02 = **Command 0xEF02 – Generate CSR keys (WLAN Only)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |

Table 244 - Response Data for Command 0xEF02 – Generate CSR keys (WLAN
Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| EF02 = **Command 0xEF02 – Generate CSR keys (WLAN Only)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 245 - Request Example

| Example (Hex)                  |
|--------------------------------|
| AA00 81 04 0155EF02 84 02 EF02 |

Table 246 - Response Example

| Example (Hex)                                 |
|-----------------------------------------------|
| AA00 81 04 8205EF02 82 04 01000000 84 02 EF02 |

#### Command 0xEF03 – Generate CSR (WLAN Only)

The host uses this command to generate a certificate signing request
(CSR) in PEM format. The CSR generated will be saved to volatile memory
in the device and will overwrite any existing CSR. The CSR will persist
in volatile memory until it is overwritten, fetched with **Command
0xD821 - Start Get File from Device** or the device is power cycled or
reset.

The sequence of events is as follows:

1)  The host will use **Command 0xEF02 – Generate CSR keys (WLAN Only)**
    if it wants generate a CSR using a new CSR key pair.

2)  The host constructs the command request in the format below and
    sends it to the device.

3)  The device sends a response in the format below to the host to
    indicate that CSR generation has completed.

4)  The host fetches the CSR with **Command 0xD821 - Start Get File from
    Device.**

5)  The CSR is used to create a certificate.

6)  The host loads the certificate into the device with **Command
    0xD811 - Start Send File to Device (Secured)**.

Table 247 - Request Data for Command 0xEF03 – Generate CSR (WLAN Only)

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
<td colspan="6">EF03 = <strong>Command 0xEF03 – Generate CSR (WLAN
Only)</strong></td>
</tr>
<tr>
<td>81</td>
<td>1</td>
<td><p>Key Identifier</p>
<p>The key identifier to use to generate the CSR. The key pair
associated with the identifier must already be present in the device for
the command to succeed.</p>
<p>0 = CSR keys</p>
<p>1 = Apollo server cert keys</p>
<p>2 = Customer server cert keys</p>
<p>3 = Commercial server cert keys</p>
<p>4 = Apollo client cert keys</p></td>
<td>B</td>
<td>O</td>
<td>0</td>
</tr>
<tr>
<td>82</td>
<td>var</td>
<td><p>Subject</p>
<p>Including this optional parameter will override the default subject.
This parameter should contain a null terminated string. This string
should contain a list of attributes separated by commas. If an
attribute’s value contains a comma, the comma should be replaced with
“\\,” Each attribute value should be prefixed with its attribute name
followed by “=”. The following is a list of valid attribute names.</p>
<p>"CN"</p>
<p>"commonName"</p>
<p>"C"</p>
<p>"countryName”</p>
<p>"O"</p>
<p>"organizationName"</p>
<p>“L”</p>
<p>“locality”</p>
<p>"R"</p>
<p>“OU”</p>
<p>"organizationalUnitName"</p>
<p>“ST”</p>
<p>"stateOrProvinceName"</p>
<p>"emailAddress"</p>
<p>"serialNumber"</p>
<p>“postalAddress”</p>
<p>"postalCode"</p>
<p>“dnQualifier”</p>
<p>"title"</p>
<p>“surname”</p>
<p>"SN"</p>
<p>“givenName”</p>
<p>"GN"</p>
<p>“initials”</p>
<p>"pseudonym"</p>
<p>"generationQualifier"</p>
<p>“domainComponent”</p>
<p>"DC"</p>
<p>“O=MagTek Inc,CN= test1.com” is an example with two
attributes.</p></td>
<td>B</td>
<td>O</td>
<td>“serialNumber=XXXXXXX,CN=df-xxxxxxx” where XXXXXXX is
<strong>Property 2.2.1.1.1.1 Serial Number</strong> and so is xxxxxxx
but in lower case</td>
</tr>
<tr>
<td>83</td>
<td>var</td>
<td><p>Subject Alternative Names</p>
<p>Including this optional parameter will override the default subject
alternative names. This parameter should contain a null terminated
string. Only DNS names and IP addresses are supported and only a maximum
of two each. DNS names must be prefixed with “DNS=” and IP addresses
must be prefixed with “IPA=”. All Subject Alternative Names</p>
<p>Must be separated with a comma and not spaces. Subject Alternative
Names may not be ordered in the CSR the same as they are ordered
here.</p>
<p>"DNS=test1.com,DNS=test2.,IPA=1.10.16.255,IPA=2.10.16.254" is an
example.</p></td>
<td>B</td>
<td>O</td>
<td>“DNS=df-xxxxxxx,IPA=192.168.0.1” where xxxxxxx is <strong>Property
2.2.1.1.1.1 Serial Number</strong> but in lower case</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 248 - Response Data for Command 0xEF03 – Generate CSR (WLAN Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| EF03 = **Command 0xEF03 – Generate CSR (WLAN Only)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 249 - Request Example

| Example (Hex)                  |
|--------------------------------|
| AA00 81 04 0155EF03 84 02 EF03 |

Table 250 - Response Example

| Example (Hex)                                 |
|-----------------------------------------------|
| AA00 81 04 8255EF03 82 04 00000000 84 02 EF03 |

#### Command 0xEF04 – Load LTPK Protection Key (MAGTEK INTERNAL ONLY FOR NOW)

The sequence of events is as follows:

1)  The hose uses **Command 0xE001 - Get Challenge** to establish a
    secure session with the device.

2)  The host determines which file type it will send to the device (See
    section **6.7.1** About files) and either opens an existing file in
    its file system for reading or begins constructing it.

3)  The host constructs **Command 0xD811 - Start Send File to Device
    (Secured)** per **Table 202**.

4)  The host constructs **Command 0xEEEE - Send Secured Command to
    Device** using the previously constructed command as the payload,
    and send that command to the device as a Request Message to start
    the process of uploading a file.

    1)  Use **Command 0xEF04 – Load LTPK Protection Key (MAGTEK INTERNAL
        ONLY FOR NOW)**

The host uses this command to load the 256-bit AES LTPK protection key.
The key is encrypted and

MAC’d with the DKEK and DKMK respectively before saving it through KPM.
This key can be loaded

at the factory or the customer’s secure site before deployment.

The sequence of events is as follows:

1)  The host composes a command request in the format below, and sends
    it to the device.

2)  The device reads the Action, if Action == 0, the device will check
    and return the key status. If Action == 1, the device will verify
    the CRC-checksum and then save the key through KPM.

3)  If the key status read, key verify or key save fails, then a
    response of failure will be sent to the host.

Table 251 - Request Data for Command 0xEF04 – Load LTPK Protection Key
(MAGTEK INTERNAL ONLY FOR NOW)

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
<td colspan="6">EF04 = <strong>Command 0xEF04 – Load LTPK Protection Key
(MAGTEK INTERNAL ONLY FOR NOW)</strong></td>
</tr>
<tr>
<td>81</td>
<td>1</td>
<td><p>Action</p>
<p>0 = Check key status.</p>
<p>1 = Load key.</p>
<p>If Action==0, ignore the TLVs below.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>20</td>
<td><p>AES-256 Key</p>
<p>32 bytes of key.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>2</td>
<td><p>CRC-16-CCITT Checksum</p>
<p>Polynomial X16 + X12 + X5 + 1, initial value=0xFFFF.</p>
<p>2-byte checksum of the 32-byte key.</p></td>
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

Table 252 - Response Data for Command 0xEF04 – Load LTPK Protection Key
(MAGTEK INTERNAL ONLY FOR NOW)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| EF04 = **Command 0xEF04 – Load LTPK Protection Key (MAGTEK INTERNAL ONLY FOR NOW)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 253 - Request Example

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
<td><p>AA 00 81 04 01 06 EF 04 84 2B EF 04 81 01 01 82 20 22 F0 66 59 0B
DA 04 F7 B9 99 B6 B4 B4 BC 2E</p>
<p>0D 95 92 C2 7A B1 55 98 2A 31 D3 06 CC E6 6B CF 85 83 02 84
99</p></td>
</tr>
</tbody>
</table>

Table 254 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 06 EF 04 82 04 00 00 00 00 |

#### Command 0xEF05 – Load Encrypted LTPK and Version (MAGTEK INTERNAL ONLY FOR NOW)

The host uses this command to load the encrypted LTPK and Version. The
data will first be decrypted

using the LTPK protection key, then encrypted and MAC’d with the DKEK
and DKMK respectively

before saving it through KPM.

The sequence of events is as follows:

1\) The host composes a command request in the format below, and sends
it to the device.

2\) The device reads the Action, if Action == 0, the device will check
and return the key status.

If Action == 1, the device will verify the CRC, decrypt and then save
the key through KPM.

3\) If the key status read, key verify or key save fails, then a
response of failure will be sent to the host.

Table 255 - Request Data for Command 0xEF05 – Load Encrypted LTPK and
Version (MAGTEK INTERNAL ONLY FOR NOW)

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
<td colspan="6">EF05 = <strong>Command 0xEF05 – Load Encrypted LTPK and
Version (MAGTEK INTERNAL ONLY FOR NOW)Load Encrypted LTPK and
Version</strong></td>
</tr>
<tr>
<td>81</td>
<td>1</td>
<td><p>Action</p>
<p>0 = Check key status.</p>
<p>1 = Load key.</p>
<p>If Action==0, ignore the TLVs below.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>4</td>
<td><p>Key Version</p>
<p>00 00 00 01=0x00000001.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>2</td>
<td><p>Raw Key Length (before the padding &amp; encryption)</p>
<p>01 23=0x0123 bytes.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>85</td>
<td>var</td>
<td><p>Encrypted Key Length</p>
<p>The length of the encrypted LTPK shall be 16-byte aligned.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>86</td>
<td>2</td>
<td><p>CRC-16-CCITT Checksum</p>
<p>Polynomial X16 + X12 + X5 + 1, initial value=0xFFFF.</p>
<p>2-byte checksum of the encrypted key.</p></td>
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

Table 256 - Response Data for Command 0xEF05 – Load Encrypted LTPK and
Version (MAGTEK INTERNAL ONLY FOR NOW)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| EF05 = **Command 0xEF05 – Load Encrypted LTPK and Version (MAGTEK INTERNAL ONLY FOR NOW)** |  |  |  |  |  |
| 81 | 4 | LTPK Key Version | B | R |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 257 - Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 07 EF 05 84 81 96 EF 05 81 01 01 82 04 00 00 00 02 83 02 00 79 85 81 80 A1 9A 2D F7 B9 99 57 9B 89 5E 58 1B AD 26 52 77 EB B8 AC 6F 6A BE A8 21 D6 38 0D 54 0B 24 65 F4 EC D4 1D 73 E1 5A BE 9F 13 6B 85 DD 96 60 FD 33 6C 23 15 14 0B 53 AC FF EF 1C 1B 22 BD 56 D7 86 6D 82 D4 E0 E6 0B F5 07 E6 5D A5 EF C2 89 A1 33 28 E1 C7 D2 00 7C 8C B8 C5 D5 F9 5B D7 4F ED BB 40 9F 10 1D 43 08 97 5B 4A 1F D4 50 EB 2B 73 82 C9 C9 6C 4C 9C BC 05 F0 74 11 3E 7E 9C 60 02 DC 86 02 69 DF |

Table 258 - Response Example

| Example (Hex)                                                           |
|-------------------------------------------------------------------------|
| AA 00 81 04 82 07 EF 05 82 04 00 00 00 00 84 08 EF 05 81 04 00 00 00 02 |

#### Command 0xEF06 – Change Device Lock State 

The host can use this command to change the device’s lock state. To get
the device’s lock state or to set it using MagTek security see
**Property 1.2.5.2.1.1 Device Lock State**. The value of the device lock
state will revert to the value of **Property 1.2.5.2.1.2 Device Lock
State After Reset** after a reset or a power cycle. See **Device Lock
Feature** for more information.

Table 259 - Request Data for Command 0xEF06 – Change Device Lock State

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
<td colspan="6">EF06 = <strong>Command 0xEF06 – Change Device Lock
State</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Device Lock State</p>
<ul>
<li><p>0x00 = Unlocked</p></li>
<li><p>0x01 = Locked</p></li>
</ul></td>
<td>B</td>
<td>M</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>01</td>
<td><p>Passcode Format</p>
<ul>
<li><p>0x00 = Clear</p></li>
<li><p>0x01 = Fixed SHA-256</p></li>
<li><p>0x02 = Variable SHA-256</p></li>
</ul></td>
<td>B</td>
<td>M</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>04-63</td>
<td><p>Passcode</p>
<p>The value of the passcode depends on the value of the passcode format
parameter.</p>
<p>If the passcode format is set to clear, then the value of the
passcode is the passcode in the clear and can have a length of 4-63
bytes.</p>
<p>If the passcode format is set to fixed SHA-256, then the value of the
passcode is the 32 byte SHA-256 hash value of the passcode.</p>
<p>If the passcode format is set to variable SHA-256, then the value of
the passcode is the 32 byte SHA-256 hash value of a 8 byte random
challenge token followed by the 4-63 byte passcode. The challenge token
must have been retrieved from the device within the last 5 minutes using
Command 0xE001 - Get Challenge.</p></td>
<td>B</td>
<td>M</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 260 - Response Data for Command 0xEF06 – Change Device Lock State

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| EF06 = **Command 0xEF06 – Change Device Lock State** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 261 - Request Example

| Example (Hex)                                              |
|------------------------------------------------------------|
| AA00 81 04 0155EF06 84 0E EF06 810100 820100 8304 34333231 |

Table 262 - Response Example

| Example (Hex)                           |
|-----------------------------------------|
| AA00 81048255EF06 820400000000 8402EF06 |

#### Command 0xEF07 – Change Device Lock Passcode

The host can use this command to change the device’s lock passcode. The
value of the device lock passcode is stored in non-volatile memory so
changes made to it will persist after the device is reset or power
cycled. To change the device lock passcode using MagTek security or to
see its default value see **Property 1.2.5.2.1.3 Device Lock Passcode**.
See **Device Lock Feature** for more information.

Table 263 - Request Data for Command 0xEF07 – Change Device Lock
Passcode

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
<td colspan="6">EF07 = Command <strong>0xEF07 – Change Device Lock
Passcode</strong></td>
</tr>
<tr>
<td>81</td>
<td>4-63</td>
<td><p>Current Passcode</p>
<p>The current passcode in the clear. This must match the value of the
current passcode or the command will fail.</p></td>
<td>B</td>
<td>M</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>04-63</td>
<td><p>New Passcode</p>
<p>The new passcode in the clear. It can only contain any printable
ASCII character or the command will fail.</p></td>
<td>B</td>
<td>M</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 264 - Response Data for Command 0xEF07 – Change Device Lock
Passcode

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| EF07 = Command **0xEF07 – Change Device Lock Passcode** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 265 - Request Example

| Example (Hex)                                            |
|----------------------------------------------------------|
| AA00 81 04 0155EF07 84 0E EF07 810434333231 820434333231 |

Table 266 - Response Example

| Example (Hex)                           |
|-----------------------------------------|
| AA00 81048255EF07 820400000000 8402EF07 |

#### Command 0xEF08 – Reset Device Lock Passcode (MAGTEK INTERNAL ONLY FOR NOW)

The host can use this command to reset the device’s lock passcode to its
default value. The value of the device lock passcode is stored in
non-volatile memory so changes made to it will persist after the device
is reset or power cycled. To change the device lock passcode using
MagTek security or to see its default value see **Property 1.2.5.2.1.3
Device Lock Passcode**. See **Device Lock Feature** for more
information.

Table 267 - Request Data for Command 0xEF08 – Reset Device Lock Passcode
(MAGTEK INTERNAL ONLY FOR NOW)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |
| EF08 = Command **0xEF08 – Reset Device Lock Passcode (MAGTEK INTERNAL ONLY FOR NOW)** |  |  |  |  |  |
| 81 | 4 | Device Serial Number. See **Property 2.2.1.1.1.1 Serial Number** for the format. | B | M |  |
| End of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |

Table 268 - Response Data for Command 0xEF08 – Reset Device Lock
Passcode (MAGTEK INTERNAL ONLY FOR NOW)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| EF08 = Command **0xEF08 – Reset Device Lock Passcode (MAGTEK INTERNAL ONLY FOR NOW)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 269 - Request Example

| Example (Hex)                                 |
|-----------------------------------------------|
| AA00 81 04 0155EF08 84 08 EF08 81 04 BE001BB0 |

Table 270 - Response Example

| Example (Hex)                                 |
|-----------------------------------------------|
| AA00 81 04 8255EF08 82 04 00000000 84 02 EF08 |

#### Command 0xEF11 - Get Key Info

The host uses this command to retrieve information about a key slot,
including details about the key stored in that slot. It can be used for
several purposes, including:

- Determine if a key exists / has been loaded

- Get key derivation data to derive a DUKPT key

- Get transport key information to retrieve the appropriate transport
  key

The sequence of events is as follows:

1)  The host constructs the command request in the format below.

2)  The host sends the command request to the device.

3)  The device sends a response in the format below to the host.

Table 271 - Request Data for Command 0xEF11 - Get Key Info

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
<td colspan="6">EF11 = <strong>Command 0xEF11 - Get Key
Info</strong></td>
</tr>
<tr>
<td>81</td>
<td>02</td>
<td><p>Key Slot ID</p>
<p>See <strong>Table 56 - Key Slot ID</strong> on page <a
href="#_Ref49929758"><strong>85</strong></a>.</p></td>
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

Table 272 - Response Data for Command 0xEF11 - Get Key Info

<table style="width:100%;">
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
<td colspan="6">EF11 = <strong>Command 0xEF11 - Get Key
Info</strong></td>
</tr>
<tr>
<td>81</td>
<td>04</td>
<td>Key Slot Information</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Key Slot Status</p>
<ul>
<li><p>0x00 = Empty</p></li>
<li><p>0x01 = Loaded (Key not assigned purpose)</p></li>
<li><p>0x02 = Loaded &amp; Active</p></li>
<li><p>0x03 = Exhausted (End of DUKPT key sequence</p></li>
<li><p>0x04 = Expired (Reserved, certificate status)</p></li>
<li><p>0xFF = Not supported in this device</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Key Slot Type</p>
<p>First byte of the Key Slot ID in the host’s request message.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(2)</td>
<td><p>Transport Key Slot ID</p>
<p>This specifies the key used to secure and load the key that the host
is retrieving information about. See <strong>Table 56 - Key Slot
ID</strong> on page <a
href="#_Ref49929758"><strong>85</strong></a>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>06</td>
<td>Loaded Key Information</td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Key Environment</p>
<ul>
<li><p>‘T’ = Test</p></li>
<li><p>‘P’ = Production</p></li>
</ul></td>
<td>A</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(4)</td>
<td><p>TR-31 Attributes</p>
<p>See <strong>Table 52 - TR-31 Key Type Table -
Usage/Algorithm/Mode.</strong></p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Encoding of Algorithm &amp; Length</p>
<ul>
<li><p>0x01 = DEA</p></li>
<li><p>0x02 = 2TDEA</p></li>
<li><p>0x03 = 3TDEA</p></li>
<li><p>0x04 = AES128</p></li>
<li><p>0x05 = AES192</p></li>
<li><p>0x06 = AES256</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>var</td>
<td><p>Key Check Value</p>
<ul>
<li><p>For AES-CMAC, 5 bytes.</p></li>
<li><p>For TDES-CMAC or TDES-CBCMAC, 3 bytes</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td><p>Key Derivation Information</p>
<p>This contains the derivation block, key serial number (KSN), or key
label, as appropriate for the key type.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>A6</td>
<td>var</td>
<td><p>Restrictions</p>
<p>Reserved. Do not include.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>81</td>
<td>02</td>
<td><p>DUKPT Restrictions</p>
<p>These restrictions come from the TR-31 block.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>89</td>
<td>var</td>
<td><p>Timestamp</p>
<p>This comes from the TR-31 block or from device’s real-time
clock.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
</tbody>
</table>

Table 273 - Request Example

| Example (Hex)                                   |
|-------------------------------------------------|
| AA 00 81 04 01 21 EF 11 84 06 EF 11 81 02 20 07 |

Table 274 - Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 21 EF 11 82 04 00 00 00 00 84 34 A2 32 81 04 02 20 10 81 82 06 54 42 31 54 58 03 84 0A FF FF 98 76 54 32 10 30 00 00 A6 04 81 02 00 3F 89 10 32 30 32 30 30 39 30 32 54 31 35 35 38 30 32 5A |

***Note: For additional support, please contact MagTek Support.***

### Command Group 0xFnnn - Manufacturing

#### Command 0xF012 - Force Tamper (MAGTEK INTERNAL ONLY)

This command is used to force the device’s tamper protection mechanisms
to register a tamper event.

The sequence of events is as follows:

1)  The device’s tamper protection features must first be enabled. See
    **Command 0xF016 - Activate Device Security (MAGTEK INTERNAL
    ONLY)**.

2)  The host uses **Command 0xE001 - Get Challenge** to establish a
    secure session with the device.

3)  The host constructs the command request for **Command 0xF012 - Force
    Tamper (MAGTEK INTERNAL ONLY)** in the format below.

4)  The host constructs **Command 0xEEEE - Send Secured Command to
    Device** using the previously constructed command request as the
    payload, and sends that command request to the device as a **Request
    Message**.

    1)  Because this command is secured using a signature, read
        **Property 2.1.2.2.2.6 Key Type** to determine which fixed key
        to use to generate the signature.

    2)  Build the **Security Parameters Type** portion of the wrapper
        with:

        1)  **Security Operation Type** populated with the following
            values:

            1)  Operation Type = **Command Authorization Using
                Signature**

            2)  Operation Algorithm = **ECDSA (indeterministic)**

            3)  Operation Hash = **SHA-256**

            4)  Operation Curve = **P521**.

5)  The device validates the request:

    1)  If the request is valid and properly authenticated, it forces
        the tamper event and automatically resets. The device does not
        send a response to the host in this case.

    2)  If the request fails validation, the device sends a response in
        the format below to report the failure to the host.

Table 275 - Request Data for Command 0xF012 - Force Tamper (MAGTEK
INTERNAL ONLY)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |
| F012 = **Command 0xF012 - Force Tamper (MAGTEK INTERNAL ONLY)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |

Table 276 - Response Data for Command 0xF012 - Force Tamper (MAGTEK
INTERNAL ONLY)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| F012 = **Command 0xF012 - Force Tamper (MAGTEK INTERNAL ONLY)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 277 - Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 14 F0 12 84 81 CA EE EE A1 24 81 04 02 01 04 05 84 00 85 00 A8 16 81 02 00 00 82 07 45 43 43 53 49 47 4E 86 05 45 43 44 53 41 88 00 A9 00 82 04 B5 03 3D A0 83 08 3B 4F A0 62 69 BB 73 38 84 02 F0 12 9E 81 8B 30 81 88 02 42 01 F7 60 F4 89 8A 81 6D E2 4E 6C 5D D1 66 41 A4 34 54 E7 32 93 48 3D E5 7D 2C C6 16 F6 E8 CC 98 C6 5D 26 A6 20 60 B7 D1 EF 78 DB 85 32 82 72 67 23 8B 04 00 93 98 14 4E 2C 47 1A 3B F6 B6 B8 93 D2 EA 02 42 01 84 B4 A4 5C 9F D8 EC AD E2 29 F8 AD 8B DD AF 4C 4E 85 F9 B9 E2 AC 7E 7D 3B AE DB 83 47 AD 1B 95 91 32 C4 AA 0F 31 B0 8C 1B 2D AD C0 76 4C A1 AB D2 9F 3B 25 6A 87 36 AC 40 67 B9 33 5B 20 36 50 30 |

Table 278 - Response Example

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
<td><p>Response only occurs in the failure case.</p>
<p>AA 00 81 04 82 0F F0 12 82 04 81 00 00 00</p></td>
</tr>
</tbody>
</table>

#### Command 0xF014 - Read Log (MAGTEK INTERNAL ONLY)

The host uses this command to read the system event log from the device.

The sequence of events is as follows:

1)  The host uses **Command 0xE001 - Get Challenge** to establish a
    secure session with the device.

2)  The host constructs the command request for **Tamper in** the format
    below.

3)  The host constructs **Command 0xEEEE - Send Secured Command to
    Device** using the previously constructed command request as the
    payload, and sends that command request to the device as a **Request
    Message**.

    1)  Because this command is secured using a signature, read
        **Property 2.1.2.2.2.6 Key Type** to determine which fixed key
        to use to generate the signature.

    2)  Build the **Security Parameters Type** portion of the wrapper
        with:

        1)  **Security Operation Type** populated with the following
            values:

            1)  Operation Type = **Command Authorization Using
                Signature**

            2)  Operation Algorithm = **ECDSA (indeterministic)**

            3)  Operation Hash = **SHA-256**

            4)  Operation Curve = **P521**.

4)  The device validates the request, then read the system event log.

5)  The device sends a response in the format below to report the result
    to the host.

Table 279 - Request Data for Command 0xF014 - Read Log (MAGTEK INTERNAL
ONLY)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |
| F014 = **Command 0xF014 - Read Log (MAGTEK INTERNAL ONLY)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |

Table 280 - Response Data for Command 0xF014 - Read Log (MAGTEK INTERNAL
ONLY)

<table>
<colgroup>
<col style="width: 8%" />
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
<td colspan="6">Beginning of any wrappers, at minimum including
<strong>Response Message</strong> found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
<tr>
<td colspan="6">F014 = <strong>Command 0xF014 - Read Log (MAGTEK
INTERNAL ONLY)</strong></td>
</tr>
<tr>
<td>83</td>
<td>var</td>
<td>System Event Log</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(2)</td>
<td><p>Number of Events</p>
<p>This specifies the number of events in the log that follows.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(2)</td>
<td><p>Length of Each Event</p>
<p>This specifies the fixed length used for each event reported in the
log that follows.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(var)</td>
<td><p>Event Log</p>
<p>This text blob contains the specified <strong>Number of
Events</strong>, up to 10 events total, of constant length equal to
<strong>Length of Each Event</strong>. If there are any empty events,
they are filled with 0x00 (Null). Each non-null contains:</p>
<ul>
<li><p>20 bytes of human readable date-time indicating when the device
wrote the entry into the log. If the device is powered on when a tamper
occurs, it records the event, reboots, then writes the event to the log.
If the device is powered off when a tamper occurs, it records the event,
then write the event to the log the next time it powers on.</p></li>
<li><p>A block of human readable text describing the event</p></li>
<li><p>Padding with 0x20 (Space)</p></li>
</ul></td>
<td>AN</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Response Message</strong> found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
</tbody>
</table>

Each Event Log text block can contain one of several human readable
strings describing the event. The following is an example of two log
entries indicating Forced Tamper:

2023-12-08 02:57 @ID:0, sensor_status=0x1, active_sensors=0xaa0374

2023-12-08 02:57 @ID:0, tamper_time_in_seconds=1702004228

In the first log entry above:

- The value after **sensor_status=** is a 32-bit hex encoded number with
  a bit set to 1 for each tamper sensor that registered an actual tamper
  event.

- The value after **active_sensors =** is a 32-bit hex encoded number
  with a bit set to 1 for each tamper sensor that was active when the
  device logged the tamper event.

- The bit values for both numbers are listed in **Table 286 below**.

In the second log entry above, the value after
**tamper_time_in_seconds=** is the value of the device’s real time clock
at the time the tamper occurred, expressed as a decimal a number of
seconds in Unix epoch time format. This is expected to differ from the
human readable date-time stamp that indicates when the device wrote the
event to the log, because the device’s always-active security subsystem
registers a basic but indelible version of the tamper event immediately,
whereas the logging subsystem may need to wait for the device to
automatically reboot after tamper, or wait to be powered up after a
powered-off tamper, before system resources are available to write the
event to the log.

Table 281 - Sensor Bit Values In Tamper Log

| Bit | Tamper Sensor |
|----|----|
| 0 | Any Tamper: This is only used for **sensor_status=**. It is reserved and set to 0 for **active_sensors=**. Note that if **Command 0xF012 - Force Tamper (MAGTEK INTERNAL ONLY)** is used, only this bit will be set. |
| 1 | Reserved and set to 0 |
| 2 | Time Overflow |
| 3 | Reserved and set to 0 |
| 4 | Voltage |
| 5 | Clock |
| 6 | Temperature |
| 7 | Reserved and set to 0 |
| 8 | Flash Security |
| 9 | Test Mode |
| 10..16 | Reserved and set to 0 |
| 17 | Tamper Pin Input 1 |
| 18 | Reserved and set to 0 |
| 19 | Tamper Pin Input 3 |
| 20 | Reserved and set to 0 |
| 21 | Tamper Pin Input 5 |
| 22 | Reserved and set to 0 |
| 23 | Tamper Pin Input 7 |
| 24..31 | Reserved and set to 0 |

Table 282 - Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 32 F0 14 84 81 CA EE EE A1 24 81 04 02 01 04 05 84 00 85 00 A8 16 81 02 00 00 82 07 45 43 43 53 49 47 4E 86 05 45 43 44 53 41 88 00 A9 00 82 04 BE 00 06 80 83 08 88 D3 F5 28 2B CF 07 ED 84 02 F0 14 9E 81 8B 30 81 88 02 42 00 99 F6 96 30 7D 27 CB 59 B8 A9 F1 C1 7A C5 A8 D1 62 C2 8A 5A 9A F2 82 25 DD AF A7 C6 62 D3 57 70 DB 52 E6 EC 77 7F 20 2D CE DB F0 5E 84 77 B4 7B EA 8F 42 FB 6B 49 41 6F 78 33 08 DB 31 94 D0 2A 18 02 42 00 93 06 2A CF 5C 29 4E D5 FE 7B 1D 00 3E 68 C9 DA 4D 94 16 DA F9 86 CC BB 18 54 2E C4 44 28 B8 1C 62 CF 9E 47 46 20 7C 20 EF DF 71 05 49 B7 F9 F7 A0 0B 4D 7C 6C 77 EB 93 AF D3 40 ED 3A 28 10 A9 B4 |

Table 283 - Response Example

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
<td><p>AA 00 81 04 82 32 F0 14 82 04 00 00 00 00 83 82 03 4C 00 02 00
54</p>
<p>32 30 32 33 2D 31 32 2D 30 38 20 30 32 3A 35 37 20 20 20 20 40 49 44
3A 30 2C 20 73 65 6E 73 6F 72 5F 73 74 61 74 75 73 3D 30 78 31 2C 20 61
63 74 69 76 65 5F 73 65 6E 73 6F 72 73 3D 30 78 61 61 30 33 37 34 20 20
20 20 20 20 20 20 20 20 20 20 20 20 20</p>
<p>32 30 32 33 2D 31 32 2D 30 38 20 30 32 3A 35 37 20 20 20 20 40 49 44
3A 30 2C 20 74 61 6D 70 65 72 5F 74 69 6D 65 5F 69 6E 5F 73 65 63 6F 6E
64 73 3D 31 37 30 32 30 30 34 32 32 38 20 20 20 20 20 20 20 20 20 20 20
20 20 20 20 20 20 20 20 20 20 20 20 20</p></td>
</tr>
</tbody>
</table>

#### Command 0xF015 - Read Log & Clear Tamper (MAGTEK INTERNAL ONLY)

The host uses this command to clear the device’s tamper status and read
the system event log from the device.

The sequence of events is as follows:

1)  The host uses **Command 0xE001 - Get Challenge** to establish a
    secure session with the device.

2)  The host constructs the command request for **Command 0xF015 - Read
    Log & Clear Tamper** in the format below.

3)  The host constructs **Command 0xEEEE - Send Secured Command to
    Device** using the previously constructed command request as the
    payload, and sends that command request to the device as a **Request
    Message**.

    1)  Because this command is secured using a signature, read
        **Property 2.1.2.2.2.6 Key Type** to determine which fixed key
        to use to generate the signature.

    2)  Build the **Security Parameters Type** portion of the wrapper
        with:

        1)  **Security Operation Type** populated with the following
            values:

            1)  Operation Type = **Command Authorization Using
                Signature**

            2)  Operation Algorithm = **ECDSA (indeterministic)**

            3)  Operation Hash = **SHA-256**

            4)  Operation Curve = **P521**.

4)  The device validates the request, then does the following:

    1)  Read and clear the system event log.

    2)  Clear the device’s tamper status.

    3)  Check the device’s tamper status.

5)  The device sends a response in the format below to report the result
    to the host. If the request started successfully, the Request Status
    in the message wrapper is **OK, Started / Running, All good /
    requested operation was successful**. If the device is still in a
    tampered state after it clears the tamper, the response reports a
    failure.

Table 284 - Request Data for Command 0xF015 - Read Log & Clear Tamper
(MAGTEK INTERNAL ONLY)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |
| F015 = **Command 0xF015 - Read Log & Clear Tamper (MAGTEK INTERNAL ONLY)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |

Table 285 - Response Data for Command 0xF015 - Read Log & Clear Tamper
(MAGTEK INTERNAL ONLY)

<table>
<colgroup>
<col style="width: 8%" />
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
<td colspan="6">Beginning of any wrappers, at minimum including
<strong>Response Message</strong> found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
<tr>
<td colspan="6">F015 = <strong>Command 0xF015 - Read Log &amp; Clear
Tamper (MAGTEK INTERNAL ONLY)</strong></td>
</tr>
<tr>
<td>83</td>
<td>var</td>
<td>System Event Log</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(2)</td>
<td><p>Number of Events</p>
<p>This specifies the number of events in the log that follows.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(2)</td>
<td><p>Length of Each Event</p>
<p>This specifies the fixed length used for each event reported in the
log that follows.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(var)</td>
<td><p>Event Log</p>
<p>This text blob contains the specified <strong>Number of
Events</strong>, up to 10 events total, of constant length equal to
<strong>Length of Each Event</strong>. If there are any empty events,
they are filled with 0x00 (Null). Each non-null contains:</p>
<ul>
<li><p>20 bytes of human readable date-time indicating when the device
wrote the entry into the log. If the device is powered on when a tamper
occurs, it records the event, reboots, then writes the event to the log.
If the device is powered off when a tamper occurs, it records the event,
then write the event to the log the next time it powers on.</p></li>
<li><p>A block of human readable text describing the event</p></li>
<li><p>Padding with 0x20 (Space)</p></li>
</ul></td>
<td>AN</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Response Message</strong> found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
</tbody>
</table>

Each **Event Log** text block can contain one of several human readable
strings describing the event. The following is an example of two log
entries indicating **Tamper Pin 3 Input** tampered:

2021-02-05 00:16 @ID:0, sensor_status=0x80001, active_sensors =0xaa0374

2021-02-05 00:16 @ID:0, tamper_time_in_seconds=1612484188

In the first log entry above:

- The value after **sensor_status=** is a 32-bit hex encoded number with
  a bit set to 1 for each tamper sensor that registered an actual tamper
  event.

- The value after **active_sensors =** is a 32 bit hex encoded number
  with a bit set to 1 for each tamper sensor that was active when the
  device logged the tamper event.

- The bit values for both numbers are listed in **Table 286 below**.

In the second log entry above, the value after
**tamper_time_in_seconds=** is the value of the device’s real time clock
at the time the tamper occurred, expressed as a decimal a number of
seconds in Unix epoch time format. This is expected to differ from the
human readable date-time stamp that indicates when the device wrote the
event to the log, because the device’s always-active security subsystem
registers a basic but indelible version of the tamper event immediately,
whereas the logging subsystem may need to wait for the device to
automatically reboot after tamper, or wait to be powered up after a
powered-off tamper, before system resources are available to write the
event to the log.

Table 286 - Sensor Bit Values in Tamper Log

| Bit | Tamper Sensor |
|----|----|
| 0 | Any Tamper: This is only used for **sensor_status=**. It is reserved and set to 0 for **active_sensors=**. Note that if **Command 0xF012 - Force Tamper (MAGTEK INTERNAL ONLY)** is used, only this bit will be set. |
| 1 | Reserved and set to 0 |
| 2 | Time Overflow |
| 3 | Reserved and set to 0 |
| 4 | Voltage |
| 5 | Clock |
| 6 | Temperature |
| 7 | Reserved and set to 0 |
| 8 | Flash Security |
| 9 | Test Mode |
| 10..16 | Reserved and set to 0 |
| 17 | Tamper Pin Input 1 |
| 18 | Reserved and set to 0 |
| 19 | Tamper Pin Input 3 |
| 20 | Reserved and set to 0 |
| 21 | Tamper Pin Input 5 |
| 22 | Reserved and set to 0 |
| 23 | Tamper Pin Input 7 |
| 24..31 | Reserved and set to 0 |

Table 287 - Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0F F0 15 84 81 C8 EE EE A1 24 81 04 02 01 06 05 84 00 85 00 A8 16 81 02 00 00 82 07 45 43 43 53 49 47 4E 86 05 45 43 44 53 41 88 00 A9 00 82 04 B5 03 3D A0 83 08 5B 6B 45 4B 00 5B CE 31 84 02 F0 15 9E 81 89 30 81 86 02 41 52 5B 04 9A C7 CC 56 DE 5A EA 89 62 47 BB B8 0D 93 80 CE C8 AD 6E 16 F7 6E DA 08 42 0B 9C 69 77 61 B0 99 FC 05 7D AE AF 75 79 9C 7B B3 81 72 5C 4E 5B 92 DC F3 B6 85 5E B3 A2 71 0D 1D 93 B5 0D 0C 02 41 46 47 0A EF 6F D5 97 ED 4F 41 E8 3C FD 20 A1 CE 7D E5 CA D3 E8 22 3B ED BC 2A 8A A0 BF 73 72 81 35 4F CB 52 B6 A9 07 6F 36 7F 5D 35 D5 29 3D 5D 78 17 0E B2 D6 AA A5 0D B3 4D B9 04 2C 03 6A AC A5 |

Table 288 - Response Example

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
<td><p>AA 00</p>
<p>81 04 82 0F F0 15 // Message Info</p>
<p>82 04 00 00 00 00 // Status is OK</p>
<p>83 82 03 50 // Payload, System Event LOG</p>
<p>00 02 // 2 events in the LOG</p>
<p>00 54 // 0x54 (84) bytes per event</p>
<p>32 30 32 30 2D 30 38 2D 32 36 2D 31 34 3A 30 30 // Event #1:
2020-08-26-14:00 @ID:0,</p>
<p>20 20 20 20 40 49 44 3A 30 2C 20 73 65 6E 73 6F // sensor_status=0x1,
active_sensors=0xaa0374</p>
<p>72 5F 73 74 61 74 75 73 3D 30 78 31 2C 20 61 63</p>
<p>74 69 76 65 5F 73 65 6E 73 6F 72 73 3D 30 78 61</p>
<p>61 30 33 37 34 20 20 20 20 20 20 20 20 20 20 20</p>
<p>20 20 20 20</p>
<p>32 30 32 30 2D 30 38 2D 32 36 2D 31 34 3A 30 30 // Event #2:
2020-08-26-14:00 @ID:0,</p>
<p>20 20 20 20 40 49 44 3A 30 2C 20 74 61 6D 70 65 //
tamper_time_in_seconds=1598450397</p>
<p>72 5F 74 69 6D 65 5F 69 6E 5F 73 65 63 6F 6E 64</p>
<p>73 3D 31 35 39 38 34 35 30 33 39 37 20 20 20 20</p>
<p>20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20</p>
<p>20 20 20 20</p></td>
</tr>
</tbody>
</table>

#### Command 0xF016 - Activate Device Security (MAGTEK INTERNAL ONLY)

The host uses this command to activate the security on the device. This
allows the manufacturer to perform initial operations on an unsecured
device, then enable security before shipping. This command is intended
to only be executed once during manufacturing, and can not be undone or
redone.

The sequence of events is as follows:

1)  The host uses **Command 0xE001 - Get Challenge** to establish a
    secure session with the device.

2)  The host constructs a request for **Command 0xF016 - Activate Device
    Security** as shown below.

3)  The host constructs **Command 0xEEEE - Send Secured Command to
    Device** using the previously constructed command request as the
    payload, and sends that command request to the device as a **Request
    Message**.

    1)  Because this command is secured using a signature, read
        **Property 2.1.2.2.2.6 Key Type** to determine which fixed key
        to use to generate the signature.

    2)  Build the **Security Parameters Type** portion of the wrapper
        with:

        1)  **Security Operation Type** populated with the following
            values:

            1)  Operation Type = **Command Authorization Using
                Signature**

            2)  Operation Algorithm = **ECDSA (indeterministic)**

            3)  Operation Hash = **SHA-256**

            4)  Operation Curve = **P521**.

4)  The device does the following:

    1)  Validates the secure wrapper around the command and terminates
        if the signature is invalid.

    2)  Set the specified date and time on the device’s real-time clock
        (RTC).

    3)  Store the specified PCI Hardware ID in the device’s battery
        backed secure RAM.

    4)  Store the specified Hardware Configuration Profile in the
        device’s battery backed secure RAM.

    5)  Store the specified MAC Address in the device’s battery backed
        secure RAM.

    6)  Enable the 23-hour automatic restart.

    7)  Generate the Master Key Derivation Key (MKDK) and four Derived
        Key Encrypting Keys (DKEK/DDEK/DKMK/DDMK).

    8)  Store the specified WLAN SoftAP MagTek Password in the device’s
        EEPROM AES 256 CBC encrypted using the DKEK.

    9)  Activate and lock the tamper protection mechanism.

5)  The device sends a **Response Message** to the host to indicate the
    result.

Table 289 - Request Data for Command 0xF016 - Activate Device Security
(MAGTEK INTERNAL ONLY)

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
<td colspan="6">F016 = <strong>Command 0xF016 - Activate Device Security
(MAGTEK INTERNAL ONLY)</strong></td>
</tr>
<tr>
<td>81</td>
<td>07</td>
<td><p>Current Date and Time</p>
<p>This initializes the device’s real-time clock (RTC) to the specified
date and time. The specified date and time should be Universal Time
Coordinated (UTC).</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Month</p>
<p>From 0x01 January to 0x0C December.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Day of Month</p>
<p>From 0x01 to 0x1F (31st).</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Hour</p>
<p>Hour in 24-hour format from 0x00 Midnight to 0x17 11PM</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Minute</p>
<p>Minutes after the hour from 0x00 0 minutes after the hour to 0x3B 59
minutes after the hour.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Seconds</p>
<p>Seconds after the minute from 0x00 0 seconds to 0x3B 59 seconds after
the minute.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td>Reserved. Set to 0x00.</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Year</p>
<p>Current year minus 2008</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>85</td>
<td>var</td>
<td><p>PCI Hardware ID</p>
<p>This specifies the PCI Hardware ID the device uses to uniquely
identify its model family on the touchscreen and via host
commands.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>86</td>
<td>var</td>
<td><p>Hardware Configuration Profile</p>
<p>This parameter contains a tightly encoded block of bytes that tells
the device’s firmware what hardware is installed. Note some values
inside this parameter must be prefixed with explicit lengths, but for
compactness they do not include tags. Such values do not have
parentheses in the <strong>Len</strong> column. This data is stored in
the secure processor’s battery-backed (VBAT) Register File and, like
keys, can only be erased by forcing a tamper event.</p>
<p>Example:</p>
<p>02</p>
<p>05 01 02 01 02 00</p>
<p>04 01 01 01 01</p>
<p>02 01 01</p>
<p>05 01 00 00 00 01</p>
<p>05 01 01 01 01 01</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>(1)</td>
<td><p>Hardware Configuration Profile Version</p>
<p>This identifies the version of the Hardware Configuration Profile to
provide future extensibility.</p>
<ul>
<li><p>0x01 = Initial release</p></li>
<li><p>0x02 = Added in specification revision 30</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>05</td>
<td><p>System Core Hardware</p>
<p>Length is included in the hardware configuration profile
value.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>Processor / SOC</p>
<ul>
<li><p>0x01 = K81</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>External Flash RAM</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = Parallel NOR 2MB</p></li>
<li><p>0x02 = Parallel NOR 4MB</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>External RAM</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = Parallel PSRAM 2MB</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>External non-volatile RAM/EEPROM</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = SPI 32KB</p></li>
<li><p>0x02 = SPI 64KB</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>On-board Host</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = Android Tablet</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>04</td>
<td><p>Readers</p>
<p>Length is included in the hardware configuration profile
value.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>MSR</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = 3 Track MagnePrint Head and MagnePrint ASIC</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>ICCR (Contact)</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = Contact block with analog chip</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>PCD (Contactless)</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = PN5180</p></li>
<li><p>0x02 = PN5190</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>BCR (Barcode Reader)</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = Barcode Reader (NLS-N1)</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>02</td>
<td><p>Power</p>
<p>Length is included in the hardware configuration profile
value.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>Battery</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = xxxx LiPo</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>PMIC</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = PF1550A9</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>05</td>
<td><p>Communication</p>
<p>Length is included in the hardware configuration profile
value.</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>USB</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = Internal FS available</p></li>
<li><p>0x03 = Internal FS available and Apple Authentication Coprocessor
present</p></li>
</ul>
<p>This configuration is bitwise.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>RS-232</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = Present</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>Ethernet</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = Present</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>Wireless LAN (WLAN)</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = Present</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>Bluetooth® Low Energy</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = Present</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/null</td>
<td>05</td>
<td><p>User Interface</p>
<p>Length is included in the hardware configuration profile
value.</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>Display</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = 320x240 16-bit RGB</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>Touchpad</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = 320x240 integrated with display</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>LEDs</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = Four RGB on face</p></li>
<li><p>0x02 = Four monochrome on face</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>Audio / Sound</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = Buzzer Transducer 3.6V 2.7kHz 85dB with PMIC output
voltage volume control</p></li>
<li><p>0x02 = Buzzer Transducer 3V 2kHz 80dB with GPIO high-low volume
control</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//null</td>
<td>(1)</td>
<td><p>Buttons</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = One pushbutton and one recessed switch</p></li>
<li><p>0x02 = One pushbutton and one virtual recessed switch</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>88</td>
<td>var</td>
<td><p>MAC Address</p>
<p>For devices with TCP/IP hardware, such as Ethernet or WLAN, this
specifies the device’s MAC address.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>89</td>
<td>var</td>
<td><p>WLAN SoftAP MagTek Password</p>
<p>The length can be a maximum of 63 bytes.</p>
<p>For devices with WLAN, this specifies the device’s SoftAP MagTek
Password. MagTek shall load this password and it shall be printed on the
device’s label. This passwork shall be unique per device. The device
will use this password for its SoftAP until a SoftAP Customer Password
is loaded.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>8A</td>
<td>4</td>
<td><p>WLAN Firmware Sequence Number</p>
<p>The length is 4 bytes, ms byte first</p></td>
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

Table 290 - Response Data for Command 0xF016 - Activate Device Security
(MAGTEK INTERNAL ONLY)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| F016 = **Command 0xF016 - Activate Device Security (MAGTEK INTERNAL ONLY)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

If the request started successfully, the Request Status in the message
wrapper is **OK, Started / Running, All good / requested operation was
successful**.

Table 291 - Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0F F0 16 84 81 EA EE EE A1 24 81 04 02 01 06 05 84 00 85 00 A8 16 81 02 00 00 82 07 45 43 43 53 49 47 4E 86 05 45 43 44 53 41 88 00 A9 00 82 04 B5 03 3D A0 83 08 BE A5 45 81 90 C9 28 0C 84 22 F0 16 81 07 08 1A 0E 16 28 04 0C 85 0B 44 65 76 65 6C 6F 70 6D 65 6E 74 86 08 31 32 33 34 35 36 37 38 9E 81 8B 30 81 88 02 42 00 CD C1 EC 9E D1 30 A6 19 0A 8D 27 F6 65 26 4A 97 3C 79 94 60 BA 57 4D 64 4A 47 FC 72 6B 83 1F 1F DB 05 40 E3 70 16 17 DB 5E A6 93 77 1D 40 F5 DE 0A 9E 01 7A B3 6D DA 8A 73 94 46 1A 68 99 B6 8C 9F 02 42 01 5E 40 4E 4C F9 BF 1B 10 4D BE 7C F6 F9 FE F8 77 1E D0 1A FE AA FC 8B BD 06 BB 8A E5 A5 B3 0E 2E B4 CC DE 60 48 96 2A 84 38 E0 41 45 CD A2 4B F9 36 DA 61 BE 06 A6 CA F2 2F 17 EC DA 0D 59 D0 01 EC |

Table 292 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 0F F0 16 82 04 00 00 00 00 |

#### Command 0xF017 - Establish Ephemeral KBPK

The host uses this command to complete the ***ECDHE-ECDSA Key
Exchange*** protocol, which enables the host and the device to generate
the same TEMP KBPK key to use with **Command 0xEF01 - Load Key Using
TR-31** to load the Master Transport Key (MTK).

The sequence of events is as follows:

1)  The host uses **Command 0xE001 - Get Challenge** to establish a
    secure session with the device.

2)  The host constructs **Command 0xF017 - Establish Ephemeral KBPK**
    per the request table below.

3)  The host constructs **Command 0xEEEE - Send Secured Command to
    Device** using the previously constructed command request as the
    payload, and sends that command request to the device as a **Request
    Message**.

    1)  Because this command is secured using a signature, read
        **Property 2.1.2.2.2.6 Key Type** to determine which fixed key
        to use to generate the signature.

    2)  Build the **Security Parameters Type** portion of the wrapper
        with:

        1)  **Security Operation Type** populated with the following
            values:

            1)  Operation Type = **Command Authorization Using
                Signature**

            2)  Operation Algorithm = **ECDSA (indeterministic)**

            3)  Operation Hash = **SHA-256**

            4)  Operation Curve = **P521**.

4)  The device does the following:

    1)  Validates the secure wrapper around the command, and terminates
        if the signature is invalid.

    2)  Determine if the Master Transport Key (MTK) has already been
        loaded. If it has, the device rejects the command request.

    3)  Generates a pair of keys, saves the Device Private Key for
        calculation.

    4)  Generates and saves 8 bytes of Device Random Token for
        calculation.

    5)  Calculates the TEMP KBPK based on Host Public Key and Host
        Random Token passed in with the command request, and the Device
        Private Key and Device Random Token the device generated.

5)  The device sends a **Response Message** to the host to indicate the
    result. The response message includes Device Random Token and Device
    Public Key.

6)  The host calculates a matching TEMP KBPK as defined in as defined in
    ***NIST SP800-56A***, using the Host Private Key, Host Random Token,
    Device Public Key, and Device Random Token. It can then use this key
    to perform encryption operations on secret data in the Master
    Transport Key (MTK).

7)  The device uses its copy of the matching TEMP KBPK to decrypt the
    secret information encrypted by the host using the same key. On
    successful MTK load, the device erases the TEMP KBPK. It also erases
    the TEMP KBPK if the device is power cycled or reset, and the host
    would need to restart the process with a new TEMP KBPK.

Table 293 - Request Data for Command 0xF017 - Establish Ephemeral KBPK

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
<td colspan="6">F017 = <strong>Command 0xF017 - Establish Ephemeral
KBPK</strong></td>
</tr>
<tr>
<td>A1</td>
<td>var</td>
<td><p>Security Parameters</p>
<p>This contains a <strong>Security Parameters Type</strong> TLV data
object with only the first parameter populated with:</p>
<p>01 = Key Agreement,</p>
<p>01 = ECDHE,</p>
<p>05 = Curve P521,</p>
<p>01 = SP800-56A</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>var</td>
<td><p>Host Ephemeral Public Key</p>
<p>This parameter is in ASN.1 format. The information of the cipher and
key size are included in the ASN.1 Public Key file (PKCS#8).</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>84</td>
<td>08</td>
<td><p>Host Random Token</p>
<p>This contains an 8 byte random number generated by the host.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
</tbody>
</table>

Table 294 - Response Data for Command 0xF017 - Establish Ephemeral KBPK

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 0%" />
<col style="width: 5%" />
<col style="width: 61%" />
<col style="width: 0%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th colspan="2">Len</th>
<th>Value / Description</th>
<th colspan="2">Typ</th>
<th>Req</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="8">Beginning of any wrappers, at minimum including
<strong>Response Message</strong> found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
<tr>
<td colspan="8">F017 = <strong>Command 0xF017 - Establish Ephemeral
KBPK</strong></td>
</tr>
<tr>
<td colspan="2">A1</td>
<td>var</td>
<td colspan="2"><p>Security Parameters</p>
<p>This contains a <strong>Security Parameters Type</strong> TLV data
object populated entirely with 0x00 padding to indicate that all values
are the same as the corresponding values in the Request.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="2">83</td>
<td>var</td>
<td colspan="2"><p>Device Ephemeral Public Key</p>
<p>This parameter is in ASN.1 format. The information of the cipher and
key size are included in the ASN.1 key file.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="2">84</td>
<td>08</td>
<td colspan="2"><p>Device Random Token</p>
<p>This contains an 8 byte random number generated by the
device.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td colspan="8">End of any wrappers, at minimum including
<strong>Response Message</strong> found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
</tbody>
</table>

Table 295 - Request Example

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
<td><p>AA 00</p>
<p>81 04 01 10 F0 17</p>
<p>84 82 01 8C</p>
<p>EE EE // Secure Wrapper</p>
<p>A1 24</p>
<p>81 04 02 01 04 05</p>
<p>84 00 85 00</p>
<p>A8 16</p>
<p>81 02 00 00</p>
<p>82 07 45 43 43 53 49 47 4E</p>
<p>86 05 45 43 44 53 41</p>
<p>88 00 A9 00</p>
<p>82 04 B5 03 3D A0</p>
<p>83 08 ED B0 79 E6 E3 F1 83 AE</p>
<p>84 81 C3 // payload is 0xF017 command body</p>
<p>F0 17</p>
<p>A1 14 // Security parameters</p>
<p>81 04 01 01 05 01</p>
<p>84 00</p>
<p>A8 0A</p>
<p>81 02 00 00</p>
<p>82 00</p>
<p>86 00</p>
<p>88 00</p>
<p>83 81 9E // TL of PKCS8 public key</p>
<p>30 81 9B // V of PKCS8 public key</p>
<p>30 10</p>
<p>06 07 2A 86 48 CE 3D 02 01</p>
<p>06 05 2B 81 04 00 23</p>
<p>03 81 86</p>
<p>00</p>
<p>04</p>
<p>01 64 1C DA 45 C5 56 B3 8B 31 29 8C 94 A1 E7 95</p>
<p>C9 D3 85 C0 4D F3 15 13 D9 91 43 84 58 15 CD 45</p>
<p>6B 67 F6 AC 7C 56 DF F8 0C 65 A7 CF 81 F1 13 2F</p>
<p>AA E5 22 10 78 23 C9 4F 1D CD 24 42 EC 1A 3F A4</p>
<p>75 58</p>
<p>00 97 59 96 9E 01 D0 62 47 B7 EF 5F 0B D0 8B E6</p>
<p>CA 12 F0 3C 13 43 AF 15 21 92 3D 6B FE 47 74 68</p>
<p>38 3F DD 1E 90 2B FD 0F D6 DA 7A A1 E9 A1 98 85</p>
<p>3A DA 93 6D EE 05 61 87 8B 81 BF 6A 78 2F 40 A5</p>
<p>E8 66</p>
<p>84 08 BD E3 77 88 83 0C F6 37 // TLV of 8-byte random # for
TEMP-KBPK</p>
<p>// end of 0xF017 command body</p>
<p>9E 81 8B</p>
<p>30 81 88</p>
<p>02 42</p>
<p>00 C4 13 1D C2 13 7A F6 FD F0 F1 BB BD 14 C2 4A</p>
<p>FE D7 6F BC 80 91 84 26 43 85 40 B6 5D BE 1D 9C</p>
<p>74 90 77 B6 41 62 69 52 04 72 93 C0 9C 59 2A DB</p>
<p>03 31 0F 8A 28 C0 DB 1A B7 1B 51 B3 E6 BD FF 50</p>
<p>77 CA</p>
<p>02 42</p>
<p>01 EE D8 2D 9F A3 D1 98 4E 74 C8 85 11 52 93 15</p>
<p>FF 9D 7D 5A 03 FD 84 B8 B9 09 20 8B 15 98 7A 5E</p>
<p>56 A5 61 71 9A 0A B9 D1 DA 1C 96 1D 0C EF F0 D2</p>
<p>E3 A4 22 84 60 E2 AA 8C AA 2B 8B AE 02 50 D8 B3</p>
<p>CF 84</p></td>
</tr>
</tbody>
</table>

Table 296 - Response Example

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
<td><p>AA 00</p>
<p>81 04 82 10 F0 17</p>
<p>82 04 00 00 00 00</p>
<p>84 81 B5 // Response Payload</p>
<p>F0 17</p>
<p>A1 06</p>
<p>81 01 00</p>
<p>82 01 00</p>
<p>83 81 9E // TL of PKCS8 public key</p>
<p>30 81 9B // V of PKCS8 public key</p>
<p>30 10</p>
<p>06 07 2A 86 48 CE 3D 02 01</p>
<p>06 05 2B 81 04 00 23</p>
<p>03 81 86</p>
<p>00</p>
<p>04</p>
<p>01 77 CD 91 56 96 34 2B C6 5A 6C EC 5D 74 96 41</p>
<p>B3 F9 2B 12 85 19 90 F8 73 BF FF 3C 10 44 E3 CB</p>
<p>21 4E CA F6 CE FC F8 C8 80 52 44 13 FA B1 97 A1</p>
<p>8C 44 FE 95 A2 0A F3 3D A4 3A 8F 2E 39 41 23 22</p>
<p>B1 AB</p>
<p>01 29 26 4F CC 0E 86 11 16 92 FF BC E1 BF DA FC</p>
<p>21 BA B1 5A C4 DE 7B C1 6F A9 17 F8 4B 1E B2 1F</p>
<p>5F 21 7D 54 00 15 41 C3 21 75 0D 21 DC 95 13 A7</p>
<p>2C 8C 11 77 96 38 87 51 08 7A 1F 63 EC A8 8F C4</p>
<p>AB B3</p>
<p>84 08 4C 4A EC 0B 47 E4 53 EB // TLV of 8-byte random # for
TEMP-KBPK</p></td>
</tr>
</tbody>
</table>

***Note: For additional support, please contact MagTek Support.***