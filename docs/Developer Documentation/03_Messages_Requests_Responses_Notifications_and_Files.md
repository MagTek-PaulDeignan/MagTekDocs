---
title: Messages (Requests, Responses, Notifications, and Files)
layout: home
parent: DynaFlex Family Programmer's Manual
nav_order: 3
---
## Messages (Requests, Responses, Notifications, and Files)

---

### Contents

- [About Messages](#about-messages)
- [Message Format](#message-format)
  - [TLV Encoding](#tlv-encoding)
    - [TLV Example](#tlv-example)
    - [How to Read TLV Tables](#how-to-read-tlv-tables)
- [Message Structure](#message-structure)
  - [Request Message](#request-message)
  - [Response Message](#response-message)
  - [Notification Message](#notification-message)
  - [Data File Message](#data-file-message)

---

### About Messages

The host and the device communicate with each other by exchanging blocks of data called **Messages**, which are standardized wrappers containing a **payload** that is either a command **Request**, a command **Response**, an unsolicited **Notification**, or a **File**.

For example, the host may send a command **request** message to the device to change a configuration setting, and the device may send a command **response** message to indicate the command was successful; when a cardholder inserts a card, the device may send a **notification** message to the host that a cardholder has initiated a transaction; the host may send the device a **file** message to load firmware.

Messages can be nested. For example, a top-level secure wrapper request from the host to the device may contain an encrypted or signed command request for the device to unpack, validate, and execute.

**Requests and Responses.** The combination of a message that contains a **request** payload and a message that contains the corresponding **response** payload is referred to generally as a **Command**. The device can only service one command request at a time, and sends each command response within a predetermined finite amount of time after receiving the request.

**Notifications.** The device sends notification messages to the host when its state changes or an external event occurs (e.g., card insertion). Notifications do not require a response.

**Data Files.** Data files are large payloads exchanged between host and device using a stream approach. They must consist only of primitive data.

All MMS devices follow a common schema for sending and receiving messages, documented in section [Message Format](#message-format).

### Message Format

This section defines how messages are structured in MMS communication using Tag-Length-Value (TLV) encoding, conforming to DER (Distinguished Encoding Rules). Each message follows the MMS framework and may contain nested TLV objects.

Refer to [TLV Encoding](#tlv-encoding) for specific rules, [TLV Example](#tlv-example) for a full message breakdown, and [How to Read TLV Tables](#how-to-read-tlv-tables) for guidance interpreting nesting and formatting.

### Message Structure

Each message type follow a specific structure, detailed in the subsections below.

#### Request Message

### **Table 10 - Request Message Format**

| Tag   | Len  | Value / Description                                                                                                     | Typ | Req | Default |
|--------|------|--------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
|        |      | **Start of Message**                                                                                                     |     |     |         |
|        |      | One byte standard Start of Message constant, not in TLV format. `0xAA`                                                  |     |     |         |
|        |      | **API Framework Version**                                                                                                |     |     |         |
|        |      | One-byte standard API version, not TLV. `0x00`, `0x01`, `0x02`, etc.                                                      |     |     |         |
| 81     | var  | Message Information                                                                                                      | B   | R   |         |
| /null  | (1)  | Message Type & Direction: `0x01` = Host→Device, `0x81` = Reserved Device→Host                                             | B   | R   |         |
| /null  | (1)  | Message Reference Number                                                                                                  | B   | R   |         |
| /null  | (2)  | Command ID                                                                                                               | B   | R   |         |
| /null  | var  | Reserved                                                                                                                |     | O   |         |
| 84     | var  | Request Payload (See Section 6 Commands)                                                                                 | B   | R   |         |
| 9E     | var  | Reserved                                                                                                                | B   | O   |         |

#### Response Message

### **Table 11 - Response Message Format**

| Tag   | Len | Value / Description                                                                                                          | Typ | Req | Default |
|--------|-----|-------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
|        |     | **Start of Message** `0xAA`                                                                                                   |     |     |         |
|        |     | **API Framework Version** `0x00` - `0x02`                                                                                    |     |     |         |
| 81     | 4   | Message Information                                                                                                          | B   | R   |         |
| /null  | (1) | Message Type & Direction: `0x02` = Reserved Host→Device, `0x82` = Device→Host                                               |     | R   |         |
| /null  | (1) | Message Reference Number                                                                                                     |     | R   |         |
| /null  | (2) | Response ID = Command ID from corresponding request (`0x1001 = Start Transaction`, etc.)                                    |     | R   |         |
| /null  | var | Reserved                                                                                                                   |     | O   |         |
| 82     | 04  | Response Status                                                                                                            | B   | R   |         |
| /null  | (1) | Operation Status Summary: `0x00` = OK, `0x80` = Failed start, etc.                                                         | B   | R   |         |
| /null  | (1) | Operation Status Detail (Group) (see Table 12)                                                                             | B   | R   |         |
| /null  | (1) | Operation Status Detail (Subgroup)                                                                                        | B   | R   |         |
| /null  | (1) | Operation Status Detail (Status Code)                                                                                      | B   | R   |         |
| 83     | var | Additional Details                                                                                                          |     | O   |         |
| 84     | var | Response Payload                                                                                                           | B   | O   |         |
| 9E     | var | Reserved                                                                                                                   | B   | O   |         |

#### **Table 12 - Operation Status Detail Codes**

| Source             | Grp | Sub | Cde | Meaning                                                                 |
|--------------------|-----|-----|-----|-------------------------------------------------------------------------|
| General            | 00  | 00  | 00  | All good / requested operation was successful.                         |
| General            | 00  | 00  | 02  | Requested Operation Failed                                             |
| General            | 00  | 00  | 10  | Setting up RTC data and time failure                                   |
| General            | 00  | 00  | 11  | Setting up RTC alarm failure                                           |
| General            | 00  | 00  | 12  | Key generation failure                                                 |
| General            | 00  | 00  | 13  | Tamper setting is locked, can’t be changed                             |
| General            | 00  | 00  | 14  | Tamper setting requires system reset to continue                       |
| General            | 00  | 00  | 15  | Tamper status can’t be cleared, failure                                |
| General            | 00  | 00  | 16  | Device has been tampered, need attention                               |
| Message Handler    | 01  | 01  | 01  | Generic Failure                                                         |
| Message Handler    | 01  | 01  | 02  | Bad message parameter                                                  |
| Message Handler    | 01  | 01  | 09  | Device offline, cannot process messages                                |
| Request Handler    | 02  | 01  | 01  | Generic Failure                                                         |
| Request Handler    | 02  | 01  | 02  | Bad Message Parameter                                                   |
| Request Handler    | 02  | 01  | 07  | Internal FW Failure                                                     |
| Request Handler    | 02  | 01  | 0A  | Image Failure                                                           |
| Request Handler    | 02  | 01  | 19  | Key does not exist                                                      |
| Request Handler    | 02  | 01  | 1A  | Not Secured                                                             |
| Request Handler    | 02  | 01  | 1B  | Passcode validation failed                                              |
| Request Handler    | 02  | 01  | 1C  | Device is locked                                                        |
| Request Handler    | 02  | 03  | 16  | Failed, device state, Low Battery (5% or less)                          |
| Request Handler    | 02  | 05  | 13  | Error in Decrypting Key data                                            |
| Request Handler    | 02  | 05  | 14  | Error in computing MAC over entire message                             |
| Request Handler    | 02  | 05  | 16  | KDF Error                                                               |
| Request Handler    | 02  | 05  | 1F  | Invalid Kcv                                                             |
| Request Handler    | 02  | 05  | 20  | Invalid Data                                                            |
| Request Handler    | 02  | 05  | 21  | Invalid DUKPT key derivation                                            |
| Request Handler    | 02  | 05  | 22  | Invalid Exportability                                                   |
| Request Handler    | 02  | 05  | 23  | Invalid Key Class                                                       |
| Request Handler    | 02  | 05  | 24  | Invalid DSN                                                             |
| Request Handler    | 02  | 05  | 25  | Invalid Challenge                                                       |

#### Notification Message

### **Table 13 - Notification Message Format**

| Tag   | Len | Value / Description                                                                                                       | Typ | Req | Default |
|--------|-----|----------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
|        |     | **Start of Message** `0xAA`                                                                                                 |     |     |         |
|        |     | **API Framework Version** `0x00` - `0x02`                                                                                  |     |     |         |
| 81     | 04  | Message Information                                                                                                         | B   | R   |         |
| /null  | (1) | Message Type & Direction: `0x03` = Reserved Host→Device, `0x83` = Device→Host Notification                                 |     | R   |         |
| /null  | (1) | Reserved (set to `0x00`)                                                                                                    |     | R   |         |
| /null  | (1) | Notification Source: (e.g., `0x01` = Transaction, `0x10` = Device, `0x18` = UI)                                            |     | R   |         |
| /null  | (1) | Notification Type: (`0x01` = Info Update, `0x02` = Warning, `0x03` = Action Request, etc.)                                 |     | R   |         |
| /null  | var | Reserved                                                                                                                   |     | O   |         |
| 82     | 04  | Notification Detail Code (6-byte ID)                                                                                       | B   | R   |         |
| /null  | 1   | Category (e.g., `0x00` = Power/Reset)                                                                                       | B   | R   |         |
| /null  | 1   | Reason (e.g., `0x02` = Battery)                                                                                               | B   | R   |         |
| /null  | 1   | Reason Detail (e.g., `0x01` = Power Down Imminent)                                                                          | B   | R   |         |
| /null  | 1   | Reserved (set to `0x00`)                                                                                                    | B   | R   |         |
| 83     | var | Additional Detail (if present)                                                                                             |     | O   |         |
| 84     | var | Notification Payload                                                                                                       | B   | O   |         |
| 9E     | var | Reserved                                                                                                                   | B   | O   |         |

#### Data File Message

### **Table 14 - Data File Message Format**

| Tag   | Len | Value / Description                                                                                                          | Typ | Req | Default |
|--------|-----|-------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
|        |     | **Start of Message** `0xAA`                                                                                                   |     |     |         |
|        |     | **API Framework Version** `0x00` - `0x02`                                                                                    |     |     |         |
| 81     | 08  | Message Information                                                                                                          | B   | R   |         |
| /null  | (1) | Message Type & Direction: `0x04` = Host→Device File, `0x84` = Device→Host File                                               | B   | R   |         |
| /null  | (1) | Message Reference Number                                                                                                     | B   | R   |         |
| /null  | (2) | Command Number that prompted this message                                                                                   | B   | R   |         |
| /null  | (4) | File Type as defined in Command Group 0xD8nn                                                                                 | B   | R   |         |
| 84     | var | File Payload                                                                                                                | B   | R   |         |

### **Table 15 - Data File Message Example**

| Example (Hex) |
|---------------|
| AA 00 81 08 84 08 D8 21 00 00 00 01 84 40 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F 20 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E 2F 30 31 32 33 34 35 36 37 38 39 3A 3B 3C 3D 3E 3F |


