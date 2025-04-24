---
title: Notification 0x0201 - Banking Functions Information Update
layout: home
parent: Notifications
nav_order: 7
---

## Notification 0x0201 - Banking Functions Information Update

This notification reports information about progress and state changes
involving the device’s Banking Functions modules.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 313 - Notification Detail Codes**, to indicate:

- The **Payment Technology** (PT) involved

- The **Reason** (Rsn) for the notification

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

Table 313 - Notification Detail Codes

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
<th>PT</th>
<th>Rsn</th>
<th>Det</th>
<th>Ext</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5"><p>Payment Technology <strong>0x07 Manual Card Entry
(MCE)</strong> contains transaction notification detail codes involving
manual card entry (MCE Only).</p>
<ul>
<li><p>Reason 0x01 = Card Event</p></li>
<li><p>Reason 0x08 = Data Update</p></li>
<li><p>Reason 0x10 = State Update</p></li>
</ul></td>
</tr>
<tr>
<td>07</td>
<td>01</td>
<td>01</td>
<td>00</td>
<td>Manual Card Entry, Card Event, Data Entered, Reserved</td>
</tr>
<tr>
<td colspan="5"><p>Payment Technology <strong>0x08 Magnetic Stripe
Reader (MSR)</strong> contains transaction notification detail codes
involving magnetic stripe cards (MSR Only).</p>
<ul>
<li><p>Reason 0x01 = Card Event</p></li>
<li><p>Reason 0x08 = Data Update</p></li>
<li><p>Reason 0x10 = State Update</p></li>
</ul></td>
</tr>
<tr>
<td>08</td>
<td>01</td>
<td>01</td>
<td>00</td>
<td>MSR, Card Event, Swiped, Reserved (MSR Only)</td>
</tr>
<tr>
<td>08</td>
<td>01</td>
<td>02</td>
<td>00</td>
<td>MSR, Card Event, Inserted, Reserved (MSR Only)</td>
</tr>
<tr>
<td>08</td>
<td>01</td>
<td>03</td>
<td>00</td>
<td>MSR, Card Event, Removed, Reserved (MSR Only)</td>
</tr>
<tr>
<td>08</td>
<td>01</td>
<td>04</td>
<td>00</td>
<td>MSR, Card Event, Detected, Reserved (MSR Only)</td>
</tr>
<tr>
<td colspan="5"><p>Payment Technology <strong>0x10 EMV Contact</strong>
contains transaction notification detail codes involving contact chip
cards (EMV Contact Only).</p>
<ul>
<li><p>Reason 0x01 = Card Event</p></li>
<li><p>Reason 0x08 = Data Update</p></li>
<li><p>Reason 0x10 = State Update</p></li>
</ul></td>
</tr>
<tr>
<td>10</td>
<td>01</td>
<td>02</td>
<td>00</td>
<td>EMV Contact, Card Event, Inserted, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td>10</td>
<td>01</td>
<td>03</td>
<td>00</td>
<td>EMV Contact, Card Event, Removed, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td>10</td>
<td>01</td>
<td>04</td>
<td>00</td>
<td>EMV Contact, Card Event, Detected, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="5"><p>Payment Technology <strong>0x20 EMV
Contactless</strong> contains transaction notification detail codes
involving contactless cards and contactless payment devices. (EMV
Contactless Only)</p>
<ul>
<li><p>Reason 0x01 = Card Event</p></li>
<li><p>Reason 0x08 = Data Update</p></li>
<li><p>Reason 0x10 = State Update</p></li>
</ul></td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>03</td>
<td>00</td>
<td>EMV Contactless, Card Event, Removed, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>04</td>
<td>00</td>
<td>EMV Contactless, Card Event, Detected, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td>20</td>
<td>01</td>
<td>05</td>
<td>00</td>
<td>EMV Contactless, Card Event, Collision, Reserved (EMV Contactless
Only)</td>
</tr>
</tbody>
</table>

#