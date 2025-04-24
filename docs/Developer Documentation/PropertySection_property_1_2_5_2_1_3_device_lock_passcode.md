---
title: Property 1.2.5.2.1.3 Device Lock Passcode
layout: home
parent: Configuration
nav_order: 128
---

## Property 1.2.5.2.1.3 Device Lock Passcode

Table 926- Property 1.2.5.2.1.3 Device Lock Passcode

| Property Description |  |
|----|----|
| Property OID | 1.2.5.2.1.3 / 0x010205020103 |
| Name | Device Lock Passcode |
| Description | This property can be used to set the device lock passcode. The value of the device lock passcode is stored in non-volatile memory so changes made to it will persist after the device is reset or power cycled. For security, the host can’t get the value of the device lock passcode from the device. If the host gets this property, the device will always return a length of 0 and no value. Setting this property requires security. Setting it requires the use of **Command 0xD112 - Set Property (Secured)** which requires MagTek's involvement. To set the device lock passcode without involving MagTek use **Command 0xEF07 – Change Device Lock Passcode**. See **Device Lock Feature** for more information. |
| Securing Key | See **Command 0xD112 - Set Property (Secured).** |
| Min. Len (b) | 4 |
| Max. Len (b) | 63 |
| Data Type | Binary |
| Valid Values | It can only contain any printable ASCII character. |
| Default | 0x34 0x33 0x32 0x31 (“4321”) |

Table 927 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02050201 8902 C300 |

Table 928 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 8482000F D101 850101 870402050201 8902 C300 |

Table 929 - Set Request Example

| Example (Hex) |
|---------------|
| TBD           |

Table 930 - Set Response Example

| Example (Hex) |
|---------------|
| TBD           |

#