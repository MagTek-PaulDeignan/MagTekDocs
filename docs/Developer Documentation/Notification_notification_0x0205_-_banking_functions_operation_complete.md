---
title: Notification 0x0205 - Banking Functions Operation Complete
layout: home
parent: Notifications
nav_order: 9
---

## Notification 0x0205 - Banking Functions Operation Complete

This notification reports information about progress and state changes
that occur during interaction with the Banking Functions modules.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 339**, to indicate:

- The **User Interface Module** (UI) involved

- The **Reason** (Rsn) for the notification (UI Event)

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

Table 314 - Notification Detail Codes

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
<td colspan="5"><p>Module <strong>0x01 Touchscreen</strong> contains UI
notification detail codes that are specific to the touchscreen module
(Touch Only)</p>
<ul>
<li><p>Reason 0x01 = Signature Capture</p></li>
<li><p>Reason 0x02 = PIN Entry (Banking Functions Only)</p></li>
</ul></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>01</td>
<td>01</td>
<td><p>(Banking Functions Only)</p>
<p>Touchscreen, PIN Entry, Success, Data Attached</p>
<p>In this case, the device includes additional data defined in
<strong>Table 315</strong>, or in <strong>Table 316</strong> if the
device is including account data with PIN data.</p></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>02</td>
<td>01</td>
<td><p>(Banking Functions Only)</p>
<p>Touchscreen, PIN Entry, Operation Failed, Timeout</p></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>02</td>
<td>02</td>
<td><p>(Banking Functions Only)</p>
<p>Touchscreen, PIN Entry, Operation Failed, Hardware Not
Available</p></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>02</td>
<td>03</td>
<td><p>(Banking Functions Only)</p>
<p>Touchscreen, PIN Entry, Operation Failed, Canceled</p></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>02</td>
<td>04</td>
<td><p>(Banking Functions Only)</p>
<p>Touchscreen, PIN Entry, Operation Failed, Error</p></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>02</td>
<td>05</td>
<td><p>(Banking Functions Only)</p>
<p>Touchscreen, PIN Entry, Operation Failed, PIN Verify Failed</p></td>
</tr>
<tr>
<td>01</td>
<td>02</td>
<td>02</td>
<td>06</td>
<td><p>(Banking Functions Only)</p>
<p>Touchscreen, PIN Entry, Operation Failed, Account Data Capture
Failed</p></td>
</tr>
</tbody>
</table>

Table 315 - Notification Payload for Touchscreen, PIN Entry, Success,
Data Attached without Account Data (Banking Functions Only)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 59%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 11%" />
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
<td colspan="6">0205 = User Interface Operation Complete</td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td>Notification Payload</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/F5</td>
<td>var</td>
<td>Container for Encrypted PIN Data</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//DF71</td>
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
<td>//99</td>
<td>var</td>
<td><p>Encrypted PIN Block</p>
<p>ISO Formats 0, 1, and 3 are 8 bytes</p>
<p>ISO Format 4 is 16 bytes</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//DFDF41</td>
<td>var</td>
<td>PIN Key Serial Number (KSN)</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//DFDF42</td>
<td>01</td>
<td><p>PIN Encryption Type</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
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

Table 316 - Notification Payload for Touchscreen, PIN Entry, Success,
Data Attached with Account Data (Banking Functions Only)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 59%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 11%" />
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
<td colspan="6">0205 = User Interface Operation Complete</td>
</tr>
<tr>
<td>84</td>
<td>var</td>
<td>Notification Payload</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF59</td>
<td>var</td>
<td><p>Encrypted Data Primitive</p>
<p>Decrypt the value of this TLV data object using the algorithm and
variant specified in the <strong>Encrypted Data KSN</strong> parameter
and the <strong>Encrypted Data Encryption Type</strong> parameter to
read its contents. The format of the decrypted data is shown in
<strong>Table 317</strong>.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF56</td>
<td>var</td>
<td>Encrypted Data KSN</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/DFDF57</td>
<td>01</td>
<td><p>Encrypted Data Encryption Type</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>/F5</td>
<td>var</td>
<td>Container for Encrypted PIN Data</td>
<td>TC</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//DF71</td>
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
<td>//99</td>
<td>var</td>
<td><p>Encrypted PIN Block</p>
<p>ISO Formats 0, 1, and 3 are 8 bytes</p>
<p>ISO Format 4 is 16 bytes</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//DFDF41</td>
<td>var</td>
<td>PIN KSN</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>//DFDF42</td>
<td>01</td>
<td><p>PIN Encryption Type</p>
<p>See section <strong>4.4 Encryption Type</strong> for a list of valid
values.</p></td>
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

Table 317 - Account Data DFDF59 Decrypted Contents (Banking Functions
Only)

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| FC | var | Decrypted Data Container | T | R |  |
| /DF42 | var | MSR Track 2 Clear Text Data | B | O |  |
| /57 | var | Track 2 Equivalent Data | B | O |  |
| /5A | var | Primary Account Number | B | O |  |
| Padding to force DFDF59 plus padding to be a multiple of 8 bytes |  |  |  |  |  |