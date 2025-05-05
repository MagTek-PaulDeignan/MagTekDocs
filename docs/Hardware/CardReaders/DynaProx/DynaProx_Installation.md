---
title: Installation and Opertation Manual
layout: home
parent: DynaProx
nav_order: 1
---
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><p>DynaProx</p>
<p>EMV Contactless/NFC Card Reader and Writer</p>
<p>Installation and Operation Manual</p></td>
</tr>
<tr>
<td><img src="./media/media/image1.png"
style="width:3.05in;height:3in" /></td>
</tr>
<tr>
<td><p>April 2025</p>
<p>Document Number:</p>
<p>D998200490-402</p>
<p>REGISTERED TO ISO 9001:2015</p></td>
</tr>
</tbody>
</table>

Copyright © 2006 - 2024 MagTek, Inc.

Printed in the United States of America

information in this publication is subject to change without notice.
MagTek cannot be held liable for any use of the contents of this
document. Any changes or improvements made to this product will be
included in the next publication release. If you have questions about
specific features and functions or when they will become available,
please contact your MagTek representative.

MagTek®, MagnePrint®, and MagneSafe® are registered trademarks of
MagTek, Inc.

Magensa™ is a trademark of MagTek, Inc.

AAMVA™ is a trademark of AAMVA.

American Express® and EXPRESSPAY FROM AMERICAN EXPRESS® are registered
trademarks of American Express Marketing & Development Corp.

D-PAYMENT APPLICATION SPECIFICATION® is a registered trademark of
Discover Financial Services CORPORATION

MasterCard® is a registered trademark and PayPass™ and Tap & Go™ are
trademarks of MasterCard International Incorporated.

Visa® and Visa payWave® are registered trademarks of Visa International
Service Association.

ANSI®, the ANSI logo, and numerous other identifiers containing "ANSI"
are registered trademarks, service marks, and accreditation marks of the
American National Standards Institute (ANSI).

ISO® is a registered trademark of the International Organization for
Standardization.

UL™ and the UL logo are trademarks of UL LLC.

PCI Security Standards Council® is a registered trademark of the PCI
Security Standards Council, LLC.

EMV® is a registered trademark in the U.S. and other countries and an
unregistered trademark elsewhere. The EMV trademark is owned by EMVCo,
LLC. The Contactless Indicator mark, consisting of four graduating arcs,
is a trademark owned by and used with permission of EMVCo, LLC.

The *Bluetooth*® word mark and logos are registered trademarks owned by
Bluetooth SIG, Inc. and any use of such marks by MagTek is under
license.

Google Play™ store, Google Wallet™ payment service, and Android™
platform are trademarks of Google LLC.

Apple Pay®, Apple Wallet®, iPhone®, iPod®, Mac®, and OS X® are
registered trademarks of Apple Inc., registered in the U.S. and other
countries. iPad™ is a trademark of Apple. Inc. App StoreSM is a service
mark of Apple Inc., registered in the U.S. and other countries. Apple
and MFi are registered trademarks of Apple Inc. IOS is a trademark or
registered trademark of Cisco in the U.S. and other countries and is
used by Apple Inc. under license.

MIFARE®, MIFARE Classic ®, and MIFARE® DESFire®, are registered
trademarks of NXP Semiconductors Austria GmbH Styria, All rights
reserved.

Microsoft®, Windows®, and .NET® are registered trademarks of Microsoft
Corporation.

All other system names and product names are the property of their
respective owners.

Table ‑ - Revisions

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 21%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">Rev Number</th>
<th style="text-align: center;">Date</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">10</td>
<td style="text-align: center;">June 1, 2022</td>
<td>Initial release</td>
</tr>
<tr>
<td style="text-align: center;">11</td>
<td style="text-align: center;">July 13, 2022</td>
<td><p>Replaced the word “Plain” with the word “Plane”.</p>
<p>Changed - Operating Temperature to:</p>
<p>DynaProx: -22°F to 185°F (-30°C to 85°C) – DynaProx BCR: -4F to 131°F
(-20°C to 55°C)</p>
<p>Changed Storage Temperature to:</p>
<p>DynaProx: -30°C to 85°C (-22°F to 185°F) – DynaProx BCR: -30°C to
70°C (-22°F to 158°F)</p></td>
</tr>
<tr>
<td style="text-align: center;">20</td>
<td style="text-align: center;">November 2, 2022</td>
<td>Updated PCI listing to PCI PTS POI v6.1</td>
</tr>
<tr>
<td style="text-align: center;">30</td>
<td style="text-align: center;">January 13, 2023</td>
<td>Minor grammatical changes throughout document. Update <strong>Table
4‑1 - RS-232 Signals,</strong> Update section <strong>6.6.1 About
Power</strong></td>
</tr>
<tr>
<td style="text-align: center;">40</td>
<td style="text-align: center;">February 10, 2023</td>
<td><p>Update <strong>1.1 Key Features</strong> to include Apple VAS for
DynaProx</p>
<p>Add <strong>6.7.4 Apple VAS for DynaProx</strong> Add
<strong>Appendix B Barcode Reader Symbologies</strong></p></td>
</tr>
<tr>
<td style="text-align: center;">41</td>
<td style="text-align: center;">May 1, 2023</td>
<td>Add section <strong>6.3 Introduction to User Interface;</strong> Add
section <strong>6.6.3 About Maintenance Reset;</strong> Update section
<strong>2.1 Logistical Planning</strong> with current metal interface
guidance.</td>
</tr>
<tr>
<td style="text-align: center;">42</td>
<td style="text-align: center;">August 22, 2023</td>
<td>Update <strong>1.1 Key Features</strong> to include NFC Tag; Add
section Error! Reference source not found. Error! Reference source not
found.<strong>.</strong></td>
</tr>
<tr>
<td style="text-align: center;">43</td>
<td style="text-align: center;">September 12, 2023</td>
<td>Update IK Rating in Section <strong>1.1 Key Features from</strong>
IK09 to IK08</td>
</tr>
<tr>
<td style="text-align: center;">44</td>
<td style="text-align: center;">December 27, 2023</td>
<td>Update section Error! Reference source not found. include Mifare
Classic and Mifare DESFire Light Card; Update <strong>1.1 Key
Features</strong> to include Buzzer Application; Add section
<strong>6.5.1 How to Play a Sequence of Tones.</strong></td>
</tr>
<tr>
<td style="text-align: center;">400</td>
<td style="text-align: center;">February 13, 2024</td>
<td>Updated <strong>Figure 4‑16 - Recommended Disassembly
Procedure</strong> to change the mounting hole dimension 1.336"[33.93mm]
to 1.20"[30.5mm], Updated Ingress Protection Rating from 65 to 66 in
<strong>1.1 Key Features</strong> and <strong>Appendix A Technical
Specifications.</strong></td>
</tr>
<tr>
<td style="text-align: center;">401</td>
<td style="text-align: center;">March 13, 2024</td>
<td>Updated section <strong>4.3.1 About Connecting to a Host</strong>
and <strong>Appendix A Technical Specifications</strong> with updated
guidelines regarding cable length and quality.</td>
</tr>
<tr>
<td style="text-align: center;">402</td>
<td style="text-align: center;">April 3, 2025</td>
<td>Add MIFARE Ultralight, MIFARE Plus, remove Lite in <strong>6.7.5 How
to Tap Contactless NFC Tags / MIFARE Ultralight / MIFARE Classic /
MIFARE DESFire /MIFARE Plus Cards and</strong> Send Pass-through
Commands</td>
</tr>
</tbody>
</table>

# Table of Contents

[Table of Contents [4](#table-of-contents)](#table-of-contents)

[1 Introduction [6](#introduction)](#introduction)

[1.1 Key Features [6](#key-features)](#key-features)

[1.2 Build for New Markets
[6](#build-for-new-markets)](#build-for-new-markets)

[1.3 Easier Integration [6](#easier-integration)](#easier-integration)

[1.4 About DynaProx Components
[7](#about-dynaprox-components)](#about-dynaprox-components)

[1.5 Available Models and Accessories
[8](#available-models-and-accessories)](#available-models-and-accessories)

[1.6 About Terminology [9](#about-terminology)](#about-terminology)

[2 Planning and Preparation
[10](#planning-and-preparation)](#planning-and-preparation)

[2.1 Logistical Planning
[10](#logistical-planning)](#logistical-planning)

[3 Handling and Storage
[12](#handling-and-storage)](#handling-and-storage)

[3.1 Handling to Avoid Damage
[12](#handling-to-avoid-damage)](#handling-to-avoid-damage)

[3.2 Handling to Avoid Accidental Tamper
[12](#handling-to-avoid-accidental-tamper)](#handling-to-avoid-accidental-tamper)

[4 Installation [13](#installation)](#installation)

[4.1 About Inspection [13](#about-inspection)](#about-inspection)

[4.2 About Host Software
[13](#about-host-software)](#about-host-software)

[4.3 Connecting to a Host
[13](#connecting-to-a-host)](#connecting-to-a-host)

[4.3.1 About Connecting to a Host
[13](#about-connecting-to-a-host)](#about-connecting-to-a-host)

[4.3.2 How to Connect DynaProx to a Host via USB
[14](#how-to-connect-dynaprox-to-a-host-via-usb)](#how-to-connect-dynaprox-to-a-host-via-usb)

[4.3.3 How to Connect DynaProx to a Host via RS-232
[16](#how-to-connect-dynaprox-to-a-host-via-rs-232)](#how-to-connect-dynaprox-to-a-host-via-rs-232)

[4.3.3.1 RS-232 Cable [16](#rs-232-cable)](#rs-232-cable)

[4.3.3.2 Chassis Ground [17](#chassis-ground)](#chassis-ground)

[4.4 Mounting [17](#mounting)](#mounting)

[4.4.1 About Mounting [17](#about-mounting)](#about-mounting)

[4.4.2 How to Mount DynaProx
[17](#how-to-mount-dynaprox)](#how-to-mount-dynaprox)

[4.4.3 How to Mount the Stand
[22](#how-to-mount-the-stand)](#how-to-mount-the-stand)

[5 Configuration [26](#configuration)](#configuration)

[6 Operation [27](#operation)](#operation)

[6.1 About Operating Modes
[27](#about-operating-modes)](#about-operating-modes)

[6.2 Operation Overview [27](#operation-overview)](#operation-overview)

[6.3 Introduction to User Interface
[27](#introduction-to-user-interface)](#introduction-to-user-interface)

[6.3.1 Component Details [28](#component-details)](#component-details)

[6.3.2 Modes of Operation
[29](#modes-of-operation)](#modes-of-operation)

[6.3.2.1 Power On via USB Cable
[29](#power-on-via-usb-cable)](#power-on-via-usb-cable)

[6.3.2.2 USB Enumeration [30](#usb-enumeration)](#usb-enumeration)

[6.3.2.3 Payment Transaction
[30](#payment-transaction)](#payment-transaction)

[6.3.2.4 Payment Transaction Successful
[31](#payment-transaction-successful)](#payment-transaction-successful)

[6.3.2.5 Payment Transaction Unsuccessful
[32](#payment-transaction-unsuccessful)](#payment-transaction-unsuccessful)

[6.3.3 USB Power Supply [34](#usb-power-supply)](#usb-power-supply)

[6.3.4 RS-232 Power Supply
[34](#rs-232-power-supply)](#rs-232-power-supply)

[6.3.5 Adding an RS-232 Power Supply
[35](#adding-an-rs-232-power-supply)](#adding-an-rs-232-power-supply)

[6.3.6 Event Notification Mode
[36](#event-notification-mode)](#event-notification-mode)

[6.3.7 Bar Code Read Only
[36](#bar-code-read-only)](#bar-code-read-only)

[6.4 About the Status LEDs
[36](#about-the-status-leds)](#about-the-status-leds)

[6.5 About Sounds [37](#about-sounds)](#about-sounds)

[6.5.1 How to Play a Sequence of Tones
[37](#how-to-play-a-sequence-of-tones)](#how-to-play-a-sequence-of-tones)

[6.6 Power Management [38](#power-management)](#power-management)

[6.6.1 About Power [38](#about-power)](#about-power)

[6.6.2 How to Power On / Wake Up from Standby Mode / Power Off
[38](#how-to-power-on-wake-up-from-standby-mode-power-off)](#how-to-power-on-wake-up-from-standby-mode-power-off)

[6.6.3 About Maintenance Reset
[38](#about-maintenance-reset)](#about-maintenance-reset)

[6.7 Card Reading [38](#card-reading)](#card-reading)

[6.7.1 About Reading Cards
[38](#about-reading-cards)](#about-reading-cards)

[6.7.2 How to Tap Contactless Cards / Devices
[40](#how-to-tap-contactless-cards-devices)](#how-to-tap-contactless-cards-devices)

[6.7.3 How to Scan Barcodes
[42](#how-to-scan-barcodes)](#how-to-scan-barcodes)

[6.7.4 Apple VAS for DynaProx
[42](#apple-vas-for-dynaprox)](#apple-vas-for-dynaprox)

[6.7.4.1 VAS App and Payment Mode (Dual Mode)
[43](#vas-app-and-payment-mode-dual-mode)](#vas-app-and-payment-mode-dual-mode)

[6.7.4.2 VAS App Only Mode (VAS Mode)
[43](#vas-app-only-mode-vas-mode)](#vas-app-only-mode-vas-mode)

[6.7.4.3 VAS App or Payment Mode (Single Mode)
[43](#vas-app-or-payment-mode-single-mode)](#vas-app-or-payment-mode-single-mode)

[6.7.4.4 Payment Only Mode (Payment Mode)
[43](#payment-only-mode-payment-mode)](#payment-only-mode-payment-mode)

[6.7.5 How to Tap Contactless NFC Tags / MIFARE Classic / MIFARE DESFire
/MIFARE Plus Cards and Send Pass-through Commands
[43](#how-to-tap-contactless-nfc-tags-mifare-ultralight-mifare-classic-mifare-desfire-mifare-plus-cards-and-send-pass-through-commands)](#how-to-tap-contactless-nfc-tags-mifare-ultralight-mifare-classic-mifare-desfire-mifare-plus-cards-and-send-pass-through-commands)

[7 Maintenance [44](#maintenance)](#maintenance)

[7.1 Mechanical Maintenance
[44](#mechanical-maintenance)](#mechanical-maintenance)

[7.2 Updates to Firmware, Documentation, Security Guidance
[44](#updates-to-firmware-documentation-security-guidance)](#updates-to-firmware-documentation-security-guidance)

[8 Developing Custom Software
[45](#developing-custom-software)](#developing-custom-software)

[Appendix A Technical Specifications
[46](#technical-specifications)](#technical-specifications)

[Appendix B Barcode Reader Symbologies
[49](#barcode-reader-symbologies)](#barcode-reader-symbologies)

[Appendix C Warranty, Standards, and Certifications
[50](#warranty-standards-and-certifications)](#warranty-standards-and-certifications)

# Introduction

DynaProx and DynaProx BCR deliver the next generation in touchless
payment acceptance. Both models come standard with contactless EMV and
near field communication (NFC) technology for original equipment
manufacturers (OEM), merchants, banks, and other developers looking to
build a secure payment solution that accepts contactless EMV and NFC
payments. Ideal for kiosks, vending machines, unattended payment
terminals, and even countertop deployment with the optional stand,
touchless payment and barcode scanning are made fast, reliable, and
secure.

DynaProx and DynaProx BCR are equipped with the next generation of
security and the MagneSafe® Security Architecture (MSA). The design and
architecture meet the requirements for contactless EMV 3.0, PCI PTS POI
v6.1, and support triple DEA encryption with DUKPT Key Management.

## Key Features

DynaProx and DynaProx BCR are easy to install and configure, with key
features that include:

- Contactless EMV 3.0 approved.

- PCI PTS POI v6.1approved.

- Optical reading for many 2D and 1D barcodes including PayPal and Venmo
  (DynaProx BCR model required).

- Transducer for audio alerts.

- User configurable audio commands to play a sequence of tones.

- USB (USB-C) or RS-232 interface

- Triple DEA encryption / DUKPT key management.

- Impact protection - IK 08.

- Ingress protection - IP 66.

- Apple Pay® / Apple Wallet® (Apple VAS protocol support).

- NFC Compatibility: Smart cards and contactless IC products, including
  MIFARE Classic / MIFARE DESFire /MIFARE Plus cards, with the ability
  to send pass-through commands.

- Optional countertop stand.

- Hard mounting points to match common kiosk and ATM bezel mounts.

- Flexible cable management.

## Build for New Markets

Touchless payments are fast, convenient, and meet the needs of new
growing markets. Major banks and card issuers are investing in
contactless EMV cards and other barcodes. Combined with the rise of
mobile wallets like Apple Pay, Samsung Pay, Google Pay, and others,
there are major opportunities to deliver a reliable and affordable
contactless EMV, NFC, and barcode reading device that is used in a
variety of deployment scenarios.

## Easier Integration

Designed to simplify development efforts, DynaProx and DynaProx BCR are
available with either a USB or RS-232 interface (with power provided
over USB or separately powered for RS-232) and are compatible with
Windows and Android applications. The beeper provides auditory feedback
to cardholders and operators delivering a more universal appeal. Contact
a representative to find the best fit for your application and to
request the software developer kits (SDKs) and application programming
interfaces (APIs).

## About DynaProx Components

**Figure 1‑1** shows the major components of DynaProx with barcode
reader. Models without a barcode reader are identical to the diagram,
but do not have a camera and do not have a QR code printed on the front
face.

<figure>
<img src="./media/media/image3.png" style="width:6.5in;height:2.87986in"
alt="Diagram, engineering drawing Description automatically generated" />
<figcaption><p>- DynaProx Major Components</p></figcaption>
</figure>

## Available Models and Accessories

Table ‑ - Available Models and Options

| Part No. | Description | Display | Connection(s) | Notes |
|----|----|:--:|----|----|
| 21078013 | DYNAPROX, PCI, BLACK, USB AND RS-232 | None | USB-C, RS-232 | MS Windows, Mac OS, Linux; Android Phone |
| 21078028 | DYNAPROX, PCI, BCR, BLACK, USB AND RS-232 | None | USB-C, RS-232 | MS Windows, Mac OS, Linux; Android Phone |
| 21078043 | DYNAPROX, PCI, BLACK, USB AND RS-232, COUNTERTOP STAND | None | USB-C, RS-232 | MS Windows, Mac OS, Linux; Android Phone |
| 21078044 | DYNAPROX, PCI, BCR, BLACK, USB AND RS-232, COUNTERTOP STAND | None | USB-C, RS-232 | MS Windows, Mac OS, Linux; Android Phone |

<span id="_Ref72491325" class="anchor"></span>Table ‑ - DynaProx
Accessories

| Part \# | Description | Accessory Notes |
|----|----|----|
| 1000007268 | CABLE, USB-C 90° RIGHT ANGLE TO USB TYPE A MALE USB 2.0, 6FT | Included with DynaProx products |
| 1000005076 | CABLE, USB-C 90° RIGHT ANGLE TO USB TYPE A MALE USB 2.0, 3FT | Optional, specify in order |
| 21078012 | DYNAPROX, KIT COUNTERTOP STAND | Kit only |
| 1000007189 | DynaProx Gasket | One (1) included with each DynaProx products. Replacement gaskets specify in order. |

## About Terminology

In this document, DynaProx products are referred to as the **device**.
They are designed to be connected to a **host**, which is a piece of
general-purpose electronic equipment which can send commands and data
to, and receive data from, the device. Host types include PC and Mac
computers/laptops, tablets, and smartphones. Generally, the host must
have **software** installed that communicates with the device and is
capable of processing transactions. During a transaction, the host and
its software interact with the **operator**, such as a customer service
representative, while the device interacts with the **cardholder** (even
if the cardholder is using a virtual representation of the card account,
such as a smartphone).

# Planning and Preparation

The guidelines in the following sections are intended to help project
planners and system administrators plan for the physical and logical
requirements of deploying and using DynaProx products. The most
effective way to ensure smooth deployment of a solution is to consider
these factors before receiving the device.

## Logistical Planning

- Determine what type of **host** DynaProx will connect to. For a list
  of supported device types and operating systems, see **Table 1‑1**.
  When planning, be sure to include any additional support or devices
  required by the host and DynaProx, such as physical locations,
  mounting, power connections, and charging cradles.

- Determine what **connection** the host will use to communicate with
  the device. Depending on the device model (see **Table 1‑1**), the
  connection can be USB or RS-232.

- Determine what **software** will be installed on the host and how it
  will be configured. Software can include the operating system,
  transaction processing software, security software, and so on. If
  teams other than the software development team will be involved in
  preliminary device testing, MagTek recommends the solution development
  team provide a smoke test harness early in the development process to
  allow basic testing (for example, communication adapter testing). In
  addition, be sure to plan for any additional support required by the
  software, such as software licenses and network connections.
  Information about software is provided in section **4.2 About Host
  Software**.

- Determine how the device will be physically presented to the
  cardholder. If the device is mounted, make sure there is adequate
  clearance for cardholders to swipe, insert, and tap. If the solution
  design includes metal objects anywhere near the device, including
  metal enclosures, make sure that at all points the metal is no further
  forward than 15mm below the face of the device. Proximity to metal can
  adversely affect the device’s performance.

- Determine how the device should be configured and specify that
  configuration when ordering the device. A full list of configurable
  options is documented in ***D998200489 DynaProx Programmer’s Manual
  (COMMANDS)***.

<!-- -->

- Select and configure a secure workstation that advanced operators will
  use to configure and/or update the device. The workstation must be
  configured as follows:

  - Available USB port.

  - A secure means of obtaining files, either via the network (such as
    SFTP) or via removable media, such as USB flash drives. This is
    required for installing software tools, copying firmware files, etc.
    If you are using Magensa Services, make sure the secure workstation
    has an internet connection and has all the required Magensa Remote
    Services software components installed.

  - ***1000007406 DynaFlex, DynaProx Test Utility*** installed, which
    advanced operators can use to configure and test the device.

  - ***1000007405 DynaFlex, DynaProx Firmware Upload Utility***
    installed, which advanced operators can use to update the device’s
    firmware.

- Determine the final set of tools advanced operators will use to
  configure, test, and update the device. This documentation uses the
  ***1000007406 DynaFlex, DynaProx Test Utility*** as an example for
  configuring the device; it can be used for initial pre-deployment
  testing and development, and as sample code showing how to communicate
  with the device, but the full solution may call for customized,
  solution-specific software for configuring the device and updating
  firmware.

- Determine how to **inspect** devices upon arrival, upon installation,
  and periodically during live usage, to ensure malicious individuals
  have not tampered with them. Details about inspection are provided in
  section **4.1 About Inspection**.

- Develop procedures for maintaining the device(s). Detailed guidance is
  provided in section **7 Maintenance**.

- Determine how to train operators. For example, training may include
  information extracted from section **5 Configuration**, section **6
  Operation**, and section **7 Maintenance**.

- Review the device’s PCI Security Policy, posted to the PCI web site
  [www.pcisecuritystandards.org](http://www.pcisecuritystandards.org)
  under **Approved PIN Transaction Security (PTS) Devices**, for
  additional information about using the device securely.

# Handling and Storage

| <img src="./media/media/image4.png" style="width:1.58in;height:0.3in" /> |
|----|
| Proper handling of the device throughout delivery, assembly, shipping, installation, usage, and maintenance is very important. Not following the guidelines in this document could damage the device, render it inoperable, and/or violate the conditions of the warranty. |

## Handling to Avoid Damage

Upon receiving the device, inspect it to make sure it originated from an
authentic source and has not been tampered with. For details, see
***D998200502 DynaProx / DynaProx BCR Device Inspection***, available
from MagTek.

From device delivery through assembly, shipping, installation, usage,
and maintenance, the device must not be exposed to conditions outside
the ratings in **Appendix A Technical Specifications**.

If the device is exposed to cold temperatures, adjust it to warmer
temperatures gradually to avoid condensation, which can interfere with
the operation of the device or cause permanent damage.

Do not drop or shake the device.

For information about ongoing maintenance of the device, such as
cleaning, see section **7 Maintenance**.

## Handling to Avoid Accidental Tamper

DynaProx products implement active tamper detection, which uses a small
amount of electricity even when the device is completely powered off.
When unpowered by an external power supply, the device powers its active
tamper detection circuitry using its non-rechargeable backup battery.
This provides 5 years of backup shelf life across the entire life of the
device. If the backup battery is allowed to completely discharge, the
device’s tamper detection engages and locks down the device, and it must
be returned to the manufacturer to reset.

To avoid accidental tamper events and to optimally condition the
battery, follow these precautions:

- Temperature is the most critical factor in extending battery life and
  preserving battery charge. Store the device at the lowest reasonable
  temperatures within its specified storage temperature range (see
  **Appendix A Technical Specifications**). Storing at temperatures
  between -30°C to 85°C (-22°F to 185°F) – DynaProx BCR -30°C to 70°C
  (-22°F to 158°F).

- Do not drop or shake the device.

- Do not attempt to disassemble the device.

# Installation

Installing DynaProx products is straightforward: The manufacturer or
acquirer configures the preferred settings, keys, and terminal and
payment brand settings before deployment; end users need only set up a
host with appropriate software, configure the software, and connect the
device to the host. This section provides general information about
inspecting, connecting, and installing DynaProx products.

## About Inspection

Before unpacking the device, it is important to inspect its secure
packaging to make sure it has not been tampered with in storage or in
transit. MagTek provides details for inspecting the integrity of the
device’s secure packaging in ***D998200501 DynaProx / DynaProx BCR
Package Inspection***.

It is important to thoroughly inspect a new device before deployment,
and regularly inspect devices in live usage (including its immediate
surroundings) to make sure malicious individuals have not tampered with
it. MagTek recommends conducting inspection training for all device
operators, and an inspection schedule with checkpoints in place to make
sure operators are performing inspections as specified and as scheduled.
MagTek provides an easy-to-follow device inspection reference
***D998200502 DynaProx / DynaProx BCR Device Inspection***.

## About Host Software

In any solution, DynaProx products are connected to a host, which must
have software installed that knows how to communicate with the device,
and which is capable of processing transactions. To set up the host to
work with DynaProx, follow the installation and configuration
instructions provided by the vendor of the host or the host software.
For information about developing custom host software, see section **8
Developing Custom Software**.

## Connecting to a Host

### About Connecting to a Host

The following sections provide steps for connecting DynaProx to a host
via the various available physical connection types.

### How to Connect DynaProx to a Host via USB

<figure>
<img src="./media/media/image5.png"
style="width:4.52083in;height:3.80208in"
alt="Diagram, engineering drawing Description automatically generated" />
<figcaption><p>- Connecting to a USB Host</p></figcaption>
</figure>

To connect DynaProx products to a USB host using the USB-C port, follow
these steps (for reference see **Figure 4‑1** and section **1.4 About
DynaProx** Components):For best results, use the cable that is included
with the device or another cable from **Table 1‑2 - DynaProx
Accessories** on page [**8**](#_Ref72491325). These cables are designed
specifically for DynaProx products and include ferrite shielding at both
ends of the cable to reduce emissions and interference. If the solution
design requires an alternate cable, contact MagTek for assistance with
ferrite selection and placement, and with connector over mold design.

Note: A poor quality cable, or cable longer than 12ft in length, can
result in unexpected reader resets. Refer to **Table 1‑2 - DynaProx
Accessories** for cable options.

1)  Connect the USB-C end of the cable to DynaProx.

2)  Connect the other end of the USB cable to the host’s USB port.

3)  As soon as the device starts receiving power through USB, it
    automatically powers on.

4)  If the specific device serial number you are connecting has not been
    connected to the host before, Windows system tray on the host
    reports it is **Setting up a device**, see **Figure 4‑2 – Device
    Setup**. When installation is complete (approximately 30 seconds
    later depending on the host), Windows reports **Device is ready**,
    (see **Figure 4‑3 – Setup Complete)** and the device shows in
    Windows Device Manager under **Human Interface Devices** (**see
    Figure 4‑4 – Windows Device Manager**) as two devices:
    **HID-compliant vendor-defined device** (see **Figure 4‑5 – HID
    Compliant Vendor-defined Device Properties**) with VID **0801** and
    PID **2020**, and **USB Input Device**.

<figure>
<img src="./media/media/image6.png"
style="width:4.45749in;height:1.70394in" />
<figcaption><p>– Device Setup</p></figcaption>
</figure>

<figure>
<img src="./media/media/image7.png"
style="width:4.48295in;height:1.77281in" />
<figcaption><p>– Setup Complete</p></figcaption>
</figure>

<figure>
<img src="./media/media/image8.png"
style="width:2.84375in;height:3in" />
<figcaption><p>– Windows Device Manager</p></figcaption>
</figure>

<figure>
<img src="./media/media/image9.png" style="width:2.77in;height:3in" />
<figcaption><p>– HID Compliant Vendor-defined Device
Properties</p></figcaption>
</figure>

5)  The operating system may put the device into **USB Suspend** mode.
    DynaProx does not support USB Suspend mode since this device relies
    on USB full power support.

### How to Connect DynaProx to a Host via RS-232

The RS-232 interface on DynaProx will provide a UART interface at RS-232
signal levels. No flow control is provided. The signals provided are on
J1 of DynaProx and are listed below. **See Table 4‑1 - RS-232 Signals.**

<table>
<caption><p>- RS-232 Signals</p></caption>
<colgroup>
<col style="width: 26%" />
<col style="width: 21%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr>
<th colspan="2" style="text-align: center;">DynaProx</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>PIN/WIRE</strong></td>
<td style="text-align: center;"><strong>SIGNAL</strong></td>
<td> </td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">5V</td>
<td rowspan="2"><p> </p>
<p>800 mA recommended</p>
<p> </p></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">5V</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">TXD</td>
<td>output of DynaProx</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">RXD</td>
<td>input to DynaProx</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">GND</td>
<td> </td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">GND</td>
<td> </td>
</tr>
</tbody>
</table>

#### RS-232 Cable

The RS-232 cable will be customer dependent. A sample cable can be
provided that has the mating connector for DynaProx and color-coded
wires. See **Figure 4‑6 - Cables and Connectors.**

<figure>
<img src="./media/media/image10.png"
style="width:6.44417in;height:3.8in" />
<figcaption><p>- Cables and Connectors</p></figcaption>
</figure>

#### Chassis Ground

The Chassis ground connection will also be a custom cable depending on
the customer’s requirement.

## Mounting

### About Mounting

DynaProx products are designed to provide flexible mounting options:

- The device can be mounted to custom mounting brackets or mounted in an
  enclosure as part of a larger solution design.

- The device can be mounted to the optional stand for countertop use.

### How to Mount DynaProx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><img src="./media/media/image4.png"
style="width:1.58in;height:0.3in" /></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>This document describes how to use DynaProx securely. Using the
device in any way other than the approved methods described in this
document invalidates the PCI PTS approval of the device.</p>
<p>Not following the guidelines in this section could damage the device,
render it inoperable, and/or violate the conditions of the
warranty.</p></td>
</tr>
</tbody>
</table>

This section provides information and guidelines for designing the
mechanical aspects of a solution that incorporates DynaProx products.
MagTek strongly recommends vetting and testing solution designs before
finalizing and deploying them, to make sure the design meets all
requirements (e.g., functional, legal, security, certification, safety,
and so on).

When designing the mechanical portions of a solution that incorporates
DynaProx products, consider the following:

- Review section **1.4 About DynaProx Components** for an overall
  introduction to the device’s physical features and what they are
  called.

- Review **Appendix A Technical Specifications**.

- Review the information below about overall device dimensions and
  mounting hole locations and use.

- Review any additional requirements from other agencies, such as PCI
  and EMV solution certification requirements, safety ordinances, and so
  on, which may introduce additional constraints to the design.

Overall dimensions of the device are shown in **Figure 4‑7**. On
request, MagTek can provide a 3D model of the device’s envelope to
assist with the mechanical portion of solution design. MagTek strongly
recommends building and testing prototypes with actual devices before
finalizing the solution design.

<figure>
<img src="./media/media/image11.png"
style="width:6.30208in;height:4.27083in"
alt="Diagram Description automatically generated" />
<figcaption><p>- DynaProx Overall Dimensions</p></figcaption>
</figure>

The screw hole placement on the bottom of DynaProx products is detailed
in **Figure 4‑8**. The holes are designed to accommodate screw size **M4
x 0.7mm** and a maximum screw depth of 0.315 inches (8mm) into the
device. The recommended torque range for installing the screws is 20 to
22 in-lbs. (2.3 to 2.5 N-m).

When mounting DynaProx, make sure gasket is seated properly to ensure
IP65 rating, see **Figure 4‑9**.

The suggested panel cutouts for the USB and RS-232 connectors are shown
in **Figure 4‑10** with a DynaProx shown for reference. The dimensions
for the suggested panel cutouts are shown in **Figure 4‑11**.

<figure>
<img src="./media/media/image12.png"
style="width:3.56571in;height:3.9in"
alt="Diagram Description automatically generated" />
<figcaption><p>- DynaProx Mounting Hole Locations</p></figcaption>
</figure>

<img src="./media/media/image13.png" style="width:3.63in;height:3in" />

– DynaProx Gasket

<figure>
<img src="./media/media/image14.png"
style="width:6.21681in;height:5.79629in"
alt="A picture containing diagram Description automatically generated" />
<figcaption><p>– DynaProx Suggested USB and RS-232 Panel
Cutouts</p></figcaption>
</figure>

<figure>
<img src="./media/media/image15.png"
style="width:6.5in;height:5.54097in"
alt="Diagram Description automatically generated" />
<figcaption><p>– DynaProx Suggested USB and RS-232 Panel Cutout
Dimensions</p></figcaption>
</figure>

When designing the enclosure or mounting bracket, make sure there is
adequate clearance for cardholders to tap or users to present a bar
code. If the solution design includes mounting to metal surfaces, there
will typically not be any impact to performance or card reading range.
If the design of the enclosure includes mounting the DynaProx such that
the top surface is flush with adjacent metal on the same plane, the
range of the contactless reader may be reduced. By keeping the card
reading plane a few millimeters above any adjacent metal surfaces or
providing a few millimeters of gap between the reader and adjacent metal
will assure acceptable card reading performance. Proximity to metal can
reduce the device’s reading range.

### How to Mount the Stand

Major Components, see **Figure 4‑12 - DynaProx Major Components.**

<figure>
<img src="./media/media/image16.png" style="width:3.41in;height:6in"
alt="Diagram Description automatically generated" />
<figcaption><p>- DynaProx Major Components</p></figcaption>
</figure>

**Stand Contents:**  
**Stand Body:** The body of the stand. Angled for better ergonomics.

**Cable Channel:** Allows the cable to be channeled out the back of the
stand body.

**(4) M4 Screws:** Attaches the stand body to the DynaProx device

**(2) Flat-head Screws:** Attaches the base plate to the stand body.

**Base Plate:** Bottom of stand, can attach the stand to counter tops

**Installation of DynaProx Stand**

1\. Place the DynaProx face down on a clean, soft surface to avoid
scratching the front face of the device. Using minimal toque, use (4) M4
screws to attach the stand to the body.

<figure>
<img src="./media/media/image17.png" style="width:2.16in;height:3in"
alt="A picture containing projector Description automatically generated" />
<figcaption><p>- Suggested Installation for DynaProx
Stand</p></figcaption>
</figure>

2\. Insert the cable and connect securely to the DynaProx device. Clip
the cable securely into the cable management hooks. Channel the cable
outside the back end of the stand body.

<figure>
<img src="./media/media/image18.png" style="width:1.85in;height:1.8in"
alt="Diagram, engineering drawing Description automatically generated" />
<figcaption><p>- Cable Management</p></figcaption>
</figure>

3\. Align the assembly base plate and using the (2) flat-head screws,
screw the base plate to the stand body. See **Figure 4‑15 – Baseplate
Installation.**

<figure>
<img src="./media/media/image19.png"
style="width:2.08483in;height:2.37513in" />
<figcaption><p>– Baseplate Installation</p></figcaption>
</figure>

4\. Assembly is complete. Additionally, you can secure the base plate to
almost any surface using (2) additional screws, not included.

**Securing DynaProx Stand to Surface**

Follow Steps 1 through 2, then –

1.  Place baseplate on the location where you want to secure the device.
    Trace the baseplate and mark the two screw set locations (Drawn
    Outline). Remove the baseplate and drill down through the surface,
    checking to make certain everything is clear beneath.

2.  Attach the baseplate to the stand body following step 3. Then align
    the surface to the tracing.

3.  Using (2) M4 x 0.7mm thread pitch (not included) screws, screw up
    through the pre-drilled holes to the baseplate. Screws should be
    long enough to go through the surface and no more than 0.25” into
    the stand body.

<img src="./media/media/image20.png"
style="width:2.81338in;height:5.04655in"
alt="A picture containing diagram Description automatically generated" />

**1.20"\[30.5mm\]**

\- Recommended Disassembly Procedure

**Disassembly**

Repeat assembly in reverse order to remove device from counter
installation and stand. See **Figure 4‑16 - Recommended Disassembly
Procedure.**

# Configuration

The device does not have an on-screen configuration interface. However,
it does have settings the host can change using commands. These settings
are documented as **Properties** in ***D998200489 DynaProx Programmer’s
Manual (COMMANDS)***.

# Operation

## About Operating Modes

During operation, DynaProx devices transition between distinct operating
modes, which are important for operators to understand so they can
properly control the device:

- **Powered Off Mode** is the shipping and storage mode of the device.
  No external power is applied to the device through the USB cable or
  RS-232 cable. In this mode, the device consumes practically no power.
  To set the device from Powered Off mode to Active mode, connect the
  device to USB power or RS-232 power.

- **Active Mode** is the device’s normal “awake” state when it is in
  use. In this mode, LEDs are powered on, and the device is ready to
  receive commands from the host. To set the device from Active mode to
  Powered Off mode remove power.

## Operation Overview

During normal operation, the operator initiates a transaction from the
host, and the cardholder interacts with the device. Transaction types
may include new accounts, teller window applications, checking, savings,
mortgages, retail transactions, or any other type of transaction where
there is interaction between the cardholder and the operator.

For each transaction type, the host software directs the cardholder, and
the transaction flow on the device may differ depending on what the host
software specifies and what the cardholder does. Section **6.6.3 About
Maintenance** Reset

For full host control, the device should not be allowed to run for \> =
23 hours without a reset. To accomplish this, have the host application
send a reset command twice a day separated by at least one hour.

Example: Host software resets the device at 1 AM and 3AM. This keeps the
device from initiating its own reset.

Card Reading provides examples of the cardholder experience for each
type of payment. If the device cannot read payment data, the host
software may prompt the cardholder to repeat the action or reject the
transaction.

## Introduction to User Interface

As mentioned in section **1.4 About DynaProx Components**, DynaProx
models equipped with a barcode reader (BCR) have a similar physical
appearance as models without a BCR, as shown in **Figure 6‑1**. BCR
models are equipped with a camera and a QR code located on the front
side of the device.

- DynaProx devices have a user interface composed of two elements: a
  visual indicator consisting of four mono LEDs and a beeper that
  produces audible alerts.

- DynaProx BCR devices have a user interface composed of three elements:
  a visual indicator consisting of four mono LEDs, a barcode reader, and
  a beeper that produces audible alerts.

- DynaProx devices do not feature any input components such as buttons
  or touch screens.

<img src="./media/media/image21.jpg"
style="width:2.20492in;height:2.5in"
alt="A picture containing appliance, kitchen appliance, sketch, drawing Description automatically generated" /><img src="./media/media/image22.jpg"
style="width:2.26052in;height:2.5in"
alt="A close-up of a machine Description automatically generated with low confidence" />

**Figure 6‑1 – DynaProx and DynaProx BCR**

### Component Details

1.  LED Ordering

The arrangement of the four mono LEDs on DynaProx and DynaProx BCR
devices is illustrated in **Figure 6‑2**. The LEDs are labeled LEDs 1 to
4 and are ordered from left to right on the device.

<img src="./media/media/image21.jpg"
style="width:2.20492in;height:2.5in"
alt="A picture containing appliance, kitchen appliance, sketch, drawing Description automatically generated" /><img src="./media/media/image22.jpg"
style="width:2.26052in;height:2.5in"
alt="A close-up of a machine Description automatically generated with low confidence" />

**1 2 3 4**

**1 2 3 4**

**Figure 6‑2 - LED Ordering**

2.  LED Status

> When DynaProx is powered on, its LEDs will illuminate green, when it
> is powered off, the LEDs will remain unlit. **Figure 6‑3** illustrates
> the on/off status of the LEDs.

**Figure 6‑3 - LED ON/OFF**

3.  BCR Status

> DynaProx devices equipped with a bar code reader have a status light
> that indicates whether the barcode feature is powered on or off.
>
> <img src="./media/media/image22.jpg" style="width:1.70988in;height:2in"
> alt="A close-up of a machine Description automatically generated with low confidence" />

**BCR Light ON BCR Light OFF**

**Figure 6‑4 - BCR Light**

4.  Beeper Alert

All DynaProx devices are equipped with a beeper that produces a short
beep lasting for half a second and a long beep that lasts for one
second.

### Modes of Operation

This section contains information regarding the operational modes of
DynaProx's LEDs, beeper, and BCR light. It is important to note that
DynaProx devices are not equipped with batteries. If there is no power
supply to the device through the USB cable or RS-232 serial port, all
LEDs, along with the BCR light, will not illuminate. In such instances,
the user interface will resemble the device as it appears in **Figure
6‑1**.

#### Power On via USB Cable

When the device USB cable is connected to the host USB port, a brief
beep will sound and all four LEDs will turn on for half a second, as
shown in **Figure 6‑5**. Following this, LED 1 and LED 2 will remain
illuminated, while LED 3 and LED 4 will remain unlit. After a duration
of 10 seconds, all LEDs will turn off, and the device will enter an idle
state. This occurs because the host sets the USB port into suspension
mode, prompting the device to enter an idle state.

<img src="./media/media/image21.jpg" style="width:1.76393in;height:2in"
alt="A picture containing appliance, kitchen appliance, sketch, drawing Description automatically generated" /><img src="./media/media/image21.jpg" style="width:1.76393in;height:2in"
alt="A picture containing appliance, kitchen appliance, sketch, drawing Description automatically generated" /><img src="./media/media/image21.jpg" style="width:1.76393in;height:2in"
alt="A picture containing appliance, kitchen appliance, sketch, drawing Description automatically generated" />

**Figure 6‑5 – LED Power on Sequence – USB Power On**

#### USB Enumeration

When DynaProx is in an idle state, it can be detected by a host through
the USB HID port see **Figure 6‑6**. After the host has connected to
DynaProx, LED 1 and LED 2 will stay on. The device is in Ready State.

<img src="./media/media/image21.jpg"
style="width:2.20492in;height:2.5in"
alt="A picture containing appliance, kitchen appliance, sketch, drawing Description automatically generated" /><img src="./media/media/image21.jpg"
style="width:2.20492in;height:2.5in"
alt="A picture containing appliance, kitchen appliance, sketch, drawing Description automatically generated" />

**Figure 6‑6 - LEDs Status (Idle State) Before Host Detection and LED
Status (Ready State) After Connecting to Host**

#### Payment Transaction

When the device is in ready state, two LEDs will be illuminated see
**Figure 6‑7**. When a card is detected only LED 1 will be on. If the
device has a BCR and it is enabled, the BCR light will also be turned on
see **Figure 6‑8**.

<img src="./media/media/image21.jpg"
style="width:2.20492in;height:2.5in"
alt="A picture containing appliance, kitchen appliance, sketch, drawing Description automatically generated" />

**Figure 6‑7 - Ready State**

<img src="./media/media/image22.jpg"
style="width:2.13734in;height:2.5in"
alt="A close-up of a machine Description automatically generated with low confidence" />

**Figure 6‑8 – Card detected.**

#### Payment Transaction Successful

When a card is read, all four LEDs will turn on in sequence (1, 2, 3,
and 4) followed by a long beep, indicating a successful transaction, see
**Figure 6‑9**. After a successful transaction, the device will return
to the ready state when the transaction is complete, see **Figure
6‑10**.

<img src="./media/media/image27.png"
style="width:6.36458in;height:2.32292in"
alt="A picture containing graphical user interface Description automatically generated" />

**Figure 6‑9 – LED Sequence – Payment Transaction Successful**

<img src="./media/media/image22.jpg"
style="width:2.13734in;height:2.5in"
alt="A close-up of a machine Description automatically generated with low confidence" />

**Figure 6‑10 – Return to Ready State After Successful Transaction**

#### Payment Transaction Unsuccessful

When the device is in ready state, two LEDs will be illuminated see
**Figure 6‑11**. When a card is detected, only LED 1 will be turned on.
If the device has a BCR and it is enabled, the BCR light will also be
turned on see **Figure 6‑12**.

<img src="./media/media/image22.jpg"
style="width:2.13734in;height:2.5in"
alt="A close-up of a machine Description automatically generated with low confidence" />

**Figure 6‑11 - Ready State**

<img src="./media/media/image22.jpg"
style="width:2.13734in;height:2.5in"
alt="A close-up of a machine Description automatically generated with low confidence" />

**Figure 6‑12 – Card Detected**

In the event of a failed or canceled transaction, LED 1 will stay
illuminated, and the device will emit two short beeps. If the device is
equipped with a BCR, its light will also be on, as shown in **Figure
6‑13**. The device will then return to the ready state, as demonstrated
in **Figure 6‑14**.

<img src="./media/media/image22.jpg"
style="width:2.13734in;height:2.5in"
alt="A close-up of a machine Description automatically generated with low confidence" />

**Figure 6‑13 - Payment Transaction Failed**

<img src="./media/media/image22.jpg"
style="width:2.13734in;height:2.5in"
alt="A close-up of a machine Description automatically generated with low confidence" />

**Figure 6‑14 - Ready State**

### USB Power Supply

Upon being connected to USB power (after a delay of three seconds), the
device will emit a short beep, and all four LEDs will turn on for half a
second, as shown in **Figure 6‑15**. The device will then return to the
Ready State.

<img src="./media/media/image21.jpg"
style="width:2.20492in;height:2.5in"
alt="A picture containing appliance, kitchen appliance, sketch, drawing Description automatically generated" /><img src="./media/media/image21.jpg"
style="width:2.20492in;height:2.5in"
alt="A picture containing appliance, kitchen appliance, sketch, drawing Description automatically generated" />

**Figure 6‑15 - Device Connected to USB Power**

### RS-232 Power Supply

Upon being connected to RS-232 power (after a delay of three seconds),
the device will emit a short beep, and all four LEDs will turn on for
half a second, see **Figure 6‑16**. The device will then return to ready
state.

<img src="./media/media/image21.jpg"
style="width:2.20492in;height:2.5in"
alt="A picture containing appliance, kitchen appliance, sketch, drawing Description automatically generated" /><img src="./media/media/image21.jpg"
style="width:2.20492in;height:2.5in"
alt="A picture containing appliance, kitchen appliance, sketch, drawing Description automatically generated" />

**Figure 6‑16 - Successful Connection to RS-232 Power Supply**

### Adding an RS-232 Power Supply

While in an idle state see **Figure 6‑17**, as described in section
**6.3.2.1 Power On** , if an RS-232 power supply is connected to the
device, it will remain in the idle state.

<img src="./media/media/image21.jpg"
style="width:2.20492in;height:2.5in"
alt="A picture containing appliance, kitchen appliance, sketch, drawing Description automatically generated" />

**Figure 6‑17 - Device in Idle State Before RS-232 Power Supply
Connection**

When the device is in a ready state, as explained in section **6.3.2.1
Power On** , connecting an RS-232 power supply to it will not change its
state and it will remain in the ready state see **Figure 6‑18**.

<img src="./media/media/image21.jpg"
style="width:2.20492in;height:2.5in"
alt="A picture containing appliance, kitchen appliance, sketch, drawing Description automatically generated" />

**Figure 6‑18 - Ready State**

### Event Notification Mode

When the device is configured in Event Notification Mode, the user
interface will have the same appearance as depicted in **6.3.2.3**
**Payment Transaction**.

### Bar Code Read Only

At present, no user interface elements such as LEDs or beeper sounds
have been established for DynaProx.

## About the Status LEDs

DynaProx provides four Mono LEDs (see section **1.4 About DynaProx**
Components), numbered LED1 through LED4, which report the device’s
current operating status.

- The meaning of each LED depends on the device’s operating mode. See
  section **6.1 About Operating Modes** and Error! Reference source not
  found. Error! Reference source not found.. Most of the time, operators
  will check the device’s status using the LEDs when it is in **Active
  Mode** while the device is not performing a transaction.

- LED blinking patterns have specific meanings as well, as described in
  **Table 6‑**. A blinking LED generally means the device is actively
  doing something to change the state that the LED is indicating, and
  solid indicates a persistent state that would require an operator or
  cardholder to take action to change. One major exception is a
  device-wide functional failure state, such as a tamper state, where
  all LEDs flash urgently to call the attention of an advanced operator
  to intervene.

In this manual, specific blinking patterns are described in more detail
in the sections where they are relevant. For example, information about
how the LEDs show the device’s connection status is in section **4.3
Connecting to a Host**.

| In This Context | LED1 | LED2 | LED3 | LED4 |
|----|----|----|----|----|
| Active Mode, not armed for a tap transaction | Power | Connection | Reserved | Card Read Result |
| Active Mode, armed for a tap transaction | Armed for Tap | Tap Read Progress | Tap Read Progress | Card Read Result |
| Device-wide failure | During major failures (such as tamper), **LED1-LED4** report the nature of the failure based on the most likely steps required to resolve it. |  |  |  |

- DynaProx LED Allocation

Table 6‑2 - DynaProx LED Patterns

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr>
<th>Color</th>
<th>Means</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Solid</p>
<p><img src="./media/media/image28.png"
style="width:0.28125in;height:0.28125in" /><img
src="./media/media/image28.png"
style="width:0.28125in;height:0.28125in" /><img
src="./media/media/image28.png"
style="width:0.28125in;height:0.28125in" /><img
src="./media/media/image28.png"
style="width:0.28125in;height:0.28125in" /></p></td>
<td><p><strong>Solid</strong> LEDs generally require an operator or
cardholder to take action to change the state the LED is reporting.</p>
<p>Example: Host is connected. Cardholder or host would have to
disconnect.</p>
<p>Example: Host is disconnected. Host would have to initiate
connection.</p></td>
</tr>
<tr>
<td><p>Blinking</p>
<p><img src="./media/media/image29.png"
style="width:0.28125in;height:0.28125in" /><img
src="./media/media/image29.png"
style="width:0.28125in;height:0.28125in" /><img
src="./media/media/image29.png"
style="width:0.28125in;height:0.28125in" /><img
src="./media/media/image29.png"
style="width:0.28125in;height:0.28125in" /></p></td>
<td><p><strong>Blinking</strong> LEDs generally indicate the device is
in the process of doing / attempting something. Blink duty cycle and
blink period are generally selected to show urgency or ongoing progress
through a series of steps.</p>
<p>Example: Device is attempting to connect to the 802.11 access
point.</p></td>
</tr>
<tr>
<td><p>Short time</p>
<p><img src="./media/media/image28.png"
style="width:0.28125in;height:0.28125in" /><img
src="./media/media/image28.png"
style="width:0.28125in;height:0.28125in" /><img
src="./media/media/image28.png"
style="width:0.28125in;height:0.28125in" /><img
src="./media/media/image28.png"
style="width:0.28125in;height:0.28125in" /></p></td>
<td><p>LEDs sometimes light for a <strong>short time</strong> to
indicate some process has ended (success or failure) and the device is
going to transition to another state soon.</p>
<p>Example: Successful card read.</p></td>
</tr>
</tbody>
</table>

## About Sounds

DynaProx products have a beeper that provides feedback to operators and
cardholders about the internal state of the device:

- The device sounds one short beep after it has successfully read a
  contactless tap, and the cardholder can safely remove the card or
  device from the contactless landing zone.

- The device emits two beeps when reading a card or contactless payment
  device to indicate a card read error occurred.

- The device sounds two beeps when an operator cancels a pending EMV
  transaction.

The device provides an internal setting the host can use to adjust the
global system volume. The device does not provide an interface to change
the volume setting directly via buttons. If the device is too quiet or
too loud:

- Make sure the device is being ordered from the manufacturer with the
  desired volume setting.

- Check to see whether the host software you are using provides a
  feature to check and/or adjust the volume setting.

<!-- -->

- If the host software does not provide that feature, request help from
  the development team that built the host software to check / change
  the volume setting. For details, see ***D998200489 DynaProx
  Programmer’s Manual (COMMANDS)***.

### How to Play a Sequence of Tones

To play a sequence of tones, follow these steps:

1)  Make sure the device is in idle state.

2)  Send an audio command to the device for playing a sequence of tones.
    For details, see ***D998200489 DynaProx Programmer’s Manual
    (COMMANDS)***.

## Power Management

### About Power

When properly powered through its USB port or RS-232 port, the device
powers on automatically. For USB mode it will remain full powered mode
to provide power to device. This device does not support USB suspend
mode.

The minimum required current and voltage are very important to the
proper operation of the DynaProx reader. During contactless card
reading, the NFC field is activated and the required current will rise
from less than 100 mA to less than 800 mA for typically around 1 second.
If the momentary current draw causes the supplied voltage to drop below
4 VDC, the DynaProx reader may reset and fail to complete the card read.

Embedded systems and Single Board Computers (SBC) may find use in a wide
range of card tending terminals. If the DynaProx will be supplied power
through a USB port from one of these SBCs, it is important to be aware
of the USB port current limitations, such as all USB ports may share a
given amount of current, or the upstream current limitation of the
system power supply.

An optional power/ground connection is available on the DynaProx RS-232
connector, even if the actual RS-232 signals are not in use.

### How to Power On / Wake Up from Standby Mode / Power Off

To power on the device connect the device to USB power or RS-232 Power.
Recommended 800 mA available current during transactions.

To power off the device, disconnect the device from USB power or RS-232
Power.

If all LEDs are off, the device is in Powered Off mode.

### About Maintenance Reset

For full host control, the device should not be allowed to run for \> =
23 hours without a reset. To accomplish this, have the host application
send a reset command twice a day separated by at least one hour.

Example: Host software resets the device at 1 AM and 3AM. This keeps the
device from initiating its own reset.

## Card Reading

### About Reading Cards

The steps for starting a transaction and reading a contactless payment
device are different depending on the device’s configuration and on the
design of the host software. Host software developers should see section
**8 Developing Custom Software** for implementation references. The
solution developer should provide solution-specific instructions for
operators to follow. A transaction generally follows this essential
flow:

1)  An advanced operator has already made sure DynaProx is configured
    properly and is connected to the host (see section **4.3 Connecting
    to a Host**). When the device is connected to the host via USB and
    powered by the USB‑C connector or RS-232, the host software may
    always keep a connection open to the device.

2)  The operator makes sure DynaProx is receiving power either from the
    USB connection or from the RS-232 connection, and is awake and
    powered on (see section **6.6.2 How to Power On / Wake Up** from
    Standby Mode / Power Off and section **6.4 About the Status LEDs**).

3)  The operator uses the host software’s user interface (for example, a
    point of sale) to finalize a transaction amount, then initiates a
    transaction. In solutions that are designed to respond to cardholder
    input events that occur when the device is idle, such as unprompted
    tapping of a card or electronic payment device, the host software
    may respond to those inputs by notifying the host, and the host
    software may trigger other operations without being initiated by an
    operator (for example, the host software may immediately start a
    transaction, or alert the cardholder or operator to take action).

4)  The host communicates with the device, and reports to the operator
    when the device is ready.

5)  The operator guides and assists the cardholder in presenting
    payment.

6)  The cardholder interacts with the device to present payment. The
    following sections provide additional details about presenting each
    of the available payment methods.

7)  The host monitors the progress of the transaction, and when
    necessary, should report issues to the operator, who may need to
    relay the messages to the cardholder.

8)  The device reports the success or failure of the transaction to the
    cardholder and to the host.

### How to Tap Contactless Cards / Devices

To tap a contactless card or smartphone, follow these steps:

1)  Check LED status:

    1)  The device shows the transaction status using the LEDs. LED1
        lights solid and all other LEDs are off, per EMV standards, to
        indicate it is ready for a tap.

    2)  All devices report detailed transaction status to the host, and
        host software may report that information to operators so they
        can guide cardholders through the transaction (for example,
        “please tap your card now”).

2)  If the cardholder is using an electronic payment device, such as a
    smartphone, make sure the payment device has **NFC** turned **On**
    and has a payment app configured to process transactions. For
    details, see the documentation provided by the smartphone
    manufacturer and payment app publisher.

3)  Briefly hold the card, smartphone, or other contactless payment
    device over the contactless landing zone, indicated by the EMVCo
    Contactless Indicator symbol on the device’s face (see **Figure
    6‑19**). Because each smartphone model may have its NFC antenna
    placed differently, the ideal tap position may vary by make and
    model. For example, Samsung users may need to center the phone on
    the contactless landing zone, while Apple users may need to tap the
    top of the phone on the contactless landing zone.

4)  Wait for LED status:

    1)  The device quickly lights the second LED to show it is
        processing, then lights the third LED to show it has
        successfully read the tap, then lights the fourth LED to show
        the read is complete (see **Figure 6‑20**).

    2)  The device beeps once.

    3)  If the transaction requires a signature, the device sends a
        notification message to the host that includes the status
        **Signature Capture Requested**. In this case, the solution
        design collects the cardholder’s signature via a different
        method.

    4)  The device ends the transaction and reports the transaction
        status to the host.

5)  If the device cannot communicate with the card, smartphone, or other
    contactless payment device:

    1)  The device ends the transaction.

    2)  The device lights LED4 for a short time.

    3)  The device beeps twice.

    4)  The device notifies the host that the transaction failed. If
        this occurs, the host software may choose to retry the
        transaction or revert to prompting the operator to perform
        another operation that is specific to the solution design.

<img src="./media/media/image30.jpeg"
style="width:1.725in;height:2.5in" /><img src="./media/media/image31.png"
style="width:1.39166in;height:2.5in" />

\- Tapping a Contactless Card / Smartphone

<figure>
<img src="./media/media/image27.png"
style="width:6.36458in;height:2.64583in"
alt="A picture containing graphical user interface Description automatically generated" />
<figcaption><p>– Contactless Read LED Sequence</p></figcaption>
</figure>

### How to Scan Barcodes

To scan a barcode, follow these steps:

1)  Make sure you are using a DynaProx model that includes a barcode
    reader, indicated by QR code markings on the face of the device
    surrounding the barcode reader lens (see section **1.4 About
    DynaProx Components**).

2)  If the barcode being scanned is not on a self-illuminated source
    such as a smartphone, make sure there is enough ambient light for
    the camera to read the barcode. In low light conditions, the barcode
    reader will only be able to read self-illuminated sources.

3)  In some solutions, the operator may have to perform an operation in
    the host software to enable the barcode reader, or to start a
    transaction with the barcode reader enabled.

4)  Wait for the device, the host, or the operator to prompt for a
    barcode read:

    1)  The device lights the barcode reader indicator LED next to the
        barcode reader lens.

5)  Hold the barcode in front of the barcode reader camera:

    1)  If possible, use the light from the barcode reader indicator LED
        to align the barcode within the barcode reader’s field of view,
        which extends 16 degrees above / below and 21 degrees to the
        left / right of a line perpendicular to the barcode reader lens.

    2)  Hold the barcode as close as 1 inch from the lens. For smaller
        barcodes, the device will read immediately. If it does not,
        gradually move away up to 14 inches from the lens until the
        device reports a successful read. Larger barcodes must be far
        enough away from the device that the whole barcode is within the
        camera’s field of view; if a large barcode is too close, the
        barcode reader can only see a zoomed in portion of the barcode.

    3)  Do not tilt the barcode more than 60 degrees from parallel to
        the device’s face.

6)  Wait for the device or the host to report the barcode has been read
    successfully:

    1)  The device beeps once.

    2)  The device turns off the barcode reader indicator LED.

<figure>
<img src="./media/media/image32.png"
style="width:1.75in;height:2.5in" />
<figcaption><p>- Scanning a Barcode</p></figcaption>
</figure>

### Apple VAS for DynaProx

DynaProx products support Apple Value Added Services (Apple VAS)
protocol.

Contactless transactions using the Apple VAS protocol permits the device
reader to perform the following supported operations:

#### VAS App and Payment Mode (Dual Mode)

The device reads both Apple VAS data and EMV payment data from a tapped
smartphone or reads EMV payment data from a tapped card. When device
sends ARQC to the host to conclude the transaction, it includes EMV
payment data in container FC and includes VAS data, if available, in
container FE

#### VAS App Only Mode (VAS Mode)

The device reads only Apple VAS data from a tapped smartphone and does
not read data from a tapped card. If the tapped smartphone does not
support VAS, the device does not detect or read from the smartphone.
When the device send ARQC to conclude the transaction, it includes VAS
data in container FE and does not include EMV payment data in container
FC.

#### VAS App or Payment Mode (Single Mode)

The device reads only Apple VAS data from a tapped smartphone or reads
EMV payment data from a tapped card. When the device sends ARQC to
conclude the transaction, it only includes either EMV payment data in
container FC for cards, or includes VAS data in container for
smartphones.

#### Payment Only Mode (Payment Mode)

The device operates the same as EMV mode (01). It reads only EMV payment
data from a tapped smartphone or a tapped card. When the device sends
ARQC to conclude the transaction, it includes EMV payment data in
container FC and does not include VAS data in container FE.

For details, see ***D998200489 DynaProx Programmer’s Manual
(COMMANDS).***

### How to Tap Contactless NFC Tags / MIFARE Ultralight / MIFARE Classic / MIFARE DESFire /MIFARE Plus Cards and Send Pass-through Commands

DynaProx is compatible with near field communication (NFC) technology
such as NTAG / MIFARE Ultralight / MIFARE Classic / MIFARE DESFire
/MIFARE Plus contactless IC products (smart cards).

To tap an NFC Contactless IC Product and Send Pass-through commands,
follow these steps:

1)  Check LED status:

    1)  Per EMV standards, the device indicates transaction status
        through its LED indicators, located on the front face of the
        device. When ready for a tap, LED 1 shines steadily while all
        other LEDs remain unlit.

    2)  All devices communicate transaction details to the host. The
        host software will relay this information to operators, allowing
        them to direct cardholders during the transaction, such as
        prompting "please tap your card now".

2)  Place the card over the device's designated contactless landing
    zone, marked by the EMVCo Contactless Indicator symbol on the front
    face of the device.

3)  Wait for LED status:

    1)  Initially, LED 2 illuminates, signaling the device is
        processing. The device subsequently illuminates LED 3 and LED 4,
        indicating card detection. Notifications are then sent to
        identify the card type and UID.

    2)  The Host application can further interact with the NFC Tag using
        pass-through commands. For details, see ***D998200489 DynaProx
        Programmer’s Manual (COMMANDS).***

    3)  If the pass-through command is the last successful command, the
        device will end the transaction, emitting a single beep
        signaling a successful transaction. The user then needs to
        remove the card.

    4)  If an error is detected, the device will end the transaction and
        emit two beeps to signal the error. The user then needs to
        remove the card.

4)  The device notifies the host that the transaction has ended with the
    NFC Tag removed.

# Maintenance

## Mechanical Maintenance

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><img src="./media/media/image4.png"
style="width:1.58in;height:0.3in" /></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>DO NOT use liquid cleaning products or insert any other objects
into the device.</p>
<p>DO NOT apply any liquid directly onto the device, to avoid seepage
into the electronics.</p></td>
</tr>
</tbody>
</table>

Periodic cleaning of the device’s exterior may be required. To clean the
outside of DynaProx products, wipe down the device with a soft, slightly
damp cloth and then wipe dry with a lint-free cloth. The glass on the
face can also be cleaned using a slightly damp specialty cleaning cloth,
like those used to wipe lenses, monitors, and smartphone displays.

## Updates to Firmware, Documentation, Security Guidance

In addition to the security guidance in the product manuals, MagTek may
provide updates to this document, as well as supplemental security
guidance or notices regarding vulnerabilities, at
[www.magtek.com](http://www.magtek.com). MagTek advises checking the
product’s home page periodically for the most up-to-date information.

Any firmware updates addressing product features, bugs, or security
vulnerabilities are also posted to
[www.magtek.com](http://www.magtek.com) or may be sent directly to
affected customers. To update the device’s firmware:

1)  Obtain the firmware image to install from your MagTek
    representative.

2)  Download ***1000007406 DynaFlex, DynaFlex II, DynaProx Utility***
    from the MagTek web site.

3)  Follow the instructions in ***D998200402 DynaFlex, DynaProx Firmware
    Update Utility Manual*** included in the firmware update utility’s
    **Docs** subfolder.

# Developing Custom Software

Custom host software uses the same underlying device command set for all
DynaProx product connection types. This section provides high-level
information about communicating with the device via the various physical
connection types in various software development frameworks, and
provides pointers to available SDKs, which include sample code. Product
documentation and SDKs are available for download by searching for the
product name on [www.magtek.com](http://www.magtek.com) and navigating
to the **Support** tab.

MagTek provides convenient SDKs and corresponding documentation for many
programming languages and operating systems. The API libraries included
in the SDKs wrap the details of the connection in an interface that
conceptually parallels the device’s internal operation, freeing software
developers to focus on the business logic, without having to deal with
the complexities of platform APIs for connecting to the various
available connection types, communicating using the various available
protocols, and parsing the various available data formats. Information
about using MagTek wrapper APIs is available in separate documentation,
including:

- ***D998200380 MagTek Universal SDK Programmer’s Manual (Microsoft
  .NET)***

- ***D998200381 MagTek Universal SDK Programmer’s Manual (Microsoft C++
  )***

- ***D998200385 MagTek Universal SDK for MMS Devices Programmer’s Manual
  (Java)***

- ***D998200387 MagTek Universal SDK Programmer’s Manual (Android)***

The documentation is bundled with the SDKs themselves, which include:

- ***1000007351 MagTek Universal SDK for MMS Devices (Windows)***

- ***1000007352 MagTek Universal SDK for MMS Devices (Android)***

The SDKs and corresponding documentation include:

- Functions for sending the direct commands described in this manual

- Wrappers for commonly used commands that further simplify development

- Sample source code to demonstrate how to communicate with the device
  using the direct commands described in this manual

To download the SDKs and documentation, search
[www.magtek.com](http://www.magtek.com) for “SDK” and select the SDK and
documentation for the programming languages and platforms you need or
contact MagTek Support Services for assistance.

In addition to the SDK API libraries, software developers also have the
option to revert to direct communication with the device using libraries
using the operating system’s native USB and serial port libraries. For
example, custom software written in Visual Basic or Visual C++ may make
API calls to the standard Windows USB HID driver. For more information
about sending commands directly, see ***D998200489 DynaFlex / DynaProx
Programmer’s Manual (COMMANDS).***

For more information about developing custom applications that integrate
with DynaProx, see the MagTek web site or contact your reseller or
MagTek Support Services.

###### Technical Specifications

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr>
<th colspan="2">DynaProx Products Technical Specifications</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Reference Standards and Certifications</td>
</tr>
<tr>
<td colspan="2"><p>EMV Contactless Level 1 Version 3.0</p>
<p>MasterCard TQM</p>
<p>MCL v3.1.3, payWave v2.2, Expresspay 4.0.2, D-PAS Terminal Payment
Application v1.0, D-PAS Terminal Application Specification Bulletins CL
TAS-002 v1.1, CL TAS-003 v1.0, CL TAS-004 v1.0</p>
<p>PCI PTS POI v6.1 SCR</p>
<p>TDEA (3DES)-CBC using DUKPT</p>
<p>FCC Part 15 Low Power Transceiver, RX verified per FCC Title 47 Part
15 Subclass C</p>
<p>UL/CSA/IEC 62368-1, 2nd edition</p>
<p>CE Certified</p>
<p>CE Safety: IEC 62368-1: 2014</p>
<p>Canada ISED Certified</p>
<p>AS/NZS CISPR 32 (2013), AS/NZS 4268 Table 1, Row 59 DTS 2400-2483MHz
SRD (802.11), and AS/NZS 4268 (2017) Table 1, Row 43 13.553-13.567MHz
(contactless reader)</p>
<p>RoHS Compliant the Electrical and Electronic Equipment (EEE)
Reduction of Hazardous Substances (RoHS) European Directive
2002/95/EC</p>
<p>California Proposition 65 (California)</p>
<p>IPC-A-610 Class II Assembly</p>
<p>EU Directive Waste Electrical and Electronic Equipment (WEEE)</p>
<p>EU Directive Restriction of Hazardous Substances (RoHS)</p>
<p>Universal Serial Bus Specifications 1.1, 2.0</p>
<p>AES, SHA-256</p></td>
</tr>
<tr>
<td colspan="2">Physical Characteristics</td>
</tr>
<tr>
<td>Dimensions (L x W x H):</td>
<td>2.09 in. x 2.52 in. x .72 in. (53mm x 64mm x18.5mm)</td>
</tr>
<tr>
<td>Weight</td>
<td><p>DynaProx = 2.0 oz. (56g)</p>
<p>DynaProx BCR = 2.0 oz. (58g)</p></td>
</tr>
<tr>
<td>Supported Mounting Options:</td>
<td><p>Mounting Screw Holes</p>
<p>Optional Stand</p></td>
</tr>
<tr>
<td colspan="2">Card Read Characteristics</td>
</tr>
<tr>
<td>Magnetic Stripe Reader:</td>
<td>Not Applicable</td>
</tr>
<tr>
<td>EMV Contact Reader:</td>
<td>Not Applicable</td>
</tr>
<tr>
<td>EMV Contactless Reader:</td>
<td><p>EMVCo L1 and L2 Contactless Reader</p>
<p>D-PAS, PayPass/MCL, payWave, Expresspay</p>
<p>Mobile wallets including but not limited to Apple Pay, Google Pay,
Samsung Pay</p></td>
</tr>
<tr>
<td>Barcode Reader:</td>
<td><p>Barcode Media: Labels, paper, smartphone / computer displays</p>
<p>Barcode Types: QR Codes, Linear Barcodes, UPC-A, UPC-E, Code 128,
PDF417 / Data Matrix, Aztec, etc.</p>
<p>Field Of View 31.5° total vertical sweep, 42° total horizontal sweep,
perpendicular to device face</p>
<p>Depth Of Field 1.2 in. (30mm) to 13.8 in. (350mm)</p>
<p>Integrated white indicator LED</p></td>
</tr>
<tr>
<td>User Interface Characteristics</td>
<td></td>
</tr>
<tr>
<td>Status Indicators:</td>
<td>4 Monochrome Green LEDs</td>
</tr>
<tr>
<td>Display Type:</td>
<td>Not Applicable</td>
</tr>
<tr>
<td>Keypad:</td>
<td>Not Applicable</td>
</tr>
<tr>
<td>Security Characteristics</td>
<td></td>
</tr>
<tr>
<td>Certifications:</td>
<td>PCI PTS POI v6.1 Certified Secure Card Reader (SCR)</td>
</tr>
<tr>
<td>Tamper Protection:</td>
<td>The enclosure and associated electronics form a Tamper Resistant
Security Module (TRSM) where attempts to penetrate or modify the unit
cause all cryptographic keys to be cleared or rendered unusable.</td>
</tr>
<tr>
<td>Electrical Characteristics</td>
<td></td>
</tr>
<tr>
<td>Power Inputs:</td>
<td><p>USB powered via USB-C receptacle</p>
<p>RS-232 powered via RS-232 custom receptacle</p></td>
</tr>
<tr>
<td>Power Outputs:</td>
<td>None</td>
</tr>
<tr>
<td>Rechargeable Battery Type:</td>
<td>None</td>
</tr>
<tr>
<td>Voltage Requirements:</td>
<td>5 VDC</td>
</tr>
<tr>
<td>Current Requirements:</td>
<td><p>800 mA recommended.</p>
<p>Note: Avoid poor quality cables, or cables longer than 12ft in
length, as they can lead to unexpected reader behavior. Refer to
<strong>Table 1‑2 - DynaProx Accessories</strong> for cable
options.</p></td>
</tr>
<tr>
<td>Data Storage:</td>
<td>Not Applicable</td>
</tr>
<tr>
<td>Communication Characteristics</td>
<td></td>
</tr>
<tr>
<td>Wired Connection Types:</td>
<td><p>USB-C, compatible with USB 1.1, USB 2.0, USB 3.0</p>
<p>Vendor-defined USB Human Interface Device (HID) data format</p>
<p>RS-232 Interface</p></td>
</tr>
<tr>
<td>Wireless Connection Types:</td>
<td>None</td>
</tr>
<tr>
<td>RF Exposure:</td>
<td>Exempt from SAR requirements due to radiated power substantially
below regulatory thresholds.</td>
</tr>
<tr>
<td>Software Characteristics</td>
<td></td>
</tr>
<tr>
<td>Tested Operating System(s):</td>
<td>USB Hosts: Windows 10, Android 4.4.2 and above</td>
</tr>
<tr>
<td colspan="2">Environmental Resistance</td>
</tr>
<tr>
<td>Ingress Protection:</td>
<td>IP66</td>
</tr>
<tr>
<td>Operating Temperature:</td>
<td>DynaProx: -22°F to 185°F (-30°C to 85°C) – DynaProx BCR: -4F to
131°F (-20°C to 55°C)</td>
</tr>
<tr>
<td>Operating Relative Humidity:</td>
<td>5% to 90% non-condensing</td>
</tr>
<tr>
<td>Storage Temperature:</td>
<td>DynaProx: -30°C to 85°C (-22°F to 185°F) – DynaProx BCR: -30°C to
70°C (-22°F to 158°F)</td>
</tr>
<tr>
<td>Storage Relative Humidity:</td>
<td>5% to 90% non-condensing</td>
</tr>
<tr>
<td>Vibration Resistance:</td>
<td>5Hz to 50Hz sinusoidal vibrations for 10 minutes at 1g acceleration
on each of XYZ axes</td>
</tr>
<tr>
<td>Shock Resistance:</td>
<td>IK08</td>
</tr>
<tr>
<td>ESD Tolerance (EMVCo):</td>
<td>Not Applicable</td>
</tr>
<tr>
<td>ESD Tolerance (FCC/CE):</td>
<td>±8kV contact discharge / ±16kV air discharge when properly
grounded</td>
</tr>
<tr>
<td>Vapor Resistance:</td>
<td>Test Gasoline-96 RON (Reference Gasoline); Reference Fuel C; Diesel
2007 Emission Certification Fuel (Reference Diesel); E10; E25; E85; M15;
Road-Use Diesel; Road Use Unleaded</td>
</tr>
<tr>
<td>Reliability</td>
<td></td>
</tr>
<tr>
<td>Shelf Life:</td>
<td>60 months at 25°C nominal</td>
</tr>
<tr>
<td>Magnetic Read Head Life:</td>
<td>Not Applicable</td>
</tr>
<tr>
<td>ICC Read Head Life:</td>
<td>Not Applicable</td>
</tr>
<tr>
<td>Battery Shelf Life:</td>
<td>5 years or longer (backup battery)</td>
</tr>
<tr>
<td>Battery Cycle Life:</td>
<td>NA</td>
</tr>
</tbody>
</table>

###### Barcode Reader Symbologies 

A Barcode symbology refers to the way in which data is encoded in a
barcode. It uses either spaced lines, dots or squares. When read, these
symbols are decoded and converted to data. The table below lists all of
the supported symbologies and which are enabled by default.

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

- Barcode Reader Supported Symbologies

###### Warranty, Standards, and Certifications

**Limited Warranty**

MagTek warrants that the products sold pursuant to this Agreement will
perform in accordance with MagTek’s published specifications. This
warranty shall be provided only for a period of one year from the date
of the shipment of the product from MagTek (the “Warranty Period”). This
warranty shall apply only to the “Buyer” (the original purchaser, unless
that entity resells the product as authorized by MagTek, in which event
this warranty shall apply only to the first repurchaser).

During the Warranty Period, should this product fail to conform to
MagTek’s specifications, MagTek will, at its option, repair or replace
this product at no additional charge except as set forth below. Repair
parts and replacement products will be furnished on an exchange basis
and will be either reconditioned or new. All replaced parts and products
become the property of MagTek. This limited warranty does not include
service to repair damage to the product resulting from accident,
disaster, unreasonable use, misuse, abuse, negligence, or modification
of the product not authorized by MagTek. MagTek reserves the right to
examine the alleged defective goods to determine whether the warranty is
applicable.

Without limiting the generality of the foregoing, MagTek specifically
disclaims any liability or warranty for goods resold in other than
MagTek’s original packages, and for goods modified, altered, or treated
without authorization by MagTek.

Service may be obtained by delivering the product during the warranty
period to MagTek (1710 Apollo Court, Seal Beach, CA 90740). If this
product is delivered by mail or by an equivalent shipping carrier, the
customer agrees to insure the product or assume the risk of loss or
damage in transit, to prepay shipping charges to the warranty service
location, and to use the original shipping container or equivalent.
MagTek will return the product, prepaid, via a three (3) day shipping
service. A Return Material Authorization (“RMA”) number must accompany
all returns. Buyers may obtain an RMA number by contacting MagTek
Support Services at (562) 546-6800.

**Each buyer understands that this MagTek product is offered as-is.
MagTek makes no other warranty, express or implied, and MagTek disclaims
any warranty of any other kind, including any warranty of
merchantability or fitness for a particular purpose.**

**If this product does not conform to MagTek’s specifications, the sole
remedy shall be repair or replacement as provided above. MagTek’s
liability, if any, shall in no event exceed the total amount paid to
MagTek under this agreement. In no event will MagTek be liable to the
Buyer for any damages, including any lost profits, lost savings, or
other incidental or consequential damages arising out of the use of, or
inability to use, such product, even if MagTek has been advised of the
possibility of such damages, or for any claim by any other party.**

**Limitation On Liability**

Except as provided in the sections relating to MagTek’s Limited
Warranty, MagTek’s liability under this agreement is limited to the
contract price of this product.

MagTek makes no other warranties with respect to the product, expressed
or implied, except as may be stated in this agreement, and MagTek
disclaims any implied warranty, including without limitation any implied
warranty of merchantability or fitness for a particular purpose.

MagTek shall not be liable for contingent, incidental, or consequential
damages to persons or property. MagTek further limits its liability of
any kind with respect to the product, including negligence on its part,
to the contract price for the goods.

MagTek’s sole liability and buyer’s exclusive remedies are stated in
this section and in the section relating to MagTek’s Limited Warranty.

**FCC Information**

This device complies with Part 15 of the FCC Rules. Operation is subject
to the following two conditions: (1) This device may not cause harmful
interference, and (2) This device must accept any interference received,
including interference that may cause undesired operation.

Note: This equipment has been tested and found to comply with the limits
for a Class B digital device, pursuant to part 15 of the FCC Rules.
These limits are designed to provide reasonable protection against
harmful interference in a residential installation. This equipment
generates, uses and can radiate radio frequency energy and, if not
installed and used in accordance with the instructions, may cause
harmful interference to radio communications. However, there is no
guarantee that interference will not occur in a particular installation.
If this equipment does cause harmful interference to radio or television
reception, which can be determined by turning the equipment off and on,
the user is encouraged to try to correct the interference by one or more
of the following measures:

- Reorient or relocate the receiving antenna.

- Increase the separation between the equipment and receiver.

- Connect the equipment into an outlet on a circuit different from that
  to which the receiver is connected.

- Consult the dealer or an experienced radio/TV technician for help.

**Caution: Changes or modifications not expressly approved by MagTek
could void the user’s authority to operate this equipment.**

**Canadian Declaration Of Conformity**

This digital apparatus does not exceed the Class B limits for radio
noise from digital apparatus set out in the Radio Interference
Regulations of the Canadian Department of Communications.

Le présent appareil numérique n’émet pas de bruits radioélectriques
dépassant les limites applicables aux appareils numériques de la classe
B prescrites dans le Réglement sur le brouillage radioélectrique édicté
par le ministère des Communications du Canada.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe B est conformé à la norme NMB-003 du
Canada.

**Industry Canada (IC) RSS**

This device complies with Industry Canada licence-exempt RSS
standard(s). Operation is subject to the following two conditions: (1)
This device may not cause interference, and (2) This device must accept
any interference, including interference that may cause undesired
operation of the device.

Le présent appareil est conforme aux CNR d'Industrie Canada applicables
aux appareils radio exempts de licence. L'exploitation est autorisée aux
deux conditions suivantes: (1) L'appareil ne doit pas produire de
brouillage, et (2) L'utilisateur de l'appareil doit accepter tout
brouillage radioélectrique subi, même si le brouillage est susceptible
d'en compromettre le fonctionnement.

**CUR/UR**

This product is recognized per Underwriter Laboratories and Canadian
Underwriter Laboratories 1950.

**CE STANDARDS**

Testing for compliance with CE requirements was performed by an
independent laboratory. The unit under test was found compliant with
standards established for Class B devices.

**EU Statement**

Hereby, MagTek Inc. declares that the radio equipment types **Wideband
Transmission System** (802.11 wireless and Bluetooth Low Energy), and
**Non-Specific Short Range Device** (contactless) are in compliance with
***Directive 2014/53/EU***. The full text of the EU declarations of
conformity is available at the following internet addresses:

- [<u>https://www.magtek.com/Content/DocumentationFiles/D998200238.pdf</u>](https://www.magtek.com/Content/DocumentationFiles/D998200238.pdf).

- [<u>https://www.magtek.com/Content/DocumentationFiles/D998200296.pdf</u>](https://www.magtek.com/Content/DocumentationFiles/D998200296.pdf)

**Australia / New Zealand Statement**

Testing for compliance with AS/NZS standards was performed by a
registered and accredited laboratory. The unit under test was found
compliant with standards established under AS/NZS CISPR 32 (2013),
AS/NZS 4268 Table 1, Row 59 DTS 2400-2483MHz SRD (802.11), and AS/NZS
4268 (2017) Table 1, Row 43 13.553-13.567MHz (contactless reader).

**UL/CSA**

This product is recognized per ***UL 60950‑1, 2nd Edition, 2011‑12‑19***
(Information Technology Equipment - Safety - Part 1: General
Requirements), ***CSA C22.2 No. 60950‑1‑07, 2nd Edition, 2011‑12***
(Information Technology Equipment - Safety - Part 1: General
Requirements).

**RoHS STATEMENT**

When ordered as RoHS compliant, this product meets the Electrical and
Electronic Equipment (EEE) Reduction of Hazardous Substances (RoHS)
Directive (EU) 2015/863 amending Annex II to Directive 2011/65/EU. The
marking is clearly recognizable, either as written words like “Pb-free,”
“lead-free,” or as another clear symbol
(<img src="./media/media/image33.png"
style="width:0.20833in;height:0.17708in" alt="PbFreeSym" />).

**PCI Statement**

PCI Security Standards Council, LLC (“PCI SSC”) has approved this PIN
Transaction Security Device to be in compliance with PCI SSC’s PIN
Security Requirements.

When granted, PCI SSC approval is provided by PCI SSC to ensure certain
security and operational characteristics important to the achievement of
PCI SSC’s goals, but PCI SSC approval does not under any circumstances
include any endorsement or warranty regarding the functionality, quality
or performance of any particular product or service. PCI SSC does not
warrant any products or services provided by third parties. PCI SSC
approval does not under any circumstances include or imply any product
warranties from PCI SSC, including, without limitation, any implied
warranties of merchantability, fitness for purpose, or non-infringement,
all of which are expressly disclaimed by PCI SSC. All rights and
remedies regarding products and services which have received PCI SSC
approval shall be provided by the party providing such products or
services, and not by PCI SSC.

**Safety**

**This product has been evaluated by multiple safety certification
agencies, including Underwriters Laboratories (UL) and the United States
Federal Communications Commission (FCC Class A and Class B), and is
designed to protect both the user and the device. This document is
written specifically to work in conjunction with these safety and
integrity features to protect the user and the device. It is very
important to follow all steps in the product documentation carefully, in
the order in which they are described, and at the recommended times.
Failure to do so could result in personal injury, and / or cause damage
to the device, and / or void the product warranty.**

**Safety Requirements**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><img src="./media/media/image4.png"
style="width:1.58in;height:0.3in"
alt="A picture containing text, font, graphics, logo Description automatically generated" /></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><strong>Never do any of the following:</strong></p>
<ul>
<li><p>DO NOT use a ground adapter plug to connect equipment to a power
socket-outlet that lacks a ground connection terminal.</p></li>
<li><p>DO NOT attempt any maintenance function that is not specifically
described in this manual or in other ExpressCard 3000 instructional
documents published by MagTek.</p></li>
<li><p>DO NOT remove any of the covers or guards that are fastened with
screws. There are no user-serviceable areas within these
covers.</p></li>
<li><p>DO NOT override or “cheat” electrical or mechanical interlock
devices.</p></li>
<li><p>DO NOT use EC3000 supplies or cleaning materials for other than
their intended purposes.</p></li>
<li><p>DO NOT operate the equipment if you or anyone else have noticed
unusual noises or odors.</p></li>
</ul>
<p><strong>Consider the following before operating the ExpressCard
3000:</strong></p>
<ul>
<li><p>Connect the EC3000 to a properly grounded AC power socket-outlet.
If in doubt, have the socket-outlet checked by a qualified electrician.
Improper connection of the device’s grounding conductor creates a risk
of electric shock.</p></li>
<li><p>Place the EC3000 on a solid surface that can safely support the
device’s weight plus the weight of a person leaning against it (such as
a service technician).</p></li>
<li><p>Be careful when moving or relocating the device. Use proper
lifting techniques.</p></li>
<li><p>Use materials and supplies specifically designed for MagTek
devices. Using unsuitable materials may result in poor performance, and
in some cases may be hazardous.</p></li>
</ul></td>
</tr>
</tbody>
</table>
