---
title: Property 1.2.5.2.1.1 Device Lock State
layout: home
parent: Configuration
nav_order: 126
---

## Property 1.2.5.2.1.1 Device Lock State

---

- [Property 1.2.5.2.1.1 Device Lock State](#property-125211-device-lock-state)

---


Table 916- Property 1.2.5.2.1.1 Device Lock State

| Property Description |  |
|----|----|
| Property OID | 1.2.5.2.1.1 / 0x010205020101 |
| Name | Device Lock State |
| Description | This property can be used to get or set the device lock state. Getting this property does not require security, however setting it does. Setting it requires the use of **Command 0xD112 - Set Property (Secured)** which requires MagTek's involvement. To set the device lock state without involving MagTek use Command 0xEF04 – Load LTPK Protection Key. The value of the device lock state will revert to the value of **Property 1.2.5.2.1.2 Device Lock State After Reset** after a reset or a power cycle. See **Device Lock Feature** for more information. |
| Securing Key | See **Command 0xD112 - Set Property (Secured).** |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0x00 = Unlocked, 0x01 = Locked |
| Default | See **Property 1.2.5.2.1.2 Device Lock State After Reset.** |

Table 917 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02050201 8902 C100 |

Table 918 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850101 870402050201 8903 C101 00 |

Table 919 - Set Request Example

| Example (Hex) |
|---------------|
| TBD           |

Table 920 - Set Response Example

| Example (Hex) |
|---------------|
| TBD           |

##