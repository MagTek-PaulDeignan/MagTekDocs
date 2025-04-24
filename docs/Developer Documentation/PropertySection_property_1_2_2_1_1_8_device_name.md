---
title: Property 1.2.2.1.1.8 Device Name
layout: home
parent: Configuration
nav_order: 80
---

## Property 1.2.2.1.1.8 Device Name

Table 703 - Property 1.2.2.1.1.8 Device Name

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.8 / 0x010202010108 |
| Name | Device Name |
| Description | The device uses this property to set Device Name for WLAN settings. Device Name is registered to the DNS which adds the domain name to create a hostname. Use Hostname to connect to device WebSocket. If the Device Name is shorter than 64 bytes, all remaining bytes after the Device Name should be set to zeros. |
| Securing Key | None |
| Min. Len (b) | 64 |
| Max. Len (b) | 64 |
| Data Type | Binary |
| Valid Values |  |
| Default | None |

Table 704 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C800 |

Table 705 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048228D101 820400000000 8482005AD101 81072B06010401F609 850101 894AE248E246E144E142C84064662D78787878787878000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 |

Table 706 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040127D111 845AD111 81072B06010401F609 850101 894AE248E246E144E142C840 64662D78787878787878000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 |

Table 707 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048227D111 820400000000 8482005AD111 81072B06010401F609 850101 894AE248E246E144E142C84064662D78787878787878000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 |

##