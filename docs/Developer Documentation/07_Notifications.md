---
title: Notifications
layout: home
parent: DynaFlex Family Programmer's Manual
nav_order: 7
---
## Notifications

This section provides definitions and practical information about
**Notification Message**s, which follow the format described in section
**3.2.2.3**. To find documentation about a specific notification:

1)  Use the **Notification Source** byte in the message to find the
    Notification Source subsection below. For example, Notification
    Source **0x01 Transaction** leads to subsection **7.1 Notification
    Source 0x01nn - Notifications from Transactions**.

2)  Within that subsection, use the **Notification Source** byte plus
    the **Notification Type** byte in the message to find the
    Notification subsection. For example, Notification Source **0x01
    Transaction** plus Notification Type **0x01 Information Update**
    leads to **Notification 0x0101 - Transaction Information Update**.

3)  Within that subsection, use the four bytes of **Notification Detail
    Code** in the message to look up the notification in the
    **Notification Detail Code** table. For example, **0x07080302**
    leads to a row in **Table 297** that provides practical information
    about what event led to the notification, and how to interpret the
    Notification Payload.

