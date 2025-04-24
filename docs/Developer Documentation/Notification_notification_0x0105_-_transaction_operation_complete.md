---
title: Notification 0x0105 - Transaction Operation Complete
layout: home
parent: Notifications
nav_order: 5
---

## Notification 0x0105 - Transaction Operation Complete

This notification reports the final result of a transaction the host
initiated using **Command 0x1001 - Start Transaction**.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 311**, to indicate:

- The **Payment Technology** (PT) involved

- The **Reason** (Rsn) for the notification

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

Table 311 - Notification Detail Codes

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 1%" />
<col style="width: 4%" />
<col style="width: 1%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr>
<th colspan="2">PT</th>
<th colspan="2">Res</th>
<th>Det</th>
<th>Ext</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="7"><p>Payment Technology <strong>0x00 None</strong>
contains transaction notification detail codes that are not specific to
a particular payment technology.</p>
<ul>
<li><p>0x00 = Reserved</p></li>
<li><p>0x01 = Timeout/No Cards Detected</p></li>
<li><p>0x02 = Kernel Outcome</p></li>
<li><p>0x03 = Transaction Terminated</p></li>
<li><p>0x04 = Transaction Completed</p></li>
</ul></td>
</tr>
<tr>
<td>00</td>
<td colspan="2">01</td>
<td colspan="2">00</td>
<td>00</td>
<td>None, Timeout/No Cards Detected, Transaction Timed Out,
Reserved</td>
</tr>
<tr>
<td>00</td>
<td colspan="2">03</td>
<td colspan="2">01</td>
<td>00</td>
<td>None, Transaction Terminated, Transaction Canceled by Host,
Reserved</td>
</tr>
<tr>
<td>00</td>
<td colspan="2">03</td>
<td colspan="2">02</td>
<td>00</td>
<td>None, Transaction Terminated, Transaction Canceled by User, Reserved
(Display Only)</td>
</tr>
<tr>
<td colspan="7"><p>Payment Technology <strong>0x07 Manual Card
Entry</strong> contains transaction notification detail codes involving
manual card entry (MCE Only).</p>
<ul>
<li><p>0x00 = Reserved</p></li>
<li><p>0x01 = Timeout/No Cards Detected</p></li>
<li><p>0x02 = Kernel Outcome</p></li>
<li><p>0x03 = Transaction Terminated</p></li>
<li><p>0x04 = Transaction Completed</p></li>
</ul></td>
</tr>
<tr>
<td>07</td>
<td colspan="2">03</td>
<td colspan="2">05</td>
<td>00</td>
<td>MCE, Transaction Terminated, Transaction Canceled due to entry
error, Reserved (MCE Only)</td>
</tr>
<tr>
<td>07</td>
<td colspan="2">04</td>
<td colspan="2">00</td>
<td>00</td>
<td>MCE, Transaction Completed, Reserved, Reserved (MCE Only)</td>
</tr>
<tr>
<td colspan="7"><p>Payment Technology <strong>0x08 Magnetic Stripe
Reader (MSR)</strong> contains transaction notification detail codes
involving magnetic stripe cards (MSR Only).</p>
<ul>
<li><p>0x00 = Reserved</p></li>
<li><p>0x01 = Timeout/No Cards Detected</p></li>
<li><p>0x02 = Kernel Outcome</p></li>
<li><p>0x03 = Transaction Terminated</p></li>
<li><p>0x04 = Transaction Completed</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">03</td>
<td>05</td>
<td>00</td>
<td>MSR, Transaction Terminated, Transaction Canceled Due to Card Read
Error, Reserved (MSR Only)</td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>06</td>
<td>00</td>
<td>MSR, Outcome, Approved, Reserved (MSR Only)</td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>06</td>
<td>01</td>
<td><p>MSR, Outcome, Approved, Signature Capture Requested (MSR
Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>06</td>
<td>04</td>
<td>MSR, Outcome, Approved, Signature Capture Available (MSR Only)
(MAGTEK INTERNAL ONLY FOR NOW, not yet implemented)</td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>06</td>
<td>05</td>
<td><p>MSR, Outcome, Approved, Signature Capture Success (MSR Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>06</td>
<td>06</td>
<td><p>MSR, Outcome, Approved, Signature Capture Fail (MSR Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>07</td>
<td>00</td>
<td>MSR, Outcome, Quick Chip Deferred, Reserved (MSR Only)</td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>07</td>
<td>01</td>
<td><p>MSR, Outcome, Quick Chip Deferred, Signature Capture Requested
(MSR Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>07</td>
<td>04</td>
<td>MSR, Outcome, Quick Chip Deferred, Signature Capture Available (MSR
Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet implemented)</td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>07</td>
<td>05</td>
<td><p>MSR, Outcome, Quick Chip Deferred, Signature Capture Success (MSR
Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>07</td>
<td>06</td>
<td><p>MSR, Outcome, Quick Chip Deferred, Signature Capture Fail (MSR
Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>80</td>
<td>00</td>
<td>MSR, Outcome, Declined, Reserved (MSR Only)</td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>80</td>
<td>01</td>
<td><p>MSR, Outcome, Declined, Signature Capture Requested (MSR
Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>80</td>
<td>04</td>
<td>MSR, Outcome, Declined, Signature Capture Available (MSR Only)
(MAGTEK INTERNAL ONLY FOR NOW, not yet implemented)</td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>80</td>
<td>05</td>
<td><p>MSR, Outcome, Declined, Signature Capture Success (MSR Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">08</td>
<td colspan="2">02</td>
<td>80</td>
<td>06</td>
<td><p>MSR, Outcome, Declined, Signature Capture Fail (MSR Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="7"><p>Payment Technology <strong>0x10 EMV Contact</strong>
(“ICC”) contains transaction notification detail codes involving contact
chip cards (EMV Contact Only).</p>
<ul>
<li><p>0x00 = Reserved</p></li>
<li><p>0x01 = Timeout, no cards detected</p></li>
<li><p>0x02 = Kernel Outcome</p></li>
<li><p>0x03 = Transaction Terminated</p></li>
<li><p>0x04 = Transaction Completed</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>08</td>
<td>03</td>
<td>ICC, Kernel Outcome, Failed, MSR Fallback (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>09</td>
<td>03</td>
<td>ICC, Kernel Outcome, Empty Candidate List, MSR Fallback (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>00</td>
<td>00</td>
<td>ICC, Kernel Outcome, None, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>00</td>
<td>02</td>
<td>ICC, Kernel Outcome, None, Technical Fallback (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>0F</td>
<td>02</td>
<td>ICC, Kernel Outcome, End Application, Technical Fallback (EMV
Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>01</td>
<td>00</td>
<td>ICC, Kernel Outcome, Try Another Interface, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>02</td>
<td>00</td>
<td>ICC, Kernel Outcome, Offline Approved, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>02</td>
<td>01</td>
<td><p>ICC, Kernel Outcome, Offline Approved, Signature Capture
Requested (EMV Contact Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>02</td>
<td>04</td>
<td>ICC, Kernel Outcome, Offline Approved, Signature Capture Available
(EMV Contact Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet
implemented)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>02</td>
<td>05</td>
<td><p>ICC, Kernel Outcome, Offline Approved, Signature Capture Success
(EMV Contact Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>02</td>
<td>06</td>
<td><p>ICC, Kernel Outcome, Offline Approved, Signature Capture Fail
(EMV Contact Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>03</td>
<td>00</td>
<td>ICC, Kernel Outcome, Offline Declined, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>04</td>
<td>00</td>
<td>ICC, Kernel Outcome, Offline Failed, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>05</td>
<td>00</td>
<td>ICC, Kernel Outcome, Offline Not Accepted, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>06</td>
<td>00</td>
<td>ICC, Kernel Outcome, Approved, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>06</td>
<td>01</td>
<td><p>ICC, Kernel Outcome, Approved, Signature Capture Requested (EMV
Contact Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>06</td>
<td>04</td>
<td>ICC, Kernel Outcome, Approved, Signature Capture Available (EMV
Contact Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet implemented)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>06</td>
<td>05</td>
<td><p>ICC, Kernel Outcome, Approved, Signature Capture Success (EMV
Contact Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>06</td>
<td>06</td>
<td><p>ICC, Kernel Outcome, Approved, Signature Capture Fail (EMV
Contact Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>07</td>
<td>00</td>
<td>ICC, Kernel Outcome, Quick Chip Deferred, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>07</td>
<td>01</td>
<td><p>ICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Requested (EMV Contact Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>07</td>
<td>04</td>
<td>ICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Available (EMV Contact Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet
implemented)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>07</td>
<td>05</td>
<td><p>ICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Success (EMV Contact Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>07</td>
<td>06</td>
<td><p>ICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Failed (EMV Contact Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>08</td>
<td>00</td>
<td>ICC, Kernel Outcome, Failed, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>09</td>
<td>00</td>
<td>ICC, Kernel Outcome, Not Accepted, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>0A</td>
<td>00</td>
<td>ICC, Kernel Outcome, Transaction Canceled, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>0B</td>
<td>00</td>
<td>ICC, Kernel Outcome, Select Next Not Accepted, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>0C</td>
<td>00</td>
<td>ICC, Kernel Outcome, Select Next Retry, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>0D</td>
<td>00</td>
<td>ICC, Kernel Outcome, Try Again, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>0E</td>
<td>00</td>
<td>ICC, Kernel Outcome, Online Request, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>0F</td>
<td>00</td>
<td>ICC, Kernel Outcome, End Application, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>10</td>
<td>00</td>
<td>ICC, Kernel Outcome, Not EMV Card Pooled, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>80</td>
<td>00</td>
<td>ICC, Kernel Outcome, Declined, Reserved (EMV Contact Only)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>80</td>
<td>01</td>
<td><p>ICC, Kernel Outcome, Declined, Signature Capture Requested (EMV
Contact Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>80</td>
<td>04</td>
<td>ICC, Kernel Outcome, Declined, Signature Capture Available (EMV
Contact Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet implemented)</td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>80</td>
<td>05</td>
<td><p>ICC, Kernel Outcome, Declined, Signature Capture Success (EMV
Contact Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">02</td>
<td>80</td>
<td>06</td>
<td><p>ICC, Kernel Outcome, Declined, Signature Capture Failed (EMV
Contact Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">10</td>
<td colspan="2">04</td>
<td>07</td>
<td>00</td>
<td>ICC, Transaction Completed, Declined, Reserved (EMV Contact
Only)</td>
</tr>
<tr>
<td colspan="7"><p>Payment Technology <strong>0x20 EMV
Contactless</strong> (“PICC”) contains transaction notification detail
codes involving contactless cards and contactless payment devices (EMV
Contactless Only).</p>
<ul>
<li><p>0x00 = Reserved</p></li>
<li><p>0x01 = Timeout, no cards detected</p></li>
<li><p>0x02 = Kernel Outcome</p></li>
<li><p>0x03 = Transaction Terminated</p></li>
<li><p>0x04 = Transaction Completed</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>00</td>
<td>00</td>
<td>PICC, Kernel Outcome, None, Reserved (EMV Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>01</td>
<td>00</td>
<td>PICC, Kernel Outcome, Try Another Interface, Reserved (EMV
Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>02</td>
<td>00</td>
<td>PICC, Kernel Outcome, Offline Approved, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>02</td>
<td>01</td>
<td><p>PICC, Kernel Outcome, Offline Approved, Signature Capture
Requested (EMV Contactless Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>02</td>
<td>04</td>
<td>PICC, Kernel Outcome, Offline Approved, Signature Capture Available
(EMV Contactless Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet
implemented)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>02</td>
<td>05</td>
<td><p>PICC, Kernel Outcome, Offline Approved, Signature Capture Success
(EMV Contactless Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>02</td>
<td>06</td>
<td><p>PICC, Kernel Outcome, Offline Approved, Signature Capture Fail
(EMV Contactless Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>03</td>
<td>00</td>
<td>PICC, Kernel Outcome, Offline Declined, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>04</td>
<td>00</td>
<td>PICC, Kernel Outcome, Offline Failed, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>05</td>
<td>00</td>
<td>PICC, Kernel Outcome, Offline Not Accepted, Reserved (EMV
Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>06</td>
<td>00</td>
<td>PICC, Kernel Outcome, Approved, Reserved (EMV Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>06</td>
<td>01</td>
<td><p>PICC, Kernel Outcome, Approved, Signature Capture Requested (EMV
Contactless Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>06</td>
<td>04</td>
<td>PICC, Kernel Outcome, Approved, Signature Capture Available (EMV
Contactless Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet
implemented)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>06</td>
<td>05</td>
<td><p>PICC, Kernel Outcome, Approved, Signature Capture Success (EMV
Contactless Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>06</td>
<td>06</td>
<td><p>PICC, Kernel Outcome, Approved, Signature Capture Fail (EMV
Contactless Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>07</td>
<td>00</td>
<td>PICC, Kernel Outcome, Quick Chip Deferred, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>07</td>
<td>01</td>
<td><p>PICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Requested (EMV Contactless Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>07</td>
<td>04</td>
<td>PICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Available (EMV Contactless Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet
implemented)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>07</td>
<td>05</td>
<td><p>PICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Success (EMV Contactless Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>07</td>
<td>06</td>
<td><p>PICC, Kernel Outcome, Quick Chip Deferred, Signature Capture
Failed (EMV Contactless Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>08</td>
<td>00</td>
<td>PICC, Kernel Outcome, Failed, Reserved (EMV Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>09</td>
<td>00</td>
<td>PICC, Kernel Outcome, Not Accepted, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>0A</td>
<td>00</td>
<td>PICC, Kernel Outcome, Transaction Canceled, Reserved (EMV
Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>0B</td>
<td>00</td>
<td>PICC, Kernel Outcome, Select Next Not Accepted, Reserved (EMV
Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>0C</td>
<td>00</td>
<td>PICC, Kernel Outcome, Select Next Retry, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>0D</td>
<td>00</td>
<td>PICC, Kernel Outcome, Try Again, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>0E</td>
<td>00</td>
<td>PICC, Kernel Outcome, Online Request, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>0F</td>
<td>00</td>
<td>PICC, Kernel Outcome, End Application, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>10</td>
<td>00</td>
<td>PICC, Kernel Outcome, Not EMV Card Pooled, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>80</td>
<td>00</td>
<td>PICC, Kernel Outcome, Declined, Reserved (EMV Contactless Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>80</td>
<td>01</td>
<td><p>PICC, Kernel Outcome, Declined, Signature Capture Requested (EMV
Contactless Only)</p>
<p>If the device includes a touchscreen, the host should respond by
sending <strong>Command 0x1801 - Request Cardholder Signature (Touch
Only)</strong>.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>80</td>
<td>04</td>
<td>PICC, Kernel Outcome, Declined, Signature Capture Available (EMV
Contactless Only) (MAGTEK INTERNAL ONLY FOR NOW, not yet
implemented)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>80</td>
<td>05</td>
<td><p>PICC, Kernel Outcome, Declined, Signature Capture Success (EMV
Contactless Only)</p>
<p>The device includes signature data inside <strong>EMV Batch Data
Type</strong> tag DFDF3E.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">02</td>
<td>80</td>
<td>06</td>
<td><p>PICC, Kernel Outcome, Declined, Signature Capture Failed (EMV
Contactless Only)</p>
<p>The host may send <strong>Command 0x1801 - Request Cardholder
Signature (Touch Only)</strong> to retry capturing a signature.</p></td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">04</td>
<td>07</td>
<td>00</td>
<td>PICC, Transaction Completed, Declined, Reserved (EMV Contactless
Only)</td>
</tr>
<tr>
<td colspan="2">20</td>
<td colspan="2">05</td>
<td>00</td>
<td>00</td>
<td>PICC, NFC TAG, Tag Removed, Reserved (EMV Contactless Only)</td>
</tr>
</tbody>
</table>

Table 312 - Notification Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 83 00 01 05 82 04 20 00 00 00 |