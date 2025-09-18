---
title: Overview
layout: home
parent: Dyna Devices Master Programmer's Manual
nav_order: 2
---

# Overview

This manual provides a complete reference to the MagTek **DynaFlex family** of secure card readers and peripherals. It is written for developers building applications that communicate directly with MagTek devices over supported transports.

---

## Device Families

MagTek devices are available in several families. Each product combines different connection methods and feature sets:

- **DynaFlex** – Core product, USB HID baseline. Variants include USB-only and BLE (internal).  
- **DynaFlex Pro** – Adds display and touch support. Available in USB-only, BLE (internal), WLAN, and Ethernet (internal) versions.  
- **DynaFlex II** – Successor to DynaFlex with updated hardware. USB and BLE (internal).  
- **DynaFlex II PED** – PED-compliant model with PIN entry, WLAN, display, and touch.  
- **DynaFlex II GO** – Portable BLE + battery-powered model with EMV Contactless and barcode reader. Supports iAP2 for iOS.  
- **DynaProx** – Contactless EMV + barcode reader. Supports SLIP (UART) and iAP2.

---

## Architecture

A MagTek system is composed of three roles:

1. **Host Application** – initiates commands (e.g., *Start Transaction*), parses responses, and manages user interaction.  
2. **MagTek Device** – executes commands, drives user prompts (LEDs, display, audio), and enforces PCI/SRED rules.  
3. **Cardholder / Mobile Wallet** – presents a payment card or NFC credential.

Communication is always host-driven: the application sends a **command**, the device responds, and the device may emit **notifications** asynchronously.

---

## Manual Structure

- **Overview** – this section, high-level concepts and families.  
- **Message Conventions** – how MagTek messages are framed, TLVs, and status codes.  
- **Connections & Setup** – supported transports, setup flows, and feature matrices.  
- **Commands** – request/response APDUs (organized by command group).  
- **Notifications** – device-to-host events.  
- **Properties** – hierarchical configuration and status tree.

---

## Developer Assumptions

- You understand basic APDU/TLV formatting (if not, see EMV Book 3, ISO 7816).  
- You understand PCI DSS and SRED restrictions on sensitive data handling.  
- You will test against real devices, not rely solely on RMS or Web HID demos.  

---

## Typical Transaction Flow

1. Host connects over USB, BLE, WLAN, or Ethernet.  
2. Host issues **0x1001 Start Transaction** with amount, currency, and type TLVs.  
3. Device drives interaction (swipe, insert, tap, or manual entry).  
4. Device returns response TLVs (Track 2, cryptogram, status).  
5. Host may **Resume (0x1004)**, **Continue (0x1002)**, or **Cancel (0x1008)**.  
6. Device returns to idle or awaits next command.  

*Note:* If a card is presented before *Start Transaction*, the device either buffers or emits a notification depending on model.
