---
title: Command Group 0xD8nn - File Operations
layout: home
parent: Commands
nav_order: 7
---

## Command Group 0xD8nn - File Operations

---

- [Command Group 0xD8nn - File Operations](#command-group-0xd8nn---file-operations)
    - [About Files](#about-files)
    - [Command 0xD801 - Load Firmware File](#command-0xd801---load-firmware-file)
    - [Command 0xD811 - Start Send File to Device (Secured)](#command-0xd811---start-send-file-to-device-secured)
    - [Command 0xD812 - Start Send File to Device (Unsecured)](#command-0xd812---start-send-file-to-device-unsecured)
    - [Command 0xD821 - Start Get File from Device](#command-0xd821---start-get-file-from-device)
    - [Command 0xD825 - Get File Info from Device](#command-0xd825---get-file-info-from-device)
    - [Command 0xD831 – Delete File from Device](#command-0xd831-–-delete-file-from-device)

---


#### About Files

Large blobs of data uploaded to / downloaded from the device are
referred to as “files” and share a common set of commands documented
here, and special message type **Data File Message**. Some file types
can be sent in the File Payload fields in “raw” form (e.g. certificates
and images) with metadata coming from the command request and response.
Other file types require the addition of MagTek metadata included inside
the File Payload blob; these are documented in the “File Type”
subsections of section **4 Data Types and Shared TLV Data Objects**.

Files Types that may come from the host include:

- EMV configuration

- Firmware updates

- Public Key Infrastructure (PKI) Certificates

- User interface images and prompts

- EMV kernels

- SRED BIN tables

File Types that may come from the device include:

- Read back of the above file types

- Signature Capture

- Logs

- Certificate Requests

The commands in this section share a common list of 4-byte file types,
listed in Table. File types marked as Secured = Yes must be loaded using
**Command 0xD811 - Start Send File to Device (Secured)**; file types
that are marked as Secured = No can be loaded using **Command 0xD812 -
Start Send File to Device (Unsecured)**.

­Table 196 - File Types

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th>Description</th>
<th>Secured</th>
<th>File Type</th>
<th>File Type Version</th>
<th>File Subtype</th>
<th>File Instance</th>
</tr>
</thead>
<tbody>
<tr>
<td>EMV configuration, terminal file. See file definition in section 4.8
on page <a href="#emv-terminal-configuration-file-type">55</a>.</td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x00</td>
<td>0x00</td>
<td>0x00</td>
<td>0x00</td>
</tr>
<tr>
<td>EMV configuration, processing file. See file definition in section
4.9 on page <a
href="#emv-processing-configuration-file-type">57</a>.</td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x00</td>
<td>0x00</td>
<td>0x01</td>
<td>0x00</td>
</tr>
<tr>
<td>EMV configuration, entry point file. See file definition in section
4.10 on page <a
href="#emv-entry-point-configuration-file-type">60</a>.</td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x00</td>
<td>0x00</td>
<td>0x02</td>
<td>0x00</td>
</tr>
<tr>
<td><p>EMV configuration, CA keys file. See file definition in section
0</p>
<p>on page <a
href="#jcb-entry-point-table-common-kernel-only">72</a>.</p></td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x00</td>
<td>0x00</td>
<td>0x03</td>
<td>0x00</td>
</tr>
<tr>
<td>EMV configuration, Visa DRL set. Reserved for future use.</td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x00</td>
<td>0x00</td>
<td>0x04</td>
<td>0x00</td>
</tr>
<tr>
<td>EMV configuration, American Express DRL set. See file definition in
section 4.12 on page <a
href="#emv-american-express-drl-configuration-file-type-not-supported-on-expresspay-4.x">76</a>.</td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x00</td>
<td>0x00</td>
<td>0x05</td>
<td>0x00</td>
</tr>
<tr>
<td>EMV configuration, MasterCard update conditions. Reserved for future
use.</td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x00</td>
<td>0x00</td>
<td>0x06</td>
<td>0x00</td>
</tr>
<tr>
<td>EMV configuration, American Express update conditions. Reserved for
future use.</td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x00</td>
<td>0x00</td>
<td>0x08</td>
<td>0x00</td>
</tr>
<tr>
<td>EMV configuration, Discover update conditions. Reserved for future
use.</td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x00</td>
<td>0x00</td>
<td>0x09</td>
<td>0x00</td>
</tr>
<tr>
<td>EMV configuration, CA revocation list. Reserved for future use.</td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x00</td>
<td>0x00</td>
<td>0x0A</td>
<td>0x00</td>
</tr>
<tr>
<td>EMV configuration, exception file list. Reserved for future
use.</td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x00</td>
<td>0x00</td>
<td>0x0B</td>
<td>0x00</td>
</tr>
<tr>
<td>EMV configuration, DPAS data storage. Reserved for future use.</td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x00</td>
<td>0x00</td>
<td>0x0C</td>
<td>0x00</td>
</tr>
<tr>
<td>(Touch Only) Signature capture file. See file definition in section
4.15 on page <a href="#security-parameters-type">81</a>.</td>
<td><p>Get: No</p>
<p>Set: NA</p></td>
<td>0x01</td>
<td>0x00</td>
<td>0x00</td>
<td>0x00</td>
</tr>
<tr>
<td>(Display Only) Custom Idle Page Image 1. For details, see Property
1.2.3.1.1.1 Custom Idle Page Image.</td>
<td><p>Get: NA</p>
<p>Set: No</p></td>
<td>0x02</td>
<td>0x00</td>
<td>0x00</td>
<td>0x00</td>
</tr>
<tr>
<td>(Display Only) Custom Idle Page Image 2. For details, see Property
1.2.3.1.1.1 Custom Idle Page Image.</td>
<td><p>Get: NA</p>
<p>Set: No</p></td>
<td>0x02</td>
<td>0x00</td>
<td>0x00</td>
<td>0x01</td>
</tr>
<tr>
<td>(Display Only) Custom Idle Page Image 3. For details, see Property
1.2.3.1.1.1 Custom Idle Page Image.</td>
<td><p>Get: NA</p>
<p>Set: No</p></td>
<td>0x02</td>
<td>0x00</td>
<td>0x00</td>
<td>0x02</td>
</tr>
<tr>
<td>(Display Only) Custom Idle Page Image 4. For details, see Property
1.2.3.1.1.1 Custom Idle Page Image.</td>
<td><p>Get: NA</p>
<p>Set: No</p></td>
<td>0x02</td>
<td>0x00</td>
<td>0x00</td>
<td>0x03</td>
</tr>
<tr>
<td><p>(WLAN Only) Apollo root CA certificate</p>
<p>See Certificate File Types.</p></td>
<td><p>Get: No</p>
<p>Set: Yes</p></td>
<td>0x03</td>
<td>0x00</td>
<td>0x00</td>
<td>0x00</td>
</tr>
<tr>
<td><p>(WLAN Only) Apollo intermediate CA certificate</p>
<p>See Certificate File Types.</p></td>
<td><p>Get: No</p>
<p>Set: Yes</p></td>
<td>0x03</td>
<td>0x00</td>
<td>0x01</td>
<td>0x00</td>
</tr>
<tr>
<td><p>(WLAN Only) Apollo server certificate</p>
<p>See Certificate File Types.</p></td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x03</td>
<td>0x00</td>
<td>0x02</td>
<td>0x00</td>
</tr>
<tr>
<td><p>(WLAN Only) Customer root CA certificate</p>
<p>See Certificate File Types.</p></td>
<td><p>Get: No</p>
<p>Set: Yes</p></td>
<td>0x03</td>
<td>0x00</td>
<td>0x03</td>
<td>0x00</td>
</tr>
<tr>
<td><p>(WLAN Only) Customer intermediate CA certificate</p>
<p>See Certificate File Types.</p></td>
<td><p>Get: No</p>
<p>Set: Yes</p></td>
<td>0x03</td>
<td>0x00</td>
<td>0x04</td>
<td>0x00</td>
</tr>
<tr>
<td><p>(WLAN Only) Customer server certificate</p>
<p>See Certificate File Types.</p></td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x03</td>
<td>0x00</td>
<td>0x05</td>
<td>0x00</td>
</tr>
<tr>
<td><p>(WLAN Only) Commercial root CA certificate</p>
<p>See Certificate File Types.</p></td>
<td><p>Get: No</p>
<p>Set: Yes</p></td>
<td>0x03</td>
<td>0x00</td>
<td>0x06</td>
<td>0x00</td>
</tr>
<tr>
<td><p>(WLAN Only) Commercial intermediate CA certificate</p>
<p>See Certificate File Types.</p></td>
<td><p>Get: No</p>
<p>Set: Yes</p></td>
<td>0x03</td>
<td>0x00</td>
<td>0x07</td>
<td>0x00</td>
</tr>
<tr>
<td><p>(WLAN Only) Commercial server certificate</p>
<p>See Certificate File Types.</p></td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x03</td>
<td>0x00</td>
<td>0x08</td>
<td>0x00</td>
</tr>
<tr>
<td><p>(WLAN Only) Apollo trust certificate</p>
<p>See Certificate File Types.</p></td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x03</td>
<td>0x00</td>
<td>0x09</td>
<td>0x00</td>
</tr>
<tr>
<td><p>(WLAN Only) Customer trust certificate</p>
<p>See Certificate File Types.</p></td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x03</td>
<td>0x00</td>
<td>0x0A</td>
<td>0x00</td>
</tr>
<tr>
<td><p>(WLAN Only) Apollo client certificate</p>
<p>See Certificate File Types.</p></td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x03</td>
<td>0x00</td>
<td>0x0B</td>
<td>0x00</td>
</tr>
<tr>
<td><p>(WLAN Only) Certificate signing request (CSR)</p>
<p>See Certificate Signing Request (CSR) File Types.</p></td>
<td><p>Get: No</p>
<p>Set: N/A</p></td>
<td>0x04</td>
<td>0x00</td>
<td>0x00</td>
<td>0x00</td>
</tr>
<tr>
<td>(WLAN Only) WebSocket Trust configuration file, Request file from
MagTek.</td>
<td><p>Get: N/A</p>
<p>Set: No</p></td>
<td>0x05</td>
<td>0x00</td>
<td>0x00</td>
<td>0x00</td>
</tr>
<tr>
<td>(WLAN Only) MQTT Trust configuration file, Request file from
MagTek.</td>
<td><p>Get: N/A</p>
<p>Set: No</p></td>
<td>0x05</td>
<td>0x00</td>
<td>0x01</td>
<td>0x00</td>
</tr>
<tr>
<td>UI configuration file. See file definition in section 4.29 UI
Configuration File Type.</td>
<td><p>Get: No</p>
<p>Set: No</p></td>
<td>0x06</td>
<td>0x00</td>
<td>0x00</td>
<td>0x00</td>
</tr>
</tbody>
</table>

#### Command 0xD801 - Load Firmware File

The host uses this command to send a firmware image file, signed by
MagTek, to the device as the first step in updating firmware. The host
also uses this command to send a firmware image file, signed by MagTek,
to the device as the first step in updating firmware. If the battery
charge is five percent or less, a response is returned indicating that
the command has not been executed. See **Table 199 - Response Example
for Command 0xD801**.

The sequence of events is as follows:

1)  The host is assumed to have access to a binary file containing a
    firmware image signed by MagTek, which contains a complete instance
    of **Firmware File Type (MAGTEK INTERNAL ONLY)**.

2)  The host composes a command request in the format below, using the
    binary file as the **Payload**, and sends it to the device.

3)  The device sends a response to the host in the format below to
    acknowledge it has received the request. The device will not allow
    the Load Firmware File command to execute if the battery charge is 5
    percent or lower.

4)  The device validates the request and authenticates the firmware file
    with the algorithm specified in the firmware file payload.

> If the upload was not successful, then go to the next step. If the
> upload was successful and auto-commit was disabled, then go to the
> next step. Else, the device will commit the image automatically. If it
> was successful, the device sends **Notification 0x0905 - Firmware
> Update Successful** to the host. If it was unsuccessful, the device
> sends **Notification 0x0906 - Firmware Update Failed**to the host.
> Commit Firmware Notification Detail Codes are used for auto-commit
> mode. In both cases, the device automatically resets.

Table 197 - Request Data for Command 0xD801 - Load Firmware File

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
<td colspan="6">D801 = <strong>Command 0xD801 - Load Firmware
File</strong></td>
</tr>
<tr>
<td>81</td>
<td>01</td>
<td><p>Progress Indicator</p>
<p>Reserved for future use. Populate with 0x03.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>85</td>
<td>02</td>
<td><p>Image Type</p>
<ul>
<li><p>0x0000 = Boot Loader 1 image</p></li>
<li><p>0x0001 = Main App image</p></li>
<li><p>0x0002 = WiFi Module image­</p></li>
<li><p>0x0003 = BLE Module image</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>86</td>
<td>20</td>
<td><p>Hash Checksum</p>
<p>This is a SHA-256 hash of the entire object <strong>Firmware
File</strong> <strong>Type (MAGTEK INTERNAL ONLY)</strong> being
uploaded. For backward compatibility, this TLV is required in Default
Mode, it is Optional in Auto-Commit Mode.</p></td>
<td>B</td>
<td>R/O</td>
<td></td>
</tr>
<tr>
<td>87</td>
<td>var</td>
<td><p>Payload</p>
<p>This is the binary file or <strong>Firmware File</strong>
<strong>Type (MAGTEK INTERNAL ONLY)</strong> object being loaded into
the device.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>88</td>
<td>01</td>
<td><p>Load Options</p>
<p>0x00 = Default mode</p>
<p>0x01 = Auto Commit</p></td>
<td>B</td>
<td>O</td>
<td>0x00</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 198 - Response Data for Command 0xD801 - Load Firmware File

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| D801 = **Command 0xD801 - Load Firmware File** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 01 D8 01 82 04 80 02 03 16 |

Table 199 - Response Example for Command 0xD801 Battery Charge State

If the request started successfully, the Request Status in the message
wrapper is **OK, Started / Running, All good / requested operation was
successful**.

Table 200 - Request Example

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
<td><p>AA 00 81 04 01 01 D8 01 84 83 0C 76 58 D8 01 81 01 03 85 02 00 01
86 20 DF C7 1E 09 A3 CE 8E 86 B0 F5 B6 75 BE B7 7A 0E 82 33 BF F1 8A CD
8F 38 34 B0 DB 20 D9 40 4B 28 87 83 0C 76 28</p>
<p>Plus 0C7628 bytes of firmware Payload, excluded here for
brevity.</p></td>
</tr>
</tbody>
</table>

Table 201 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 01 D8 01 82 04 00 00 00 00 |

#### Command 0xD811 - Start Send File to Device (Secured)

The host uses this command to start sending secured files to the device
for storage or processing. It is similar to **Command 0xD812 - Start
Send File to Device (Unsecured)**, but is used to send a different
subset of file types that impact device security and require some form
of authentication from the host. Refer to ­Table 196 to determine which
file type requires a secure command All files require the command to be
authorized via a secure wrapper. In some cases, files include additional
signatures within the file structure itself. This command is paired with
**Command 0xD821 - Start Get File from Device**, which the host can use
to retrieve files. However, some file types are “one way only” and can
not be retrieved using that command after the host sends them to the
device.

The sequence of events is as follows:

1)  The host uses **Command 0xE001 - Get Challenge** to establish a
    secure session with the device.

2)  The host determines which file type it will send to the device (see
    section **6.7.1 About Files**), and either opens an existing file in
    its file system for reading, or begins constructing it.

3)  The host constructs **Command 0xD811 - Start Send File to Device
    (Secured)** per **Table 202**.

4)  The host constructs **Command 0xEEEE - Send Secured Command to
    Device** using the previously constructed command as the payload,
    and sends that command to the device as a **Request Message** to
    start the process of uploading a file.

    1)  Use **Command 0xEF04 – Load LTPK Protection Key (MAGTEK INTERNAL
        ONLY FOR NOW)** to gather information about the key to use to
        secure the message payload(s). Because this command requires a
        MAC, use key slot 1111.

    2)  Build the **Security Parameters Type** portion of the wrapper
        with:

        1)  **Security Operation Type** populated with the following
            values:

            1)  Operation Type = **Command Authorization Using MAC**

            2)  Operation Algorithm = CMAC

            3)  Operation Cipher=AES-256

            4)  Padding = One and zeros

            5)  **MAC Block Size** with any number

        2)  **Key Information Type** populated with the key information
            gathered earlier.

5)  The device sends a **Response Message** so the host knows it can
    begin sending the file.

6)  The host sends a **Data File Message** to the device. If the device
    does not receive file data within a reasonable period of time, it
    times out and stops listening for the data file.

7)  The device checks to make sure the **File ID** and the length and
    hash of the File Payload match with the values the host specified in
    this command.

8)  The device repeats the same **Response Message**, this time with the
    **Message Reference Number** set to the same value the host used in
    the **Data File Message**.

Table 202 - Request Data for Command 0xD811 - Start Send File to Device
(Secured)

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
<td colspan="6">D811 = <strong>Command 0xD811 - Start Send File to
Device (Secured)</strong></td>
</tr>
<tr>
<td>81</td>
<td>04</td>
<td>File ID from ­Table 196</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>A2</td>
<td>var</td>
<td>File transfer properties</td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>var</td>
<td><p>Length of File Payload</p>
<p>This is the length of the <strong>File Payload</strong> parameter in
the <strong>Data File Message</strong> the host sends to the
device.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>01</td>
<td><p>Hash Checksum Type</p>
<ul>
<li><p>0x04 = SHA-256</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>20</td>
<td><p>Hash Checksum</p>
<p>Anticipated checksum calculated against the <strong>File
Payload</strong>, according to the standard specified in <strong>Hash
Checksum Type</strong>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>A3</td>
<td>var</td>
<td><p>File Description</p>
<p>The host should populate this value to help identify the file using
<strong>Command 0xD825 - Get File Info from Device</strong>.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>var</td>
<td><p>File Name</p>
<p>Maximum length 32 bytes</p>
<p>Reserved for future use. Leave empty.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>/82</td>
<td>var</td>
<td><p>File Label</p>
<p>Maximum length 16 bytes</p>
<p>Reserved for future use. Leave empty.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>/83</td>
<td>var</td>
<td><p>File Version</p>
<p>Maximum length 7 bytes</p>
<p>Reserved for future use. Leave empty.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>/84</td>
<td>var</td>
<td><p>File Date</p>
<p>Maximum length 20 bytes</p>
<p>Reserved for future use. Leave empty.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>87</td>
<td>01</td>
<td>Reserved for future use. Leave empty.</td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 203 - Response Data for Command 0xD811 - Start Send File to Device
(Secured)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| D811 = **Command 0xD811 - Start Send File to Device (Secured)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

If the request started successfully, the Request Status in the message
wrapper is **OK, Started / Running, All good / requested operation was
successful**.

***Note: For additional support, please contact MagTek Support.***

Table 204 - Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 04 D8 11 84 81 8F EE EE A1 19 81 05 03 03 06 02 08 84 00 85 00 A8 0A 81 02 11 02 82 00 86 00 88 00 A9 00 82 04 FF FF FF F0 83 08 C9 65 45 F2 97 69 85 B1 84 4E D8 11 81 04 00 00 03 00 A2 2B 81 04 00 00 02 99 82 01 04 83 20 87 A4 B3 54 61 C5 CB D3 1D DC BA 9D 65 25 5A D4 6A 22 FA 51 5E FD 65 87 AF AC A8 8C 4F AF 80 9B A3 14 38 31 30 38 33 30 33 30 33 30 33 30 33 30 33 33 33 30 33 30 87 01 01 9E 10 7D E4 27 C8 A0 70 72 08 19 0A 1E 0A 3F 48 BB F1 |

Table 205 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 0C D8 11 82 04 00 00 00 00 |

#### Command 0xD812 - Start Send File to Device (Unsecured)

The host uses this command to start sending unsecured files to the
device for storage or processing. It is similar to **Command 0xD811 -
Start Send File to Device (Secured)** but is used to send a different
subset of file types that do not impact device security, Refer to ­Table
196 to determine which file type can use unsecure command This command
is paired with **Command 0xD821 - Start Get File from Device**, which
the host can use to retrieve files. However, some file types are “one
way only” and can not be retrieved using that command after the host
sends them to the device.

The sequence of events is as follows:

1)  The host determines which file type it will send to the device (see
    section **6.7.1 About Files**), and either opens an existing file in
    its file system for reading, or begins constructing it.

2)  The host constructs **Command 0xD812 - Start Send File to Device
    (Unsecured)** per **­­Table 206**.

3)  The host sends that command to the device as a **Request Message**
    to start the process of uploading a file.

4)  The device sends a **Response Message** so the host knows it can
    begin sending the file.

5)  The host sends a **Data File Message** to the device. (MAGTEK
    INTERNAL ONLY FOR NOW) If the device does not receive file data
    within a reasonable period of time, it times out and stops listening
    for the data file.

6)  The device checks to make sure the **File ID** and the length and
    hash of the **File Payload** match with the values the host
    specified in this command.

7)  The device repeats the same **Response Message**, this time with the
    **Message Reference Number** set to the same value the host used in
    the **Data File Message**.

­­Table 206 - Request Data for Command 0xD812 - Start Send File to Device
(Unsecured)

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
<td colspan="6">D812 = <strong>Command 0xD812 - Start Send File to
Device (Unsecured)</strong></td>
</tr>
<tr>
<td>81</td>
<td>04</td>
<td>File ID from ­Table 196</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>A2</td>
<td>var</td>
<td>File transfer properties</td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>var</td>
<td><p>Length of File Payload</p>
<p>This is the length of the <strong>File Payload</strong> parameter in
the <strong>Data File Message</strong> the host sends to the
device.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>01</td>
<td><p>Hash Checksum Type</p>
<ul>
<li><p>0x04 = SHA-256</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>20</td>
<td><p>Hash Checksum</p>
<p>Anticipated checksum calculated against the <strong>File
Payload</strong>, according to the standard specified in <strong>Hash
Checksum Type</strong>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>A3</td>
<td>var</td>
<td><p>File Description</p>
<p>The host should populate this value to help identify the file using
<strong>Command 0xD825 - Get File Info from Device</strong>.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>var</td>
<td><p>File Name</p>
<p>Maximum length 32 bytes</p>
<p>Reserved for future use. Leave empty.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>/82</td>
<td>var</td>
<td><p>File Label</p>
<p>Maximum length 16 bytes</p>
<p>Reserved for future use. Leave empty.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>/83</td>
<td>var</td>
<td><p>File Version</p>
<p>Maximum length 7 bytes</p>
<p>Reserved for future use. Leave empty.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>/84</td>
<td>var</td>
<td><p>File Date</p>
<p>Maximum length 20 bytes</p>
<p>Reserved for future use. Leave empty.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>87</td>
<td>01</td>
<td>Reserved for future use. Leave empty.</td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 207 - Response Data for Command 0xD812 - Start Send File to Device
(Unsecured)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| D812 = **Command 0xD812 - Start Send File to Device (Unsecured)** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

If the request started successfully, the Request Status in the message
wrapper is **OK, Started / Running, All good / requested operation was
successful**.

***Note: For additional support, please contact MagTek Support.***

Table 208 - Request Example

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
<p>81 04 01 07 D8 12</p>
<p>84 44</p>
<p>D8 12</p>
<p>81 04 02 00 00 00</p>
<p>A2 2B</p>
<p>81 04 00 02 58 38</p>
<p>82 01 04</p>
<p>83 20</p>
<p>D5 B8 BF 2F 3A 15 D9 EE 1D 0D E5 8E DD 68 37 73</p>
<p>18 51 C7 3C 3D 79 58 2B A6 07 90 5C 2B 86 3C E5</p>
<p>A3 0A</p>
<p>81 08 30 32 30 30 30 30 30 30 87 01 01</p></td>
</tr>
</tbody>
</table>

Table 209 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 07 D8 12 82 04 00 00 00 00 |

#### Command 0xD821 - Start Get File from Device

The host uses this command to request a file stored on the device. File
types include standard files (images and certificates), MagTek custom
files (configuration, firmware), and in some cases even large data blob
output (such as signature capture data). In many cases, the files
retrieved by this command have been sent by a host previously using
**Command 0xD811 - Start Send File to Device (Secured)** or **Command
0xD812 - Start Send File to Device (Unsecured)**. In other cases, such
as retrieving signature capture data, the data may originate with the
device and the host uses this command to retrieve it. Such data and is
not persistent, in the sense that the device does not retain it through
power cycles.

The sequence of events is as follows:

1)  The host composes a command request in the format below, and sends
    it to the device.

2)  The device sends a response in the format below so the host knows it
    can begin listening for a file message.

3)  The device sends a **Data File Message** to the host. If the host
    does not receive file data within a reasonable period of time, it
    should time out and stop listening for the data file.

4)  Upon receiving the end of the **Data File Message**, the host should
    check to make sure the **File ID**, length, and hash of the **File
    Payload** in the **Data File Message** match the values the device
    specified in its response to ensure the file has not been tampered
    with.

Table 210 - Request Data for Command 0xD821 - Start Get File from Device

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
<td colspan="6">D821 = <strong>Command 0xD821 - Start Get File from
Device</strong></td>
</tr>
<tr>
<td>81</td>
<td>04</td>
<td>File ID from ­Table 196</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>87</td>
<td>01</td>
<td><p>Progress indicator behavior (Reserved for future use / Subject to
change)</p>
<ul>
<li><p>0x00 = None</p></li>
<li><p>0x01 = LED</p></li>
</ul></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Request Message</strong> found on page <a
href="#request-message"><strong>23</strong></a></td>
</tr>
</tbody>
</table>

Table 211 - Response Data for Command 0xD821 - Start Get File from
Device

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
<td colspan="6">D821 = <strong>Command 0xD821 - Start Get File from
Device</strong></td>
</tr>
<tr>
<td>81</td>
<td>04</td>
<td>File ID from ­Table 196</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>A2</td>
<td>var</td>
<td>File transfer properties</td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>var</td>
<td><p>Length of File Payload</p>
<p>This is the length of the <strong>File Payload</strong> parameter in
the <strong>Data File Message</strong> the device sends to the
host.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>01</td>
<td><p>Hash Checksum Type</p>
<ul>
<li><p>0x04 = SHA-256</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>20</td>
<td><p>Hash Checksum</p>
<p>Anticipated checksum calculated against the <strong>File
Payload</strong>, according to the standard specified in <strong>Hash
Checksum Type</strong>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>A3</td>
<td>var</td>
<td><p>File Description</p>
<p>The values the host populated for convenience when it sent the file
to help identify the file. Not all values are required.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>var</td>
<td><p>File Name</p>
<p>Maximum length 32 bytes</p>
<p>Reserved for future use.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>/82</td>
<td>var</td>
<td><p>File Label</p>
<p>Maximum length 16 bytes</p>
<p>Reserved for future use.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>/83</td>
<td>var</td>
<td><p>File Version</p>
<p>Maximum length 7 bytes</p>
<p>Reserved for future use.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>/84</td>
<td>var</td>
<td><p>File Date</p>
<p>Maximum length 20 bytes</p>
<p>Reserved for future use.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Response Message</strong> found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
</tbody>
</table>

If the request started successfully, the Request Status in the message
wrapper is **OK, Done.**

Table 212 - Request Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA 00 81 04 01 08 D8 21 84 0B D8 21 81 04 00 00 00 01 87 01 01 |

Table 213 - Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 08 D8 21 82 04 00 00 00 00 84 54 D8 21 81 04 00 00 00 01 A2 2B 81 04 00 00 00 40 82 01 04 83 20 FD EA B9 AC F3 71 03 62 BD 26 58 CD C9 A2 9E 8F 9C 75 7F CF 98 11 60 3A 8C 44 7C D1 D9 15 11 08 A3 1D 81 0B 54 45 53 54 5F 31 4B 2E 62 69 6E 82 05 4C 61 62 65 6C 83 07 31 2E 30 2E 30 2E 31 |

***Note: For additional support, please contact MagTek Support.***

#### Command 0xD825 - Get File Info from Device

The host uses this command to request the file information of a file
stored on the device. File types include standard files (images and
certificates), MagTek custom files (configuration, firmware), and in
some cases even large data blob output (such as signature capture data).
In many cases, the file information retrieved by this command have been
sent by a host previously using **Command 0xD811 - Start Send File to
Device (Secured)** or **Command 0xD812 - Start Send File to Device
(Unsecured)**. In other cases, such as retrieving file information of
signature capture data, the data may originate with the device and the
host uses this command to retrieve the information. Such information is
not persistent, in the sense that the device does not retain it through
power cycles.

The sequence of events is as follows:

1)  The host composes a command request in the format below, and sends
    it to the device.

2)  The device sends a response in the format below. The response
    contains the file information.

3)  If the file can not be found, then a response of failure will be
    sent to the host.

Table 214 - Request Data for Command 0xD825 - Get File Info from Device

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |
| D825 = **Command 0xD825 - Get File Info from Device** |  |  |  |  |  |
| 81 | 04 | File ID from ­Table 196 | B | R |  |
| End of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |

Table 215 - Response Data for Command 0xD825 - Get File Info from Device

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
<td colspan="6">D825 = <strong>Command 0xD825 - Get File Info from
Device</strong></td>
</tr>
<tr>
<td>81</td>
<td>04</td>
<td>File ID from ­Table 196</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>A2</td>
<td>var</td>
<td>File transfer properties</td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>var</td>
<td><p>Length of File</p>
<p>This is the length of the file.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>01</td>
<td><p>Hash Checksum Type</p>
<ul>
<li><p>0x04 = SHA-256</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>20</td>
<td><p>Hash Checksum</p>
<p>Anticipated checksum calculated against the file, according to the
standard specified in <strong>Hash Checksum Type</strong>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>A3</td>
<td>var</td>
<td><p>File Description</p>
<p>The values the host populated for convenience when it sent the file
to help identify the file. Not all values are required.</p></td>
<td>T</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/81</td>
<td>var</td>
<td><p>File Name</p>
<p>Maximum length 32 bytes</p>
<p>Reserved for future use.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>/82</td>
<td>var</td>
<td><p>File Label</p>
<p>Maximum length 16 bytes</p>
<p>Reserved for future use.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>/83</td>
<td>var</td>
<td><p>File Version</p>
<p>Maximum length 7 bytes</p>
<p>Reserved for future use.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td>/84</td>
<td>var</td>
<td><p>File Date</p>
<p>Maximum length 20 bytes</p>
<p>Reserved for future use.</p></td>
<td>B</td>
<td>O</td>
<td>Null</td>
</tr>
<tr>
<td colspan="6">End of any wrappers, at minimum including
<strong>Response Message</strong> found on page <a
href="#response-message"><strong>24</strong></a></td>
</tr>
</tbody>
</table>

If the request started successfully, the Request Status in the message
wrapper is **OK, Started / Running, All good / requested operation was
successful**.

Table 216 - Request Example

| Example (Hex)                                         |
|-------------------------------------------------------|
| AA 00 81 04 01 08 D8 21 84 08 D8 25 81 04 00 00 00 01 |

Table 217 - Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 08 D8 25 82 04 00 00 00 00 84 54 D8 25 81 04 00 00 00 01 A2 2B 81 04 00 00 00 40 82 01 04 83 20 FD EA B9 AC F3 71 03 62 BD 26 58 CD C9 A2 9E 8F 9C 75 7F CF 98 11 60 3A 8C 44 7C D1 D9 15 11 08 A3 1D 81 0B 54 45 53 54 5F 31 4B 2E 62 69 6E 82 05 4C 61 62 65 6C 83 07 31 2E 30 2E 30 2E 31 |

***Note: For additional support, please contact MagTek Support.***

#### Command 0xD831 – Delete File from Device

The host uses this command to request the deletion of a file stored on
the device. File types include

Custom Idle Page Image 1 to 4 in **­­Table 206**.

The sequence of events is as follows:

1\) The host composes a command request in the format below and sends it
to the device.

2\) The device reads and erases the file and sends a response to the
host in the format below.

3\) If the file read or the file erase fails, a response of failure will
be sent to the host.

Table 218 - Request Data for Command 0xD831 – Delete File from Device

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |
| D831 = **Command 0xD831 – Delete File from Device** |  |  |  |  |  |
| 81 | 04 | File ID from ­Table 196 | B | R |  |
| End of any wrappers, at minimum including **Request Message** found on page [**23**](#request-message) |  |  |  |  |  |

Table 219 - Response Data for Command 0xD831 – Delete File from Device

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| D831 = **Command 0xD831 – Delete File from Device** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

Table 220 - Request Example

| Example (Hex)                                         |
|-------------------------------------------------------|
| AA 00 81 04 01 05 D8 31 84 08 D8 31 81 04 02 00 00 00 |

Table 221 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 05 D8 31 82 04 00 00 00 00 |