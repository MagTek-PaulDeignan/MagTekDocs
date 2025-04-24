---
title: Property 1.1.1.1.1.6 ARPC Retry Attempts
layout: home
parent: Configuration
nav_order: 8
---

## Property 1.1.1.1.1.6 ARPC Retry Attempts

---

- [Property 1.1.1.1.1.6 ARPC Retry Attempts](#property-111116-arpc-retry-attempts)

---


Table 369 - Property 1.1.1.1.1.6 ARPC Retry Attempts

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.6 / 0x010101010106 |
| Name | ARPC Retry Attempts |
| Description | The device uses this property to control its ARPC Retry Attempts. If a timeout occurs when the device is waiting for the host to send **Command 0x1004 - Resume Transaction** with ARPC data, the device re-sends **Notification 0x0101 - Transaction Information Update** to report **ARQC Update** and waits for ARPC data again, up to the number of retries specified by this property. After the final retry, the device continues with the transaction. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0x00..0xFF |
| Default | 0x00 |

Table 370 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 C600 |

Table 371 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 10 D1 01 85 01 01 87 04 01 01 01 01 89 03 C6 01 00 |

Table 372 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870401010101 8903 C60100 |

Table 373 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 01 01 01 01 89 03 C6 01 00 |

##