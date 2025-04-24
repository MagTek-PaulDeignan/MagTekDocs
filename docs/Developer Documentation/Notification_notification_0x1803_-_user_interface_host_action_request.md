---
title: Notification 0x1803 - User Interface Host Action Request
layout: home
parent: Notifications
nav_order: 21
---

## Notification 0x1803 - User Interface Host Action Request

This notification requests that the host take action during operations
involving the device’s User Interface modules.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 334**, to indicate:

- The **User Interface Module** (UI) involved

- The **Reason** (Rsn) for the notification (UI Event)

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

Table 334 - Notification Detail Codes

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th>UI</th>
<th>Rsn</th>
<th>Det</th>
<th>Ext</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5">Module <strong>0x00 Miscellaneous</strong> contains UI
notification detail codes that are not specific to a particular UI
module.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="5"><p>Module <strong>0x01 Touchscreen</strong> contains UI
notification detail codes that are specific to the touchscreen module
(Touch Only).</p>
<ul>
<li><p>Reason 0x01 = Signature Capture</p></li>
<li><p>Reason 0x02 = Functional button selected</p></li>
<li><p>Reason 0x03 = Button text string selected</p></li>
<li><p>Reason 0x04 = Button $Amount selected</p></li>
<li><p>Reason 0x05 = Present card functional button Right is
selected</p></li>
</ul></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>01</td>
<td>00</td>
<td>Touchscreen, Functional button Left selected</td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>02</td>
<td>00</td>
<td>Touchscreen, Functional button Middle selected</td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>03</td>
<td>00</td>
<td>Touchscreen, Functional button Right selected</td>
</tr>
<tr>
<td>01</td>
<td>03</td>
<td>01</td>
<td>00</td>
<td>Touchscreen, Text string button 1 selected</td>
</tr>
<tr>
<td>01</td>
<td>03</td>
<td>02</td>
<td>00</td>
<td>Touchscreen, Text string button 2 selected</td>
</tr>
<tr>
<td>01</td>
<td>03</td>
<td>03</td>
<td>00</td>
<td>Touchscreen, Text string button 3 selected</td>
</tr>
<tr>
<td>01</td>
<td>03</td>
<td>04</td>
<td>00</td>
<td>Touchscreen, Text string button 4 selected</td>
</tr>
<tr>
<td>01</td>
<td>03</td>
<td>05</td>
<td>00</td>
<td>Touchscreen, Text string button 5 selected</td>
</tr>
<tr>
<td>01</td>
<td>03</td>
<td>06</td>
<td>00</td>
<td>Touchscreen, Text string button 6 selected</td>
</tr>
<tr>
<td>01</td>
<td>04</td>
<td>00</td>
<td>00</td>
<td>Touchscreen, $Amount button selected, Data Attached contain the
amount selected as described in <strong>Table 336 - Notification Payload
for $ Amount button selected, Data Attached</strong></td>
</tr>
<tr>
<td>01</td>
<td>05</td>
<td>00</td>
<td>00</td>
<td>Touchscreen, Present card functional button Right selected</td>
</tr>
<tr>
<td colspan="5"><p>Module <strong>0x02 Display</strong> contains UI
notification detail codes that are specific to the display module. The
device primarily uses these notifications to request that the host stand
in as a display to interact with cardholders / operators when the device
does not have a display of its own (No Display Only).</p>
<ul>
<li><p>Reason 0x01 = Display Message Request</p></li>
<li><p>Reason 0x02 = Cardholder Selection Request</p></li>
<li><p>Reason 0x03 = Online PIN Request (MAGTEK INTERNAL ONLY FOR
NOW)</p></li>
</ul></td>
</tr>
<tr>
<td>02</td>
<td>01</td>
<td>00</td>
<td>00</td>
<td><p>Display, Display Message, No Data Attached, Clear Display.</p>
<p>The host should clear any existing messages it is currently
displaying (No Display Only).</p></td>
</tr>
<tr>
<td>02</td>
<td>01</td>
<td>01</td>
<td>00</td>
<td><p>Display, Display Message, Data Attached, No Cancel Function (No
Display Only)</p>
<p>In this case, the notification includes additional data and display
control, defined in <strong>Table 335</strong>, in the
<strong>Notification Payload</strong> portion of the
<strong>Notification Message</strong>.</p>
<p>This notification is for simple messages. The host should show the
requested message until another notification arrives or until the host
needs to use the display for its own purposes. For example, during a
transaction, this notification will pass along the simple messages in
the transaction sequence like <strong>CARD READ OK - REMOVE
CARD</strong>, <strong>THANK YOU</strong>, and
<strong>WELCOME</strong>.</p></td>
</tr>
<tr>
<td>02</td>
<td>01</td>
<td>02</td>
<td>00</td>
<td><p>Display, Display Message, Data Attached, Include Cancel Function
(No Display Only)</p>
<p>In this case, the notification includes additional data and display
control, defined in <strong>Table 335</strong>, in the
<strong>Notification Payload</strong> portion of the
<strong>Notification Message</strong>.</p>
<p>The host should show the requested message and should allow the
request to be canceled by a cardholder or operator. For example, during
a transaction, this notification will pass along the simple messages in
the transaction sequence like “TAP, INSERT, or SWIPE CARD,” where
cancelation is appropriate. If the cancel button involves canceling the
whole transaction, the host should send <strong>Command 0x1008 - Cancel
Transaction</strong>.</p></td>
</tr>
<tr>
<td>02</td>
<td>02</td>
<td>00</td>
<td>00</td>
<td><p>Display, Cardholder Selection, Data Attached, Reserved (No
Display Only)</p>
<p>In this case, the notification includes additional data and display
control, defined in <strong>Table 337</strong>, in the
<strong>Notification Payload</strong> portion of the
<strong>Notification Message</strong>.</p>
<p>The host should show the requested selection, then send
<strong>Command 0x1802 - Report Cardholder Selection</strong> to device
to return the cardholder’s selection to the device.</p></td>
</tr>
<tr>
<td>02</td>
<td>03</td>
<td>00</td>
<td>00</td>
<td><p>(MAGTEK INTERNAL ONLY FOR NOW, No Display Only)</p>
<p>Display, Online PIN Request, Application ID / Amount, Data Attached,
Reserved.</p>
<p>In this case, the notification includes additional data, defined in
<strong>Table 338</strong>, in the <strong>Notification Payload</strong>
portion of the <strong>Notification Message</strong>.</p>
<p>The host must send Command TBD to the device to indicate PIN Capture
data and result.</p></td>
</tr>
</tbody>
</table>

Table 335 - Notification Payload for Display Message Request
Notifications (No Display Only)

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
<td colspan="6">1803 = <strong>Notification 0x1803 - User Interface Host
Action Request</strong></td>
</tr>
<tr>
<td>/81</td>
<td>01</td>
<td><p>Reserved for time functions.</p>
<p>0x00</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>01</td>
<td><p>Append or Clear Display</p>
<ul>
<li><p>0x00 = Append the message(s) on the next available row.</p></li>
<li><p>0x01 = Clear the display first and display the requested message
on the first row.</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>var</td>
<td><p>Message</p>
<p>This parameter is a set of one or more ASCII strings the host should
show, with each string terminated by any one of the following
characters. MagTek recommends proceeding to the next row on receiving
any of these characters:</p>
<ul>
<li><p>Null (0x00)</p></li>
<li><p>LF (0x0A)</p></li>
<li><p>The end of the Message parameter.</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/85</td>
<td>var</td>
<td><p>Enhanced Application Select Message</p>
<p>For Contactless, this parameter will return the PPSE response
starting from tag BF0C</p>
<p>BF0C &lt;LEN&gt;&lt;VALUE&gt;</p>
<p>For Contact, this parameter will return all available AID returned
from the PSE or List Of AIDs, from tag 70</p>
<p>70 &lt;len&gt;</p>
<p>61 &lt;len&gt;</p>
<p>4F&lt;len&gt;&lt;value of AID&gt;</p>
<p>50&lt;len&gt;&lt;value of Application Label&gt;</p>
<p>87&lt;len&gt;&lt;value of Application Priority Indicator&gt;</p>
<p>61 &lt;len&gt;</p>
<p>4F&lt;len&gt;&lt;value of AID&gt;</p>
<p>50&lt;len&gt;&lt;value of Application Label&gt;</p>
<p>87&lt;len&gt;&lt;value of Application Priority Indicator,
optional&gt;</p>
<p>If the GPO Response returns a <strong>Notification 0x0101 -
Transaction Information Update of</strong>’69 85’, the response will be
sent first by the device and this Enhanced Application Select Message
will be sent again.</p></td>
<td>B</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td colspan="6">End of <strong>Notification Message</strong> found on
page <strong><a href="#notification-message">30</a>.</strong></td>
</tr>
</tbody>
</table>

**Table 336 - Notification Payload for \$ Amount button selected, Data
Attached**

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page **[30](#notification-message).** |  |  |  |  |  |
| 1803 = **Command 0x1803 - Display Message (Display Only)** |  |  |  |  |  |
| 84 | 9 | Amount selected payload | B | R |  |
| /9F02 | 6 | Dollar and cents amount selected in BCD format | B | R |  |
| End of **Notification Message** found on page **[30](#notification-message).** |  |  |  |  |  |

Table 337 - Notification Payload for Cardholder Selection Notifications
(No Display Only)

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
<td colspan="6">1803 = <strong>Notification 0x1803 - User Interface Host
Action Request</strong></td>
</tr>
<tr>
<td>/81</td>
<td>01</td>
<td>Time in seconds the device will wait for host to respond with
<strong>Command 0x1802 - Report Cardholder Selection</strong>.</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/82</td>
<td>01</td>
<td><p>Append or Clear Display</p>
<ul>
<li><p>0x00 = Append, display the messages on the next line.</p></li>
<li><p>0x01 = Clear, clear the display first and display the requested
message on the first line.</p></li>
</ul></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/83</td>
<td>var</td>
<td><p>Message</p>
<p>This parameter is a set of one or more ASCII strings the host should
show, with each string terminated by any one of the following
characters. MagTek recommends proceeding to the next row on receiving
any of these characters:</p>
<ul>
<li><p>Null (0x00)</p></li>
<li><p>LF (0x0A)</p></li>
<li><p>The end of the Message parameter.</p></li>
</ul></td>
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

Table 338 - Notification Payload for Display Online PIN Request
Notifications (MAGTEK INTERNAL ONLY FOR NOW, No Display Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |
| 1803 = **Notification 0x1803 - User Interface Host Action Request** |  |  |  |  |  |
| /9F12 | var | This contains AID Preferred Name (Tag 9F12) if it is provided by the card. | B | O |  |
| /9F06 | var | This contains the AID (Tag) if Tag 9F12 is not provided by the card. | B | O |  |
| /9F02 | 06 | This contains the Amount (Tag 9F02) if it should be displayed. For example, the device excludes this when using a provisional amount for a Quick Chip transaction. | B | O |  |
| End of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |

#