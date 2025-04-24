---
title: Notification 0x0104 - Transaction Callback (MAGTEK INTERNAL ONLY FOR NOW)
layout: home
parent: Notifications
nav_order: 4
---

## Notification 0x0104 - Transaction Callback (MAGTEK INTERNAL ONLY FOR NOW)

This notification fulfills callback subscriptions the host has
requested.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 308**, to indicate:

- The …

- The …

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

Table 308 - Notification Detail Codes

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
<th>??</th>
<th>??</th>
<th>Det</th>
<th>Ext</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5"><p>xxx <strong>0x00 None</strong> contains transaction
notification detail codes xxx</p>
<ul>
<li><p>xxx 0x01 = xxx</p></li>
</ul></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="5"><p>xxx <strong>0x00 None</strong> contains transaction
notification detail codes xxx</p>
<ul>
<li><p>xxx 0x01 = xxx</p></li>
</ul></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="5"><p>xxx <strong>0x00 None</strong> contains transaction
notification detail codes xxx</p>
<ul>
<li><p>xxx 0x01 = xxx</p></li>
</ul></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

**Notification Payload** described in section **3.2.2.3 Notification
Message** is only included in some cases, described in **Table 297**.
When a Notification Payload is included, it follows the structure shown
in **Table 309**.

Table 309 - Notification Payload

| Tag | Len | Value / Description | Typ | Req | Default |
|----|----|----|----|----|----|
| Beginning of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |
| 0103 = **Notification 0x0104 - Transaction Callback (MAGTEK INTERNAL ONLY FOR NOW)** |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
| End of **Notification Message** found on page [**30**](#notification-message) |  |  |  |  |  |

Table 310 - Notification Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 83 00 01 05 82 04 20 00 00 00 |

#