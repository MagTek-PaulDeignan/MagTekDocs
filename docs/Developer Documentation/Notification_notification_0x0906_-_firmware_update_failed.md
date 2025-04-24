---
title: Notification 0x0906 - Firmware Update Failed
layout: home
parent: Notifications
nav_order: 12
---

## Notification 0x0906 - Firmware Update Failed

This notification reports the failure of a Firmware Update command the
host initiated using **Command 0xD801 - Load Firmware File** and
**Command 0xD901 - Commit Firmware from File**. The **Notification
Detail** for those two commands are shown in the table below.

Table 319 - Notification Detail Codes

| B1  | B2  | B3  | B4  | Meaning                                    |
|-----|-----|-----|-----|--------------------------------------------|
| 08  | 01  | 0A  | 04  | Commit Firmware from File Complete, Failed |
| 08  | 01  | 09  | 04  | Load Firmware File Complete, Failed        |

#