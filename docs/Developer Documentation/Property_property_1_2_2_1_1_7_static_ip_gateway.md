---
title: Property 1.2.2.1.1.7 Static IP Gateway
layout: home
parent: Configuration
nav_order: 79
---

## Property 1.2.2.1.1.7 Static IP Gateway

---

- [Property 1.2.2.1.1.7 Static IP Gateway](#property-122117-static-ip-gateway)

---


Table 698 - Property 1.2.2.1.1.7 Static IP Gateway

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.7 / 0x010202010107 |
| Name | Static_IP_Gateway |
| Description | The device uses this property as its network gateway IP address. |
| Securing Key | None |
| Min. Len (b) | 4 |
| Max. Len (b) | 4 |
| Data Type | IP4 Format/quad decimal (x.x.x.x) |
| Valid Values | 0.0.0.0 to 255.255.255.255 |
| Default | None |

Table 699 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104011AD101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C700 |

Table 700 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104821BD101 820400000000 8482001ED101 81072B06010401F609 850101 890EE20CE20AE108E106C704C0A801FE |

Table 701 - Set Request Example

| Example (Hex) |
|----|
| AA00 8104011CD111 841ED111 81072B06010401F609 850101 890EE20CE20AE108E106C704C0A801FE |

Table 702 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104821CD111 820400000000 8482001ED111 81072B06010401F609 850101 890EE20CE20AE108E106C704C0A801FE |

##