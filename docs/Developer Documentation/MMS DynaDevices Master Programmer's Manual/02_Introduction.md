---
title: Introduction
layout: default
parent: MMS Dyna Devices Master Programmer's Manual
nav_order: 2
---

# Introduction
Introduction

## About This Document

This document describes how to communicate with Secure Card Reader Authenticator
(SCRA) devices which implement MagTek Messaging Schema (MMS) and the DynaFlex
family, DynaFlex II Go and DynaProx system architecture.

This document also describes how to communicate with PIN Entry Devices (PED)
which implement MagTek Messaging Schema (MMS) and the DynaFlex/DynaProx family
system architecture. (PED ONLY)

The document uses **bold face** to:

-   Highlight terms / concepts being formally defined in the current sentence /
    paragraph
-   Highlight important distinguishing keywords in sentences
-   Indicate hyperlinks to other sections / tables

The document uses a small number of annotation standards that are important to
understand:

-   Hexadecimal values are prefixed with **0x** unless the context clearly
    indicates an un-prefixed number is hexadecimal (for example, TLV tags,
    lengths, and values are always assumed to be hex).
-   Binary values are prefixed with **0b** unless the context clearly indicates
    the value is binary.
-   Decimal values are not prefixed unless required for clarity, in which case
    the prefix is **0d**.

The standard documented by this document makes extensive use of Tag-Length-Value
encoding. Section **3.2.1 Tag-Length-Value (TLV) Encoding** describes how to
encode and decode TLV, and how to read the tables in this document that describe
TLV data objects.

## About Terminology

The general terms “device” and “host” are used in different, often incompatible
ways in a multitude of specifications and contexts. For instance, the term
"host" can signify different things depending on the context—such as USB
communication versus networked financial transaction processing. In this
document, "device" and "host" are defined specifically as follows:

-   **Device** refers to the Secure Card Reader Authenticator (SCRA) or PIN
    Entry Device (PED) that receives and responds to the command set specified
    in this document. Refer to **Table 3 - Device Features**, to determine a
    device’s specific capabilities, not all devices support PIN entry. Devices
    include DynaFlex, DynaProx, DynaFlex II, and so on.
-   **Host** refers to the piece of general-purpose electronic equipment the
    device is connected or paired to, which can send data to and receive data
    from the device. Host types include PC and Mac computers/laptops, tablets,
    smartphones, teletype terminals, and even test harnesses. In many cases the
    host may have custom software installed on it that communicates with the
    device. When “host” must be used differently, it is qualified as something
    specific, such as “acquirer host” or “USB host.”

Similarly, the word “user” is used in different ways in different contexts. This
document separates users into more descriptive categories:

-   The **cardholder**
-   The **operator** (such as a cashier, bank teller, customer service
    representative, or server), and
-   The **developer** or the **administrator** (such as an integrator
    configuring the device for the first time).

Because some connection types, payment brands, and other vocabulary name spaces
(notably Bluetooth® LE, EMV, smart phones, and more recent versions of Windows)
use very specific meanings for the term “Application,” this document favors the
term **host software** to refer to software on the host that provides a user
interface for the operator.

The combination of device(s), host(s), host software, device firmware, device
configuration settings, physical mounting and environment, user experience, and
documentation is referred to as the **solution**.

## About SDKs and Sample Code

MagTek provides convenient SDKs and corresponding documentation for many
programming languages and operating systems. The API libraries included in the
SDKs wrap the details of the connection in an interface that conceptually
parallels the device’s internal operation, freeing software developers to focus
on the business logic, without having to deal with the complexities of platform
APIs for connecting to the various available connection types, communicating
using the various available protocols, and parsing the various available data
formats. Information about using MagTek wrapper APIs is available in separate
documentation, including:

-   **D998200380 MagTek Universal SDK Programmer’s Manual (Microsoft .NET)**
-   **D998200381 MagTek Universal SDK Programmer’s Manual (Microsoft C++ )**
-   **D998200385 MagTek Universal SDK Programmer’s Manual (Java)**
-   **D998200386 MagTek Universal SDK Programmer’s Manual (iOS)**
-   **D998200387 MagTek Universal SDK Programmer’s Manual (Android)**
-   **D998200388 MagTek Universal SDK Programmer’s Manual (macOS)**

The documentation is bundled with the SDKs themselves, which include:

-   **1000007351 MagTek Universal SDK for MMS Devices (Windows)**
-   **1000007352 MagTek Universal SDK for MMS Devices (Android)**
-   **1000007353 MagTek Universal SDK for MMS Devices (iOS)**
-   **1000007354 MagTek Universal SDK for MMS Devices (macOS)**

The SDKs and corresponding documentation include:

-   Functions for sending the direct commands described in this manual
-   Wrappers for commonly used commands that further simplify development
-   Sample source code to demonstrate how to communicate with the device using
    the direct commands described in this manual

To download the SDKs and documentation, search
[www.MagTek.com](http://www.magtek.com) for “SDK” and select the SDK and
documentation for the programming languages and platforms you need or contact
MagTek Support Services for assistance.

Software developers also have the option to revert to direct communication with
the device using libraries available in the chosen development framework. For
example, custom software written in Visual Basic or visual C++ may make API
calls to the standard Windows USB HID driver. This document provides information
and support for developing host software using that method.

MagTek has also developed sample software that demonstrates direct communication
with the device, which software developers can use to test the device and which
provides a starting point for developing other software. For more information,
see the MagTek web site, or contact your reseller or MagTek Support Services.

## About Connections and Data Formats

MMS products transmit data using a set of common data formats across a variety
of physical connection layers, which can include universal serial bus (USB)
acting as a vendor-defined HID device (“USB HID”), wireless LAN (WLAN),
Bluetooth®, Bluetooth® Low Energy (“Bluetooth® LE”), RS-232, Apple Lightning,
and so on. The set of available physical connection types and the data formats
available on each connection type is device dependent. **Table 2** shows the
physical connection types available on each product, and the data formats
supported on each connection type for that device. Details about connection
types and formats can be found in section **2 Connection Types**. Section
headings in this document include tags that indicate which connection types
and/or data formats they apply to.

Table 2 - Device Connection Types / Data Formats

| Product / Connection                                           | Bluetooth® LE GATT | RS232 / UART | USB HID | WLAN  | iAP2     | Ethernet |
|----------------------------------------------------------------|--------------------|--------------|---------|-------|----------|----------|
| DynaFlex with USB Only                                         |                    |              | HID     |       |          |          |
| DynaFlex w/Bluetooth® LE (MAGTEK INTERNAL ONLY FOR NOW)        | GATT               |              | HID     |       |          |          |
| DynaFlex Pro with USB Only                                     |                    |              | HID     |       |          |          |
| DynaFlex Pro w/Bluetooth® LE (MAGTEK INTERNAL ONLY FOR NOW)    | GATT               |              | HID     |       |          |          |
| DynaFlex Pro w/WLAN                                            |                    |              | HID     | WLAN  |          |          |
| DynaFlex Pro w/Ethernet (MAGTEK INTERNAL ONLY FOR NOW)         |                    |              | HID     |       |          | Ethernet |
| DynaProx                                                       |                    | SLIP         | HID     |       | iAP2-USB |          |
| DynaFlex II with USB Only                                      |                    |              | HID     |       |          |          |
| DynaFlex II w/Bluetooth® LE (MAGTEK INTERNAL ONLY FOR NOW)     | GATT               |              | HID     |       |          |          |
| DynaFlex II PED with USB Only                                  |                    |              | HID     |       |          |          |
| DynaFlex II PED w/Bluetooth® LE (MAGTEK INTERNAL ONLY FOR NOW) | GATT               |              | HID     |       |          |          |
| DynaFlex II PED w/WLAN                                         |                    |              | HID     | WLAN  |          |          |
| DynaFlex II PED w/Ethernet (MAGTEK INTERNAL ONLY FOR NOW)      |                    |              | HID     |       |          | Ethernet |
| DynaFlex II Go with USB Only                                   |                    |              | HID     |       | iAP2-USB |          |
| DynaFlex II Go w/Bluetooth® LE                                 | GATT               |              | HID     |       | iAP2-USB |          |

## About Device Features

Much of the information in this document is applicable to multiple devices. When
developing solutions that use a specific device or set of devices, integrators
must be aware of each device’s connection types, data formats, features, and
configuration options, which affect the availability and behavior of some
commands. **Table 3** provides a list of device features that may impact command
availability and behavior. All section headings in this document include tags
that indicate which features they apply to.

Table 3 - Device Features

| Feature / Product       | DynaFlex II GO | DynaFlex with USB Only | DynaFlex w/Bluetooth® LE | DynaFlex Pro with USB Only | DynaFlex Pro with Bluetooth® LE | DynaFlex Pro with WLAN | DynaFlex Pro with Ethernet | DynaProx | DynaFlex II with USB Only | DynaFlex II w/Bluetooth® LE | DynaFlex II PED with USB Only | DynaFlex II PED with Bluetooth® LE | DynaFlex II PED with WLAN | DynaFlex II PED with Ethernet |
|-------------------------|----------------|------------------------|--------------------------|----------------------------|---------------------------------|------------------------|----------------------------|----------|---------------------------|-----------------------------|-------------------------------|------------------------------------|---------------------------|-------------------------------|
| MSR                     | Y              | Y                      | Y                        | Y                          | Y                               | Y                      | Y                          | N        | Y                         | Y                           | Y                             | Y                                  | Y                         | Y                             |
| EMV Contact             | Y              | Y                      | Y                        | Y                          | Y                               | Y                      | Y                          | N        | Y                         | Y                           | Y                             | Y                                  | Y                         | Y                             |
| EMV Contactless         | Y              | Y                      | Y                        | Y                          | Y                               | Y                      | Y                          | Y        | Y                         | Y                           | Y                             | Y                                  | Y                         | Y                             |
| MCE (Manual Card Entry) | N              | N                      | N                        | Y                          | Y                               | Y                      | Y                          | N        | N                         | N                           | Y                             | Y                                  | Y                         | Y                             |
| BCR (Barcode Reader)    | Y              | Y                      | Y                        | Y                          | Y                               | Y                      | Y                          | Y        | Y                         | Y                           | Y                             | Y                                  | Y                         | Y                             |
| LED RGBx4               | 1              | Y                      | Y                        | Y                          | Y                               | Y                      | Y                          | N        | Y                         | Y                           | Y                             | Y                                  | Y                         | Y                             |
| LED Monox4              | Y              | N                      | N                        | N                          | N                               | N                      | N                          | Y        | N                         | N                           | N                             | N                                  | N                         | N                             |
| Touch                   | N              | N                      | N                        | Y                          | Y                               | Y                      | Y                          | N        | N                         | N                           | Y                             | Y                                  | Y                         | Y                             |
| No Touch                | Y              | Y                      | Y                        | N                          | N                               | N                      | N                          | Y        | Y                         | Y                           | N                             | N                                  | N                         | N                             |
| Display                 | N              | N                      | N                        | Y                          | Y                               | Y                      | Y                          | N        | N                         | N                           | Y                             | Y                                  | Y                         | Y                             |
| No Display              | Y              | Y                      | Y                        | N                          | N                               | N                      | N                          | Y        | Y                         | Y                           | N                             | N                                  | N                         | N                             |
| Battery Power           | Y              | N                      | Y                        | N                          | Y                               | Y                      | Y                          | N        | N                         | Y                           | N                             | Y                                  | Y                         | Y                             |
| Banking Functions       | N              | N                      | N                        | Y                          | Y                               | Y                      | Y                          | N        | N                         | N                           | Y                             | Y                                  | Y                         | Y                             |
| Session Management      | N              | N                      | N                        | N                          | N                               | Y                      | N                          | N        | N                         | N                           | N                             | N                                  | Y                         | N                             |
| Apple VAS               | Y              | N                      | N                        | N                          | N                               | N                      | N                          | Y        | Y                         | Y                           | Y                             | Y                                  | Y                         | Y                             |
| Google Wallet Smart Tap | Y              | N                      | N                        | N                          | N                               | N                      | N                          | Y        | Y                         | Y                           | Y                             | Y                                  | Y                         | Y                             |
| Flexible UI             | N              | N                      | N                        | N                          | N                               | N                      | N                          | N        | N                         | N                           | Y                             | Y                                  | Y                         | Y                             |
| Common Kernel           | Y              | N                      | N                        | N                          | N                               | N                      | N                          | Y        | Y                         | Y                           | Y                             | Y                                  | Y                         | Y                             |
| Card Emulation          | Y              | Y                      | Y                        | Y                          | Y                               | Y                      | Y                          | Y        | Y                         | Y                           | Y                             | Y                                  | Y                         | Y                             |