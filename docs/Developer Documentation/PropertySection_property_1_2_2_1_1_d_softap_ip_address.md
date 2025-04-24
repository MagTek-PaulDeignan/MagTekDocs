---
title: Property 1.2.2.1.1.D SoftAP IP Address
layout: home
parent: Configuration
nav_order: 85
---

## Property 1.2.2.1.1.D SoftAP IP Address

Table 728 - Property 1.2.2.1.1.D SoftAP IP Address

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.D / 0x01020201010D |
| Name | SoftAP_IP_Address |
| Description | This OID is used to store a soft AP IP address. When a device starts AP mode, it reads this value as its IP address. A new value will be stored with this OID if a user modifies the soft AP IP address. |
| Securing Key | None |
| Min. Len (b) | 4 |
| Max. Len (b) | 4 |
| Data Type | IP4 Format/quad decimal (x.x.x.x) |
| Valid Values | 0.0.0.0 to 255.255.255 |
| Default | 192.168.0.1 |

Table 729 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040103D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102CD00 |

Table 730 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048203D101 820400000000 8482001ED101 81072B06010401F609 850101 890EE20CE20AE108E106CD0400000000 |

Table 731 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040107D111 841ED111 81072B06010401F609 850101 890EE20CE20AE108E106CD04C0A80177 |

Table 732 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048207D111 820400000000 8482001ED111 81072B06010401F609 850101 890EE20CE20AE108E106CD04C0A80177 |

##