---
title: Notification 0x1001 – Low Battery Warning
layout: home
parent: Notifications
nav_order: 16
---

## Notification 0x1001 – Low Battery Warning

The device sends this notification when the battery charge reaches 15
percent. If a device is powered on with a charge that is already 15
percent or below, this notification is sent shortly after power up and
includes the current battery charge percentage. Percent indicates the
percent of battery charge remaining. It is recommended that the device
is charged using a USB power source soon after receiving this
notification. See **Table 13 - Notification Message Format** and **Table
321 Low Battery Notification Example**.

| Example (Hex)                          |
|----------------------------------------|
| AA 00 81 04 83 00 10 01 82 00 02 00 0D |

Table 321 Low Battery Notification Example

##