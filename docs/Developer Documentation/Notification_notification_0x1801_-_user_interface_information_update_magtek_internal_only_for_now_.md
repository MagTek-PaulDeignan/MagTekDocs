---
title: Notification 0x1801 - User Interface Information Update (MAGTEK INTERNAL ONLY FOR NOW)
layout: home
parent: Notifications
nav_order: 20
---

## Notification 0x1801 - User Interface Information Update (MAGTEK INTERNAL ONLY FOR NOW)

This notification reports information about progress and state changes
involving the device’s User Interface modules.

For this notification, **Notification Detail** described in section
**3.2.2.3 Notification Message** contains one byte each, to indicate:

- The **Payment Technology** (PT) involved

- The **Reason** (Rsn) for the notification

- **Detail** (Det) about the notification that has different meanings
  depending on the Reason, and

- An **Extra** field (Ext) that has different meanings depending on the
  Reason.

#