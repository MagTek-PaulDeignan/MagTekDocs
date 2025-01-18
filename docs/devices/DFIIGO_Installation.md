---
title: Installation and Operation
layout: home
parent: DynaFlexIIGO
nav_order: 2
---

## **DynaFlex II Go Installation and Operation Manual**  
**Secure Card Reader Authenticator**  
### **Installation and Operation Manual**  
**July 2024**  
**Document Number:** D998200554-100  
**REGISTERED TO ISO 9001:2015**

---

# DynaFlex II Go Device Inspection Document

## Table of Contents

- [Introduction](#introduction)
- [Overall Form Factor](#overall-form-factor)
- [Top of Device](#top-of-device)
  - [Payment Methods](#payment-methods)
  - [Chip Card Insertion Slot](#chip-card-insertion-slot)
  - [Swipe Path](#swipe-path)
- [Front Face](#front-face)
  - [Contactless Landing Zone](#contactless-landing-zone)
  - [Barcode Reader (BCR)](#barcode-reader-bcr)
  - [LED Feedback](#led-feedback)
- [Bottom of Device](#bottom-of-device)
- [Right-Facing Side of Device](#right-facing-side-of-device)
- [Back Side of Device](#back-side-of-device)
- [Additional Details and Checklist](#additional-details-and-checklist)
- [Compliance](#compliance)
  - [FCC Information](#fcc-information)
  - [Canadian Declaration of Conformity](#canadian-declaration-of-conformity)
  - [EU Statement](#eu-statement)
  - [RoHS Statement](#rohs-statement)
  - [PCI Statement](#pci-statement)
  - [UKCA Statement](#ukca-statement)

# 1 Introduction

DynaFlex II is a secure card reader authenticator engineered for attended, unattended, and mobile payment environments. The reader features a magnetic stripe reader, EMV chip reader for both contact and contactless cards, an optional barcode reader, and support for NFC-enabled mobile wallets such as Samsung Pay®, Google Pay®, Apple Pay®, and Apple VAS. DynaFlex II communicates with host devices via USB or wireless local area network (WLAN) on pin entry devices (PED). DynaFlex II products are compatible with iOS, Android, and Windows operating systems.

For details on how to set up Google Wallet Smart Tap for DynaFlex II, see *D100006469 DYNAFLEX, DYNAPROX, DYNAFLEX II GO FAMILY - GOOGLE WALLET SMART TAP SETUP GUIDE*. For details on how to set up Apple VAS for DynaFlex II, see *D998200597 DYNAFLEX II GO PROGRAMMER'S MANUAL (COMMANDS)*.

## 1.1 About Terminology

In this document, DynaFlex II products are referred to as the device or inclusively as DynaFlex II products. They are designed to be connected to a host, which is a piece of general-purpose electronic equipment that sends commands and data to, and receives data from, the device. Host types include PC and Mac computers/laptops, tablets, and smartphones. The host must have software installed that communicates with the device and is capable of processing transactions. During a transaction, the host and its software interact with the operator, such as a customer service representative, while the device interacts with the cardholder (even if the cardholder is using a virtual representation of the card account, such as a smartphone).

Throughout this document:
- **DynaFlex II Product Family** refers to all devices in the DynaFlex II family, including all DynaFlex II models and DynaFlex II PED models.
- **DynaFlex II PED** refers to DynaFlex II PED products with a display, including those with a kiosk back cover and barcode reader.
- **DynaFlex II** refers to DynaFlex II devices that are not equipped with a touchscreen display, including those with a kiosk back cover and barcode reader.

## 1.2 Magensa Services

DynaFlex II products can be paired with Magensa Services to make the certification cycle easier and remove unencrypted data from the payment environment. A service representative will collaborate with you to determine if Magensa Decrypt, Magensa Decrypt and Forward, or the Magensa Payment Protection Gateway is best for you.

## 1.3 MagTek Support

MagTek offers developer tools, including free software developer kits with APIs. Support is available at [https://www.magtek.com/support](https://www.magtek.com/support). For faster development, use MagneFlex Prism, a suite of interface tools for browser and middleware applications that streamline the development process. Instead of creating multiple interfaces for the hardware device, POS application, and gateway, you can use MagneFlex. It drives the hardware, interfaces with the POS app, and handles data processing commands.

---

## 1.4 Available Models and Accessories

### Table 1-1 - Available Models and Options

| Part No.   | Description                                                        | Display       | Connection(s)        |
|------------|--------------------------------------------------------------------|---------------|----------------------|
| 21078307   | DYNAFLEX II, PCI, BLACK, USB                                       | None          | USB-C                |
| 21078309   | DYNAFLEX II PED, PCI, TOUCHSCREEN DISPLAY, BLACK, USB              | Touchscreen   | USB-C                |
| 21078311   | DYNAFLEX II PED, PCI, TOUCHSCREEN DISPLAY, BLACK, WLAN             | Touchscreen   | USB-C, Wireless LAN  |
| 21078314   | DYNAFLEX II KIOSK, PCI, BCR, BLACK, USB                            | None          | USB-C                |
| 21078321   | DYNAFLEX II PED, KIOSK, PCI, TOUCHSCREEN DISPLAY, BLACK, USB       | Touchscreen   | USB-C                |
| 21078322   | DYNAFLEX II, KIOSK, PCI, BLACK, USB                                | None          | USB-C                |
| 21078325   | DYNAFLEX II PED, KIOSK, PCI, TOUCHSCREEN DISPLAY, BLACK, WLAN      | Touchscreen   | USB-C, Wireless LAN  |
| 21078331   | DYNAFLEX II, PCI, BCR, BLACK, USB                                  | None          | USB-C                |
| 21078332   | DYNAFLEX II PED, PCI, TOUCHSCREEN DISPLAY, BCR, BLACK, WLAN        | Touchscreen   | USB-C, Wireless LAN  |
| 21078333   | DYNAFLEX II PED, PCI, TOUCHSCREEN DISPLAY, BCR, BLACK, USB         | Touchscreen   | USB-C                |
| 21078334   | DYNAFLEX II PED, KIOSK, PCI, TOUCHSCREEN DISPLAY, BCR, BLACK, USB  | Touchscreen   | USB-C                |

All models are black by default and have countertop, handheld, and custom mounting options.

### Table 1-2 – DynaFlex II Accessories

| Part #       | Description                                           | Accessory Notes                                  |
|--------------|-------------------------------------------------------|--------------------------------------------------|
| 1000006016   | CABLE, USB A - C, 6FT, DYNAFLEX                       | Included with DynaFlex products                  |
| 1000006017   | CABLE, USB C - C, 6FT, DYNAFLEX                       | Optional, specify in order                       |
| 21078006     | CHARGING STATION, DYNAFLEX                            | Optional, specify in order                       |
| 96700004     | CLEANING CARD, DOUBLE SIDED                           | Optional, specify in order                       |
| 1000008559   | FOOT, BACK, SIDE A, ADHESIVE MOUNTING STRIP, DYNAFLEX | Optional, specify 1 ea. for complete replacement |
| 1000008560   | FOOT, BACK, SIDE B, ADHESIVE MOUNTING STRIP, DYNAFLEX | Optional, specify 1 ea. for complete replacement |
| 1000008561   | FOOT, FRONT, ADHESIVE MOUNTING STRIP, DYNAFLEX        | Optional, specify 1 ea. For complete replacement |
