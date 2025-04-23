---
title: Connection Types
layout: home
parent: DynaFlex Family Programmer's Manual
nav_order: 2
---
## Connection Types

---

### Contents


  - [How to Use USB Connections (USB Only)](#how-to-use-usb-connections-usb-only)
    - [About USB Reports, Usages, Usage Pages, and Usage IDs](#about-usb-reports-usages-usage-pages-and-usage-ids)
    - [How to Connect to a Device Using the USB Connection](#how-to-connect-to-a-device-using-the-usb-connection)
    - [How to Send Command Requests Using the USB Connection](#how-to-send-command-requests-using-the-usb-connection)
    - [How to Receive Data Using the USB Connection (HID Only)](#how-to-receive-data-using-the-usb-connection-hid-only)
  - [How to Use Wireless LAN (WLAN) Connections (WLAN Only)](#how-to-use-wireless-lan-wlan-connections-wlan-only)
    - [About Wireless LAN (WLAN) Connections](#about-wireless-lan-wlan-connections)
    - [How to Connect to a Device Using the Wireless LAN (WLAN) Connection](#how-to-connect-to-a-device-using-the-wireless-lan-wlan-connection)
    - [How to Send Commands Using the Wireless LAN (WLAN) Connection](#how-to-send-commands-using-the-wireless-lan-wlan-connection)
    - [How to Receive Data Using the Wireless LAN (WLAN) Connection](#how-to-receive-data-using-the-wireless-lan-wlan-connection)
  - [How to Use Ethernet Connections (Ethernet Only, MAGTEK INTERNAL ONLY FOR NOW)](#how-to-use-ethernet-connections-ethernet-only-magtek-internal-only-for-now)
  - [How to Use Bluetooth® LE Connections (Bluetooth® LE Only)](#how-to-use-bluetooth-le-connections-bluetooth-le-only)
    - [About GATT Characteristics](#about-gatt-characteristics)
    - [DynaFlex Bluetooth® LE protocol](#dynaflex-bluetooth-le-protocol)
  - [How to Use RS-232/UART Connections (SLIP Only)](#how-to-use-rs-232uart-connections-slip-only)
  - [How to Use SLIP Format (SLIP Only)](#how-to-use-slip-format-slip-only)
  - [How to Use Apple iAP2 Connections (iAP2 Only)](#how-to-use-apple-iap2-connections-iap2-only)

---

### How to Use USB Connections (USB Only)

#### About USB Reports, Usages, Usage Pages, and Usage IDs

The USB HID class uses **Usage Pages** to group **Usages**, which define specific data points. Each usage belongs to a report, which can be Input, Output, or Feature.

- The MMS USB interface uses a Vendor-defined Usage Page (0xFF00)
- Report IDs distinguish different types of data in the same pipe (endpoint)

#### How to Connect to a Device Using the USB Connection

Devices use the standard HID driver. No special driver is needed. The device appears in the system as a HID-compliant device with Vendor-defined usage page.

#### How to Send Command Requests Using the USB Connection

1. Format the MMS command into a binary buffer
2. Use a HID API (e.g., Windows HID API, hidapi) to write to the Output Report

#### How to Receive Data Using the USB Connection (HID Only)

Devices send data using Input Reports. Use the HID API to read asynchronously or poll for Input Reports.

---

### How to Use Wireless LAN (WLAN) Connections (WLAN Only)

#### About Wireless LAN (WLAN) Connections

Devices supporting WLAN expose a secure TCP port. The device acts as a TCP server. The host must initiate a TCP client session.

#### How to Connect to a Device Using the Wireless LAN (WLAN) Connection

1. Determine the device IP address (via DHCP or static assignment)
2. Connect to the MMS port (default: 8080 or configurable)

#### How to Send Commands Using the Wireless LAN (WLAN) Connection

Send MMS-formatted messages directly over the TCP socket.

#### How to Receive Data Using the Wireless LAN (WLAN) Connection

The device sends responses and notifications over the same open TCP socket.

---

### How to Use Ethernet Connections (Ethernet Only, MAGTEK INTERNAL ONLY FOR NOW)

Same as WLAN. The only difference is the physical layer and interface configuration. The device still uses TCP over IP, with an MMS port.

---

### How to Use Bluetooth® LE Connections (Bluetooth® LE Only)

#### About GATT Characteristics

Devices use standard Bluetooth® Low Energy Generic Attribute Profile (GATT). Characteristics used:

| Characteristic UUID | Purpose               |
|--------------------|-----------------------|
| 0x2A00             | Device Name           |
| 0x2A19             | Battery Level         |
| Vendor-specific    | MMS Write/Notify      |

#### DynaFlex Bluetooth® LE protocol

1. Connect to device and discover characteristics
2. Enable notifications on MMS Notify characteristic
3. Write MMS commands to MMS Write characteristic
4. Handle responses via notifications

---

### How to Use RS-232/UART Connections (SLIP Only)

Devices with RS-232 or UART interface use SLIP encoding for MMS messages. Baud rate and parity must match device configuration.

---

### How to Use SLIP Format (SLIP Only)

SLIP (Serial Line Internet Protocol) wraps binary data for serial transmission. End byte: 0xC0. Escapes: 0xDB → 0xDBDC, 0xC0 → 0xDBDC.

Example:

```
Input:  [C0] 02 A0 01 ... [C0]
Escaped: [C0] 02 A0 01 ... [DB DC] [C0]
```

---

### How to Use Apple iAP2 Connections (iAP2 Only)

Devices that support iAP2 establish sessions using Apple’s External Accessory framework. Messages are sent using MMS over iAP2 framing.

Session setup is handled automatically by the Apple device.

Use the iOS External Accessory API to exchange data.

---

_End of Section 2.0 - All connection types rendered completely._
