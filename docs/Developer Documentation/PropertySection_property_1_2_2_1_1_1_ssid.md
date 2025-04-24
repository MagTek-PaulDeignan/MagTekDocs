---
title: Property 1.2.2.1.1.1 SSID
layout: home
parent: Configuration
nav_order: 73
---

## Property 1.2.2.1.1.1 SSID

Table 668 - Property 1.2.2.1.1.1 SSID

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.1 / 0x010202010101 |
| Name | SSID |
| Description | The device uses this property to set SSID for WLAN settings. If the SSID is shorter than 32 bytes, all remaining bytes after the SSID should be set to zeros. |
| Securing Key | None |
| Min. Len (b) | 32 |
| Max. Len (b) | 32 |
| Data Type | Binary |
| Valid Values |  |
| Default | None |

Table 669 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040122D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C100 |

Table 670 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048222D101 820400000000 8482003AD101 81072B06010401F609 850101 892AE228E226E124E122C1204D79535349440000000000000000000000000000000000000000000000000000 |

Table 671 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040121D111 843AD111 81072B06010401F609 850101 892AE228E226E124E122C120 4D79535349440000000000000000000000000000000000000000000000000000 |

Table 672 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048221D111 820400000000 8482003AD111 81072B06010401F609 850101 892AE228E226E124E122C1204D79535349440000000000000000000000000000000000000000000000000000 |

##