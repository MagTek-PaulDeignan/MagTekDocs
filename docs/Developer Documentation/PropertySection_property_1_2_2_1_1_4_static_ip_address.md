---
title: Property 1.2.2.1.1.4 Static IP Address
layout: home
parent: Configuration
nav_order: 76
---

## Property 1.2.2.1.1.4 Static IP Address

Table 683 - Property 1.2.2.1.1.4 Static IP Address

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.4 / 0x010202010104 |
| Name | Static_IP_Address |
| Description | The device uses this property as its IP address in web socket mode if **Property 1.2.2.1.1.5 Use DHCP** is set to 0000 (Static IP mode). |
| Securing Key | None |
| Min. Len (b) | 4 |
| Max. Len (b) | 4 |
| Data Type | IP4 Format/quad decimal (x.x.x.x) |
| Valid Values | 0.0.0.0 to 255.255.255 |
| Default | None |

Table 684 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040105D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C400 |

Table 685 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048205D101 820400000000 8482001ED101 81072B06010401F609 850101 890EE20CE20AE108E106C404C0A80177 |

Table 686 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040111D111 841ED111 81072B06010401F609 850101 890EE20CE20AE108E106C404C0A8016D |

Table 687 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048211D111 820400000000 8482001ED111 81072B06010401F609 850101 890EE20CE20AE108E106C404C0A8016D |

##