---
title: DynaFlexIIGO
nav_order: 5
layout: home
---

MagTek I 1710 Apollo Court I Seal Beach, CA 90740 I Phone: (562) 546-6400 I Technical Support: 562-546-6800
www.magtek.com
DynaFlex II Go
Secure Card Reader Authenticator
Installation and Operation Manual
April 2024
Document Number:
D998200595-120
REGISTERED TO ISO 9001:2015
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 2 of 62 (D998200595-120)
Copyright © 2006 - 2024 MagTek, Inc.
Printed in the United States of America
INFORMATION IN THIS PUBLICATION IS SUBJECT TO CHANGE WITHOUT NOTICE. MAGTEK CANNOT BE HELD LIABLE FOR ANY USE OF THE CONTENTS OF THIS DOCUMENT. ANY CHANGES OR IMPROVEMENTS MADE TO THIS PRODUCT WILL BE INCLUDED IN THE NEXT PUBLICATION RELEASE. IF YOU HAVE QUESTIONS ABOUT SPECIFIC FEATURES AND FUNCTIONS OR WHEN THEY WILL BECOME AVAILABLE, PLEASE CONTACT YOUR MAGTEK REPRESENTATIVE.
MagTek®, MagnePrint®, and MagneSafe® are registered trademarks of MagTek, Inc.
Magensa™ is a trademark of MagTek, Inc.
AAMVA™ is a trademark of AAMVA.
ANSI®, the ANSI logo, and numerous other identifiers containing "ANSI" are registered trademarks, service marks, and accreditation marks of the American National Standards Institute (ANSI).
ISO® is a registered trademark of the International Organization for Standardization.
UL™ and the UL logo are trademarks of UL LLC.
PCI Security Standards Council® is a registered trademark of the PCI Security Standards Council, LLC.
EMV® is a registered trademark in the U.S. and other countries and an unregistered trademark elsewhere. The EMV trademark is owned by EMVCo, LLC. The Contactless Indicator mark, consisting of four graduating arcs, is a trademark owned by and used with permission of EMVCo, LLC.
Google Play™ store, Google Wallet™ payment service, and Android™ platform are trademarks of Google LLC.
Apple Pay®, Apple Wallet®, iPhone®, iPod®, Mac®, and OS X® are registered trademarks of Apple Inc., registered in the U.S. and other countries. iPad™ is a trademark of Apple. Inc. App StoreSM is a service mark of Apple Inc., registered in the U.S. and other countries. Apple and MFi are registered trademarks of Apple Inc. IOS is a trademark or registered trademark of Cisco in the U.S. and other countries and is used by Apple Inc. under license.
The OtterBox® and uniVERSE® trademarks are property of Otter Products, LLC, registered in the U.S. and other countries.
MIFARE®, MIFARE Classic ®, and MIFARE® DESFire®, are registered trademarks of NXP Semiconductors Austria GmbH Styria, All rights reserved.
The Bluetooth® word mark, logos, and Bluetooth® Low Energy (LE) are registered trademarks owned by Bluetooth® SIG, Inc.
Microsoft®, Windows®, and .NET® are registered trademarks of Microsoft Corporation.
All other system names and product names are the property of their respective owners.
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 3 of 62 (D998200595-120)
Table 0-1 - Revisions Rev Number Date Notes
100
November 16, 2023
Initial release
110
February 1, 2024
Update all Device Images, Update Device Specifications throughout document; Updated 1.1 Key Features and Components to include NFC Tag/Mifare Classic/Mifare DESFire Light, and Buzzer command support; Added 6.4.1 How to Play a Sequence of Tones; Added 7.9.5 How to Tap NFC Contactless IC Products and Send Pass-through Commands. miscellaneous clarifications and corrections.
120
April 12, 2024
Update Table 1-2 - DynaFlex II Go Accessories with current USB Type A-C and type C cable Part Numbers and Descriptions, Add section 7.5.7 DynaFlex II Go Bluetooth® Low Energy (LE) Sleep Mode, Add 6.2 Physical Button Operation, Add reference to BLE Sleep mode in 6.3 About Operating Modes
0 - Table of Contents
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 4 of 62 (D998200595-120)
Table of Contents
Table of Contents .............................................................................................................................................. 4
1 Introduction ............................................................................................................................................... 6
1.1 Key Features and Components ...................................................................................................... 6
1.2 Available Models and Accessories ................................................................................................ 7
1.3 About Terminology ........................................................................................................................... 9
2 Planning and Preparation ..................................................................................................................... 10
2.1 Logistical Planning ......................................................................................................................... 10
3 Handling and Storage ............................................................................................................................ 12
3.1 Handling to Avoid Damage ........................................................................................................... 12
3.2 Handling to Avoid Accidental Tamper ......................................................................................... 12
4 Installation ............................................................................................................................................... 13
4.1 About Inspection............................................................................................................................. 13
4.2 About Host Software ...................................................................................................................... 13
4.3 Connecting DynaFlex II Go to a Host ........................................................................................... 14
4.3.1 How to Connect DynaFlex II Go to a Host Computer via USB-C ...................................... 14
4.3.2 How to Connect DynaFlex II Go to an iOS Host via Bluetooth® Low Energy (LE) ........ 16
4.3.3 How to Connect DynaFlex II Go to an Android Host via Bluetooth® Low Energy (LE) . 16
4.3.4 How to Connect DynaFlex II Go to a Windows 10 Host [Version 1703 or Above] via Bluetooth® Low Energy (LE) (Windows Drivers) ................................................................................ 17
4.4 Mounting .......................................................................................................................................... 17
4.4.1 About Mounting ...................................................................................................................... 17
4.4.2 How to Mount DynaFlex II Go ............................................................................................... 18
5 Configuration ........................................................................................................................................... 19
6 Operation ................................................................................................................................................. 20
6.1 Operation Overview ........................................................................................................................ 20
6.2 Physical Button Operation ............................................................................................................ 20
6.3 About Operating Modes ................................................................................................................. 22
6.4 About Sounds .................................................................................................................................. 22
6.4.1 How to Play a Sequence of Tones ....................................................................................... 23
7 Introduction to User Interface ............................................................................................................... 23
7.1 Component Details ........................................................................................................................ 24
7.2 Power On via USB Cable LED Behavior ....................................................................................... 25
7.3 USB Enumeration ........................................................................................................................... 25
7.4 About the Status LEDs ................................................................................................................... 26
7.5 Bluetooth® Low Energy (LE) LED Behavior ................................................................................ 27
7.5.1 Bluetooth® Low Energy (LE) Status LED 2 and LED 3 ..................................................... 27
7.5.2 Power On DynaFlex II Go in Battery Operating Mode ....................................................... 27
7.5.3 Power Off DynaFlex II Go in Battery Operating Mode ...................................................... 28
0 - Table of Contents
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 5 of 62 (D998200595-120)
7.5.4 DynaFlex II Go Bluetooth® Low Energy (LE) Host Pairing ............................................... 29
7.5.5 DynaFlex II Go Bluetooth® Low Energy (LE) Host Connected ......................................... 30
7.5.6 DynaFlex II Go Bluetooth® Low Energy (LE) Host Disconnect ........................................ 30
7.5.7 DynaFlex II Go Bluetooth® Low Energy (LE) Sleep Mode ................................................ 31
7.6 LED Behavior: Successful Transactions ...................................................................................... 31
7.6.1 BCR Payment Transaction Successful (Connected via USB)........................................... 31
7.6.2 MSR Payment Transaction Successful (Connected via USB) .......................................... 32
7.6.3 EMV Contact Payment Transaction Successful (Connected via USB)............................ 33
7.6.4 EMV Contactless Payment Transaction Successful (Connected via USB) .................... 33
7.6.5 BCR Payment Transaction Successful (Connected via Bluetooth® LE) ........................ 34
7.6.6 MSR Payment Transaction Successful (Connected via Bluetooth® LE) ....................... 35
7.6.7 EMV Contact Payment Transaction Successful (Connected via Bluetooth® LE) ......... 35
7.6.8 EMV Contactless Payment Transaction Successful (Connected via Bluetooth® LE) .. 36
7.7 LED Behavior: Errors, Timeouts, and Canceled Transactions .................................................. 36
7.8 Power Management....................................................................................................................... 39
7.8.1 About Power ........................................................................................................................... 39
7.8.2 How to Charge the Battery ................................................................................................... 39
7.8.3 How to Power On / Wake Up from Standby Mode / Power Off ...................................... 39
7.8.4 About Maintenance Reset .................................................................................................... 40
7.9 Card Reading .................................................................................................................................. 41
7.9.1 About Reading Cards ............................................................................................................. 41
7.9.2 How to Tap Contactless Cards / Devices ........................................................................... 41
7.9.3 How to Scan Barcodes .......................................................................................................... 42
7.9.4 Apple VAS for DynaFlex II Go ............................................................................................... 44
7.9.4.1 VAS App and Payment Mode (Dual Mode) ................................................................ 44
7.9.4.2 VAS App Only Mode (VAS Mode) ................................................................................. 44
7.9.4.3 VAS App or Payment Mode (Single Mode) ................................................................. 44
7.9.4.4 Payment Only Mode (Payment Mode) ........................................................................ 44
7.9.5 How to Tap NFC Contactless IC Products and Send Pass-through Commands ........... 45
8 Maintenance ............................................................................................................................................ 46
8.1 Mechanical Maintenance .............................................................................................................. 46
8.2 Updates to Firmware, Documentation, Security Guidance...................................................... 46
9 Developing Custom Software ............................................................................................................... 47
Appendix A Technical Specifications ....................................................................................................... 48
Appendix B Barcode Reader Symbologies .............................................................................................. 51
Appendix C Optional Accessories ............................................................................................................. 52
Appendix D Warranty, Standards, and Certifications ............................................................................ 56
1 - Introduction
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 6 of 62 (D998200595-120)
1 Introduction
DynaFlex II Go and DynaFlex II Go with Barcode Reader (BCR) deliver the next generation of mobile payment solutions. Both models offer an integrated secure card reader authenticator for magnetic stripe cards, EMV chip cards (contact and contactless), and NFC enabled mobile wallets including Samsung Pay, Google Pay™ with support for Google VAS, and Apple Pay® with support for Apple VAS. Ideal for cafés, restaurants, boutiques, airlines, retail banks and other developers looking to build a secure payment solution that accepts contactless EMV and NFC payments. DynaFlex II Go is suited for deployment in many scenarios, including mobile handsets, tablets, and desktop computers.
DynaFlex II Go and DynaFlex II Go BCR are equipped with MagneSafe® Security Architecture (MSA). The design and architecture meet the requirements for contactless EMV 3.1, PCI PTS POI v6.2, and support triple DEA encryption with DUKPT Key Management.
1.1 Key Features and Components
DynaFlex II Go and DynaFlex II Go BCR are easy to install and configure, with key features that include:
•
Contactless EMV 3.1 Approved.
•
Contact EMV 4.4a Approved.
•
PCI PTS POI v6.2 Approved.
•
Optical reading for many 2D and 1D barcodes including PayPal and Venmo (DynaFlex II Go BCR Model Only).
•
Transducer for audio alerts.
•
User configurable audio commands to play a sequence of tones.
•
Bluetooth® Low Energy (LE).
•
USB-C interface.
•
iAP2® Protocol Support.
•
Triple DEA encryption / DUKPT key management.
•
AES-128 and AES-256 encryption.
•
Ingress protection - IP 30.
•
Apple Pay® / Apple Wallet® (Apple VAS protocol support).
•
Google Wallet Smart Tap. (Google VAS protocol support).
•
Google Pay™.
•
NFC Compatibility: Smart cards and contactless IC products, including MIFARE®, MIFARE Classic®, and MIFARE® DESFire® Light, with the ability to send pass-through commands. • Optional OtterBox® uniVERSE® case.
•
Optional countertop stand.
Figure 1-1 illustrates the major components of DynaFlex II Go (BCR model shown). Models without a barcode reader are identical to the illustration, but do not have a camera and do not have a QR code printed on the front face.
1 - Introduction
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 7 of 62 (D998200595-120)
Figure 1-1 - DynaFlex II Go Major Components
1.2 Available Models and Accessories
Table 1-1 - Available Models and Options Part No. Description Display Connection(s) Operating Systems
21078400
DynaFlex II Go, PCI, BCR, BLACK, BLUETOOTH LE
None
USB-C, Bluetooth® (LE), iAP2®
MS Windows, Mac OS, Linux; Android Phone
21078401
DynaFlex II Go, PCI, BLACK, BLUETOOTH LE
None
USB-C, Bluetooth® (LE), iAP2®
MS Windows, Mac OS, Linux; Android Phone
21078402
DynaFlex II Go, PCI, BCR, BLACK
None
USB-C, iAP2®
MS Windows, Mac OS, Linux; Android Phone
21078403
DynaFlex II Go, PCI, BLACK
None
USB-C, iAP2®
MS Windows, Mac OS, Linux; Android Phone
21078404
DynaFlex II Go, PCI, BCR, BLACK, BLUETOOTH LE, LOCKED MAGENSA BUNDLE LMB
None
USB-C, Bluetooth® (LE), iAP2®
MS Windows, Mac OS, Linux; Android Phone
21078405
DynaFlex II Go, PCI, BLACK, BLUETOOTH LE, LOCKED MAGENSA BUNDLE LMB
None
USB-C, Bluetooth® (LE), iAP2®
MS Windows, Mac OS, Linux; Android Phone
21078406
DynaFlex II Go, PCI, BCR, BLACK, LOCKED MAGENSA BUNDLE LMB
None
USB-C, iAP2®
MS Windows, Mac OS, Linux; Android Phone
21078407
DynaFlex II Go, PCI, BLACK, LOCKED MAGENSA BUNDLE LMB
None
USB-C, iAP2®
MS Windows, Mac OS, Linux; Android Phone
1 - Introduction
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 8 of 62 (D998200595-120)
Table 1-2 - DynaFlex II Go Accessories Part # Description Accessory Notes
1000005076
CABLE, USB-C TO USB TYPE A MALE USB 2.0, 20AWG
Optional, specify in order
1000006016
USB CABLE TYPE A – C, 6FT
Optional, specify in order
1000006017
USB CABLE TYPE C, 6FT
Optional, specify in order
21078408
DYNAFLEX II GO, KIT COUNTERTOP STAND
Refer to Appendix C Optional Accessories for additional information.
21078409
DYNAFLEX II GO ADAPTOR FOR OTTERBOX
Refer to Appendix C Optional Accessories for additional information.
21078410
DYNAFLEX II GO RUBBER SLEEVE
Refer to Appendix C Optional Accessories for additional information.
21078411
DYNAFLEX II GO RUBBER SLEEVE HALF SIZE
Refer to Appendix C Optional Accessories for additional information.
Note: At least one cable will be shipped with the device, specify when ordering.
1 - Introduction
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 9 of 62 (D998200595-120)
1.3 About Terminology
In this document, DynaFlex II Go products are referred to as the device. They are designed to be connected to a host, which is a piece of general-purpose electronic equipment that can send commands and data to, and receive data from, the device. Host types include PC and Mac computers/laptops, tablets, and smartphones. Generally, the host must have software installed that communicates with the device and is capable of processing transactions. During a transaction, the host and its software interact with the operator, such as a customer service representative, while the device interacts with the cardholder (even if the cardholder is using a virtual representation of the card account, such as a smartphone).
2 - Planning and Preparation
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 10 of 62 (D998200595-120)
2 Planning and Preparation
The guidelines in the following sections are intended to help project planners and system administrators plan for the physical and logical requirements of deploying and using DynaFlex II Go products. The most effective way to ensure smooth deployment of a solution is to consider these factors before receiving the device.
2.1 Logistical Planning
•
Determine what type of host DynaFlex II Go will connect to. For a list of supported device types and operating systems, see Table 1-1. When planning, be sure to include any additional support or devices required by the host and DynaFlex II Go, such as physical locations, mounting, power connections, and charging cradles.
•
Determine what connection the host will use to communicate with the device. The available connections are USB-C for power and control and Bluetooth® Low Energy (LE) for wireless connectivity (see Table 1-1).
•
Determine what software will be installed on the host and how it will be configured. Software can include the operating system, transaction processing software, security software, and so on. If teams other than the software development team will be involved in preliminary device testing, MagTek recommends the solution development team provide a smoke test harness early in the development process to allow basic testing (for example, communication adapter testing). In addition, be sure to plan for any additional support required by the software, such as software licenses and network connections. Information about software is provided in section 4.2 About Host Software.
•
Determine how the device will be physically presented to the cardholder. If the device is mounted, make sure there is adequate clearance for cardholders to swipe, insert, and tap. If the solution design includes metal objects anywhere near the device, including metal enclosures, make sure that at all points the metal is no closer than 15mm from the MSR swipe path or card insertion slot. Proximity to metal can adversely affect the device’s performance.
•
Determine how the device should be configured and specify that configuration when ordering the device. A full list of configurable options is documented in D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS).
•
Select and configure a secure workstation that advanced operators will use to configure and/or update the device. The workstation must be configured as follows:
o
Available USB port.
o
A secure means of obtaining files, either via the network (such as SFTP) or via removable media, such as USB flash drives. This is required for installing software tools, copying firmware files, etc. If you are using Magensa Services, make sure the secure workstation has an internet connection and has all the required Magensa Remote Services software components installed.
o
1000007406 DynaFlex, DynaProx Test Utility installed, which advanced operators can use to configure and test the device.
•
Determine the final set of tools advanced operators will use to configure, test, and update the device. This documentation uses the 1000007406 DynaFlex, DynaProx Test Utility as an example for configuring the device; it can be used for initial pre-deployment testing and development, and as sample code showing how to communicate with the device, but the full solution may call for customized, solution-specific software for configuring the device and updating firmware.
•
Determine how to inspect devices upon arrival, upon installation, and periodically during live usage, to ensure malicious individuals have not tampered with them. Details about inspection are provided in section 4.1 About Inspection.
2 - Planning and Preparation
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 11 of 62 (D998200595-120)
•
Develop procedures for maintaining the device(s). Detailed guidance is provided in section 8 Maintenance.
•
Determine how to train operators. For example, training may include information extracted from section 5 Configuration, section 6 Operation, and section 8 Maintenance.
•
Review the device’s PCI Security Policy, posted to the PCI web site www.pcisecuritystandards.org under Approved PIN Transaction Security (PTS) Devices, for additional information about using the device securely.
3 - Handling and Storage
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 12 of 62 (D998200595-120)
3 Handling and Storage
Proper handling of the device throughout delivery, assembly, shipping, installation, usage, and maintenance is very important. Not following the guidelines in this document could damage the device, render it inoperable, and/or violate the conditions of the warranty.
3.1 Handling to Avoid Damage
Upon receiving the device, inspect it to make sure it originated from an authentic source and has not been tampered with. For details, see D998200593 DynaFlex II Go Device Inspection Document, available from MagTek.
From device delivery through assembly, shipping, installation, usage, and maintenance, the device must not be exposed to conditions outside the ratings in Appendix A Technical Specifications.
If the device is exposed to cold temperatures, adjust it to warmer temperatures gradually to avoid condensation, which can interfere with the operation of the device or cause permanent damage.
Do not drop or shake the device.
For information about ongoing maintenance of the device, such as cleaning, see section 8 Maintenance.
3.2 Handling to Avoid Accidental Tamper
DynaFlex II Go products implement active tamper detection, which uses a small amount of electricity even when the device is completely powered off. When unpowered by an external power supply, the device powers its active tamper detection circuitry using its non-rechargeable internal backup battery. This provides 5 years of backup shelf life across the entire life of the device. If the backup battery is allowed to completely discharge, the device’s tamper detection engages and locks down the device, and it must be returned to the manufacturer to reset.
To avoid accidental tamper events and to optimally condition the battery, follow these precautions:
•
Temperature is the most critical factor in extending battery life and preserving battery charge. Store the device at the lowest reasonable temperatures within its specified storage temperature range (see Appendix A Technical Specifications). Storing at temperatures between -4°F to 113°F (-20°C to 45°C).
•
Do not drop or shake the device.
•
Do not attempt to disassemble the device.
4 - Installation
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 13 of 62 (D998200595-120)
4 Installation
Installing DynaFlex II Go products is straightforward: The manufacturer or acquirer, configures the preferred settings, keys, terminal, and payment brand settings before deployment; end users need only set up a host with appropriate software, configure the software, and connect the device to the host. This section provides general information about inspecting, connecting, and installing DynaFlex II Go products.
4.1 About Inspection
Before unpacking the device, it is important to inspect its secure packaging to make sure it has not been tampered with in storage or in transit. MagTek provides details for inspecting the integrity of the device’s secure packaging in D998200594 DynaFlex II Go Package Inspection Document.
It is important to thoroughly inspect a new device before deployment, and regularly inspect devices in live usage (including its immediate surroundings) to make sure malicious individuals have not tampered with it. MagTek recommends conducting inspection training for all device operators, and an inspection schedule with checkpoints in place to make sure operators are performing inspections as specified and as scheduled. MagTek provides an easy-to-follow device inspection reference D998200593 DynaFlex II Go Device Inspection Document.
4.2 About Host Software
DynaFlex II Go products do not have a display. In any solution, DynaFlex II Go must be connected to a host, which must have software installed that can communicate with the device and is capable of processing transactions. To set up the host to work with DynaFlex II Go, follow the installation and configuration instructions provided by the vendor of the host or the host software. For information about developing custom host software, see section 9 Developing Custom Software.
4 - Installation
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 14 of 62 (D998200595-120)
4.3 Connecting DynaFlex II Go to a Host
The following sections describe how to connect DynaFlex II Go to a host using the available USB-C receptacle or Bluetooth® Low Energy (LE) connections.
4.3.1 How to Connect DynaFlex II Go to a Host Computer via USB-C
Figure 4-1 - Connecting to a Host via USB-C
To connect DynaFlex II Go products to a USB host computer or charger using the USB-C port, follow these steps (for reference see Figure 4-1):For best results, use the cable that is included with the device or another cable from Table 1-2 - DynaFlex II Go Accessories on page 8. Connect the USB-C end of the cable to DynaFlex II Go see Figure 4-1 - Connecting to a Host via USB-C.
1)
Connect the other end of the USB cable to the host’s USB port.
2)
As soon as the device starts receiving power through USB, it automatically powers on.
3)
If the specific device serial number you are connecting has not been previously connected to the host, the Windows system tray on the host reports it is setting up a device.
4)
When installation is complete, Windows reports Device is ready, (see Figure 4-2 – Setup Complete) and the device shows in Windows Device Manager under Human Interface Devices (see Figure 4-3 – Windows Device Manager) as two devices: HID-compliant vendor-defined device (see Figure 4-4 – HID Compliant Vendor-defined Device Properties) with VID 0801 and PID 2024, and USB Input Device.
Figure 4-2 – Setup Complete
4 - Installation
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 15 of 62 (D998200595-120)
Figure 4-3 – Windows Device Manager
Figure 4-4 – HID Compliant Vendor-defined Device Properties
5)
The operating system may put the device into USB Suspend mode.
4 - Installation
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 16 of 62 (D998200595-120)
4.3.2 How to Connect DynaFlex II Go to an iOS Host via Bluetooth® Low Energy (LE)
To connect DynaFlex II Go via Bluetooth® LE to an iOS device, refer to section 9 Developing Custom Software and D998200386 MagTek Universal SDK for MMS Devices Programmer's Manual ( iOS ).
4.3.3 How to Connect DynaFlex II Go to an Android Host via Bluetooth® Low Energy (LE)
To connect DynaFlex II Go to an Android host that supports Bluetooth® Low Energy (LE):
1)
If any Bluetooth® Low Energy (LE) host software has an active data connection to the device, close the connection.
2)
On the Android host, install and configure the host software you intend to use with DynaFlex II Go. If you do not yet have that software, you can download a test tool from the Google Play store called MTUSDK Demo, published by MagTek, Inc..
3)
Make sure the DynaFlex II Go output connection is configured to transmit card data over Bluetooth® LE. This is the factory default.
4)
Press and hold the Power Button for 4 beeps until LED 4 starts flashing indicating Bluetooth® Pairing is in process. The Bluetooth® Status LED flashes once per second for up to three minutes, or until a host pairs or connects.
5)
On the Android host, launch the Settings application and open the Bluetooth® menu.
6)
Press the SEARCH FOR DEVICES or Scan button to show an AVAILABLE Bluetooth® DEVICES list.
7)
Locate the seven-digit serial number on the label on the bottom of the device.
8)
Device will appear in the list as DF II Go-xxxxxxx where xxxxxxx matches the serial number.
9)
When the host pops up a Bluetooth® Pairing Request message asking for a code, enter the configured passkey (or the default 000000) to return to the Bluetooth® configuration page. The device appears in the PAIRED DEVICES list.
10)
Use the host software or the MagTek Test app to test swiping a card.
11)
Remember to change the default password. See 1000007352 MagTek Universal SDK for MMS Devices (Android).
To unpair from the device, follow these steps:
1)
Locate the device in the Bluetooth® configuration page.
2)
Press the settings (gear) icon.
3)
Press the Forget button and make sure the device disappears from the Paired devices list.
4 - Installation
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 17 of 62 (D998200595-120)
4.3.4 How to Connect DynaFlex II Go to a Windows 10 Host [Version 1703 or Above] via Bluetooth® Low Energy (LE) (Windows Drivers)
To connect DynaFlex II Go to a host with Windows 10 version 1703 or above, and Bluetooth® 4.0 or higher hardware that supports Bluetooth® Low Energy (LE), follow these steps:
1)
Make sure the host’s Bluetooth® LE interface is turned on and working correctly.
2)
If any Bluetooth® Low Energy LE host software has an active data connection to the device, close the connection.
1.
On the host, install and configure the software you intend to use with DynaFlex II Go (if you do not yet have that software, you can use 1000007351 MagTek Universal SDK for MMS Devices (Windows) available from MagTek.com, to perform simple tests):
a)
Make sure the host software is configured to look for the device on the proper connection type.
b)
Make sure the host software knows which device(s) it should interface with.
c)
Make sure the host software is configured to properly interpret incoming data from the device. When using Bluetooth® LE, the device transmits data in GATT format.
3)
Make sure the DynaFlex II Go output connection is configured to transmit card data over Bluetooth® LE. This is the factory default.
4)
In the Start menu type Bluetooth® and select Bluetooth® and other devices settings, or double-click the Bluetooth® Devices icon in the taskbar to launch the Bluetooth® & other devices settings window.
5)
Locate the seven-digit serial number on the label on the bottom of the device.
6)
Press and hold the Power Button for 4 beeps until LED 4 starts flashing indicating Bluetooth® Pairing is in process. The Bluetooth® Status LED flashes once per second for up to three minutes, or until a host pairs or connects.
7)
Press the Add Bluetooth® or other device button to launch an Add a device window.
8)
Under Choose the kind of device you want to add, select Bluetooth® .
9)
Locate the device called DF II Go-xxxxxxx, where xxxxxxx matches the device’s serial number. Enter the configured passkey (or the default 999999) and press the Connect button.
10)
After a short period of time, the text Connected appears below the device you are pairing with. Note that in this case, “Connected” means the device is paired, but the host does not have an active data connection until the host software initiates one.
11)
Press the Done button to close the Add a device window.
12)
Use the host software to test swiping a card.
13)
Remember to change the default password. See the DynaFlex II Go Programmer’s Reference documents for detail to unpair the device:
1)
Select the device in the Bluetooth® and other devices settings window.
2)
Press the Remove device button.
4.4 Mounting
4.4.1 About Mounting
DynaFlex II Go products are designed to provide flexible mounting options:
•
The device can be mounted to the host via external clip or embedded lanyard.
4 - Installation
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 18 of 62 (D998200595-120)
4.4.2 How to Mount DynaFlex II Go
This document describes how to use DynaFlex II Go securely. Using the device in any way other than the approved methods described in this document invalidates the PCI PTS approval of the device.
Not following the guidelines in this section could damage the device, render it inoperable, and/or violate the conditions of the warranty.
This section provides information and guidelines for designing the mechanical aspects of a solution that incorporates DynaFlex II Go products. MagTek strongly recommends vetting and testing solution designs before finalizing and deploying them, to make sure the design meets all requirements (e.g., functional, legal, security, certification, safety, and so on).
When designing the mechanical portions of a solution that incorporates DynaFlex II Go products, consider the following:
•
Review section 1.1 Key Features and Components for an overall introduction to the device’s physical features and what they are called.
•
Review Appendix A Technical Specifications.
•
Review the information below about overall device dimensions and mounting hole locations and use.
•
Review any additional requirements from other agencies, such as PCI and EMV solution certification requirements, safety ordinances, and so on, which may introduce additional constraints to the design.
Overall dimensions of the device are shown in Figure 4-5. On request, MagTek can provide a 3D model of the device’s envelope to assist with the mechanical portion of solution design. MagTek strongly recommends building and testing prototypes with actual devices before finalizing the solution design.
Figure 4-5 - DynaFlex II Go Overall Dimensions
When designing an enclosure or mounting bracket, make sure there is adequate clearance for cardholders to tap or users to present a bar code. Proximity to metal can reduce the device’s reading range.
5 - Configuration
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 19 of 62 (D998200595-120)
5 Configuration
The device does not have an on-screen configuration interface. However, it does have settings the host can change using commands. These settings are documented as Properties in D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS).
6 - Operation
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 20 of 62 (D998200595-120)
6 Operation
6.1 Operation Overview
The operator initiates a transaction from the host, and the cardholder interacts with the device. Transaction types may include retail transactions, new accounts, teller window applications, checking, savings, mortgages, and any other type of transaction where there is interaction between the cardholder and the operator.
For each transaction type, the host software directs the cardholder. The transaction flow on the device may differ depending on what the host software specifies and what the cardholder does. Section 7.9 Card Reading provides examples of the cardholder experience for each type of payment. If the device cannot read payment data, the host software may require the cardholder to repeat the action or require the host to reject the transaction.
6.2 Physical Button Operation
All DynaFlex II Go devices have a single physical button, see Figure 6-1 - Power Button. Pressing and holding this button can activate extra functions. To active a specific function, press and hold the button until a specific number of beeps are heard. Table 6-1 - Button Functions contains functions that can be activated. Beep counts that are not listed are not supported.
Figure 6-1 - Power Button
Table 6-1 - Button Functions Beep Count Function 2
Power Off
Hold for two beeps to power the device off. The device will reboot if it is connected to USB when powered off. 3
Settings Menu
SoftAP Mode in the Settings Menu is Available on WLAN enabled devices only.
6 - Operation
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 21 of 62 (D998200595-120)
Beep Count Function 4
BLE Pairing
BLE Enabled devices only. 5
Demo
See Appendix C for more information. 6
Battery Level
Light the LEDs to indicate the current state of charge of the battery. The LEDs will light for 3 seconds then return to their original state.
DynaFlex II Go has only green LEDs. Instead of lighting the first LED in amber, it will slowly flash the first LED. Instead of Red, the first LED will flash quickly.
6 - Operation
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 22 of 62 (D998200595-120)
6.3 About Operating Modes
During operation, DynaFlex II Go devices transition between distinct operating modes, which are important for operators to understand:
•
Powered Off Mode is the shipping and storage mode of the device. No external power is applied to the device through the USB cable or from the internal rechargeable battery. In this mode, the device consumes very little power. To set the device from Powered Off mode to Active Mode, connect the device to USB power, or press the power button, see Figure 6-1 - Power Button .
•
Active Mode is the device’s normal “awake” state when it is in use. In this mode, the device LED indicators are powered on, and the device is ready to receive commands from the host. For more information on Status LEDs and LED behavior see sections 7.4 About the Status LEDs, 7.5 Bluetooth® Low Energy (LE) LED Behavior, 7.5.7 DynaFlex II Go Bluetooth® Low Energy (LE) Sleep Mode
When in Bluetooth® LE Sleep Mode, DynaFlex II Go will conserve battery life by limiting power to non-essential hardware features and entering low power mode. When in Sleep Mode, the device will appear to be powered off, with no LEDs illuminated, see Figure 7-15 – Bluetooth® (LE) Sleep Mode. For information on how to disable this feature, see D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS).
Figure 7-15 – Bluetooth® (LE) Sleep Mode
•
LED Behavior: Successful Transactions, and 7.7 LED Behavior: Errors, Timeouts, and Canceled Transactions. To set the device from Active mode to Powered Off mode remove power press and hold the power button for two beeps.
•
BLE Sleep Mode is a standard feature that conserves battery life by limiting power to non-essential hardware features. When in Sleep Mode, the device will appear to be powered off, with no LEDs illuminated, see 7.5.7 DynaFlex II Go Bluetooth® Low Energy (LE) Sleep Mode, for more information on BLE Sleep Mode.
6.4 About Sounds
DynaFlex II Go products have a beeper that provides feedback to operators and cardholders about the internal state of the device:
•
The device sounds one short beep after it has successfully read a contactless tap, and the cardholder can safely remove the card or device from the contactless landing zone.
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 23 of 62 (D998200595-120)
•
The device emits two beeps when reading a card or contactless payment device to indicate a card read error occurred.
•
The device sounds two beeps when an operator cancels a pending EMV transaction.
The device provides an internal setting the host can use to adjust the global system volume. The device does not provide an interface to change the volume setting directly via buttons. If the device is too quiet or too loud:
•
Make sure the device is being ordered from the manufacturer with the desired volume setting.
•
Check to see whether the host software you are using provides a feature to check and/or adjust the volume setting.
•
If the host software does not provide that feature, request help from the development team that built the host software to check / change the volume setting. For details, see D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS).
6.4.1 How to Play a Sequence of Tones
To play a sequence of tones, follow these steps:
1)
Make sure the device is in idle state.
2)
Send an audio command to the device to play a sequence of tones. For details, see D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS).
7 Introduction to User Interface
This section contains information on DynaFlex II Go's LEDs, beeper, and BCR status LED. It is important to note that DynaFlex II Go devices are equipped with an optional rechargeable battery. If there is no power supply to the device through the USB cable or optional internal rechargeable battery, all LEDs, along with the BCR status LED, will not illuminate. When this occurs, the user interface will resemble the device as shown in Figure 7-1.
As mentioned in section 1.1 Key Features and Components, DynaFlex II Go models equipped with a barcode reader (BCR) have a similar physical appearance as models without a BCR, as shown in Figure 7-1. BCR models are equipped with a camera and a QR code located on the front side of the device.
•
DynaFlex II Go devices have a user interface composed of three elements: a visual indicator consisting of four LEDs, a beeper that produces audible alerts, and a power button see Figure 6-1 - Power Button.
•
DynaFlex II Go BCR devices have a user interface composed of four elements: a visual indicator consisting of four LEDs, a barcode reader status LED, a beeper that produces audible alerts, and a power button see Figure 6-1 - Power Button.
•
DynaFlex II Go devices do not feature input components such as touch screens.
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 24 of 62 (D998200595-120)
Figure 7-1 – DynaFlex II Go and DynaFlex II Go BCR
7.1 Component Details
1.
LED Ordering
The arrangement of the four LED indicators on DynaFlex II Go devices is illustrated in Figure 7-2. The LEDs are designated 1 to 4 and are ordered from left to right on the device.
Figure 7-2 - LED Ordering
2.
LED Status
When DynaFlex II Go is powered on, its LEDs will illuminate green, when it is powered off, the LEDs will remain unlit.
Figure 7-3 illustrates the On/Off status of the LEDs.
Figure 7-3 - LED ON/OFF
3.
BCR Status
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 25 of 62 (D998200595-120)
DynaFlex II Go devices equipped with a bar code reader have a status LED that indicates whether the barcode feature is scanning.
Figure 7-4 - BCR Status LED
4.
Beeper Alert
All DynaFlex II Go devices are equipped with a beeper that produces a short beep lasting for half a second and a long beep that lasts for one second.
7.2 Power On via USB Cable LED Behavior
DynaFlex II Go will power on immediately when connected to USB power. A brief beep will sound, and all four LEDs will turn on for half a second, as shown in Figure 7-5. Following this, LED 1 and LED 2 will remain illuminated, while LED 3 and LED 4 will remain unlit.
Figure 7-5 – LED Power on Sequence – USB Power On
7.3 USB Enumeration
When DynaFlex II Go is connected via USB in an idle state, it can be detected by a host through the USB HID port see Figure 7-6. After the host has connected to DynaFlex II Go, LED 1 will stay on. The device is in Ready State.
BCR Status Light ON
BCR Status Light OFF
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 26 of 62 (D998200595-120)
Figure 7-6 - LED Status (Idle State) Before Host Detection and LED Status (USB Ready State) After Connecting to Host
7.4 About the Status LEDs
DynaFlex II Go provides four LEDs (see section 7.1 Component Details), numbered LED1 through LED4, which report the device’s current operating status.
•
The meaning of each LED depends on the device’s operating mode, see section 6 Operation. Most of the time, operators will check the device’s status using the LEDs when it is in Active Mode while the device is not performing a transaction.
•
LED blinking patterns have specific meanings as described in Table 7-. A blinking LED generally means the device is actively doing something to change the state that the LED is indicating, and solid indicates a persistent state that would require an operator or cardholder to take action to change. One major exception is a device-wide functional failure state, such as a tamper state, where all LEDs flash urgently to call the attention of an advanced operator to intervene.
In this manual, specific blinking patterns are described in more detail in the sections where they are relevant. For example, information about how the LEDs show the device’s connection status is in section 4.3 Connecting DynaFlex II Go to a Host.
Table 7-1 - DynaFlex II Go LED Allocation In This Context LED1 LED2 LED3 LED4 Active Mode, not armed for a tap transaction
Power
Connection
Reserved
Card Read Result Active Mode, armed for a tap transaction
Armed for Tap
Tap Read Progress
Tap Read Progress
Card Read Result Device-wide failure
During major failures (such as tamper), LED1-LED4 report the nature of the failure based on the most likely steps required to resolve it.
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 27 of 62 (D998200595-120)
Table 7-2 - DynaFlex II Go LED Patterns Color Means
Solid
Solid LEDs generally require an operator or cardholder to take action to change the state the LED is reporting.
Example: Host is connected. Cardholder or host would have to disconnect.
Example: Host is disconnected. Host would have to initiate connection.
Blinking
Blinking LEDs generally indicate the device is in the process of doing / attempting something. Blink duty cycle and blink period are generally selected to show urgency or ongoing progress through a series of steps.
Example: Device is attempting to pair with the host via Bluetooth® Low Energy (LE).
Short time
LEDs sometimes light for a short time to indicate some process has ended (success or failure) and the device is going to transition to another state soon.
Example: Successful card read.
7.5 Bluetooth® Low Energy (LE) LED Behavior
7.5.1 Bluetooth® Low Energy (LE) Status LED 2 and LED 3
LED 2 is designated for indicating Bluetooth® connection status, not USB connection status.
•
When LED 2 is off, it indicates that the device is not currently connected via Bluetooth®. In most cases, this implies that the device has a Bluetooth® signal that is not connected, unless this has been intentionally disabled through configuration.
•
When LED 2 is on, it indicates that the device is currently connected via Bluetooth®.
LED 3 is designated for indicating readiness for Bluetooth® message exchange.
•
When LED 3 is off, it indicates that the Bluetooth® connection is not yet ready. This could be due to the absence of a secure connection or the non-activation of device-to-host characteristic notifications.
•
When LED 3 is on, it indicates that the Bluetooth® connection is ready, signaling the establishment of a secure connection and the activation of device-to-host characteristic notifications.
7.5.2 Power On DynaFlex II Go in Battery Operating Mode
Press and hold the Power Button for two seconds: initially, LED 4 will light up, followed by all four LEDs illuminating for one second. This is followed by LEDs 1 and 2 remaining lit for 2 seconds, after which only LED 1 will be active.
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 28 of 62 (D998200595-120)
Figure 7-7 - Power On in Battery Operating Mode
Figure 7-8 - LED Behavior for Bluetooth® Low Energy (LE) Ready State
If the host is within the Bluetooth® Low Energy (LE) connection range, all three LEDs (LED 1, 2, 3) will be illuminated, as described in Figure 7-8 - LED Behavior for Bluetooth® Low Energy (LE) Ready State .
7.5.3 Power Off DynaFlex II Go in Battery Operating Mode
DynaFlex II Go is capable of being powered off while in Battery Operating Mode only. To initiate the power-off sequence, press and hold the Power Button for two beeps then release. It's important to note that DynaFlex II Go cannot be powered off while connected via USB. If a two-beep sequence is initiated while connected to USB the device will reboot.
Figure 7-9 - Power Off Device in Battery Operating Mode
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 29 of 62 (D998200595-120)
7.5.4 DynaFlex II Go Bluetooth® Low Energy (LE) Host Pairing
DynaFlex II Go must first be paired with the host device before a secure Bluetooth® connection can be established. Follow the steps below to activate Bluetooth® pairing mode:
1.
Press and Hold the Power Button for 4 beeps
2.
Release the Power Button
3.
LED 1 will remain steadily illuminated while LED 4 will begin to blink. When LED 4 is blinking it indicates the device is waiting to pair with the host. It will continue to blink for 3 minutes, waiting to pair with the host.
Figure 7-10 - Activate BLE Pairing Mode
4.
When the host is pairing with DynaFlex II GO, LED 4 will remain off and LED 2 will power on, indicating the pair is processing.
Figure 7-11 - Bluetooth® LE Pair Processing
5.
The device will return to Power On status if pairing Succeeds or Fails. LED 2 will power off and LED 1 will remain powered on.
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 30 of 62 (D998200595-120)
Figure 7-12 - Pairing Successful/Failed
7.5.5 DynaFlex II Go Bluetooth® Low Energy (LE) Host Connected
When the device establishes a connection to the host via BLE and is prepared for secure communication, all three LEDs (LED 1, 2, 3) will illuminate steadily.
Figure 7-13 - BLE Connected to Host
7.5.6 DynaFlex II Go Bluetooth® Low Energy (LE) Host Disconnect
When the device is disconnected from the host Bluetooth® Low Energy (LE) connection, LED 3 will power off first and after 4 seconds, LED 2 will power off, LED 1 will remain powered on as the device returns to Ready State.
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 31 of 62 (D998200595-120)
Figure 7-14 - Bluetooth® LE Disconnect LED Sequence
7.5.7 DynaFlex II Go Bluetooth® Low Energy (LE) Sleep Mode
When in Bluetooth® LE Sleep Mode, DynaFlex II Go will conserve battery life by limiting power to non-essential hardware features and entering low power mode. When in Sleep Mode, the device will appear to be powered off, with no LEDs illuminated, see Figure 7-15 – Bluetooth® (LE) Sleep Mode. For information on how to disable this feature, see D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS).
Figure 7-15 – Bluetooth® (LE) Sleep Mode
7.6 LED Behavior: Successful Transactions
7.6.1 BCR Payment Transaction Successful (Connected via USB)
When the operator presses the Start button on the host device, LED 1,2, and the BCR status light will be illuminated see Figure 7-16. When a barcode is detected, only LED 1 will remain illuminated, the BCR status LED will be off, and a long beep will sound see Figure 7-17.
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 32 of 62 (D998200595-120)
Figure 7-16 – BCR Transaction USB Ready State
Figure 7-17 – BCR Transaction Barcode Detected (Connected via USB)
7.6.2 MSR Payment Transaction Successful (Connected via USB)
When the operator presses the Start transaction button on the host device, LED 1 and 2 will remain on. When a card is swiped, all four LEDs will turn on in sequence (1,2,3 then 4), followed by a long beep, indicating a successful transaction, see Figure 7-18. After a successful transaction, the device will return to the ready state, see Figure 7-19.
Figure 7-18 – LED Sequence – Payment Transaction Successful MSR Swipe (Connected via USB)
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 33 of 62 (D998200595-120)
Figure 7-19 – Return to Ready State After Successful Transaction
7.6.3 EMV Contact Payment Transaction Successful (Connected via USB)
When the operator presses the Start transaction button on the host device, LED 1 and 2 will remain on. When a card is inserted, LEDs 1, 2 and 4 will turn on in sequence, followed by a long beep, indicating a successful transaction, see Figure 7-20 – LED Sequence – Payment Transaction Successful EMV Contact (Connected via USB). LED 4 will remain on, and the device will sound a double beep until the card is removed from the slot. After a successful transaction, the device will return to the ready state, see Figure 7-19.
Figure 7-20 – LED Sequence – Payment Transaction Successful EMV Contact (Connected via USB)
7.6.4 EMV Contactless Payment Transaction Successful (Connected via USB)
When the operator presses the Start transaction button on the host device, LED 1 will remain on. When a card is presented within range of the contactless reader, LEDs 1,2,3, and 4 will turn on in sequence, followed by a long beep, indicating a successful transaction, see Figure 7-21 - LED Sequence – Payment Transaction Successful EMV Contactless (Connected via USB). After a successful transaction, the device will return to the ready state, see Figure 7-19.
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 34 of 62 (D998200595-120)
Figure 7-21 - LED Sequence – Payment Transaction Successful EMV Contactless (Connected via USB)
7.6.5 BCR Payment Transaction Successful (Connected via Bluetooth® LE)
When the operator presses the Start button on the host device, LED 1,2, and the BCR status light will be illuminated see Figure 7-22. When a barcode is detected, only LED 1 will remain illuminated, the BCR status LED will be off, and a long beep will sound see Figure 7-23.
Figure 7-22 – BCR Transaction Bluetooth® LE Ready State
Figure 7-23 – BCR Transaction Barcode Detected (Connected via Bluetooth® LE)
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 35 of 62 (D998200595-120)
7.6.6 MSR Payment Transaction Successful (Connected via Bluetooth® LE)
When the operator presses the Start transaction button on the host device, LED 1 and 2 will remain on. When a card is swiped, all four LEDs will turn on in sequence 1,2,3 then 4, followed by a long beep, indicating a successful transaction, see Figure 7-24. After a successful transaction, the device will return to the ready state, see Figure 7-25.
Figure 7-24 – LED Sequence – Payment Transaction Successful MSR Swipe (Connected via Bluetooth® LE)
Figure 7-25 – Return to Ready State After Successful Transaction (Bluetooth® LE Ready State)
7.6.7 EMV Contact Payment Transaction Successful (Connected via Bluetooth® LE)
When the operator presses the Start transaction button on the host device, LED 1 and 2 will remain on. When a card is inserted, LEDs 1,2 and 4 will turn on in sequence, followed by a long beep, indicating a successful transaction, see Figure 7-26 - LED Sequence – Payment Transaction Successful EMV Contact (Connected via Bluetooth® LE). LED 4 will remain on and the device will sound a double beep until the card is removed from the slot. After a successful transaction, the device will return to the ready state, see Figure 7-25.
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 36 of 62 (D998200595-120)
Figure 7-26 - LED Sequence – Payment Transaction Successful EMV Contact (Connected via Bluetooth® LE)
7.6.8 EMV Contactless Payment Transaction Successful (Connected via Bluetooth® LE)
When the operator presses the Start transaction button on the host device, LED 1 will remain on from ready state. When a card is presented within range of the contactless reader, LEDs 1,2,3, and 4 will turn on in sequence, followed by a long beep, indicating a successful transaction, see Figure 7-27. After a successful transaction, the device will return to the ready state, see Figure 7-25.
Figure 7-27 - LED Sequence – Payment Transaction Successful EMV Contactless (Connected via Bluetooth® LE)
7.7 LED Behavior: Errors, Timeouts, and Canceled Transactions
Table 7-3 - LED Behavior for Errors, Timeouts, and Canceled Transactions, contains LED behavior related to errors, timeouts, and canceled transactions. If the device is exhibiting LED behavior not previously mentioned, it may be contained in this section.
Table 7-2 - LED and BCR Indicator Light ON/OFF State ON/OFF State LED
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 37 of 62 (D998200595-120)
ON/OFF State BCR Indicator Light
Table 7-3 - LED Behavior for Errors, Timeouts, and Canceled Transactions Device Model Error LED Behavior Timeout LED Behavior Cancel LED Behavior
DynaFlex II Go BCR
Connected via USB
LED 1,2 ON – BCR ON
> LED1,2 ON, BCR OFF + Double Beeps
> Ready
LED1,2,3 OFF – LED 4 BCR ON + Double Beeps
LED 1,2 ON – BCR ON
> LED1,2 ON – BCR OFF + Double Beeps
> Ready
DynaFlex II Go BCR
Connected via Bluetooth® LE
LED 1,2 ON – BCR ON
> LED1,2 ON, BCR OFF + Double Beeps
> Ready
LED1,2,3 OFF – LED 4 BCR ON + Double Beeps
LED 1,2 ON - BCR ON
> LED1,2 ON - BCR OFF + Double Beeps
> Ready
DynaFlex II Go MSR
Connected via USB
LED 1,2 ON
> LED1,2,3 OFF – LED 4 ON + Double beeps
LED1,2,3 OFF – LED4 ON + Double beeps
LED 1,2 ON
> LED1,2 ON + Double Beeps
> Ready
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 38 of 62 (D998200595-120)
Device Model Error LED Behavior Timeout LED Behavior Cancel LED Behavior
DynaFlex II Go MSR
Connected via Bluetooth® LE
LED 1,2 ON
> LED1,2,3 OFF – LED 4 ON + Double beeps
LED1,2,3 OFF – LED 4 ON + Double beeps
LED 1,2 ON
> LED1,2 ON + Double Beeps
> Ready
DynaFlex II Go EMV Contact
Connected via USB
LED 1,2 ON
> LED1,2,3 OFF – LED 4 ON + Double beeps
LED 1,2,3 OFF – LED 4 ON + Double Beeps
LED 1 ON
> LED1 ON + Double Beeps
> Ready
DynaFlex II Go EMV Contact
Connected via Bluetooth® LE
LED 1,2 ON
> LED1,2,3 OFF – LED 4 ON + Double Beeps
LED 1,2,3 OFF – LED 4 ON + Double Beeps
LED 1,2 ON
> LED1,2 ON + Double Beeps
> Ready
DynaFlex II Go EMV Contactless
Connected via USB
LED 1 ON
> LED1,2,3 OFF – LED 4 ON + Double beeps
LED 1,2,3 OFF – LED4 ON + Double beeps
LED 1 ON
> LED1 ON + Double Beeps
> Ready
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 39 of 62 (D998200595-120)
Device Model Error LED Behavior Timeout LED Behavior Cancel LED Behavior
DynaFlex II Go EMV Contactless
Connected via Bluetooth® LE
LED 1 ON
> LED1,2,3 OFF – LED 4 ON + Double Beeps
LED 1,2,3 OFF – LED4 ON + Double Beeps
LED 1 ON
> LED1 ON + Double Beeps
> Ready
7.8 Power Management
7.8.1 About Power
With a sufficiently charged battery, the device will power on when the power button is pressed (see Figure 6-1 - Power Button). The device will also power on when connected to USB power. In USB mode the device will remain in full power mode to provide power to device. If a power-off sequence is initiated, the device will reboot and remain in full power mode.
7.8.2 How to Charge the Battery
Per UL requirements, the device is designed to not recharge its internal battery when the external temperature is below 0°C or above 40°C.
DynaFlex II Go products have an optional rechargeable battery to supply their own power when they are not powered through the USB-C port. The battery must be periodically recharged by connecting the device to a USB port or stand-alone USB charger. The device requires a USB power supply that can provide at least 500mA @ 5V.
To charge the device, connect it to a USB-C charger or a USB host as described in section 4.3.1 How to Connect DynaFlex II Go to a Host Computer via USB-C. For best results, use the cable that is included with the device. When charging, make sure the device is receiving enough power from the USB connection (the battery level should increase even when the device is in use). A full recharge cycle for a completely drained battery depends on the charging method. From a host USB port at 500mA, full charge takes approximately 5 hours. From a dedicated wall charger, a full charge may take approximately 5 hours. After connecting the device to a power source, make sure the LEDs indicate the device is charging (see sec 4.3.1 How to Connect DynaFlex II Go to a Host Computer via USB-C)
For important information about the device’s power systems, optimal charging methods during regular use, optimal handling and storage, and other information about keeping the device’s power systems in the best possible condition, see section 3.2 Handling to Avoid Accidental Tamper and section 7.8.1 About Power.
7.8.3 How to Power On / Wake Up from Standby Mode / Power Off
To power on the device connect the device to USB power. To power off the device, disconnect the device from USB power. Press and hold the power button (see Figure 6-1 - Power Button) on the device (for two beeps), all LED indicators should power off and remain unlit. If all LEDs are off, the device is in Powered Off mode. It is important to note the device cannot be powered off when connected via USB.
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 40 of 62 (D998200595-120)
7.8.4 About Maintenance Reset
DynaFlex II Go will automatically reset once every 24 hours if it is continuously powered on.
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 41 of 62 (D998200595-120)
7.9 Card Reading
7.9.1 About Reading Cards
The steps for starting a transaction and reading a contactless payment device are different depending on the device’s configuration and on the design of the host software. Host software developers should see section 9 Developing Custom Software for implementation references. The solution developer should provide solution-specific instructions for operators to follow. A transaction generally follows this essential flow:
1)
An advanced operator has already made sure DynaFlex II Go is configured properly and is connected to the host (see section 4.3 Connecting DynaFlex II Go to a Host). When the device is connected to the host and powered via the USB-C connector or internal rechargeable battery, the host software may keep a connection open to the device.
2)
The operator makes sure DynaFlex II Go is receiving power either from the USB connection, or from the internal rechargeable battery, and is awake and powered on (see section 7.8.3)
3)
The operator uses the host software’s user interface (for example, a point of sale) to finalize a transaction amount, then initiates a transaction. In solutions that are designed to respond to cardholder input events that occur when the device is idle, such as unprompted tapping of a card or electronic payment device, the host software may respond to those inputs by notifying the host. The host software may trigger other operations without being initiated by an operator (for example, the host software may immediately start a transaction, or alert the cardholder or operator to take action).
4)
The host communicates with the device, and reports to the operator when the device is ready.
5)
The operator guides and assists the cardholder in presenting payment.
6)
The cardholder interacts with the device to present payment. The following sections provide additional details about presenting each of the available payment methods.
7)
The host monitors the progress of the transaction, and when necessary, and should report issues to the operator, who may need to relay the messages to the cardholder.
8)
The device reports the success or failure of the transaction to the cardholder and to the host.
7.9.2 How to Tap Contactless Cards / Devices
To tap a contactless card or smartphone, follow these steps:
1)
Check LED status:
a)
The device shows the transaction status using the LEDs. LED1 lights solid and all other LEDs are off, per EMV standards, to indicate it is ready for a tap.
b)
All devices report detailed transaction status to the host, and host software may report that information to operators so they can guide cardholders through the transaction (for example, “please tap your card now”).
2)
If the cardholder is using an electronic payment device, such as a smartphone, make sure the payment device has NFC turned On and has a payment app configured to process transactions. For details, see the documentation provided by the smartphone manufacturer and payment app publisher.
3)
Briefly hold the card, smartphone, or other contactless payment device over the contactless landing zone, indicated by the EMVCo Contactless Indicator symbol on the device’s face (see Figure 7-28). Because each smartphone model may have its NFC antenna placed differently, the ideal tap position may vary by make and model. For example, Samsung users may need to center the phone on the contactless landing zone, while Apple users may need to tap the top of the phone on the contactless landing zone.
4)
Wait for LED status:
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 42 of 62 (D998200595-120)
a)
The device quickly lights the second LED to show it is processing, then lights the third LED to show it has successfully read the tap, then lights the fourth LED to show the read is complete (see Figure 7-29) The device then returns to Ready State, when connected to USB ready state is LED 1 and 2 on only, ready state for BLE is LED 1,2, and 3 on.
b)
The device beeps once.
c)
If the transaction requires a signature, the device sends a notification message to the host that includes the status Signature Capture Requested. In this case, the solution design collects the cardholder’s signature manually or via a different method.
d)
The device ends the transaction and reports the transaction status to the host.
5)
If the device cannot communicate with the card, smartphone, or other contactless payment device:
a)
The device ends the transaction.
b)
The device lights LED 4 for a short time.
c)
The device beeps twice.
d)
The device notifies the host that the transaction failed. If this occurs, the host software may choose to retry the transaction or revert to prompting the operator to perform another operation that is specific to the solution design.
Figure 7-28 - Tapping a Contactless Card / Smartphone
Figure 7-29 – Contactless Read LED Sequence – Read Complete (Connected via Bluetooth® LE)
7.9.3 How to Scan Barcodes
To scan a barcode, follow these steps:
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 43 of 62 (D998200595-120)
1)
Make sure you are using a DynaFlex II Go model that includes a barcode reader, indicated by QR Code markings on the face of the device surrounding the barcode reader lens (see section 1.1 Key Features and Components).
2)
If the barcode being scanned is not on a self-illuminated source such as a smartphone, make sure there is enough ambient light for the camera to read the barcode. In low light conditions, the barcode reader will only be able to read self-illuminated sources.
3)
In some solutions, the operator may have to perform an operation in the host software to enable the barcode reader, or to start a transaction with the barcode reader enabled.
4)
Wait for the device, the host, or the operator to prompt for a barcode read:
a)
The device lights the barcode reader indicator LED next to the barcode reader lens.
5)
Hold the barcode in front of the barcode reader camera:
a)
If possible, use the light from the barcode reader indicator LED to align the barcode within the barcode reader’s field of view, which extends 16 degrees above / below and 21 degrees to the left / right of a line perpendicular to the barcode reader lens.
b)
Hold the barcode as close as 6 inches from the lens. For smaller barcodes, the device will read immediately. If it does not, gradually move away up to 14 inches from the lens until the device reports a successful read. Larger barcodes must be far enough away from the device that the whole barcode is within the camera’s field of view; if a large barcode is too close, the barcode reader can only see a zoomed in portion of the barcode.
c)
Do not tilt the barcode more than 60 degrees from parallel to the device’s face.
6)
Wait for the device or the host to report the barcode has been read successfully:
a)
The device beeps once.
b)
The device turns off the barcode reader indicator LED.
Figure 7-30 - Scanning a Barcode
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 44 of 62 (D998200595-120)
7.9.4 Apple VAS for DynaFlex II Go
DynaFlex II Go products support Apple Value Added Services (Apple VAS) protocol.
Contactless transactions using the Apple VAS protocol permits the device reader to perform the following supported operations:
7.9.4.1 VAS App and Payment Mode (Dual Mode)
The device reads both Apple VAS data and EMV payment data from a tapped smartphone or reads EMV payment data from a tapped card. When device sends ARQC to the host to conclude the transaction, it includes EMV payment data in container FC and includes VAS data, if available, in container FE
7.9.4.2 VAS App Only Mode (VAS Mode)
The device reads only Apple VAS data from a tapped smartphone and does not read data from a tapped card. If the tapped smartphone does not support VAS, the device does not detect or read from the smartphone. When the device sends ARQC to conclude the transaction, it includes VAS data in container FE and does not include EMV payment data in container FC.
7.9.4.3 VAS App or Payment Mode (Single Mode)
The device reads only Apple VAS data from a tapped smartphone or reads EMV payment data from a tapped card. When the device sends ARQC to conclude the transaction, it only includes either EMV payment data in container FC for cards, or includes VAS data in container for smartphones.
7.9.4.4 Payment Only Mode (Payment Mode)
The device operates the same as EMV mode (01). It reads only EMV payment data from a tapped smartphone or a tapped card. When the device sends ARQC to conclude the transaction, it includes EMV payment data in container FC and does not include VAS data in container FE. Note: THIS MODE MAY NOT BE NEEDED.
For details, see D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS).
7 - Introduction to User Interface
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 45 of 62 (D998200595-120)
7.9.5 How to Tap NFC Contactless IC Products and Send Pass-through Commands
DynaFlex II Go is compatible with near field communication (NFC) technology such as MIFARE®, MIFARE Classic ®, and MIFARE® DESFire® Light contactless IC products (smart cards).
To tap an NFC Contactless IC product and send pass-through commands, follow these steps:
1)
Check LED status:
a)
Per EMV standards, the device indicates transaction status through its LED indicators, located on the front face of the device. When ready for a tap, LED 1 is steadily illuminated while all other LEDs remain unlit.
b)
All devices communicate transaction details to the host. The host software will relay this information to operators, allowing them to direct cardholders during the transaction, such as prompting "please tap your card now".
2)
Place the card over the device's designated contactless landing zone, marked by the EMVCo Contactless Indicator symbol on the front face of the device.
3)
Wait for LED status:
a)
Initially, LED 2 illuminates, signaling the device is processing. The device subsequently illuminates LED 3 and LED 4, indicating card detection. Notifications are then sent to identify the card type and UID.
b)
The Host application can further interact with the NFC Tag using pass-through commands. For details, see D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS).
c)
If the pass-through command is the last successful command, the device will end the transaction, emitting a single beep signaling a successful transaction. The user then needs to remove the card.
d)
If an error is detected, the device will end the transaction and emit two beeps to signal the error. The user then needs to remove the card.
4)
The device notifies the host that the transaction has ended with the NFC Tag removed.
8 - Maintenance
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 46 of 62 (D998200595-120)
8 Maintenance
8.1 Mechanical Maintenance
DO NOT use liquid cleaning products or insert any other objects into the device.
DO NOT apply any liquid directly onto the device, to avoid seepage into the electronics.
Periodic cleaning of the device’s exterior may be required. To clean the outside of DynaFlex II Go products, wipe down the device with a soft, slightly damp cloth and then wipe dry with a lint-free cloth. The graphic overlay on the face of the device can also be cleaned using a slightly damp specialty cleaning cloth, like those used to wipe lenses, monitors, and smartphone displays.
8.2 Updates to Firmware, Documentation, Security Guidance
In addition to the security guidance in the product manuals, MagTek may provide updates to this document, as well as supplemental security guidance or notices regarding vulnerabilities, at www.magtek.com. MagTek advises checking the product’s home page periodically for the most up-to-date information.
Any firmware updates addressing product features, bugs, or security vulnerabilities are also posted to www.magtek.com or may be sent directly to affected customers. To update the device’s firmware:
1)
Obtain the firmware image to install from your MagTek representative.
2)
Download 1000007406 DynaFlex, DynaProx Test Utility from the MagTek web site.
3)
Follow the instructions in D998200402 DynaFlex, DynaProx Utility User Manual (Windows) included in the firmware update utility’s Docs subfolder.
9 - Developing Custom Software
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 47 of 62 (D998200595-120)
9 Developing Custom Software
Custom host software uses the same underlying device command set for all DynaFlex II Go product connection types. This section provides high-level information about communicating with the device via the various physical connection types in various software development frameworks, and provides pointers to available SDKs, which include sample code. Product documentation and SDKs are available for download by searching for the product name on www.magtek.com and navigating to the Support tab.
MagTek provides convenient SDKs and corresponding documentation for many programming languages and operating systems. The API libraries included in the SDKs wrap the details of the connection in an interface that conceptually parallels the device’s internal operation, freeing software developers to focus on the business logic, without having to deal with the complexities of platform APIs for connecting to the various available connection types, communicating using the various available protocols, and parsing the various available data formats. Information about using MagTek wrapper APIs is available in separate documentation, including:
•
D998200380 MagTek Universal SDK Programmer’s Manual (Microsoft .NET)
•
D998200381 MagTek Universal SDK Programmer’s Manual (Microsoft C++ )
•
D998200385 MagTek Universal SDK for MMS Devices Programmer’s Manual (Java)
•
D998200386 MagTek Universal SDK for MMS Devices Programmer’s Manual (iOS)
•
D998200387 MagTek Universal SDK Programmer’s Manual (Android)
The documentation is bundled with the SDKs themselves, which include:
•
1000007351 MagTek Universal SDK for MMS Devices (Windows)
•
1000007352 MagTek Universal SDK for MMS Devices (Android)
The SDKs and corresponding documentation include:
•
Functions for sending the direct commands described in this manual
•
Wrappers for commonly used commands that further simplify development
•
Sample source code to demonstrate how to communicate with the device using the direct commands described in this manual
To download the SDKs and documentation, search www.magtek.com for “SDK” and select the SDK and documentation for the programming languages and platforms you need or contact MagTek Support Services for assistance.
In addition to the SDK API libraries, software developers also have the option to revert to direct communication with the device using libraries using the operating system’s native USB and serial port libraries. For example, custom software written in Visual Basic or Visual C++ may make API calls to the standard Windows USB HID driver. For more information about sending commands directly, see D998200597 DynaFlex II Go Programmer’s Manual (COMMANDS).
For more information about developing custom applications that integrate with DynaFlex II Go, see the MagTek web site or contact your reseller or MagTek Support Services.
Appendix A - Technical Specifications
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 48 of 62 (D998200595-120)
Appendix A Technical Specifications DynaFlex II Go Products Technical Specifications Reference Standards and Certifications
ISO 7810, ISO 7811, AAMVA
ISO/IEC 7816-1, 2, 3, & 4 Identification Cards Integrated Circuits with Contacts
EMV ICC Specifications for Payment Systems Version 4.3d, L1 Contact and Version 4.4a, L2 Contact
EMV Contactless Level 1 Version 3.1a
MasterCard TQM
MCL v3.1.4, payWave v2.2c, Expresspay 4.1, D-PAS Terminal Payment Application v2.0
PCI PTS POI v6.2 SCR
DUKPT TDES, AES 128 DUKPT
FCC Part 15 Low Power Transceiver, RX verified per FCC Title 47 Part 15 Subclass C
UL/CSA/IEC 62368-1, 2nd edition
CE Certified
CE Safety: IEC 62368-1: 2014
Canada ISED Certified
AS/NZS CISPR 32 (2013), AS/NZS 4268 Table 1, Row 59 DTS 2400-2483MHz SRD (802.11), and AS/NZS 4268 (2017) Table 1, Row 43 13.553-13.567MHz (contactless reader)
RoHS Compliant the Electrical and Electronic Equipment (EEE) Reduction of Hazardous Substances (RoHS) European Directive 2002/95/EC
California Proposition 65 (California)
IPC-A-610 Class II Assembly
EU Directive Waste Electrical and Electronic Equipment (WEEE)
EU Directive Restriction of Hazardous Substances (RoHS)
Universal Serial Bus Specifications 1.1, 2.0
AES-128 and AES-256 Encryption
Apple VAS
iAP2® Protocol Support
Bluetooth® Core Specification 5.2 Physical Characteristics
Dimensions (L x W x H):
2.76 in. x 2.57 in. x .79 in. (70.10mm x 65.3mm x20.1mm)
Weight
DynaFlex II Go = 3.17 oz. (90g)
DynaFlex II Go BCR = 3.24 oz. (92g)
Supported Mounting Options:
Mounting to host via external clip or embedded lanyard Reader Characteristics
Magnetic Stripe Reader:
Three track bidirectional encrypting reader with MagnePrint
Magnetic Stripe Decoding:
Financial (ISO Type B), AAMVA, or Other
Magnetic Swipe Speeds:
6 inches per second to 60 inches per second
EMV Contact Reader:
EMVCo L1 and L2 Contact Reader
Appendix A - Technical Specifications
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 49 of 62 (D998200595-120)
DynaFlex II Go Products Technical Specifications
EMV Contactless Reader:
EMVCo L1 and L2 Contactless Reader
D-PAS, PayPass/MCL, payWave, Expresspay
Mobile wallets including but not limited to Apple Pay, Google Pay, Samsung Pay
Barcode Reader:
Barcode Media: Labels, paper, smartphone / computer displays
Barcode Types: QR Codes, Linear Barcodes, UPC-A, UPC-E, Code 128, PDF417 / Data Matrix, Aztec, etc.
Field Of View 31.5° total vertical sweep, 42° total horizontal sweep, perpendicular to device face
Depth Of Field 1.2 in. (30mm) to 13.8 in. (350mm)
Integrated white indicator LED User Interface Characteristics
Status Indicators:
4 Monochrome Green LEDs
1 Integrated white indicator LED for BCR
Display Type:
Not Applicable
Keypad:
Not Applicable Security Characteristics
Certifications:
PCI PTS POI v6.2 Certified Secure Card Reader (SCR)
Tamper Protection:
The enclosure and associated electronics form a Tamper Resistant Security Module (TRSM) where attempts to penetrate or modify the unit cause all cryptographic keys to be cleared or rendered unusable. Electrical Characteristics
Power Inputs:
USB powered via USB-C receptacle
Power Outputs:
None
Rechargeable Battery Type:
Lithium-Ion Polymer (LiPo)
Voltage Requirements:
5 VDC
Current Requirements:
500 mA Maximum
Data Storage:
Not Applicable Communication Characteristics
Wired Connection Types:
USB-C, compatible with USB 1.1, USB 2.0, USB 3.0 preferred
Vendor-defined USB Human Interface Device (HID) data format
Wireless Connection Types:
None
RF Exposure:
SAR Certified Software Characteristics
Appendix A - Technical Specifications
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 50 of 62 (D998200595-120)
DynaFlex II Go Products Technical Specifications
Tested Operating System(s):
USB Hosts: Windows 11 Environmental Resistance
Ingress Protection:
IP30
Operating Temperature:
DynaFlex II Go/DynaFlex II Go BCR: 32°F to 95°F (0°C to 35°C)
Operating Relative Humidity:
5% to 90% RH non-condensing
Storage Temperature:
DynaFlex II Go/DynaFlex II Go BCR: -4°F to 113°F (-20°C to 45°C)
Storage Relative Humidity:
5% to 90% RH non-condensing
Vibration Resistance:
None
Shock Resistance:
None
ESD Tolerance (EMVCo):
±12.0 kV air discharge / 5 different paddles
ESD Tolerance (FCC/CE):
±8kV air discharge / ±4kV contact discharge
Vapor Resistance:
None Reliability
Shelf Life:
60 Months Minimum
Magnetic Read Head Life:
500k Swipes
Battery Shelf Life:
5 years or longer (backup battery)
Battery Cycle Life:
NA
Appendix B - Barcode Reader Symbologies
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 51 of 62 (D998200595-120)
Appendix B Barcode Reader Symbologies
Barcode symbology refers to the way in which data is encoded in a barcode. It uses either spaced lines, dots, or squares. When read, these symbols are decoded and converted to data. The table below lists all of the supported symbologies and which are enabled by default.
Table 9-1 - Barcode Reader Supported Symbologies Symbology Default AIM 128
Disabled Aztec
Enabled Codabar
Enabled Code 11
Disabled Code128
Enabled Code 32
Disabled Code 39
Enabled Code 93
Disabled Data Matrix
Enabled EAN-8
Enabled EAN-13
Enabled Febraban
Disabled GSI-128 (UCC/EAN-128)
Enabled GS1 Databar (RSS)
Disabled Industrial 25
Disable Interleaved 2 of 5,
Enabled ISSN
Disabled ISBN
Disabled ITF-14
Disabled ITF-6
Disabled Matrix 2 of 5
Enabled Micro QR
Disabled MSI Plessey
Disabled PDF417
Enabled Plessey
Disabled QR Code
Enabled Standard 25
Disabled UPC-E
Enabled UPC-A
Enabled
Appendix C - Optional Accessories
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 52 of 62 (D998200595-120)
Appendix C Optional Accessories
Tailored for use with mobile handsets, tablets, and desktop computers, DynaFlex II Go offers a variety of accessories designed to meet a wide range of operational needs.
Part Number Description 21078408 DYNAFLEX II GO, KIT COUNTERTOP STAND
The Countertop Stand is well-suited for countertop placement or battery charging, providing a convenient and secure means of positioning the device.
Appendix C - Optional Accessories
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 53 of 62 (D998200595-120)
Part Number Description 21078409 DYNAFLEX II GO ADAPTOR FOR OTTERBOX Users can take advantage of the OtterBox® uniVERSE® adaptor for easy sliding and connection to a wide range of mobile devices, including phones and tablets.
Appendix C - Optional Accessories
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 54 of 62 (D998200595-120)
Part Number Description 21078410 DYNAFLEX II GO RUBBER SLEEVE DynaFlex II Go can be equipped with a full-rubber sleeve specifically engineered to enhance the device's ingress protection.
Appendix C - Optional Accessories
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 55 of 62 (D998200595-120)
Part Number Description 21078411 DYNAFLEX II GO RUBBER SLEEVE HALF SIZE
DynaFlex II Go offers the option to install a half-rubber sleeve, intended to boost the device's ingress protection when utilizing the OtterBox® uniVERSE® adaptor for DynaFlex II Go.
Appendix D - Warranty, Standards, and Certifications
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 56 of 62 (D998200595-120)
Appendix D Warranty, Standards, and Certifications
LIMITED WARRANTY
MagTek warrants that the products sold pursuant to this Agreement will perform in accordance with MagTek’s published specifications. This warranty shall be provided only for a period of one year from the date of the shipment of the product from MagTek (the “Warranty Period”). This warranty shall apply only to the “Buyer” (the original purchaser, unless that entity resells the product as authorized by MagTek, in which event this warranty shall apply only to the first repurchaser).
During the Warranty Period, should this product fail to conform to MagTek’s specifications, MagTek will, at its option, repair or replace this product at no additional charge except as set forth below. Repair parts and replacement products will be furnished on an exchange basis and will be either reconditioned or new. All replaced parts and products become the property of MagTek. This limited warranty does not include service to repair damage to the product resulting from accident, disaster, unreasonable use, misuse, abuse, negligence, or modification of the product not authorized by MagTek. MagTek reserves the right to examine the alleged defective goods to determine whether the warranty is applicable.
Without limiting the generality of the foregoing, MagTek specifically disclaims any liability or warranty for goods resold in other than MagTek’s original packages, and for goods modified, altered, or treated without authorization by MagTek.
Service may be obtained by delivering the product during the warranty period to MagTek (1710 Apollo Court, Seal Beach, CA 90740). If this product is delivered by mail or by an equivalent shipping carrier, the customer agrees to insure the product or assume the risk of loss or damage in transit, to prepay shipping charges to the warranty service location, and to use the original shipping container or equivalent. MagTek will return the product, prepaid, via a three (3) day shipping service. A Return Material Authorization (“RMA”) number must accompany all returns. Buyers may obtain an RMA number by contacting MagTek Support Services at (562) 546-6800.
EACH BUYER UNDERSTANDS THAT THIS MAGTEK PRODUCT IS OFFERED AS-IS. MAGTEK MAKES NO OTHER WARRANTY, EXPRESS OR IMPLIED, AND MAGTEK DISCLAIMS ANY WARRANTY OF ANY OTHER KIND, INCLUDING ANY WARRANTY OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.
IF THIS PRODUCT DOES NOT CONFORM TO MAGTEK’S SPECIFICATIONS, THE SOLE REMEDY SHALL BE REPAIR OR REPLACEMENT AS PROVIDED ABOVE. MAGTEK’S LIABILITY, IF ANY, SHALL IN NO EVENT EXCEED THE TOTAL AMOUNT PAID TO MAGTEK UNDER THIS AGREEMENT. IN NO EVENT WILL MAGTEK BE LIABLE TO THE BUYER FOR ANY DAMAGES, INCLUDING ANY LOST PROFITS, LOST SAVINGS, OR OTHER INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF, OR INABILITY TO USE, SUCH PRODUCT, EVEN IF MAGTEK HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES, OR FOR ANY CLAIM BY ANY OTHER PARTY.
Appendix D - Warranty, Standards, and Certifications
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 57 of 62 (D998200595-120)
LIMITATION ON LIABILITY
EXCEPT AS PROVIDED IN THE SECTIONS RELATING TO MAGTEK’S LIMITED WARRANTY, MAGTEK’S LIABILITY UNDER THIS AGREEMENT IS LIMITED TO THE CONTRACT PRICE OF THIS PRODUCT.
MAGTEK MAKES NO OTHER WARRANTIES WITH RESPECT TO THE PRODUCT, EXPRESSED OR IMPLIED, EXCEPT AS MAY BE STATED IN THIS AGREEMENT, AND MAGTEK DISCLAIMS ANY IMPLIED WARRANTY, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTY OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.
MAGTEK SHALL NOT BE LIABLE FOR CONTINGENT, INCIDENTAL, OR CONSEQUENTIAL DAMAGES TO PERSONS OR PROPERTY. MAGTEK FURTHER LIMITS ITS LIABILITY OF ANY KIND WITH RESPECT TO THE PRODUCT, INCLUDING NEGLIGENCE ON ITS PART, TO THE CONTRACT PRICE FOR THE GOODS.
MAGTEK’S SOLE LIABILITY AND BUYER’S EXCLUSIVE REMEDIES ARE STATED IN THIS SECTION AND IN THE SECTION RELATING TO MAGTEK’S LIMITED WARRANTY.
Appendix D - Warranty, Standards, and Certifications
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 58 of 62 (D998200595-120)
FCC INFORMATION
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) This device must accept any interference received, including interference that may cause undesired operation.
Note: This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates, uses and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:
•
Reorient or relocate the receiving antenna.
•
Increase the separation between the equipment and receiver.
•
Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
•
Consult the dealer or an experienced radio/TV technician for help.
Caution: Changes or modifications not expressly approved by MagTek could void the user’s authority to operate this equipment.
CANADIAN DECLARATION OF CONFORMITY
This digital apparatus does not exceed the Class B limits for radio noise from digital apparatus set out in the Radio Interference Regulations of the Canadian Department of Communications.
Le présent appareil numérique n’émet pas de bruits radioélectriques dépassant les limites applicables aux appareils numériques de la classe B prescrites dans le Réglement sur le brouillage radioélectrique édicté par le ministère des Communications du Canada.
This Class B digital apparatus complies with Canadian ICES-003.
Cet appareil numérique de la classe B est conformé à la norme NMB-003 du Canada.
INDUSTRY CANADA (IC) RSS
This device complies with Industry Canada licence-exempt RSS standard(s). Operation is subject to the following two conditions: (1) This device may not cause interference, and (2) This device must accept any interference, including interference that may cause undesired operation of the device.
Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) L'appareil ne doit pas produire de brouillage, et (2) L'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.
CUR/UR
This product is recognized per Underwriter Laboratories and Canadian Underwriter Laboratories 1950.
Appendix D - Warranty, Standards, and Certifications
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 59 of 62 (D998200595-120)
CE STANDARDS
Testing for compliance with CE requirements was performed by an independent laboratory. The unit under test was found compliant with standards established for Class B devices.
EU STATEMENT
Hereby, MagTek Inc. declares that the radio equipment types Wideband Transmission System (802.11 wireless and Bluetooth® Low Energy), and Non-Specific Short Range Device (contactless) are in compliance with Directive 2014/53/EU. The full text of the EU declarations of conformity is available at the following internet addresses:
•
https://www.magtek.com/Content/DocumentationFiles/D998200296.pdf
AUSTRALIA / NEW ZEALAND STATEMENT
Testing for compliance with AS/NZS standards was performed by a registered and accredited laboratory. The unit under test was found compliant with standards established under AS/NZS CISPR 32 (2013), AS/NZS 4268 Table 1, Row 59 DTS 2400-2483MHz SRD (802.11), and AS/NZS 4268 (2017) Table 1, Row 43 13.553-13.567MHz (contactless reader).
UL/CSA
This product is recognized per UL 60950-1, 2nd Edition, 2011-12-19 (Information Technology Equipment - Safety - Part 1: General Requirements), CSA C22.2 No. 60950-1-07, 2nd Edition, 2011-12 (Information Technology Equipment - Safety - Part 1: General Requirements).
ROHS STATEMENT
When ordered as RoHS compliant, this product meets the Electrical and Electronic Equipment (EEE) Reduction of Hazardous Substances (RoHS) Directive (EU) 2015/863 amending Annex II to Directive 2011/65/EU. The marking is clearly recognizable, either as written words like “Pb-free,” “lead-free,” or as another clear symbol ().
PCI STATEMENT
PCI Security Standards Council, LLC (“PCI SSC”) has approved this PIN Transaction Security Device to be in compliance with PCI SSC’s PIN Security Requirements.
When granted, PCI SSC approval is provided by PCI SSC to ensure certain security and operational characteristics important to the achievement of PCI SSC’s goals, but PCI SSC approval does not under any circumstances include any endorsement or warranty regarding the functionality, quality or performance of any particular product or service. PCI SSC does not warrant any products or services provided by third parties. PCI SSC approval does not under any circumstances include or imply any product warranties from PCI SSC, including, without limitation, any implied warranties of merchantability, fitness for purpose, or non-infringement, all of which are expressly disclaimed by PCI SSC. All rights and remedies regarding products and services which have received PCI SSC approval shall be provided by the party providing such products or services, and not by PCI SSC.
Appendix D - Warranty, Standards, and Certifications
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 60 of 62 (D998200595-120)
SAFETY
This product has been evaluated by multiple safety certification agencies, including Underwriters Laboratories (UL) and the United States Federal Communications Commission (FCC Class A and Class B), and is designed to protect both the user and the device. This document is written specifically to work in conjunction with these safety and integrity features to protect the user and the device. It is very important to follow all steps in the product documentation carefully, in the order in which they are described, and at the recommended times. Failure to do so could result in personal injury, and / or cause damage to the device, and / or void the product warranty.
SAFETY REQUIREMENTS
Never do any of the following:
•
DO NOT use a ground adapter plug to connect equipment to a power socket-outlet that lacks a ground connection terminal.
•
DO NOT attempt any maintenance function that is not specifically described in this manual or in other ExpressCard 3000 instructional documents published by MagTek.
•
DO NOT remove any of the covers or guards that are fastened with screws. There are no user-serviceable areas within these covers.
•
DO NOT override or “cheat” electrical or mechanical interlock devices.
•
DO NOT use EC3000 supplies or cleaning materials for other than their intended purposes.
•
DO NOT operate the equipment if you or anyone else have noticed unusual noises or odors.
Consider the following before operating the ExpressCard 3000:
•
Connect the EC3000 to a properly grounded AC power socket-outlet. If in doubt, have the socket-outlet checked by a qualified electrician. Improper connection of the device’s grounding conductor creates a risk of electric shock.
•
Place the EC3000 on a solid surface that can safely support the device’s weight plus the weight of a person leaning against it (such as a service technician).
•
Be careful when moving or relocating the device. Use proper lifting techniques.
•
Use materials and supplies specifically designed for MagTek devices. Using unsuitable materials may result in poor performance, and in some cases may be hazardous.
Appendix D - Warranty, Standards, and Certifications
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 61 of 62 (D998200595-120)
SOFTWARE LICENSE AGREEMENT
IMPORTANT: YOU SHOULD CAREFULLY READ ALL THE TERMS, CONDITIONS AND RESTRICTIONS OF THIS LICENSE AGREEMENT BEFORE INSTALLING THE SOFTWARE PACKAGE. YOUR INSTALLATION OF THE SOFTWARE PACKAGE PRESUMES YOUR ACCEPTANCE OF THE TERMS, CONDITIONS, AND RESTRICTIONS CONTAINED IN THIS AGREEMENT. IF YOU DO NOT AGREE WITH THESE TERMS, CONDITIONS, AND RESTRICTIONS, PROMPTLY RETURN THE SOFTWARE PACKAGE AND ASSOCIATED DOCUMENTATION TO THE ADDRESS IN THIS DOCUMENT, ATTENTION: CUSTOMER SUPPORT.
TERMS, CONDITIONS, AND RESTRICTIONS
MagTek, Incorporated (the "Licensor") owns and has the right to distribute the described software and documentation, collectively referred to as the "Software."
LICENSE: Licensor grants you (the "Licensee") the right to use the Software in conjunction with MagTek products. LICENSEE MAY NOT COPY, MODIFY, OR TRANSFER THE SOFTWARE IN WHOLE OR IN PART EXCEPT AS EXPRESSLY PROVIDED IN THIS AGREEMENT. Licensee may not decompile, disassemble, or in any other manner attempt to reverse engineer the Software. Licensee shall not tamper with, bypass, or alter any security features of the software or attempt to do so.
TRANSFER: Licensee may not transfer the Software or license to the Software to another party without the prior written authorization of the Licensor. If Licensee transfers the Software without authorization, all rights granted under this Agreement are automatically terminated.
COPYRIGHT: The Software is copyrighted. Licensee may not copy the Software except for archival purposes or to load for execution purposes. All other copies of the Software are in violation of this Agreement.
TERM: This Agreement is in effect as long as Licensee continues the use of the Software. The Licensor also reserves the right to terminate this Agreement if Licensee fails to comply with any of the terms, conditions, or restrictions contained herein. Should Licensor terminate this Agreement due to Licensee's failure to comply, Licensee agrees to return the Software to Licensor. Receipt of returned Software by the Licensor shall mark the termination.
LIMITED WARRANTY: Licensor warrants to the Licensee that the disk(s) or other media on which the Software is recorded are free from defects in material or workmanship under normal use.
THE SOFTWARE IS PROVIDED AS IS. LICENSOR MAKES NO OTHER WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
Because of the diversity of conditions and hardware under which the Software may be used, Licensor does not warrant that the Software will meet Licensee specifications or that the operation of the Software will be uninterrupted or free of errors.
IN NO EVENT WILL LICENSOR BE LIABLE FOR ANY DAMAGES, INCLUDING ANY LOST PROFITS, LOST SAVINGS, OR OTHER INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE, OR INABILITY TO USE THE SOFTWARE. Licensee's sole remedy in the event of a defect in material or workmanship is expressly limited to replacement of the Software disk(s) if applicable.
Appendix D - Warranty, Standards, and Certifications
DynaFlex II Go| Secure Card Reader Authenticator | Installation and Operation Manual
Page 62 of 62 (D998200595-120)
GOVERNING LAW: If any provision of this Agreement is found to be unlawful, void, or unenforceable, that provision shall be removed from consideration under this Agreement and will not affect the enforceability of any of the remaining provisions. This Agreement shall be governed by the laws of the State of California and shall inure to the benefit of MagTek, Incorporated, its successors or assigns.
ACKNOWLEDGMENT: LICENSEE ACKNOWLEDGES THAT LICENSEE HAS READ THIS AGREEMENT, UNDERSTANDS ALL OF ITS TERMS, CONDITIONS, AND RESTRICTIONS, AND AGREES TO BE BOUND BY THEM. LICENSEE ALSO AGREES THAT THIS AGREEMENT SUPERSEDES ANY AND ALL VERBAL AND WRITTEN COMMUNICATIONS BETWEEN LICENSOR AND LICENSEE OR THEIR ASSIGNS RELATING TO THE SUBJECT MATTER OF THIS AGREEMENT.
QUESTIONS REGARDING THIS AGREEMENT SHOULD BE ADDRESSED IN WRITING TO MAGTEK, INCORPORATED, ATTENTION: CUSTOMER SUPPORT, AT THE ADDRESS LISTED IN THIS DOCUMENT, OR E-MAILED TO SUPPORT@MAGTEK.COM.
DEMO SOFTWARE / SAMPLE CODE: Unless otherwise stated, all demo software and sample code are to be used by Licensee for demonstration purposes only and MAY NOT BE incorporated into any production or live environment. The PIN Pad sample implementation is for software PIN Pad test purposes only and is not PCI compliant. To meet PCI compliance in production or live environments, a third-party PCI compliant component (hardware or software-based) must be used.