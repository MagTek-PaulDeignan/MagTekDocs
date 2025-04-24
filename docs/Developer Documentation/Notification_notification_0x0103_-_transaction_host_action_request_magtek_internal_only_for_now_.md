---
title: Notification 0x0103 - Transaction Host Action Request (MAGTEK INTERNAL ONLY FOR NOW)
layout: home
parent: Notifications
nav_order: 3
---

## Notification 0x0103 - Transaction Host Action Request (MAGTEK INTERNAL ONLY FOR NOW)

This notification requests the host take action to support a transaction
in progress.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 303**, to indicate:

- The **Payment Technology**, which is always set to 0x00.

- The **Reason** (Rsn) for the notification

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

Table 303 - Notification Detail Codes

| PT | Rsn | Det | Ext | Meaning |
|----|----|----|----|----|
| Payment Technology **0x00 All** contains all transaction host request detail codes. |  |  |  |  |
|  |  |  |  |  |

**Notification Payload** described in section **3.2.2.3 Notification
Message** is only included in some cases, described in **Table 297**.
When a Notification Payload is included, it follows the structure shown
in **Table 304**.

Table 304 - Notification Payload for Transaction Host Action Request

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |
| 0103 = **Notification 0x0103 - Transaction Host Action Request (MAGTEK INTERNAL ONLY FOR NOW)** |  |  |  |  |  |
|  |  |  |  |  |  |
| End of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |

Table 305 - Notification Example for Display Message Request
Notifications (No Display Only)

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
<td><p>Display Message Request to show PROCESSING</p>
<p>AA 00</p>
<p>81 04 83 00 01 03 // Notification source/type = 0x0103</p>
<p>82 04</p>
<p>00</p>
<p>01 // 0x01=Display Message Request</p>
<p>01 // 0x01=Data Attached</p>
<p>00</p>
<p>84 82 00 12 // Payload, 18 bytes (using two-byte Length)</p>
<p>81 01 01 // Clear Screen is enabled</p>
<p>82 82 00 0B // Messages, 11 bytes (using two-byte Length)</p>
<p>50 52 4F 43 45 53 53 49 4E 47 00 // “PROCESSING” (line terminator is
0x00)</p></td>
</tr>
</tbody>
</table>

Table 306 - Notification Example for Cardholder Selection Request (No
Display Only)

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
<td><p>Cardholder Selection Request to show:</p>
<p>APPLICATION SELECT</p>
<p>1 - VISA CREDIT</p>
<p>2 - VISA DEBIT</p>
<p>3 - VISA ELECTRON</p>
<p>AA 00</p>
<p>81 04 83 00 01 03 // Notification source/type = 0x0103</p>
<p>82 04</p>
<p>00</p>
<p>02 // 0x02=Cardholder Selection Request</p>
<p>00</p>
<p>00 // Timeout, TT=0x00</p>
<p>84 82 00 4B // Payload, 75 bytes (using two-byte Length)</p>
<p>81 01 01 // Clear Display</p>
<p>82 82 00 44 // Messages, 68 bytes (using two-byte Length)</p>
<p>41 50 50 4C 49 43 41 54 49 4F 4E 20 53 45 4C 45 43 54 0A</p>
<p>31 20 2D 20 56 49 53 41 20 43 52 45 44 49 54 0A</p>
<p>32 20 2D 20 56 49 53 41 20 44 45 42 49 54 0A</p>
<p>33 20 2D 20 56 49 53 41 20 45 4C 45 43 54 52 4F 4E 00</p></td>
</tr>
</tbody>
</table>

Table 307 - Notification Example for Online PIN Request (MAGTEK INTERNAL
ONLY FOR NOW, No Display Only)

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
<td><p>(MAGTEK INTERNAL ONLY FOR NOW)</p>
<p>Online PIN Request to show:</p>
<p>VISA DEBIT</p>
<p>100.00</p>
<p>AA 00 81 04 83 00 01 05 82 04 00 03 00 00 84 16 9F 12 0A 56 49 53 41
20 44 45 42 49 54 9F 02 06 00 00 00 01 00 00</p></td>
</tr>
</tbody>
</table>

#