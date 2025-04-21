---
title: Introduction
layout: home
Parent: Developer Documentation
nav_order: 1
---



# Introduction


  
## About Connections and Data Formats

MMS products transmit data using a set of common data formats across a variety of physical connection layers, which can include universal serial bus (USB) acting as a vendor-defined HID device (“USB HID”), wireless LAN (WLAN), Bluetooth®, Bluetooth® Low Energy (“Bluetooth® LE”), RS-232, Apple Lightning, and so on. The set of available physical connection types and the data formats available on each connection type is device dependent. [Table 1.41](#table-1-41) shows the physical connection types available on each product, and the data formats supported on each connection type for that device. Details about connection types and formats can be found in section **2 Connection Types**. Section headings in this document include tags that indicate which connection types and/or data formats they apply to.

### [Table 1.41](#table-1-41) - Device Connection Types / Data Formats

| Product / Connection                                           | Bluetooth®® LE GATT | RS232 / UART | USB HID | WLAN | iAP2     | Ethernet |
|----------------------------------------------------------------|---------------------|--------------|---------|------|----------|----------|
| DynaFlex with USB Only                                         |                     |              | HID     |      |          |          |
| DynaFlex w/Bluetooth® LE (MAGTEK INTERNAL ONLY FOR NOW)        | GATT                |              | HID     |      |          |          |
| DynaFlex Pro with USB Only                                     |                     |              | HID     |      |          |          |
| DynaFlex Pro w/Bluetooth® LE (MAGTEK INTERNAL ONLY FOR NOW)    | GATT                |              | HID     |      |          |          |
| DynaFlex Pro w/WLAN                                            |                     |              | HID     | WLAN |          |          |
| DynaFlex Pro w/Ethernet (MAGTEK INTERNAL ONLY FOR NOW)         |                     |              | HID     |      |          | Ethernet |
| DynaProx                                                       |                     | SLIP         | HID     |      | iAP2-USB |          |
| DynaFlex II with USB Only                                      |                     |              | HID     |      |          |          |
| DynaFlex II w/Bluetooth® LE (MAGTEK INTERNAL ONLY FOR NOW)     | GATT                |              | HID     |      |          |          |
| DynaFlex II PED with USB Only                                  |                     |              | HID     |      |          |          |
| DynaFlex II PED w/Bluetooth® LE (MAGTEK INTERNAL ONLY FOR NOW) | GATT                |              | HID     |      |          |          |
| DynaFlex II PED w/WLAN                                         |                     |              | HID     | WLAN |          |          |
| DynaFlex II PED w/Ethernet (MAGTEK INTERNAL ONLY FOR NOW)      |                     |              | HID     |      |          | Ethernet |
| DynaFlex II Go with USB Only                                   |                     |              | HID     |      | iAP2-USB |          |
| DynaFlex II Go w/Bluetooth® LE                                 | GATT                |              | HID     |      | iAP2-USB |          |

## About Device Features

Much of the information in this document is applicable to multiple devices. When developing solutions that use a specific device or set of devices, integrators must be aware of each device’s connection types, data formats, features, and configuration options, which affect the availability and behavior of some commands. [Table 1.51](#table-1-51) provides a list of device features that may impact command availability and behavior. All section headings in this document include tags that indicate which features they apply to.

### [Table 1.51](#table-1-51) - Device Features

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
| Common Kernel           | N              | N                      | N                        | N                          | N                               | N                      | N                          | Y        | Y                         | Y                           | Y                             | Y                                  | Y                         | Y                             |
| Card Emulation          | Y              | N                      | N                        | N                          | N                               | N                      | N                          | Y        | Y                         | Y                           | Y                             | Y                                  | Y                         | Y                             |
