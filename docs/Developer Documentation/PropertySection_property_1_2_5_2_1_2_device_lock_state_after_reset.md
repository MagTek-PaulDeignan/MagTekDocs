---
title: Property 1.2.5.2.1.2 Device Lock State After Reset
layout: home
parent: Configuration
nav_order: 127
---

## Property 1.2.5.2.1.2 Device Lock State After Reset

Table 921- Property 1.2.5.2.1.2 Device Lock State After Reset

| Property Description |  |
|----|----|
| Property OID | 1.2.5.2.1.2 / 0x010205020102 |
| Name | Device Lock State After Reset |
| Description | This property can be used to get or set what **Property 1.2.5.2.1.1 Device Lock State** will be set to after the device is reset or power cycled. Systems that use the optional device lock feature should set this property to locked, otherwise all someone would need to do to unlock the device would be to power cycle or reset it. The value of the device lock state after reset property is stored in non-volatile memory so changes made to it will persist after the device is reset or power cycled. See **Device Lock Feature** for more information. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0x00 = Unlocked, 0x01 = Locked |
| Default | 0x00 |

Table 922 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02050201 8902 C200 |

Table 923 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850101 870402050201 8903 C201 00 |

Table 924 - Set Request Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA00 81040155D111 8410 D111 8501 01 8704 02050201 8903 C201 00 |

Table 925 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048255D111 820400000000 84820010 D111 850101 870402050201 8903 C201 00 |

##