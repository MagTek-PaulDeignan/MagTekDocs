---
title: Connections & Setup
layout: home
parent: Dyna Devices Master Programmer's Manual
nav_order: 4
---

# Connections & Setup

This section covers supported transports, setup flows, and the features available across product families.

---

## Supported Transports

See **Table 2 – Device Connection Types / Data Formats**:

| Product / Connection | Bluetooth® LE GATT | RS232 / UART | USB HID | WLAN | iAP2 | Ethernet |
|----------------------|--------------------|--------------|---------|------|------|----------|
| DynaFlex USB Only    |                    |              | HID     |      |      |          |
| DynaFlex Pro WLAN    |                    |              | HID     | WLAN |      |          |
| DynaProx             |                    | SLIP         | HID     |      | iAP2 |          |
| DynaFlex II GO       | GATT               |              | HID     |      | iAP2 |          |
| DynaFlex II PED WLAN |                    |              | HID     | WLAN |      |          |
| …                    | …                  | …            | …       | …    | …    | …        |

**How to read this table:**
- **USB HID** is the baseline — supported on every variant.  
- **BLE (GATT)** is only in GO and internal-only builds.  
- **WLAN/Ethernet** are available on Pro/PED for unattended or countertop solutions.  
- **iAP2** is required for iOS integrations (Go, Prox).  
- **SLIP (UART)** appears only on Prox.

---

## Device Features

See **Table 3 – Device Features**:

- **Card acceptance**: MSR, EMV Contact, EMV Contactless, Manual Entry, Barcode Reader  
- **UI**: LEDs (RGB/Mono), Touch/No Touch, Display/No Display  
- **Power**: Battery vs. fixed power  
- **Banking**: PED Banking Functions, Session Management  
- **Wallet support**: Apple VAS, Google Smart Tap  
- **System**: Common Kernel, Card Emulation

**Developer implications:**
- Need PIN entry? → Choose **PED** models.  
- Need mobile/battery? → Use **GO** or BLE variants.  
- Need iOS iAP2? → Choose **GO** or **Prox**.  
- Need kiosk Ethernet/WLAN? → Use **PED** or **Pro**.  
- Need barcode scanning? → Supported on most, verify in Table 3.  

---

## Setup Sequences

### USB
- Enumerates as HID class.  
- Exchange commands via HID reports.  

### BLE
- Pair device.  
- Discover MagTek service.  
- Subscribe to notification characteristic.  
- Write commands to control characteristic.  

### WLAN / Ethernet
- Configure network parameters via setup utility.  
- Open TCP socket to device.  
- Send/receive APDU frames over socket.  

### iAP2
- Supported on iOS with GO and Prox.  
- Requires Apple MFi environment.  

---

## First Transaction

1. Establish connection over chosen transport.  
2. Send **0x1001 Start Transaction** with minimal TLVs (amount, date, type, currency).  
3. Device prompts user and returns response TLVs.  
4. Host handles result (approve, resume, cancel).  

---

## Troubleshooting

| Symptom            | Likely Cause               | Resolution                        |
|--------------------|----------------------------|-----------------------------------|
| No response        | Wrong transport or framing | Verify HID report or GATT service |
| Timeout            | User action not taken      | Prompt user to swipe/insert/tap   |
| `6985` response    | Wrong state                | Ensure Start Transaction was sent |
| `6A80` response    | Malformed TLV              | Validate TLV encoding             |

---

## Recovery & Power

- Use **0x1009 Close/Clear Transaction** if connection is lost mid-transaction.  
- If battery <5%, Start Transaction will fail with “not executed.”  
- Always cancel gracefully with **0x1008 Cancel Transaction** if user abandons flow.
