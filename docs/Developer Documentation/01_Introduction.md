---
title: Introduction
layout: home
parent: DynaFlex Family Programmer's Manual
nav_order: 1
---
## Introduction

---

### Table of Contents


  - [About This Document](#about-this-document)
  - [About Terminology](#about-terminology)
  - [About SDKs and Sample Code](#about-sdks-and-sample-code)
  - [About Connections and Data Formats](#about-connections-and-data-formats)
  - [About Device Features](#about-device-features)

---

### About This Document

This document describes how to communicate with Secure Card Reader Authenticator (SCRA) devices which implement MagTek Messaging Schema (MMS) and the DynaFlex family, DynaFlex II Go and DynaProx system architecture.

This document also describes how to communicate with PIN Entry Devices (PED) which implement MagTek Messaging Schema (MMS) and the DynaFlex/DynaProx family system architecture. (PED ONLY)

The document uses **bold face** to:

- Highlight terms / concepts being formally defined in the current sentence / paragraph
- Highlight important distinguishing keywords in sentences
- Indicate hyperlinks to other sections / tables

The document uses a small number of annotation standards that are important to understand:

- Hexadecimal values are prefixed with **0x** unless the context clearly indicates an un-prefixed number is hexadecimal.
- Binary values are prefixed with **0b** unless the context clearly indicates the value is binary.
- Decimal values are not prefixed unless required for clarity, in which case the prefix is **0d**.

The standard documented by this document makes extensive use of Tag-Length-Value encoding. Section [3.2.1 - Tag-Length-Value (TLV) Encoding](#321-tag-length-value-tlv-encoding) describes how to encode and decode TLV, and how to read the tables in this document that describe TLV data objects.

### About Terminology

- **Device**: Refers to the Secure Card Reader Authenticator (SCRA) or PIN Entry Device (PED) that receives and responds to the command set specified in this document. Refer to [Table 2 - Device Features](#table-2---device-features) to determine a device’s specific capabilities. Not all devices support PIN entry.
- **Host**: The general-purpose hardware the device is connected or paired to (e.g., PC, Mac, smartphone). May include host software.
- **User**: Categorized as cardholder, operator (e.g., cashier), or developer/administrator (e.g., integrator).
- **Host Software**: Software running on the host that interacts with the device.
- **Solution**: The complete system, including devices, hosts, host software, firmware, configuration, physical setup, user experience, and documentation.

### About SDKs and Sample Code

MagTek provides SDKs for many programming languages and platforms. These include APIs that wrap device communication and abstract platform-specific implementation details.

**SDK Manuals:**

- D998200380: MagTek Universal SDK Programmer’s Manual (.NET)
- D998200381: MagTek Universal SDK Programmer’s Manual (C++)
- D998200385: MagTek Universal SDK Programmer’s Manual (Java)
- D998200386: MagTek Universal SDK Programmer’s Manual (iOS)
- D998200387: MagTek Universal SDK Programmer’s Manual (Android)
- D998200388: MagTek Universal SDK Programmer’s Manual (macOS)

**SDK Packages:**

- 1000007351: SDK for MMS Devices (Windows)
- 1000007352: SDK for MMS Devices (Android)
- 1000007353: SDK for MMS Devices (iOS)
- 1000007354: SDK for MMS Devices (macOS)

These SDKs include:

- Functions for sending direct device commands
- Wrappers for simplifying development
- Sample code to demonstrate communication

Developers may also communicate directly with devices using native libraries. Example: using Visual C++ with Windows USB HID APIs. MagTek provides additional sample applications for testing and development.

### About Connections and Data Formats

MMS devices support multiple connection types:

- USB HID
- WLAN
- Bluetooth / Bluetooth LE
- RS-232 / UART
- Apple Lightning

Connection availability and supported data formats are device-dependent.

**[Table 1 - Device Connection Types / Data Formats](#table-1---device-connection-types--data-formats)**

| Product / Connection              | Bluetooth® LE GATT | RS 232 / UART | USB HID | WLAN | iAP2     | Ethernet |
|----------------------------------|----------------------|---------------|---------|------|----------|----------|
| DynaFlex with USB Only           |                      |               | HID     |      |          |          |
| DynaFlex w/Bluetooth® LE        | GATT                 |               | HID     |      |          |          |
| DynaFlex Pro with USB Only       |                      |               | HID     |      |          |          |
| DynaFlex Pro w/Bluetooth® LE    | GATT                 |               | HID     |      |          |          |
| DynaFlex Pro w/WLAN              |                      |               | HID     | WLAN |          |          |
| DynaFlex Pro w/Ethernet          |                      |               | HID     |      |          | Ethernet |
| DynaProx                         |                      | SLIP          | HID     |      | iAP2-USB |          |
| DynaFlex II with USB Only        |                      |               | HID     |      |          |          |
| DynaFlex II w/Bluetooth® LE     | GATT                 |               | HID     |      |          |          |
| DynaFlex II PED with USB Only    |                      |               | HID     |      |          |          |
| DynaFlex II PED w/Bluetooth® LE | GATT                 |               | HID     |      |          |          |
| DynaFlex II PED w/WLAN           |                      |               | HID     | WLAN |          |          |
| DynaFlex II PED w/Ethernet       |                      |               | HID     |      |          | Ethernet |
| DynaFlex II Go with USB Only     |                      |               | HID     |      | iAP2-USB |          |
| DynaFlex II Go w/Bluetooth® LE  | GATT                 |               | HID     |      | iAP2-USB |          |

### About Device Features

Not all features are available on every device. Use the table below to understand which features apply to each model.

**[Table 2 - Device Features](#table-2---device-features)**

| Feature / Product       | DynaFlex II GO | DynaFlex USB | DynaFlex BLE | DynaFlex Pro USB | DynaFlex Pro BLE | DynaFlex Pro WLAN | DynaFlex Pro Ethernet | DynaProx | DynaFlex II USB | DynaFlex II BLE | DynaFlex II PED USB | DynaFlex II PED BLE | DynaFlex II PED WLAN | DynaFlex II PED Ethernet |
|------------------------|----------------|---------------|---------------|------------------|-------------------|--------------------|------------------------|----------|------------------|------------------|----------------------|----------------------|------------------------|---------------------------|
| MSR                   | Y              | Y             | Y             | Y                | Y                 | Y                  | Y                      | N        | Y                | Y                | Y                    | Y                    | Y                        | Y                         |
| EMV Contact           | Y              | Y             | Y             | Y                | Y                 | Y                  | Y                      | N        | Y                | Y                | Y                    | Y                    | Y                        | Y                         |
| EMV Contactless       | Y              | Y             | Y             | Y                | Y                 | Y                  | Y                      | Y        | Y                | Y                | Y                    | Y                    | Y                        | Y                         |
| MCE (Manual Entry)    | N              | N             | N             | Y                | Y                 | Y                  | Y                      | N        | N                | N                | Y                    | Y                    | Y                        | Y                         |
| BCR                   | Y              | Y             | Y             | Y                | Y                 | Y                  | Y                      | Y        | Y                | Y                | Y                    | Y                    | Y                        | Y                         |
| LED RGBx4             | 1              | Y             | Y             | Y                | Y                 | Y                  | Y                      | N        | Y                | Y                | Y                    | Y                    | Y                        | Y                         |
| LED Monox4            | Y              | N             | N             | N                | N                 | N                  | N                      | Y        | N                | N                | N                    | N                    | N                        | N                         |
| Touch                 | N              | N             | N             | Y                | Y                 | Y                  | Y                      | N        | N                | N                | Y                    | Y                    | Y                        | Y                         |
| No Touch              | Y              | Y             | Y             | N                | N                 | N                  | N                      | Y        | Y                | Y                | N                    | N                    | N                        | N                         |
| Display               | N              | N             | N             | Y                | Y                 | Y                  | Y                      | N        | N                | N                | Y                    | Y                    | Y                        | Y                         |
| No Display            | Y              | Y             | Y             | N                | N                 | N                  | N                      | Y        | Y                | Y                | N                    | N                    | N                        | N                         |
| Battery Power         | Y              | N             | Y             | N                | Y                 | Y                  | Y                      | N        | N                | Y                | N                    | Y                    | Y                        | Y                         |
| Banking Functions     | N              | N             | N             | Y                | Y                 | Y                  | Y                      | N        | N                | N                | Y                    | Y                    | Y                        | Y                         |
| Session Management    | N              | N             | N             | N                | N                 | Y                  | N                      | N        | N                | N                | N                    | N                    | Y                        | N                         |
| Apple VAS             | Y              | N             | N             | N                | N                 | N                  | N                      | Y        | Y                | Y                | Y                    | Y                    | Y                        | Y                         |
| Google Wallet SmartTap| Y              | N             | N             | N                | N                 | N                  | N                      | Y        | Y                | Y                | Y                    | Y                    | Y                        | Y                         |
| Flexible UI           | N              | N             | N             | N                | N                 | N                  | N                      | N        | N                | N                | Y                    | Y                    | Y                        | Y                         |
| Common Kernel         | N              | N             | N             | N                | N                 | N                  | N                      | Y        | Y                | Y                | Y                    | Y                    | Y                        | Y                         |
| Card Emulation        | Y              | N             | N             | N                | N                 | N                  | N                      | Y        | Y                | Y                | Y                    | Y                    | Y                        | Y                         |
