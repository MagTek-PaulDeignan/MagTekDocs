---
title: DynaFlex II GO Installation and Operation Manual
layout: home
parent: DynaFlex II GO
nav_order: 1
---
<style>
table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  text-align: left;
  padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2}

th {
  background-color: black;
  color: white;
}
</style>

<button class="btn js-toggle-dark-mode">Preview dark color scheme</button>

<script>
const toggleDarkMode = document.querySelector('.js-toggle-dark-mode');

 jtd.addEvent(toggleDarkMode, 'click', function(){
   if (jtd.getTheme() === 'dark') {
     jtd.setTheme('light');
     toggleDarkMode.textContent = 'Preview dark color scheme';
   } else {
     jtd.setTheme('dark');
     toggleDarkMode.textContent = 'Return to the light side';
   }
 });
 </script>




| DynaFlex II GO Installation and Operation Manual                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------|
| ![A close-up of a device Description automatically generated](<DynaFlex II Go Images/9fd12164974def7ad4c3fe270a989cc3.png>) |
| June 2025  Document Number: D998200595-126  REGISTERED TO ISO 9001:2015                                                     |

Copyright © 2006 - 2025 MagTek, Inc.

Printed in the United States of America

information in this publication is subject to change without notice. MagTek cannot be held liable for any use of the contents of this document. Any changes or improvements made to this product will be included in the next publication release. If you have questions about specific features and functions or when they will become available, please contact your MagTek representative.

MagTek®, MagnePrint®, and MagneSafe® are registered trademarks of MagTek, Inc.

Magensa™ is a trademark of MagTek, Inc.

AAMVA™ is a trademark of AAMVA.

ANSI®, the ANSI logo, and numerous other identifiers containing "ANSI" are registered trademarks, service marks, and accreditation marks of the American National Standards Institute (ANSI).

ISO® is a registered trademark of the International Organization for Standardization.

PCI Security Standards Council® is a registered trademark of the PCI Security Standards Council, LLC.

EMV® is a registered trademark in the U.S. and other countries and an unregistered trademark elsewhere. The EMV trademark is owned by EMVCo, LLC. The Contactless Indicator mark, consisting of four graduating arcs, is a trademark owned by and used with permission of EMVCo, LLC.

Google Play™ store, Google Wallet™ payment service, and Android™ platform are trademarks of Google LLC.

Apple Pay®, Apple Wallet®, iPhone®, iPod®, Mac®, and OS X® are registered trademarks of Apple Inc., registered in the U.S. and other countries. iPad™ is a trademark of Apple. Inc. App StoreSM is a service mark of Apple Inc., registered in the U.S. and other countries. Apple and MFi are registered trademarks of Apple Inc. IOS is a trademark or registered trademark of Cisco in the U.S. and other countries and is used by Apple Inc. under license.

The OtterBox® and uniVERSE® trademarks are property of Otter Products, LLC, registered in the U.S. and other countries.

MIFARE®, MIFARE Classic ®, and MIFARE® DESFire®, are registered trademarks of NXP Semiconductors Austria GmbH Styria, All rights reserved.

The Bluetooth® word mark, logos, and Bluetooth® Low Energy (LE) are registered trademarks owned by Bluetooth® SIG, Inc.

Microsoft®, Windows®, and .NET® are registered trademarks of Microsoft Corporation.

All other system names and product names are the property of their respective owners.

Table 1 - Revisions

| Rev Number | Date              | Notes                                                                                                                                                                                                                                                                                                                                                                                       |
|------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 100        | November 16, 2023 | Initial release                                                                                                                                                                                                                                                                                                                                                                             |
| 110        | February 1, 2024  | Update all Device Images, Update Device Specifications throughout document; Updated **1.1 Key Features and Components** to include NFC Tag/Mifare Classic/Mifare DESFire Light, and Buzzer command support; Added **6.4.1 How to Play a Sequence of Tones**; Added Error! Reference source not found. Error! Reference source not found.**.** miscellaneous clarifications and corrections. |
| 120        | April 12, 2024    | Update **Table 3 - DynaFlex II Go Accessories** with current USB Type A-C and type C cable Part Numbers and Descriptions, Add section **7.5.7 DynaFlex II Go Bluetooth® Low Energy (LE) Sleep Mode,** Add **6.2 Physical Button Operation**, Add reference to BLE Sleep mode in **6.3 About Operating Modes**                                                                              |
| 121        | May 15, 2024      | Updated **7.6.2** **MSR Payment Transaction Successful (Connected via USB)**and **7.6.6** **MSR Payment Transaction Successful (Connected via Bluetooth® LE)** with correct LED behavior for MSR Transactions                                                                                                                                                                               |
| 122        | February 14, 2025 | Removed UL language from Boiler Plate and updated Safety Language in **Appendix D**.                                                                                                                                                                                                                                                                                                        |
| 123        | February 27, 2025 | Removed the word "preferred" from wired connection specification for USB 3.0 in **Appendix A Technical Specifications.**                                                                                                                                                                                                                                                                    |
| 124        | March 11, 2025    | Remove outdated language in **Appendix D:** Removed UL and Canada UL statement (this is included in the “safety” section) Modified the EU statement to reflect the correct DoC Added the UKCA statement Modified the Australia statement per the updated requirements and added link to the DoC                                                                                             |
| 125        | April 2, 2025     | Add MIFARE Plus, remove MIFARE Lite in **7.9.5 How to Tap Contactless NFC Tags / MIFARE Classic / MIFARE DESFire /MIFARE Plus Cards and Send Pass-through Commands**                                                                                                                                                                                                                        |
| 126        | June 5, 2025      | Update **Appendix A Technical Specifications** storage and operating relative humidity values from 5% to 90% RH non-condensing to Up to 90% RH non-condensing.                                                                                                                                                                                                                              |

# Table of Contents

- [Introduction](#introduction)
  - [Key Features and Components](#key-features-and-components)
  - [Available Models and Accessories](#available-models-and-accessories)
  - [About Terminology](#about-terminology)
- [Planning and Preparation](#planning-and-preparation)
  - [Logistical Planning](#logistical-planning)
- [Handling and Storage](#handling-and-storage)
  - [Handling to Avoid Damage](#handling-to-avoid-damage)
  - [Handling to Avoid Accidental Tamper](#handling-to-avoid-accidental-tamper)
- [Installation](#installation)
  - [About Inspection](#about-inspection)
  - [About Host Software](#about-host-software)
  - [Connecting DynaFlex II Go to a Host](#connecting-dynaflex-ii-go-to-a-host)
    - [How to Connect DynaFlex II Go to a Host Computer via USB-C](#how-to-connect-dynaflex-ii-go-to-a-host-computer-via-usb-c)
    - [How to Connect DynaFlex II Go to an iOS Host via Bluetooth® Low Energy (LE)](#how-to-connect-dynaflex-ii-go-to-an-ios-host-via-bluetooth-low-energy-le)
    - [How to Connect DynaFlex II Go to an Android Host via Bluetooth® Low Energy (LE)](#how-to-connect-dynaflex-ii-go-to-an-android-host-via-bluetooth-low-energy-le)
    - [How to Connect DynaFlex II Go to a Windows 10 Host [Version 1703 or Above] via Bluetooth® Low Energy (LE) (Windows Drivers)](#how-to-connect-dynaflex-ii-go-to-a-windows-10-host-version-1703-or-above-via-bluetooth-low-energy-le-windows-drivers)
  - [Mounting](#mounting)
    - [About Mounting](#about-mounting)
    - [How to Mount DynaFlex II Go](#how-to-mount-dynaflex-ii-go)
- [Configuration](#configuration)
- [Operation](#operation)
  - [Operation Overview](#operation-overview)
  - [Physical Button Operation](#physical-button-operation)
  - [About Operating Modes](#about-operating-modes)
  - [About Sounds](#about-sounds)
    - [How to Play a Sequence of Tones](#how-to-play-a-sequence-of-tones)
- [Introduction to User Interface](#introduction-to-user-interface)
  - [Component Details](#component-details)
  - [Power On via USB Cable LED Behavior](#power-on-via-usb-cable-led-behavior)
  - [USB Enumeration](#usb-enumeration)
  - [About the Status LEDs](#about-the-status-leds)
  - [Bluetooth® Low Energy (LE) LED Behavior](#bluetooth-low-energy-le-led-behavior)
    - [Bluetooth® Low Energy (LE) Status LED 2 and LED 3](#bluetooth-low-energy-le-status-led-2-and-led-3)
    - [Power On DynaFlex II Go in Battery Operating Mode](#power-on-dynaflex-ii-go-in-battery-operating-mode)
    - [Power Off DynaFlex II Go in Battery Operating Mode](#power-off-dynaflex-ii-go-in-battery-operating-mode)
    - [DynaFlex II Go Bluetooth® Low Energy (LE) Host Pairing](#dynaflex-ii-go-bluetooth-low-energy-le-host-pairing)
    - [DynaFlex II Go Bluetooth® Low Energy (LE) Host Connected](#dynaflex-ii-go-bluetooth-low-energy-le-host-connected)
    - [DynaFlex II Go Bluetooth® Low Energy (LE) Host Disconnect](#dynaflex-ii-go-bluetooth-low-energy-le-host-disconnect)
    - [DynaFlex II Go Bluetooth® Low Energy (LE) Sleep Mode](#dynaflex-ii-go-bluetooth-low-energy-le-sleep-mode)
  - [LED Behavior: Successful Transactions](#led-behavior-successful-transactions)
    - [BCR Payment Transaction Successful (Connected via USB)](#bcr-payment-transaction-successful-connected-via-usb)
    - [MSR Payment Transaction Successful (Connected via USB)](#msr-payment-transaction-successful-connected-via-usb)
    - [EMV Contact Payment Transaction Successful (Connected via USB)](#emv-contact-payment-transaction-successful-connected-via-usb)
    - [EMV Contactless Payment Transaction Successful (Connected via USB)](#emv-contactless-payment-transaction-successful-connected-via-usb)
    - [BCR Payment Transaction Successful (Connected via Bluetooth® LE)](#bcr-payment-transaction-successful-connected-via-bluetooth-le)
    - [MSR Payment Transaction Successful (Connected via Bluetooth® LE)](#msr-payment-transaction-successful-connected-via-bluetooth-le)
    - [EMV Contact Payment Transaction Successful (Connected via Bluetooth® LE)](#emv-contact-payment-transaction-successful-connected-via-bluetooth-le)
    - [EMV Contactless Payment Transaction Successful (Connected via Bluetooth® LE)](#emv-contactless-payment-transaction-successful-connected-via-bluetooth-le)
  - [LED Behavior: Errors, Timeouts, and Canceled Transactions](#led-behavior-errors-timeouts-and-canceled-transactions)
  - [Power Management](#power-management)
    - [About Power](#about-power)
    - [How to Charge the Battery](#how-to-charge-the-battery)
    - [How to Power On / Wake Up from Standby Mode / Power Off](#how-to-power-on--wake-up-from-standby-mode--power-off)
    - [About Maintenance Reset](#about-maintenance-reset)
  - [Card Reading](#card-reading)
    - [About Reading Cards](#about-reading-cards)
    - [How to Tap Contactless Cards / Devices](#how-to-tap-contactless-cards--devices)
    - [How to Scan Barcodes](#how-to-scan-barcodes)
    - [Apple VAS for DynaFlex II Go](#apple-vas-for-dynaflex-ii-go)
      - [VAS App and Payment Mode (Dual Mode)](#vas-app-and-payment-mode-dual-mode)
      - [VAS App Only Mode (VAS Mode)](#vas-app-only-mode-vas-mode)
      - [VAS App or Payment Mode (Single Mode)](#vas-app-or-payment-mode-single-mode)
      - [Payment Only Mode (Payment Mode)](#payment-only-mode-payment-mode)
    - [How to Tap Contactless NFC Tags / MIFARE Classic / MIFARE DESFire /MIFARE Plus Cards and Send Pass-through Commands](#how-to-tap-contactless-nfc-tags--mifare-classic--mifare-desfire-mifare-plus-cards-and-send-pass-through-commands)
- [Maintenance](#maintenance)
  - [Mechanical Maintenance](#mechanical-maintenance)
  - [Updates to Firmware, Documentation, Security Guidance](#updates-to-firmware-documentation-security-guidance)
- [Developing Custom Software](#developing-custom-software)
          - [Technical Specifications](#technical-specifications)
          - [Barcode Reader Symbologies](#barcode-reader-symbologies)
          - [Optional Accessories](#optional-accessories)
          - [Warranty, Standards, and Certifications](#warranty-standards-and-certifications)

# Introduction

DynaFlex II Go and DynaFlex II Go with Barcode Reader (BCR) deliver the next generation of mobile payment solutions. Both models offer an integrated secure card reader authenticator for magnetic stripe cards, EMV chip cards (contact and contactless), and NFC enabled mobile wallets including Samsung Pay, Google Pay™ with support for Google VAS, and Apple Pay® with support for Apple VAS. Ideal for cafés, restaurants, boutiques, airlines, retail banks and other developers looking to build a secure payment solution that accepts contactless EMV and NFC payments. DynaFlex II Go is suited for deployment in many scenarios, including mobile handsets, tablets, and desktop computers.

DynaFlex II Go and DynaFlex II Go BCR are equipped with MagneSafe® Security Architecture (MSA). The design and architecture meet the requirements for contactless EMV 3.1, PCI PTS POI v6.2, and support triple DEA encryption with DUKPT Key Management.

## Key Features and Components

DynaFlex II Go and DynaFlex II Go BCR are easy to install and configure, with key features that include:

-   Contactless EMV 3.1 Approved.
-   Contact EMV 4.4a Approved.
-   PCI PTS POI v6.2 Approved.
-   Optical reading for many 2D and 1D barcodes including PayPal and Venmo (DynaFlex II Go BCR Model Only).
-   Transducer for audio alerts.
-   User configurable audio commands to play a sequence of tones.
-   Bluetooth® Low Energy (LE).
-   USB-C interface.
-   iAP2® Protocol Support.
-   Triple DEA encryption / DUKPT key management.
-   AES-128 and AES-256 encryption.
-   Ingress protection - IP 30.
-   Apple Pay® / Apple Wallet® (Apple VAS protocol support).
-   Google Wallet Smart Tap. (Google VAS protocol support).
-   Google Pay™.
-   NFC Compatibility: Smart cards and contactless IC products, including MIFARE Classic / MIFARE DESFire /MIFARE Plus cards, with the ability to send pass-through commands.
-   Optional OtterBox® uniVERSE® case.
-   Optional countertop stand.

**Figure 1** illustrates the major components of DynaFlex II Go (BCR model shown). Models without a barcode reader are identical to the illustration, but do not have a camera and do not have a QR code printed on the front face.

![A close-up of a fingerprint scanner Description automatically generated](<DynaFlex II Go Images/9a6cfaf06a3b70cae4511c4fdb09476f.png>)

Figure 1 - DynaFlex II Go Major Components

## Available Models and Accessories

Table 2 - Available Models and Options

| Part No. | Description                                                               | Display | Connection(s)                 | Operating Systems                        |
|----------|---------------------------------------------------------------------------|---------|-------------------------------|------------------------------------------|
| 21078400 | DynaFlex II Go, PCI, BCR, BLACK, BLUETOOTH LE                             | None    | USB-C, Bluetooth® (LE), iAP2® | MS Windows, Mac OS, Linux; Android Phone |
| 21078401 | DynaFlex II Go, PCI, BLACK, BLUETOOTH LE                                  | None    | USB-C, Bluetooth® (LE), iAP2® | MS Windows, Mac OS, Linux; Android Phone |
| 21078402 | DynaFlex II Go, PCI, BCR, BLACK                                           | None    | USB-C, iAP2®                  | MS Windows, Mac OS, Linux; Android Phone |
| 21078403 | DynaFlex II Go, PCI, BLACK                                                | None    | USB-C, iAP2®                  | MS Windows, Mac OS, Linux; Android Phone |
| 21078404 | DynaFlex II Go, PCI, BCR, BLACK, BLUETOOTH LE, LOCKED MAGENSA BUNDLE LMB  | None    | USB-C, Bluetooth® (LE), iAP2® | MS Windows, Mac OS, Linux; Android Phone |
| 21078405 | DynaFlex II Go, PCI, BLACK, BLUETOOTH LE, LOCKED MAGENSA BUNDLE LMB       | None    | USB-C, Bluetooth® (LE), iAP2® | MS Windows, Mac OS, Linux; Android Phone |
| 21078406 | DynaFlex II Go, PCI, BCR, BLACK, LOCKED MAGENSA BUNDLE LMB                | None    | USB-C, iAP2®                  | MS Windows, Mac OS, Linux; Android Phone |
| 21078407 | DynaFlex II Go, PCI, BLACK, LOCKED MAGENSA BUNDLE LMB                     | None    | USB-C, iAP2®                  | MS Windows, Mac OS, Linux; Android Phone |

Table 3 - DynaFlex II Go Accessories

| Part \#                                                                                | Description                                    | Accessory Notes                                                           |
|----------------------------------------------------------------------------------------|------------------------------------------------|---------------------------------------------------------------------------|
| 1000005076                                                                             | CABLE, USB-C TO USB TYPE A MALE USB 2.0, 20AWG | Optional, specify in order                                                |
| 1000006016                                                                             | USB CABLE TYPE A – C, 6FT                      | Optional, specify in order                                                |
| 1000006017                                                                             | USB CABLE TYPE C, 6FT                          | Optional, specify in order                                                |
| 21078408                                                                               | DYNAFLEX II GO, KIT COUNTERTOP STAND           | Refer to **Appendix C Optional Accessories** for additional information.  |
| 21078409                                                                               | DYNAFLEX II GO ADAPTOR FOR OTTERBOX            | Refer to **Appendix C Optional Accessories** for additional information.  |
| 21078410                                                                               | DYNAFLEX II GO RUBBER SLEEVE                   | Refer to **Appendix C Optional Accessories** for additional information.  |
| 21078411                                                                               | DYNAFLEX II GO RUBBER SLEEVE HALF SIZE         | Refer to **Appendix C Optional Accessories** for additional information.  |
| **Note**: *At least one cable will be shipped with the device, specify when ordering.* |                                                |                                                                           |

## About Terminology

In this document, DynaFlex II Go products are referred to as the **device**. They are designed to be connected to a **host**, which is a piece of general-purpose electronic equipment that can send commands and data to, and receive data from, the device. Host types include PC and Mac computers/laptops, tablets, and smartphones. Generally, the host must have **software** installed that communicates with the device and is capable of processing transactions. During a transaction, the host and its software interact with the **operator**, such as a customer service representative, while the device interacts with the **cardholder** (even if the cardholder is using a virtual representation of the card account, such as a smartphone).

# Planning and Preparation

The guidelines in the following sections are intended to help project planners and system administrators plan for the physical and logical requirements of deploying and using DynaFlex II Go products. The most effective way to ensure smooth deployment of a solution is to consider these factors before receiving the device.

## Logistical Planning

-   Determine what type of **host** DynaFlex II Go will connect to. For a list of supported device types and operating systems, see **Table 2**. When planning, be sure to include any additional support or devices required by the host and DynaFlex II Go, such as physical locations, mounting, power connections, and charging cradles.
-   Determine what **connection** the host will use to communicate with the device. The available connections are USB-C for power and control and Bluetooth® Low Energy (LE) for wireless connectivity (see **Table 2**).
-   Determine what **software** will be installed on the host and how it will be configured. Software can include the operating system, transaction processing software, security software, and so on. If teams other than the software development team will be involved in preliminary device testing, MagTek recommends the solution development team provide a smoke test harness early in the development process to allow basic testing (for example, communication adapter testing). In addition, be sure to plan for any additional support required by the software, such as software licenses and network connections. Information about software is provided in section **4.2 About Host Software**.
-   Determine how the device will be physically presented to the cardholder. If the device is mounted, make sure there is adequate clearance for cardholders to swipe, insert, and tap. If the solution design includes metal objects anywhere near the device, including metal enclosures, make sure that at all points the metal is no closer than 15mm from the MSR swipe path or card insertion slot. Proximity to metal can adversely affect the device’s performance.
-   Determine how the device should be configured and specify that configuration when ordering the device. A full list of configurable options is documented in **D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS)**.
-   Select and configure a secure workstation that advanced operators will use to configure and/or update the device. The workstation must be configured as follows:
    -   Available USB port.
    -   A secure means of obtaining files, either via the network (such as SFTP) or via removable media, such as USB flash drives. This is required for installing software tools, copying firmware files, etc. If you are using Magensa Services, make sure the secure workstation has an internet connection and has all the required Magensa Remote Services software components installed.
    -   **1000007406 DynaFlex, DynaProx Test Utility** installed, which advanced operators can use to configure and test the device.
-   Determine the final set of tools advanced operators will use to configure, test, and update the device. This documentation uses the **1000007406 DynaFlex, DynaProx Test Utility** as an example for configuring the device; it can be used for initial pre-deployment testing and development, and as sample code showing how to communicate with the device, but the full solution may call for customized, solution-specific software for configuring the device and updating firmware.
-   Determine how to **inspect** devices upon arrival, upon installation, and periodically during live usage, to ensure malicious individuals have not tampered with them. Details about inspection are provided in section **4.1 About Inspection**.
-   Develop procedures for maintaining the device(s). Detailed guidance is provided in section **8 Maintenance**.
-   Determine how to train operators. For example, training may include information extracted from section **5 Configuration**, section **6 Operation**, and section **8 Maintenance**.
-   Review the device’s PCI Security Policy, posted to the PCI web site [www.pcisecuritystandards.org](http://www.pcisecuritystandards.org) under **Approved PIN Transaction Security (PTS) Devices**, for additional information about using the device securely.

# Handling and Storage

| ![](<DynaFlex II Go Images/bdb6a105147891251b84fbdb350ba870.png>)                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Proper handling of the device throughout delivery, assembly, shipping, installation, usage, and maintenance is very important. Not following the guidelines in this document could damage the device, render it inoperable, and/or violate the conditions of the warranty. |

## Handling to Avoid Damage

Upon receiving the device, inspect it to make sure it originated from an authentic source and has not been tampered with. For details, see **D998200593 DynaFlex II Go Device Inspection Document**, available from MagTek.

From device delivery through assembly, shipping, installation, usage, and maintenance, the device must not be exposed to conditions outside the ratings in **Appendix A Technical Specifications**.

If the device is exposed to cold temperatures, adjust it to warmer temperatures gradually to avoid condensation, which can interfere with the operation of the device or cause permanent damage.

Do not drop or shake the device.

For information about ongoing maintenance of the device, such as cleaning, see section **8 Maintenance**.

## Handling to Avoid Accidental Tamper

DynaFlex II Go products implement active tamper detection, which uses a small amount of electricity even when the device is completely powered off. When unpowered by an external power supply, the device powers its active tamper detection circuitry using its non-rechargeable internal backup battery. This provides 5 years of backup shelf life across the entire life of the device. If the backup battery is allowed to completely discharge, the device’s tamper detection engages and locks down the device, and it must be returned to the manufacturer to reset.

To avoid accidental tamper events and to optimally condition the battery, follow these precautions:

-   Temperature is the most critical factor in extending battery life and preserving battery charge. Store the device at the lowest reasonable temperatures within its specified storage temperature range (see **Appendix A Technical Specifications**). Storing at temperatures between -4°F to 113°F (-20°C to 45°C).
-   Do not drop or shake the device.
-   Do not attempt to disassemble the device.

# Installation

Installing DynaFlex II Go products is straightforward: The manufacturer or acquirer, configures the preferred settings, keys, terminal, and payment brand settings before deployment; end users need only set up a host with appropriate software, configure the software, and connect the device to the host. This section provides general information about inspecting, connecting, and installing DynaFlex II Go products.

## About Inspection

Before unpacking the device, it is important to inspect its secure packaging to make sure it has not been tampered with in storage or in transit. MagTek provides details for inspecting the integrity of the device’s secure packaging in **D998200594 DynaFlex II Go Package Inspection Document**.

It is important to thoroughly inspect a new device before deployment, and regularly inspect devices in live usage (including its immediate surroundings) to make sure malicious individuals have not tampered with it. MagTek recommends conducting inspection training for all device operators, and an inspection schedule with checkpoints in place to make sure operators are performing inspections as specified and as scheduled. MagTek provides an easy-to-follow device inspection reference **D998200593 DynaFlex II Go Device Inspection Document**.

## About Host Software

DynaFlex II Go products do not have a display. In any solution, DynaFlex II Go must be connected to a host, which must have software installed that can communicate with the device and is capable of processing transactions. To set up the host to work with DynaFlex II Go, follow the installation and configuration instructions provided by the vendor of the host or the host software. For information about developing custom host software, see section **9 Developing Custom Software**.

## Connecting DynaFlex II Go to a Host

The following sections describe how to connect DynaFlex II Go to a host using the available USB-C receptacle or Bluetooth® Low Energy (LE) connections.

### How to Connect DynaFlex II Go to a Host Computer via USB-C

![A drawing of a device Description automatically generated](<DynaFlex II Go Images/820c3f0f95c1e43cbaa1def833e224d8.png>)

Figure 2 - Connecting to a Host via USB-C

To connect DynaFlex II Go products to a USB host computer or charger using the USB-C port, follow these steps (for reference see **Figure 2**):For best results, use the cable that is included with the device or another cable from **Table 3 - DynaFlex II Go Accessories** on page **9**. Connect the USB-C end of the cable to DynaFlex II Go see **Figure 2 - Connecting to a Host via USB-C**.

1.  Connect the other end of the USB cable to the host’s USB port.
2.  As soon as the device starts receiving power through USB, it automatically powers on.
3.  If the specific device serial number you are connecting has not been previously connected to the host, the Windows system tray on the host reports it is setting up a device.
4.  When installation is complete, Windows reports **Device is ready**, (see **Figure 3 – Setup Complete)** and the device shows in Windows Device Manager under **Human Interface Devices** (**see Figure 4 – Windows Device Manager**) as two devices: **HID-compliant vendor-defined device** (see **Figure 5 – HID Compliant Vendor-defined Device Properties**) with VID **0801** and PID **2024**, and **USB Input Device**.

![A screenshot of a computer Description automatically generated](<DynaFlex II Go Images/5242ab19616db3c9047b5c511b6cf3ff.png>)

Figure 3 – Setup Complete

![A screenshot of a computer Description automatically generated](<DynaFlex II Go Images/2594ddbb972171fe207210fcccaee568.png>)

Figure 4 – Windows Device Manager

![A screenshot of a computer Description automatically generated](<DynaFlex II Go Images/42c4a5805bcf9f513fc90e9275163e6a.png>)

Figure 5 – HID Compliant Vendor-defined Device Properties

5.  The operating system may put the device into **USB Suspend** mode.

### How to Connect DynaFlex II Go to an iOS Host via Bluetooth® Low Energy (LE)

To connect DynaFlex II Go via Bluetooth® LE to an iOS device, refer to section **9 Developing Custom Software** and **D998200386 MagTek Universal SDK for MMS Devices Programmer's Manual ( iOS ).**

### How to Connect DynaFlex II Go to an Android Host via Bluetooth® Low Energy (LE)

To connect DynaFlex II Go to an Android host that supports Bluetooth® Low Energy (LE):

1.  If any Bluetooth® Low Energy (LE) host software has an active data connection to the device, close the connection.
2.  On the Android host, install and configure the host software you intend to use with DynaFlex II Go. If you do not yet have that software, you can download a test tool from the Google Play store called **MTUSDK Demo**, published by **MagTek, Inc.**.
3.  Make sure the DynaFlex II Go output connection is configured to transmit card data over Bluetooth® LE. This is the factory default.
4.  Press and hold the **Power Button** for 4 beeps until LED 4 starts flashing indicating Bluetooth® Pairing is in process. The Bluetooth® Status LED flashes once per second for up to three minutes, or until a host pairs or connects.
5.  On the Android host, launch the **Settings** application and open the **Bluetooth®**  menu.
6.  Press the **SEARCH FOR DEVICES** or **Scan** button to show an **AVAILABLE Bluetooth® DEVICES** list.
7.  Locate the seven-digit serial number on the label on the bottom of the device.
8.  Device will appear in the list as **DF II Go-xxxxxxx** where **xxxxxxx** matches the serial number.
9.  When the host pops up a **Bluetooth®  Pairing Request** message asking for a code, enter the configured passkey (or the default **000000**) to return to the **Bluetooth®**  configuration page. The device appears in the **PAIRED DEVICES** list.
10. Use the host software or the **MagTek Test** app to test swiping a card.
11. Remember to change the default password. See **1000007352 MagTek Universal SDK for MMS Devices (Android).**

To unpair from the device, follow these steps:

1.  Locate the device in the **Bluetooth®** configuration page.
2.  Press the settings (gear) icon.
3.  Press the **Forget** button and make sure the device disappears from the **Paired devices** list.

### How to Connect DynaFlex II Go to a Windows 10 Host [Version 1703 or Above] via Bluetooth® Low Energy (LE) (Windows Drivers)

To connect DynaFlex II Go to a host with Windows 10 version 1703 or above, and Bluetooth® 4.0 or higher hardware that supports Bluetooth® Low Energy (LE), follow these steps:

1.  Make sure the host’s Bluetooth® LE interface is turned on and working correctly.
2.  If any Bluetooth® Low Energy LE host software has an active data connection to the device, close the connection.
3.  On the host, install and configure the software you intend to use with DynaFlex II Go (if you do not yet have that software, you can use **1000007351 MagTek Universal SDK for MMS Devices (Windows)** available from MagTek.com, to perform simple tests):
    1.  Make sure the host software is configured to look for the device on the proper connection type.
    2.  Make sure the host software knows which device(s) it should interface with.
    3.  Make sure the host software is configured to properly interpret incoming data from the device. When using Bluetooth® LE, the device transmits data in GATT format.
4.  Make sure the DynaFlex II Go output connection is configured to transmit card data over Bluetooth® LE. This is the factory default.
5.  In the **Start** menu type **Bluetooth®**  and select **Bluetooth®  and other devices settings**, or double-click the **Bluetooth®  Devices** icon in the taskbar to launch the **Bluetooth®  & other devices settings** window.
6.  Locate the seven-digit serial number on the label on the bottom of the device.
7.  Press and hold the **Power Button** for 4 beeps until LED 4 starts flashing indicating Bluetooth® Pairing is in process. The Bluetooth® Status LED flashes once per second for up to three minutes, or until a host pairs or connects.
8.  Press the **Add Bluetooth®  or other device** button to launch an **Add a device** window.
9.  Under **Choose the kind of device you want to add**, select **Bluetooth®** .
10. Locate the device called **DF II Go-xxxxxxx**, where **xxxxxxx** matches the device’s serial number. Enter the configured passkey (or the default **999999**) and press the **Connect** button.
11. After a short period of time, the text **Connected** appears below the device you are pairing with. Note that in this case, “Connected” means the device is paired, but the host does not have an active data connection until the host software initiates one.
12. Press the **Done** button to close the **Add a device** window.
13. Use the host software to test swiping a card.
14. Remember to change the default password. See the **DynaFlex II Go Programmer’s Reference** documents for detail to unpair the device:
15. Select the device in the **Bluetooth®  and other devices settings** window.
16. Press the **Remove device** button.

## Mounting

### About Mounting

DynaFlex II Go products are designed to provide flexible mounting options:

-   The device can be mounted to the host via external clip or embedded lanyard.

### How to Mount DynaFlex II Go

| ![](<DynaFlex II Go Images/bdb6a105147891251b84fbdb350ba870.png>)                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| This document describes how to use DynaFlex II Go securely. Using the device in any way other than the approved methods described in this document invalidates the PCI PTS approval of the device. Not following the guidelines in this section could damage the device, render it inoperable, and/or violate the conditions of the warranty. |

This section provides information and guidelines for designing the mechanical aspects of a solution that incorporates DynaFlex II Go products. MagTek strongly recommends vetting and testing solution designs before finalizing and deploying them, to make sure the design meets all requirements (e.g., functional, legal, security, certification, safety, and so on).

When designing the mechanical portions of a solution that incorporates DynaFlex II Go products, consider the following:

-   Review section **1.1 Key Features and Components** for an overall introduction to the device’s physical features and what they are called.
-   Review **Appendix A Technical Specifications**.
-   Review the information below about overall device dimensions and mounting hole locations and use.
-   Review any additional requirements from other agencies, such as PCI and EMV solution certification requirements, safety ordinances, and so on, which may introduce additional constraints to the design.

Overall dimensions of the device are shown in **Figure 6**. On request, MagTek can provide a 3D model of the device’s envelope to assist with the mechanical portion of solution design. MagTek strongly recommends building and testing prototypes with actual devices before finalizing the solution design.

![A diagram of a card reader Description automatically generated](<DynaFlex II Go Images/4dfda043f5da3255f778264f438f868a.JPG>)

Figure 6 - DynaFlex II Go Overall Dimensions

When designing an enclosure or mounting bracket, make sure there is adequate clearance for cardholders to tap or users to present a bar code. Proximity to metal can reduce the device’s reading range.

# Configuration

The device does not have an on-screen configuration interface. However, it does have settings the host can change using commands. These settings are documented as **Properties** in **D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS)**.

# Operation

## Operation Overview

The operator initiates a transaction from the host, and the cardholder interacts with the device. Transaction types may include retail transactions, new accounts, teller window applications, checking, savings, mortgages, and any other type of transaction where there is interaction between the cardholder and the operator.

For each transaction type, the host software directs the cardholder. The transaction flow on the device may differ depending on what the host software specifies and what the cardholder does. Section **7.9 Card Reading** provides examples of the cardholder experience for each type of payment. If the device cannot read payment data, the host software may require the cardholder to repeat the action or require the host to reject the transaction.

## Physical Button Operation

All DynaFlex II Go devices have a single physical button, see **Figure 61 - Power Button**. Pressing and holding this button can activate extra functions. To active a specific function, press and hold the button until a specific number of beeps are heard. **Table 61 - Button Functions** contains functions that can be activated. Beep counts that are not listed are not supported.

![A close-up of a device Description automatically generated](<DynaFlex II Go Images/f978f9763e490b07b99c80ece38ec294.png>)

**Figure 61 - Power Button**

**Table 61 - Button Functions**

| Beep Count | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2          | **Power Off**  Hold for two beeps to power the device off. The device will reboot if it is connected to USB when powered off.                                                                                                                                                                                                                                                                                                                                                   |
| 3          | **Settings Menu**  SoftAP Mode in the Settings Menu is Available on WLAN enabled devices only.                                                                                                                                                                                                                                                                                                                                                                                  |
| 4          | **BLE Pairing**  BLE Enabled devices only.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 5          | **Demo**  See Appendix C for more information.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 6          | **Battery Level**  Light the LEDs to indicate the current state of charge of the battery. The LEDs will light for 3 seconds then return to their original state.  ![A table with green and black text Description automatically generated](<DynaFlex II Go Images/f2360506bcf6ee65eed8eea973e3519b.png>)  DynaFlex II Go has only green LEDs. Instead of lighting the first LED in amber, it will slowly flash the first LED. Instead of Red, the first LED will flash quickly. |

-   

## About Operating Modes

During operation, DynaFlex II Go devices transition between distinct operating modes, which are important for operators to understand:

-   **Powered Off Mode** is the shipping and storage mode of the device. No external power is applied to the device through the USB cable or from the internal rechargeable battery. In this mode, the device consumes very little power. To set the device from **Powered Off** mode to **Active Mode**, connect the device to USB power, or press the power button, see **Figure 61 - Power Button** .
-   **Active Mode** is the device’s normal “awake” state when it is in use. In this mode, the device LED indicators are powered on, and the device is ready to receive commands from the host. For more information on Status LEDs and LED behavior see sections **7.4 About the Status LEDs**, **7.5** Bluetooth**® Low Energy** (LE) LED Behavior, **7.5.7 DynaFlex II Go Bluetooth®** Low Energy (LE) Sleep Mode

When in Bluetooth® LE Sleep Mode, DynaFlex II Go will conserve battery life by limiting power to non-essential hardware features and entering low power mode. When in Sleep Mode, the device will appear to be powered off, with no LEDs illuminated, see **Figure 7 – Bluetooth® (LE) Sleep Mode**. For information on how to disable this feature, see **D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS).**

![](<DynaFlex II Go Images/ae69f4b03c0748ff9fbd64f521017a05.png>)

Figure 7 – Bluetooth® (LE) Sleep Mode

-   LED Behavior: Successful Transactions, and **7.7 LED Behavior: Errors, Timeouts, and Canceled Transactions**. To set the device from Active mode to Powered Off mode remove power press and hold the power button for two beeps.
-   **BLE Sleep Mode** is a standard feature that conserves battery life by limiting power to non-essential hardware features. When in Sleep Mode, the device will appear to be powered off, with no LEDs illuminated, see **7.5.7 DynaFlex II Go Bluetooth® Low Energy (LE) Sleep Mode,** for more information on BLE Sleep Mode.

## About Sounds

DynaFlex II Go products have a beeper that provides feedback to operators and cardholders about the internal state of the device:

-   The device sounds one short beep after it has successfully read a contactless tap, and the cardholder can safely remove the card or device from the contactless landing zone.
-   The device emits two beeps when reading a card or contactless payment device to indicate a card read error occurred.
-   The device sounds two beeps when an operator cancels a pending EMV transaction.

The device provides an internal setting the host can use to adjust the global system volume. The device does not provide an interface to change the volume setting directly via buttons. If the device is too quiet or too loud:

-   Make sure the device is being ordered from the manufacturer with the desired volume setting.
-   Check to see whether the host software you are using provides a feature to check and/or adjust the volume setting.
-   If the host software does not provide that feature, request help from the development team that built the host software to check / change the volume setting. For details, see **D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS)**.

### How to Play a Sequence of Tones

To play a sequence of tones, follow these steps:

1.  Make sure the device is in idle state.
2.  Send an audio command to the device to play a sequence of tones. For details, see **D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS).**

# Introduction to User Interface

This section contains information on DynaFlex II Go's LEDs, beeper, and BCR status LED. It is important to note that DynaFlex II Go devices are equipped with an optional rechargeable battery. If there is no power supply to the device through the USB cable or optional internal rechargeable battery, all LEDs, along with the BCR status LED, will not illuminate. When this occurs, the user interface will resemble the device as shown in **Figure 71**.

As mentioned in section **1.1 Key Features and Components**, DynaFlex II Go models equipped with a barcode reader (BCR) have a similar physical appearance as models without a BCR, as shown in **Figure 71**. BCR models are equipped with a camera and a QR code located on the front side of the device.

-   DynaFlex II Go devices have a user interface composed of three elements: a visual indicator consisting of four LEDs, a beeper that produces audible alerts, and a power button see **Figure 61 - Power Button**.
-   DynaFlex II Go BCR devices have a user interface composed of four elements: a visual indicator consisting of four LEDs, a barcode reader status LED, a beeper that produces audible alerts, and a power button see **Figure 61 - Power Button**.
-   DynaFlex II Go devices do not feature input components such as touch screens.

![A close-up of a device Description automatically generated](<DynaFlex II Go Images/b775d6c4e82bce75a0caa119b31b6ddf.png>)

**Figure 71 – DynaFlex II Go and DynaFlex II Go BCR**

## Component Details

1.  **LED Ordering**

The arrangement of the four LED indicators on DynaFlex II Go devices is illustrated in **Figure 72**. The LEDs are designated 1 to 4 and are ordered from left to right on the device.

![A white rectangular device with a hand pressing a button Description automatically generated](<DynaFlex II Go Images/b1a2e232dc7ededd067821b80cdf8b84.png>)

**Figure 72 - LED Ordering**

2.  **LED Status**

When DynaFlex II Go is powered on, its LEDs will illuminate green, when it is powered off, the LEDs will remain unlit.

**Figure 73** illustrates the On/Off status of the LEDs.

**Figure 73 - LED ON/OFF**

3.  **BCR Status**

DynaFlex II Go devices equipped with a bar code reader have a status LED that indicates whether the barcode feature is scanning.

![](<DynaFlex II Go Images/e9475d73642ce1b52b2da3779cfd894a.png>)![](<DynaFlex II Go Images/e9475d73642ce1b52b2da3779cfd894a.png>)

**Figure 74 - BCR Status LED**

4.  **Beeper Alert**

All DynaFlex II Go devices are equipped with a beeper that produces a short beep lasting for half a second and a long beep that lasts for one second.

## Power On via USB Cable LED Behavior

DynaFlex II Go will power on immediately when connected to USB power. A brief beep will sound, and all four LEDs will turn on for half a second, as shown in **Figure 75**. Following this, LED 1 and LED 2 will remain illuminated, while LED 3 and LED 4 will remain unlit.

![A close-up of a device Description automatically generated](<DynaFlex II Go Images/f9e9deeb6139514637f2762972a56d4a.jpg>)

**Figure 75 – LED Power on Sequence – USB Power On**

## USB Enumeration

When DynaFlex II Go is connected via USB in an idle state, it can be detected by a host through the USB HID port see **Figure 76**. After the host has connected to DynaFlex II Go, LED 1 will stay on. The device is in Ready State.

![A black square with white text Description automatically generated](<DynaFlex II Go Images/70a461fbd0c75542a95d769ed7441e9b.JPG>)![A black square with white text Description automatically generated](<DynaFlex II Go Images/2f80be7122cac3b84faec073da5dcb3b.JPG>)

**Figure 76 - LED Status (Idle State) Before Host Detection and LED Status (USB Ready State) After Connecting to Host**

## About the Status LEDs

DynaFlex II Go provides four LEDs (see section **7.1 Component Details**), numbered LED1 through LED4, which report the device’s current operating status.

-   The meaning of each LED depends on the device’s operating mode, see section **6 Operation**. Most of the time, operators will check the device’s status using the LEDs when it is in **Active Mode** while the device is not performing a transaction.
-   LED blinking patterns have specific meanings as described in **Table 7**. A blinking LED generally means the device is actively doing something to change the state that the LED is indicating, and solid indicates a persistent state that would require an operator or cardholder to take action to change. One major exception is a device-wide functional failure state, such as a tamper state, where all LEDs flash urgently to call the attention of an advanced operator to intervene.

In this manual, specific blinking patterns are described in more detail in the sections where they are relevant. For example, information about how the LEDs show the device’s connection status is in section **4.3 Connecting DynaFlex II Go** to a Host.

Table 4 - DynaFlex II Go LED Allocation

| In This Context                              | LED1                                                                                                                                          | LED2              | LED3              | LED4             |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-------------------|------------------|
| Active Mode, not armed for a tap transaction | Power                                                                                                                                         | Connection        | Reserved          | Card Read Result |
| Active Mode, armed for a tap transaction     | Armed for Tap                                                                                                                                 | Tap Read Progress | Tap Read Progress | Card Read Result |
| Device-wide failure                          | During major failures (such as tamper), **LED1-LED4** report the nature of the failure based on the most likely steps required to resolve it. |                   |                   |                  |

Table 5 - DynaFlex II Go LED Patterns

| Color        | Means                                                                                                                                                                                                                                                                                                          |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Solid        | **Solid** LEDs generally require an operator or cardholder to take action to change the state the LED is reporting. Example: Host is connected. Cardholder or host would have to disconnect. Example: Host is disconnected. Host would have to initiate connection.                                            |
| Blinking     | **Blinking** LEDs generally indicate the device is in the process of doing / attempting something. Blink duty cycle and blink period are generally selected to show urgency or ongoing progress through a series of steps. Example: Device is attempting to pair with the host via Bluetooth® Low Energy (LE). |
| Short time   | LEDs sometimes light for a **short time** to indicate some process has ended (success or failure) and the device is going to transition to another state soon. Example: Successful card read.                                                                                                                  |

## Bluetooth® Low Energy (LE) LED Behavior

### Bluetooth® Low Energy (LE) Status LED 2 and LED 3

LED 2 is designated for indicating Bluetooth® connection status, not USB connection status.

-   When LED 2 is **off**, it indicates that the device is not currently connected via Bluetooth®. In most cases, this implies that the device has a Bluetooth® signal that is not connected, unless this has been intentionally disabled through configuration.
-   When LED 2 is **on**, it indicates that the device is currently connected via Bluetooth®.

LED 3 is designated for indicating readiness for Bluetooth® message exchange.

-   When LED 3 is **off**, it indicates that the Bluetooth® connection is not yet ready. This could be due to the absence of a secure connection or the non-activation of device-to-host characteristic notifications.
-   When LED 3 is **on**, it indicates that the Bluetooth® connection is ready, signaling the establishment of a secure connection and the activation of device-to-host characteristic notifications.

### Power On DynaFlex II Go in Battery Operating Mode

Press and hold the Power Button for two seconds: initially, LED 4 will light up, followed by all four LEDs illuminating for one second. This is followed by LEDs 1 and 2 remaining lit for 2 seconds, after which only LED 1 will be active.

![A close up of a device Description automatically generated](<DynaFlex II Go Images/865f32ad54420ca786c5f179b39fd635.jpg>)

Figure 8 - Power On in Battery Operating Mode

![A black square with white text and green lights Description automatically generated](<DynaFlex II Go Images/b4b95162f8ffcf8efc92a898ce07aa9c.JPG>)

Figure 9 - LED Behavior for Bluetooth® Low Energy (LE) Ready State

If the host is within the Bluetooth® Low Energy (LE) connection range, all three LEDs (LED 1, 2, 3) will be illuminated, as described in **Figure 9 - LED Behavior for Bluetooth® Low Energy (LE) Ready State** .

### Power Off DynaFlex II Go in Battery Operating Mode

DynaFlex II Go is capable of being powered off while in Battery Operating Mode only. To initiate the power-off sequence, press and hold the Power Button for two beeps then release. It's important to note that DynaFlex II Go cannot be powered off while connected via USB. If a two-beep sequence is initiated while connected to USB the device will reboot.

![A black square with white text Description automatically generated](<DynaFlex II Go Images/70a461fbd0c75542a95d769ed7441e9b.JPG>)

Figure 10 - Power Off Device in Battery Operating Mode

### DynaFlex II Go Bluetooth® Low Energy (LE) Host Pairing

DynaFlex II Go must first be paired with the host device before a secure Bluetooth® connection can be established. Follow the steps below to activate Bluetooth® pairing mode:

1.  Press and Hold the Power Button for 4 beeps
2.  Release the Power Button
3.  LED 1 will remain steadily illuminated while LED 4 will begin to blink. When LED 4 is blinking it indicates the device is waiting to pair with the host. It will continue to blink for 3 minutes, waiting to pair with the host.

    ![A close-up of a card reader Description automatically generated](<DynaFlex II Go Images/adb028718902e13e6c6a85c5ef0a97d9.jpg>)

    Figure 710 - Activate BLE Pairing Mode

4.  When the host is pairing with DynaFlex II GO, LED 4 will remain off and LED 2 will power on, indicating the pair is processing.

    ![A black square with white text and green lights Description automatically generated](<DynaFlex II Go Images/e37d7f1aa00c978f4b2e7beb4d64e059.JPG>)

    Figure 711 - Bluetooth® LE Pair Processing

5.  The device will return to Power On status if pairing Succeeds or Fails. LED 2 will power off and LED 1 will remain powered on.

    ![A black square with white text Description automatically generated](<DynaFlex II Go Images/2f80be7122cac3b84faec073da5dcb3b.JPG>)

    Figure 712 - Pairing Successful/Failed

### DynaFlex II Go Bluetooth® Low Energy (LE) Host Connected

When the device establishes a connection to the host via BLE and is prepared for secure communication, all three LEDs (LED 1, 2, 3) will illuminate steadily.

![A black square with white text and green lights Description automatically generated](<DynaFlex II Go Images/b4b95162f8ffcf8efc92a898ce07aa9c.JPG>)

Figure 1 - BLE Connected to Host

### DynaFlex II Go Bluetooth® Low Energy (LE) Host Disconnect

When the device is disconnected from the host Bluetooth® Low Energy (LE) connection, LED 3 will power off first and after 4 seconds, LED 2 will power off, LED 1 will remain powered on as the device returns to Ready State.

![A close-up of a device Description automatically generated](<DynaFlex II Go Images/b07ad25330f21dc9600ad19eb5899e34.jpg>)

Figure 12 - Bluetooth® LE Disconnect LED Sequence

### DynaFlex II Go Bluetooth® Low Energy (LE) Sleep Mode

When in Bluetooth® LE Sleep Mode, DynaFlex II Go will conserve battery life by limiting power to non-essential hardware features and entering low power mode. When in Sleep Mode, the device will appear to be powered off, with no LEDs illuminated, see **Figure 7 – Bluetooth® (LE) Sleep Mode**. For information on how to disable this feature, see **D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS).**

![](<DynaFlex II Go Images/ae69f4b03c0748ff9fbd64f521017a05.png>)

Figure 7 – Bluetooth® (LE) Sleep Mode

## LED Behavior: Successful Transactions

### BCR Payment Transaction Successful (Connected via USB)

When the operator presses the **Start** button on the host device, LED 1,2, and the BCR status light will be illuminated see **Figure 716**. When a barcode is detected, only LED 1 will remain illuminated, the BCR status LED will be off, and a long beep will sound see **Figure 717**.

![A close-up of a card reader Description automatically generated](<DynaFlex II Go Images/e583e57753036b5b650628cb0dc75839.jpg>)

**Figure 716 – BCR Transaction USB Ready State**

![A black square with a fingerprint scanner Description automatically generated](<DynaFlex II Go Images/55592f66b1250b985b7b06e8e52fc213.jpg>)

**Figure 717 – BCR Transaction Barcode Detected (Connected via USB)**

### MSR Payment Transaction Successful (Connected via USB)

When the operator presses the **Start** transaction button on the host device, LED 1 and 2 will remain on. When a card is swiped, LEDs 1,2 and 4 will turn on in sequence (1,2 then 4), followed by a long beep, indicating a successful transaction, see **Figure 718**. After a successful transaction, the device will return to the ready state, see **Figure 719**.

![](<DynaFlex II Go Images/373ab8afe89113dbe26a56754a8eff96.png>)

**Figure 718 – LED Sequence – Payment Transaction Successful MSR Swipe (Connected via USB)**

![A close-up of a card reader Description automatically generated](<DynaFlex II Go Images/ebb68dac3f6d5864656de76c365f3532.png>)

**Figure 719 – Return to Ready State After Successful Transaction**

### EMV Contact Payment Transaction Successful (Connected via USB)

When the operator presses the **Start** transaction button on the host device, LED 1 and 2 will remain on. When a card is inserted, LEDs 1, 2 and 4 will turn on in sequence, followed by a long beep, indicating a successful transaction, see **Figure 14 – LED Sequence – Payment Transaction Successful EMV Contact (Connected** via USB). LED 4 will remain on, and the device will sound a double beep until the card is removed from the slot. After a successful transaction, the device will return to the ready state, see **Figure 719**.

![A close-up of a device Description automatically generated](<DynaFlex II Go Images/be72b1dabb9b6a55894b1ced35bf001e.jpg>)

Figure 14 – LED Sequence – Payment Transaction Successful EMV Contact (Connected via USB)

### EMV Contactless Payment Transaction Successful (Connected via USB)

When the operator presses the **Start** transaction button on the host device, LED 1 will remain on. When a card is presented within range of the contactless reader, LEDs 1,2,3, and 4 will turn on in sequence, followed by a long beep, indicating a successful transaction, see **Figure 15 - LED Sequence – Payment Transaction Successful EMV Contactless (Connected** via USB). After a successful transaction, the device will return to the ready state, see **Figure 719**.

![A close-up of a card reader Description automatically generated](<DynaFlex II Go Images/4d3475d61fce928806ece768186639d2.jpg>)

Figure 15 - LED Sequence – Payment Transaction Successful EMV Contactless (Connected via USB)

### BCR Payment Transaction Successful (Connected via Bluetooth® LE)

When the operator presses the **Start** button on the host device, LED 1,2, and the BCR status light will be illuminated see **Figure 722**. When a barcode is detected, only LED 1 will remain illuminated, the BCR status LED will be off, and a long beep will sound see **Figure 723**.

![A close-up of a card reader Description automatically generated](<DynaFlex II Go Images/e583e57753036b5b650628cb0dc75839.jpg>)

**Figure 722 – BCR Transaction Bluetooth® LE Ready State**

![A black square with a fingerprint scanner Description automatically generated](<DynaFlex II Go Images/55592f66b1250b985b7b06e8e52fc213.jpg>)

**Figure 723 – BCR Transaction Barcode Detected (Connected via Bluetooth® LE)**

### MSR Payment Transaction Successful (Connected via Bluetooth® LE)

When the operator presses the **Start** transaction button on the host device, LED 1 and 2 will remain on. When a card is swiped, LEDs 1,2 and 4 will turn on in sequence (1,2, then 4), followed by a long beep, indicating a successful transaction, see **Figure 724**. After a successful transaction, the device will return to the ready state, see **Figure 725**.

![](<DynaFlex II Go Images/3de9d5925c36e946bd610702ba95606f.png>)

**Figure 724 – LED Sequence – Payment Transaction Successful MSR Swipe (Connected via Bluetooth® LE)**

![A black square with white text and green lights Description automatically generated](<DynaFlex II Go Images/b4b95162f8ffcf8efc92a898ce07aa9c.JPG>)

**Figure 725 – Return to Ready State After Successful Transaction (Bluetooth® LE Ready State)**

### EMV Contact Payment Transaction Successful (Connected via Bluetooth® LE)

When the operator presses the **Start** transaction button on the host device, LED 1 and 2 will remain on. When a card is inserted, LEDs 1,2 and 4 will turn on in sequence, followed by a long beep, indicating a successful transaction, see **Figure 16 - LED Sequence – Payment Transaction Successful EMV Contact (Connected via** Bluetooth® LE). LED 4 will remain on and the device will sound a double beep until the card is removed from the slot. After a successful transaction, the device will return to the ready state, see **Figure 725**.

![A close-up of a device Description automatically generated](<DynaFlex II Go Images/1372e79778065565171e0b629578a908.jpg>)

Figure 16 - LED Sequence – Payment Transaction Successful EMV Contact (Connected via Bluetooth® LE)

### EMV Contactless Payment Transaction Successful (Connected via Bluetooth® LE)

When the operator presses the **Start** transaction button on the host device, LED 1 will remain on from ready state. When a card is presented within range of the contactless reader, LEDs 1,2,3, and 4 will turn on in sequence, followed by a long beep, indicating a successful transaction, see **Figure 17**. After a successful transaction, the device will return to the ready state, see **Figure 725**.

![A close-up of a device Description automatically generated](<DynaFlex II Go Images/a2f278d23bdbc8fde8d39a7ccefafcb1.jpg>)

Figure 17 - LED Sequence – Payment Transaction Successful EMV Contactless (Connected via Bluetooth® LE)

## LED Behavior: Errors, Timeouts, and Canceled Transactions

**Table 7 - LED Behavior for Errors, Timeouts, and Canceled Transactions,** contains LED behavior related to errors, timeouts, and canceled transactions. If the device is exhibiting LED behavior not previously mentioned, it may be contained in this section.

Table 6 - LED and BCR Indicator Light ON/OFF State

| **ON/OFF State**        |                                                                                                                                                                    |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **LED**                 | **![A green and grey circles Description automatically generated](<DynaFlex II Go Images/6514c3a70db2c32d4e197391ea2c64aa.png>)**                                  |
| **BCR Indicator Light** | **![A couple of triangles with shadows Description automatically generated with medium confidence](<DynaFlex II Go Images/087cf4d85d952661bfb764ad2598951a.png>)** |

Table 7 - LED Behavior for Errors, Timeouts, and Canceled Transactions

| **Device Model**                                                   | **Error LED Behavior**                                                 | **Timeout LED Behavior**                    | **Cancel LED Behavior**                                                |
|--------------------------------------------------------------------|------------------------------------------------------------------------|---------------------------------------------|------------------------------------------------------------------------|
| **DynaFlex II Go BCR** **Connected via USB**                       | LED 1,2 ON – BCR ON   \> LED1,2 ON, BCR OFF + Double Beeps   \> Ready  | LED1,2,3 OFF – LED 4 BCR ON + Double Beeps  | LED 1,2 ON – BCR ON   \> LED1,2 ON – BCR OFF + Double Beeps  \> Ready  |
| **DynaFlex II Go BCR** **Connected via Bluetooth® LE**             | LED 1,2 ON – BCR ON   \> LED1,2 ON, BCR OFF + Double Beeps   \> Ready  | LED1,2,3 OFF – LED 4 BCR ON + Double Beeps  | LED 1,2 ON - BCR ON   \> LED1,2 ON - BCR OFF + Double Beeps  \> Ready  |
| **DynaFlex II Go MSR** **Connected via USB**                       | LED 1,2 ON  \> LED1,2,3 OFF – LED 4 ON + Double beeps                  | LED1,2,3 OFF – LED4 ON + Double beeps       | LED 1,2 ON   \> LED1,2 ON + Double Beeps   \> Ready                    |
| **DynaFlex II Go MSR** **Connected via Bluetooth® LE**             | LED 1,2 ON   \> LED1,2,3 OFF – LED 4 ON + Double beeps                 | LED1,2,3 OFF – LED 4 ON + Double beeps      | LED 1,2 ON   \> LED1,2 ON + Double Beeps   \> Ready                    |
| **DynaFlex II Go EMV Contact** **Connected via USB**               | LED 1,2 ON   \> LED1,2,3 OFF – LED 4 ON + Double beeps                 | LED 1,2,3 OFF – LED 4 ON + Double Beeps     | LED 1 ON   \> LED1 ON + Double Beeps   \> Ready                        |
| **DynaFlex II Go EMV Contact** **Connected via Bluetooth® LE**     | LED 1,2 ON   \> LED1,2,3 OFF – LED 4 ON + Double Beeps                 | LED 1,2,3 OFF – LED 4 ON + Double Beeps     | LED 1,2 ON   \> LED1,2 ON + Double Beeps   \> Ready                    |
| **DynaFlex II Go EMV Contactless** **Connected via USB**           | LED 1 ON   \> LED1,2,3 OFF – LED 4 ON + Double beeps                   | LED 1,2,3 OFF – LED4 ON + Double beeps      | LED 1 ON   \> LED1 ON + Double Beeps   \> Ready                        |
| **DynaFlex II Go EMV Contactless** **Connected via Bluetooth® LE** | LED 1 ON   \> LED1,2,3 OFF – LED 4 ON + Double Beeps                   | LED 1,2,3 OFF – LED4 ON + Double Beeps      | LED 1 ON   \> LED1 ON + Double Beeps   \> Ready                        |

## Power Management

### About Power

With a sufficiently charged battery, the device will power on when the power button is pressed (see **Figure 61 - Power Button**). The device will also power on when connected to USB power. In USB mode the device will remain in full power mode to provide power to device. If a power-off sequence is initiated, the device will reboot and remain in full power mode.

### How to Charge the Battery

| ![A black and white sign with letters Description automatically generated](<DynaFlex II Go Images/03555afcb3177a7ebf5f264c12d86851.png>)       |
|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Per UL requirements, the device is designed to not recharge its internal battery when the external temperature is below 0°C or above 40°C.** |

DynaFlex II Go products have an optional rechargeable battery to supply their own power when they are not powered through the USB-C port. The battery must be periodically recharged by connecting the device to a USB port or stand-alone USB charger. The device requires a USB power supply that can provide at least **500mA @ 5V**.

To charge the device, connect it to a USB-C charger or a USB host as described in section **4.3.1 How to Connect DynaFlex II Go to a Host Computer via USB-C**. For best results, use the cable that is included with the device. When charging, make sure the device is receiving enough power from the USB connection (the battery level should increase even when the device is in use). A full recharge cycle for a completely drained battery depends on the charging method. From a host USB port at 500mA, full charge takes approximately 5 hours. From a dedicated wall charger, a full charge may take approximately 5 hours. After connecting the device to a power source, make sure the LEDs indicate the device is charging (see sec **4.3.1 How to Connect DynaFlex II Go to a Host Computer via USB-C)**

For important information about the device’s power systems, optimal charging methods during regular use, optimal handling and storage, and other information about keeping the device’s power systems in the best possible condition, see section **3.2 Handling to Avoid Accidental Tamper** and section **7.8.1 About Power**.

### How to Power On / Wake Up from Standby Mode / Power Off

To power on the device connect the device to USB power. To power off the device, disconnect the device from USB power. Press and hold the power button (see **Figure 61 - Power Button**) on the device (for two beeps), all LED indicators should power off and remain unlit. If all LEDs are off, the device is in Powered Off mode. It is important to note the device cannot be powered off when connected via USB.

### About Maintenance Reset

DynaFlex II Go will automatically reset once every 24 hours if it is continuously powered on.

## Card Reading

### About Reading Cards

The steps for starting a transaction and reading a contactless payment device are different depending on the device’s configuration and on the design of the host software. Host software developers should see section **9 Developing Custom Software** for implementation references. The solution developer should provide solution-specific instructions for operators to follow. A transaction generally follows this essential flow:

1.  An advanced operator has already made sure DynaFlex II Go is configured properly and is connected to the host (see section **4.3 Connecting DynaFlex II Go** to a Host). When the device is connected to the host and powered via the USBC connector or internal rechargeable battery, the host software may keep a connection open to the device.
2.  The operator makes sure DynaFlex II Go is receiving power either from the USB connection, or from the internal rechargeable battery, and is awake and powered on (see section **7.8.3)**
3.  The operator uses the host software’s user interface (for example, a point of sale) to finalize a transaction amount, then initiates a transaction. In solutions that are designed to respond to cardholder input events that occur when the device is idle, such as unprompted tapping of a card or electronic payment device, the host software may respond to those inputs by notifying the host. The host software may trigger other operations without being initiated by an operator (for example, the host software may immediately start a transaction, or alert the cardholder or operator to take action).
4.  The host communicates with the device, and reports to the operator when the device is ready.
5.  The operator guides and assists the cardholder in presenting payment.
6.  The cardholder interacts with the device to present payment. The following sections provide additional details about presenting each of the available payment methods.
7.  The host monitors the progress of the transaction, and when necessary, and should report issues to the operator, who may need to relay the messages to the cardholder.
8.  The device reports the success or failure of the transaction to the cardholder and to the host.

### How to Tap Contactless Cards / Devices

To tap a contactless card or smartphone, follow these steps:

1.  Check LED status:
    1.  The device shows the transaction status using the LEDs. LED1 lights solid and all other LEDs are off, per EMV standards, to indicate it is ready for a tap.
    2.  All devices report detailed transaction status to the host, and host software may report that information to operators so they can guide cardholders through the transaction (for example, “please tap your card now”).
2.  If the cardholder is using an electronic payment device, such as a smartphone, make sure the payment device has **NFC** turned **On** and has a payment app configured to process transactions. For details, see the documentation provided by the smartphone manufacturer and payment app publisher.
3.  Briefly hold the card, smartphone, or other contactless payment device over the contactless landing zone, indicated by the EMVCo Contactless Indicator symbol on the device’s face (see **Figure 18**). Because each smartphone model may have its NFC antenna placed differently, the ideal tap position may vary by make and model. For example, Samsung users may need to center the phone on the contactless landing zone, while Apple users may need to tap the top of the phone on the contactless landing zone.
4.  Wait for LED status:
    1.  The device quickly lights the second LED to show it is processing, then lights the third LED to show it has successfully read the tap, then lights the fourth LED to show the read is complete (see **Figure 19**) The device then returns to Ready State, when connected to USB ready state is LED 1 and 2 on only, ready state for BLE is LED 1,2, and 3 on.
    2.  The device beeps once.
    3.  If the transaction requires a signature, the device sends a notification message to the host that includes the status **Signature Capture Requested**. In this case, the solution design collects the cardholder’s signature manually or via a different method.
    4.  The device ends the transaction and reports the transaction status to the host.
5.  If the device cannot communicate with the card, smartphone, or other contactless payment device:
    1.  The device ends the transaction.
    2.  The device lights LED 4 for a short time.
    3.  The device beeps twice.
    4.  The device notifies the host that the transaction failed. If this occurs, the host software may choose to retry the transaction or revert to prompting the operator to perform another operation that is specific to the solution design.

        ![A close-up of a card Description automatically generated](<DynaFlex II Go Images/857b22bb8e88b40f75c40591438a384c.jpg>)![A close-up of a phone Description automatically generated](<DynaFlex II Go Images/b16868fb66ee336e6d18ace9a16d0bf0.JPG>)

Figure 18 - Tapping a Contactless Card / Smartphone

Figure 19 – Contactless Read LED Sequence – Read Complete (Connected via Bluetooth® LE)

### How to Scan Barcodes

To scan a barcode, follow these steps:

1.  Make sure you are using a DynaFlex II Go model that includes a barcode reader, indicated by QR Code markings on the face of the device surrounding the barcode reader lens (see section **1.1 Key Features and Components**).
2.  If the barcode being scanned is not on a self-illuminated source such as a smartphone, make sure there is enough ambient light for the camera to read the barcode. In low light conditions, the barcode reader will only be able to read self-illuminated sources.
3.  In some solutions, the operator may have to perform an operation in the host software to enable the barcode reader, or to start a transaction with the barcode reader enabled.
4.  Wait for the device, the host, or the operator to prompt for a barcode read:
    1.  The device lights the barcode reader indicator LED next to the barcode reader lens.
5.  Hold the barcode in front of the barcode reader camera:
    1.  If possible, use the light from the barcode reader indicator LED to align the barcode within the barcode reader’s field of view, which extends 16 degrees above / below and 21 degrees to the left / right of a line perpendicular to the barcode reader lens.
    2.  Hold the barcode as close as 6 inches from the lens. For smaller barcodes, the device will read immediately. If it does not, gradually move away up to 14 inches from the lens until the device reports a successful read. Larger barcodes must be far enough away from the device that the whole barcode is within the camera’s field of view; if a large barcode is too close, the barcode reader can only see a zoomed in portion of the barcode.
    3.  Do not tilt the barcode more than 60 degrees from parallel to the device’s face.
6.  Wait for the device or the host to report the barcode has been read successfully:
    1.  The device beeps once.
    2.  The device turns off the barcode reader indicator LED.

![](<DynaFlex II Go Images/fd7cd5907b37f38f73d15117e701622e.png>)

Figure 20 - Scanning a Barcode

### Apple VAS for DynaFlex II Go

DynaFlex II Go products support Apple Value Added Services (Apple VAS) protocol.

Contactless transactions using the Apple VAS protocol permits the device reader to perform the following supported operations:

#### VAS App and Payment Mode (Dual Mode)

The device reads both Apple VAS data and EMV payment data from a tapped smartphone or reads EMV payment data from a tapped card. When device sends ARQC to the host to conclude the transaction, it includes EMV payment data in container FC and includes VAS data, if available, in container FE

#### VAS App Only Mode (VAS Mode)

The device reads only Apple VAS data from a tapped smartphone and does not read data from a tapped card. If the tapped smartphone does not support VAS, the device does not detect or read from the smartphone. When the device sends ARQC to conclude the transaction, it includes VAS data in container FE and does not include EMV payment data in container FC.

#### VAS App or Payment Mode (Single Mode)

The device reads only Apple VAS data from a tapped smartphone or reads EMV payment data from a tapped card. When the device sends ARQC to conclude the transaction, it only includes either EMV payment data in container FC for cards, or includes VAS data in container for smartphones.

#### Payment Only Mode (Payment Mode)

The device operates the same as EMV mode (01). It reads only EMV payment data from a tapped smartphone or a tapped card. When the device sends ARQC to conclude the transaction, it includes EMV payment data in container FC and does not include VAS data in container FE. Note: THIS MODE MAY NOT BE NEEDED.

For details, see **D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS).**

### How to Tap Contactless NFC Tags / MIFARE Classic / MIFARE DESFire /MIFARE Plus Cards and Send Pass-through Commands

DynaFlex II Go is compatible with near field communication (NFC) technology such as MIFARE Classic / MIFARE DESFire /MIFARE Plus contactless IC products (smart cards).

To tap an NFC Contactless IC product and send pass-through commands, follow these steps:

1.  Check LED status:
    1.  Per EMV standards, the device indicates transaction status through its LED indicators, located on the front face of the device. When ready for a tap, LED 1 is steadily illuminated while all other LEDs remain unlit.
    2.  All devices communicate transaction details to the host. The host software will relay this information to operators, allowing them to direct cardholders during the transaction, such as prompting "please tap your card now".
2.  Place the card over the device's designated contactless landing zone, marked by the EMVCo Contactless Indicator symbol on the front face of the device.
3.  Wait for LED status:
    1.  Initially, LED 2 illuminates, signaling the device is processing. The device subsequently illuminates LED 3 and LED 4, indicating card detection. Notifications are then sent to identify the card type and UID.
    2.  The Host application can further interact with the NFC Tag using pass-through commands. For details, see **D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS).**
    3.  If the pass-through command is the last successful command, the device will end the transaction, emitting a single beep signaling a successful transaction. The user then needs to remove the card.
    4.  If an error is detected, the device will end the transaction and emit two beeps to signal the error. The user then needs to remove the card.
4.  The device notifies the host that the transaction has ended with the NFC Tag removed.

# Maintenance

## Mechanical Maintenance

| ![](<DynaFlex II Go Images/bdb6a105147891251b84fbdb350ba870.png>)                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DO NOT use liquid cleaning products or insert any other objects into the device.  DO NOT apply any liquid directly onto the device, to avoid seepage into the electronics. |

Periodic cleaning of the device’s exterior may be required. To clean the outside of DynaFlex II Go products, wipe down the device with a soft, slightly damp cloth and then wipe dry with a lint-free cloth. The graphic overlay on the face of the device can also be cleaned using a slightly damp specialty cleaning cloth, like those used to wipe lenses, monitors, and smartphone displays.

## Updates to Firmware, Documentation, Security Guidance

In addition to the security guidance in the product manuals, MagTek may provide updates to this document, as well as supplemental security guidance or notices regarding vulnerabilities, at [www.magtek.com](http://www.magtek.com). MagTek advises checking the product’s home page periodically for the most up-to-date information.

Any firmware updates addressing product features, bugs, or security vulnerabilities are also posted to [www.magtek.com](http://www.magtek.com) or may be sent directly to affected customers. To update the device’s firmware:

1.  Obtain the firmware image to install from your MagTek representative.
2.  Download **1000007406 DynaFlex, DynaProx Test Utility** from the MagTek web site.
3.  Follow the instructions in **D998200402 DynaFlex, DynaProx Utility User Manual (Windows)** included in the firmware update utility’s **Docs** subfolder.

# Developing Custom Software

Custom host software uses the same underlying device command set for all DynaFlex II Go product connection types. This section provides high-level information about communicating with the device via the various physical connection types in various software development frameworks, and provides pointers to available SDKs, which include sample code. Product documentation and SDKs are available for download by searching for the product name on [www.magtek.com](http://www.magtek.com) and navigating to the **Support** tab.

MagTek provides convenient SDKs and corresponding documentation for many programming languages and operating systems. The API libraries included in the SDKs wrap the details of the connection in an interface that conceptually parallels the device’s internal operation, freeing software developers to focus on the business logic, without having to deal with the complexities of platform APIs for connecting to the various available connection types, communicating using the various available protocols, and parsing the various available data formats. Information about using MagTek wrapper APIs is available in separate documentation, including:

-   **D998200380 MagTek Universal SDK Programmer’s Manual (Microsoft .NET)**
-   **D998200381 MagTek Universal SDK Programmer’s Manual (Microsoft C++ )**
-   **D998200385 MagTek Universal SDK for MMS Devices Programmer’s Manual (Java)**
-   **D998200386 MagTek Universal SDK for MMS Devices Programmer’s Manual (iOS)**
-   **D998200387 MagTek Universal SDK Programmer’s Manual (Android)**

The documentation is bundled with the SDKs themselves, which include:

-   **1000007351 MagTek Universal SDK for MMS Devices (Windows)**
-   **1000007352 MagTek Universal SDK for MMS Devices (Android)**

The SDKs and corresponding documentation include:

-   Functions for sending the direct commands described in this manual
-   Wrappers for commonly used commands that further simplify development
-   Sample source code to demonstrate how to communicate with the device using the direct commands described in this manual

To download the SDKs and documentation, search [www.magtek.com](http://www.magtek.com) for “SDK” and select the SDK and documentation for the programming languages and platforms you need or contact MagTek Support Services for assistance.

In addition to the SDK API libraries, software developers also have the option to revert to direct communication with the device using libraries using the operating system’s native USB and serial port libraries. For example, custom software written in Visual Basic or Visual C++ may make API calls to the standard Windows USB HID driver. For more information about sending commands directly, see **D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS).**

For more information about developing custom applications that integrate with DynaFlex II Go, see the MagTek web site or contact your reseller or MagTek Support Services.

###### Technical Specifications

| DynaFlex II Go Products Technical Specifications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference Standards and Certifications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                      |
| ISO 7810, ISO 7811, AAMVA ISO/IEC 7816-1, 2, 3, & 4 Identification Cards Integrated Circuits with Contacts EMV ICC Specifications for Payment Systems Version 4.3d, L1 Contact and Version 4.4a, L2 Contact EMV Contactless Level 1 Version 3.1a MasterCard TQM MCL v3.1.4, payWave v2.2c, Expresspay 4.1, D-PAS Terminal Payment Application v2.0 PCI PTS POI v6.2 SCR DUKPT TDES, AES 128 DUKPT FCC Part 15 Low Power Transceiver, RX verified per FCC Title 47 Part 15 Subclass C UL/CSA/IEC 62368-1, 2nd edition CE Certified CE Safety: IEC 62368-1: 2014 Canada ISED Certified AS/NZS CISPR 32 (2013), AS/NZS 4268 Table 1, Row 59 DTS 2400-2483MHz SRD (802.11), and AS/NZS 4268 (2017) Table 1, Row 43 13.553-13.567MHz (contactless reader) RoHS Compliant the Electrical and Electronic Equipment (EEE) Reduction of Hazardous Substances (RoHS) European Directive 2002/95/EC California Proposition 65 (California) IPC-A-610 Class II Assembly EU Directive Waste Electrical and Electronic Equipment (WEEE) EU Directive Restriction of Hazardous Substances (RoHS) Universal Serial Bus Specifications 1.1, 2.0 AES-128 and AES-256 Encryption Apple VAS iAP2® Protocol Support Bluetooth® Core Specification 5.2 |                                                                                                                                                                                                                                                                                                                                                      |
| Physical Characteristics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                      |
| Dimensions (L x W x H):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 2.76 in. x 2.57 in. x .79 in. (70.10mm x 65.3mm x20.1mm)                                                                                                                                                                                                                                                                                             |
| Weight                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | DynaFlex II Go = 3.17 oz. (90g) DynaFlex II Go BCR = 3.24 oz. (92g)                                                                                                                                                                                                                                                                                  |
| Supported Mounting Options:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Mounting to host via external clip or embedded lanyard                                                                                                                                                                                                                                                                                               |
| Reader Characteristics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                      |
| Magnetic Stripe Reader:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Three track bidirectional encrypting reader with MagnePrint                                                                                                                                                                                                                                                                                          |
| Magnetic Stripe Decoding:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Financial (ISO Type B), AAMVA, or Other                                                                                                                                                                                                                                                                                                              |
| Magnetic Swipe Speeds:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 6 inches per second to 60 inches per second                                                                                                                                                                                                                                                                                                          |
| EMV Contact Reader:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | EMVCo L1 and L2 Contact Reader                                                                                                                                                                                                                                                                                                                       |
| EMV Contactless Reader:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | EMVCo L1 and L2 Contactless Reader D-PAS, PayPass/MCL, payWave, Expresspay Mobile wallets including but not limited to Apple Pay, Google Pay, Samsung Pay                                                                                                                                                                                            |
| Barcode Reader:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Barcode Media: Labels, paper, smartphone / computer displays Barcode Types: QR Codes, Linear Barcodes, UPC-A, UPC-E, Code 128, PDF417 / Data Matrix, Aztec, etc. Field Of View 31.5° total vertical sweep, 42° total horizontal sweep, perpendicular to device face Depth Of Field 1.2 in. (30mm) to 13.8 in. (350mm) Integrated white indicator LED |
| User Interface Characteristics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                      |
| Status Indicators:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 4 Monochrome Green LEDs 1 Integrated white indicator LED for BCR                                                                                                                                                                                                                                                                                     |
| Display Type:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Not Applicable                                                                                                                                                                                                                                                                                                                                       |
| Keypad:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Not Applicable                                                                                                                                                                                                                                                                                                                                       |
| Security Characteristics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                      |
| Certifications:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | PCI PTS POI v6.2 Certified Secure Card Reader (SCR)                                                                                                                                                                                                                                                                                                  |
| Tamper Protection:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The enclosure and associated electronics form a Tamper Resistant Security Module (TRSM) where attempts to penetrate or modify the unit cause all cryptographic keys to be cleared or rendered unusable.                                                                                                                                              |
| Electrical Characteristics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                      |
| Power Inputs:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | USB powered via USB-C receptacle                                                                                                                                                                                                                                                                                                                     |
| Power Outputs:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | None                                                                                                                                                                                                                                                                                                                                                 |
| Rechargeable Battery Type:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Lithium-Ion Polymer (LiPo)                                                                                                                                                                                                                                                                                                                           |
| Voltage Requirements:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 5 VDC                                                                                                                                                                                                                                                                                                                                                |
| Current Requirements:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 500 mA Maximum                                                                                                                                                                                                                                                                                                                                       |
| Data Storage:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Not Applicable                                                                                                                                                                                                                                                                                                                                       |
| Communication Characteristics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                      |
| Wired Connection Types:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | USB-C, compatible with USB 1.1, USB 2.0, USB 3.0 Vendor-defined USB Human Interface Device (HID) data format                                                                                                                                                                                                                                         |
| Wireless Connection Types:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | None                                                                                                                                                                                                                                                                                                                                                 |
| RF Exposure:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | SAR Certified                                                                                                                                                                                                                                                                                                                                        |
| Software Characteristics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                      |
| Tested Operating System(s):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | USB Hosts: Windows 11                                                                                                                                                                                                                                                                                                                                |
| Environmental Resistance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                      |
| Ingress Protection:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | IP30                                                                                                                                                                                                                                                                                                                                                 |
| Operating Temperature:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | DynaFlex II Go/DynaFlex II Go BCR: 32°F to 95°F (0°C to 35°C)                                                                                                                                                                                                                                                                                        |
| Operating Relative Humidity:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Up to 90% RH non-condensing                                                                                                                                                                                                                                                                                                                          |
| Storage Temperature:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | DynaFlex II Go/DynaFlex II Go BCR: -4°F to 113°F (-20°C to 45°C)                                                                                                                                                                                                                                                                                     |
| Storage Relative Humidity:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Up to 90% RH non-condensing                                                                                                                                                                                                                                                                                                                          |
| Vibration Resistance:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | None                                                                                                                                                                                                                                                                                                                                                 |
| Shock Resistance:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | None                                                                                                                                                                                                                                                                                                                                                 |
| ESD Tolerance (EMVCo):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ±12.0 kV air discharge / 5 different paddles                                                                                                                                                                                                                                                                                                         |
| ESD Tolerance (FCC/CE):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | ±8kV air discharge / ±4kV contact discharge                                                                                                                                                                                                                                                                                                          |
| Vapor Resistance:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | None                                                                                                                                                                                                                                                                                                                                                 |
| Reliability                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                      |
| Shelf Life:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 60 Months Minimum                                                                                                                                                                                                                                                                                                                                    |
| Magnetic Read Head Life:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 500k Swipes                                                                                                                                                                                                                                                                                                                                          |
| Battery Shelf Life:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 5 years or longer (backup battery)                                                                                                                                                                                                                                                                                                                   |
| Battery Cycle Life:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | NA                                                                                                                                                                                                                                                                                                                                                   |

###### Barcode Reader Symbologies

Barcode symbology refers to the way in which data is encoded in a barcode. It uses either spaced lines, dots, or squares. When read, these symbols are decoded and converted to data. The table below lists all of the supported symbologies and which are enabled by default.

Table 8 - Barcode Reader Supported Symbologies

| Symbology             | Default  |
|-----------------------|----------|
| AIM 128               | Disabled |
| Aztec                 | Enabled  |
| Codabar               | Enabled  |
| Code 11               | Disabled |
| Code128               | Enabled  |
| Code 32               | Disabled |
| Code 39               | Enabled  |
| Code 93               | Disabled |
| Data Matrix           | Enabled  |
| EAN-8                 | Enabled  |
| EAN-13                | Enabled  |
| Febraban              | Disabled |
| GSI-128 (UCC/EAN-128) | Enabled  |
| GS1 Databar (RSS)     | Disabled |
| Industrial 25         | Disable  |
| Interleaved 2 of 5,   | Enabled  |
| ISSN                  | Disabled |
| ISBN                  | Disabled |
| ITF-14                | Disabled |
| ITF-6                 | Disabled |
| Matrix 2 of 5         | Enabled  |
| Micro QR              | Disabled |
| MSI Plessey           | Disabled |
| PDF417                | Enabled  |
| Plessey               | Disabled |
| QR Code               | Enabled  |
| Standard 25           | Disabled |
| UPC-E                 | Enabled  |
| UPC-A                 | Enabled  |

###### Optional Accessories

Tailored for use with mobile handsets, tablets, and desktop computers, DynaFlex II Go offers a variety of accessories designed to meet a wide range of operational needs.

| **Part Number**                                     | **Description**                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **21078408** DYNAFLEX II GO, KIT COUNTERTOP STAND   | The Countertop Stand is well-suited for countertop placement or battery charging, providing a convenient and secure means of positioning the device.  ![A diagram of a computer power cord Description automatically generated with medium confidence](<DynaFlex II Go Images/7b60e808419f9cce16d11980d5779d17.png>)                                                                             |
| **21078409** DYNAFLEX II GO ADAPTOR FOR OTTERBOX    | Users can take advantage of the OtterBox® uniVERSE® adaptor for easy sliding and connection to a wide range of mobile devices, including phones and tablets. ![A black plastic holder with two clips Description automatically generated with medium confidence](<DynaFlex II Go Images/1ffb652d971598bec988c635b3c9553d.jpeg>)![](<DynaFlex II Go Images/cfbf04b67290a1181cf273537c30da86.png>) |
| **21078410** DYNAFLEX II GO RUBBER SLEEVE           | DynaFlex II Go can be equipped with a full-rubber sleeve specifically engineered to enhance the device's ingress protection.![](<DynaFlex II Go Images/2b229e80a06fe29d5be8720577a7568a.jpeg>)![](<DynaFlex II Go Images/3a515eb97f676870213cce76e53604ec.png>)                                                                                                                                  |
| **21078411** DYNAFLEX II GO RUBBER SLEEVE HALF SIZE | DynaFlex II Go offers the option to install a half-rubber sleeve, intended to boost the device's ingress protection when utilizing the OtterBox® uniVERSE® adaptor for DynaFlex II Go.![](<DynaFlex II Go Images/f10988ed25312bf2d7b8565d382d9ed6.jpeg>)![A blueprint of a computer device Description automatically generated](<DynaFlex II Go Images/73a762a2e8aa5c70adb880cc91189825.png>)    |

###### Warranty, Standards, and Certifications

**Limited Warranty**

MagTek warrants that the products sold pursuant to this Agreement will perform in accordance with MagTek’s published specifications. This warranty shall be provided only for a period of one year from the date of the shipment of the product from MagTek (the “Warranty Period”). This warranty shall apply only to the “Buyer” (the original purchaser, unless that entity resells the product as authorized by MagTek, in which event this warranty shall apply only to the first repurchaser).

During the Warranty Period, should this product fail to conform to MagTek’s specifications, MagTek will, at its option, repair or replace this product at no additional charge except as set forth below. Repair parts and replacement products will be furnished on an exchange basis and will be either reconditioned or new. All replaced parts and products become the property of MagTek. This limited warranty does not include service to repair damage to the product resulting from accident, disaster, unreasonable use, misuse, abuse, negligence, or modification of the product not authorized by MagTek. MagTek reserves the right to examine the alleged defective goods to determine whether the warranty is applicable.

Without limiting the generality of the foregoing, MagTek specifically disclaims any liability or warranty for goods resold in other than MagTek’s original packages, and for goods modified, altered, or treated without authorization by MagTek.

Service may be obtained by delivering the product during the warranty period to MagTek (1710 Apollo Court, Seal Beach, CA 90740). If this product is delivered by mail or by an equivalent shipping carrier, the customer agrees to insure the product or assume the risk of loss or damage in transit, to prepay shipping charges to the warranty service location, and to use the original shipping container or equivalent. MagTek will return the product, prepaid, via a three (3) day shipping service. A Return Material Authorization (“RMA”) number must accompany all returns. Buyers may obtain an RMA number by contacting MagTek Support Services at (562) 546-6800.

**Each buyer understands that this MagTek product is offered as-is. MagTek makes no other warranty, express or implied, and MagTek disclaims any warranty of any other kind, including any warranty of merchantability or fitness for a particular purpose.**

**If this product does not conform to MagTek’s specifications, the sole remedy shall be repair or replacement as provided above. MagTek’s liability, if any, shall in no event exceed the total amount paid to MagTek under this agreement. In no event will MagTek be liable to the Buyer for any damages, including any lost profits, lost savings, or other incidental or consequential damages arising out of the use of, or inability to use, such product, even if MagTek has been advised of the possibility of such damages, or for any claim by any other party.**

**Limitation On Liability**

Except as provided in the sections relating to MagTek’s Limited Warranty, MagTek’s liability under this agreement is limited to the contract price of this product.

MagTek makes no other warranties with respect to the product, expressed or implied, except as may be stated in this agreement, and MagTek disclaims any implied warranty, including without limitation any implied warranty of merchantability or fitness for a particular purpose.

MagTek shall not be liable for contingent, incidental, or consequential damages to persons or property. MagTek further limits its liability of any kind with respect to the product, including negligence on its part, to the contract price for the goods.

MagTek’s sole liability and buyer’s exclusive remedies are stated in this section and in the section relating to MagTek’s Limited Warranty.

**FCC Information**

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) This device must accept any interference received, including interference that may cause undesired operation.

Note: This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates, uses and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

-   Reorient or relocate the receiving antenna.
-   Increase the separation between the equipment and receiver.
-   Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
-   Consult the dealer or an experienced radio/TV technician for help.

**Caution: Changes or modifications not expressly approved by MagTek could void the user’s authority to operate this equipment.**

**Canadian Declaration Of Conformity**

This digital apparatus does not exceed the Class B limits for radio noise from digital apparatus set out in the Radio Interference Regulations of the Canadian Department of Communications.

Le présent appareil numérique n’émet pas de bruits radioélectriques dépassant les limites applicables aux appareils numériques de la classe B prescrites dans le Réglement sur le brouillage radioélectrique édicté par le ministère des Communications du Canada.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe B est conformé à la norme NMB-003 du Canada.

**Industry Canada (IC) RSS**

This device complies with Industry Canada licence-exempt RSS standard(s). Operation is subject to the following two conditions: (1) This device may not cause interference, and (2) This device must accept any interference, including interference that may cause undesired operation of the device.

Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) L'appareil ne doit pas produire de brouillage, et (2) L'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

**CUR/UR**

This product is recognized per Underwriter Laboratories and Canadian Underwriter Laboratories 1950.

**CE STANDARDS**

Testing for compliance with CE requirements was performed by an independent laboratory. The unit under test was found compliant with standards established for Class B devices.

**EU Statement**

Hereby, MagTek Inc. declares that the radio equipment types **Wideband Transmission System** (802.11 wireless and Bluetooth® Low Energy), and **Non-Specific Short Range Device** (contactless) are in compliance with **Directive 2014/53/EU**. The full text of the EU declarations of conformity is available at the following internet addresses:

-   https://www.magtek.com/Content/DocumentationFiles/D998200650.pdf

**UKCA Statement**

Hereby, MagTek Inc. declares that the radio equipment types **Wideband Transmission System** (802.11 wireless and Bluetooth® Low Energy), and **Non-Specific Short Range Device** (contactless) are in compliance with **Directive 2014/53/EU**. The full text of the EU declarations of conformity is available at the following internet address:

-   <https://www.magtek.com/Content/DocumentationFiles/D998200651.pdf>

**Australia / New Zealand Statement**

Testing for compliance with AS/NZS standards was performed by a registered and accredited laboratory. Per Subclause 53(4) of Part 15 of Schedule 5 to the General Equipment Rules, DynaFlex II GO meets the requirements of the Short-Range Equipment Standard as tested in **EN 300 330 V2.1.1 (2017-02)**. The AS declaration of conformity is available at the following internet address:

-   <https://www.magtek.com/Content/DocumentationFiles/D998200700.pdf>

**RoHS STATEMENT**

When ordered as RoHS compliant, this product meets the Electrical and Electronic Equipment (EEE) Reduction of Hazardous Substances (RoHS) Directive (EU) 2015/863 amending Annex II to Directive 2011/65/EU. The marking is clearly recognizable, either as written words like “Pb-free,” “lead-free,” or as another clear symbol (![PbFreeSym](<DynaFlex II Go Images/4d77d9668e7bdc54b2ee2546cc21077c.png>)).

**PCI Statement**

PCI Security Standards Council, LLC (“PCI SSC”) has approved this PIN Transaction Security Device to be in compliance with PCI SSC’s PIN Security Requirements.

When granted, PCI SSC approval is provided by PCI SSC to ensure certain security and operational characteristics important to the achievement of PCI SSC’s goals, but PCI SSC approval does not under any circumstances include any endorsement or warranty regarding the functionality, quality or performance of any particular product or service. PCI SSC does not warrant any products or services provided by third parties. PCI SSC approval does not under any circumstances include or imply any product warranties from PCI SSC, including, without limitation, any implied warranties of merchantability, fitness for purpose, or non-infringement, all of which are expressly disclaimed by PCI SSC. All rights and remedies regarding products and services which have received PCI SSC approval shall be provided by the party providing such products or services, and not by PCI SSC.

**Safety**

This product has been tested to **IEC 62368-1 -Audio/Video, information and communication technology equipment - Part 1**: General Requirements and U.S. (**UL 62368-1**), Canadian, Australian & New Zealand National Deviations by an ISO 17025 Accredited Testing Laboratory.

**This document is written specifically to work in conjunction with these safety and integrity features to protect the user and the device. It is very important to follow all steps in the product documentation carefully, in the order in which they are described, and at the recommended times. Failure to do so could result in personal injury, and / or cause damage to the device, and / or void the product warranty.**

**Safety Requirements**

| ![A picture containing text, font, graphics, logo Description automatically generated](<DynaFlex II Go Images/bdb6a105147891251b84fbdb350ba870.png>)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Never do any of the following:** DO NOT use a ground adapter plug to connect equipment to a power socket-outlet that lacks a ground connection terminal. DO NOT attempt any maintenance function that is not specifically described in this manual or in other ExpressCard 3000 instructional documents published by MagTek. DO NOT remove any of the covers or guards that are fastened with screws. There are no user-serviceable areas within these covers. DO NOT override or “cheat” electrical or mechanical interlock devices. DO NOT use EC3000 supplies or cleaning materials for other than their intended purposes. DO NOT operate the equipment if you or anyone else have noticed unusual noises or odors.  **Consider the following before operating the ExpressCard 3000:** Connect the EC3000 to a properly grounded AC power socket-outlet. If in doubt, have the socket-outlet checked by a qualified electrician. Improper connection of the device’s grounding conductor creates a risk of electric shock. Place the EC3000 on a solid surface that can safely support the device’s weight plus the weight of a person leaning against it (such as a service technician). Be careful when moving or relocating the device. Use proper lifting techniques. Use materials and supplies specifically designed for MagTek devices. Using unsuitable materials may result in poor performance, and in some cases may be hazardous. |

**SOFTWARE LICENSE AGREEMENT**

**IMPORTANT:** YOU SHOULD CAREFULLY READ ALL THE TERMS, CONDITIONS AND RESTRICTIONS OF THIS LICENSE AGREEMENT BEFORE INSTALLING THE SOFTWARE PACKAGE. YOUR INSTALLATION OF THE SOFTWARE PACKAGE PRESUMES YOUR ACCEPTANCE OF THE TERMS, CONDITIONS, AND RESTRICTIONS CONTAINED IN THIS AGREEMENT. IF YOU DO NOT AGREE WITH THESE TERMS, CONDITIONS, AND RESTRICTIONS, PROMPTLY RETURN THE SOFTWARE PACKAGE AND ASSOCIATED DOCUMENTATION TO THE ADDRESS IN THIS DOCUMENT, ATTENTION: CUSTOMER SUPPORT.

**TERMS, CONDITIONS, AND RESTRICTIONS**

MagTek, Incorporated (the "Licensor") owns and has the right to distribute the described software and documentation, collectively referred to as the "Software."

**LICENSE:** Licensor grants you (the "Licensee") the right to use the Software in conjunction with MagTek products. LICENSEE MAY NOT COPY, MODIFY, OR TRANSFER THE SOFTWARE IN WHOLE OR IN PART EXCEPT AS EXPRESSLY PROVIDED IN THIS AGREEMENT. Licensee may not decompile, disassemble, or in any other manner attempt to reverse engineer the Software. Licensee shall not tamper with, bypass, or alter any security features of the software or attempt to do so.

**TRANSFER:** Licensee may not transfer the Software or license to the Software to another party without the prior written authorization of the Licensor. If Licensee transfers the Software without authorization, all rights granted under this Agreement are automatically terminated.

**COPYRIGHT:** The Software is copyrighted. Licensee may not copy the Software except for archival purposes or to load for execution purposes. All other copies of the Software are in violation of this Agreement.

**TERM:** This Agreement is in effect as long as Licensee continues the use of the Software. The Licensor also reserves the right to terminate this Agreement if Licensee fails to comply with any of the terms, conditions, or restrictions contained herein. Should Licensor terminate this Agreement due to Licensee's failure to comply, Licensee agrees to return the Software to Licensor. Receipt of returned Software by the Licensor shall mark the termination.

**LIMITED WARRANTY:** Licensor warrants to the Licensee that the disk(s) or other media on which the Software is recorded are free from defects in material or workmanship under normal use.

THE SOFTWARE IS PROVIDED AS IS. LICENSOR MAKES NO OTHER WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

Because of the diversity of conditions and hardware under which the Software may be used, Licensor does not warrant that the Software will meet Licensee specifications or that the operation of the Software will be uninterrupted or free of errors.

IN NO EVENT WILL LICENSOR BE LIABLE FOR ANY DAMAGES, INCLUDING ANY LOST PROFITS, LOST SAVINGS, OR OTHER INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE, OR INABILITY TO USE THE SOFTWARE. Licensee's sole remedy in the event of a defect in material or workmanship is expressly limited to replacement of the Software disk(s) if applicable.

**GOVERNING LAW:** If any provision of this Agreement is found to be unlawful, void, or unenforceable, that provision shall be removed from consideration under this Agreement and will not affect the enforceability of any of the remaining provisions. This Agreement shall be governed by the laws of the State of California and shall inure to the benefit of MagTek, Incorporated, its successors or assigns.

**ACKNOWLEDGMENT:** LICENSEE ACKNOWLEDGES THAT LICENSEE HAS READ THIS AGREEMENT, UNDERSTANDS ALL OF ITS TERMS, CONDITIONS, AND RESTRICTIONS, AND AGREES TO BE BOUND BY THEM. LICENSEE ALSO AGREES THAT THIS AGREEMENT SUPERSEDES ANY AND ALL VERBAL AND WRITTEN COMMUNICATIONS BETWEEN LICENSOR AND LICENSEE OR THEIR ASSIGNS RELATING TO THE SUBJECT MATTER OF THIS AGREEMENT.

QUESTIONS REGARDING THIS AGREEMENT SHOULD BE ADDRESSED IN WRITING TO MAGTEK, INCORPORATED, ATTENTION: CUSTOMER SUPPORT, AT THE ADDRESS LISTED IN THIS DOCUMENT, OR E-MAILED TO SUPPORT@MAGTEK.COM.

**DEMO SOFTWARE / SAMPLE CODE**: Unless otherwise stated, all demo software and sample code are to be used by Licensee for demonstration purposes only and MAY NOT BE incorporated into any production or live environment. The PIN Pad sample implementation is for software PIN Pad test purposes only and is not PCI compliant. To meet PCI compliance in production or live environments, a third-party PCI compliant component (hardware or software-based) must be used.
