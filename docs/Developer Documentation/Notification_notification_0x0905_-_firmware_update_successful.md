---
title: Notification 0x0905 - Firmware Update Successful
layout: home
parent: Notifications
nav_order: 11
---

## Notification 0x0905 - Firmware Update Successful

This notification reports the successful completion of firmware update
operations the host initiated using **Command 0xD801 - Load Firmware
File** and **Command 0xD901 - Commit Firmware from File**. The
**Notification Detail** for those two commands are shown in the table
below.

Table 318 - Notification Detail Codes

| B1  | B2  | B3  | B4  | Meaning                                     |
|-----|-----|-----|-----|---------------------------------------------|
| 08  | 01  | 0A  | 03  | Commit Firmware from File Complete, Success |
| 08  | 01  | 09  | 03  | Load Firmware File Complete, Success        |

#