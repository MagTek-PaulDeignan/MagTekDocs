---
title: DynaFlexII
nav_order: 5
layout: home
---

# DynaFlex Products
## Three-way Secure Card Reader Authenticators
## Programmer’s Manual (COMMANDS)

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


1 Introduction
1.1 About This Document
This document describes how to communicate with Secure Card Reader Authenticator (SCRA) devices
which implement MagTek Messaging Schema (MMS) and the DynaFlex family, DynaFlex II Go and
DynaProx system architecture.
This document also describes how to communicate with PIN Entry Devices (PED) which implement
MagTek Messaging Schema (MMS) and the DynaFlex/DynaProx family system architecture. (PED
ONLY)
The document uses bold face to:
• Highlight terms / concepts being formally defined in the current sentence / paragraph
• Highlight important distinguishing keywords in sentences
• Indicate hyperlinks to other sections / tables
The document uses a small number of annotation standards that are important to understand:
• Hexadecimal values are prefixed with 0x unless the context clearly indicates an un-prefixed number
is hexadecimal (for example, TLV tags, lengths, and values are always assumed to be hex).
• Binary values are prefixed with 0b unless the context clearly indicates the value is binary.
• Decimal values are not prefixed unless required for clarity, in which case the prefix is 0d.
The standard documented by this document makes extensive use of Tag-Length-Value encoding. Section
3.2.1 Tag-Length-Value (TLV) Encoding describes how to encode and decode TLV, and how to read the
tables in this document that describe TLV data objects.


[Just the Docs]: https://just-the-docs.github.io/just-the-docs/
[GitHub Pages]: https://docs.github.com/en/pages
[README]: https://github.com/just-the-docs/just-the-docs-template/blob/main/README.md
[Jekyll]: https://jekyllrb.com
[GitHub Pages / Actions workflow]: https://github.blog/changelog/2022-07-27-github-pages-custom-github-actions-workflows-beta/
[use this template]: https://github.com/just-the-docs/just-the-docs-template/generate
