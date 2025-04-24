---
title: Property 1.2.2.1.1.9 Wireless Heartbeat Time
layout: home
parent: Configuration
nav_order: 81
---

## Property 1.2.2.1.1.9 Wireless Heartbeat Time

---

- [Property 1.2.2.1.1.9 Wireless Heartbeat Time](#property-122119-wireless-heartbeat-time)

---


Table 708 - Property 1.2.2.1.1.9 Wireless Heartbeat Time

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.9 / 0x010202010109 |
| Name | Wireless Heartbeat Time |
| Description | The device uses this property to set Heartbeat Time for WLAN settings. Device will check the Websocket connection based on this timer setting. The unit is second. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0x00 to 0xFF |
| Default | 0x00 (disabled) |

Table 709 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104011AD101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C900 |

Table 710 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104821AD101 820400000000 8482001BD101 81072B06010401F609 850101 890BE209E207E105E103C90100 |

Table 711 - Set Request Example

| Example (Hex) |
|----|
| AA00 8104011CD111 841BD111 81072B06010401F609 850101 890BE209E207E105E103C90120 |

Table 712 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104821CD111 820400000000 8482001BD111 81072B06010401F609 850101 890BE209E207E105E103C90120 |

##