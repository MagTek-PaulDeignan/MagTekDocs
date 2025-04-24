---
title: Property 1.2.2.1.1.6 Static IP Netmask
layout: home
parent: Configuration
nav_order: 78
---

## Property 1.2.2.1.1.6 Static IP Netmask

---

- [Property 1.2.2.1.1.6 Static IP Netmask](#property-122116-static-ip-netmask)

---


Table 693 - Property 1.2.2.1.1.6 Static IP Netmask

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.6 / 0x010202010106 |
| Name | Static_IP_Netmask |
| Description | The device uses this property as its network mask in web socket mode. |
| Securing Key | None |
| Min. Len (b) | 4 |
| Max. Len (b) | 4 |
| Data Type | IP4 Format/quad decimal (x.x.x.x) |
| Valid Values | 0.0.0.0 to 255.255.255.255 |
| Default | None |

Table 694 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040118D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C600 |

Table 695 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048218D101 820400000000 8482001ED101 81072B06010401F609 850101 890EE20CE20AE108E106C604FFFFFF00 |

Table 696 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040119D111 841ED111 81072B06010401F609 850101 890EE20CE20AE108E106C604FFFFFF00 |

Table 697 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048219D111 820400000000 8482001ED111 81072B06010401F609 850101 890EE20CE20AE108E106C604FFFFFF00 |

##