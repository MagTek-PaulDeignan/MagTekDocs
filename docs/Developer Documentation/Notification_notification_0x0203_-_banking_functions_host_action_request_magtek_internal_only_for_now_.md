---
title: Notification 0x0203 - Banking Functions Host Action Request(MAGTEK INTERNAL ONLY FOR NOW)
layout: home
parent: Notifications
nav_order: 8
---

## Notification 0x0203 - Banking Functions Host Action Request(MAGTEK INTERNAL ONLY FOR NOW)

This notification requests that the host take action during operations
involving the device’s Banking Functions modules.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, shown in
**Table 334**, to indicate:

- The **User Interface Module** (UI) involved

- The **Reason** (Rsn) for the notification (UI Event)

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

#