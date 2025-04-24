---
title: Property 1.2.2.1.2.2 MQTT Port
layout: home
parent: Configuration
nav_order: 91
---

## Property 1.2.2.1.2.2 MQTT Port

---

- [Property 1.2.2.1.2.2 MQTT Port](#property-122122-mqtt-port)

---


| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.2.2 / 0x010202010202 |
| Name | MQTT Port |
| Description | The device uses this property to connect to broker on this network port. MQTT Port addresses are normally 8883 for secure (Recommended), 1883 for unsecure. |
| Securing Key | None |
| Min. Len (b) | 2 |
| Max. Len (b) | 2 |
| Data Type | Binary |
| Valid Values | 0x00 0x00 (0) – 0xFF 0xFF (65535) MSB first |
| Default | 8883 |

Table 757 -Property 1.2.2.1.2.2 MQTT Port

| Example (Hex)                                              |
|------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 870402020102 8902 C200 |

Table 758 -Get Request Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D10182040000000084820011D1018501018704020201028904C20222B3 |

Table 759 -Get Response Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA00 81040155D111 8411 D111 850101 870402020102 8904 C202 22B3 |

Table 760 -Set Request Example

| Example (Hex)                                                           |
|-------------------------------------------------------------------------|
| AA0081048255D11182040000000084820011D1118501018704020201028904C202 22B3 |

Table 761 -Set Response Example

##