---
title: Property 1.2.7.1.2.1 User Event Notification Controls Enable
layout: home
parent: Configuration
nav_order: 134
---

## Property 1.2.7.1.2.1 User Event Notification Controls Enable

Table 950 - Property 1.2.7.1.2.1 User Event Notification Controls Enable

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Bit Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.7.1.2.1 / 0x010207010201</td>
</tr>
<tr>
<td>Name</td>
<td>User Event Notifications Enable</td>
</tr>
<tr>
<td>Description</td>
<td><p>The host can use this property to enable <strong>notification
reasons</strong> defined in <strong>Notification 0x1001 - Device
Information Update</strong> in the <strong>User Events</strong>
Category. Each bit enables a specific <strong>Reason</strong> by setting
that bit to 1. Byte 0 is the first byte, bit 0 is the LSB of each
byte.</p>
<p>The device only detects these user events and sends these
notifications when it is idle. While processing a command (not idle),
such as when processing a transaction with <strong>Command 0x1001 -
Start Transaction</strong>, the device only sends notifications related
to the command it is currently processing.</p>
<p>Notification reasons may consume power when idle. For example,
enabling Contactless reasons requires the device to continuously consume
some radio frequency power to detect the presence of a contactless card
when idle. To conserve power, only enable the notification reasons that
are required by the solution design, if any. The readers and their
associated notifications will be disabled if the battery charge is 5
percent or lower.</p>
<p>Changes to this property do not take effect until the device is power
cycled or reset.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Byte 0</p>
<ul>
<li><p>bit 0 = Reason: Contactless Card Presented</p></li>
<li><p>bit 1 = Reason: Contactless Card Removed</p></li>
<li><p>bit 2 = Reason: Card Seated in Slot</p></li>
<li><p>bit 3 = Reason: Card Unseated from Slot</p></li>
<li><p>bit 4 = Reason: Card Swiped</p></li>
<li><p>bit 5 = Reason: Touch Sensor Press Detected</p></li>
<li><p>bit 6 = Reason: Touch Sensor Release Detected</p></li>
<li><p>bit 7 = Reason: Barcode Read Detected</p></li>
</ul>
<p>Byte 1</p>
<ul>
<li><p>bit 0 = Reason: Encrypt Barcode Reader Event Data</p></li>
</ul>
<ul>
<li><p>bit 1 = Reserved (set to 0x00)</p></li>
<li><p>etc.</p></li>
</ul>
<p>Byte 2</p>
<ul>
<li><p>bit 0 = Reserved (set to 0x00)</p></li>
<li><p>etc.</p></li>
</ul>
<p>Byte 3</p>
<ul>
<li><p>bit 0 = Reserved (set to 0x00)</p></li>
<li><p>etc.</p></li>
</ul>
<p>Any byte / bit not listed here is reserved for future use. The host
should set those values to 0, so if a future revision of firmware starts
using those bits, the related notifications will be disabled and will
not affect the existing host software.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00, 0x00, 0x00, 0x00 (all User Event notifications disabled)</td>
</tr>
</tbody>
</table>

Table 951 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02070102 8902 C100 |

Table 952 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D101 8204 00000000 84820013 D101 8501 01 8704 02070102 8906 C1 04 00 00 00 00 |

Table 953 - Set Request Example

| Example (Hex) |
|----|
| AA00 8104 0155D111 8413 D111 8501 01 8704 02070102 8906 C1 04 03 00 00 00 |

Table 954 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D111 8204 00000000 84820013 D111 8501 01 8704 02070102 8906 C1 04 03 00 00 00 |

##