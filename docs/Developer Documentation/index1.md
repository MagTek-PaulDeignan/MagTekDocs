---
title: DynaFlex Family Programmer's Manual
layout: home
---
## [1.0 Introduction](#10-introduction)

---

### [1.1 About This Document](#11-about-this-document)

This document describes communication methods with Secure Card Reader Authenticator (SCRA) devices and PIN Entry Devices (PED) implementing the MagTek Messaging Schema (MMS). Devices include DynaFlex, DynaFlex II Go, and DynaProx. It defines formatting conventions, such as bold text for emphasis and TLV (Tag-Length-Value) encoding, detailed in [section 3.2.1](#321-tlv-encoding).

### [1.2 About Terminology](#12-about-terminology)

- **Device**: Refers to SCRA or PED units. Device capabilities vary; see [Table 1.5.1 - Device Features](#table-161---device-features).
- **Host**: General-purpose hardware connected to a device (e.g., PC, tablet). May include host software.
- **User**: Categorized into cardholder, operator, or developer/administrator.
- **Solution**: The complete system including devices, hosts, software, firmware, and environment.

### [1.3 About SDKs and Sample Code](#13-about-sdks-and-sample-code)

MagTek offers SDKs for multiple platforms:

**SDK Manuals:**

| Document Number | Description                                        |
| --------------- | -------------------------------------------------- |
| D998200380      | MagTek Universal SDK Programmer’s Manual (.NET)    |
| D998200381      | MagTek Universal SDK Programmer’s Manual (C++)     |
| D998200385      | MagTek Universal SDK Programmer’s Manual (Java)    |
| D998200386      | MagTek Universal SDK Programmer’s Manual (iOS)     |
| D998200387      | MagTek Universal SDK Programmer’s Manual (Android) |
| D998200388      | MagTek Universal SDK Programmer’s Manual (macOS)   |

**SDK Packages:**

| Part Number | Description                                    |
| ----------- | ---------------------------------------------- |
| 1000007351  | MagTek Universal SDK for MMS Devices (Windows) |
| 1000007352  | MagTek Universal SDK for MMS Devices (Android) |
| 1000007353  | MagTek Universal SDK for MMS Devices (iOS)     |
| 1000007354  | MagTek Universal SDK for MMS Devices (macOS)   |

Developers can use SDK APIs or communicate directly with devices via platform APIs (e.g., Windows USB HID driver).

### [1.4 About Connections and Data Formats](#14-about-connections-and-data-formats)

Devices support varied connections: USB HID, WLAN, Bluetooth LE, RS-232, Apple Lightning, and more. Compatibility per device is shown in [Table 1.4.1 - Device Connection Types / Data Formats](#table-141---device-connection-types--data-formats).

**Table 1.4.1 - Device Connection Types / Data Formats** {#table-141---device-connection-types--data-formats}

| Product / Connection            | Bluetooth® LE GATT | RS 232 / UART | USB HID | WLAN | iAP2     | Ethernet |
| ------------------------------- | ------------------ | ------------- | ------- | ---- | -------- | -------- |
| DynaFlex with USB Only          |                    |               | HID     |      |          |          |
| DynaFlex w/Bluetooth® LE        | GATT               |               | HID     |      |          |          |
| DynaFlex Pro with USB Only      |                    |               | HID     |      |          |          |
| DynaFlex Pro w/Bluetooth® LE    | GATT               |               | HID     |      |          |          |
| DynaFlex Pro w/WLAN             |                    |               | HID     | WLAN |          |          |
| DynaFlex Pro w/Ethernet         |                    |               | HID     |      |          | Ethernet |
| DynaProx                        |                    | SLIP          | HID     |      | iAP2-USB |          |
| DynaFlex II with USB Only       |                    |               | HID     |      |          |          |
| DynaFlex II w/Bluetooth® LE     | GATT               |               | HID     |      |          |          |
| DynaFlex II PED with USB Only   |                    |               | HID     |      |          |          |
| DynaFlex II PED w/Bluetooth® LE | GATT               |               | HID     |      |          |          |
| DynaFlex II PED w/WLAN          |                    |               | HID     | WLAN |          |          |
| DynaFlex II PED w/Ethernet      |                    |               | HID     |      |          | Ethernet |
| DynaFlex II Go with USB Only    |                    |               | HID     |      | iAP2-USB |          |
| DynaFlex II Go w/Bluetooth® LE  | GATT               |               | HID     |      | iAP2-USB |          |

### [1.5 About Device Features](#15-about-device-features)

Device-specific features impact command availability and behavior. These include support for MSR, EMV (contact/contactless), manual card entry, barcode reader, LED types, display, power options, banking functions, and session management.

**Table 1.5.1 - Device Features**

| Feature / Product       | DynaFlex II GO | DynaFlex USB | DynaFlex BLE | DynaFlex Pro USB | DynaFlex Pro BLE | DynaFlex Pro WLAN | DynaFlex Pro Ethernet | DynaProx | DynaFlex II USB | DynaFlex II BLE | DynaFlex II PED USB | DynaFlex II PED BLE | DynaFlex II PED WLAN | DynaFlex II PED Ethernet |
| ----------------------- | -------------- | ------------ | ------------ | ---------------- | ---------------- | ----------------- | --------------------- | -------- | --------------- | --------------- | ------------------- | ------------------- | -------------------- | ------------------------ |
| MSR                     | Y              | Y            | Y            | Y                | Y                | Y                 | Y                     | N        | Y               | Y               | Y                   | Y                   | Y                    | Y                        |
| EMV Contact             | Y              | Y            | Y            | Y                | Y                | Y                 | Y                     | N        | Y               | Y               | Y                   | Y                   | Y                    | Y                        |
| EMV Contactless         | Y              | Y            | Y            | Y                | Y                | Y                 | Y                     | Y        | Y               | Y               | Y                   | Y                   | Y                    | Y                        |
| MCE (Manual Card Entry) | N              | N            | N            | Y                | Y                | Y                 | Y                     | N        | N               | N               | Y                   | Y                   | Y                    | Y                        |
| BCR (Barcode Reader)    | Y              | Y            | Y            | Y                | Y                | Y                 | Y                     | Y        | Y               | Y               | Y                   | Y                   | Y                    | Y                        |
| LED RGBx4               | 1              | Y            | Y            | Y                | Y                | Y                 | Y                     | N        | Y               | Y               | Y                   | Y                   | Y                    | Y                        |
| LED Monox4              | Y              | N            | N            | N                | N                | N                 | N                     | Y        | N               | N               | N                   | N                   | N                    | N                        |
| Touch                   | N              | N            | N            | Y                | Y                | Y                 | Y                     | N        | N               | N               | Y                   | Y                   | Y                    | Y                        |
| No Touch                | Y              | Y            | Y            | N                | N                | N                 | N                     | Y        | Y               | Y               | N                   | N                   | N                    | N                        |
| Display                 | N              | N            | N            | Y                | Y                | Y                 | Y                     | N        | N               | N               | Y                   | Y                   | Y                    | Y                        |
| No Display              | Y              | Y            | Y            | N                | N                | N                 | N                     | Y        | Y               | Y               | N                   | N                   | N                    | N                        |
| Battery Power           | Y              | N            | Y            | N                | Y                | Y                 | Y                     | N        | N               | Y               | N                   | Y                   | Y                    | Y                        |
| Banking Functions       | N              | N            | N            | Y                | Y                | Y                 | Y                     | N        | N               | N               | Y                   | Y                   | Y                    | Y                        |
| Session Management      | N              | N            | N            | N                | N                | Y                 | N                     | N        | N               | N               | N                   | N                   | Y                    | N                        |
| Apple VAS               | Y              | N            | N            | N                | N                | N                 | N                     | Y        | Y               | Y               | Y                   | Y                   | Y                    | Y                        |
| Google Wallet Smart Tap | Y              | N            | N            | N                | N                | N                 | N                     | Y        | Y               | Y               | Y                   | Y                   | Y                    | Y                        |
| Flexible UI             | N              | N            | N            | N                | N                | N                 | N                     | N        | N               | N               | Y                   | Y                   | Y                    | Y                        |
| Common Kernel           | N              | N            | N            | N                | N                | N                 | N                     | Y        | Y               | Y               | Y                   | Y                   | Y                    | Y                        |
| Card Emulation          | Y              | N            | N            | N                | N                | N                 | N                     | Y        | N               | N               | N                   | N                   | N                    | N                        |

## <a name="2.0-connection-types"></a>[2.0 Connection Types](#2.0-connection-types)

Details for each supported connection type for MMS devices:

### <a name="2.1-usb-connections"></a>[2.1 USB Connections (USB Only)](#2.1-usb-connections)

- USB spec 1.1, HID class 1.1
- Vendor ID: `0x0801`, with product-specific PIDs
- HID Communication:
  - **Output Reports**: Host → Device
  - **Input Reports**: Device → Host
- Usage Page: `0xFF00`, Usage ID: `0x0020`

#### <a name="2.1.1-usb-message-formats"></a>[2.1.1 USB Message Formats](#2.1.1-usb-message-formats)

- **Single Packet**: ≤62 bytes
- **Multi-Packet**: Head, Middle, Tail, and Cancel formats

### <a name="2.2-wireless-lan"></a>[2.2 Wireless LAN (WLAN Only)](#2.2-wireless-lan)

- Uses WebSocket protocol ([RFC 6455](https://tools.ietf.org/html/rfc6455))
- Device joins AP and opens WebSocket listener
- Use binary WebSocket frames for command messages

### <a name="2.3-ethernet"></a>[2.3 Ethernet (Ethernet Only)](#2.3-ethernet)

(To be expanded in future revisions)

### <a name="2.4-bluetooth-le"></a>[2.4 Bluetooth® LE (Bluetooth® LE Only)](#2.4-bluetooth-le)

- GATT Characteristics:
  - **Service UUID**: `0cba14b7-ff24-47b0-be09-26440538530c`
  - **Host Message UUID**: `47f05ffa-5909-4969-bc57-250d47e874e5`
  - **Device Message UUID**: `fed49118-c7e2-4a61-9ed5-e6dd65c3071b`
- Protocol structure:
  - Byte 1: Message counter
  - Byte 2: PDU counter
  - Byte 3+: Message length and content

### <a name="2.5-rs232-uart"></a>[2.5 RS-232/UART (SLIP Only)](#2.5-rs232-uart)

- **Baud**: 115200, 8N1, no flow control
- **Encapsulation via SLIP format**:
  - Start/end delimiter: `0xC0`
  - Escape sequences for `0xC0` and `0xDB`

See [Section 2.6 - SLIP Format](#2.6-slip-format).

### <a name="2.6-slip-format"></a>[2.6 SLIP Format](#2.6-slip-format)

Encapsulation used in RS-232 connections. Adds start and end delimiters, length, and optional escape bytes. Related to [Section 2.5 - RS-232/UART](#2.5-rs232-uart).

### <a name="2.7-apple-iap2"></a>[2.7 Apple iAP2 (iAP2 Only)](#2.7-apple-iap2)

- Requires iOS app using Apple ExternalAccessory framework
- Example App: Apple’s `EADemo`
- Uses AppBundleID and platform APIs for data exchange

## <a name="3.0-messages"></a>[3.0 Messages](#3.0-messages)

### <a name="3.1-message-structure"></a>[3.1 Message Structure](#3.1-message-structure)
Messages sent to and from the device follow a structured format. Messages are composed of a header, payload, and optional TLV (Tag-Length-Value) structures.

[Table 3.1.1 – Message Structure](#table-3.1.1-message-structure)

| Field         | Length (Bytes) | Description                              |
|---------------|----------------|------------------------------------------|
| Command Code  | 2              | Identifies the command                   |
| Payload       | Variable       | Command-specific data                    |
| Checksum      | 2              | CRC-16 of the command and payload        |

### <a name="3.2-tlv-format"></a>[3.2 TLV Format](#3.2-tlv-format)
The TLV format is used to encode additional data in a structured way.

[Table 3.2.1 – TLV Format](#table-3.2.1-tlv-format)

| Field | Length (Bytes) | Description            |
|--------|----------------|------------------------|
| Tag    | 1–3            | Identifies the data    |
| Length | 1–2            | Length of the value    |
| Value  | Variable       | Actual data            |

Nested TLVs are supported, meaning a Value may contain additional TLVs.

### <a name="3.3-command-categories"></a>[3.3 Command Categories](#3.3-command-categories)
Commands are organized into functional categories:

- **Device Management**: Reset, Update Firmware, etc.
- **Security**: Key injection, MAC generation, etc.
- **Transaction**: Start, approve, cancel, etc.
- **Diagnostic**: Get status, echo, etc.

### <a name="3.4-example-command"></a>[3.4 Example Command](#3.4-example-command)
To reset the device:

```text
Command Code: 0x1F01
Payload: None
Checksum: Calculated over Command Code
```

### <a name="3.5-response-messages"></a>[3.5 Response Messages](#3.5-response-messages)
Response messages echo the Command Code and include a status field.

[Table 3.5.1 – Response Message Format](#table-3.5.1-response-message-format)

| Field         | Length (Bytes) | Description                                |
|---------------|----------------|--------------------------------------------|
| Command Code  | 2              | Mirrors request                            |
| Status Code   | 2              | Indicates success or error                 |
| Payload       | Variable       | Optional, command-specific data            |
| Checksum      | 2              | CRC-16 of the entire response              |

### <a name="3.6-status-codes"></a>[3.6 Status Codes](#3.6-status-codes)

[Table 3.6.1 – Status Codes](#table-3.6.1-status-codes)

| Status Code | Meaning                        |
|--------------|---------------------------------|
| 0x0000       | Success                        |
| 0x0001       | Unknown Command                |
| 0x0002       | Invalid Parameters             |
| 0x0003       | CRC Error                      |
| 0x0004       | Device Busy                    |
| 0x0005       | Permission Denied              |

### <a name="3.7-message-encoding"></a>[3.7 Message Encoding](#3.7-message-encoding)
Messages are encoded as binary data using little-endian format for multi-byte fields. The CRC is calculated using the standard CRC-16-CCITT algorithm.

### <a name="3.8-timeouts-and-retries"></a>[3.8 Timeouts and Retries](#3.8-timeouts-and-retries)
The host should implement timeouts for commands. If no response is received within the configured timeout window (typically 2 seconds), the host may retry the command up to 3 times before declaring the device unresponsive.

---

### Table Anchors
- <a name="table-3.1.1-message-structure"></a>Table 3.1.1 – Message Structure
- <a name="table-3.2.1-tlv-format"></a>Table 3.2.1 – TLV Format
- <a name="table-3.5.1-response-message-format"></a>Table 3.5.1 – Response Message Format
- <a name="table-3.6.1-status-codes"></a>Table 3.6.1 – Status Codes

## <a name="section-4-data-types-tlv"></a>[Section 4: Data Types (TLV)](#section-4-data-types-tlv)

This section describes all the data types supported in the TLV format. Each TLV has a Tag field (1 byte), followed by a Length field (1 byte), followed by the Value field (up to 255 bytes).

All values are stored in little-endian format (least significant byte first).

Each section below defines a unique tag identifier and explains the format, meaning, and usage.

### <a name="41-tlv_device_serial"></a>[4.1 TLV_DEVICE_SERIAL](#41-tlv_device_serial)
- **Tag:** `0x01`
- **Length:** 8
- **Value:** 8-byte unsigned integer (Little-endian).
- **Example:** `0x01 08 78 56 34 12 00 00 00 00` (represents serial number `0x0000000012345678`)

### <a name="42-tlv_model_name"></a>[4.2 TLV_MODEL_NAME](#42-tlv_model_name)
- **Tag:** `0x02`
- **Length:** Length of the ASCII string (1–255)
- **Value:** ASCII string (not null-terminated)
- **Example:** `0x02 07 44 79 6E 61 50 72 6F` (represents "DynaPro")

### <a name="43-tlv_fw_version"></a>[4.3 TLV_FW_VERSION](#43-tlv_fw_version)
- **Tag:** `0x03`
- **Length:** 3
- **Value:** 3-byte version: Major.Minor.Patch (e.g., `0x02 01 0A` = 2.1.10)
- **Example:** `0x03 03 02 01 0A`

### <a name="44-tlv_hw_revision"></a>[4.4 TLV_HW_REVISION](#44-tlv_hw_revision)
- **Tag:** `0x04`
- **Length:** 2
- **Value:** 2-byte BCD (Binary-coded decimal), representing hardware revision (e.g., "01.02" is `0x01 0x02`)
- **Example:** `0x04 02 01 02`

### <a name="45-tlv_supported_features"></a>[4.5 TLV_SUPPORTED_FEATURES](#45-tlv_supported_features)
- **Tag:** `0x05`
- **Length:** Variable (usually 1–4 bytes)
- **Value:** Bitmask representing supported features.

| Bit | Feature             |
|-----|----------------------|
| 0   | NFC Support          |
| 1   | Bluetooth Enabled    |
| 2   | Wi-Fi Capable        |
| 3   | Secure Boot Enabled  |
| 4–7 | Reserved             |

- **Example:** `0x05 01 0B` → NFC, Bluetooth, and Secure Boot are enabled.

### <a name="46-tlv_manufacturer"></a>[4.6 TLV_MANUFACTURER](#46-tlv_manufacturer)
- **Tag:** `0x06`
- **Length:** Variable
- **Value:** ASCII string of manufacturer name
- **Example:** `0x06 07 4E 6F 72 74 65 6C 20` → "Nortel "

### <a name="47-tlv_production_date"></a>[4.7 TLV_PRODUCTION_DATE](#47-tlv_production_date)
- **Tag:** `0x07`
- **Length:** 4
- **Value:** 4-byte date in format YYYYMMDD as BCD
- **Example:** `0x07 04 20 23 12 31` → December 31, 2023

### <a name="48-tlv_certificate"></a>[4.8 TLV_CERTIFICATE](#48-tlv_certificate)
- **Tag:** `0x08`
- **Length:** Variable (length of the certificate in bytes)
- **Value:** Binary certificate data (DER encoded)

### <a name="49-tlv_device_type"></a>[4.9 TLV_DEVICE_TYPE](#49-tlv_device_type)
- **Tag:** `0x09`
- **Length:** 1
- **Value:** Enum

| Value | Device Type   |
|--------|----------------|
| 0x00   | Unknown        |
| 0x01   | Mobile         |
| 0x02   | Terminal       |
| 0x03   | Reader         |

- **Example:** `0x09 01 02` → Terminal

### <a name="410-tlv_encryption_key"></a>[4.10 TLV_ENCRYPTION_KEY](#410-tlv_encryption_key)
- **Tag:** `0x0A`
- **Length:** 16
- **Value:** 128-bit AES key

### <a name="411-tlv_mac_address"></a>[4.11 TLV_MAC_ADDRESS](#411-tlv_mac_address)
- **Tag:** `0x0B`
- **Length:** 6
- **Value:** 6-byte MAC address
- **Example:** `0x0B 06 00 1A 2B 3C 4D 5E`

### <a name="412-tlv_ip_address"></a>[4.12 TLV_IP_ADDRESS](#412-tlv_ip_address)
- **Tag:** `0x0C`
- **Length:** 4 (IPv4) or 16 (IPv6)
- **Value:** IP address in binary
- **Example (IPv4):** `0x0C 04 C0 A8 01 01` → 192.168.1.1

### <a name="413-tlv_port"></a>[4.13 TLV_PORT](#413-tlv_port)
- **Tag:** `0x0D`
- **Length:** 2
- **Value:** 2-byte port number (little-endian)
- **Example:** `0x0D 02 1F 90` → 8080

### <a name="414-tlv_location"></a>[4.14 TLV_LOCATION](#414-tlv_location)
- **Tag:** `0x0E`
- **Length:** Variable
- **Value:** UTF-8 encoded string of physical device location

### <a name="415-tlv_timezone"></a>[4.15 TLV_TIMEZONE](#415-tlv_timezone)
- **Tag:** `0x0F`
- **Length:** 1
- **Value:** Signed integer representing GMT offset (e.g., -8 for PST)
- **Example:** `0x0F 01 F8` → -8

### <a name="416-tlv_language"></a>[4.16 TLV_LANGUAGE](#416-tlv_language)
- **Tag:** `0x10`
- **Length:** 2
- **Value:** 2-letter ISO 639-1 language code
- **Example:** `0x10 02 65 6E` → "en" (English)

### <a name="417-tlv_country"></a>[4.17 TLV_COUNTRY](#417-tlv_country)
- **Tag:** `0x11`
- **Length:** 2
- **Value:** 2-letter ISO 3166-1 alpha-2 country code
- **Example:** `0x11 02 55 53` → "US"

### <a name="418-tlv_currency"></a>[4.18 TLV_CURRENCY](#418-tlv_currency)
- **Tag:** `0x12`
- **Length:** 3
- **Value:** 3-letter ISO 4217 currency code
- **Example:** `0x12 03 55 53 44` → "USD"

### <a name="419-tlv_decimal_separator"></a>[4.19 TLV_DECIMAL_SEPARATOR](#419-tlv_decimal_separator)
- **Tag:** `0x13`
- **Length:** 1
- **Value:** ASCII value of decimal separator character
- **Example:** `0x13 01 2E` → '.' (dot)

### <a name="420-tlv_thousand_separator"></a>[4.20 TLV_THOUSAND_SEPARATOR](#420-tlv_thousand_separator)
- **Tag:** `0x14`
- **Length:** 1
- **Value:** ASCII value of thousand separator character
- **Example:** `0x14 01 2C` → ',' (comma)

### <a name="421-tlv_date_format"></a>[4.21 TLV_DATE_FORMAT](#421-tlv_date_format)
- **Tag:** `0x15`
- **Length:** Variable
- **Value:** ASCII string representing format, e.g., "MM/DD/YYYY"

### <a name="422-tlv_time_format"></a>[4.22 TLV_TIME_FORMAT](#422-tlv_time_format)
- **Tag:** `0x16`
- **Length:** Variable
- **Value:** ASCII string, e.g., "HH:mm:ss" or "hh:mm a"

### <a name="423-tlv_supported_languages"></a>[4.23 TLV_SUPPORTED_LANGUAGES](#423-tlv_supported_languages)
- **Tag:** `0x17`
- **Length:** Multiple of 2
- **Value:** List of 2-letter language codes
- **Example:** `0x17 06 65 6E 66 72 65 73` → "en", "fr", "es"

### <a name="424-tlv_supported_countries"></a>[4.24 TLV_SUPPORTED_COUNTRIES](#424-tlv_supported_countries)
- **Tag:** `0x18`
- **Length:** Multiple of 2
- **Value:** List of ISO 2-letter country codes
- **Example:** `0x18 06 55 53 43 41 4D 58` → "US", "CA", "MX"

### <a name="425-tlv_supported_currencies"></a>[4.25 TLV_SUPPORTED_CURRENCIES](#425-tlv_supported_currencies)
- **Tag:** `0x19`
- **Length:** Multiple of 3
- **Value:** List of ISO 3-letter currency codes
- **Example:** `0x19 09 55 53 44 45 55 52 47 42 50` → "USD", "EUR", "GBP"

### <a name="426-tlv_device_status"></a>[4.26 TLV_DEVICE_STATUS](#426-tlv_device_status)
- **Tag:** `0x1A`
- **Length:** 1
- **Value:** Enum: 0x00=Inactive, 0x01=Active, 0x02=Error

### <a name="427-tlv_last_update"></a>[4.27 TLV_LAST_UPDATE](#427-tlv_last_update)
- **Tag:** `0x1B`
- **Length:** 4
- **Value:** UNIX timestamp (32-bit little-endian)

### <a name="428-tlv_signature"></a>[4.28 TLV_SIGNATURE](#428-tlv_signature)
- **Tag:** `0x1C`
- **Length:** 64
- **Value:** ECDSA signature (binary)

### <a name="429-tlv_checksum"></a>[4.29 TLV_CHECKSUM](#429-tlv_checksum)
- **Tag:** `0x1D`
- **Length:** 4
- **Value:** CRC-32 checksum (little-endian)

### <a name="430-tlv_card_emulation"></a>[4.30 TLV_CARD_EMULATION](#430-tlv_card_emulation)
- **Tag:** `0x1E`
- **Length:** 1
- **Value:** Enum: 0x00=None, 0x01=HCE, 0x02=SE

| Value | Card Emulation Mode       |
|--------|----------------------------|
| 0x00   | None                       |
| 0x01   | HCE (Host Card Emulation) |
| 0x02   | SE (Secure Element)       |

This concludes the list of supported TLV data types.


