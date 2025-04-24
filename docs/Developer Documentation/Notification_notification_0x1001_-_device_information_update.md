---
title: Notification 0x1001 - Device Information Update
layout: home
parent: Notifications
nav_order: 15
---

## Notification 0x1001 - Device Information Update

This notification reports information about general state changes that
occur within the device, outside the context of specific operations like
transactions (**Notification Source 0x01nn - Notifications from
Transactions**), requests the host receives from the firmware’s
integrated display interface (**Notification Source 0x18nn -
Notifications from User Interface**), and so on.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 320** **below**, to indicate:

- The **Category** (Cat) of notification (for example, the subsystem the
  notification is originating from)

- The **Reason** (Rsn) for the notification (Device Event)

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

The other optional message parameters in the **Notification Message**
depend on which combination of four bytes is included in **Notification
Detail**, and are described in **Table 320**.

Table 320 - Notification Detail Codes

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr>
<th>Cat</th>
<th>Rsn</th>
<th>Det</th>
<th>Ext</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5"><p>Category <strong>0x00 Power / Reset</strong> contains
notification detail codes involving the device’s power and reset
functionality. Each possible notification has a unique
<strong>Reason</strong> value:</p>
<ul>
<li><p>Reason 0x00 = Device Reset Occurred</p></li>
<li><p>Reason 0x01 = Device Reset Will Occur Soon</p></li>
<li><p>Reason 0x02 = Low Battery</p></li>
<li><p>Reason 0x03 = Key Management</p></li>
<li><p>Reason 0x04 = Temperature</p></li>
</ul></td>
</tr>
<tr>
<td>00</td>
<td>00</td>
<td>00</td>
<td>00</td>
<td><p>Power/Reset, Device Reset Occurred, Reserved, Reserved</p>
<p>The device sends and repeats this notification after the device power
cycles or resets, depending on the setting in <strong>Property
1.2.7.1.1.1 Device Reset Occurred Notification Control</strong>. If it
is set to repeat, it does so until the host acknowledges it using
<strong>Property 1.2.7.1.1.2 Device Reset Occurred Notification
Acknowledged</strong>.</p>
<p>These notifications always include the <strong>Notification
Payload</strong> parameter in the <strong>Notification Message</strong>,
as shown in <strong>Table 334</strong>.</p></td>
</tr>
<tr>
<td>00</td>
<td>01</td>
<td>00</td>
<td>00</td>
<td><p>Power/Reset, Device Reset Will Occur Soon, Reserved, Reserved</p>
<p>The device sends this notification before it automatically resets to
conform to PCI’s 24 hour Self-Test requirement, and behaves according to
the setting in <a
href="#property-1.2.7.1.1.3-device-reset-will-occur-soon-notification-control"><strong>Property
1.2.7.1.1.3 Device Reset Will Occur Soon Notification
Control</strong></a>.</p>
<p>See <strong>24 Hour Automatic Reset PCI Requirement</strong> for more
information.</p>
<p>These notifications always include the <strong>Notification
Payload</strong> parameter in the <strong>Notification Message</strong>,
which directly contains one byte indicating the number of minutes (0x01
to 0xFF) until the device will perform the reset.</p></td>
</tr>
<tr>
<td>00</td>
<td>02</td>
<td>00</td>
<td>00</td>
<td><p>Power/Reset, Battery, Low Battery Warning, Percent</p>
<p>The device sends this notification when the battery charge reaches 15
percent. If a device is powered on with a charge that is already 15
percent or below, this notification is sent shortly after power up and
includes the current battery charge percentage. Percent indicates the
percent of battery charge remaining.</p></td>
</tr>
<tr>
<td>00</td>
<td>02</td>
<td>01</td>
<td>00</td>
<td><p>Power/Reset, Battery, Power Down Imminent, Reserved</p>
<p>The device sends this notification one minute before it automatically
powers down the device because the battery charge has reached 0
percent.</p></td>
</tr>
<tr>
<td>00</td>
<td>02</td>
<td>02</td>
<td>00</td>
<td><p>Power/Reset, Battery, Battery Charge Complete, Reserved</p>
<p>The device sends this notification when the battery charger detects
that the battery is fully charged.</p></td>
</tr>
<tr>
<td>00</td>
<td>03</td>
<td>00</td>
<td>00</td>
<td><p>Power/Reset, Device reset per Command 0x1F01.</p>
<p>The device sends this notification to notify the host when Device
executes Reset Command 0x1F01.</p></td>
</tr>
<tr>
<td colspan="5"><p>Category <strong>0x01 User Event</strong> contains
notification detail codes involving events triggered by user actions.
Each possible notification has a unique <strong>Reason</strong>
value:</p>
<ul>
<li><p>Reason 0x00 = Contactless Card Presented (EMV Contactless
Only)</p></li>
<li><p>Reason 0x01 = Contactless Card Removed (EMV Contactless
Only)</p></li>
<li><p>Reason 0x02 = Card Seated in Slot (EMV Contact Only)</p></li>
<li><p>Reason 0x03 = Card Unseated from Slot (EMV Contact Only)</p></li>
<li><p>Reason 0x04 = Card Swiped (MSR Only)</p></li>
<li><p>Reason 0x05 = Touch Sensor Press On Display (Touch Only)</p></li>
<li><p>Reason 0x06 = Touch Sensor Release On Display (Touch
Only)</p></li>
<li><p>Reason 0x07 = Barcode Read (BCR Only)</p></li>
</ul>
<p>The host can use <strong>Property 1.2.7.1.2.1 User Event Notification
Controls</strong> Enable to enable these notification reasons
individually.</p>
<p>The host may choose to use these notifications to determine when to
send additional commands. For example, it may send <strong>Command
0x1001 - Start Transaction</strong>. The host should do this as quickly
as possible to minimize the response time between when the cardholder
presents a card and when the device provides feedback via a visible or
audible state change or attempts to read a chip card. Note there are
cases where the device may send a notification with
<strong>Reason</strong> = <strong>Contactless Card Presented</strong>
while the cardholder is inserting or swiping a card, so the host should
start transactions with all supported card interfaces enabled to
maximize the chances of a successful card read.</p></td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>00</td>
<td>00</td>
<td>User Event, Contactless Card Presented, EMV, Reserved (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>00</td>
<td>00</td>
<td>User Event, Contactless Card Removed, EMV, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>01</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, NTag/MIFARE Ultralite,
Reserved (EMV Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>01</td>
<td>00</td>
<td>User Event, Contactless Card Removed, NTag/MIFARE Ultralite,
Reserved (EMV Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>02</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE Classic, 1K (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>02</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE Classic, 1K (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>03</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE Classic, 4K (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>03</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE Classic, 4K (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>04</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE DESFire Light (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>04</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE DESFire Light (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>05</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE MINI® (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>05</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE MINI® (EMV Contactless
Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>06</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE Plus EV1 (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read an NFC tag. In this
case, the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>06</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE Plus EV1 (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>07</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE Plus EV2 (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read an NFC tag. In this
case, the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID.</strong></p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>07</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE Plus EV2 (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>08</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE Plus SE (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read an NFC tag. In this
case, the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>08</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE Plus SE (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>09</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE Plus X (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read an NFC tag. In this
case, the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>09</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE Plus X (EMV Contactless
Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>0A</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE DESFire EV1 (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>0A</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE DESFire EV1 (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>0B</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE DESFire EV2 (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>0B</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE DESFire EV2 (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>00</td>
<td>0C</td>
<td>00</td>
<td><p>User Event, Contactless Card Presented, MIFARE DESFire EV3 (EMV
Contactless Only)</p>
<p>The contactless reader has successfully read a NFC tag. In this case,
the device includes UID data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
UID Data is in the format described in <strong>Table 332 - Notification
Payload for UID</strong>.</p>
<p>A sample notification is shown here: <strong>Table 333 – Notification
Payload for UID Example</strong></p></td>
</tr>
<tr>
<td>01</td>
<td>01</td>
<td>0C</td>
<td>00</td>
<td>User Event, Contactless Card Removed, MIFARE DESFire EV3 (EMV
Contactless Only)</td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>00</td>
<td>00</td>
<td>User Event, Card Seated in Slot, Reserved, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td>01</td>
<td>03</td>
<td>00</td>
<td>00</td>
<td>User Event, Card Unseated from Slot, Reserved, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td>01</td>
<td>04</td>
<td>00</td>
<td>00</td>
<td><p>User Event, Card Swiped, Reserved, Reserved (MSR Only)</p>
<p>When the host receives this notification, it should call
<strong>Command 0x1001 - Start Transaction</strong> before the timeout
configured in <strong>Property 1.2.7.1.2.2 User Event Notification MSR
Data Timeout (MSR Only)</strong> to process the MSR swipe data the
device is temporarily storing in memory.</p></td>
</tr>
<tr>
<td>01</td>
<td>05</td>
<td>00</td>
<td>00</td>
<td><p>User Event, Touch Sensor Press On Display, Reserved, Reserved
(Touch Only)</p>
<p>These notifications always include the <strong>Notification
Payload</strong> parameter in the <strong>Notification Message</strong>,
as shown in <strong>Table 326</strong>.</p></td>
</tr>
<tr>
<td>01</td>
<td>06</td>
<td>00</td>
<td>00</td>
<td><p>User Event, Touch Sensor Release On Display, Reserved, Reserved
(Touch Only)</p>
<p>These notifications always include the <strong>Notification
Payload</strong> parameter in the <strong>Notification Message</strong>,
as shown in <strong>Table 326</strong>.</p></td>
</tr>
<tr>
<td>01</td>
<td>07</td>
<td>00</td>
<td>00</td>
<td><p>Barcode Reader, Read Barcode Result, Type, Reserved (BCR
Only)</p>
<ul>
<li><p>Type 0x00 = Unknown</p></li>
<li><p>Type 0x01 = MagTek</p></li>
<li><p>Type 0x02 = EMV</p></li>
</ul>
<p>The barcode reader has successfully read a barcode. In this case, the
device includes barcode data in the <strong>Notification
Payload</strong> portion of the <strong>Notification Message</strong>.
If the data is encrypted, the data is in the format described in
<strong>Table 341</strong>. Data that is not encrypted is in the format
described in <strong>Table 342</strong>.</p></td>
</tr>
<tr>
<td colspan="5"><p>Category <strong>0x02 Session Management</strong>
contains notification detail codes involving session management
functionality (Session Management Only). Each possible notification has
a unique <strong>Reason</strong> value:</p>
<ul>
<li><p>Reason 0x00 = Session Expiring Soon</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">02</td>
<td style="text-align: center;">00</td>
<td>00</td>
<td>00</td>
<td><p>Session Management, Session Expiring Soon, Reserved, Reserved</p>
<p>The device sends this notification 5 minutes before a session expires
and every minute after that until the session is extended or the
connection is closed. The host can optionally extend the session with
<strong>Command 0x1F03 - Extend Session</strong> or by sending any
command request.</p>
<p>These notifications always include the <strong>Notification
Payload</strong> parameter in the <strong>Notification Message</strong>,
as shown in <strong>Table 328</strong>.</p></td>
</tr>
<tr>
<td colspan="5"><p>Category <strong>0x03 Key Management</strong>
contains notification detail codes involving key management
functionality (WLAN Only). Each possible notification has a unique
<strong>Reason</strong> value:</p>
<ul>
<li><p>Reason 0x00 = CSR keys generated Reason</p></li>
<li><p>0x01 = Certificate Expiring Soon</p></li>
</ul></td>
</tr>
<tr>
<td>03</td>
<td>00</td>
<td>00</td>
<td>00</td>
<td><p>Key management, CSR keys generated, Reserved, Reserved</p>
<p>This notification does not include a Notification Payload. See
<strong>Command 0xEF02 – Generate CSR keys (WLAN Only)</strong> for more
information.</p></td>
</tr>
<tr>
<td>03</td>
<td>01</td>
<td>00</td>
<td>00</td>
<td><p>Key management, Certificate Expiring Soon, Reserved, Reserved</p>
<p>See <strong>Property 1.2.2.1.1.B Certificate Expiring Soon
Notification Threshold</strong> for more information.</p>
<p>These notifications always include the <strong>Notification
Payload</strong> parameter in the <strong>Notification Message</strong>,
as shown in <strong>Table 330 - Notification Payload for Key management,
Certificate Expiring Soon</strong>.</p></td>
</tr>
<tr>
<td colspan="5"><p>Category <strong>0x04 Temperature</strong> contains
notification detail codes involving temperature reporting. Each possible
notification has a unique <strong>Reason</strong> value:</p>
<ul>
<li><p>Reason 0x00 = Temperature out of range</p></li>
</ul></td>
</tr>
<tr>
<td>04</td>
<td>00</td>
<td>00</td>
<td>00</td>
<td><p>Temperature, Out of Range, Low Warning, Temperature</p>
<p>The device sends this notification when the device’s temperature
falls below the temperature set in Low Temperature Notification Level
(1.2.7.1.4.1). The temperature reported is in Celsius.</p></td>
</tr>
<tr>
<td>04</td>
<td>00</td>
<td>01</td>
<td>00</td>
<td><p>Temperature, Out of Range, High Warning, Temperature</p>
<p>The device sends this notification when the device’s temperature
rises above the temperature set in High Temperature Notification Level
(1.2.7.1.4.2). The temperature reported is in Celsius.</p></td>
</tr>
</tbody>
</table>

##