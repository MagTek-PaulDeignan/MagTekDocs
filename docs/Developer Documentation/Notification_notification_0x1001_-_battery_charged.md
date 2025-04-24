---
title: Notification 0x1001 - Battery Charged
layout: home
parent: Notifications
nav_order: 18
---

## Notification 0x1001 - Battery Charged

The device sends this notification when the battery charger detects that
the battery is fully charged. This only occurs when the device is
powered by a USB power source. See **Table 13 - Notification Message
Format** and **Table 323 - Battery Charged Notification Example**.

Table 323 - Battery Charged Notification Example

| Example (Hex)                          |
|----------------------------------------|
| AA 00 81 04 83 00 10 01 82 00 02 02 00 |

Table 324 - Notification Payload for Device Reset Occurred

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |
| 1001 = Device Information Update |  |  |  |  |  |
| 81 | var | This parameter has the same length and value described by **Property 2.3.1.2.1.1 Device Operational Status**. | B | R |  |
| 82 | var | This parameter has the same length and value described by **Property 2.3.1.2.1.2 Offline Status Detail**. | B | R |  |
| xx | var | More data objects may be added in future firmware revisions. |  |  |  |
| End of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |

Table 325 - Notification Example for Device Reset Occurred

| Example (Hex)                                                   |
|-----------------------------------------------------------------|
| AA00 81 04 83001001 82 04 00000000 84 08 1001 81 01 02 82 01 00 |

Table 326 - Notification Payload for Touch Sensor Press or Release On
Display (Touch Only)

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
<td colspan="6">1001 = Device Information Update</td>
</tr>
<tr>
<td>81</td>
<td>04</td>
<td><p>Press / Release Coordinates</p>
<p>Coordinates of the press / release from origin 0,0 at the top left
corner of the display, automatically adjusted to match the device’s
orientation as configured by Property 1.2.3.1.1.2 Custom Idle Page Image
Device Locked (Display Only).</p>
<p>Bytes 1..2 X Coordinate</p>
<p>X coordinate of press / release, in big endian order.</p>
<p>Bytes 3..4 Y Coordinate</p>
<p>Y Coordinate of press / release, in big endian order.</p></td>
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

Table 327 - Notification Example for Touch Sensor Press or Release On
Display (Touch Only)

| Example (Hex)                                                   |
|-----------------------------------------------------------------|
| AA00 81 04 83001001 82 04 00000000 84 08 1001 81 04 00 80 00 80 |

Table 328 - Notification Payload for Session Expiring Soon (Session
Management Only)

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
<td colspan="6">1001 = Device Information Update</td>
</tr>
<tr>
<td>81</td>
<td>1</td>
<td><p>Interface</p>
<p>0x00 = WLAN</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>82</td>
<td>1</td>
<td><p>Connection</p>
<p>0x00 = Connection 0, Interfaces that only support one connection will
use connection 0. WLAN will always set this to 0 even if the device is
configured to support more than one connection with <strong>Property
1.2.2.1.1.A Maximum Client Connections</strong> since there is only a
single session for all clients. See <strong>Command 0x1F03 - Extend
Session (Session Management Only)</strong> for more information on this
scenario.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>83</td>
<td>1</td>
<td><p>Expiration Time</p>
<p>The time in minutes until the session expires.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>xx</td>
<td>var</td>
<td>More data objects may be added in future firmware revisions.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="6">End of <strong>Notification Message</strong> found on
page <a href="#notification-message"><strong>30</strong></a></td>
</tr>
</tbody>
</table>

Table 329 - Notification Example for Session Expiring Soon (Session
Management Only)

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA00 81 04 83001001 82 04 00000000 84 0B 1001 81 01 00 82 01 00 83 01 05 |

Table 330 - Notification Payload for Key management, Certificate
Expiring Soon (Session Management Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |
| 1001 = Device Information Update |  |  |  |  |  |
| 81 | 1 | This parameter has the same length and value described by **Property 1.2.2.1.1.B Certificate Expiring Soon Notification Threshold**. | B | R |  |
| 82 | 1 | This parameter contains the certificate identifier. See the certificate file type section (File Type 0x03) from ­Table 196 to identify this certificate by locating the certificate that has a File Subtype that matches this certificate identifier. | B | R |  |
| 83 | 1 | The number of days the certificate is still valid. | B | R |  |
| End of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |

Table 331 - Notification Example for Key management, Certificate
Expiring Soon (Session Management Only)

| Example (Hex)                                                   |
|-----------------------------------------------------------------|
| AA00 81 04 83001001 82 04 00000000 84 08 1001 81 01 02 82 01 00 |

Table 332 - Notification Payload for UID

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |
| 1001 = Device Information Update |  |  |  |  |  |
| 84 | var | NFC Payload | B | R |  |
| /DF79 | var | NFC UID | B | R |  |
| End of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |

Table 333 – Notification Payload for UID Example

| Example (Hex) |
|----|
| AA 00 81 04 83 00 10 01 82 04 01 00 01 00 84 0E 10 01 84 0A DF 79 07 04 37 1F 71 BF 61 80 |