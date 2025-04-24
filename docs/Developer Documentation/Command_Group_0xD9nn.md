---
title: Command Group 0xD9nn - Process Files
layout: home
parent: Commands
nav_order: 8
---

## Command Group 0xD9nn - Process Files

---

- [Command Group 0xD9nn - Process Files](#command-group-0xd9nn---process-files)
    - [Command 0xD901 - Commit Firmware from File](#command-0xd901---commit-firmware-from-file)

---


#### Command 0xD901 - Commit Firmware from File

The host uses this command to commit a file previously uploaded using
**Command 0xD801 - Load Firmware File** into the device’s permanent
memory after the device has authenticated the file.

The sequence of events is as follows:

1)  The host composes a command request in the format below, and sends
    it to the device.

2)  The device sends a response in the format below.

3)  The device writes the image file to permanent storage.

4)  If the commit operation was successful, the device sends
    **Notification 0x0905 - Firmware Update Successful** to the host. If
    the commit operation was not successful, the device sends
    **Notification 0x0906 - Firmware Update Failed** to the host. In
    both cases, the device automatically resets.

Table 222 - Request Data for Command 0xD901 - Commit Firmware from File

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
<td colspan="6">D901 = <strong>Command 0xD901 - Commit Firmware from
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
<td>82</td>
<td>01</td>
<td><p>Operation Options</p>
<p>Reserved for future use. Populate with 0x00.</p></td>
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
<li><p>0x0002 = WiFi Module image</p></li>
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
<p>This is a SHA-256 hash of the entire <strong>Firmware File Type
(MAGTEK INTERNAL ONLY)</strong> object being uploaded.</p></td>
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

Table 223 - Response Data for Command 0xD901 - Commit Firmware from File

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |
| D901 = **Command 0xD901 - Commit Firmware from File** |  |  |  |  |  |
| No parameters. |  |  |  |  |  |
| End of any wrappers, at minimum including **Response Message** found on page [**24**](#response-message) |  |  |  |  |  |

If the request started successfully, the Request Status in the message
wrapper is **OK, Started / Running, All good / requested operation was
successful**.

Table 224 - Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 02 D9 01 84 2E D9 01 81 01 03 82 01 00 85 02 00 01 86 20 DF C7 1E 09 A3 CE 8E 86 B0 F5 B6 75 BE B7 7A 0E 82 33 BF F1 8A CD 8F 38 34 B0 DB 20 D9 40 4B 28 |

Table 225 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 02 D9 01 82 04 00 00 00 00 |

Table 226 - Notification Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 83 00 09 05 82 04 08 01 0A 03 |

***Note: For additional support, please contact MagTek Support.***