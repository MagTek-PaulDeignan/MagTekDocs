---
title: Property 2.1.2.5.6.2 WLAN WiFi RSSI
layout: home
parent: Configuration
nav_order: 197
---

## Property 2.1.2.5.6.2 WLAN WiFi RSSI

Table 1111 - Property 2.1.2.5.6.2 WLAN WiFi RSSIWLAN WiFi RSSI

| Property Description |  |
|----|----|
| Property OID | 2.1.2.5.6.2 / 0x020102050602 |
| Name | WLAN WiFi RSSI (Received Signal Strength Indicator) |
| Description | The device uses this property to report its WiFi RSSI. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Signed Character |
| Valid Values | 0x00 – 0xFF |
| Default | None |

Table 1112 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104010ED101 841AD101 81072B06010401F609 850102 890AE108E206E504E602C200 |

Table 1113 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104820ED101 820400000000 8482001BD101 81072B06010401F609 850102 890BE109E207E505E603C2 01BE |

##