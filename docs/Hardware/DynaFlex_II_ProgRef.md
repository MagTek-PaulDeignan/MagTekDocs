---
title: Programmer's Reference Manual
layout: home
parent: DynaFlex_II_PED
nav_order: 3
---

# DynaFlex Products
## Three-way Secure Card Reader Authenticators  Programmer’s Manual (COMMANDS)

INFORMATION IN THIS PUBLICATION IS SUBJECT TO CHANGE WITHOUT NOTICE.
MAGTEK CANNOT BE HELD LIABLE FOR ANY USE OF THE CONTENTS OF THIS
DOCUMENT. ANY CHANGES OR IMPROVEMENTS MADE TO THIS PRODUCT WILL BE
INCLUDED IN THE NEXT PUBLICATION RELEASE. IF YOU HAVE QUESTIONS ABOUT
SPECIFIC FEATURES AND FUNCTIONS OR WHEN THEY WILL BECOME AVAILABLE,
PLEASE CONTACT YOUR MAGTEK REPRESENTATIVE.
MagTek®, MagnePrint®, and MagneSafe® are registered trademarks of MagTek, Inc.
Magensa™ is a trademark of MagTek, Inc.
AAMVA™ is a trademark of AAMVA.
American Express® and EXPRESSPAY FROM AMERICAN EXPRESS® are registered trademarks of
American Express Marketing & Development Corp.
D-PAYMENT APPLICATION SPECIFICATION® is a registered trademark of Discover Financial
Services CORPORATION
MasterCard® is a registered trademark and PayPass™ and Tap & Go™ are trademarks of MasterCard
International Incorporated.
Visa® and Visa payWave® are registered trademarks of Visa International Service Association.
ANSI®, the ANSI logo, and numerous other identifiers containing "ANSI" are registered trademarks,
service marks, and accreditation marks of the American National Standards Institute (ANSI).
ISO® is a registered trademark of the International Organization for Standardization.
UL™ and the UL logo are trademarks of UL LLC.
PCI Security Standards Council® is a registered trademark of the PCI Security Standards Council, LLC.
EMV® is a registered trademark in the U.S. and other countries and an unregistered trademark elsewhere.
The EMV trademark is owned by EMVCo, LLC. The Contactless Indicator mark, consisting of four
graduating arcs, is a trademark owned by and used with permission of EMVCo, LLC.
The Bluetooth® word mark and logos are registered trademarks owned by Bluetooth SIG, Inc. and any
use of such marks by MagTek is under license.
Google Play™ store, Google Wallet™ payment service, and Android™ platform are trademarks of
Google LLC.
Apple Pay®, iPhone®, iPod®, Mac®, and OS X® are registered trademarks of Apple Inc., registered in
the U.S. and other countries. iPad™ is a trademark of Apple. Inc. App StoreSM is a service mark of
Apple Inc., registered in the U.S. and other countries. IOS is a trademark or registered trademark of
Cisco in the U.S. and other countries and is used by Apple Inc. under license.
Microsoft®, Windows®, and .NET® are registered trademarks of Microsoft Corporation.
MIFARE, the MIFARE logo, MIFARE Ultralight, MIFARE Plus, MIFARE Classic, MIFARE MINI®
MIFARE FleX, DESFire, and MIFARE4Mobile are registered trademarks of NXP B.V.
All other system names and product names are the property of their respective owners.


# 1 Introduction
## 1.1 About This Document
This document describes how to communicate with Secure Card Reader Authenticator (SCRA) devices
which implement MagTek Messaging Schema (MMS) and the DynaFlex family, DynaFlex II Go and
DynaProx system architecture.
This document also describes how to communicate with PIN Entry Devices (PED) which implement
MagTek Messaging Schema (MMS) and the DynaFlex/DynaProx family system architecture. (PED
ONLY)

The document uses **bold** face to:
* Highlight terms / concepts being formally defined in the current sentence / paragraph
* Highlight important distinguishing keywords in sentences
* Indicate hyperlinks to other sections / tables

The document uses a small number of annotation standards that are important to understand:
* Hexadecimal values are prefixed with 0x unless the context clearly indicates an un-prefixed number
is hexadecimal (for example, TLV tags, lengths, and values are always assumed to be hex).
* Binary values are prefixed with 0b unless the context clearly indicates the value is binary.
* Decimal values are not prefixed unless required for clarity, in which case the prefix is 0d.

The standard documented by this document makes extensive use of Tag-Length-Value encoding. Section
3.2.1 Tag-Length-Value (TLV) Encoding describes how to encode and decode TLV, and how to read the
tables in this document that describe TLV data objects.



## 2.1.3 How to Send Command Requests Using the USB Connection
MMS communication between the host and the device consists of Messages, which are independent of
connection type and are documented in section 2.4. This section focuses specifically on how to use the
device’s USB HID connection to transmit a Command to the host by composing and sending a Request
Message, then listening for and interpreting the corresponding Response Message.
When the device is connected to the host via USB, the host sends one or more Output Reports to the
device to send the requests for commands, and listens / waits for the device to send one or more Input
Reports containing a response (see section 2.1.1). All reports use Usage Page 0xFF00, Usage ID 0x20,
and no Report ID (which some platform libraries present to the calling software as Report ID 0x00).
The host may send Output Reports by using either the default Control pipe or the Interrupt OUT pipe
using a blocking call to the platform’s USB libraries. The device ACKs all Output Reports immediately.
Upon detecting the ACK for the last Output Report in the message stream, the host software can
immediately begin listening for one or more follow-up Input Reports containing the device’s response.
Some messages defined in section 2.4 may exceed the maximum packet length allowed by USB HID.
For this reason, MMS implements a packetizing scheme the host must use when it composes Output
Reports to send commands, and when it decomposes Input Reports to receive responses. The host should
follow this general sequence to send a request and receive a response:

1)  Choose the command to invoke from section 6 Commands.
2) Construct the command request message using the Request table in the command documentation.
For a deeper explanation of the contents of request tables, see section 2.4.
3) .
4) Determine the complete length of the command request message.
5) Examine the device’s Report Descriptor to determine what payload length the device expects for an
Output Report (operating system libraries may refer to this length as the “Report Length” or “Report
Count”). MMS devices using USB HID generally use a payload length of 64 bytes.
a)  If the message length fits the Single Packet payload length of 62 bytes, wrap the message in the
Single Packet format shown in Table 2.1-1.
b) If the message length does not fit the Single Packet payload length, wrap the message in the
format of a single Multi-Packet Head, followed by zero or more Multi-Packet Middles as
necessary, followed by one Multi-Packet Tail, as shown in Table 2.1-2, Table 2.1-3, and Table
2.1-4. If necessary, the host can cancel in the middle of a Multi-Packet message using the Multi-
Packet Cancel packet shown in Table 2.1-5.

6) For each packet, send an Output Report to the device, and wait for the device to ACK the output
report USB packet. Upon ACK, either send the next packet in the sequence (if any), or begin
listening for an Input Report containing the device’s response message [see section 2.1.4 How to
Receive Data Using the USB Connection (HID Only)]. If an ACK does not arrive, time out and
assume the command needs to be started again.

7) Strip wrappers off the device’s response in exactly the same way you constructed the command (using
either Single Packet format or Multi-Packet format), and recompose the response message. Be sure to
assemble the packets in the correct order using Packet Number, and to truncate the padding based on
Message Length or Remaining Message Length.
8) Parse the final response message using the Response table in the documentation for the command.

[Just the Docs]: https://just-the-docs.github.io/just-the-docs/
[GitHub Pages]: https://docs.github.com/en/pages
[README]: https://github.com/just-the-docs/just-the-docs-template/blob/main/README.md
[Jekyll]: https://jekyllrb.com
[GitHub Pages / Actions workflow]: https://github.blog/changelog/2022-07-27-github-pages-custom-github-actions-workflows-beta/
[use this template]: https://github.com/just-the-docs/just-the-docs-template/generate
