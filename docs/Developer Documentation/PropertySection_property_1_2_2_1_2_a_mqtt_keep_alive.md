---
title: Property 1.2.2.1.2.A MQTT Keep Alive
layout: home
parent: Configuration
nav_order: 99
---

## Property 1.2.2.1.2.A MQTT Keep Alive

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.2.A / 0x01020201020A |
| Name | MQTT Keep Alive |
| Description | The device uses this property to set the MQTT Keep Alive timing. Value is in seconds, used to guarantee the connection between device and MQTT broker remains active. A value of 0 disables Keep Alive monitoring. |
| Securing Key | None |
| Min. Len (b) | 2 |
| Max. Len (b) | 2 |
| Data Type | Binary |
| Valid Values | 0x00 0x00 (0) – 0xFF 0xFF (0 = Disabled, 1 🡪 65535 seconds) MSB first |
| Default | 300 seconds |

Table 797 - Property 1.2.2.1.2.A MQTT Keep Alive

| Example (Hex)                                              |
|------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 870402020102 8902 CA00 |

Table 798 - Get Request Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D10182040000000084820011D1018501018704020201028904CA02012C |

Table 799 - Get Response Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA00 81040155D111 8411 D111 850101 870402020102 8904 CA02 012C |

Table 800 - Set Request Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D11182040000000084820011D1118501018704020201028904CA02012C |

Table 801 - Set Response Example

#