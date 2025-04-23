---
title: Configurations
layout: home
parent: DynaFlex Family Programmer's Manual
nav_order: 8
---
## Configuration

### About Configuration

The device provides two mechanisms for the host to retrieve information
about the device and to configure / customize device behavior:

- **Properties** are smaller configuration values (generally up to 255
  bytes and often significantly smaller). The device stores properties
  in a hierarchical tree, where each property has its own unique ID
  (sometimes referred to as an Object Identifier or OID) that identifies
  its position in the tree. The host can set and get properties using
  the commands in Command Group 0xD1nn - Settings and Information. For
  further information about OIDs, see **Appendix A Object IDs (OIDs) and
  ITU-T X660**.

<!-- -->

- **Files** are larger configuration values, which include custom
  graphics files and large configuration data blobs such as EMV terminal
  and application settings. Each file has a unique identifier more akin
  to a file path in a file system. The host can set and get files using
  the commands in **Command Group 0xD8nn - File Operations**.

This section focuses on **properties**, which the host can either read
from the device to retrieve device information (such as its PCI hardware
ID, serial number, firmware revision numbers, etc.), or write to the
device to change device behavior, or to store values for future
reference.

Property unique IDs represent a tree structure, where each property is
at the “leaf” level of the tree. Some operations allow the host to work
with entire groups of properties (branches or even the trunk containing
all its leaves) by using a property number representing a higher level
of the tree.

Each property (a “leaf” in the tree) is described in a subsection below,
including whether it can be written to, how it is secured, how to
construct or interpret its value(s), and how it affects device behavior.

To reflect this hierarchy, this section of the document groups settings
by major categories that correspond to the tree structure, which roughly
breaks down into overall property **type**, **module**, and
**submodule**.

### Property Group 1.1.nnnn Financial Settings

#### Property Subgroup 1.1.1.nnn EMV Settings

##### Property 1.1.1.1.1.1 EMV Terminal Identification

Table 344 - Property 1.1.1.1.1.1 EMV Terminal Identification

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.1 / 0x010101010101 |
| Name | EMV Terminal Identification |
| Description | The device uses this property to report its Terminal ID / Terminal Identification in tag **9F1C** in all EMV-related communication. Merchants usually configure each device with a different terminal ID per their own proprietary system standards to help identify the source of a transaction. |
| Securing Key | None |
| Min. Len (b) | 8 |
| Max. Len (b) | 8 |
| Data Type | Alphanumeric |
| Valid Values | Any string |
| Default | “00000000” (0x3030303030303030) |

Table 345 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 04 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E1 06 E1 04 E1 02 C1 00 |

Table 346 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 04 D1 01 82 04 00 00 00 00 84 82 00 22 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 12 E1 10 E1 0E E1 0C E1 0A C1 08 30 30 30 30 30 30 30 30 |

Table 347 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 3E D1 11 84 22 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 12 E1 10 E1 0E E1 0C E1 0A C1 08 31 31 31 31 31 31 31 31 |

Table 348 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 3E D1 11 82 04 00 00 00 00 84 82 00 22 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 12 E1 10 E1 0E E1 0C E1 0A C1 08 31 31 31 31 31 31 31 31 |

##### Property 1.1.1.1.1.2 EMV ARQC Message Tag List

Table 349 - Property 1.1.1.1.1.2 EMV ARQC Message Tag List

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.2 / 0x010101010102 |
| Name | EMV ARQC Message Tag List |
| Description | The device uses this property when it generates an **EMV ARQC Type** data object, to determine what tags to include in the data object. It serves the same purpose that MagTek custom tag DFDF02 serves on some other MagTek devices. |
| Securing Key | None |
| Min. Len (b) | 0 |
| Max. Len (b) | 255 |
| Data Type | Binary |
| Valid Values | List of any valid standard EMV message tags and device custom tags |
| Default | 50 5A 57 82 84 95 9A 9B 9C F4 5F 1A 5F 20 5F 24 5F 2A 5F 30 5F 34 9F 02 9F 03 9F 06 9F 09 9F 10 9F 15 9F 1A 9F 1D 9F 1E 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 9F 39 9F 41 9F 45 9F 4C 9F 4E 9F 5D 9F 66 9F 6E 9F 7C |

Table 350 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 08 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E1 06 E1 04 E1 02 C2 00 |

Table 351 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 08 D1 01 82 04 00 00 00 00 84 82 00 64 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 54 E1 52 E1 50 E1 4E E1 4C C2 4A 50 5A 57 82 84 95 9A 9B 9C F4 5F 1A 5F 20 5F 24 5F 2A 5F 30 5F 34 9F 02 9F 03 9F 06 9F 09 9F 10 9F 15 9F 1A 9F 1D 9F 1E 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 9F 39 9F 41 9F 45 9F 4C 9F 4E 9F 5D 9F 66 9F 6E 9F 7C |

Table 352 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 09 D1 11 84 64 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 54 E1 52 E1 50 E1 4E E1 4C C2 4A 50 5A 57 82 84 95 9A 9B 9C F4 5F 1A 5F 20 5F 24 5F 2A 5F 30 5F 34 9F 02 9F 03 9F 06 9F 09 9F 10 9F 15 9F 1A 9F 1D 9F 1E 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 9F 39 9F 41 9F 45 9F 4C 9F 4E 9F 5D 9F 66 9F 6E 9F 7C |

Table 353 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 09 D1 11 82 04 00 00 00 00 84 82 00 64 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 54 E1 52 E1 50 E1 4E E1 4C C2 4A 50 5A 57 82 84 95 9A 9B 9C F4 5F 1A 5F 20 5F 24 5F 2A 5F 30 5F 34 9F 02 9F 03 9F 06 9F 09 9F 10 9F 15 9F 1A 9F 1D 9F 1E 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 9F 39 9F 41 9F 45 9F 4C 9F 4E 9F 5D 9F 66 9F 6E 9F 7C |

##### Property 1.1.1.1.1.3 EMV Batch Data Tag List

Table 354 - Property 1.1.1.1.1.3 EMV Batch Data Tag List

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.3 / 0x010101010103 |
| Name | EMV Batch Data Tag List |
| Description | The device uses this property when it generates an **EMV Batch Data Type** data object to contain **transaction result data**, to determine what tags to include in the data object. It serves the same purpose that MagTek custom tag DFDF17 serves on some other MagTek devices. |
| Securing Key | None |
| Min. Len (b) | 0 |
| Max. Len (b) | 255 |
| Data Type | Binary |
| Valid Values | List of any valid standard EMV message tags and device custom tags |
| Default | 50 57 5A 82 84 8E 95 9A 9C F4 5F 20 5F 24 5F 25 5F 28 5F 2A 5F 2D 5F 34 9F 02 9F 03 9F 07 9F 09 9F 0B 9F 0D 9F 0E 9F 0F 9F 10 9F 11 9F 12 9F 15 9F 16 9F 1A 9F 1C 9F 1E 9F 21 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 DF DF 25 |

Table 355 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 15 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E1 06 E1 04 E1 02 C3 00 |

Table 356 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 15 D1 01 82 04 00 00 00 00 84 82 00 66 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 56 E1 54 E1 52 E1 50 E1 4E C3 4C 50 57 5A 82 84 8E 95 9A 9C 5F 20 5F 24 5F 25 5F 28 5F 2A 5F 2D 5F 34 9F 02 9F 03 9F 07 9F 09 9F 0B 9F 0D 9F 0E 9F 0F 9F 10 9F 11 9F 12 9F 15 9F 16 9F 1A 9F 1C 9F 1E 9F 21 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 DF DF 25 |

Table 357 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0B D1 11 84 66 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 56 E1 54 E1 52 E1 50 E1 4E C3 4C 50 57 5A 82 84 8E 95 9A 9C 5F 20 5F 24 5F 25 5F 28 5F 2A 5F 2D 5F 34 9F 02 9F 03 9F 07 9F 09 9F 0B 9F 0D 9F 0E 9F 0F 9F 10 9F 11 9F 12 9F 15 9F 16 9F 1A 9F 1C 9F 1E 9F 21 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 DF DF 25 |

Table 358 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0B D1 11 82 04 00 00 00 00 84 82 00 66 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 56 E1 54 E1 52 E1 50 E1 4E C3 4C 50 57 5A 82 84 8E 95 9A 9C 5F 20 5F 24 5F 25 5F 28 5F 2A 5F 2D 5F 34 9F 02 9F 03 9F 07 9F 09 9F 0B 9F 0D 9F 0E 9F 0F 9F 10 9F 11 9F 12 9F 15 9F 16 9F 1A 9F 1C 9F 1E 9F 21 9F 24 9F 26 9F 27 9F 33 9F 34 9F 35 9F 36 9F 37 DF DF 25 |

##### Property 1.1.1.1.1.4 EMV Reversal Data Tag List (EMV Contact Only)

Table 359 - Property 1.1.1.1.1.4 EMV Reversal Data Tag List (EMV Contact
Only)

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.4 / 0x010101010104 |
| Name | EMV Reversal Data Tag List |
| Description | The device uses this property when it generates an **EMV Batch Data Type** data object to contain **reversal data**, to determine what tags to include in the data object. It serves the same purpose that MagTek custom tag DFDF05 serves on some other MagTek devices. |
| Securing Key | None |
| Min. Len (b) | 0 |
| Max. Len (b) | 255 |
| Data Type | Binary |
| Valid Values | List of any valid standard EMV message tags and device custom tags |
| Default | 57 5A 82 8A 95 9A 9C 5F 24 5F 2A 5F 34 9F 01 9F 02 9F 10 9F 15 9F 16 9F 1A 9F 1C 9F 21 9F 33 9F 35 9F 36 9F 39 9F 5B DF DF 25 |

Table 360 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 16 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E1 06 E1 04 E1 02 C4 00 |

Table 361 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 16 D1 01 82 04 00 00 00 00 84 82 00 44 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 34 E1 32 E1 30 E1 2E E1 2C C4 2A 57 5A 82 8A 95 9A 9C 5F 24 5F 2A 5F 34 9F 01 9F 02 9F 10 9F 15 9F 16 9F 1A 9F 1C 9F 21 9F 33 9F 35 9F 36 9F 39 9F 5B DF DF 25 |

Table 362 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0D D1 11 84 44 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 34 E1 32 E1 30 E1 2E E1 2C C4 2A 57 5A 82 8A 95 9A 9C 5F 24 5F 2A 5F 34 9F 01 9F 02 9F 10 9F 15 9F 16 9F 1A 9F 1C 9F 21 9F 33 9F 35 9F 36 9F 39 9F 5B DF DF 25 |

Table 363 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0D D1 11 82 04 00 00 00 00 84 82 00 44 D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 34 E1 32 E1 30 E1 2E E1 2C C4 2A 57 5A 82 8A 95 9A 9C 5F 24 5F 2A 5F 34 9F 01 9F 02 9F 10 9F 15 9F 16 9F 1A 9F 1C 9F 21 9F 33 9F 35 9F 36 9F 39 9F 5B DF DF 25 |

##### Property 1.1.1.1.1.5 ARPC Receive Timeout

Table 364 - Property 1.1.1.1.1.5 ARPC Receive Timeout

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.1.1.1.5 / 0x010101010105</td>
</tr>
<tr>
<td>Name</td>
<td>ARPC Receive Timeout</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine how long to wait for the
host to send <strong>Command 0x1004 - Resume Transaction</strong> with
ARPC data before it times out and continues a transaction the host
started with <strong>Command 0x1001 - Start Transaction</strong>.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Infinite timeout</p>
<p>0x01..0xFE = Timeout in seconds</p>
<p>0xFF = Use Transaction Timeout parameter in <strong>Command 0x1001 -
Start Transaction</strong></p></td>
</tr>
<tr>
<td>Default</td>
<td>0xFF</td>
</tr>
</tbody>
</table>

Table 365 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 C500 |

Table 366 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 10 D1 01 85 01 01 87 04 01 01 01 01 89 03 C5 01 FF |

Table 367 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870401010101 8903 C501FF |

Table 368 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 01 01 01 01 89 03 C5 01 FF |

##### Property 1.1.1.1.1.6 ARPC Retry Attempts

Table 369 - Property 1.1.1.1.1.6 ARPC Retry Attempts

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.6 / 0x010101010106 |
| Name | ARPC Retry Attempts |
| Description | The device uses this property to control its ARPC Retry Attempts. If a timeout occurs when the device is waiting for the host to send **Command 0x1004 - Resume Transaction** with ARPC data, the device re-sends **Notification 0x0101 - Transaction Information Update** to report **ARQC Update** and waits for ARPC data again, up to the number of retries specified by this property. After the final retry, the device continues with the transaction. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0x00..0xFF |
| Default | 0x00 |

Table 370 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 C600 |

Table 371 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 10 D1 01 85 01 01 87 04 01 01 01 01 89 03 C6 01 00 |

Table 372 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870401010101 8903 C60100 |

Table 373 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 01 01 01 01 89 03 C6 01 00 |

##### Property 1.1.1.1.1.7 Apple VAS Merchant ID and URL Slot 1

Table 374 - Property 1.1.1.1.1.7 Apple VAS Merchant ID and URL Slot 1

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.7 / 0x010101010107 |
| Name | Apple VAS Merchant ID and URL Slot 1 |
| Description | The device uses this property for Apple VAS processing to configure the device’s supported Merchant ID and URL. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 102 |
| Data Type | Binary |
| Valid Values | 00 or see **Table 375 - VAS Merchant ID and URL Type** |
| Default | 0x00 |

Table 375 - VAS Merchant ID and URL Type

| Tag  | Len            | Value / Description | Typ | Req | Default |
|------|----------------|---------------------|-----|-----|---------|
| 9F25 | 0x20           | Merchant ID         | B   | O   |         |
| 9F29 | Var up to 0x40 | Merchant URL        | B   | O   |         |

Table 376 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 C700 |

Table 377 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 49 D1 01 85 01 01 87 04 01 01 01 01 89 3C C7 3A 9F 25 20 3E 22 54 3A AF 0A C5 E4 AC FC 25 67 1A 6E BF 6E DE 5A C1 96 74 6C 55 F3 D4 37 08 19 FF F9 22 C3 9F 29 14 77 77 77 2E 65 78 61 6D 70 6C 65 2D 75 72 6C 2E 63 6F 6D |

Table 378 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870401010101 8903 C70100 |

Table 379 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 01 01 01 01 89 03 C7 01 00 |

##### Property 1.1.1.1.1.8 Apple VAS Merchant ID and URL Slot 2

Table 380 - Property 1.1.1.1.1.8 Apple VAS Merchant ID and URL Slot 2

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.8 / 0x010101010108 |
| Name | Apple VAS Merchant ID and URL Slot 2 |
| Description | The device uses this property for Apple VAS processing to configure the device’s supported Merchant ID and URL. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 102 |
| Data Type | Binary |
| Valid Values | 00 or see **Table 375 - VAS Merchant ID and URL Type** |
| Default | 0x00 |

Table 381 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 C800 |

Table 382 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 49 D1 01 85 01 01 87 04 01 01 01 01 89 3C C8 3A 9F 25 20 3E 22 54 3A AF 0A C5 E4 AC FC 25 67 1A 6E BF 6E DE 5A C1 96 74 6C 55 F3 D4 37 08 19 FF F9 22 C3 9F 29 14 77 77 77 2E 65 78 61 6D 70 6C 65 2D 75 72 6C 2E 63 6F 6D |

Table 383 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870401010101 8903 C80100 |

Table 384 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 01 01 01 01 89 03 C8 01 00 |

##### Property 1.1.1.1.1.9 Apple VAS Merchant ID and URL Slot 3

Table 385 - Property 1.1.1.1.1.9 Apple VAS Merchant ID and URL Slot 3

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.9 / 0x010101010109 |
| Name | Apple VAS Merchant ID and URL Slot 3 |
| Description | The device uses this property for Apple VAS processing to configure the device’s supported Merchant ID and URL. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 102 |
| Data Type | Binary |
| Valid Values | 00 or see **Table 375 - VAS Merchant ID and URL Type** |
| Default | 0x00 |

Table 386 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 C900 |

Table 387 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 49 D1 01 85 01 01 87 04 01 01 01 01 89 3C C9 3A 9F 25 20 3E 22 54 3A AF 0A C5 E4 AC FC 25 67 1A 6E BF 6E DE 5A C1 96 74 6C 55 F3 D4 37 08 19 FF F9 22 C3 9F 29 14 77 77 77 2E 65 78 61 6D 70 6C 65 2D 75 72 6C 2E 63 6F 6D |

Table 388 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870401010101 8903 C90100 |

Table 389 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 01 01 01 01 89 03 C9 01 00 |

##### Property 1.1.1.1.1.A Apple VAS Merchant ID and URL Slot 4

Table 390 - Property 1.1.1.1.1.A Apple VAS Merchant ID and URL Slot 4

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.A / 0x01010101010A |
| Name | Apple VAS Merchant ID and URL Slot 4 |
| Description | The device uses this property for Apple VAS processing to configure the device’s supported Merchant ID and URL. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 102 |
| Data Type | Binary |
| Valid Values | 00 or see **Table 375 - VAS Merchant ID and URL Type** |
| Default | 0x00 |

Table 391 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 CA00 |

Table 392 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 49 D1 01 85 01 01 87 04 01 01 01 01 89 3C CA 3A 9F 25 20 3E 22 54 3A AF 0A C5 E4 AC FC 25 67 1A 6E BF 6E DE 5A C1 96 74 6C 55 F3 D4 37 08 19 FF F9 22 C3 9F 29 14 77 77 77 2E 65 78 61 6D 70 6C 65 2D 75 72 6C 2E 63 6F 6D |

Table 393 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870401010101 8903 CA0100 |

Table 394 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 01 01 01 01 89 03 CA 01 00 |

##### Property 1.1.1.1.1.B Apple VAS Merchant ID and URL Slot 5

Table 395 - Property 1.1.1.1.1.B Apple VAS Merchant ID and URL Slot 5

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.B / 0x01010101010B |
| Name | Apple VAS Merchant ID and URL Slot 5 |
| Description | The device uses this property for Apple VAS processing to configure the device’s supported Merchant ID and URL. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 102 |
| Data Type | Binary |
| Valid Values | 00 or see **Table 375 - VAS Merchant ID and URL Type** |
| Default | 0x00 |

Table 396 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 CB00 |

Table 397 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 49 D1 01 85 01 01 87 04 01 01 01 01 89 3C CB 3A 9F 25 20 3E 22 54 3A AF 0A C5 E4 AC FC 25 67 1A 6E BF 6E DE 5A C1 96 74 6C 55 F3 D4 37 08 19 FF F9 22 C3 9F 29 14 77 77 77 2E 65 78 61 6D 70 6C 65 2D 75 72 6C 2E 63 6F 6D |

Table 398 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870401010101 8903 CB0100 |

Table 399 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 01 01 01 01 89 03 CB 01 00 |

##### Property 1.1.1.1.1.C Apple VAS Merchant ID and URL Slot 6

Table 400 - Property 1.1.1.1.1.C Apple VAS Merchant ID and URL Slot 6

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.C / 0x01010101010C |
| Name | Apple VAS Merchant ID and URL Slot 6 |
| Description | The device uses this property for Apple VAS processing to configure the device’s supported Merchant ID and URL. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 102 |
| Data Type | Binary |
| Valid Values | 00 or see **Table 375 - VAS Merchant ID and URL Type** |
| Default | 0x00 |

Table 401 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 CC00 |

Table 402 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 49 D1 01 85 01 01 87 04 01 01 01 01 89 3C CC 3A 9F 25 20 3E 22 54 3A AF 0A C5 E4 AC FC 25 67 1A 6E BF 6E DE 5A C1 96 74 6C 55 F3 D4 37 08 19 FF F9 22 C3 9F 29 14 77 77 77 2E 65 78 61 6D 70 6C 65 2D 75 72 6C 2E 63 6F 6D |

Table 403 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870401010101 8903 CC0100 |

Table 404 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 01 01 01 01 89 03 CC 01 00 |

##### Property 1.1.1.1.1.D Apple iAP2 AppBundleID 

Table 405 - Property 1.1.1.1.1.D Apple iAP2 AppBundleID

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.D / 0x01010101010D |
| Name | Apple iAP2 AppBundleID |
| Description | This setting allows the iOS device to recommend installation of a specific app or set of apps to use with the iOS device when connects to an accessory. |
| Securing Key | None |
| Min. Len (b) | A valid reverse-DNS similar to the Default below |
| Max. Len (b) | 50 |
| Data Type | ASCII |
| Valid Values | ASCII |
| Default | com.magtek.dynaflex2go |

Table 406 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E1 06 E1 04 E1 02 CD 00 |

Table 407 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 4C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 3C E1 3A E1 38 E1 36 E1 34 CD 32 63 6F 6D 2E 6D 61 67 74 65 6B 2E 64 79 6E 61 66 6C 65 78 32 67 6F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |

Table 408 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 07 D1 11 84 4C D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 3C E1 3A E1 38 E1 36 E1 34 CD 32 63 6F 6D 2E 6D 61 67 74 65 6B 2E 64 79 6E 61 66 6C 65 78 32 67 6F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |

Table 409 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 07 D1 11 82 04 00 00 00 00 84 82 00 4C D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 3C E1 3A E1 38 E1 36 E1 34 CD 32 63 6F 6D 2E 6D 61 67 74 65 6B 2E 64 79 6E 61 66 6C 65 78 32 67 6F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |

##### Property 1.1.1.1.1.10 Google Smart Tap Collector ID Slot 1

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.10 / 0x010101010110 |
| Name | Google Smart Tap Collector ID Slot 1 |
| Description | The device uses this property for Google Smart Tap processing to configure the device’s supported Collector ID and Service Types. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 25 |
| Data Type | Binary |
| Valid Values | 00 or see **Table 375 - VAS Merchant ID and URL Types** |
| Default | 0x00 |

Table 410 - Property 1.1.1.1.1.10 Google Smart Tap Collector ID Slot 1

Table 411 - Google Smart Tap Collector ID and Service Types

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 29%" />
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th>Tag</th>
<th>Len</th>
<th>Value / Description</th>
<th>Typ</th>
<th>Req</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td>DF7C</td>
<td>0x08</td>
<td>GWST Collector ID</td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
<tr>
<td>DF7D</td>
<td>Var up to 0x0E</td>
<td><p>GWST Service Types</p>
<p>0x00 = All services</p>
<p>0x01 = All services except PPSE</p>
<p>0x02 = PPSE</p>
<p>0x03 = Loyalty</p>
<p>0x04 = Offer</p>
<p>0x05 = Gift card</p>
<p>0x06 = Private label card</p>
<p>0x07 = Event ticket</p>
<p>0x08 = Flight</p>
<p>0x09 = Transit</p>
<p>0x10 = Cloud-based wallet</p>
<p>0x11 = Mobil marketing platform</p>
<p>0x12 = Generic</p>
<p>0x13 = Generic private pass</p>
<p>0x40 = Wallet customer</p></td>
<td>B</td>
<td>R</td>
<td></td>
</tr>
</tbody>
</table>

Table 412 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 D000 |

Table 413 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 1E D1 01 85 01 01 87 04 01 01 01 01 89 11 D0 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

Table 414 - Set Request Example

| Example (Hex) |
|----|
| AA00 81048255D111 8427 D111 8107 2B06010401F609 8501 01 8704 01010101 8911 D00F DF7C083230313830363038DF7D0100 |

Table 415 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 2 7D 11 18 10 7 2B 06 01 04 01 F6 09 85 01 01 87 04 01 01 01 01 89 11 D0 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

##### Property 1.1.1.1.1.11 Google Smart Tap Collector ID Slot 2

Table 416 - Property 1.1.1.1.1.11 Google Smart Tap Collector ID Slot 2

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.11 / 0x010101010111 |
| Name | Google Smart Tap Collector ID Slot 2 |
| Description | The device uses this property for Google Smart Tap processing to configure the device’s supported Collector ID and Service Types. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 25 |
| Data Type | Binary |
| Valid Values | 00 or see **Table 375 - VAS Merchant ID and URL Types** |
| Default | 0x00 |

Table 417 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 D100 |

Table 418 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 1E D1 01 85 01 01 87 04 01 01 01 01 89 11 D1 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

Table 419 - Set Request Example

| Example (Hex) |
|----|
| AA00 81048255D111 8427 D111 8107 2B06010401F609 8501 01 8704 01010101 8911 D10F DF7C083230313830363038DF7D0100 |

Table 420 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 2 7D 11 18 10 7 2B 06 01 04 01 F6 09 85 01 01 87 04 01 01 01 01 89 11 D1 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

##### Property 1.1.1.1.1.12 Google Smart Tap Collector ID Slot 3

Table 421- Property 1.1.1.1.1.12 Google Smart Tap Collector ID Slot 3

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.12 / 0x010101010112 |
| Name | Google Smart Tap Collector ID Slot 3 |
| Description | The device uses this property for Google Smart Tap processing to configure the device’s supported Collector ID and Service Types. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 25 |
| Data Type | Binary |
| Valid Values | 00 or see **Table 375 - VAS Merchant ID and URL Types** |
| Default | 0x00 |

Table 422 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 D200 |

Table 423 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 1E D1 01 85 01 01 87 04 01 01 01 01 89 11 D2 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

Table 424 - Set Request Example

| Example (Hex) |
|----|
| AA00 81048255D111 8427 D111 8107 2B06010401F609 8501 01 8704 01010101 8911 D20F DF7C083230313830363038DF7D0100 |

Table 425 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 2 7D 11 18 10 7 2B 06 01 04 01 F6 09 85 01 01 87 04 01 01 01 01 89 11 D2 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

##### Property 1.1.1.1.1.13 Google Smart Tap Collector ID Slot 4

Table 426 - Property 1.1.1.1.1.13 Google Smart Tap Collector ID Slot 4

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.13 / 0x010101010113 |
| Name | Google Smart Tap Collector ID Slot 4 |
| Description | The device uses this property for Google Smart Tap processing to configure the device’s supported Collector ID and Service Types. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 25 |
| Data Type | Binary |
| Valid Values | 00 or see **Table 375 - VAS Merchant ID and URL Types** |
| Default | 0x00 |

Table 427 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 D300 |

Table 428 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 1E D1 01 85 01 01 87 04 01 01 01 01 89 11 D3 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

Table 429 - Set Request Example

| Example (Hex) |
|----|
| AA00 81048255D111 8427 D111 8107 2B06010401F609 8501 01 8704 01010101 8911 D30F DF7C083230313830363038DF7D0100 |

Table 430 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 2 7D 11 18 10 7 2B 06 01 04 01 F6 09 85 01 01 87 04 01 01 01 01 89 11 D3 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

##### Property 1.1.1.1.1.14 Google Smart Tap Collector ID Slot 5

Table 431 - Property 1.1.1.1.1.14 Google Smart Tap Collector ID Slot 5

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.14 / 0x010101010114 |
| Name | Google Smart Tap Collector ID Slot 5 |
| Description | The device uses this property for Google Smart Tap processing to configure the device’s supported Collector ID and Service Types. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 25 |
| Data Type | Binary |
| Valid Values | 00 or see **Table 375 - VAS Merchant ID and URL Types** |
| Default | 0x00 |

Table 432 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 D400 |

Table 433 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 1E D1 01 85 01 01 87 04 01 01 01 01 89 11 D4 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

Table 434 - Set Request Example

| Example (Hex) |
|----|
| AA00 81048255D111 8427 D111 8107 2B06010401F609 8501 01 8704 01010101 8911 D40F DF7C083230313830363038DF7D0100 |

Table 435 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 2 7D 11 18 10 7 2B 06 01 04 01 F6 09 85 01 01 87 04 01 01 01 01 89 11 D4 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

##### Property 1.1.1.1.1.15 Google Smart Tap Collector ID Slot 6

Table 436 - Property 1.1.1.1.1.15 Google Smart Tap Collector ID Slot 6

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.1.15 / 0x010101010115 |
| Name | Google Smart Tap Collector ID Slot 6 |
| Description | The device uses this property for Google Smart Tap processing to configure the device’s supported Collector ID and Service Types. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 25 |
| Data Type | Binary |
| Valid Values | 00 or see **Table 375 - VAS Merchant ID and URL Types** |
| Default | 0x00 |

Table 437 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 D500 |

Table 438 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 1E D1 01 85 01 01 87 04 01 01 01 01 89 11 D5 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

Table 439 - Set Request Example

| Example (Hex) |
|----|
| AA00 81048255D111 8427 D111 8107 2B06010401F609 8501 01 8704 01010101 8911 D50F DF7C083230313830363038DF7D0100 |

Table 440 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 2 7D 11 18 10 7 2B 06 01 04 01 F6 09 85 01 01 87 04 01 01 01 01 89 11 D5 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

##### Property 1.1.1.1.1.1A Google Smart Tap POS Capabilities

Table 441 - Property 1.1.1.1.1.1A Google Smart Tap POS CapabilitiesPOS
Capabilities

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.1.1.1.1A / 0x01010101011A</td>
</tr>
<tr>
<td>Name</td>
<td>Google Smart Tap POS Capabilities</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property for Google Smart Tap processing to
configure the device’s supported POS Capabilities.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Byte value where each bit of the byte indicates a particular POS
capability. Bit 0 is the least significant bit. The Tap byte is
generated by the device.</p>
<p>Byte 1 – System:</p>
<p>Bit 0: Standalone</p>
<p>Bit 1: Semi-integrated</p>
<p>Bit 2: Unattended</p>
<p>Bit 3: Online</p>
<p>Bit 4: Offline</p>
<p>Bit 5: MMP</p>
<p>Bit 6: zlib support</p>
<p>Bit 7: RFU</p>
<p>Byte 2 – UI:</p>
<p>Bit 0: Printer</p>
<p>Bit 1: Printer graphics</p>
<p>Bit 2: Display</p>
<p>Bit 3: Images</p>
<p>Bit 4: Audio</p>
<p>Bit 5: Animation</p>
<p>Bit 6: Video</p>
<p>Bit 7: RFU</p>
<p>Byte 3 – Checkout:</p>
<p>Bit 0: Support payment</p>
<p>Bit 1: Support digital receipt</p>
<p>Bit 2: Support service issuance</p>
<p>Bit 3: Support OTA POS data</p>
<p>Bit 4: RFU</p>
<p>Bit 5: RFU</p>
<p>Bit 6: RFU</p>
<p>Bit 7: RFU</p>
<p>Byte 4 – CVM</p>
<p>Bit 0: Online PIN</p>
<p>Bit 1: CD PIN</p>
<p>Bit 2: Signature</p>
<p>Bit 3: No CVM</p>
<p>Bit 4: Device-generated code</p>
<p>Bit 5: SP-generated code</p>
<p>Bit 6: ID capture</p>
<p>Bit 7: Biometric</p></td>
</tr>
<tr>
<td>Default</td>
<td><p>DynaProx, DynaFlex II Go and DynaFlex II: 0x08, 0x10, 0x03,
0x00</p>
<p>All Other devices: 0x08, 0x14, 0x03, 0x05</p></td>
</tr>
</tbody>
</table>

Table 442 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010101 8902 D400 |

Table 443 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 1E D1 01 85 01 01 87 04 01 01 01 01 89 11 D4 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

Table 444 - Set Request Example

| Example (Hex) |
|----|
| AA00 81048255D111 8427 D111 8107 2B06010401F609 8501 01 8704 01010101 8911 D40F DF7C083230313830363038DF7D0100 |

Table 445 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 2 7D 11 18 10 7 2B 06 01 04 01 F6 09 85 01 01 87 04 01 01 01 01 89 11 D4 0F DF 7C 08 32 30 31 38 30 36 30 38 DF 7D 01 00 |

##### Property 1.1.1.1.2.1 Start Transaction on Touchscreen Event Control(Touch Only)

Table 446 - Property 1.1.1.1.2.1 Start Transaction on Touchscreen Event
Control(Touch Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.1.1.2.1 / 0x010101010201</td>
</tr>
<tr>
<td>Name</td>
<td>Start Transaction on Touchscreen Event Control</td>
</tr>
<tr>
<td>Description</td>
<td>The device use this property to determine if a transaction operation
is to be started when a Touchscreen event is detected.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 – Do not start Transaction on Touchscreen event</p>
<p>0x01 – Start Transaction on Touchscreen Event</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00 - Do not start Transaction on Touchscreen event s</td>
</tr>
</tbody>
</table>

Table 447 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101028902C100 |

Table 448 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704010101028903C10100 |

Table 449 - Set Request Example

| Example (Hex)                                        |
|------------------------------------------------------|
| AA0081040155D1118410D1118501018704010101028903C10100 |

Table 450 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704010101028903C10100 |

##### Property 1.1.1.1.2.2 Tip Mode(Touch Only)

Table 451 - Property 1.1.1.1.2.2 Tip Mode(Touch Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.1.1.2.2 / 0x010101010202</td>
</tr>
<tr>
<td>Name</td>
<td>Tip Mode</td>
</tr>
<tr>
<td>Description</td>
<td>The Tip Mode to use when in Event Driven mode</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1F</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1F</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Byte 1 Tip Mode</p>
<p>0x00 – Disable Tip Mode</p>
<p>0x01 – Show Tip GUI immediately using % value</p>
<p>0x02 – Show Tip GUI immediately using $ amount</p>
<p>Byte 2, Display Mode for Button1</p>
<p>0 - % or Amount</p>
<p>1 – Display Custom</p>
<p>2 – Display NO TIP</p>
<p>3 – Disabled (An OID controls whether the button is blank, grayed out
or not showing)</p>
<p>Bytes 3 to 6 Value in % or Amount for Button 1, if applicable</p>
<p>Byte 7, Display Mode for Button 2 (See Byte 2 for Details)</p>
<p>Bytes 8 to 11 Value in % or Amount for Button 2, if applicable</p>
<p>Byte 12, Display Mode for Button 3 (See Byte 2 for Details)</p>
<p>Bytes 13 to 16 Value in % or Amount for Button 3, if applicable</p>
<p>Byte 17, Display Mode for Button 4 (See Byte 2 for Details)</p>
<p>Bytes 18 to 21 Value in % or Amount for Button 4, if applicable</p>
<p>Byte 22, Display Mode for Button 5 (See Byte 2 for Details)</p>
<p>Bytes 23 to 26 Value in % or Amount for Button 5, if applicable</p>
<p>Byte 27, Display Mode for Button 6 (See Byte 2 for Details)</p>
<p>Bytes 28 to 31 Value in % or Amount for Button 6, if
applicable</p></td>
</tr>
<tr>
<td>Default</td>
<td><p>0x1, // show tip GUI using %</p>
<p>0x0, 0x0, 0x0, 0x0, 0x15, // button 1, %, value 15</p>
<p>0x0, 0x0, 0x0, 0x0, 0x20, // button 2, %, value 20</p>
<p>0x0, 0x0, 0x0, 0x0, 0x25, // button 3, %, value 25</p>
<p>0x2, 0x0, 0x0, 0x0, 0x0, // button 4 'no tip'</p>
<p>0x1, 0x0, 0x0, 0x0, 0x0, // button 5 'custom'</p>
<p>0x3, 0x0, 0x0, 0x0, 0x0, // button 6 disabled</p></td>
</tr>
</tbody>
</table>

Table 452 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 01010102 8902 C200 |

Table 453 - Get Response Example

| Example (Hex) |
|----|
| AA0081048255D1018204000000008482002ED1018501018704010101028921C21F00000000001500000000200000000025020000000001000000000300000000 |

Table 454 - Set Request Example

| Example (Hex) |
|----|
| AA0081040155D111842ED1118501018704010101028921C21F00000000001500000000200000000025020000000001000000000300000000 |

Table 455 - Set Response Example

| Example (Hex) |
|----|
| AA0081048255D1118204000000008482002ED1118501018704010101028921C21F00000000001500000000200000000025020000000001000000000300000000 |

##### Property 1.1.1.1.2.3 Tax Rate (Touch Only)

Table 456 - Property 1.1.1.1.2.3 Tax Rate (Touch Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.1.1.2.3/ 0x010101010203</td>
</tr>
<tr>
<td>Name</td>
<td>Tax Rate</td>
</tr>
<tr>
<td>Description</td>
<td>Tax Rate that is used when in Event Driven Mode</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>3</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>3</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x000000 – Tax Display and Calculation Disabled</p>
<p>0x000001 thru 0x999999- Tax Rate (0.0001% thru 99.9999%)</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x000000 - Tax Display and Calculation Disabled</td>
</tr>
</tbody>
</table>

Table 457 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101028902C300 |

Table 458 - Get Response Example

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA0081048255D10182040000000084820012D1018501018704010101028905C303000000 |

Table 459 - Set Request Example

| Example (Hex)                                            |
|----------------------------------------------------------|
| AA0081040155D1118412D1118501018704010101028905C303108725 |

Table 460 - Set Response Example

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA0081048255D11182040000000084820012D1118501018704010101028905C303108725 |

##### Property 1.1.1.1.2.4 Display Tax or Surcharge (Touch Only)

Table 461 - Property 1.1.1.1.2.4 Display Tax or Surcharge (Touch Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.1.1.2.4 / 0x010101010204</td>
</tr>
<tr>
<td>Name</td>
<td>Display Tax or Surcharge Control</td>
</tr>
<tr>
<td>Description</td>
<td>The device will check this property to determine to display Tax or
Surcharge label.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 – Display Tax</p>
<p>0x01 – Display Surcharge</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00 – Display Tax</td>
</tr>
</tbody>
</table>

Table 462 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101028902C400 |

Table 463 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704010101028903C40100 |

Table 464 - Set Request Example

| Example (Hex)                                        |
|------------------------------------------------------|
| AA0081040155D1118410D1118501018704010101028903C40100 |

Table 465 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704010101028903C40100 |

##### Property 1.1.1.1.2.5 Disabled Tip Button Display Mode (Touch Only)

Table 466 - Property 1.1.1.1.2.5 Disabled Tip Button Display Mode (Touch
Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.1.1.2.5 / 0x010101010205</td>
</tr>
<tr>
<td>Name</td>
<td>Disabled Tip Button Display Mode</td>
</tr>
<tr>
<td>Description</td>
<td>The device will check this property to determine how to handle or
display a disabled Tip button.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 – Display as Blank</p>
<p>0x01 – Display as Disabled (grayed-out)</p>
<p>0x02 - Invisible</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x02 - Invisible</td>
</tr>
</tbody>
</table>

Table 467 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101028902C500 |

Table 468 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704010101028903C50100 |

Table 469 - Set Request Example

| Example (Hex)                                        |
|------------------------------------------------------|
| AA0081040155D1118410D1118501018704010101028903C50100 |

Table 470 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704010101028903C50100 |

##### Property 1.1.1.1.2.6 Tip Mode Enable Submit on Amount Button Press

Table 471 - Property 1.1.1.1.2.6 Tip Mode Enable Submit on Amount Button
Press

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.1.1.2.6 / 0x010101010206</td>
</tr>
<tr>
<td>Name</td>
<td>Tip Mode Enable Submit on Amount Button Press</td>
</tr>
<tr>
<td>Description</td>
<td>When enabled, pressing an amount, percent, or ‘no tip’ button on the
tip entry page will proceed immediately without requiring a subsequent
tap of the ‘Submit’ button.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 – Disabled: Require submit button tap</p>
<p>0x01 – Enabled: Don’t require submit button tap</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00 - Disabled</td>
</tr>
</tbody>
</table>

Table 472 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101028902C600 |

Table 473 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704010101028903C60101 |

Table 474 - Set Request Example

| Example (Hex)                                        |
|------------------------------------------------------|
| AA0081040155D1118410D1118501018704010101028903C60101 |

Table 475 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704010101028903C60101 |

##### Property 1.1.1.1.3.1 Timeout (Touch Only)

Table 476 - Property 1.1.1.1.3.1 Timeout (Touch Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.1.1.3.1 / 0x010101010301</td>
</tr>
<tr>
<td>Name</td>
<td>Timeout</td>
</tr>
<tr>
<td>Description</td>
<td>Transaction Timeout in seconds</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 – No Timeout</p>
<p>0x01 – 0xFF (1 to 255 Seconds)</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x78 – 120 seconds</td>
</tr>
</tbody>
</table>

Table 477 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101038902C100 |

Table 478 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704010101038903C10178 |

Table 479 - Set Request Example

| Example (Hex)                                        |
|------------------------------------------------------|
| AA0081040155D1118410D1118501018704010101038903C10150 |

Table 480 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704010101038903C10150 |

##### Property 1.1.1.1.3.2 Reader Options (Touch Only)

Table 481 - Property 1.1.1.1.3.2 Reader Options (Touch Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.1.1.3.2 / 0x010101010302</td>
</tr>
<tr>
<td>Name</td>
<td>Reader Options</td>
</tr>
<tr>
<td>Description</td>
<td>Configures which payment method interface is enabled, PIN Block
format</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>9</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>20</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td><p>810101 820101 830101 85020101 860100</p>
<p>MSR Enabled</p>
<p>Contact Enabled</p>
<p>Contactless Enabled</p>
<p>BCR Enabled and Encrypt Non-EMV</p>
<p>PIN Block Format 0</p></td>
</tr>
</tbody>
</table>

Table 482 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101038902C200 |

Table 483 - Get Response Example

| Example (Hex) |
|----|
| AA0081048255D10182040000000084820023D1018501018704010101038916C2148101018201018301018400000085020101860100 |

Table 484 - Set Request Example

| Example (Hex) |
|----|
| AA0081040155D111841FD1118501018704010101038912C21081010182010183010185020101860100 |

Table 485 - Set Response Example

| Example (Hex) |
|----|
| AA0081048255D1118204000000008482001FD1118501018704010101038912C21081010182010183010185020101860100 |

##### Property 1.1.1.1.3.3 Transaction Options (Touch Only)

Table 486 - Property 1.1.1.1.3.3 Transaction Options (Touch Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.1.1.3.3 / 0x010101010303</td>
</tr>
<tr>
<td>Name</td>
<td>Transaction Options</td>
</tr>
<tr>
<td>Description</td>
<td>Sets various device behaviors that change the transaction flow or
the way the device reports transaction results</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>20</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td><p>84020007</p>
<p>Apple VAS Disabled</p>
<p>Quickchip</p>
<p>Skip MSR signature capture if service code is chip card</p>
<p>Do not display amount in Quickchip</p></td>
</tr>
</tbody>
</table>

Table 487 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101038902C300 |

Table 488 - Get Response Example

| Example (Hex) |
|----|
| AA0081048255D10182040000000084820023D1018501018704010101038916C3148402000700000000000000000000000000000000 |

Table 489 - Set Request Example

| Example (Hex)                                              |
|------------------------------------------------------------|
| AA0081040155D1118413D1118501018704010101038906C30484020007 |

Table 490 - Set Response Example

| Example (Hex) |
|----|
| AA0081048255D11182040000000084820013D1118501018704010101038906C30484020007 |

##### Property 1.1.1.1.3.4 Other TLV (Touch Only)

Table 491 - Property 1.1.1.1.3.4 Other TLV (Touch Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.1.1.3.4 / 0x010101010304</td>
</tr>
<tr>
<td>Name</td>
<td>Other TLV</td>
</tr>
<tr>
<td>Description</td>
<td>This is a list of self-contained TLV data objects that defines the
basic parameters for the transaction.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>3</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>100</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td><p>9C0100 9F0206000000000100 9F0306000000000000 5F2A020840
5F360102</p>
<p>Transaction Type = Purchase</p>
<p>Default Amount for Quickchip = $1.00</p>
<p>Amount, Other = 0</p>
<p>Transaction Currency Code = US Dollar</p>
<p>Transaction Currency Exponent = 2</p></td>
</tr>
</tbody>
</table>

Table 492 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501018704010101038902C400 |

Table 493 - Get Response Example

| Example (Hex) |
|----|
| AA0081048255D1018204000000008482002DD1018501018704010101038920C41E9C01009F02060000000001009F03060000000000005F2A0208405F360102 |

Table 494 - Set Request Example

| Example (Hex) |
|----|
| AA0081040155D111842DD1118501018704010101038920C41E9C01009F02060000000001009F03060000000000005F2A0208405F360102 |

Table 495 - Set Response Example

| Example (Hex) |
|----|
| AA0081048255D1118204000000008482002DD1118501018704010101038920C41E9C01009F02060000000001009F03060000000000005F2A0208405F360102 |

##### Property 1.1.1.1.4.1 EMV Configuration Filename

Table 496 - Property 1.1.1.1.4.1 EMV Configuration Filename

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.4.1 / 0x010101010401 |
| Name | EMV Configuration Filename |
| Description | This string contains the part number and the revision of the EMV Configuration File. |
| Securing Key | None |
| Min. Len (b) | 14 |
| Max. Len (b) | 14 |
| Data Type | ASCII |
| Valid Values | CFG000xxxx-xxx |
| Default | None |

Table 497 - Get Request Example

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA0081040106D101841AD10181072B06010401F609850101890AE108E106E104E402C100 |

Table 498 - Get Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048206D10182040000000084820028D10181072B06010401F609850101</p>
<p>8918E116E114E112E410C10E434647303030363831322D323030</p></td>
</tr>
</tbody>
</table>

Table 499 - Set Request Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081040106D1118428D11181072B06010401F6098501018918E116E114E112E410C10E</p>
<p>434647303030363831322D323030</p></td>
</tr>
</tbody>
</table>

Table 500 - Set Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048206D11182040000000084820028D11181072B06010401F609850101</p>
<p>8918E116E114E112E410C10E434647303030363831322D323030</p></td>
</tr>
</tbody>
</table>

##### Property 1.1.1.1.4.2 CA Public Key Configuration Filename

Table 501 - Property 1.1.1.1.4.2 CA Public Key Configuration Filename

| Property Description |  |
|----|----|
| Property OID | 1.1.1.1.4.2 / 0x010101010402 |
| Name | CA Public Key Configuration Filename |
| Description | This string contains the part number and the revision of the CA Public Key Configuration File. |
| Securing Key | None |
| Min. Len (b) | 14 |
| Max. Len (b) | 14 |
| Data Type | ASCII |
| Valid Values | CFG000xxxx-xxx |
| Default | None |

Table 502 - Get Request Example

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA0081040106D101841AD10181072B06010401F609850101890AE108E106E104E402C200 |

Table 503 - Get Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048206D10182040000000084820028D10181072B06010401F609850101</p>
<p>8918E116E114E112E410C20E434647303030363831322D323030</p></td>
</tr>
</tbody>
</table>

Table 504 - Set Request Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081040106D1118428D11181072B06010401F6098501018918E116E114E112E410C20E</p>
<p>434647303030363831322D323030</p></td>
</tr>
</tbody>
</table>

Table 505 - Set Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048206D11182040000000084820028D11181072B06010401F609850101</p>
<p>8918E116E114E112E410C20E434647303030363831322D323030</p></td>
</tr>
</tbody>
</table>

#### Property Subgroup 1.1.2.nnn SRED Settings

##### Property 1.1.2.2.1.2 ISO/ABA Masking Character

Table 506 - Property 1.1.2.2.1.2 ISO/ABA Masking Character

| Property Description |  |
|----|----|
| Property OID | 1.1.2.2.1.2 / 0x010102020102 |
| Name | ISO/ABA Masking Character |
| Description | The device uses this property to determine what character it should use when sending masked ISO/ABA track data. If the **Property 1.1.2.2.1.5 PAN MOD 10 Check Digit Correction** is enabled, the masked portions of the track will always be masked with ‘0’. For more information about masking, see the information at the bottom of this section. |
| Securing Key | None |
| Min. Len (b) | 0x00 |
| Max. Len (b) | 0x01 |
| Data Type | Character |
| Valid Values | Any ASCII character |
| Default | ‘0’ |

Table 507 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 17 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E2 04 E1 02 C2 00 |

Table 508 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 17 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C2 01 2A |

Table 509 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0F D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C2 01 30 |

Table 510 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0F D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C2 01 30 |

When the device sends masked track data, it replaces some characters in
the track data with a specified mask character. The specific characters
the device masks depends on the card encode type. The device only
selectively masks data that came from ISO/ABA cards (Financial Cards
with ***ISO/IEC 7813*** Format code B); it sends data from all other
card types entirely unmasked.

The device masks all fields from ISO/ABA cards except a number of
configurable leading and trailing characters of the PAN. See **Property
1.1.2.2.1.3 PAN Number of Leading Unmasked Characters** and **Property
1.1.2.2.1.4 PAN Number of Trailing Unmasked Characters**.

For chip card transactions, masked track 2 data is contained in TLV data
object DFDF4D. For magnetic stripe transactions, masked track 1, 2 and 3
data is contained in TLV data objects DFDF31, DFDF33 and DFDF35,
respectively.

**Table 511** **below** provides an example of data from tracks 1, 2,
and 3 of an ISO/ABA card after it has been decrypted or if the device
has sent it in the clear. **Table 512** shows the same data as it might
appear with a specific set of masking rules applied.

Table 511 - Sample ISO/ABA Track Data, Clear Text / Decrypted

| Sample ISO/ABA Track Data, Clear Text / Decrypted |  |
|----|----|
| Track 1 | %B6011000995500000^ TEST CARD ^15121015432112345678? |
| Track 2 | ;6011000995500000=15121015432112345678? |
| Track 3 | ;6011000995500000=15121015432112345678333333333333333333333? |

Table 512 - Sample ISO/ABA Track Data, Masked

| Sample ISO/ABA Track Data, Masked |  |
|----|----|
| Track 1 | %B6011000020000000^0000000000^00000000000000000000? |
| Track 2 | ;6011000020000000=00000000000000000000? |
| Track 3 | ;6011000020000000=00000000000000000000000000000000000000000? |

##### Property 1.1.2.2.1.3 PAN Number of Leading Unmasked Characters

Table 513 - Property 1.1.2.2.1.3 PAN Number of Leading Unmasked
Characters

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.2.2.1.3 / 0x010102020103</td>
</tr>
<tr>
<td>Name</td>
<td>PAN Number of Leading Unmasked Characters</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine how many of the leading
characters of the PAN the device sends unmasked in <strong>Masked Track
x Data</strong> in ISO/ABA account information For details about ISO/ABA
track masking, see <strong>Property 1.1.2.2.1.2 ISO/ABA</strong> Masking
Character.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Min 0x00</p>
<p>Max 0x08, if PAN length is less than 16, the number of unmasked
characters will be limited to 6.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x04</td>
</tr>
</tbody>
</table>

Table 514 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 18 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E2 04 E1 02 C3 00 |

Table 515 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 18 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C3 01 04 |

Table 516 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 10 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C3 01 04 |

Table 517 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 10 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C3 01 04 |

##### Property 1.1.2.2.1.4 PAN Number of Trailing Unmasked Characters

Table 518 - Property 1.1.2.2.1.4 PAN Number of Trailing Unmasked
Characters

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.2.2.1.4 / 0x010102020104</td>
</tr>
<tr>
<td>Name</td>
<td>PAN Number of Trailing Unmasked Characters</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine how many of the trailing
characters of the PAN the device sends unmasked in <strong>Masked Track
x Data</strong> in ISO/ABA account information For details about ISO/ABA
track masking, see <strong>Property 1.1.2.2.1.2 ISO/ABA Masking
Character</strong>.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Min 0x00</p>
<p>Max 0x04</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x04</td>
</tr>
</tbody>
</table>

Table 519 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 19 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E2 04 E1 02 C4 00 |

Table 520 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 19 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C4 01 04 |

Table 521 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 11 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C4 01 04 |

Table 522 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 11 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C4 01 04 |

##### Property 1.1.2.2.1.5 PAN MOD 10 Check Digit Correction

Table 523 - Property 1.1.2.2.1.5 PAN MOD 10 Check Digit Correction

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.2.2.1.5 / 0x010102020105</td>
</tr>
<tr>
<td>Name</td>
<td>PAN MOD 10 Check Digit Correction</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine whether it should modify
one of the masked PAN digits such that the masked PAN passes the Luhn
MOD-10 algorithm check. If this property is enabled, the device uses
masking character ‘0’ to mask the PAN, regardless of the setting in
<strong>Property 1.1.2.2.1.2 ISO/ABA Masking Character</strong>, and
masks the remainder of the track data with the configured masking
character.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Disabled</p>
<p>0x01 = Enabled</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x01</td>
</tr>
</tbody>
</table>

Table 524 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1A D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E2 04 E1 02 C5 00 |

Table 525 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 1A D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C5 01 01 |

Table 526 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 12 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C5 01 01 |

Table 527 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 12 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C5 01 01 |

##### Property 1.1.2.2.1.6 PAN MOD 10 Check Digit Validation (MCE Only)

Table 528 - Property 1.1.2.2.1.6 PAN MOD 10 Check Digit Validation (MCE
Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.2.2.1.6 / 0x010102020106</td>
</tr>
<tr>
<td>Name</td>
<td>PAN MOD 10 Check Digit Validation</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine whether to use the Luhn
MOD-10 algorithm to validate card number (PAN) digits a cardholder or
operator enters in manual card entry mode during <strong>Command 0x1001
- Start Transaction</strong>. If validation is enabled, the device
checks the PAN digits during entry, and until the PAN passes the check,
the device disables the ENTER key, sounds an error tone when the Enter
key is pressed (if the command has audio feedback enabled), and stays at
the Card Number prompt until the cardholder or operator presses the
Cancel button or corrects the PAN.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Disabled</p>
<p>0x01 = Enabled</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 529 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1A D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E2 04 E1 02 C6 00 |

Table 530 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 1A D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C6 01 00 |

Table 531 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 12 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C6 01 01 |

Table 532 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 12 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E2 05 E1 03 C6 01 01 |

##### Property 1.1.2.4.1.1 Key Mapping of PIN-TDES (Touch Only)

Table 533 - Property 1.1.2.4.1.1 Key Mapping of PIN-TDES (Touch Only)Key
Mapping of PIN-TDES

| Property Description |  |
|----|----|
| Property OID | 1.1.2.4.1.1 / 0x010102040101 |
| Name | Key Mapping of PIN-TDES |
| Description | The device uses this property to determine which DUKPT Key Set and Variant shall be used for PIN-TDES. |
| Securing Key | None |
| Min. Len (b) | 0x03 |
| Max. Len (b) | 0x03 |
| Data Type | Binary |
| Valid Values | See DUKPT Key Mapping for detail information. |
| Default | 0x00, 0x00, 0x01 |

Table 534 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040159D101 841AD101 81072B06010401F609 850101 890AE108E206E404E102C100 |

Table 535 - Get Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 81048259D101 820400000000 8482001DD101 81072B06010401F609
850101</p>
<p>890DE10BE209E407E105C1 03200701</p></td>
</tr>
</tbody>
</table>

Table 536 - Set Request Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104015AD111 841DD111 81072B06010401F609 850101
890DE10BE209E407E105C1</p>
<p>03200701</p></td>
</tr>
</tbody>
</table>

Table 537 - Set Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104825AD111 820400000000 8482001DD111 81072B06010401F609
850101</p>
<p>890DE10BE209E407E105C1 03200701</p></td>
</tr>
</tbody>
</table>

##### Property 1.1.2.4.1.2 Key Mapping of Account Data

Table 538 - Property 1.1.2.4.1.2 Key Mapping of Account DataKey Mapping
of Account Data

| Property Description |  |
|----|----|
| Property OID | 1.1.2.4.1.2 / 0x010102040102 |
| Name | Key Mapping of Account Data |
| Description | The device uses this property to determine which DUKPT Key Set and Variant/Usage shall be used for Account Data. |
| Securing Key | None |
| Min. Len (b) | 0x03 |
| Max. Len (b) | 0x03 |
| Data Type | Binary |
| Valid Values | See DUKPT Key Mapping for detail information. |
| Default | 0x20, 0x07, 0x04 |

Table 539 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040159D101 841AD101 81072B06010401F609 850101 890AE108E206E404E102C200 |

Table 540 - Get Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 81048259D101 820400000000 8482001DD101 81072B06010401F609
850101</p>
<p>890DE10BE209E407E105C2 03200704</p></td>
</tr>
</tbody>
</table>

Table 541 - Set Request Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104015AD111 841DD111 81072B06010401F609 850101
890DE10BE209E407E105C2</p>
<p>03200704</p></td>
</tr>
</tbody>
</table>

Table 542 - Set Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104825AD111 820400000000 8482001DD111 81072B06010401F609
850101</p>
<p>890DE10BE209E407E105C2 03200704</p></td>
</tr>
</tbody>
</table>

##### Property 1.1.2.4.1.3 Key Mapping of MAC

Table 543 - Property 1.1.2.4.1.3 Key Mapping of MACKey Mapping of MAC

| Property Description |  |
|----|----|
| Property OID | 1.1.2.4.1.3 / 0x010102040103 |
| Name | Key Mapping of MAC |
| Description | The device uses this property to determine which DUKPT Key Set and Variant/Usage shall be used for MAC. |
| Securing Key | None |
| Min. Len (b) | 0x03 |
| Max. Len (b) | 0x03 |
| Data Type | Binary |
| Valid Values | See DUKPT Key Mapping for detail information. |
| Default | 0x20, 0x07, 0x02 |

Table 544 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040159D101 841AD101 81072B06010401F609 850101 890AE108E206E404E102C300 |

Table 545 - Get Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 81048259D101 820400000000 8482001DD101 81072B06010401F609
850101</p>
<p>890DE10BE209E407E105C3 03200702</p></td>
</tr>
</tbody>
</table>

Table 546 - Set Request Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104015AD111 841DD111 81072B06010401F609 850101
890DE10BE209E407E105C3</p>
<p>03200702</p></td>
</tr>
</tbody>
</table>

Table 547 - Set Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104825AD111 820400000000 8482001DD111 81072B06010401F609
850101</p>
<p>890DE10BE209E407E105C3 03200702</p></td>
</tr>
</tbody>
</table>

##### Property 1.1.2.4.1.4 Key Mapping of Magneprint (MSR Only)

Table 548 - Property 1.1.2.4.1.4 Key Mapping of Magneprint (MSR Only)Key
Mapping of Magneprint

| Property Description |  |
|----|----|
| Property OID | 1.1.2.4.1.4 / 0x010102040104 |
| Name | Key Mapping of Magneprint |
| Description | The device uses this property to determine which DUKPT Key Set and Variant/Usage shall be used for Magneprint. |
| Securing Key | None |
| Min. Len (b) | 0x03 |
| Max. Len (b) | 0x03 |
| Data Type | Binary |
| Valid Values | See DUKPT Key Mapping for detail information. |
| Default | 0x20, 0x07, 0x04 |

Table 549 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040159D101 841AD101 81072B06010401F609 850101 890AE108E206E404E102C400 |

Table 550 - Get Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 81048259D101 820400000000 8482001DD101 81072B06010401F609
850101</p>
<p>890DE10BE209E407E105C4 03200704</p></td>
</tr>
</tbody>
</table>

Table 551 - Set Request Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104015AD111 841DD111 81072B06010401F609 850101
890DE10BE209E407E105C4</p>
<p>03200704</p></td>
</tr>
</tbody>
</table>

Table 552 - Set Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104825AD111 820400000000 8482001DD111 81072B06010401F609
850101</p>
<p>890DE10BE209E407E105C4 03200704</p></td>
</tr>
</tbody>
</table>

##### Property 1.1.2.4.1.5 Key Mapping of MagTek Token

This OID is reserved for Mey Mapping of MagTek Token.

##### Property 1.1.2.4.1.6 Key Mapping of User Data 1

This OID is reserved for Mey Mapping of User Data 1.

##### Property 1.1.2.4.1.7 Key Mapping of PIN-AES (Touch Only)

Table 553 - Property 1.1.2.4.1.7 Key Mapping of PIN-AES (Touch Only)Key
Mapping of PIN-AES

| Property Description |  |
|----|----|
| Property OID | 1.1.2.4.1.7 / 0x010102040107 |
| Name | Key Mapping of PIN-AES |
| Description | The device uses this property to determine which DUKPT Key Set and Usage shall be used for PIN-AES. |
| Securing Key | None |
| Min. Len (b) | 0x03 |
| Max. Len (b) | 0x03 |
| Data Type | Binary |
| Valid Values | See DUKPT Key Mapping for detail information. |
| Default | 0x00, 0x00, 0x07 |

Table 554 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040159D101 841AD101 81072B06010401F609 850101 890AE108E206E404E102C700 |

Table 555 - Get Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 81048259D101 820400000000 8482001DD101 81072B06010401F609
850101</p>
<p>890DE10BE209E407E105C7 03200207</p></td>
</tr>
</tbody>
</table>

Table 556 - Set Request Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104015AD111 841DD111 81072B06010401F609 850101
890DE10BE209E407E105C7</p>
<p>03200207</p></td>
</tr>
</tbody>
</table>

Table 557 - Set Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104825AD111 820400000000 8482001DD111 81072B06010401F609
850101</p>
<p>890DE10BE209E407E105C7 03200207</p></td>
</tr>
</tbody>
</table>

##### Property 1.1.2.5.1.1 AAMVA Allowed (MSR Only)

Table 558 - Property 1.1.2.5.1.1 AAMVA Allowed (MSR Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.2.5.1.1 / 0x010102 050101</td>
</tr>
<tr>
<td>Name</td>
<td>AAMVA Allowed</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine whether it should accept
AAMVA (driver’s license) and other permutations of ISO encoded cards in
addition to ISO/ABA financial cards. If this is disabled, the
<strong>EMV ARQC Type</strong> the device returns to the host includes
Track Status = <strong>Error</strong> for any track that exists but does
not comply with ISO/ABA financial card format.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Disabled</p>
<p>0x01 = Enabled</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x01</td>
</tr>
</tbody>
</table>

Table 559 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1B D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E5 04 E1 02 C1 00 |

Table 560 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 1B D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C1 01 01 |

Table 561 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 14 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C1 01 01 |

Table 562 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 14 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C1 01 01s |

##### Property 1.1.2.5.1.2 Track 1 Enable (MSR Only)

Table 563 - Property 1.1.2.5.1.2 Track 1 Enable (MSR Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.2.5.1.2 / 0x010102050102</td>
</tr>
<tr>
<td>Name</td>
<td>Track 1 Enable</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine whether it should read
include or suppress Track 1 data when reading and transmitting ISO/ABA
account information from a card’s magnetic stripe.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Disabled</p>
<p>0x01 = Enabled</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x01</td>
</tr>
</tbody>
</table>

Table 564 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1C D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E5 04 E1 02 C2 00 |

Table 565 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 1C D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C2 01 01 |

Table 566 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 17 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C2 01 01 |

Table 567 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 17 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C2 01 01 |

##### Property 1.1.2.5.1.3 Track 2 Enable (MSR Only)

Table 568 - Property 1.1.2.5.1.3 Track 2 Enable (MSR Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.2.5.1.3 / 0x010102050103</td>
</tr>
<tr>
<td>Name</td>
<td>Track 2 Enable</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine whether it should read
include or suppress Track 2 data when reading and transmitting ISO/ABA
account information from a card’s magnetic stripe.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Disabled</p>
<p>0x01 = Enabled</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x01</td>
</tr>
</tbody>
</table>

Table 569 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1D D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E5 04 E1 02 C3 00 |

Table 570 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 1D D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C3 01 01 |

Table 571 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 09 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C3 01 01 |

Table 572 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 09 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C3 01 01 |

##### Property 1.1.2.5.1.4 Track 3 Enable (MSR Only)

Table 573 - Property 1.1.2.5.1.4 Track 3 Enable (MSR Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.2.5.1.4 / 0x010102050104</td>
</tr>
<tr>
<td>Name</td>
<td>Track 2 Enable</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine whether it should read
include or suppress Track 3 data when reading and transmitting ISO/ABA
account information from a card’s magnetic stripe.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>0x01</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Disabled</p>
<p>0x01 = Enabled</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x01</td>
</tr>
</tbody>
</table>

Table 574 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 02 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E5 04 E1 02 C4 00 |

Table 575 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 02 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C4 01 01 |

Table 576 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0A D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C4 01 01 |

Table 577 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0A D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E1 09 E2 07 E5 05 E1 03 C4 01 01 |

##### Property 1.1.2.6.1.1 Selectable Card Data Encryption Enable (MAGTEK INTERNAL ONLY FOR NOW)

<table>
<caption><p>Table 578 - Property 1.1.2.6.1.1 Selectable Card Data
Encryption Enable (MAGTEK INTERNAL ONLY FOR NOW)</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.1.2.6.1.1 / 0x010102060101</td>
</tr>
<tr>
<td>Name</td>
<td>Selectable Card Data Encryption Enable</td>
</tr>
<tr>
<td>Description</td>
<td>The host can use this property to enable Selectable Card Data
Encryption. Each bit enables a specific card data encryption by setting
that bit to 1. Byte 0 is the first byte, bit 0 is the LSB of each byte.
This is a secured OID, the set request shall be from 0xD112 command. If
the Key DKPTM1F has not been injected, enabling any bits in this OID
will return failure response status 80-02-05-27 (TR31 errors, Key not
present). If the Key DKPTM1F becomes unavailable after this OID has been
enabled, then this OID will be reset to 0 as a status indicator.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>Refer to 0xD112 Command.</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>0x02</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>0x02</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>This OID is bit mapped as follows:</p>
<p>Byte 0</p>
<p>• bit 0: Card Holder Name</p>
<p>• bit 1: Reserved</p>
<p>• bit 2: Expiration Date</p>
<p>• bit 3: Service Code</p>
<p>• bit 4: T1 Discretionary Data</p>
<p>• bit 5: T2 Discretionary Data</p>
<p>• bit 6 - 7: Reserved</p>
<p>Byte 1</p>
<p>• bit 0 - 7: Reserved</p>
<p>The host shall set all the reserved bits to 0.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x0000</td>
</tr>
</tbody>
</table>

Table 579 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E1 08 E2 06 E6 04 E1 02 C1 00 |

Table 580 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 1C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0C E1 0A E2 08 E6 06 E1 04 C1 02 3F 00 |

Table 581 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0B D1 12 84 5D EE EE A1 19 81 05 03 03 06 02 08 84 00 85 00 A8 0A 81 02 11 11 82 00 86 00 88 00 A9 00 82 04 BE 00 11 D0 83 08 E7 9F B1 FE 99 9F 8D A2 84 1C D1 12 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0C E1 0A E2 08 E6 06 E1 04 C1 02 3F 00 9E 10 D9 38 F1 6E 7F 8C CE 87 02 35 0F DF 8C C2 75 64 |

Table 582 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0B D1 12 82 04 00 00 00 00 84 82 00 1C D1 12 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0C E1 0A E2 08 E6 06 E1 04 C1 02 3F 00 |

### Property Group 1.2.nnnn Device Settings

#### Property Subgroup 1.2.1.nnn Transaction Settings

##### Property 1.2.1.1.1.1 Device-Driven Fallback Behavior (MSR Only)

Table 583 - Property 1.2.1.1.1.1 Device-Driven Fallback Behavior (MSR
Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.1.1 / 0x010201010101</td>
</tr>
<tr>
<td>Name</td>
<td>Device-Driven Fallback Behavior</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine whether it should
automatically implement payment brand fallback rules without host
intervention when running <strong>Command 0x1001 - Start
Transaction</strong>.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = No device-driven fallback</p>
<p>0x01 = Device-driven fallback enabled</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x01</td>
</tr>
</tbody>
</table>

Table 584 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 04 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E1 02 C1 00 |

Table 585 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 04 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E1 03 C1 01 01 |

Table 586 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 02 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E1 03 C1 01 01 |

Table 587 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 02 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E1 03 C1 01 01 |

##### Property 1.2.1.1.1.2 Application Selection Behavior (Contactless Only)

Table 588 - Property 1.2.1.1.1.2 Application Selection Behavior
(Contactless Only)Application Selection Behavior

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.1.2 / 0x010201010102</td>
</tr>
<tr>
<td>Name</td>
<td>Application Selection Behavior</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to set the device’s application
selection behavior for payment brand selection.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 –Card Preference.</p>
<p>The device automatically chooses the application that is mutually
supported by the card and the terminal, based on the priority order
specified by the card. This is the default and is standard EMV
transaction flow behavior.</p>
<p>0x01 – Reserved</p>
<p>0x02 – Reserved</p>
<p>0x03 – Enhanced Prompt Cardholder.</p>
<p>The device sends the host <strong>Notification 0x1803 – 02 02 00
00</strong> (Display Cardholder, Data Attached, Reserved) to request
that the cardholder select from a list of available applications. Each
application may include additional tags such as - priority indicator,
Issuer Country Code and Issuer Identification Number. After the
cardholder selects an application, the host passes the selection to the
device using <strong>Command 0x1802 - Report Cardholder
Selection</strong> to device to return the cardholder’s selection to the
device.</p>
<p>Note that if the device is configured to use this option, the
cardholder must hold the card or contactless payment device in contact
with the device for until cardholder application selection is complete,
otherwise the device will report the transaction failed. For this
reason, MagTek does not recommend using this setting.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00 – Card Preference</td>
</tr>
</tbody>
</table>

Table 589 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02010101 8902 C200 |

Table 590 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 10 D1 01 85 01 01 87 04 02 01 01 01 89 03 C2 01 00 |

Table 591 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870402010101 8903 C20103 |

Table 592 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 02 01 01 01 89 03 C2 01 03 |

##### Property 1.2.1.1.2.1 Signature Capture Control

Table 593 - Property 1.2.1.1.2.1 Signature Capture Control

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.2.1 / 0x010201010201</td>
</tr>
<tr>
<td>Name</td>
<td>Signature Capture Control</td>
</tr>
<tr>
<td>Description</td>
<td>The host can use this property to change whether the device
automatically prompts the cardholder for a signature when running
<strong>Command 0x1001 - Start Transaction</strong>, or leaves the
triggering of signature capture prompts to the host.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Device-driven Signature Capture</p>
<p>0x01 = Host-driven Signature Capture</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 594 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 04 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E2 02 C1 00 |

Table 595 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 04 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C1 01 01 |

Table 596 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 02 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C1 01 01 |

Table 597 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 02 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C1 01 01 |

##### Property 1.2.1.1.2.2 Include Signature Data in EMV Batch Data (Touch Only)

Table 598 - Property 1.2.1.1.2.2 Include Signature Data in EMV Batch
Data (Touch Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.2.2 / 0x010201010202</td>
</tr>
<tr>
<td>Name</td>
<td>Include Signature Data in EMV Batch Data</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine whether to include
signature capture coordinate data in TLV data object DFDF3E when it
returns <strong>EMV Batch Data Type</strong> while running
<strong>Command 0x1001 - Start Transaction</strong>.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Include signature data in <strong>EMV Batch Data
Type</strong></p>
<p>0x01 = RESERVED. Make signature data available as file. Use
<strong>Command 0xD821 - Start Get File from Device</strong> to request
file type <strong>Signature Capture File</strong> to retrieve the data
as a <strong>Signature Capture File Type</strong>.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 599 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 04 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E2 02 C2 00 |

Table 600 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 04 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C2 01 01 |

Table 601 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 02 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C2 01 01 |

Table 602 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 02 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C2 01 01 |

##### Property 1.2.1.1.2.3 Signature Timing Window (Touch Only)

Table 603 - Property 1.2.1.1.2.3 Signature Timing Window (Touch Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.2.3 / 0x010201010203</td>
</tr>
<tr>
<td>Name</td>
<td>Signature Timing Window</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine how long to wait, in
seconds, for <strong>Command 0x1801 - Request Cardholder
Signature</strong> while running <strong>Command 0x1001 - Start
Transaction</strong>.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = No Wait Time. If the device uses this setting, the host
must wait at least one second after receiving <strong>Notification
0x0105 - Transaction Operation Complete</strong> before performing any
other operations.</p>
<p>0x01..0xFF = Wait the Specified Number of Seconds</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x01 (second)</td>
</tr>
</tbody>
</table>

Table 604 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 04 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E2 02 C3 00 |

Table 605 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 04 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C3 01 03 |

Table 606 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 02 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C3 01 01 |

Table 607 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 02 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E2 03 C3 01 01 |

##### Property 1.2.1.1.3.1 Contactless Low Power Card Detect (Contactless Only)

Table 608 - Property 1.2.1.1.3.1 Contactless Low Power Card Detect
(Contactless Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.3.1 / 0x0102010100301</td>
</tr>
<tr>
<td>Name</td>
<td>Contactless Low Power Card Detect</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to enable/disable contactless low
power card detect (Proximity Detection Mode). When disabled, device will
read a contactless card as soon as the card is detected. If enabled,
device will track and delay reading a contactless card, allowing user to
use Contact or MSR card slots.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Disable</p>
<p>0x01 = Enable</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00 - Disabled</td>
</tr>
</tbody>
</table>

Table 609 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 01 84 0F D1 01 85 01 01 87 04 02 01 01 03 89 02 C1 00 |

Table 610 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 10 D1 01 85 01 01 87 04 02 01 01 03 89 03 C1 01 00 |

Table 611 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 10 D1 11 85 01 01 87 04 02 01 01 03 89 03 C1 01 00 |

Table 612 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 02 01 01 03 89 03 C1 01 00 |

##### Property 1.2.1.1.4.1 MIFARE Ultralight C 2keys3DES

Table 613 - Property 1.2.1.1.4.1 MIFARE Ultralight C 2keys3DES

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.4.1 / 0x0102010100401</td>
</tr>
<tr>
<td>Name</td>
<td>MIFARE Ultralight C 2keys3DES</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set 16-byte of the 2keys 3DES
for MIFARE Ultralight C authentication.</p>
<p>On an example of Key1 = 0001020304050607h and Key2 =
08090A0B0C0D0E0Fh, the setting should be
000102030405060708090A0B0C0D0E0F</p>
<p>For security, the Get request for this property will always return
3-MSB of KCV.</p>
<p>This key will be encrypted and stored in KPM.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td>49454D4B 41455242 214E4143 554F5946</td>
</tr>
</tbody>
</table>

Table 614 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 C1 00 |

Table 615 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 1D D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0D E2 0B E1 09 E1 07 E4 05 C1 03 29 07 96 |

Table 616 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C1 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

Table 617 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C1 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

##### Property 1.2.1.1.4.2 MIFARE Ultralight AES DataProtKey.

Table 618 - Property 1.2.1.1.4.2 MIFARE Ultralight AES DataProtKey.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.4.2 / 0x0102010100402</td>
</tr>
<tr>
<td>Name</td>
<td>MIFARE Ultralight AES DataProtKey.</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set 16-byte of the
AES_DataProtKey for MIFARE Ultralight AES authentication.</p>
<p>On an example of ASE Key = 000102030405060708090A0B0C0D0E0Fh, the
setting should be 000102030405060708090A0B0C0D0E0F</p>
<p>For security, the Get request for this property will always return
4-MSB of KCV.</p>
<p>This key will be encrypted and stored in KPM.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td>00000000 00000000 00000000 00000000</td>
</tr>
</tbody>
</table>

Table 619 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 C2 00 |

Table 620 - Get Response Example

| Example (Hex) |
|----|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406C204763CBCDE |

Table 621 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C2 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

Table 622 - Set Response Example

| Example (Hex) |
|----|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412C210000102030405060708090A0B0C0D0E0F |

##### Property 1.2.1.1.4.3 MIFARE Ultralight AES UIDRetrKey.

Table 623 - Property 1.2.1.1.4.3 MIFARE Ultralight AES UIDRetrKey.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.4.3 / 0x0102010100403</td>
</tr>
<tr>
<td>Name</td>
<td>MIFARE Ultralight AES UIDRetrKey.</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set 16-byte of the AES
UIDRetrKey for MIFARE Ultralight AES authentication.</p>
<p>On an example of the ASE Key = 000102030405060708090A0B0C0D0E0Fh, the
setting should be 000102030405060708090A0B0C0D0E0F</p>
<p>For security, the Get request for this property will always return
4-MSB of KCV.</p>
<p>This key will be encrypted and stored in KPM.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td>00000000 00000000 00000000 00000000</td>
</tr>
</tbody>
</table>

Table 624 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 C3 00 |

Table 625 - Get Response Example

| Example (Hex) |
|----|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406C304B548CFB4 |

Table 626 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C3 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

Table 627 - Set Response Example

| Example (Hex) |
|----|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412C310000102030405060708090A0B0C0D0E0F |

##### Property 1.2.1.1.4.4 MIFARE Ultralight AES OriginalityKey.

Table 628 - Property 1.2.1.1.4.4 MIFARE Ultralight AES OriginalityKey.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.4.4 / 0x0102010100404</td>
</tr>
<tr>
<td>Name</td>
<td>MIFARE Ultralight AES OriginalityKey.</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set 16-byte of the AES
OriginalityKey for MIFARE Ultralight AES.</p>
<p>On an example of the ASE Key = 000102030405060708090A0B0C0D0E0Fh, the
setting should be 000102030405060708090A0B0C0D0E0F</p>
<p>For security, the Get request for this property will always return
4-MSB of KCV.</p>
<p>This key will be encrypted and stored in KPM.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td>00000000 00000000 00000000 00000000</td>
</tr>
</tbody>
</table>

Table 629 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 C4 00 |

Table 630 - Get Response Example

| Example (Hex) |
|----|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406C404763CBCDE |

Table 631 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C4 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

Table 632 - Set Response Example

| Example (Hex) |
|----|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412C410000102030405060708090A0B0C0D0E0F |

##### Property 1.2.1.1.4.5 MIFARE Plus AES_Key1.

Table 633 - Property 1.2.1.1.4.5 MIFARE Plus AES_Key1.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.4.5 / 0x0102010100405</td>
</tr>
<tr>
<td>Name</td>
<td>MIFARE Plus AES_Key1.</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set 16-byte of the AES_Key1 for
MIFARE Plus.</p>
<p>On example of the ASE Key = 000102030405060708090A0B0C0D0E0Fh, the
setting should be 000102030405060708090A0B0C0D0E0F</p>
<p>For security, the Get request for this property will always return
4-MSB of KCV.</p>
<p>This key will be encrypted and stored in KPM.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td>00000000 00000000 00000000 00000000</td>
</tr>
</tbody>
</table>

Table 634 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 C5 00 |

Table 635 - Get Response Example

| Example (Hex) |
|----|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406C504763CBCDE |

Table 636 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C5 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

Table 637 - Set Response Example

| Example (Hex) |
|----|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412C510000102030405060708090A0B0C0D0E0F |

##### Property 1.2.1.1.4.6 MIFARE Plus AES_Key2.

Table 638 - Property 1.2.1.1.4.6 MIFARE Plus AES_Key2.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.4.6 / 0x0102010100406</td>
</tr>
<tr>
<td>Name</td>
<td>MIFARE Plus AES_Key2.</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set 16-byte of the AES_Key2 for
MIFARE Plus.</p>
<p>On example of the ASE Key = 000102030405060708090A0B0C0D0E0Fh, the
setting should be 000102030405060708090A0B0C0D0E0F</p>
<p>For security, the Get request for this property will always return
4-MSB of KCV.</p>
<p>This key will be encrypted and stored in KPM.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td>00000000 00000000 00000000 00000000</td>
</tr>
</tbody>
</table>

Table 639 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 C6 00 |

Table 640 - Get Response Example

| Example (Hex) |
|----|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406C604763CBCDE |

Table 641 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C6 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

Table 642 - Set Response Example

| Example (Hex) |
|----|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412C610000102030405060708090A0B0C0D0E0F |

##### Property 1.2.1.1.4.7 MIFARE Plus AES_Key3.

Table 643 - Property 1.2.1.1.4.7 MIFARE Plus AES_Key3.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.4.7 / 0x0102010100407</td>
</tr>
<tr>
<td>Name</td>
<td>MIFARE Plus AES_Key3.</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set 16-byte of the AES_Key3 for
MIFARE Plus.</p>
<p>On example of the ASE Key = 000102030405060708090A0B0C0D0E0Fh, the
setting should be 000102030405060708090A0B0C0D0E0F</p>
<p>For security, the Get request for this property will always return
4-MSB of KCV.</p>
<p>This key will be encrypted and stored in KPM.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td>00000000 00000000 00000000 00000000</td>
</tr>
</tbody>
</table>

Table 644 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 C7 00 |

Table 645 - Get Response Example

| Example (Hex) |
|----|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406C704763CBCDE |

Table 646 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C7 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

Table 647 - Set Response Example

| Example (Hex) |
|----|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412C710000102030405060708090A0B0C0D0E0F |

##### Property 1.2.1.1.4.8 MIFARE Plus AES_Key4.

Table 648 - Property 1.2.1.1.4.8 MIFARE Plus AES_Key4.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.4.8 / 0x0102010100408</td>
</tr>
<tr>
<td>Name</td>
<td>MIFARE Plus AES_Key4.</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set 16-byte of the AES_Key4 for
MIFARE Plus.</p>
<p>On example of the ASE Key = 000102030405060708090A0B0C0D0E0Fh, the
setting should be 000102030405060708090A0B0C0D0E0F</p>
<p>For security, the Get request for this property will always return
4-MSB of KCV.</p>
<p>This key will be encrypted and stored in KPM.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td>00000000 00000000 00000000 00000000</td>
</tr>
</tbody>
</table>

Table 649 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 C8 00 |

Table 650 - Get Response Example

| Example (Hex) |
|----|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406C804763CBCDE |

Table 651 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C8 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

Table 652 - Set Response Example

| Example (Hex) |
|----|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412C810000102030405060708090A0B0C0D0E0F |

##### Property 1.2.1.1.4.9 MIFARE Plus AES_Key5.

Table 653 - Property 1.2.1.1.4.9 MIFARE Plus AES_Key5.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.4.9 / 0x0102010100409</td>
</tr>
<tr>
<td>Name</td>
<td>MIFARE Plus AES_Key5.</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set 16-byte of the AES_Key5 for
MIFARE Plus.</p>
<p>On example of the ASE Key = 000102030405060708090A0B0C0D0E0Fh, the
setting should be 000102030405060708090A0B0C0D0E0F</p>
<p>For security, the Get request for this property will always return
4-MSB of KCV.</p>
<p>This key will be encrypted and stored in KPM.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td>00000000 00000000 00000000 00000000</td>
</tr>
</tbody>
</table>

Table 654 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 C9 00 |

Table 655 - Get Response Example

| Example (Hex) |
|----|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406C904763CBCDE |

Table 656 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C9 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

Table 657 - Set Response Example

| Example (Hex) |
|----|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412C910000102030405060708090A0B0C0D0E0F |

##### Property 1.2.1.1.4.A MIFARE Plus AES_Key6.

Table 658 - Property 1.2.1.1.4.A MIFARE Plus AES_Key6.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.4.A / 0x010201010040A</td>
</tr>
<tr>
<td>Name</td>
<td>MIFARE Plus AES_Key6.</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set 16-byte of the AES_Key6 for
MIFARE Plus.</p>
<p>On example of the ASE Key = 000102030405060708090A0B0C0D0E0Fh, the
setting should be 000102030405060708090A0B0C0D0E0F</p>
<p>For security, the Get request for this property will always return
4-MSB of KCV.</p>
<p>This key will be encrypted and stored in KPM.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td>00000000 00000000 00000000 00000000</td>
</tr>
</tbody>
</table>

Table 659 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 CA 00 |

Table 660 - Get Response Example

| Example (Hex) |
|----|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406CA04763CBCDE |

Table 661 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 CA 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

Table 662 - Set Response Example

| Example (Hex) |
|----|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412CA10000102030405060708090A0B0C0D0E0F |

##### Property 1.2.1.1.5.1 MCE Mode Setting

Table 663 - Property 1.2.1.1.5.1 MCE Mode Setting

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.1.1.5.1 / 0x0102010100501</td>
</tr>
<tr>
<td>Name</td>
<td>MCE Mode Setting (MCE: Manual Card Entry)</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine how to present a sequence
of pages to the host, prompting the cardholder or operator to enter the
specified sequence of values.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Card Number, Expiration Date, CVV/CVC/Card ID</p>
<p>0x01 = Card Number, Expiration Date</p>
<p>0x02 = Card Number, CVV/CVC/Card ID</p>
<p>0x03 = Card Number</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 664 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E5 02 C1 00 |

Table 665 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E5 03 C1 01 03 |

Table 666 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E5 03 C1 01 03 |

Table 667 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E1 07 E1 05 E5 03 C1 01 03 |

#### Property Subgroup 1.2.2.1.nn WLAN Settings (WLAN Only)

##### Property 1.2.2.1.1.1 SSID

Table 668 - Property 1.2.2.1.1.1 SSID

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.1 / 0x010202010101 |
| Name | SSID |
| Description | The device uses this property to set SSID for WLAN settings. If the SSID is shorter than 32 bytes, all remaining bytes after the SSID should be set to zeros. |
| Securing Key | None |
| Min. Len (b) | 32 |
| Max. Len (b) | 32 |
| Data Type | Binary |
| Valid Values |  |
| Default | None |

Table 669 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040122D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C100 |

Table 670 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048222D101 820400000000 8482003AD101 81072B06010401F609 850101 892AE228E226E124E122C1204D79535349440000000000000000000000000000000000000000000000000000 |

Table 671 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040121D111 843AD111 81072B06010401F609 850101 892AE228E226E124E122C120 4D79535349440000000000000000000000000000000000000000000000000000 |

Table 672 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048221D111 820400000000 8482003AD111 81072B06010401F609 850101 892AE228E226E124E122C1204D79535349440000000000000000000000000000000000000000000000000000 |

##### Property 1.2.2.1.1.2 Password

Table 673 - Property 1.2.2.1.1.2 Password

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.1.2 / 0x010202010102</td>
</tr>
<tr>
<td>Name</td>
<td>Password</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set password for WLAN settings.
If the password is shorter than 63 bytes, all remaining bytes after the
password should be set to zeros.</p>
<p>For EAP-PEAP authentication, the maximum length of password is 32
bytes. The real password has to be &lt;= 32 bytes, all bytes after the
desired password must be set to zeroes.</p>
<p>For security, the Get request for this property will always return a
value with 63 zeroes, so you can only set the password and not get
it.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>63</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>63</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 674 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040110D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C200 |

Table 675 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104820CD101 820400000000 84820059D101 81072B06010401F609 850101 8949E247E245E143E141C23F00000000 |

Table 676 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040112D111 8459D111 81072B06010401F609 850101 8949E247E245E143E141C23F546F744031386342 |

Table 677 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048212D111 820400000000 84820059D111 81072B06010401F609 850101 8949E247E245E143E141C23F546F744031386342 |

##### Property 1.2.2.1.1.3 Security Mode

Table 678 - Property 1.2.2.1.1.3 Security Mode

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.1.3 / 0x010202010103</td>
</tr>
<tr>
<td>Name</td>
<td>Security Mode</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to determine the authentication method
to be used to connect to an WiFi Access Point.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = PSK (Personal) Mode, requires <strong>Property 1.2.2.1.1.2
Password</strong></p>
<p>0x01 = EAP-PEAP (Enterprise) Mode, requires <strong>Property
1.2.2.1.1.2 Password</strong>, <strong>Property 1.2.2.1.1.C
Username</strong></p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 679 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040103D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C300 |

Table 680 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048203D101 820400000000 8482001BD101 81072B06010401F609 850101 890BE209E207E105E103C30100 |

Table 681 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040104D111 841BD111 81072B06010401F609 850101 890BE209E207E105E103C30101 |

Table 682 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048204D111 820400000000 8482001BD111 81072B06010401F609 850101 890BE209E207E105E103C30101 |

##### Property 1.2.2.1.1.4 Static IP Address

Table 683 - Property 1.2.2.1.1.4 Static IP Address

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.4 / 0x010202010104 |
| Name | Static_IP_Address |
| Description | The device uses this property as its IP address in web socket mode if **Property 1.2.2.1.1.5 Use DHCP** is set to 0000 (Static IP mode). |
| Securing Key | None |
| Min. Len (b) | 4 |
| Max. Len (b) | 4 |
| Data Type | IP4 Format/quad decimal (x.x.x.x) |
| Valid Values | 0.0.0.0 to 255.255.255 |
| Default | None |

Table 684 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040105D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C400 |

Table 685 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048205D101 820400000000 8482001ED101 81072B06010401F609 850101 890EE20CE20AE108E106C404C0A80177 |

Table 686 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040111D111 841ED111 81072B06010401F609 850101 890EE20CE20AE108E106C404C0A8016D |

Table 687 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048211D111 820400000000 8482001ED111 81072B06010401F609 850101 890EE20CE20AE108E106C404C0A8016D |

##### Property 1.2.2.1.1.5 Use DHCP

Table 688 - Property 1.2.2.1.1.5 Use DHCP

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.1.5 / 0x010202010105</td>
</tr>
<tr>
<td>Name</td>
<td>Use_DHCP</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if it gets its IP from
a DHCP server or uses a static IP.</p>
<p>0000—use static IP address;</p>
<p>othervalue—get IP address from DHCP server</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0000 to FFFF</td>
</tr>
<tr>
<td>Default</td>
<td>0001</td>
</tr>
</tbody>
</table>

Table 689 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040117D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C500 |

Table 690 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048217D101 820400000000 8482001ED101 81072B06010401F609 850101 890EE20CE20AE108E106C50400000001 |

Table 691 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040116D111 841ED111 81072B06010401F609 850101 890EE20CE20AE108E106C50400000001 |

Table 692 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048216D111 820400000000 8482001ED111 81072B06010401F609 850101 890EE20CE20AE108E106C50400000001 |

##### Property 1.2.2.1.1.6 Static IP Netmask

Table 693 - Property 1.2.2.1.1.6 Static IP Netmask

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.6 / 0x010202010106 |
| Name | Static_IP_Netmask |
| Description | The device uses this property as its network mask in web socket mode. |
| Securing Key | None |
| Min. Len (b) | 4 |
| Max. Len (b) | 4 |
| Data Type | IP4 Format/quad decimal (x.x.x.x) |
| Valid Values | 0.0.0.0 to 255.255.255.255 |
| Default | None |

Table 694 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040118D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C600 |

Table 695 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048218D101 820400000000 8482001ED101 81072B06010401F609 850101 890EE20CE20AE108E106C604FFFFFF00 |

Table 696 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040119D111 841ED111 81072B06010401F609 850101 890EE20CE20AE108E106C604FFFFFF00 |

Table 697 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048219D111 820400000000 8482001ED111 81072B06010401F609 850101 890EE20CE20AE108E106C604FFFFFF00 |

##### Property 1.2.2.1.1.7 Static IP Gateway

Table 698 - Property 1.2.2.1.1.7 Static IP Gateway

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.7 / 0x010202010107 |
| Name | Static_IP_Gateway |
| Description | The device uses this property as its network gateway IP address. |
| Securing Key | None |
| Min. Len (b) | 4 |
| Max. Len (b) | 4 |
| Data Type | IP4 Format/quad decimal (x.x.x.x) |
| Valid Values | 0.0.0.0 to 255.255.255.255 |
| Default | None |

Table 699 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104011AD101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C700 |

Table 700 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104821BD101 820400000000 8482001ED101 81072B06010401F609 850101 890EE20CE20AE108E106C704C0A801FE |

Table 701 - Set Request Example

| Example (Hex) |
|----|
| AA00 8104011CD111 841ED111 81072B06010401F609 850101 890EE20CE20AE108E106C704C0A801FE |

Table 702 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104821CD111 820400000000 8482001ED111 81072B06010401F609 850101 890EE20CE20AE108E106C704C0A801FE |

##### Property 1.2.2.1.1.8 Device Name

Table 703 - Property 1.2.2.1.1.8 Device Name

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.8 / 0x010202010108 |
| Name | Device Name |
| Description | The device uses this property to set Device Name for WLAN settings. Device Name is registered to the DNS which adds the domain name to create a hostname. Use Hostname to connect to device WebSocket. If the Device Name is shorter than 64 bytes, all remaining bytes after the Device Name should be set to zeros. |
| Securing Key | None |
| Min. Len (b) | 64 |
| Max. Len (b) | 64 |
| Data Type | Binary |
| Valid Values |  |
| Default | None |

Table 704 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C800 |

Table 705 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048228D101 820400000000 8482005AD101 81072B06010401F609 850101 894AE248E246E144E142C84064662D78787878787878000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 |

Table 706 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040127D111 845AD111 81072B06010401F609 850101 894AE248E246E144E142C840 64662D78787878787878000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 |

Table 707 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048227D111 820400000000 8482005AD111 81072B06010401F609 850101 894AE248E246E144E142C84064662D78787878787878000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 |

##### Property 1.2.2.1.1.9 Wireless Heartbeat Time

Table 708 - Property 1.2.2.1.1.9 Wireless Heartbeat Time

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.9 / 0x010202010109 |
| Name | Wireless Heartbeat Time |
| Description | The device uses this property to set Heartbeat Time for WLAN settings. Device will check the Websocket connection based on this timer setting. The unit is second. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0x00 to 0xFF |
| Default | 0x00 (disabled) |

Table 709 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104011AD101 841AD101 81072B06010401F609 850101 890AE208E206E104E102C900 |

Table 710 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104821AD101 820400000000 8482001BD101 81072B06010401F609 850101 890BE209E207E105E103C90100 |

Table 711 - Set Request Example

| Example (Hex) |
|----|
| AA00 8104011CD111 841BD111 81072B06010401F609 850101 890BE209E207E105E103C90120 |

Table 712 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104821CD111 820400000000 8482001BD111 81072B06010401F609 850101 890BE209E207E105E103C90120 |

##### Property 1.2.2.1.1.A Maximum Client Connections

Table 713 - Property 1.2.2.1.1.A Maximum Client Connections

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.1.A / 0x01020201010A</td>
</tr>
<tr>
<td>Name</td>
<td>Maximum Client Connections</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine how many clients it
will allow to connect to its WLAN WebSocket server at one time. Most use
cases will only want to allow one client at a time. If more than one
client is connected, all outgoing data from the device will be sent to
all clients. For example, all notifications and all command responses
will be sent to all clients. If more than one client is connected, any
client can send a command to the device at any time. Since having more
than one client send commands to the device at the same time can result
in command collisions and unexpected device behavior, it is recommended
that only one client be in charge of sending commands and that other
clients only listen to outgoing messages. A use case for allowing more
than once client may be to have a second client for diagnostic or
monitoring purposes.</p>
<p><strong>Property 2.1.2.5.6.4 Active Client Connections</strong> is
related.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x01 – 0x04</td>
</tr>
<tr>
<td>Default</td>
<td>0x01</td>
</tr>
</tbody>
</table>

Table 714 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020101 8902 CA00 |

Table 715 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020201018903CA0101 |

Table 716 - Set Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 8704 02020101 8903 CA0101 |

Table 717 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020201018903CA0101 |

##### Property 1.2.2.1.1.B Certificate Expiring Soon Notification Threshold

Table 718 - Property 1.2.2.1.1.B Certificate Expiring Soon Notification
Threshold

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.1.B / 0x01020201010B</td>
</tr>
<tr>
<td>Name</td>
<td>Certificate Expiring Soon Notification Threshold</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine how many days before a
certificate expires it should start notifying the host that it is about
to expire. If the value is set to 0, the notification will be
disabled.</p>
<p>The notification will only be sent if TLS is enabled, and the
notification will only be sent for they server certificate that the
device is configured to use. The notification will be sent every time
the first client connects to the device shortly after it connects.</p>
<p><strong>Notification 0x1001 - Device Information Update</strong>
category Key management, reason Certificate Expiring Soon is
related.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 – 0xFF</td>
</tr>
<tr>
<td>Default</td>
<td>0x1E (30 days)</td>
</tr>
</tbody>
</table>

Table 719 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020101 8902 CB00 |

Table 720 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020201018903CB011E |

Table 721 - Set Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 8704 02020101 8903 CB011E |

Table 722 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020201018903CB011E |

##### Property 1.2.2.1.1.C Username

Table 723 - Property 1.2.2.1.1.C Username

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.1.C / 0x01020201010C</td>
</tr>
<tr>
<td>Name</td>
<td>Username</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set up the Username for EAP-PEAP
authentication method which is used to connect to an WiFi Access Point.
Username is not used by</p>
<p>PSK authentication method.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>N/A</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>32</td>
</tr>
<tr>
<td>Data Type</td>
<td>ASCII String</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Example: joe@MagTek.com</td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 724 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104010DD101 841AD101 81072B06010401F609 850101 890AE208E206E104E102CC00 |

Table 725 - Get Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104820DD101 820400000000 8482003AD101 81072B06010401F609
850101</p>
<p>892AE228E226E124E122CC
206A6F65406D616774656B2E636F6D00000000000000</p>
<p>0000000000000000000000</p></td>
</tr>
</tbody>
</table>

Table 726 - Set Request Example

| Example (Hex) |
|----|
| AA00 8104010ED111 843AD111 81072B06010401F609 850101 892AE228E226E124E122CC 206A6F65406D616774656B2E636F6D000000000000000000 |

Table 727 - Set Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104820ED111 820400000000 8482003AD111 81072B06010401F609
850101</p>
<p>892AE228E226E124E122CC 206A6F65406D616774656B2E636F6D</p>
<p>000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

##### Property 1.2.2.1.1.D SoftAP IP Address

Table 728 - Property 1.2.2.1.1.D SoftAP IP Address

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.D / 0x01020201010D |
| Name | SoftAP_IP_Address |
| Description | This OID is used to store a soft AP IP address. When a device starts AP mode, it reads this value as its IP address. A new value will be stored with this OID if a user modifies the soft AP IP address. |
| Securing Key | None |
| Min. Len (b) | 4 |
| Max. Len (b) | 4 |
| Data Type | IP4 Format/quad decimal (x.x.x.x) |
| Valid Values | 0.0.0.0 to 255.255.255 |
| Default | 192.168.0.1 |

Table 729 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040103D101 841AD101 81072B06010401F609 850101 890AE208E206E104E102CD00 |

Table 730 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048203D101 820400000000 8482001ED101 81072B06010401F609 850101 890EE20CE20AE108E106CD0400000000 |

Table 731 - Set Request Example

| Example (Hex) |
|----|
| AA00 81040107D111 841ED111 81072B06010401F609 850101 890EE20CE20AE108E106CD04C0A80177 |

Table 732 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048207D111 820400000000 8482001ED111 81072B06010401F609 850101 890EE20CE20AE108E106CD04C0A80177 |

##### Property 1.2.2.1.1.E Web App Enabled (MAGTEK INTERNAL ONLY FOR NOW)

Table 733 - Property 1.2.2.1.1.E Web App Enabled (MAGTEK INTERNAL ONLY
FOR NOW)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.1.E / 0x01020201010E</td>
</tr>
<tr>
<td>Name</td>
<td>Web App Enabled</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if its web application
is enabled. The web app can be used to send commands to the device over
the WLAN interface using a web browser. The web app appears as a web
page on a browser.</p>
<p>The URL and port used to access the web page depend on how the device
is configured. The default port is 26 (not 80 or 443). See
<strong>Property 1.2.2.1.1.F Web App Port</strong> for changing the web
app port. The security required to access the web page depends on if the
device has been configured to use TLS or not.</p>
<p>https://df-b62b3aa.lan:26 and https://192.168.86.31:26 are examples
of how to access the web page on a device that has TLS enabled.
http://df-b62b3aa.lan:26 and http://192.168.86.31:26 are examples of how
to access the web page on a device that does not have TLS enabled.</p>
<p>If this property is changed, the device must be or power cycled or
reset before the change will take effect.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 (not enabled), 0x01 (enabled)</td>
</tr>
<tr>
<td>Default</td>
<td>0x00 (not enabled)</td>
</tr>
</tbody>
</table>

Table 734 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020101 8902 CE00 |

Table 735 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020201018903CE0101 |

Table 736 - Set Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 8704 02020101 8903 CE0101 |

Table 737 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020201018903CE0101 |

##### Property 1.2.2.1.1.F Web App Port (MAGTEK INTERNAL ONLY FOR NOW)

Table 738 - Property 1.2.2.1.1.F Web App Port (MAGTEK INTERNAL ONLY FOR
NOW)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.1.F / 0x01020201010F</td>
</tr>
<tr>
<td>Name</td>
<td>Web App Port</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine which port the web app
can be accessed on. See <strong>Web App Enabled</strong> for more
details about the web app.</p>
<p>The device does not support having both WLAN web socket and the web
app accessible on the same port. By default, the device will use port
443 for the WLAN web socket port when TLS is enabled and port 80 when
TLS is not enabled. If the web app port is set to the same port
configured for the WLAN web socket port, then the web app will not be
accessible.</p>
<p>If this property is changed, the device must be power cycled or reset
before the change will take effect.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 0x00 (0) - 0xFF 0xFF (65535) MSB first</td>
</tr>
<tr>
<td>Default</td>
<td>0x00 0x1A (26)</td>
</tr>
</tbody>
</table>

Table 739 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020101 8902 CF00 |

Table 740 - Get Response Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D10182040000000084820011D1018501018704020201018904CF02001A |

Table 741 - Set Request Example

| Example (Hex)                                                 |
|---------------------------------------------------------------|
| AA00 81040155D111 8411 D111 850101 870402020101 8904 CF02001A |

Table 742 - Set Response Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D11182040000000084820011D1118501018704020201018904CF02001A |

##### Property 1.2.2.1.1.10 Firmware Authentication Hash (MAGTEK INTERNAL ONLY)

Table 743 - Property 1.2.2.1.1.10 Firmware Authentication Hash (MAGTEK
INTERNAL ONLY)

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.1.10 / 0x010202010110 |
| Name | Firmware Authentication Hash |
| Description | The device uses this property to get and set the WLAN firmware hash. Only required when WLAN firmware is preloaded using JTAG during production. Allows MFG CFG to validate WLAN firmware is loaded properly. |
| Securing Key | None |
| Min. Len (b) | 44 |
| Max. Len (b) | 44 |
| Data Type | Binary |
| Valid Values | FW_adr\[4\], FW_len\[4\], hash_len\[4\], hash\[32\] |
| Default | None |

Table 744 - Get Request Example

| Example (Hex)                                          |
|--------------------------------------------------------|
| AA00 81040155D101 840FD101 850101870402020101 8902D000 |

Table 745 - Get Response Example

| Example (Hex) |
|----|
| AA0081048255D1018204000000008482003BD101850101870402020101892ED02C0000C000000F40000000002013160562C59F77F9EAC8EEA603BCC6C7E0DCED13B640C14BF550AB8520FAF758 |

Table 746 - Set Request Example

| Example (Hex) |
|----|
| AA0081040155D111843BD111850101870402020101892ED02C0000C000000F4000000000201F1E1D1C1B1A191817161514131211100F0E0D0C0B0A09080706050403020100 |

Table 8.3‑75 - Set Response Example

| Example (Hex) |
|----|
| AA0081048255D1118204000000008482003BD111850101870402020101892ED02C0000C000000F4000000000201F1E1D1C1B1A191817161514131211100F0E0D0C0B0A09080706050403020100 |

##### Property 1.2.2.1.1.11 WLAN Protocol

<table>
<caption><p>Table 747 - Property 1.2.2.1.2.11 WLAN
Protocol</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.1.11 / 0x010202010111</td>
</tr>
<tr>
<td>Name</td>
<td>WLAN Protocol</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set the WLAN Protocol.</p>
<p>0x00 = MQTT</p>
<p>0x01 = RFU</p>
<p>0x02 = WebSocket Server</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 – 0x02</td>
</tr>
<tr>
<td>Default</td>
<td>0x02</td>
</tr>
</tbody>
</table>

| Example (Hex)                                              |
|------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 870402020101 8902 D100 |

Table 748 - Get Request Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020201018903D10102 |

Table 749 - Get Response Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870402020101 8903 D101 02 |

Table 750 - Set Request Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020201018903D10102 |

Table 751 -Set Response Example

##### Property 1.2.2.1.2.1 MQTT Broker Address

<table>
<caption><p>Table 752 - Property 1.2.2.1.2.1 MQTT Broker
Address</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.2.1 / 0x010202010201</td>
</tr>
<tr>
<td>Name</td>
<td>MQTT Broker Address</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to connect to broker on network.
Address can be an URL or IP address.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>N/A</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>64</td>
</tr>
<tr>
<td>Data Type</td>
<td>ASCII String with no spaces</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Any string</p>
<p>Example: test.mosquitto.org</p></td>
</tr>
<tr>
<td>Default</td>
<td>test.mosquitto.org</td>
</tr>
</tbody>
</table>

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 8704 02020102 8902 C100 |

Table 753 -Get Request Example

<table>
<caption><p>Table 754 -Get Response Example</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048255D1018204000000008482004FD1018501018704020201028942C140</p>
<p>746573742E6D6F7371756974746F2E6F726700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

| Example (Hex) |
|----|
| AA00 81040155D111 844F D111 850101 870402020102 8942 C140 746573742E6D6F7371756974746F2E6F 72670000000000000000000000000000 00000000000000000000000000000000 00000000000000000000000000000000 |

Table 755 -Set Request Example

<table>
<caption><p>Table 756 -Set Response Example</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048255D1118204000000008482004FD1118501018704020201028942C140</p>
<p>746573742E6D6F7371756974746F2E6F726700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

##### Property 1.2.2.1.2.2 MQTT Port

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.2.2 / 0x010202010202 |
| Name | MQTT Port |
| Description | The device uses this property to connect to broker on this network port. MQTT Port addresses are normally 8883 for secure (Recommended), 1883 for unsecure. |
| Securing Key | None |
| Min. Len (b) | 2 |
| Max. Len (b) | 2 |
| Data Type | Binary |
| Valid Values | 0x00 0x00 (0) – 0xFF 0xFF (65535) MSB first |
| Default | 8883 |

Table 757 -Property 1.2.2.1.2.2 MQTT Port

| Example (Hex)                                              |
|------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 870402020102 8902 C200 |

Table 758 -Get Request Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D10182040000000084820011D1018501018704020201028904C20222B3 |

Table 759 -Get Response Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA00 81040155D111 8411 D111 850101 870402020102 8904 C202 22B3 |

Table 760 -Set Request Example

| Example (Hex)                                                           |
|-------------------------------------------------------------------------|
| AA0081048255D11182040000000084820011D1118501018704020201028904C202 22B3 |

Table 761 -Set Response Example

##### Property 1.2.2.1.2.3 MQTT QoS Quality of Service

<table>
<caption><p>Table 762 -Property 1.2.2.1.2.3 MQTT QoS Quality of
Service</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.2.3 / 0x010202010203</td>
</tr>
<tr>
<td>Name</td>
<td>MQTT QoS</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set the MQTT QoS.</p>
<p>0x00 = At most once (Recomnended)</p>
<p>0x01 = At least once</p>
<p>0x02 = Exactly once</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 – 0x02</td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

| Example (Hex)                                              |
|------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 870402020102 8902 C300 |

Table 763 -Get Request Example

| Example (Hex)                                                         |
|-----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020201028903C301 00 |

Table 764 -Get Response Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870402020102 8903C301 00 |

Table 765 -Set Request Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020201028903C30100 |

Table 766 -Set Response Example

##### Property 1.2.2.1.2.4 MQTT Subscribe Topic

<table>
<caption><p>Table 767 -Property 1.2.2.1.2.4 MQTT Subscribe
Topic</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.2.4 / 0x010202010204</td>
</tr>
<tr>
<td>Name</td>
<td>MQTT Subscribe Topic</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to set the MQTT Subscribe Topic for
receiving MMS message payloads</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>N/A</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>64</td>
</tr>
<tr>
<td>Data Type</td>
<td>ASCII String with no spaces</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Any string</p>
<p>Example: <strong>MagTek/Device/DynaFlexIIPED/B62B3C6</strong><em>[MMS
Message Payload]</em></p></td>
</tr>
<tr>
<td>Default</td>
<td><p>MagTek/Device/[DevModelName]/[DevSN]</p>
<p>[DevModelName] = DynaFlexIIPED, Device Model Name with no spaces.</p>
<p>[DevSN] = Device Serial #</p></td>
</tr>
</tbody>
</table>

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 8704 02020102 8902 C400 |

Table 768 -Get Request Example

<table>
<caption><p>Table 769 -Get Response Example</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048255D1018204000000008482004FD1018501018704020201028942C440</p>
<p>4D616754656B2F4465766963652F44796E61466C657849495045442F423632423343360000000000000000000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

| Example (Hex) |
|----|
| AA00 81040155D111 844F D111 850101 870402020102 8942 C440 4D616754656B2F4465766963652F4479 6E61466C657849495045442F42363242 33433600000000000000000000000000 00000000000000000000000000000000 |

Table 770 -Set Request Example

<table>
<caption><p>Table 771 - Set Response Example</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048255D1118204000000008482004FD1118501018704020201028942C440</p>
<p>4D616754656B2F4465766963652F44796E61466C657849495045442F423632423343360000000000000000000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

##### Property 1.2.2.1.2.5 MQTT Publish Topic

<table>
<caption><p>Table 772 -Property 1.2.2.1.2.5 MQTT Publish
Topic</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.2.5 / 0x010202010205</td>
</tr>
<tr>
<td>Name</td>
<td>MQTT Publish Topic</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set the MQTT Publish Topic for
sending MMS message payloads.</p>
<p>Device will add append the string <em>/MMSMessage</em> to the MQTT
Publish Topic string set in this property.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>N/A</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>64</td>
</tr>
<tr>
<td>Data Type</td>
<td>ASCII String with no spaces</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Any string</p>
<p>Example:
<strong>MagTek/Server/DynaFlexIIPED/B62B3C6</strong><em>/MMSMessage[MMS
Message Payload]</em></p></td>
</tr>
<tr>
<td>Default</td>
<td><p>MagTek/Server/[DevModelName]/[DevSN]</p>
<p>[DevModelName] = DynaFlexIIPED, Device Model Name with no spaces.</p>
<p>[DevSN] = Device Serial #</p></td>
</tr>
</tbody>
</table>

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 8704 02020102 8902 C500 |

Table 773 -Get Request Example

<table>
<caption><p>Table 774 -Get Response Example</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048255D1018204000000008482004FD1018501018704020201028942C540</p>
<p>4D616754656B2F5365727665722F44796E61466C657849495045442F423632423343360000000000000000000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

| Example (Hex) |
|----|
| AA00 81040155D111 844F D111 850101 870402020102 8942 C540 4D616754656B2F5365727665722F4479 6E61466C657849495045442F42363242 33433600000000000000000000000000 00000000000000000000000000000000 |

Table 775 -Set Request Example

<table>
<caption><p>Table 776 -Set Response Example</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048255D1118204000000008482004FD1118501018704020201028942C540</p>
<p>4D616754656B2F5365727665722F44796E61466C657849495045442F423632423343360000000000000000000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

##### Property 1.2.2.1.2.6 MQTT Client ID

<table>
<caption><p>Table 777 -Property 1.2.2.1.2.6 MQTT Client IDClient
ID</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.2.6 / 0x010202010206</td>
</tr>
<tr>
<td>Name</td>
<td>MQTT Client ID</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to set the MQTT Client ID.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>N/A</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>32</td>
</tr>
<tr>
<td>Data Type</td>
<td>ASCII String with no spaces</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Any string</p>
<p>Example: MagTek_Device-B62B3C6</p></td>
</tr>
<tr>
<td>Default</td>
<td><p>MagTek_Device-[DevSN]</p>
<p>[DevSN] = Device Serial #</p></td>
</tr>
</tbody>
</table>

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 8704 02020102 8902 C600 |

Table 778 -Get Request Example

<table>
<caption><p>Table 779 -Get Response Example</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048255D1018204000000008482002FD1018501018704020201028922C620</p>
<p>4D616754656B5F4465766963652D423632423343360000000000000000000000</p></td>
</tr>
</tbody>
</table>

| Example (Hex) |
|----|
| AA00 81040155D111 842F D111 850101 870402020102 8922 C620 4D616754656B5F4465766963652D4236 32423343360000000000000000000000 |

Table 780 -Set Request Example

<table>
<caption><p>Table 781 - Set Response Example</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048255D1118204000000008482002FD1118501018704020201028922C620</p>
<p>4D616754656B5F4465766963652D423632423343360000000000000000000000</p></td>
</tr>
</tbody>
</table>

##### Property 1.2.2.1.2.7 MQTT Username

<table>
<caption><p>Table 782 - Property 1.2.2.1.2.7 MQTT
UsernameUsername</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.2.7 / 0x010202010207</td>
</tr>
<tr>
<td>Name</td>
<td>MQTT UserName</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to set the MQTT Username.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>N/A</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>32</td>
</tr>
<tr>
<td>Data Type</td>
<td>ASCII String with no spaces</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Any string</p>
<p>Example: magtek_testonly1</p></td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 8704 02020102 8902 C700 |

Table 783 - Get Request Example

<table>
<caption><p>Table 784 - Get Response Example</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048255D1018204000000008482002FD1018501018704020201028922C720</p>
<p>6D616774656B5F746573746F6E6C793100000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

| Example (Hex) |
|----|
| AA00 81040155D111 842F D111 850101 870402020102 8922 C720 6D616774656B5F746573746F6E6C7931 00000000000000000000000000000000 |

Table 785 - Set Request Example

<table>
<caption><p>Table 786 - Set Response Example</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048255D1118204000000008482002FD1118501018704020201028922C720</p>
<p>6D616774656B5F746573746F6E6C793100000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

##### Property 1.2.2.1.2.8 MQTT Password

<table>
<caption><p>Table 787 - Property 1.2.2.1.2.8 MQTT
PasswordPassword</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.2.8 / 0x010202010208</td>
</tr>
<tr>
<td>Name</td>
<td>MQTT Password</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to set the MQTT Password.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>N/A</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>32</td>
</tr>
<tr>
<td>Data Type</td>
<td>ASCII String with no spaces</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Any string</p>
<p>Example: emqx-tST1!</p></td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 8704 02020102 8902 C800 |

Table 788 -Get Request Example

<table>
<caption><p>Table 789 - Get Response Example</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048255D1018204000000008482002FD1018501018704020201028922C820</p>
<p>656D71782D745354312100000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

| Example (Hex) |
|----|
| AA00 81040155D111 842F D111 850101 870402020102 8922 C820 656d71782d7453543121000000000000 00000000000000000000000000000000 |

Table 790 - Set Request Example

<table>
<caption><p>Table 791 -Set Response Example</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048255D1118204000000008482002FD1118501018704020201028922C820</p>
<p>656D71782D745354312100000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

##### Property 1.2.2.1.2.8 MQTT Peer Common Name

<table>
<caption><p>Table 792 - Property 1.2.2.1.2.8 MQTT Peer Common NamePeer
Common Name</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.1.2.9 / 0x010202010209</td>
</tr>
<tr>
<td>Name</td>
<td>MQTT Peer Common Name</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to set the MQTT Peer Common Name. If
not set device will use Broker Address for server authentication.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>N/A</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>64</td>
</tr>
<tr>
<td>Data Type</td>
<td>ASCII String with no spaces</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Any string</p>
<p>Example: test.mosquitto.org</p></td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 8704 02020102 8902 C900 |

Table 793 - Get Request Example

<table>
<caption><p>Table 794 - Get Response Example</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048255D1018204000000008482004FD1018501018704020201028942C940</p>
<p>746573742E6D6F7371756974746F2E6F726700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</p></td>
</tr>
</tbody>
</table>

| Example (Hex) |
|----|
| AA00 81040155D111 844F D111 850101 870402020102 8942 C940 746573742E6D6F7371756974746F2E6F 72670000000000000000000000000000 00000000000000000000000000000000 00000000000000000000000000000000 |

Table 795 - Set Request Example

| Example (Hex) |
|----|
| AA0081048255D1118204000000008482004FD1118501018704020201028942C940746573742E6D6F7371756974746F2E6F726700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 |

Table 796 - Set Response Example

##### Property 1.2.2.1.2.A MQTT Keep Alive

| Property Description |  |
|----|----|
| Property OID | 1.2.2.1.2.A / 0x01020201020A |
| Name | MQTT Keep Alive |
| Description | The device uses this property to set the MQTT Keep Alive timing. Value is in seconds, used to guarantee the connection between device and MQTT broker remains active. A value of 0 disables Keep Alive monitoring. |
| Securing Key | None |
| Min. Len (b) | 2 |
| Max. Len (b) | 2 |
| Data Type | Binary |
| Valid Values | 0x00 0x00 (0) – 0xFF 0xFF (0 = Disabled, 1 🡪 65535 seconds) MSB first |
| Default | 300 seconds |

Table 797 - Property 1.2.2.1.2.A MQTT Keep Alive

| Example (Hex)                                              |
|------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 850101 870402020102 8902 CA00 |

Table 798 - Get Request Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D10182040000000084820011D1018501018704020201028904CA02012C |

Table 799 - Get Response Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA00 81040155D111 8411 D111 850101 870402020102 8904 CA02 012C |

Table 800 - Set Request Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D11182040000000084820011D1118501018704020201028904CA02012C |

Table 801 - Set Response Example

#### Property Subgroup 1.2.2.2.nn USB Settings (USB Only)

##### Property 1.2.2.2.1.1 Reduce Power During USB Suspend

Table 802 - Property 1.2.2.2.1.1 Reduce Power During USB Suspend

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.2.1.1 / 0x010202020101</td>
</tr>
<tr>
<td>Name</td>
<td>Reduce Power During USB Suspend</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine whether it should
reduce its power consumption when a USB host directs it to suspend. If
this property is set to Disabled, the device will not have a USB
compliant current draw when suspended, which, for example, allows it to
continue to turn on LEDs and the display if present.</p>
<p>To activate changes made to this property, the device must be reset
or power cycled.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Disabled</p>
<p>0x01 = Enabled</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x01</td>
</tr>
</tbody>
</table>

Table 803 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020201 8902 C100 |

Table 804 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020202018903C10101 |

Table 805 - Set Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 8704 02020201 8903 C10101 |

Table 806 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020202018903C10101 |

##### Property 1.2.2.2.1.2 USB Configuration Type

Table 807 - Property 1.2.2.2.1.2 USB Configuration Type

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.2.1.2 / 0x010202020102</td>
</tr>
<tr>
<td>Name</td>
<td>USB Configuration Type</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if it should behave as
a USB HID device or an USB iAP2 device. USB HID devices can communicate
with most hosts except for Apple hosts. USB iAP2 devices can communicate
to Apple hosts like iPads and iPhones. The behavior affects USB
enumeration and communications.</p>
<p>To activate changes made to this property, the device must be reset
or power cycled.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = HID only</p>
<p>0x01 = iAP2 only</p>
<p>0x02 = autodetect (iAP2 with HID fallback)</p>
<p>The autodetect option can allow a device to work with iAP2 hosts and
HID hosts. With this option, every time the device is attached to a USB
host it will first enumerate as an iAP2 device, if the device does not
receive an iAP2 initialization sequence response from the host within 2
seconds the device will perform a soft USB detach from the host and then
a soft USB attach and next enumerate as a USB HID device.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x02</td>
</tr>
</tbody>
</table>

Table 808 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020201 8902 C200 |

Table 809 - Get Response Example (HID only)

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020202018903C20100 |

Table 810 - Set Request Example (HID only)

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 8704 02020201 8903 C20100 |

Table 811 - Set Response Example (HID only)

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020202018903C20100 |

Table 812 - Set Request Example (iAP2 only)

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 8704 02020201 8903 C20101 |

Table 813 - Set Response Example (iAP2 only)

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020202018903C20101 |

Table 814 - Set Request Example (autodetect (iAP2 with HID fallback))

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 8704 02020201 8903 C20102 |

Table 815 - Set Response Example (autodetect (iAP2 with HID fallback))

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020202018903C20102 |

#### Property Subgroup 1.2.2.3.nn Bluetooth® LE Settings (Bluetooth® LE Only)

##### Property 1.2.2.3.1.1 Bluetooth® LE Device Name

Table 816 - Property 1.2.2.3.1.1 Bluetooth® LE Device Name

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.3.1.1 / 0x010202030101</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Device Name</td>
</tr>
<tr>
<td>Description</td>
<td><p>This property contains the Bluetooth® device name, which is
typically used by the host software to present an operator with a list
of devices to interact with. To avoid ambiguity, if the solution
specifies that more than one device of the same name will be available,
MagTek recommends including a unique identifier in the device name so
the operator can differentiate.</p>
<p>The name should not contain any null string characters (0x00) at the
beginning or in the middle, 0x00 can be used at the end of the name for
padding to a total length of 20 characters. When setting this property,
you can enter 0 to 20 characters. If set to a length of 0, the value
reverts to its original default value described below. After modifying
the Bluetooth® device name, you must reset the Bluetooth® LE module.</p>
<p>When getting this property, device will always return 20 characters
If the name is less than 20 characters long, device will return 0x00 for
the remaining characters.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>0</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>20</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td><p>A prefix, such as “DF II Go-“ for DynaFlex II Go, followed by the
device’s serial number. For example, “DF II Go-B603226”.</p>
<p>Devices are always deployed with the serial number loaded, but prior
to loading the serial number at MagTek, the prefix will be followed by
the second to last and the last least significant bytes of the
Bluetooth® device address converted to ASCII hex. For example, “DF II
Go-97C2”.</p></td>
</tr>
</tbody>
</table>

Table 817 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102C100 |

Table 818 - Get Response Example

| Example (Hex) |
|----|
| AA008104825CD10182040000000084820020D10181072B06010401F6098501028910E10EE20CE70AE208C106943469B297A5 |

Table 819 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D111842ED11181072B06010401F609850101891EE21CE21AE318E116C11444594E41464C4558000000000000000000000000 |

Table 820 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D1118204000000008482002ED11181072B06010401F609850101891EE21CE21AE318E116C11444594E41464C4558000000000000000000000000 |

##### Property 1.2.2.3.1.2 Bluetooth® LE Desired Minimum Connection Interval

Table 821 - Property 1.2.2.3.1.2 Bluetooth® LE Desired Minimum
Connection Interval

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.3.1.2 / 0x010202030102</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Desired Minimum Connection Interval</td>
</tr>
<tr>
<td>Description</td>
<td><p>This two-byte property, in most significant byte order, contains
the Interval Min value in 1.25 millisecond units that the device sends
to a Bluetooth® LE host in a CONNECTION PARAMETER UPDATE REQUEST. See
the Core Bluetooth® Specification for details. Only values between 6 and
3200 are valid.</p>
<p>After the host changes this property, the device must be reset before
the changes will take effect.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 0x06 (6) - 0x0C 0x80 (3200) MSB first</td>
</tr>
<tr>
<td>Default</td>
<td>0x00 0x0C (15.0 milliseconds)</td>
</tr>
</tbody>
</table>

Table 822 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102C200 |

Table 823 - Get Response Example

| Example (Hex) |
|----|
| AA0081048232D1018204000000008482001CD10181072B06010401F609850101890CE20AE208E306E104C202000C |

Table 824 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D111841CD11181072B06010401F609850101890CE20AE208E306E104C2020010 |

Table 825 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D1118204000000008482001CD11181072B06010401F609850101890CE20AE208E306E104C2020010 |

##### Property 1.2.2.3.1.3 Bluetooth® LE Desired Maximum Connection Interval

Table 826 - Property 1.2.2.3.1.3 Bluetooth® LE Desired Maximum
Connection Interval

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.3.1.3 / 0x010202030103</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Desired Maximum Connection Interval</td>
</tr>
<tr>
<td>Description</td>
<td><p>This two-byte property, in most significant byte order, contains
the Interval Max value in 1.25 millisecond units that the device sends
to a Bluetooth® LE host in a CONNECTION PARAMETER UPDATE REQUEST. See
the Core Bluetooth® Specification for more details. Only values between
6 and 3200 are valid.</p>
<p>After the host changes this property, the device must be reset before
the changes will take effect.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 0x06 (6) - 0x0C 0x80 (3200) MSB first</td>
</tr>
<tr>
<td>Default</td>
<td>0x00 0x00C (15.0 milliseconds)</td>
</tr>
</tbody>
</table>

Table 827 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102C300 |

Table 828 - Get Response Example

| Example (Hex) |
|----|
| AA0081048232D1018204000000008482001CD10181072B06010401F609850101890CE20AE208E306E104C302000C |

Table 829 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D111841CD11181072B06010401F609850101890CE20AE208E306E104C3020010 |

Table 830 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D1118204000000008482001CD11181072B06010401F609850101890CE20AE208E306E104C3020010 |

##### Property 1.2.2.3.1.4 Bluetooth® LE Desired Slave Latency

Table 831 - Property 1.2.2.3.1.4 Bluetooth® LE Desired Slave Latency

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.3.1.4 / 0x010202030104</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Desired Slave Latency</td>
</tr>
<tr>
<td>Description</td>
<td><p>This two byte property, in most significant byte order, contains
the Slave Latency value the device sends to the Bluetooth® LE host in a
CONNECTION PARAMETER UPDATE REQUEST. See the Core Bluetooth®
Specification for details. Only values between 0 and 499 are valid.</p>
<p>After the host changes this property, the device must be reset before
the changes will take effect.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 0x00 (0) – 0x01 0xF3 (499) MSB first</td>
</tr>
<tr>
<td>Default</td>
<td>0x00 0x00</td>
</tr>
</tbody>
</table>

Table 832 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102C400 |

Table 833 - Get Response Example

| Example (Hex) |
|----|
| AA0081048232D1018204000000008482001CD10181072B06010401F609850101890CE20AE208E306E104C4020004 |

Table 834 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D111841CD11181072B06010401F609850101890CE20AE208E306E104C4020004 |

Table 835 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D1118204000000008482001CD11181072B06010401F609850101890CE20AE208E306E104C4020004 |

##### Property 1.2.2.3.1.5 Bluetooth® LE Desired Supervision Timeout

Table 836 - Property 1.2.2.3.1.5 Bluetooth® LE Desired Supervision
Timeout

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.3.1.5 / 0x010202030105</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Desired Supervision Timeout</td>
</tr>
<tr>
<td>Description</td>
<td><p>This two-byte property, in most significant byte order, contains
the value of the Timeout Multiplier sent in 10 millisecond units that
the device sends to a Bluetooth® LE host in a CONNECTION PARAMETER
UPDATE REQUEST. See the Core Bluetooth® Specification for details. Only
values between 10 and 3200 are valid.</p>
<p>After the host changes this property, the device must be reset before
the changes will take effect.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 0x0A (10) - 0x0C 0x80 (3200) MSB first</td>
</tr>
<tr>
<td>Default</td>
<td>0x01 0xF4 (5000 milliseconds)</td>
</tr>
</tbody>
</table>

Table 837 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102C500 |

Table 838 - Get Response Example

| Example (Hex) |
|----|
| AA0081048232D1018204000000008482001CD10181072B06010401F609850101890CE20AE208E306E104C50201F4 |

Table 839 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D111841CD11181072B06010401F609850101890CE20AE208E306E104C50201F4 |

Table 840 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D1118204000000008482001CD11181072B06010401F609850101890CE20AE208E306E104C50201F4 |

##### Property 1.2.2.3.1.6 Bluetooth® LE Connection Parameter Update Request Control

Table 841 - Property 1.2.2.3.1.6 Bluetooth® LE Connection Parameter
Update Request Control

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.3.1.6 / 0x010202030106</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Connection Parameter Update Request Control</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if the Bluetooth® LE
connection parameter update request control is enabled. When it is
enabled, the device sends a connection parameter update request once
after each Bluetooth® LE connection.</p>
<p>After the host changes this property, the device must be reset before
the changes will take effect.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 (Disabled)</p>
<p>0x01 (Enabled)</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x01 (Enabled)</td>
</tr>
</tbody>
</table>

Table 842 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102C600 |

Table 843 - Get Response Example

| Example (Hex) |
|----|
| AA0081048232D1018204000000008482001BD10181072B06010401F609850101890BE209E207E305E103C60100 |

Table 844 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D111841BD11181072B06010401F609850101890BE209E207E305E103C60100 |

Table 845 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D1118204000000008482001BD11181072B06010401F609850101890BE209E207E305E103C60100 |

##### Property 1.2.2.3.1.7 Bluetooth® LE Minimum Advertising Interval

Table 846 - Property 1.2.2.3.1.7 Bluetooth® LE Minimum Advertising
Interval

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.3.1.7 / 0x010202030107</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Minimum Advertising Interval</td>
</tr>
<tr>
<td>Description</td>
<td><p>This two property, in most significant byte order, contains the
device’s minimum Bluetooth® LE advertising interval in 625 microsecond
increments. This property, combined with <strong>Property 1.2.2.3.1.8
Bluetooth® LE Maximum Advertising Interval,</strong> specifies the
Bluetooth® LE advertising interval the device uses. Smaller advertising
intervals cause the device to consume more power when advertising, which
may be a concern when running on battery power.</p>
<p>Only values between 32 (20ms) and 65535 (40.96s) are valid. The host
may need to adjust the maximum advertising interval property when
changing this property; if the maximum advertising interval is less than
the minimum, the device may behave unpredictably.</p>
<p>After the host changes this property, the device must be reset before
the changes will take effect.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 0x20 (32) - 0xFF 0xFF (65535) MSB first</td>
</tr>
<tr>
<td>Default</td>
<td>0x00 0xA0 = 160 (100 milliseconds)</td>
</tr>
</tbody>
</table>

Table 847 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102C700 |

Table 848 - Get Response Example

| Example (Hex) |
|----|
| AA0081048232D1018204000000008482001CD10181072B06010401F609850101890CE20AE208E306E104C70200A0 |

Table 849 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D111841CD11181072B06010401F609850101890CE20AE208E306E104C70200B0 |

Table 850 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D1118204000000008482001CD11181072B06010401F609850101890CE20AE208E306E104C70200B0 |

##### Property 1.2.2.3.1.8 Bluetooth® LE Maximum Advertising Interval

Table 851 - Property 1.2.2.3.1.8 Bluetooth® LE Maximum Advertising
Interval

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.3.1.8 / 0x010202030108</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Maximum Advertising Interval</td>
</tr>
<tr>
<td>Description</td>
<td><p>This two-byte property, in most significant byte order, contains
the device’s maximum Bluetooth® LE advertising interval in 625
microsecond increments. This property, combined with <strong>Interval,
specifies</strong> the Bluetooth® LE advertising interval the device
uses. Smaller advertising intervals cause the device to consume more
power when advertising, which may be a concern when running on battery
power.</p>
<p>Only values between 32 (20ms) and 65535 (40.96s) are valid. The host
may need to adjust the minimum advertising interval property when
changing this property. If the minimum advertising interval is greater
than the maximum, the device may behave unpredictably.</p>
<p>After the host changes this property, the device must be reset before
the changes will take effect.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 0x20 (32) - 0xFF 0xFF (65535) MSB first</td>
</tr>
<tr>
<td>Default</td>
<td>0x00 0xA0 = 160 (100 milliseconds)</td>
</tr>
</tbody>
</table>

Table 852 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102C800 |

Table 853 - Get Response Example

| Example (Hex) |
|----|
| AA0081048232D1018204000000008482001CD10181072B06010401F609850101890CE20AE208E306E104C80200A0 |

Table 854 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D111841CD11181072B06010401F609850101890CE20AE208E306E104C80200B0 |

Table 855 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D1118204000000008482001CD11181072B06010401F609850101890CE20AE208E306E104C80200B0 |

##### Property 1.2.2.3.1.9 Bluetooth® LE Passkey

Table 856 - Property 1.2.2.3.1.9 Bluetooth® LE Passkey

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.3.1.9 / 0x010202030109</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Passkey</td>
</tr>
<tr>
<td>Description</td>
<td><p>This six-byte property contains the device’s Bluetooth® passkey
as a six-character with valid value for each character between ‘0’ and
‘9’</p>
<p>After the host changes this property, the device must be reset before
the changes will take effect.</p>
<p>For security, the Get request for this property will always return a
length of zero and no value, so you can only set the passkey and not get
it.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>6</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>6</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>'000000' - '999999'</td>
</tr>
<tr>
<td>Default</td>
<td>'000000'</td>
</tr>
</tbody>
</table>

Table 857 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102C900 |

Table 858 - Get Response Example

| Example (Hex) |
|----|
| AA0081048232D1018204000000008482001AD10181072B06010401F609850101890AE208E206E304E102C900 |

Table 859 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D1118420D11181072B06010401F6098501018910E20EE20CE30AE108C906303132333435 |

Table 860 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D11182040000000084820020D11181072B06010401F6098501018910E20EE20CE30AE108C906303132333435 |

##### Property 1.2.2.3.1.A Bluetooth® LE Never Advertise

Table 861 - Property 1.2.2.3.1.A Bluetooth® LE Never Advertise

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.3.1.A / 0x01020203010A</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Never Advertise</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if the Bluetooth® LE
Never Advertise is enabled. When it is enabled, the device never
advertises. This mode may be useful for operators who only want to use
the USB interface and don’t want the device to advertise.</p>
<p>After the host changes this property, the device must be reset before
the changes will take effect.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 (Disabled)</p>
<p>0x01 (Enabled)</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00 (Disabled)</td>
</tr>
</tbody>
</table>

Table 862 - Get Request Example

| Example (Hex) |
|----|
| AA00 81040128D101 841AD101 81072B06010401F609 850101 890AE208E206E304E102CA00 |

Table 863 - Get Response Example

| Example (Hex) |
|----|
| AA0081048232D1018204000000008482001BD10181072B06010401F609850101890BE209E207E305E103CA0100 |

Table 864 - Set Request Example

| Example (Hex) |
|----|
| AA0081040112D111841BD11181072B06010401F609850101890BE209E207E305E103CA0100 |

Table 865 - Set Response Example

| Example (Hex) |
|----|
| AA0081048212D1118204000000008482001BD11181072B06010401F609850101890BE209E207E305E103CA0100 |

##### Property 1.2.2.3.1.B Bluetooth® LE FCC Test Control (MAGTEK INTERNAL ONLY)

Table 866 - Property 1.2.2.3.1.B Bluetooth® LE FCC Test Control (MAGTEK
INTERNAL ONLY)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.3.1.B / 0x01020203010B</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE FCC Test Control</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if Bluetooth® LE FCC
test mode is enabled and to control it. FCC test mode is only used by
MagTek for FCC testing. When it is enabled, the device sends packets
continuously with a fixed interval and all other Bluetooth® LE
communications are disabled.</p>
<p>If the value of this property is set between 0 and 39 (0x27) FCC test
mode is enabled and the value is the transmit channel C. The transmit
frequency is (2C + 2402) Mhz. If the value is greater than 39 (0x27)
then FCC test mode is disabled.</p>
<p>After the host changes this property, the device must be reset before
the changes will take effect.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 – 0xFF</td>
</tr>
<tr>
<td>Default</td>
<td>0xFF (FCC test disabled)</td>
</tr>
</tbody>
</table>

Table 867 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020301 8902 CB00 |

Table 868 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020203018903CB01FF |

Table 869 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870402020301 8903 CB01FF |

Table 870 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020203018903CB01FF |

##### Property 1.2.2.3.1.C Bluetooth® LE Sleep Enabled 

Table 871 - Property 1.2.2.3.1.C Bluetooth® LE Sleep Enabled

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.3.1.C / 0x01020203010C</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Sleep Enabled</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if Bluetooth® LE Sleep
is enabled. When it is enabled, the device will conserve battery power
when USB power is not present and the device is not in a secure
Bluetooth® LE connection with notifications enabled (not able to
exchange messages with a host). The device will conserve battery power
by turning off various hardware features and by going into low power
modes.</p>
<p>The battery life when the device is idle can be increased by about 3
times for DynaFlex II Go when the host application takes advantage of
this feature.</p>
<p>Here is an example of how the host application can be written to take
advantage of this feature and extend battery life.</p>
<p>1) Establish a BLE connection with the device only when the host
needs to perform a transaction or other operation.</p>
<p>2) Perform the transaction or other operation.</p>
<p>3) Close the BLE connection.</p>
<p>4) The device will sleep at this point and use less power.</p>
<p>Some operations in addition to connecting USB power or establishing a
BLE connection will wake the device from sleep mode temporarily. The
following are examples of these operations.</p>
<p>1) Pressing the button.</p>
<p>2) Putting the device into pairing mode.</p>
<p>When the device is sleeping, all LEDs will go off so the device will
look similar to when it is off.</p>
<p>If the value of this property is set to 0, sleep is disabled. If it
is set to 1, sleep is enabled.</p>
<p>After the host changes this property, the device must be reset before
the changes will take effect.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 – 0x01</td>
</tr>
<tr>
<td>Default</td>
<td>0x01 (Bluetooth® LE Sleep enabled)</td>
</tr>
</tbody>
</table>

Table 872 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020301 8902 CC00 |

Table 873 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020203018903CC0100 |

Table 874 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870402020301 8903 CC0100 |

Table 875 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020203018903CC0100 |

##### Property 1.2.2.3.1.D Bluetooth® LE Debug Mode Enabled 

Table 876 - Property 1.2.2.3.1.D Bluetooth® LE Debug Mode Enabled

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.2.3.1.D / 0x01020203010D</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Debug Mode Enabled</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to determine if Bluetooth® LE Debug
Mode is enabled. When it is enabled, the secure connections bonding uses
known debug keys, so that the encrypted packet can be opened by a
Bluetooth® protocol analyzer. Bondings made in debug mode are unsecure.
This mode should only be enabled for debugging for development purposes
and not for regular device use.</p>
<p>Prior to enabling or disabling Debug Mode, the following should be
done. Erase all of the device's bonds with <strong>Command 0x1F05 –
Erase All Bluetooth® LE Bonds (Bluetooth® LE Only)</strong>. Forget the
device on all hosts that have paired with it by using the host's
Bluetooth® settings application. Reboot all of those hosts.</p>
<p>Some hosts like Windows 10 will not pair with devices that use known
debug keys.</p>
<p>If the value of this property is set to 0, Debug Mode is disabled. If
it is set to 1, Debug Mode is enabled.</p>
<p>After the host changes this property, the device must be reset before
the changes will take effect.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 – 0x01</td>
</tr>
<tr>
<td>Default</td>
<td>0x00 (Bluetooth® LE Debug Mode disabled)</td>
</tr>
</tbody>
</table>

Table 877 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02020301 8902 CD00 |

Table 878 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501018704020203018903CD0100 |

Table 879 - Set Request Example

| Example (Hex)                                               |
|-------------------------------------------------------------|
| AA00 81040155D111 8410 D111 850101 870402020301 8903 CD0100 |

Table 880 - Set Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D11182040000000084820010D1118501018704020203018903CD0100 |

#### Property Subgroup 1.2.3.nnn User Interface Settings

##### Property 1.2.3.1.1.1 Custom Idle Page Image (Display Only)

Table 881- Property 1.2.3.1.1.1 Custom Idle Page Image (Display Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.3.1.1.1 / 0x010203010101</td>
</tr>
<tr>
<td>Name</td>
<td>Custom Idle Page Image</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set which custom image it
displays when idle. If the selected image does not exist, the device
falls back to showing text. This property does not take effect
instantly; it takes effect the next time the device transitions to idle
(for example, after a transaction or after resetting).</p>
<ul>
<li><p>0x00 = Show text “Welcome”</p></li>
<li><p>0x01 = Show custom image 1</p></li>
<li><p>0x02 = Show custom image 2</p></li>
<li><p>0x03 = Show custom image 3</p></li>
<li><p>0x04 = Show custom image 4</p></li>
</ul>
<p>To use this feature, the host must first load an image into the
selected slot using <strong>Command 0xD812 - Start Send File to Device
(Unsecured)</strong>. Images must be BMP format, 160KB or smaller with
no compression, maximum 320px by 240px, with color depth 16 color, 256
color, 16-bit color, 24-bit color. Images smaller than the maximum size
are centered on the display. Note images at full screen size must be
16-bit color or lower to meet the size requirement.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any number</td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 882 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E3 06 E1 04 E1 02 C1 00 |

Table 883 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5E D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E1 03 C1 01 03 |

Table 884 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5D D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E1 03 C1 01 03 |

Table 885 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5D D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E1 03 C1 01 03 |

##### Property 1.2.3.1.1.2 Custom Idle Page Image Device Locked (Display Only)

Table 886- Property 1.2.3.1.1.2 Custom Idle Page Image Device Locked
(Display Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.3.1.1.2 / 0x010203010102</td>
</tr>
<tr>
<td>Name</td>
<td>Custom Idle Page Image Device Locked</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set which custom image it
displays when idle and locked. If the selected image does not exist, the
device falls back to showing text. This property does not take effect
instantly; it takes effect the next time the device transitions to idle
(for example, after a transaction or after resetting). See
<strong>Device Lock Feature</strong> for more information.</p>
<ul>
<li><p>0x00 = Show text “Welcome” “Device is Locked”</p></li>
<li><p>0x01 = Show custom image 1</p></li>
<li><p>0x02 = Show custom image 2</p></li>
<li><p>0x03 = Show custom image 3</p></li>
<li><p>0x04 = Show custom image 4</p></li>
</ul>
<p>To use this feature, the host must first load an image into the
selected slot using <strong>Command 0xD812 - Start Send File to Device
(Unsecured)</strong>. Images must be BMP format, 160KB or smaller with
no compression, maximum 320px by 240px, with color depth 16 color, 256
color, 16-bit color, 24-bit color. Images smaller than the maximum size
are centered on the display. Note images at full screen size must be
16-bit color or lower to meet the size requirement.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any number</td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 887 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02030101 8902 C200 |

Table 888 - Get Response Example

| Example (Hex) |
|----|
| AA00 81 04 8255D101 82 04 00000000 84 820010 D101 85 01 01 87 04 02030101 89 03 C2 01 00 |

Table 889 - Set Request Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA00 81040155D111 8410 D111 8501 01 8704 02030101 8903 C201 00 |

Table 890 - Set Response Example

| Example (Hex) |
|----|
| AA00 81 04 8255D111 82 04 00000000 84 820010 D111 85 01 01 87 04 02030101 89 03 C2 01 00 |

##### Property 1.2.3.1.2.1 Display Orientation (Display Only)

Table 891- Property 1.2.3.1.2.1 Display Orientation (Display Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.3.1.2.1 / 0x010203010201</td>
</tr>
<tr>
<td>Name</td>
<td>Display Orientation</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to set the orientation of the display.
There are four modes: Landscape with magnetic stripe reader (MSR) on the
top, Landscape with MSR on the bottom, Portrait with MSR on the right,
and Portrait with MSR on the left. This property does not take effect
immediately, it takes effect the next time the device transitions to
idle (for example, after a transaction or after power cycle /
reset).</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Landscape with MSR on Top</p>
<p>0x01 = Portrait with MSR on Right</p>
<p>0x02 = Portrait with MSR on Left</p>
<p>0x03 = Landscape with MSR on Bottom</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 892 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E3 06 E1 04 E2 02 C1 00 |

Table 893 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5E D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E2 03 C1 01 00 |

Table 894 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5D D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E2 03 C1 01 01 |

Table 895 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5D D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E2 03 C1 01 01 |

##### Property 1.2.3.1.3.1 Enable Card Logos Page at Startup

Table 896- Property 1.2.3.1.3.1 Enable Card Logos Page at Startup

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.3.1.3.1 / 0x010203010301</td>
</tr>
<tr>
<td>Name</td>
<td>Enable Card Logos Page at Startup</td>
</tr>
<tr>
<td>Description</td>
<td>Enables a page at startup that displays supported payment type brand
logos.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Disable Logo Page at Startup</p>
<p>0x01 = Enable Logo Page at Startup</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 897 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E3 06 E1 04 E3 02 C1 00 |

Table 898 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5E D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E3 03 C1 01 00 |

Table 899 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5D D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E3 03 C1 01 01 |

Table 900 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5D D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E3 03 C1 01 01 |

##### Property 1.2.3.1.3.2 Display Card Logo While Authorizing

Table 901- Property 1.2.3.1.3.2 Display Card Logo While Authorizing

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.3.1.3.2 / 0x010203010302</td>
</tr>
<tr>
<td>Name</td>
<td>Display Card Logo While Authorizing</td>
</tr>
<tr>
<td>Description</td>
<td>Enable display of logo for card brand used in transaction</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Disable Logo</p>
<p>0x01 = Enable Logo</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 902 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E3 06 E1 04 E3 02 C2 00 |

Table 903 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5E D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E3 03 C2 01 00 |

Table 904 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5D D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E3 03 C2 01 01 |

Table 905 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5D D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E1 05 E3 03 C2 01 01 |

##### Property 1.2.3.1.2.2 Display Backlight Intensity (Display Only)

Table 906- Property 1.2.3.1.2.2 Display Backlight Intensity (Display
Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.3.1.2.2 / 0x010203010202</td>
</tr>
<tr>
<td>Name</td>
<td>Display Backlight Intensity</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to set the intensity of the
display’s backlight, expressed as a percentage range from 1% to
100%.</p>
<p>The backlight setting takes effect immediately after the host changes
it.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x01..0x64</td>
</tr>
<tr>
<td>Default</td>
<td>0x5A (90%)</td>
</tr>
</tbody>
</table>

Table 907 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 01 84 0F D1 01 85 01 01 87 04 02 03 01 02 89 02 C2 00 |

Table 908 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 10 D1 01 85 01 01 87 04 02 03 01 02 89 03 C2 01 5A |

Table 909 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 10 D1 11 85 01 01 87 04 02 03 01 02 89 03 C2 0164 |

Table 910 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 02 03 01 02 89 03 C2 01 64 |

##### Property 1.2.3.2.1.1 System Volume Control

Table 911- Property 1.2.3.2.1.1 System Volume Control

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.3.2.1.1 / 0x010203020101</td>
</tr>
<tr>
<td>Name</td>
<td>System Volume Control</td>
</tr>
<tr>
<td>Description</td>
<td><p>This property sets the output volume for all sounds the device
produces after startup, expressed as a percentage range from 0% (no
sound) to 100%. The volume setting takes effect immediately after the
host changes it.</p>
<p>Note that devices with limited volume control hardware allocate
ranges of numbers to represent the same physical volume level (for
example, 1..49 = Low, 50..100 = High).</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00..0x64</td>
</tr>
<tr>
<td>Default</td>
<td>0x32 (50%)</td>
</tr>
</tbody>
</table>

Table 912 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E3 06 E2 04 E1 02 C1 00 |

Table 913 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5E D1 01 82 04 00 00 00 00 84 82 00 1B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E2 05 E1 03 C1 01 32 |

Table 914 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 5D D1 11 84 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E2 05 E1 03 C1 01 01 |

Table 915 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 5D D1 11 82 04 00 00 00 00 84 82 00 1B D1 11 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0B E2 09 E3 07 E2 05 E1 03 C1 01 01 |

#### Property Subgroup 1.2.5.nnn Security Settings

##### Property 1.2.5.2.1.1 Device Lock State

Table 916- Property 1.2.5.2.1.1 Device Lock State

| Property Description |  |
|----|----|
| Property OID | 1.2.5.2.1.1 / 0x010205020101 |
| Name | Device Lock State |
| Description | This property can be used to get or set the device lock state. Getting this property does not require security, however setting it does. Setting it requires the use of **Command 0xD112 - Set Property (Secured)** which requires MagTek's involvement. To set the device lock state without involving MagTek use Command 0xEF04 – Load LTPK Protection Key. The value of the device lock state will revert to the value of **Property 1.2.5.2.1.2 Device Lock State After Reset** after a reset or a power cycle. See **Device Lock Feature** for more information. |
| Securing Key | See **Command 0xD112 - Set Property (Secured).** |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0x00 = Unlocked, 0x01 = Locked |
| Default | See **Property 1.2.5.2.1.2 Device Lock State After Reset.** |

Table 917 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02050201 8902 C100 |

Table 918 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850101 870402050201 8903 C101 00 |

Table 919 - Set Request Example

| Example (Hex) |
|---------------|
| TBD           |

Table 920 - Set Response Example

| Example (Hex) |
|---------------|
| TBD           |

##### Property 1.2.5.2.1.2 Device Lock State After Reset

Table 921- Property 1.2.5.2.1.2 Device Lock State After Reset

| Property Description |  |
|----|----|
| Property OID | 1.2.5.2.1.2 / 0x010205020102 |
| Name | Device Lock State After Reset |
| Description | This property can be used to get or set what **Property 1.2.5.2.1.1 Device Lock State** will be set to after the device is reset or power cycled. Systems that use the optional device lock feature should set this property to locked, otherwise all someone would need to do to unlock the device would be to power cycle or reset it. The value of the device lock state after reset property is stored in non-volatile memory so changes made to it will persist after the device is reset or power cycled. See **Device Lock Feature** for more information. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0x00 = Unlocked, 0x01 = Locked |
| Default | 0x00 |

Table 922 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02050201 8902 C200 |

Table 923 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850101 870402050201 8903 C201 00 |

Table 924 - Set Request Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA00 81040155D111 8410 D111 8501 01 8704 02050201 8903 C201 00 |

Table 925 - Set Response Example

| Example (Hex) |
|----|
| AA00 81048255D111 820400000000 84820010 D111 850101 870402050201 8903 C201 00 |

##### Property 1.2.5.2.1.3 Device Lock Passcode

Table 926- Property 1.2.5.2.1.3 Device Lock Passcode

| Property Description |  |
|----|----|
| Property OID | 1.2.5.2.1.3 / 0x010205020103 |
| Name | Device Lock Passcode |
| Description | This property can be used to set the device lock passcode. The value of the device lock passcode is stored in non-volatile memory so changes made to it will persist after the device is reset or power cycled. For security, the host can’t get the value of the device lock passcode from the device. If the host gets this property, the device will always return a length of 0 and no value. Setting this property requires security. Setting it requires the use of **Command 0xD112 - Set Property (Secured)** which requires MagTek's involvement. To set the device lock passcode without involving MagTek use **Command 0xEF07 – Change Device Lock Passcode**. See **Device Lock Feature** for more information. |
| Securing Key | See **Command 0xD112 - Set Property (Secured).** |
| Min. Len (b) | 4 |
| Max. Len (b) | 63 |
| Data Type | Binary |
| Valid Values | It can only contain any printable ASCII character. |
| Default | 0x34 0x33 0x32 0x31 (“4321”) |

Table 927 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02050201 8902 C300 |

Table 928 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 8482000F D101 850101 870402050201 8902 C300 |

Table 929 - Set Request Example

| Example (Hex) |
|---------------|
| TBD           |

Table 930 - Set Response Example

| Example (Hex) |
|---------------|
| TBD           |

#### Property Subgroup 1.2.7.nnn System Settings

##### Property 1.2.7.1.1.1 Device Reset Occurred Notification Control

Table 931 - Property 1.2.7.1.1.1 Device Reset Occurred Notification
Control

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.7.1.1.1 / 0x010207010101</td>
</tr>
<tr>
<td>Name</td>
<td>Device Reset Occurred Notification Control</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to control behavior of the
<strong>Device Reset Occurred</strong> notification in
<strong>Notification 0x1001 - Device Information Update</strong>.</p>
<p>Changes to this property do not take effect until the device is power
cycled or reset.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Never send this notification.</p>
<p>0x01..0xFE = The frequency in seconds the device should repeat
sending the notification until the host requests that it stop with
<strong>Property 1.2.7.1.1.2 Device Reset Occurred Notification
Acknowledged</strong>.</p>
<p>0xFF = Only send this notification once.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 932 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 01 84 0F D1 01 85 01 01 87 04 02 07 01 01 89 02 C1 00 |

Table 933 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 10 D1 01 85 01 01 87 04 02 07 01 01 89 03 C1 01 00 |

Table 934 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 10 D1 11 85 01 01 87 04 02 07 01 01 89 03 C1 01 05 |

Table 935 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 02 07 01 01 89 03 C1 01 05 |

##### Property 1.2.7.1.1.2 Device Reset Occurred Notification Acknowledged

Table 936 - Property 1.2.7.1.1.2 Device Reset Occurred Notification
Acknowledged

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.7.1.1.2 / 0x010207010102</td>
</tr>
<tr>
<td>Name</td>
<td>Device Reset Occurred Notification Acknowledged</td>
</tr>
<tr>
<td>Description</td>
<td><p>The host can use this property to acknowledge it has received the
<strong>Device Reset Occurred</strong> notification in
<strong>Notification 0x1001 - Device Information Update</strong> and to
request that the device stop sending it.</p>
<p>Alternatively, because the device automatically sets the value of
this property to 0x00 on boot, the host can use this property to detect
power cycles or resets using a polling method. To implement this, the
host should read the value on a set schedule (for example, every 2
seconds). If the host finds a value of 0x00, a power cycle or reset has
occurred, and the host should set the value back to 0x01. From that
point until the next power cycle or reset, the value will remain
0x01.</p>
<p>Changes made to this property will not persist after a power cycle or
reset. After a power cycle or reset, this property has a value of 0x00
until the host changes it to 0x01.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Not acknowledged. Only the device can set to this
value.</p>
<p>0x01 = Acknowledged. Do not continue to send the
notification.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00</td>
</tr>
</tbody>
</table>

Table 937 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02070101 8902 C200 |

Table 938 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D101 8204 00000000 84820010 D101 8501 01 8704 02070101 8903 C201 00 |

Table 939 - Set Request Example

| Example (Hex)                                                 |
|---------------------------------------------------------------|
| AA00 81040155D111 8410 D111 8501 01 8704 02070101 8903 C20101 |

Table 940 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D111 8204 00000000 84820010 D111 8501 01 8704 02070101 8903 C201 01 |

##### Property 1.2.7.1.1.3 Device Reset Will Occur Soon Notification Control

Table 941 - Property 1.2.7.1.1.3 Device Reset Will Occur Soon
Notification Control

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.7.1.1.3 / 0x010207010103</td>
</tr>
<tr>
<td>Name</td>
<td>Device Reset Will Occur Soon Notification Control</td>
</tr>
<tr>
<td>Description</td>
<td><p>The host can use this property to control behavior of the
<strong>Device Reset Will Occur Soon</strong> notification in
<strong>Notification 0x1001 - Device Information Update</strong>.</p>
<p>See <strong>24 Hour Automatic Reset PCI Requirement</strong> for more
information.</p>
<p>Changes to this property do not take effect until the device is power
cycled or reset.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Never send this notification.</p>
<p>0x01..0xFF = Number of minutes before a reset to send the
notification message.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x03</td>
</tr>
</tbody>
</table>

Table 942 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 01 84 0F D1 01 85 01 01 87 04 02 07 01 01 89 02 C3 00 |

Table 943 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 01 82 04 00 00 00 00 84 82 00 10 D1 01 85 01 01 87 04 02 07 01 01 89 03 C3 01 05 |

Table 944 - Set Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 55 D1 11 84 10 D1 11 85 01 01 87 04 02 07 01 01 89 03 C1 01 05 |

Table 8‑115 - Set Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 02 07 01 01 89 03 C1 01 05 |

##### Property 1.2.7.1.1.4 Auto Reset Configuration

Table 945 - Property 1.2.7.1.1.4 Auto Reset Configuration

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.7.1.1.4 / 0x010207010104</td>
</tr>
<tr>
<td>Name</td>
<td>Auto Reset Configuration</td>
</tr>
<tr>
<td>Description</td>
<td><p>This property controls the device’s auto reset feature. The auto
reset feature can be configured such that the device automatically
resets 23 hours after booting up or at a specific time of day. The
auto-reset feature cannot be disabled.</p>
<p>See <strong>24 Hour Automatic Reset PCI Requirement</strong> for more
information.</p>
<p>Changes to this property do not take effect until the device is power
cycled or reset.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>First byte 0 - 23 hours and second byte 0 - 59 minutes = Reset at
the time of day specified. The time of day specified should be 24-hour
Universal Time Coordinated (UTC). For example, values of 0 0 would be
12:00am UTC and values of 23 59 (0x17 0x3B) would be 11:59pm UTC.</p>
<p>First byte 0xFF and second byte 0xFF = Auto reset 23 hours after
booting up.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0xFF 0xFF</td>
</tr>
</tbody>
</table>

Table 946 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02070101 8902 C400 |

Table 947 - Get Response Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D10182040000000084820011D1018501018704020701018904C402FFFF |

Table 948 - Set Request Example

| Example (Hex)                                                    |
|------------------------------------------------------------------|
| AA00 81040155D111 8411 D111 8501 01 8704 02070101 8904 C402 FFFF |

Table 949 - Set Response Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D11182040000000084820011D1118501018704020701018904C402FFFF |

##### Property 1.2.7.1.2.1 User Event Notification Controls Enable

Table 950 - Property 1.2.7.1.2.1 User Event Notification Controls Enable

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Bit Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.7.1.2.1 / 0x010207010201</td>
</tr>
<tr>
<td>Name</td>
<td>User Event Notifications Enable</td>
</tr>
<tr>
<td>Description</td>
<td><p>The host can use this property to enable <strong>notification
reasons</strong> defined in <strong>Notification 0x1001 - Device
Information Update</strong> in the <strong>User Events</strong>
Category. Each bit enables a specific <strong>Reason</strong> by setting
that bit to 1. Byte 0 is the first byte, bit 0 is the LSB of each
byte.</p>
<p>The device only detects these user events and sends these
notifications when it is idle. While processing a command (not idle),
such as when processing a transaction with <strong>Command 0x1001 -
Start Transaction</strong>, the device only sends notifications related
to the command it is currently processing.</p>
<p>Notification reasons may consume power when idle. For example,
enabling Contactless reasons requires the device to continuously consume
some radio frequency power to detect the presence of a contactless card
when idle. To conserve power, only enable the notification reasons that
are required by the solution design, if any. The readers and their
associated notifications will be disabled if the battery charge is 5
percent or lower.</p>
<p>Changes to this property do not take effect until the device is power
cycled or reset.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Byte 0</p>
<ul>
<li><p>bit 0 = Reason: Contactless Card Presented</p></li>
<li><p>bit 1 = Reason: Contactless Card Removed</p></li>
<li><p>bit 2 = Reason: Card Seated in Slot</p></li>
<li><p>bit 3 = Reason: Card Unseated from Slot</p></li>
<li><p>bit 4 = Reason: Card Swiped</p></li>
<li><p>bit 5 = Reason: Touch Sensor Press Detected</p></li>
<li><p>bit 6 = Reason: Touch Sensor Release Detected</p></li>
<li><p>bit 7 = Reason: Barcode Read Detected</p></li>
</ul>
<p>Byte 1</p>
<ul>
<li><p>bit 0 = Reason: Encrypt Barcode Reader Event Data</p></li>
</ul>
<ul>
<li><p>bit 1 = Reserved (set to 0x00)</p></li>
<li><p>etc.</p></li>
</ul>
<p>Byte 2</p>
<ul>
<li><p>bit 0 = Reserved (set to 0x00)</p></li>
<li><p>etc.</p></li>
</ul>
<p>Byte 3</p>
<ul>
<li><p>bit 0 = Reserved (set to 0x00)</p></li>
<li><p>etc.</p></li>
</ul>
<p>Any byte / bit not listed here is reserved for future use. The host
should set those values to 0, so if a future revision of firmware starts
using those bits, the related notifications will be disabled and will
not affect the existing host software.</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x00, 0x00, 0x00, 0x00 (all User Event notifications disabled)</td>
</tr>
</tbody>
</table>

Table 951 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02070102 8902 C100 |

Table 952 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D101 8204 00000000 84820013 D101 8501 01 8704 02070102 8906 C1 04 00 00 00 00 |

Table 953 - Set Request Example

| Example (Hex) |
|----|
| AA00 8104 0155D111 8413 D111 8501 01 8704 02070102 8906 C1 04 03 00 00 00 |

Table 954 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D111 8204 00000000 84820013 D111 8501 01 8704 02070102 8906 C1 04 03 00 00 00 |

##### Property 1.2.7.1.2.2 User Event Notification MSR Data Timeout (MSR Only)

Table 955 - Property 1.2.7.1.2.2 User Event Notification MSR Data
Timeout (MSR Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Bit Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.7.1.2.2 / 0x010207010202</td>
</tr>
<tr>
<td>Name</td>
<td>User Event Notification MSR Data Timeout</td>
</tr>
<tr>
<td>Description</td>
<td><p>This parameter defines the number of seconds the device waits for
the host to take action (by sending <strong>Command 0x1001 - Start
Transaction)</strong> after the device sends <strong>Notification 0x1001
- Device Information Update</strong> to report a User Event / Card
Swiped event. After this period of time passes, the device erases the
buffered card data from memory.</p>
<p>Changes to this property do not take effect until the device is power
cycled or reset.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><ul>
<li><p>0x00 = Invalid value. (will be converted to 0x02 in the
firmware)</p></li>
<li><p>0x01 to 0xFF = 1 to 255 seconds</p></li>
</ul></td>
</tr>
<tr>
<td>Default</td>
<td>0x02 (2 seconds)</td>
</tr>
</tbody>
</table>

Table 956 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104 010CD101 841A D101 8107 2B06010401F609 8501 01 890A E208E706E104E202C200 |

Table 957 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104 820CD101 8204 00000000 8482001B D101 8107 2B06010401F609 8501 01 890B E209E707E105E203C2 0102 |

Table 958 - Set Request Example

| Example (Hex) |
|----|
| AA00 8104 010DD111 841B D111 8107 2B06010401F609 8501 01 890B E209E707E105E203C2 0102 |

Table 959 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104 820DD111 8204 00000000 8482001B D111 8107 2B06010401F609 8501 01 890B E209E707E105E203C2 0102 |

##### Property 1.2.7.1.3.1 Maximum Battery Charge Level (Deprecated)

Table 960 - Property 1.2.7.1.3.1 Maximum Battery Charge Level
(Deprecated)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.7.1.3.1 / 0x010207010301</td>
</tr>
<tr>
<td>Name</td>
<td>Maximum Battery Charge Level</td>
</tr>
<tr>
<td>Description</td>
<td><p>This OID has been deprecated. The OID can be written or read but
it will have no effect of the device’s behavior.</p>
<p>The host can use this property to control the maximum charge level
for the battery. All charge percentages reported or displayed will use
this percentage as 100% charged.</p>
<p>Setting this value to lower than 0x64 (100%) will increase the life
of the battery but reduce the run time when running from the
battery.</p>
<p>The Maximum Battery Charge Level takes effect immediately after the
host changes it.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x0A..0x64</td>
</tr>
<tr>
<td>Default</td>
<td><p>0x64 (100%) if WLAN device</p>
<p>0x50 (80%) for all other devices</p></td>
</tr>
</tbody>
</table>

Table 961 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02070103 8902 C100 |

Table 962 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D101 8204 00000000 84820010 D101 8501 01 8704 02070103 8903 C101 50 |

Table 963 - Set Request Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA00 81040155D111 8410 D111 8501 01 8704 02070103 8903 C101 50 |

Table 8.3‑222 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D111 8204 00000000 84820010 D111 8501 01 8704 02070103 8903 C101 50 |

##### Property 1.2.7.1.4.1 Device Low Temperature Notification Level

Table 964 - Property 1.2.7.1.4.1 Device Low Temperature Notification
Level

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.7.1.4.1 / 0x010207010401</td>
</tr>
<tr>
<td>Name</td>
<td>Device Low Temperature Notification Level</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device will send a low temperature notification when the
device’s temperature falls below this temperature. The temperature is in
degrees Celsius.</p>
<p>The Device Low Temperature Notification Level takes effect
immediately after the host changes it.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Signed Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Temperature in Celsius:<br />
DynaProx: 0xE2 .. 0x55 (-30 .. 85)<br />
DynaProx BCR: 0xEC .. 0x37 (-20 .. 55)<br />
DynaFlex: 0x00 .. 0x2D (0 .. 45)</p>
<p>This value must be less than that set in 1.2.7.1.4.2.</p></td>
</tr>
<tr>
<td>Default</td>
<td>Temperature in Celsius:<br />
DynaProx: 0xE2 (-30<br />
DynaProx BCR: 0xEC (-20)<br />
DynaFlex: 0x00 (0)</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table 965 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02070104 8902 C100 |

Table 966 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D101 8204 00000000 84820010 D101 8501 01 8704 02070104 8903 C101 00 |

Table 967 - Set Request Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA00 81040155D111 8410 D111 8501 01 8704 02070104 8903 C101 05 |

Table 8.3‑227 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D111 8204 00000000 84820010 D111 8501 01 870402070104 8903 C101 05 |

##### Property 1.2.7.1.4.2 Device High Temperature Notification Level

Table 968 - Property 1.2.7.1.4.2 Device High Temperature Notification
Level

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.7.1.4.2 / 0x010207010402</td>
</tr>
<tr>
<td>Name</td>
<td>Device High Temperature Notification Level</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device will send a high temperature notification when the
device’s temperature rises above this temperature. The temperature is in
degrees Celsius.</p>
<p>The Device High Temperature Notification Level takes effect
immediately after the host changes it.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Signed Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Temperature in Celsius:<br />
DynaProx: 0xE2 .. 0x55 (-30 .. 85)<br />
DynaProx BCR: 0xEC .. 0x37 (-20 .. 55)<br />
DynaFlex: 0x00 .. 0x2D (0 .. 45)</p>
<p>This value must be greater than that set in 1.2.7.1.4.1.</p></td>
</tr>
<tr>
<td>Default</td>
<td>Temperature in Celsius:<br />
DynaProx: 0x55 (85)<br />
DynaProx BCR: 0x37 (55)<br />
DynaFlex: 0x2D (45)</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table 969 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02070104 8902 C200 |

Table 8.3‑230 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D101 8204 00000000 84820010 D101 8501 01 8704 02070104 8903 C201 2D |

Table 970 - Set Request Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA00 81040155D111 8410 D111 8501 01 8704 02070104 8903 C201 2D |

Table 8.3‑232 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D111 8204 00000000 84820010 D111 8501 01 870402070104 8903 C201 2D |

##### Property 1.2.7.1.4.3 Device Temperature Notification Repeat Interval

Table 971 - Property 1.2.7.1.4.3 Device Temperature Notification Repeat
Interval

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>1.2.7.1.4.3 / 0x010207010403</td>
</tr>
<tr>
<td>Name</td>
<td>Device Temperature Notification Repeat Interval</td>
</tr>
<tr>
<td>Description</td>
<td><p>While the device’s temperature is outside of the range defined by
Device Low Temperature Notification Level (1.2.7.1.4.1) and Device High
Temperature Notification Level (1.2.7.1.4.2), notifications will be sent
to the host. This property sets the period between notifications.</p>
<p>The Device Temperature Notification Repeat Interval takes effect
immediately after the host changes it.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 Send once. Do not repeat.</p>
<p>0x0F .. 0xFF Repeat period in seconds. Must be multiple of 0x0F
(15).</p></td>
</tr>
<tr>
<td>Default</td>
<td>0x1E (30 seconds)</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table 972 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 01 8704 02070104 8902 C300 |

Table 8.3‑235 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D101 8204 00000000 84820010 D101 8501 01 8704 02070104 8903 C301 1E |

Table 8.36 - Set Request Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA00 81040155D111 8410 D111 8501 01 8704 02070104 8903 C301 1E |

Table 8.3‑237 - Set Response Example

| Example (Hex) |
|----|
| AA00 8104 8255D111 8204 00000000 84820010 D111 8501 01 870402070104 8903 C301 1E |

### Property Group 2.1.1.nnn Device Firmware Feature Information (MAGTEK INTERNAL ONLY FOR NOW)

#### 8.4.1 Property Subgroup 2.1.1.1.nn MainApp Firmware Information

##### 8.4.1.1 Property 2.1.1.1.1.1 API Feature Set

Table 973 - 8.4.1.1 Property 2.1.1.1.1.1 API Feature Set

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.1.1.1.1 / 0x020101010101</td>
</tr>
<tr>
<td>Name</td>
<td>Main App Firmware API Feature Set</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report which API features are
active:</p>
<p>Bit 0: Banking Features</p>
<p>Bit 1 🡪 15: RFU</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Bit Mapped</td>
</tr>
<tr>
<td>Default</td>
<td>0x0000</td>
</tr>
</tbody>
</table>

Table 974 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 05 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E1 06 E1 04 E1 02 C1 00 |

Table 975 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 05 D1 01 82 04 00 00 00 00 84 82 00 1C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0C E1 0A E1 08 E1 06 E1 04 C1 02 01 00 |

### Property Group 2.1.2.nnn Device Firmware Identification Information

#### Property Subgroup 2.1.2.1.nn Boot Firmware Information

##### Property 2.1.2.1.1.2 Boot1 Firmware Version

Table 976 - Property 2.1.2.1.1.2 Boot1 Firmware Version

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.1.1.2 / 0x020102010102</td>
</tr>
<tr>
<td>Name</td>
<td>Boot 1 Firmware Version</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its bootloader firmware
version number in the form <strong>PartNumber-Version-PCI</strong>,
padded with null characters.</p>
<p>Example: 1000007536-A0-PCI</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>19</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>19</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 977 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 05 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E1 04 E1 02 C2 00 |

Table 978 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 05 D1 01 82 04 00 00 00 00 84 82 00 2D D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1D E1 1B E2 19 E1 17 E1 15 C2 13 31 30 30 30 30 30 37 35 33 36 2D 41 30 2D 50 43 49 00 00 |

##### Property 2.1.2.1.1.4 Boot1 Firmware Part Number

Table 979 - Property 2.1.2.1.1.4 Boot1 Firmware Part Number

| Property Description |  |
|----|----|
| Property OID | 2.1.2.1.1.4 / 0x020102010104 |
| Name | Boot 1 Firmware Part Number |
| Description | The device uses this property to report its bootloader firmware part number as a string, padded with null characters. |
| Securing Key | None |
| Min. Len (b) | 11 |
| Max. Len (b) | 11 |
| Data Type | Alphanumeric |
| Valid Values | Any string |
| Default |  |

Table 980 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 03 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E1 04 E1 02 C4 00 |

Table 981 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 03 D1 01 82 04 00 00 00 00 84 82 00 25 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 15 E1 13 E2 11 E1 0F E1 0D C4 0B 31 30 30 30 30 30 37 35 33 36 00 |

##### Property 2.1.2.1.2.2 Boot0 Firmware Version

Table 982 - Property 2.1.2.1.2.2 Boot0 Firmware Version

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.1.2.2 / 0x020102010202</td>
</tr>
<tr>
<td>Name</td>
<td>Boot 0 Firmware Version</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its bootloader firmware
version number in the form <strong>PartNumber-Version-PCI</strong>,
padded with null characters.</p>
<p>Example: 1000007535-A0-PCI</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>19</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>19</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 983 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 05 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E1 04 E2 02 C2 00 |

Table 984 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 05 D1 01 82 04 00 00 00 00 84 82 00 2D D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1D E1 1B E2 19 E1 17 E1 15 C2 13 31 30 30 30 30 30 37 35 33 35 2D 41 30 2D 50 43 49 00 00 |

##### Property 2.1.2.1.2.4 Boot0 Firmware Part Number

| Property Description |  |
|----|----|
| Property OID | 2.1.2.1.2.4 / 0x020102010204 |
| Name | Boot 0 Firmware Part Number |
| Description | The device uses this property to report its bootloader firmware part number as a string, padded with null characters. |
| Securing Key | None |
| Min. Len (b) | 11 |
| Max. Len (b) | 11 |
| Data Type | Alphanumeric |
| Valid Values | Any string |
| Default |  |

Table 985 - Property 2.1.2.1.2.4 Boot0 Firmware Part Number

| Example (Hex) |
|----|
| AA 00 81 04 01 0A D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E1 04 E2 02 C4 00 |

Table 986 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0A D1 01 82 04 00 00 00 00 84 82 00 25 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 15 E1 13 E2 11 E1 0F E2 0D C4 0B 31 30 30 30 30 30 37 35 33 35 00 |

Table 987 - Get Response Example

#### Property Subgroup 2.1.2.2.nn Core Firmware Information

##### Property 2.1.2.2.2.1 Device Model Name

Table 988 - Property 2.1.2.2.2.1 Device Model Name

| Property Description |  |
|----|----|
| Property OID | 2.1.2.2.2.1 / 0x020102020201 |
| Name | Device Model Name |
| Description | The device uses this property to report its model name as string, padded with null characters. |
| Securing Key | None |
| Min. Len (b) | 10 |
| Max. Len (b) | 20 |
| Data Type | Alphanumeric |
| Valid Values | Any string |
| Default |  |

Table 989 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E2 04 E2 02 C1 00 |

Table 990 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 27 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 17 E1 15 E2 13 E2 11 E2 0F C1 0D 44 79 6E 61 46 6C 65 78 20 50 72 6F 00 |

##### Property 2.1.2.2.2.2 Main Firmware Version

Table 991 - Property 2.1.2.2.2.2 Main Firmware Version

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.2.2.2 / 0x020102020202</td>
</tr>
<tr>
<td>Name</td>
<td>Main Firmware Version</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its main firmware version
number in the form <strong>PartNumber-Version-PCI</strong>, padded with
null characters.</p>
<p>Example: 1000007183-A0-PCI</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>19</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>19</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 992 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 08 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E2 04 E2 02 C2 00 |

Table 993 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 08 D1 01 82 04 00 00 00 00 84 82 00 2D D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1D E1 1B E2 19 E2 17 E2 15 C2 13 31 30 30 30 30 30 37 31 38 33 2D 41 31 2D 50 43 49 00 00 |

##### Property 2.1.2.2.2.4 Main Firmware Part Number

Table 994 - Property 2.1.2.2.2.4 Main Firmware Part Number

| Property Description |  |
|----|----|
| Property OID | 2.1.2.2.2.4 / 0x020102020204 |
| Name | Main Firmware Part Number |
| Description | The device uses this property to report its main firmware part number as a string, padded with null characters. |
| Securing Key | None |
| Min. Len (b) | 11 |
| Max. Len (b) | 11 |
| Data Type | Alphanumeric |
| Valid Values | Any string |
| Default |  |

Table 995 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0A D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E2 04 E2 02 C4 00 |

Table 996 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0A D1 01 82 04 00 00 00 00 84 82 00 25 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 15 E1 13 E2 11 E2 0F E2 0D C4 0B 31 30 30 30 30 30 37 31 38 33 00 |

##### Property 2.1.2.2.2.6 Key Type

Table 997 - Property 2.1.2.2.2.6 Key Type

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.2.2.6 / 0x020102020206</td>
</tr>
<tr>
<td>Name</td>
<td>Key Type</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device’s firmware can be compiled to use one of two available
ECDSA P-521 key sets when signing and verifying the signature in
<strong>Command 0xEEEE - Send Secured Command to Device</strong>.</p>
<p>This property indicates which of the two keys the firmware is
configured to expect the host and device to use:</p>
<ul>
<li><p>0xFF00 = Development Key</p></li>
<li><p>Any other value = Production Key</p></li>
</ul></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>2</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 998 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 31 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E2 04 E2 02 C6 00 |

Table 999 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 31 D1 01 82 04 00 00 00 00 84 82 00 1C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0C E1 0A E2 08 E2 06 E2 04 C6 02 FF 00 |

#### Property Subgroup 2.1.2.3.nn EMV Firmware Information 

##### Property 2.1.2.3.1.1 Encryption ID (MAGTEK INTERNAL ONLY FOR NOW)

##### Property 2.1.2.3.1.2 Encryption Checksum (MAGTEK INTERNAL ONLY FOR NOW)

##### Property 2.1.2.3.2.1 EMV Contact L1 Kernel ID (Contact Only)

Table 1000 - Property 2.1.2.3.2.1 EMV Contact L1 Kernel ID (Contact
Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.2.1 / 0x020102030201</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contact L1 Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contact L1 Kernel
ID as string, padded with null characters.</p>
<p>Example: CT L1 EMVCO 4.3C</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>17</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>17</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1001 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 12 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E2 02 C1 00 |

Table 1002 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 12 D1 01 82 04 00 00 00 00 84 82 00 2B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1B E1 19 E2 17 E3 15 E2 13 C1 11 43 54 20 4C 31 20 45 4D 56 43 4F 20 34 2E 33 43 00 |

##### Property 2.1.2.3.2.2 EMV Contact L1 Kernel Firmware Part Number (Contact Only)

Table 1003 - Property 2.1.2.3.2.2 EMV Contact L1 Kernel Firmware Part
Number (Contact Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.2.2 / 0x020102030202</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contact L1 Kernel Firmware Part Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contact L1 Kernel
Part Number as string, padded with null characters.</p>
<p>Example: 1000007176 Ver A</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>17</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>17</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1004 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 13 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E2 02 C2 00 |

Table 1005 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 13 D1 01 82 04 00 00 00 00 84 82 00 2B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1B E1 19 E2 17 E3 15 E2 13 C2 11 31 30 30 30 30 30 37 31 37 36 20 56 65 72 20 41 00 |

##### Property 2.1.2.3.3.1 EMV Contact L2 Kernel ID (Contact Only)

Table 1006 - Property 2.1.2.3.3.1 EMV Contact L2 Kernel ID (Contact
Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.3.1 / 0x020102030301</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contact L2 Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contact L2 Kernel
ID as string, padded with null characters.</p>
<p>Example: CT L2 4.3K</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>11</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>11</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1007 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 15 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E3 02 C1 00 |

Table 1008 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 16 D1 01 82 04 00 00 00 00 84 82 00 25 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 15 E1 13 E2 11 E3 0F E3 0D C1 0B 43 54 20 4C 32 20 34 2E 33 4B 00 |

##### Property 2.1.2.3.3.2 EMV Contact L2 Kernel Firmware Part Number(Contact Only)

Table 1009 - Property 2.1.2.3.3.2 EMV Contact L2 Kernel Firmware Part
Number(Contact Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.3.2 / 0x020102030302</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contact L2 Kernel Firmware Part Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contact L2 Kernel
Part Number as string, padded with null characters.</p>
<p>Example: 1000008878 Ver A DynaFlex PED L2 Kernel</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>40</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>40</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1010 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1A D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E3 02 C2 00 |

Table 1011 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 1A D1 01 82 04 00 00 00 00 84 82 00 42 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 32 E1 30 E2 2E E3 2C E3 2A C2 28 31 30 30 30 30 30 38 38 37 38 20 56 65 72 20 41 20 44 79 6E 61 46 6C 65 78 20 50 45 44 20 4C 32 20 4B 65 72 6E 65 6C 00 |

##### Property 2.1.2.3.3.3 EMV Contact L2 Kernel Checksum (Contact Only)

Table 1012 - Property 2.1.2.3.3.3 EMV Contact L2 Kernel Checksum
(Contact Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.3.3/ 0x020102030303</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contact L2 Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contact L2 Kernel
Checksum as string, no padding.</p>
<p>Example: vxxCAAgnos33_17
b54f31bcb61a26fc823bce9ab8989b31ab90f9a4</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Variable</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>75</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1013 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1B D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E3 02 C3 00 |

Table 1014 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 1B D1 01 82 04 00 00 00 00 84 82 00 52 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 42 E1 40 E2 3E E3 3C E3 3A C3 38 76 78 78 43 41 41 67 6E 6F 73 33 33 5F 31 37 20 62 35 34 66 33 31 62 63 62 36 31 61 32 36 66 63 38 32 33 62 63 65 39 61 62 38 39 38 39 62 33 31 61 62 39 30 66 39 61 34 |

##### Property 2.1.2.3.3.4 EMV Contact L2 Kernel Configuration Checksum (Contact Only)

Table 1015 - Property 2.1.2.3.3.4 EMV Contact L2 Kernel Configuration
Checksum (Contact Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.3.4/ 0x020102030304</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contact L2 Kernel Configuration Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contact L2 Kernel
Configuration Checksum as string, no padding.</p>
<p>Example: 17AC3C4A</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>8</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>8</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1016 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 1F D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E3 02 C4 00 |

Table 1017 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 1F D1 01 82 04 00 00 00 00 84 82 00 1E D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0E E1 0C E2 0A E3 08 E3 06 C4 04 17 AC 3C 4A |

##### Property 2.1.2.3.4.1 EMV Contactless L1 Kernel ID (Contactless Only)

Table 1018 - Property 2.1.2.3.4.1 EMV Contactless L1 Kernel ID
(Contactless Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.4.1 / 0x020102030401</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contactless L1 Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contactless L1
Kernel ID as string, padded with null characters.</p>
<p>Example: CL L1 EMVCO 3.0</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1019 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 21 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E4 02 C1 00 |

Table 1020 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 21 D1 01 82 04 00 00 00 00 84 82 00 2A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1A E1 18 E2 16 E3 14 E4 12 C1 10 43 4C 20 4C 31 20 45 4D 56 43 4F 20 33 2E 30 00 |

##### Property 2.1.2.3.4.2 EMV Contactless L1 Kernel Firmware Part Number (Contactless Only)

Table 1021 - Property 2.1.2.3.4.2 EMV Contactless L1 Kernel Firmware
Part Number (Contactless Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.4.2 / 0x020102030402</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contactless L1 Kernel Firmware Part Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contactless L1
Kernel Part Number as string, padded with null characters.</p>
<p>Example: 1000007177 Ver A</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>17</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>17</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1022 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 25 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E4 02 C2 00 |

Table 1023 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 25 D1 01 82 04 00 00 00 00 84 82 00 2B D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1B E1 19 E2 17 E3 15 E4 13 C2 11 31 30 30 30 30 30 37 31 37 37 20 56 65 72 20 41 00 |

##### Property 2.1.2.3.4.3 EMV Contactless L1 Kernel Checksum (Contactless Only)

Table 1024 - Property 2.1.2.3.4.3 EMV Contactless L1 Kernel Checksum
(Contactless Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.4.3/ 0x020102030403</td>
</tr>
<tr>
<td>Name</td>
<td>EMV Contactless L1 Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the EMV Contactless L1
Kernel Checksum as string, no padding.</p>
<p>Example: d3c5d413334178d1d5929a752b8d29adc1e5829c</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Variable</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>75</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1025 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 26 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E4 02 C3 00 |

Table 1026 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 26 D1 01 82 04 00 00 00 00 84 82 00 42 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 32 E1 30 E2 2E E3 2C E4 2A C3 28 64 33 63 35 64 34 31 33 33 33 34 31 37 38 64 31 64 35 39 32 39 61 37 35 32 62 38 64 32 39 61 64 63 31 65 35 38 32 39 63 |

##### Property 2.1.2.3.5.1 Mastercard MCL Kernel ID (Contactless Only)

Table 1027 - Property 2.1.2.3.5.1 Mastercard MCL Kernel ID (Contactless
Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.5.1 / 0x020102030501</td>
</tr>
<tr>
<td>Name</td>
<td>Mastercard MCL Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Mastercard MCL Kernel
ID as string, padded with null characters.</p>
<p>Example: MCL 3.1.3</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>10</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>10</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1028 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 28 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E5 02 C1 00 |

Table 1029 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 28 D1 01 82 04 00 00 00 00 84 82 00 24 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 14 E1 12 E2 10 E3 0E E5 0C C1 0A 4D 43 4C 20 33 2E 31 2E 33 00 |

##### Property 2.1.2.3.5.2 Mastercard MCL Kernel Firmware Part Number (Contactless Only)

Table 1030 - Property 2.1.2.3.5.2 Mastercard MCL Kernel Firmware Part
Number (Contactless Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.5.2 / 0x020102030502</td>
</tr>
<tr>
<td>Name</td>
<td>Mastercard MCL Firmware Part Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Mastercard MCL Kernel
Part Number as string, padded with null characters.</p>
<p>Example: 1000007179 Ver A0</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1031 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 29 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E5 02 C2 00 |

Table 1032 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 29 D1 01 82 04 00 00 00 00 84 82 00 2C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1C E1 1A E2 18 E3 16 E5 14 C2 12 31 30 30 30 30 30 37 31 37 39 20 56 65 72 20 41 30 00 |

##### Property 2.1.2.3.5.3 Mastercard MCL Kernel Checksum (Contactless Only)

Table 1033 - Property 2.1.2.3.5.3 Mastercard MCL Kernel Checksum
(Contactless Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.5.3/ 0x020102030503</td>
</tr>
<tr>
<td>Name</td>
<td>Mastercard MCL Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Mastercard MCL Kernel
Checksum as string, no padding.</p>
<p>Example: C2.2.8 -&gt; v1.0.2
[ade94c13b0c6a31f1be682b12536528264b1efc0]</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Variable</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>75</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1034 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 2A D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E5 02 C3 00 |

Table 1035 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 2A D1 01 82 04 00 00 00 00 84 82 00 55 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 45 E1 43 E2 41 E3 3F E5 3D C3 3B 43 32 2E 32 2E 38 20 2D 3E 20 76 31 2E 30 2E 32 20 5B 61 64 65 39 34 63 31 33 62 30 63 36 61 33 31 66 31 62 65 36 38 32 62 31 32 35 33 36 35 32 38 32 36 34 62 31 65 66 63 30 5D |

##### Property 2.1.2.3.6.1 Visa payWave Kernel ID (Contactless Only)

Table 1036 - Property 2.1.2.3.6.1 Visa payWave Kernel ID (Contactless
Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.6.1 / 0x020102030601</td>
</tr>
<tr>
<td>Name</td>
<td>Visa payWave Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Visa payWave Kernel
ID as string, padded with null characters.</p>
<p>Example: PayWave 2.2</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>12</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>12</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1037 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 03 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E6 02 C1 00 |

Table 1038 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 03 D1 01 82 04 00 00 00 00 84 82 00 26 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 16 E1 14 E2 12 E3 10 E6 0E C1 0C 50 61 79 57 61 76 65 20 32 2E 32 00 |

##### Property 2.1.2.3.6.2 Visa payWave Kernel Firmware Part Number (Contactless Only)

Table 1039 - Property 2.1.2.3.6.2 Visa payWave Kernel Firmware Part
Number (Contactless Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.6.2 / 0x020102030602</td>
</tr>
<tr>
<td>Name</td>
<td>Visa payWave Firmware Part Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Visa payWave Kernel
Part Number as string, padded with null characters.</p>
<p>Example: 1000007180 Ver A1</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1040 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 05 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E6 02 C2 00 |

Table 1041 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 05 D1 01 82 04 00 00 00 00 84 82 00 2C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1C E1 1A E2 18 E3 16 E6 14 C2 12 31 30 30 30 30 30 37 31 38 30 20 56 65 72 20 41 31 00 |

##### Property 2.1.2.3.6.3 Visa payWave Kernel Checksum (Contactless Only)

Table 1042 - Property 2.1.2.3.6.3 Visa payWave Kernel Checksum
(Contactless Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.6.3/ 0x020102030603</td>
</tr>
<tr>
<td>Name</td>
<td>Visa payWave Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Visa payWave Kernel
Checksum as string, no padding.</p>
<p>Example: VCPS 2.2x [00000000]-&gt; v1.5.6
[F1CBB8A23E00984E9E753EF4884C33EA368E570C]</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Variable</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>75</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1043 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E6 02 C3 00 |

Table 1044 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 62 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 52 E1 50 E2 4E E3 4C E6 4A C3 48 56 43 50 53 20 32 2E 32 78 20 5B 30 30 30 30 30 30 30 30 5D 2D 3E 20 76 31 2E 35 2E 36 20 5B 46 31 43 42 42 38 41 32 33 45 30 30 39 38 34 45 39 45 37 35 33 45 46 34 38 38 34 43 33 33 45 41 33 36 38 45 35 37 30 43 5D |

##### Property 2.1.2.3.6.5 Entry Point Checksum (Contactless Only)(Common Kernel Only)

Table 1045 - Property 2.1.2.3.6.5 Entry Point Checksum (Contactless
Only)(Common Kernel Only)(Common Kernel Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.6.5/ 0x020102030605</td>
</tr>
<tr>
<td>Name</td>
<td>Entry Point Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Entry Point Checksum
as string, no padding.</p>
<p>Example: 1B3725A7DBC220805DF369E035E935EF404C4B71</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Variable</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>75</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1046 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E6 02 C5 00 |

Table 1047 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 42 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 32 E1 30 E2 2E E3 2C E6 2A C5 28 31 42 33 37 32 35 41 37 44 42 43 32 32 30 38 30 35 44 46 33 36 39 45 30 33 35 45 39 33 35 45 46 34 30 34 43 34 42 37 31 |

##### Property 2.1.2.3.7.1 Discover D-PAS Kernel ID (Contactless Only)

Table 1048 - Property 2.1.2.3.7.1 Discover D-PAS Kernel ID (Contactless
Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.7.1 / 0x020102030701</td>
</tr>
<tr>
<td>Name</td>
<td>Discover D-PAS Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Discover D-PAS Kernel
ID as string, padded with null characters.</p>
<p>Example: DPAS 1.0</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>9</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>9</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1049 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 07 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E7 02 C1 00 |

Table 1050 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 07 D1 01 82 04 00 00 00 00 84 82 00 23 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 13 E1 11 E2 0F E3 0D E7 0B C1 09 44 50 41 53 20 31 2E 30 00 |

##### Property 2.1.2.3.7.2 Discover D-PAS Kernel Firmware Part Number (Contactless Only)

Table 1051 – Property 2.1.2.3.7.2 Discover D-PAS Kernel Firmware Part
Number (Contactless Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.7.2 / 0x020102030702</td>
</tr>
<tr>
<td>Name</td>
<td>Discover D-PAS Firmware Part Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Discover D-PAS Kernel
Part Number as string, padded with null characters.</p>
<p>Example: 1000007181 Ver A0</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1052 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 09 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E7 02 C2 00 |

Table 1053 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 09 D1 01 82 04 00 00 00 00 84 82 00 2C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1C E1 1A E2 18 E3 16 E7 14 C2 12 31 30 30 30 30 30 37 31 38 31 20 56 65 72 20 41 30 00 |

##### Property 2.1.2.3.7.3 Discover D-PAS Kernel Checksum (Contactless Only)

Table 1054 - Property 2.1.2.3.7.3 Discover D-PAS Kernel Checksum
(Contactless Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.7.3/ 0x020102030703</td>
</tr>
<tr>
<td>Name</td>
<td>Discover D-PAS Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Discover D-PAS Kernel
Checksum as string, no padding.</p>
<p>Example: DPAS 1.0 + TAS 00x -&gt; v1.3.42
[e28bf053de947cf6ad456a2a7c71059a2c5ac61e]</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Variable</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>75</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1055 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0C D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E7 02 C3 00 |

Table 1056 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0C D1 01 82 04 00 00 00 00 84 82 00 62 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 52 E1 50 E2 4E E3 4C E7 4A C3 48 44 50 41 53 20 31 2E 30 20 2B 20 54 41 53 20 30 30 78 20 2D 3E 20 76 31 2E 33 2E 34 32 20 5B 65 32 38 62 66 30 35 33 64 65 39 34 37 63 66 36 61 64 34 35 36 61 32 61 37 63 37 31 30 35 39 61 32 63 35 61 63 36 31 65 5D |

##### Property 2.1.2.3.8.1 American Express Expresspay Kernel ID (Contactless Only)

Table 1057 - Property 2.1.2.3.8.1 American Express Expresspay Kernel ID
(Contactless Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.8.1 / 0x020102030801</td>
</tr>
<tr>
<td>Name</td>
<td>American Express Expresspay Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the American Express
Expresspay Kernel ID as string, padded with null characters.</p>
<p>Example: AMEX 4.0.2</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>11</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>11</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1058 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E8 02 C1 00 |

Table 1059 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0E D1 01 82 04 00 00 00 00 84 82 00 25 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 15 E1 13 E2 11 E3 0F E8 0D C1 0B 41 4D 45 58 20 34 2E 30 2E 32 00 |

##### Property 2.1.2.3.8.2 American Express Expresspay Kernel Firmware Part Number (Contactless Only)

Table 1060 – Property 2.1.2.3.8.2 American Express Expresspay Kernel
Firmware Part Number (Contactless Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.8.2 / 0x020102030802</td>
</tr>
<tr>
<td>Name</td>
<td>American Express Expresspay Firmware Part Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the American Express
Expresspay Part Number as string, padded with null characters.</p>
<p>Example: 1000007181 Ver A0</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1061 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0F D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E8 02 C2 00 |

Table 1062 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 0F D1 01 82 04 00 00 00 00 84 82 00 2C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1C E1 1A E2 18 E3 16 E8 14 C2 12 31 30 30 30 30 30 37 31 38 32 20 56 65 72 20 41 30 00 |

##### Property 2.1.2.3.8.3 American Express Expresspay Kernel Checksum (Contactless Only)

Table 1063 - Property 2.1.2.3.8.3 American Express Expresspay Kernel
Checksum (Contactless Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.8.3/ 0x020102030803</td>
</tr>
<tr>
<td>Name</td>
<td>American Express Expresspay Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the American Express
Expresspay Kernel Checksum as string, no padding.</p>
<p>Example: C4.2.7 -&gt; v1.0.6
[5D5CC3073F64FE7F14F5454D62026EDB9E202930]</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Variable</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>75</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1064 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 11 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E8 02 C3 00 |

Table 1065 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 11 D1 01 82 04 00 00 00 00 84 82 00 55 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 45 E1 43 E2 41 E3 3F E8 3D C3 3B 43 34 2E 32 2E 37 20 2D 3E 20 76 31 2E 30 2E 36 20 5B 35 44 35 43 43 33 30 37 33 46 36 34 46 45 37 46 31 34 46 35 34 35 34 44 36 32 30 32 36 45 44 42 39 45 32 30 32 39 33 30 5D |

##### Property 2.1.2.3.9.1 Apple VAS Kernel ID

Table 1066 - Property 2.1.2.3.9.1 Apple VAS Kernel ID

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.9.1 / 0x020102030901</td>
</tr>
<tr>
<td>Name</td>
<td>Apple VAS Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Apple VAS Kernel ID
as a string, padded with null characters.</p>
<p>Example: APPLE VAS 1.0.0</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1067 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 E9 02 C1 00 |

Table 1068 - Get Response Example

| Example (Hex) |
|----|
| AA008104820ED1018204000000008482002AD10181072B06010401F609850102891AE118E216E314E912C1104150504C452056415320312E302E3000 |

##### Property 2.1.2.3.A.1 JCB Kernel ID (Contactless Only) (Common Kernel Only)

Table 1069 - Property 2.1.2.3.A.1 JCB Kernel ID (Contactless Only)
(Common Kernel Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.A.1 / 0x020102030A01</td>
</tr>
<tr>
<td>Name</td>
<td>JCB Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the JCB Kernel ID as
string, padded with null characters.</p>
<p>Example: JCB 1.6</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>11</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>11</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1070 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EA 02 C1 00 |

Table 1071 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 22 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 12 E1 10 E2 0E E3 0C EA 0A C1 08 4A 43 42 20 31 2E 36 00 |

##### Property 2.1.2.3.A.2 JCB Kernel Firmware Part Number (Contactless Only) (Common Kernel Only)

Table 1072 – Property 2.1.2.3.A.2 JCB Kernel Firmware Part Number
(Contactless Only) (Common Kernel Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.A.2 / 0x020102030A02</td>
</tr>
<tr>
<td>Name</td>
<td>JCB Firmware Part Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the JCB Part Number as
string, padded with null characters.</p>
<p>Example: 1000009650 Ver A0</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1073 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0F D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EA 02 C2 00 |

Table 1074 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 2D D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1D E1 1B E2 19 E3 17 EA 15 C2 13 31 30 30 30 30 30 39 36 35 30 20 56 65 72 20 41 41 30 00 |

##### Property 2.1.2.3.A.3 JCB Kernel Checksum (Contactless Only) (Common Kernel Only)

Table 1075 - Property 2.1.2.3.A.3 JCB Kernel Checksum (Contactless Only)
(Common Kernel Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.A.3/ 0x020102030A03</td>
</tr>
<tr>
<td>Name</td>
<td>JCB Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the JCB Kernel Checksum
as string, no padding.</p>
<p>Example: JCB 1.6 -&gt; v1.0.29
[ca44a90cd42d379088fcb8ca8d1fab195546b278]</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Variable</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>75</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1076 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 11 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EA 02 C3 00 |

Table 1077 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 57 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 47 E1 45 E2 43 E3 41 EA 3F C3 3D 4A 43 42 20 31 2E 36 20 2D 3E 20 76 31 2E 30 2E 32 39 20 5B 63 61 34 34 61 39 30 63 64 34 32 64 33 37 39 30 38 38 66 63 62 38 63 61 38 64 31 66 61 62 31 39 35 35 34 36 62 32 37 38 5D |

##### Property 2.1.2.3.A.4 Reader Core Checksum (Contactless Only) (Common Kernel Only)

Table 1078 - Property 2.1.2.3.A.4 Reader Core Checksum (Contactless
Only) (Common Kernel Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.A.4/ 0x020102030A04</td>
</tr>
<tr>
<td>Name</td>
<td>Reader Core Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Reader Core Checksum
as string, no padding.</p>
<p>Example: 371835cedcd7f8a3e4cf8b32cc03803dfdc1f507</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Variable</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>75</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1079 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 11 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EA 02 C4 00 |

Table 1080 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 42 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 32 E1 30 E2 2E E3 2C EA 2A C4 28 33 37 31 38 33 35 63 65 64 63 64 37 66 38 61 33 65 34 63 66 38 62 33 32 63 63 30 33 38 30 33 64 66 64 63 31 66 35 30 37 |

##### Property 2.1.2.3.A.5 Entry Point Checksum (Contactless Only) (Common Kernel Only)

Table 1081 - Property 2.1.2.3.A.5 Entry Point Checksum (Contactless
Only) (Common Kernel Only) (Common Kernel Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.A.5/ 0x020102030A05</td>
</tr>
<tr>
<td>Name</td>
<td>Entry Point Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Entry Point Checksum
as string, no padding.</p>
<p>Example: 1B3725A7DBC220805DF369E035E935EF404C4B71</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Variable</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>75</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1082 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EA 02 C5 00 |

Table 1083 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 42 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 32 E1 30 E2 2E E3 2C EA 2A C5 28 31 42 33 37 32 35 41 37 44 42 43 32 32 30 38 30 35 44 46 33 36 39 45 30 33 35 45 39 33 35 45 46 34 30 34 43 34 42 37 31 |

##### Property 2.1.2.3.B.1 China Union Pay Kernel ID (Contactless Only) (Common Kernel Only)

Table 1084 - Property 2.1.2.3.B.1 China Union Pay Kernel ID (Contactless
Only) (Common Kernel Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.B.1 / 0x020102030B01</td>
</tr>
<tr>
<td>Name</td>
<td>China Union Pay Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the China Union Pay
Kernel ID as string, padded with null characters.</p>
<p>Example: CUP 1.0.2</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>11</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>11</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1085 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EB 02 C1 00 |

Table 1086 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 24 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 14 E1 12 E2 10 E3 0E EB 0C C1 0A 43 55 50 20 31 2E 30 2E 32 00 |

##### Property 2.1.2.3.B.2 China Union Pay Kernel Firmware Part Number (Contactless Only) (Common Kernel Only)

Table 1087 – Property 2.1.2.3.B.2 China Union Pay Kernel Firmware Part
Number (Contactless Only) (Common Kernel Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.B.2 / 0x020102030B02</td>
</tr>
<tr>
<td>Name</td>
<td>China Union Pay Firmware Part Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the China Union Pay Part
Number as string, padded with null characters.</p>
<p>Example: 1000009651 Ver AA0</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1088 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0F D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EB 02 C2 00 |

Table 1089 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 2D D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1D E1 1B E2 19 E3 17 EB 15 C2 13 31 30 30 30 30 30 39 36 35 31 20 56 65 72 20 41 41 30 00 |

##### Property 2.1.2.3.B.3 China Union Pay Kernel Checksum (Contactless Only) (Common Kernel Only)

Table 1090 - Property 2.1.2.3.B.3 China Union Pay Kernel Checksum
(Contactless Only) (Common Kernel Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.B.3/ 0x020102030B03</td>
</tr>
<tr>
<td>Name</td>
<td>China Union Pay Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the China Union Pay
Kernel Checksum as string, no padding.</p>
<p>Example: CUP v1.0.2 -&gt; v1.3.40
[23e9bc82b4ecbf422c2054c91914848017e0ed0f]</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Variable</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>75</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1091 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 11 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EB 02 C3 00 |

Table 1092 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 5A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 4A E1 48 E2 46 E3 44 EB 42 C3 40 43 55 50 20 76 31 2E 30 2E 32 20 2D 3E 20 76 31 2E 33 2E 34 30 20 5B 32 33 65 39 62 63 38 32 62 34 65 63 62 66 34 32 32 63 32 30 35 34 63 39 31 39 31 34 38 34 38 30 31 37 65 30 65 64 30 66 5D |

##### Property 2.1.2.3.C.1 Interact Flash Kernel ID (Contactless Only) (Common Kernel Only)

Table 1093 - Property 2.1.2.3.C.1 Interact Flash Kernel ID (Contactless
Only) (Common Kernel Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.C.1 / 0x020102030C01</td>
</tr>
<tr>
<td>Name</td>
<td>Interact Flash Kernel ID</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Interact Flash Kernel
ID as string, padded with null characters.</p>
<p>Example: FLASH 1.9</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>11</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>11</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1094 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0E D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EC 02 C1 00 |

Table 1095 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 24 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 14 E1 12 E2 10 E3 0E EC 0C C1 0A 46 4C 41 53 48 20 31 2E 39 00 |

##### Property 2.1.2.3.C.2 Interact Flash Kernel Firmware Part Number (Contactless Only) (Common Kernel Only)

Table 1096 – Property 2.1.2.3.C.2 Interact Flash Kernel Firmware Part
Number (Contactless Only) (Common Kernel Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.C.2 / 0x020102030C02</td>
</tr>
<tr>
<td>Name</td>
<td>Interact Flash Firmware Part Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Interact Flash Part
Number as string, padded with null characters.</p>
<p>Example: 1000009652 Ver AA0</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1097 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 0F D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EC 02 C2 00 |

Table 1098 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 2D D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 1D E1 1B E2 19 E3 17 EC 15 C2 13 31 30 30 30 30 30 39 36 35 32 20 56 65 72 20 41 41 30 00 |

##### Property 2.1.2.3.C.3 Interact Flash Kernel Checksum (Contactless Only) (Common Kernel Only)

Table 1099 - Property 2.1.2.3.C.3 Interact Flash Kernel Checksum
(Contactless Only) (Common Kernel Only)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.3.C.3/ 0x020102030C03</td>
</tr>
<tr>
<td>Name</td>
<td>Interact Flash Kernel Checksum</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the Interact Flash Kernel
Checksum as string, no padding.</p>
<p>Example: Flash 1.9 -&gt; v1.3.41
[394e45aed865e276e4f6737de26aa84c6eb1b174]</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Variable</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>75</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1100 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 11 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E1 08 E2 06 E3 04 EC 02 C3 00 |

Table 1101 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 06 D1 01 82 04 00 00 00 00 84 82 00 59 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 49 E1 47 E2 45 E3 43 EC 41 C3 3F 46 6C 61 73 68 20 31 2E 39 20 2D 3E 20 76 31 2E 33 2E 34 31 20 5B 33 39 34 65 34 35 61 65 64 38 36 35 65 32 37 36 65 34 66 36 37 33 37 64 65 32 36 61 61 38 34 63 36 65 62 31 62 31 37 34 5D |

#### Property Subgroup 2.1.2.4.nn Main Application Firmware Information (MAGTEK INTERNAL ONLY FOR NOW)

#### Property Subgroup 2.1.2.5.nn WLAN Information (WLAN Only)

##### Property 2.1.2.5.3.1 WLAN Firmware Version

Table 1102 - Property 2.1.2.5.3.1 WLAN Firmware Version

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.5.3.1 / 0x020102050301</td>
</tr>
<tr>
<td>Name</td>
<td>WLAN Firmware Version</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its WLAN firmware version
number in the form <strong>PartNumber-Version-PCI</strong>, padded with
null characters.</p>
<p>Example: 1000007537-A0-PCI</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1103 - Get Request Example

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA0081040108D101841AD10181072B06010401F609850102890AE108E206E504E302C100 |

Table 1104 - Get Response Example

| Example (Hex) |
|----|
| AA0081048208D1018204000000008482002CD10181072B06010401F609850102891CE11AE218E516E314C112313030303030383633352D31302D44455600 |

##### Property 2.1.2.5.3.2 WLAN WiFi Module Build Hash (MAGTEK INTERNAL ONLY)

Table 1105 - Property 2.1.2.5.3.2 WLAN WiFi Module Build Hash (MAGTEK
INTERNAL ONLY) (MAGTEL INTERNAL ONLY)

| Property Description |  |
|----|----|
| Property OID | 2.1.2.5.3.2 / 0x020102050302 |
| Name | WLAN WiFi Module MAC Build Hash |
| Description | The device uses this property to report its WiFi module Build Hash. |
| Securing Key | None |
| Min. Len (b) | 18 |
| Max. Len (b) | 6 |
| Data Type | Binary |
| Valid Values | IEEE 802 EUI-48 |
| Default | None |

Table 1106 - Get Request Example

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA0081040108D101841AD10181072B06010401F609850102890AE108E206E504E302C200 |

Table 1107 - Get Response Example

| Example (Hex) |
|----|
| AA0081048208D1018204000000008482002CD10181072B06010401F609850102891CE11AE218E516E314C212623233626639333900000000000000000000 |

##### Property 2.1.2.5.3.3 WLAN Firmware Sequence Number (MAGTEK INTERNAL ONLY)

Table 8.5‑91 - Property 2.1.2.5.3.3 WLAN Firmware Sequence Number
(MAGTEK INTERNAL ONLY)

| Property Description |  |
|----|----|
| Property OID | 2.1.2.5.3.3 / 0x020102050303 |
| Name | WLAN Firmware Sequence Number |
| Description | The device uses this property to report its WLAN firmware sequence number. |
| Securing Key | None |
| Min. Len (b) | 4 |
| Max. Len (b) | 4 |
| Data Type | Binary |
| Valid Values | Any |
| Default | None |

Table 8.5‑92 - Get Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA0081040155D101840FD1018501028704010205038902C300 |

Table 8.5‑93 - Get Response Example

| Example (Hex) |
|----|
| AA0081048255D10182040000000084820013D1018501028704010205038906C3040000001D |

##### Property 2.1.2.5.6.1 WLAN WiFi Module MAC Address

Table 1108 - Property 2.1.2.5.6.1 WLAN WiFi Module MAC AddressWLAN WiFi
Module MAC Address

| Property Description |  |
|----|----|
| Property OID | 2.1.2.5.6.1 / 0x020102050601 |
| Name | WLAN WiFi Module MAC Address |
| Description | The device uses this property to report its WiFi module MAC address. |
| Securing Key | None |
| Min. Len (b) | 6 |
| Max. Len (b) | 6 |
| Data Type | Binary |
| Valid Values | IEEE 802 EUI-48 |
| Default | None |

Table 1109 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104010ED101 841AD101 81072B06010401F609 850102 890AE108E206E504E602C100 |

Table 1110 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104820ED101 820400000000 84820020D101 81072B06010401F609 850102 8910E10EE20CE50AE608C1 06C47F51A41701 |

##### Property 2.1.2.5.6.2 WLAN WiFi RSSI

Table 1111 - Property 2.1.2.5.6.2 WLAN WiFi RSSIWLAN WiFi RSSI

| Property Description |  |
|----|----|
| Property OID | 2.1.2.5.6.2 / 0x020102050602 |
| Name | WLAN WiFi RSSI (Received Signal Strength Indicator) |
| Description | The device uses this property to report its WiFi RSSI. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Signed Character |
| Valid Values | 0x00 – 0xFF |
| Default | None |

Table 1112 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104010ED101 841AD101 81072B06010401F609 850102 890AE108E206E504E602C200 |

Table 1113 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104820ED101 820400000000 8482001BD101 81072B06010401F609 850102 890BE109E207E505E603C2 01BE |

##### Property 2.1.2.5.6.3 WLAN Dynamic IP Address 

Table 1114 - Property 2.1.2.5.6.3 WLAN Dynamic IP AddressWLAN Dynamic IP
Address

| Property Description |  |
|----|----|
| Property OID | 2.1.2.5.6.3 / 0x020102050603 |
| Name | WLAN Dynamic IP Address |
| Description | The device uses this property to report its WLAN Dynamic IP Address. |
| Securing Key | None |
| Min. Len (b) | 4 |
| Max. Len (b) | 4 |
| Data Type | Binary |
| Valid Values | Internet Protocol version 4 |
| Default | None |

Table 1115 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104010ED101 841AD101 81072B06010401F609 850102 890AE108E206E504E602C300 |

Table 1116 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104820ED101 820400000000 8482001ED101 81072B06010401F609 850102 890EE10CE20AE508E606C3 04C0A8017D |

##### Property 2.1.2.5.6.4 Active Client Connections

Table 1117 - Property 2.1.2.5.6.4 Active Client Connections

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.5.6.4 / 0x020102050604</td>
</tr>
<tr>
<td>Name</td>
<td>Active Client Connections</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its number of active
client connections.</p>
<p><strong>Property 1.2.2.1.1.A Maximum Client Connections</strong> is
related.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td>0x00 – 0x04</td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1118 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020506 8902 C400 |

Table 1119 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870401020506 8903 C401 01 |

##### Property 2.1.2.5.6.5 Server Certificate Chain Select

Table 1120 - Property 2.1.2.5.6.5 Server Certificate Chain Select

| Property Description |  |
|----|----|
| Property OID | 2.1.2.5.6.5 / 0x020102050605 |
| Name | Server Certificate Chain Select |
| Description | The device uses this property to report the certificate chain used for server certificate. Server Certificate Chain Select is set by loading a Trust Configuration File. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0x00 – 0x01: 0x00=client chain, 0x01=server chain |
| Default | None |

Table 1121 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020506 8902 C500 |

Table 1122 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870401020506 8903 C501 00 |

##### Property 2.1.2.5.6.6 Security Protocol

Table 1123 - Property 2.1.2.5.6.6 Security Protocol

| Property Description |  |
|----|----|
| Property OID | 2.1.2.5.6.6 / 0x020102050606 |
| Name | Security Protocol |
| Description | The device uses this property to report the security protocol. Security Protocol is set by loading a Trust Configuration File. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0x00 – 0x02: 0x00=mTLS, 0x01=TLS, 02=None |
| Default | None |

Table 1124 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020506 8902 C600 |

Table 1125 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870401020506 8903 C601 00 |

##### Property 2.1.2.5.6.7 Available Access Points

Table 1126 - Property 2.1.2.5.6.7 Available Access Points

| Property Description |  |
|----|----|
| Property OID | 2.1.2.5.6.7 / 0x020102050607 |
| Name | Available Access Points |
| Description | The device uses this property to report a list of available access points. The access points are in a list of tags starting with 0xA0 and incrementing. The list can contain up to 20 access points. Each access point contains two tags. Tag 0x80 contains the access point’s SSID. The SSID is a text string of 1 to 32 characters. Tag 0x81 is the RSSI for the access point. The RSSI is a signed binary number between -30 and -90. |
| Securing Key | None |
| Min. Len (b) | 0 |
| Max. Len (b) | 740 |
| Data Type | Binary |
| Valid Values | See **Table 8.5-146 – Access Point Payload Detail** |
| Default | None |

Table 1127 – Access Point Payload Detail

| Tag | Len | Value / Description                       | Typ | Req | Default |
|-----|-----|-------------------------------------------|-----|-----|---------|
| A0  | var | Access Point Container 1                  | T   | O   |         |
| /80 | var | Service Set Identifier (SSID)             | B   | R   |         |
| /81 | var | Received Signal Strength Indicator (RSSI) | B   | R   |         |
| A1  | var | Access Point Container 2                  | T   | O   |         |
| /80 | var | Service Set Identifier (SSID)             | B   | R   |         |
| /81 | var | Received Signal Strength Indicator (RSSI) | B   | R   |         |
| A2  | var | Access Point Container 3                  | T   | O   |         |
| /80 | var | Service Set Identifier (SSID)             | B   | R   |         |
| /81 | var | Received Signal Strength Indicator (RSSI) | B   | R   |         |
| …   |     |                                           |     |     |         |
| Ax  | var | Access Point Container x+1                | T   | O   |         |
| /80 | var | Service Set Identifier (SSID)             | B   | R   |         |
| /81 | var | Received Signal Strength Indicator (RSSI) | B   | R   |         |

Table 1128 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020506 8902 C700 |

Table 1129 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048206D101 820400000000 84820065 D101 81072B06010401F609 850102 8955E153E251E54FE64DC74B A00E80094D79416363657373318102FFC7 A10F800A4D7957694669535349448102FFA9 A22580204449524543542D46442D4850204465736B4A65742033363330207365726965738102FFA6 |

#### Property Subgroup 2.1.2.6.nn General Firmware Information (MAGTEK INTERNAL ONLY)

##### Property 2.1.2.6.1.1 Firmware Git and Build information (MAGTEK INTERNAL ONLY)

Table 1130 - Property 2.1.2.6.1.1 Firmware Git and Build information
(MAGTEK INTERNAL ONLY)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.6.1.1 / 0x020102060101</td>
</tr>
<tr>
<td>Name</td>
<td>Firmware Git and Build information</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its firmware Git and
build information. Git bash command “git describe --long --dirty
--always” is used to return information about each repository “MAIN”,
“SDK”, “EXT” and “AMADIS” in the same order followed by the date and
time the firmware was built as a null terminated string.</p>
<p>An example of the string returned is
“MAIN[PCI-A3-20200929-61-g46efa1a-dirty]_SDK[PCI-A2-NO-LCD-20200930-2-g6b69d7f]_EXT[PCI-A3-20200929-14-g370c7f0]_AMADIS[PCI-A2-NO-LCD-20200930-4-g5957fb6]_[2020-11-17][14:48:03]”
where:</p>
<ul>
<li><p>“MAIN” means the main repository</p></li>
<li><p>“PCI-A3-20200929” is the last tag found in this
repository</p></li>
<li><p>“61” means there have been 61 commits made since this
tag</p></li>
<li><p>“g46efa1a” means the hash of the latest commit starts with
46efa1a</p></li>
<li><p>“dirty” means that the repository has uncommitted changes made
since the last commit</p></li>
<li><p>“[2020-11-17][14:48:03]” is the date and time the firmware was
built.</p></li>
</ul></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>Compile time dependent</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>Compile time dependent</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1131 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020601 8902 C100 |

Table 1132 - Get Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA00 8104 8255D101 8204 00000000 848200C4 D101 8501 02 8704
01020601 898200B5 C18200B1
4D41494E5B5043492D41332D32303230303932392D36312D67343665666131612D64697274795D5F53444B5B5043492D41322D4E4F2D4C43442D32303230303933302D322D67366236396437665D5F4558545B5043492D41332D32303230303932392D31342D67333730633766305D5F414D414449535B5043492D41322D4E4F2D4C43442D32303230303933302D342D67353935376662365D5F5B323032302D31312D31375D5B31343A34383A30335D00</p>
<p>Text value:
MAIN[PCI-A3-20200929-61-g46efa1a-dirty]_SDK[PCI-A2-NO-LCD-20200930-2-g6b69d7f]_EXT[PCI-A3-20200929-14-g370c7f0]_AMADIS[PCI-A2-NO-LCD-20200930-4-g5957fb6]_[2020-11-17][14:48:03]</p></td>
</tr>
</tbody>
</table>

#### Property Subgroup 2.1.2.7.nn Bluetooth® LE Information (Bluetooth® LE Only, MAGTEK INTERNAL ONLY FOR NOW)

##### Property 2.1.2.7.1.1 Bluetooth® LE Firmware Version

Table 1133 - Property 2.1.2.7.1.1 Bluetooth® LE Firmware Version

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.7.1.1 / 0x020102070101</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Firmware Version</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its BLE firmware version
number in the form <strong>PartNumber-Version-PCI</strong>, padded with
null characters.</p>
<p>Example: 1000009327-A0-PCI</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>18</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td>Any string</td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1134 - Get Request Example

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA0081040108D101841AD10181072B06010401F609850102890AE108E206E704E102C100 |

Table 1135 - Get Response Example

| Example (Hex) |
|----|
| AA0081048208D1018204000000008482002CD10181072B06010401F609850102891CE11AE218E716E114C112313030303030393332372D41302D50434900 |

##### Property 2.1.2.7.1.2 Bluetooth® LE Firmware Sequence Number

| Property Description |  |
|----|----|
| Property OID | 2.1.2.7.1.2 / 0x020102070102 |
| Name | Bluetooth® LE Firmware Sequence Number |
| Description | The device uses this property to report its BLE firmware sequence number. |
| Securing Key | None |
| Min. Len (b) | 4 |
| Max. Len (b) | 4 |
| Data Type | Binary |
| Valid Values | Non-zero. |
| Default | None |

Table 1136 - Property 2.1.2.7.1.2 Bluetooth® LE Firmware Sequence Number

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA0081040106D101841AD10181072B06010401F609850102890AE108E206E704E102C200 |

Table 1137 - Get Request Example

| Example (Hex) |
|----|
| AA0081048206D1018204000000008482001ED10181072B06010401F609850102890EE10CE20AE708E106C20400000009 |

Table 1138 - Get Response Example

##### Property 2.1.2.7.2.1 Bluetooth® LE Device Address

Table 1139 – Bluetooth® LE Device Address

| Property Description |  |
|----|----|
| Property OID | 2.1.2.7.2.1 / 0x020102070201 |
| Name | Bluetooth® LE Device Address |
| Description | The device uses this property to report its Bluetooth® LE Device address in most significant byte order. |
| Securing Key | None |
| Min. Len (b) | 6 |
| Max. Len (b) | 6 |
| Data Type | Binary |
| Valid Values | IEEE 802 EUI-48 |
| Default | None |

Table 1140 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104010ED101 841AD101 81072B06010401F609 850102 890AE108E206E704E202C100 |

Table 1141 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104820ED101 820400000000 84820020D101 81072B06010401F609 850102 8910E10EE20CE70AE208C1 06943469B297A5 |

##### Property 2.1.2.7.2.2 Bluetooth® LE Connection Status

Table 1142 – Bluetooth® LE Connection Status

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.1.2.7.2.2 / 0x020102070202</td>
</tr>
<tr>
<td>Name</td>
<td>Bluetooth® LE Connection Status</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to report its Bluetooth® LE Connection
Status.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>One byte value where each bit of the byte indicates a particular
status. Bit 0 is the least significant bit.<br />
<br />
Bit 0 is the advertising status. If set to 1 the device is advertising,
otherwise 0.</p>
<p>Bit 1 is the connection status. If set to 1 the device is in a
connection, otherwise 0.</p>
<p>Bit 2 is the secure connection status. If set to 1 the device is in a
secure connection, otherwise 0.</p>
<p>Bit 3 is the notification status. If set to 1 notifications are
enabled, otherwise 0.</p>
<p>Bits 4 to 7 are reserved and will be set to zero for now.</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1143 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020702 8902 C200 |

Table 1144 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501028704010207028903C20101 |

##### Property 2.1.2.7.2.3 Bluetooth® LE Number of Bondings

Table 1145 – Bluetooth® LE Number of Bondings

| Property Description |  |
|----|----|
| Property OID | 2.1.2.7.2.3 / 0x020102070203 |
| Name | Bluetooth® LE Number of Bondings |
| Description | The device uses this property to report its Bluetooth® LE Number of Bondings. The maximum number of bondings is 9. If the device has 9 bondings and another host pairs with it, the new bonding will overwrite the oldest existing bonding. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0 - 9 |
| Default | None |

Table 1146 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020702 8902 C300 |

Table 1147 - Get Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA0081048255D10182040000000084820010D1018501028704010207028903C30101 |

##### Property 2.1.2.7.2.4 Bluetooth® LE MTU Size

Table 1148 – Bluetooth® LE MTU Size

| Property Description |  |
|----|----|
| Property OID | 2.1.2.7.2.4 / 0x020102070204 |
| Name | Bluetooth® LE MTU Size |
| Description | The device uses this two-byte property, in most significant byte order, to report its Bluetooth® LE MTU size. The maximum transmission unit (MTU) is agreed upon between the host and the device during a connection. For DynaFlex, the value will be between 23 and 247 depending on the size the host supports. If the device is not in a connection, it will report 23. |
| Securing Key | None |
| Min. Len (b) | 2 |
| Max. Len (b) | 2 |
| Data Type | Binary |
| Valid Values | 23 - 247 |
| Default | None |

Table 1149 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 01020702 8902 C400 |

Table 1150 - Get Response Example

| Example (Hex)                                                          |
|------------------------------------------------------------------------|
| AA0081048255D10182040000000084820011D1018501028704010207028904C40200F7 |

#### Property Subgroup 2.1.2.8.nn Custom UI

##### Property 2.1.2.8.1.1 UI Configuration File

Table 1151 - Property 2.1.2.8.1.1 UI Configuration File

| Property Description |  |
|----|----|
| Property OID | 2.1.2.8.1.1 / 0x020102080101 |
| Name | UI Configuration Filename |
| Description | This string contains the part number and the revision of the UI Configuration File. |
| Securing Key | None |
| Min. Len (b) | 14 |
| Max. Len (b) | 14 |
| Data Type | ASCII |
| Valid Values | CFG000xxxx-xxx |
| Default | None |

Table 1152 - Get Request Example

| Example (Hex)                                                            |
|--------------------------------------------------------------------------|
| AA0081040106D101841AD10181072B06010401F609850102890AE108E206E804E102C100 |

Table 1153 - Get Response Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Example (Hex)</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>AA0081048206D10182040000000084820028D10181072B06010401F609850102</p>
<p>8918E116E214E812E110C10E434647303030363831322D323030</p></td>
</tr>
</tbody>
</table>

### Property Group 2.2.1.nnn Device Hardware Information

#### Property Subgroup 2.2.1.1.1.n Device Common Configuration Information

##### Property 2.2.1.1.1.1 Serial Number

Table 1154 - Property 2.2.1.1.1.1 Serial Number

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.2.1.1.1.1 / 0x020201010101</td>
</tr>
<tr>
<td>Name</td>
<td>Device Serial Number</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its serial number. The
left 3.5 bytes represent the 7 digit serial number, and the remaining
half byte is always 0.</p>
<p>Example: Serial number <strong>B603226</strong> is reported as 0xB6,
0x03, 0x22, 0x60.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Min 0x00000000</p>
<p>Max 0xFFFFFFF0</p></td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1155 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 B5 D1 01 84 18 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 87 04 02 01 01 01 89 02 C1 00 |

Table 1156 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 B5 D1 01 82 04 00 00 00 00 84 82 00 1C D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 87 04 02 01 01 01 89 06 C1 04 B6 13 78 A0 |

##### Property 2.2.1.1.1.2 Device Capabilities Report (MAGTEK INTERNAL ONLY FOR NOW)

Table 1157 - Property 2.2.1.1.1.2 Device Capabilities Report (MAGTEK
INTERNAL ONLY FOR NOW)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.2.1.1.1.2 / 0x020201010102</td>
</tr>
<tr>
<td>Name</td>
<td>Device Capabilities Report</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its capabilities in
string format padded with null characters.</p>
<p>Example: “V=1,SC=1,SR=1,UDE=0,CE=2,CLE=2,BT=0,WF=0”</p>
<ul>
<li><p>V = Version</p></li>
<li><p>SC = Signature Capture</p></li>
<li><p>SR = SRED</p></li>
<li><p>UDE = Cardholder Data Entry Mode</p></li>
<li><p>CE = Contact EMV Level Supported</p></li>
<li><p>CLE = Contactless Level Supported</p></li>
<li><p>BT = Bluetooth®</p></li>
<li><p>WF = Wireless LAN (WLAN)</p></li>
</ul></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>64</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>64</td>
</tr>
<tr>
<td>Data Type</td>
<td>Alphanumeric</td>
</tr>
<tr>
<td>Valid Values</td>
<td></td>
</tr>
<tr>
<td>Default</td>
<td></td>
</tr>
</tbody>
</table>

Table 1158 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 E0 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E2 08 E1 06 E1 04 E1 02 C2 00 |

Table 1159 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 E0 D1 01 82 04 00 00 00 00 84 82 00 5A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 4A E2 48 E1 46 E1 44 E1 42 C2 40 56 3D 31 2C 53 43 3D 31 2C 53 52 3D 31 2C 55 44 45 3D 30 2C 43 45 3D 32 2C 43 4C 45 3D 32 2C 42 54 3D 30 2C 57 46 3D 30 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |

##### Property 2.2.1.1.1.3 PCI Hardware ID

Table 1160 - Property 2.2.1.1.1.3 PCI Hardware ID

| Property Description |  |
|----|----|
| Property OID | 2.2.1.1.1.3 / 0x020201010103 |
| Name | PCI Hardware ID |
| Description | The device uses this property to report its PCI Hardware ID. Customers can use this value to compare against the device’s certification records on the PCI web site. |
| Securing Key | None |
| Min. Len (b) | 10 |
| Max. Len (b) | 256 |
| Data Type | Alphanumeric |
| Valid Values | Any string |
| Default |  |

Table 1161 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 E3 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E2 08 E1 06 E1 04 E1 02 C3 00 |

Table 1162 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 E3 D1 01 82 04 00 00 00 00 84 82 00 24 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 14 E2 12 E1 10 E1 0E E1 0C C3 0A 33 36 50 43 49 34 35 30 41 30 |

##### Property 2.2.1.1.1.4 Device Hardware Configuration (MAGTEK INTERNAL ONLY)

Table 1163 - Property 2.2.1.1.1.4 Device Hardware Configuration (MAGTEK
INTERNAL ONLY)

| Property Description |  |
|----|----|
| Property OID | 2.2.1.1.1.4 / 0x020201010104 |
| Name | Device Hardware Configuration |
| Description | The device uses this property to report its hardware configuration profile. See the **Hardware Configuration Profile** parameter in **Command 0xF016 - Activate Device Security (MAGTEK INTERNAL ONLY)** for detail. |
| Securing Key | None |
| Min. Len (b) | 10 |
| Max. Len (b) | 256 |
| Data Type | Binary |
| Valid Values | Any number |
| Default |  |

Table 1164 - Get Request Example

| Example (Hex) |
|----|
| AA 00 81 04 01 E3 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 0A E2 08 E1 06 E1 04 E1 02 C4 00 |

Table 1165 - Get Response Example

| Example (Hex) |
|----|
| AA 00 81 04 82 08 D1 01 82 04 00 00 00 00 84 82 00 34 D1 01 81 07 2B 06 01 04 01 F6 09 85 01 02 89 24 E2 22 E1 20 E1 1E E1 1C C4 1A 01 05 01 02 01 02 00 03 01 01 01 02 01 01 05 01 00 00 00 01 05 01 01 01 01 01 |

### Property Group 2.3.1.nnn System Status Information

#### Property Subgroup 2.3.1.1.1.n System Status Injected Key Information

##### Property 2.3.1.1.1.1 Device Key Status

Table 1166 - Property 2.3.1.1.1.1 Device Key Status

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.3.1.1.1.1 / 0x020301010101</td>
</tr>
<tr>
<td>Name</td>
<td>Device Key Status</td>
</tr>
<tr>
<td>Description</td>
<td>This OID contains a 32-bit bitmap. Each bit indicates the status of
a device key. A bit value of 1 indicates the corresponding key has been
injected.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Bit 0: TMPTK_1000</p>
<p>Bit 1: MTK_1001</p>
<p>Bit 2: DEVTK_1002</p>
<p>Bit 3: FINTK_1003</p>
<p>Bit 4: PRODTK_1021</p>
<p>Bit 5: MFGTK_1022</p>
<p>Bit 6: MFIFTK_1081</p>
<p>Bit 7: AKIFTK_1091</p>
<p>Bit 8: FREQMK_1101</p>
<p>Bit 9: MREQMK_1102</p>
<p>Bit 10: MFRQMK_1111</p>
<p>Bit 11: ARQ1MK_1121</p>
<p>Bit 12: ARQ2MK_1122</p>
<p>Bit 13 – 31: Reserved</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1167 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104010ED101 841AD101 81072B06010401F609 850102 890AE308E106E104E102C100 |

Table 1168 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104820ED101 820400000000 8482001E D101 81072B06010401F609 850102 890EE30CE10AE108E106C1040000077E |

##### Property 2.3.1.1.1.2 Transaction Key Status

Table 1169 - Property 2.3.1.1.1.2 Transaction Key Status

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.3.1.1.1.2 / 0x020301010102</td>
</tr>
<tr>
<td>Name</td>
<td>Transaction Key Status</td>
</tr>
<tr>
<td>Description</td>
<td>This OID contains a 32-bit bitmap. Each bit indicates the status of
a transaction key. A bit value of 1 indicates the corresponding key has
been injected.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>4</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Bit 0: DKPTM0_2000 Bit 16: DKPTM10_2010</p>
<p>Bit 1: DKPTM1_2001 Bit 17: DKPTM11_2011</p>
<p>Bit 2: DKPTM2_2002 Bit 18: DKPTM12_2012</p>
<p>Bit 3: DKPTM3_2003 Bit 19: DKPTM13_2013</p>
<p>Bit 4: DKPTM4_2004 Bit 20: DKPTM14_2014</p>
<p>Bit 5: DKPTM5_2005 Bit 21: DKPTM15_2015</p>
<p>Bit 6: DKPTM6_2006 Bit 22: DKPTM16_2016</p>
<p>Bit 7: DKPTM7_2007 Bit 23: DKPTM17_2017</p>
<p>Bit 8: DKPTM8_2008 Bit 24: DKPTM18_2018</p>
<p>Bit 9: DKPTM9_2009 Bit 25: DKPTM19_2019</p>
<p>Bit 10: DKPTMA_200A Bit 26: DKPTM1A_201A</p>
<p>Bit 11: DKPTMB_200B Bit 27: DKPTM1B_201B</p>
<p>Bit 12: DKPTMC_200C Bit 28: DKPTM1C_201C</p>
<p>Bit 13: DKPTMD_200D Bit 29: DKPTM1D_201D</p>
<p>Bit 14: DKPTME_200E Bit 30: DKPTM1E_201E</p>
<p>Bit 15: DKPTMF_200F Bit 31: DKPTM1F_201F</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1170 - Get Request Example

| Example (Hex) |
|----|
| AA00 8104010FD101 841AD101 81072B06010401F609 850102 890AE308E106E104E102C200 |

Table 1171 - Get Response Example

| Example (Hex) |
|----|
| AA00 8104820FD101 820400000000 8482001ED101 81072B06010401F609 850102 890EE30CE10AE108E106C20400000081 |

#### Property Subgroup 2.3.1.1.2.n System Status Security Protection Information

##### Property 2.3.1.1.2.1 Real Time Clock Enabled

Table 1172 - Property 2.3.1.1.2.1 Real Time Clock Enabled

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.3.1.1.2.1 / 0x020301010201</td>
</tr>
<tr>
<td>Name</td>
<td>Real Time Clock Enabled</td>
</tr>
<tr>
<td>Description</td>
<td>The device maps this property to its internal register that enables
its internal real-time clock. Because the device ensures that register
is enabled every time it powers up, this property should always report
Real Time Clock Enabled.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Real Time Clock Not Enabled</p>
<p>0x01 = Real Time Clock Enabled</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1173 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010102 8902 C100 |

Table 1174 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010102 8903 C101 01 |

##### Property 2.3.1.1.2.2 Tamper Sensors Activated

Table 1175 - Property 2.3.1.1.2.2 Tamper Sensors Activated

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.3.1.1.2.2 / 0x020301010202</td>
</tr>
<tr>
<td>Name</td>
<td>Tamper Sensors Activated</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to report whether its tamper sensors
have been activated using <strong>Command 0xF016 - Activate Device
Security (MAGTEK INTERNAL ONLY)</strong>. A device that is operating
normally should always have its tamper sensors activated.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Tamper Sensors Not Activated</p>
<p>0x01 = Tamper Sensors Activated</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1176 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010102 8902 C100 |

Table 1177 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010102 8903 C101 01 |

##### Property 2.3.1.1.2.3 Tamper Sensor Tampered

Table 1178 - Property 2.3.1.1.2.3 Tamper Sensor Tampered

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.3.1.1.2.3 / 0x020301010203</td>
</tr>
<tr>
<td>Name</td>
<td>Tamper Sensor Tampered</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to report whether a tamper sensor has
tampered. A device that is operating normally should not reported that
it has been tampered with. To examine the device’s tamper history to
determine the cause, use <strong>Command 0xF014 - Read Log (MAGTEK
INTERNAL ONLY)</strong> or <strong>Command 0xF015 - Read Log &amp; Clear
Tamper (MAGTEK INTERNAL ONLY)</strong>.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Not Tampered</p>
<p>0x01 = Tampered</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1179 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010102 8902 C300 |

Table 1180 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010102 8903 C301 00 |

##### Property 2.3.1.1.2.4 Tamper Configuration Revision (MAGTEK INTERNAL ONLY)

Table 1181 - Property 2.3.1.1.2.4 Tamper Configuration Revision (MAGTEK
INTERNAL ONLY)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.3.1.1.2.4 / 0x020301010204</td>
</tr>
<tr>
<td>Name</td>
<td>Tamper Configuration Revision</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report which tamper
configuration its security systems are currently using. Tampers are
configured and locked for security the first time a host calls
<strong>Command 0xF016 - Activate Device Security (MAGTEK INTERNAL
ONLY)</strong>, and the device determines and sets this property based
on the firmware version installed in the device at that time.</p>
<p>This property exists because the host can not determine which tamper
configuration the device is currently using by examining the currently
installed firmware version; if a host activates the device’s security
systems while the device is loaded with firmware that uses an earlier
tamper configuration, installing firmware that supports a newer tamper
configuration does not change the tamper configuration until an operator
resets the device’s security systems.</p>
<p>To reset the device’s security systems and change the tamper
configuration, an operator must first reset this property to <strong>Not
Configured</strong> by disconnecting all tamper-related power from the
device. For example, disconnect USB power, the rechargeable battery, and
the coin cell battery, which requires physical access to the inside of
the device. This process clears and unlocks the tamper configuration.
The host must then call <strong>Command 0xF016 - Activate Device
Security (MAGTEK INTERNAL ONLY)</strong> to activate the device’s
security systems again.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Not Configured</p>
<p>0x01 = Original Configuration</p>
<p>0x02 = Coin Cell Current Optimized</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1182 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010102 8902 C400 |

Table 1183 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010102 8903 C401 02 |

#### Property Subgroup 2.3.1.2.1.n System Status Device State Information

##### Property 2.3.1.2.1.1 Device Operational Status

Table 1184 - Property 2.3.1.2.1.1 Device Operational Status

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.3.1.2.1.1 / 0x020301020101</td>
</tr>
<tr>
<td>Name</td>
<td>Device Operational Status</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report its operational
status.</p>
<p><strong>Online</strong> is the status the manufacturer populates in
this property before shipping, and is the result of the device going
through processes that configure its security subsystems and features.
In this state, the device is fully functional and can perform
transactions.</p>
<p><strong>Offline</strong> means the device is no longer fully
functional and can no longer perform transactions. The device
automatically transitions to this state if it detects a problem with
security or any of the subsystems it checks. For example, trying to open
the device triggers a tamper response, which causes the device to change
its operational status to Offline. To retrieve more information about
the cause of an Offline status, the host can retrieve <strong>Property
2.3.1.2.1.2 Offline Status Detail</strong>.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x01 = Offline</p>
<p>0x02 = Online</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1185 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010201 8902 C100 |

Table 1186 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010201 8903 C101 02 |

##### Property 2.3.1.2.1.2 Offline Status Detail

Table 1187 - Property 2.3.1.2.1.2 Offline Status Detail

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.3.1.2.1.2 / 0x020301020102</td>
</tr>
<tr>
<td>Name</td>
<td>Offline Status Detail</td>
</tr>
<tr>
<td>Description</td>
<td><p>The device uses this property to report the status of every
subsystem that can cause the device’s operation status to be set to
<strong>Offline</strong> in <strong>Property 2.3.1.2.1.1 Device
Operational</strong> Status.</p>
<p>The property consists of a sequence of bytes where each bit in each
byte represents the status of a subsystem. If a bit is set to one, then
there is a problem with the subsystem, otherwise no problem was
detected.</p>
<p>Some subsystems provide other properties or commands that can be used
to get more information about the subsystem’s status. For example,
<strong>Property 2.3.1.1.2.2 Tamper Sensors Activated</strong> and
<strong>Property 2.3.1.1.2.3 Tamper Sensor Tampered</strong>.</p></td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>16 (reserved for future expansion)</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>Byte 0</p>
<ul>
<li><p>Bit 0 = Tamper problem present</p></li>
<li><p>Bit 1 = Master Key problem present</p></li>
<li><p>Bit 2 = Keys and Certificates problem present</p></li>
<li><p>Bit 3 = Real Time Clock problem present</p></li>
<li><p>Bit 4 = Random Number Generator problem present</p></li>
<li><p>Bit 5 = Cryptography Engine problem present</p></li>
<li><p>Bit 6 = Magnetic Stripe Reader Hardware problem present</p></li>
<li><p>Bit 7 = Reserved</p></li>
</ul></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1188 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010201 8902 C200 |

Table 1189 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010201 8903 C201 00 |

##### Property 2.3.1.2.1.3 External Power Supplied

Table 1190 - Property 2.3.1.2.1.3 External Power Supplied

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.3.1.2.1.3 / 0x020301020103</td>
</tr>
<tr>
<td>Name</td>
<td>External Power Supplied</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to report the status of external
power.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = No external power supplied</p>
<p>0x01 = Power supplied by USB port</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 1191 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010201 8902 C300 |

Table 8‑200 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010201 8903 C301 01 |

##### Property 2.3.1.2.1.4 Battery State of Charge

Table 8‑201 - Property 2.3.1.2.1.4 Battery State of Charge

| Property Description |  |
|----|----|
| Property OID | 2.3.1.2.1.4 / 0x020301020104 |
| Name | Battery State of Charge |
| Description | The device uses this property to report the charge status of the internal battery. The charge status is reported as a percentage of full charge. |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Binary |
| Valid Values | 0x00..0x64 |
| Default | None |

Table 8‑202 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010201 8902 C400 |

Table 8‑203 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010201 8903 C401 64 |

##### Property 2.3.1.2.1.5 Battery Charger Status

Table 8‑204 - Property 2.3.1.2.1.5 Battery Charger Status

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Property Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Property OID</td>
<td>2.3.1.2.1.5 / 0x020301020105</td>
</tr>
<tr>
<td>Name</td>
<td>Battery Charger Status</td>
</tr>
<tr>
<td>Description</td>
<td>The device uses this property to report the status of the battery
charger.</td>
</tr>
<tr>
<td>Securing Key</td>
<td>None</td>
</tr>
<tr>
<td>Min. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Max. Len (b)</td>
<td>1</td>
</tr>
<tr>
<td>Data Type</td>
<td>Binary</td>
</tr>
<tr>
<td>Valid Values</td>
<td><p>0x00 = Precharge</p>
<p>0x01 = Fast charge – constant current</p>
<p>0x02 = Fast charge – constant voltage</p>
<p>0x03 = End of charge</p>
<p>0x04 = Charge complete</p>
<p>0x08 = No external power supplied</p></td>
</tr>
<tr>
<td>Default</td>
<td>None</td>
</tr>
</tbody>
</table>

Table 8‑205 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010201 8902 C500 |

Table 8‑206 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010201 8903 C501 04 |

##### Property 2.3.1.2.1.6 Device Temperature

Table 8‑207 - Property 2.3.1.2.1.6 Device Temperature

| Property Description |  |
|----|----|
| Property OID | 2.3.1.2.1.6 / 0x020301020106 |
| Name | Device Temperature |
| Description | The device uses this property to report the temperature in Celsius |
| Securing Key | None |
| Min. Len (b) | 1 |
| Max. Len (b) | 1 |
| Data Type | Signed Binary |
| Valid Values | 0x80 .. 0x7F (-128 .. 127) |
| Default | None |

Table 8‑208 - Get Request Example

| Example (Hex)                                                |
|--------------------------------------------------------------|
| AA00 8104 0155D101 840F D101 8501 02 8704 03010201 8902 C600 |

Table 8‑209 - Get Response Example

| Example (Hex) |
|----|
| AA00 81048255D101 820400000000 84820010 D101 850102 870403010201 8903 C601 26 |

### Object IDs (OIDs) and ITU-T X660

#### About OIDs

For modular management of device functions, information, and settings,
this standard makes extensive use of Object Identifiers (also known as
Object IDs or OIDs) as defined in ***ITU-T X.660 \| ISO/IEC 9834-1***,
which can be found by searching for **X.660** in the publications on
[www.itu.int](http://www.itu.int).

OIDs are identifiers for any generic data element, and are managed by
standards bodies to be globally unique (much like web domains, IP
addresses, and Media Access Control MAC addresses). They are managed by
using a tree structure consisting of **nodes**, where the tree structure
is defined and controlled by a hierarchy of subordinate **Registration
Authorities**, each with their authority delegated by a Registration
Authority one level higher in the tree, starting with the root nodes
managed by ITU-T and ISO. The ***X.660*** standard for OIDs is
harmonized with the data representation standard of ***ASN.1*** via that
standard’s OBJECT IDENTIFIER and OID-IRI types. Every node is assigned a
**primary integer value** (or primary value for short) which serves to
uniquely identify the node, and may be assigned secondary identifiers
(such as strings) for human readability.

MagTek is the Registration Authority for the OID tree beginning at
**{iso(1) identified-organization(3) dod(6) internet(1) private(4)
enterprise(1) MagTek(15113)}** (using **value notation** of the
***ASN.1*** OBJECT IDENTIFIER type). The branch can also be represented
in numerical shorthand as **1.3.6.1.4.1.15113**, which is the
**encoding** form of the ***ASN.1*** OBJECT IDENTIFIER type.

Per ***X.660***, OIDs can be encoded in **constructed** form or
**primitive** form. The primitive form is a sequence of octets (bytes)
and is summarized in section **A.2 Octet Encoding of OIDs**. The
constructed form is a TLV data object and is summarized in section **A.3
TLV Encoding of OIDs**.

In many cases, the MagTek implementation of OID-based message elements
allows the host to specify an optional **Company ID** and **Tree
prefix** alongside a **Relative OID**, where the full OID is a
concatenation of the company ID, followed by the tree prefix, followed
by the relative OID. If a message does not include the optional company
ID or tree prefix, company ID is assumed to be the MagTek arc above, and
the tree prefix is assumed to be a reasonable sequence of additional
nodes based on the purpose and scope of the message.

##### Octet Encoding of OIDs

In addition to human-readable ***ASN.1*** value notation and encoding
forms above, OIDs can be encoded as binary values (octets) as follows
(per ***X.660*** section ***8.19 Encoding of an object identifier
value***):

1)  Start with the numerical form (for example, MagTek’s arc
    **1.3.6.1.4.1.15113** from section **A.1**).

2)  Multiply the primary value of the first node in the OID by 40
    decimal (e.g., 1\*40=40) and add it to the primary value of the
    second node. The sum is used as the first byte (e.g., 43 decimal =
    **0x2B**) of the octet form. The first two nodes receive this
    special treatment because their possible value ranges are expected
    to remain very small indefinitely.

3)  The next bytes in the octet encoded form are simply equal to each
    primary value in the OID sequence, unless the primary value is
    greater than 128 decimal (0x80). For primary values greater than
    0x80, additional encoding rules apply that are not necessary to
    detail here, because for simplicity MagTek selects OID primary
    values that are equal to 0x79 or less (and in many cases, 0x30 or
    less); In addition, TLV encoding places additional restrictions on
    selection of OID, in that if the OID is to be used directly as a tag
    in a TLV data object, it must not be greater than 0x1F (see section
    **3.2.1.1 About TLV Encoding**). The only portion of MagTek’s arc
    that is subject to these additional encoding rules is the primary
    value **15113** at the end, which encodes to **0xF609** hex (per the
    rules not detailed here, see ***X.660*** for details). The full arc
    **1.3.6.1.4.1.15113** therefore encodes to **0x2B 06 01 04 01
    F609**.

#### TLV Encoding of OIDs

The primary method of encoding OIDs, as specified in ***X.660*** section
***8 Basic encoding rules***, is BER Tag-Length-Value (TLV) format. A
TLV-encoded OID is a set of nested TLV data objects, where:

- The **tag** of each TLV data object equals the primary value of the
  node it represents in the OID sequence, encoded according to the BER
  TLV tag number rules; the assigned primary values in this standard are
  all **private** (11nnnnnn), the bottom level value / leaf of any OID
  arc is encoded as **primitive** (nn0nnnnn), and the levels above it
  are encoded as **composed** (nn1nnnnn). This information makes it
  possible to use the bit definitions for **Tag** in section **3.2.1
  Tag-Length-Value (TLV) Encoding** as a reference to encode each level
  of the OID as a tag. Generally the primary values in this standard are
  selected to be less than 0x1F, and so do not require multi-byte tags.

- The **length** of each TLV data object, like all TLV data objects, is
  equal to the length of its value.

- The **value** of each TLV data object is equal to a nested TLV data
  object containing all subsequent nodes in the OID sequence, so
  TLV-encoded OIDs must be built from the bottom up. The primitive value
  in the bottom node of a TLV-encoded OID is the set of actual values
  contained by that OID (e.g., string, byte\[s\], and so on), or in the
  case of requests where the value is (by definition) not known to the
  requester, the length is **0x00**.

For example, the process of TLV encoding the OID in a request to
retrieve the contents of **OID 3.5.7.9** with 9 being a leaf node looks
like this (all values are hexadecimal unless otherwise noted):

1)  First, realize OID 3.5.7.9 is to be interpreted as a nested set of
    containers. Node 3 contains node 5, which contains node 7, which
    contains node 9. Although node 9 presumably contains one or more
    values, the entity making the request for its contents, by
    definition, does not know the contents when composing the request,
    so in this example, node 9 is treated like an “empty bucket.” In the
    corresponding response, node 9 would include its actual contents.

2)  Because TLV is built from the inside out (bottom up), start the
    encoding process with the node at the end which has a primary value
    equal to 9. Like all OIDs in this standard it is **private**, and
    because it is a leaf node at the bottom / end of the OID tree and
    therefore does not contain any further nested TLV data objects, it
    is **primitive**: 0x09 primary value OR 0b11000000 private OR
    0b00000000 primitive = **C9**. As explained above, in this case it
    is an empty bucket, so its length is **00**. Its TLV encoding is
    **C9 00**.

3)  Up one level to the node with primary value equal to 7, it is also
    **private**, but unlike the previous level it contains a nested TLV
    data object (C9 00 from above) so it is **constructed** instead of
    primitive: 0x07 primary value OR 0b11000000 private OR 0b00100000
    constructed = **E7**. It has contents C9 00 so length is **02**. Its
    TLV encoding is **E7 02 C9 00**.

4)  Up one level to the node with primary value 5, it is **private** and
    contains TLV data object E7 02 C9 00 from above, so it is
    **constructed**: 0x05 primary value OR 0b11000000 private OR
    0b00100000 constructed = **E5**. It has contents E7 02 C9 00 so
    length is **04**. Its TLV encoding is **E5 04 E7 02 C9 00**.

5)  Up to the root with primary value 3, it is **private** and
    **constructed** so tag is **E3**, value is the TLV data object from
    above, so length is equal to that object’s length **06**. Its
    encoding is **E3 06 E5 04 E7 02 C9 00**, which is the final encoding
    of whole “empty bucket” OID **3.5.7.9**.

#### Design Intent (MAGTEK INTERNAL ONLY)

The main body of this document describes MMS from a customer’s point of
view. However, when MagTek firmware engineers need to make decisions
about extending or modifying the standard, there are additional factors
that are important to the design that are not important to customers.
For example, although the first release of MMS includes four Message
Types, it may become necessary in the future to add another one, and in
that case, the design intent behind the existing Message Type numbers
becomes an important consideration, because dependent software may make
assumptions that rely on certain “invisible rules” being consistently
followed. This section collects the design factors to consider.

#### Tag Selection

When constructing a new tag, these are the general parameters for
deciding what it should be:

#### Message Types

When adding a message type, these are the general parameters for
deciding what it should be:

<span class="mark">  
</span>

## Demo Mode (MAGTEK INTERNAL ONLY FOR NOW) 

Demo Mode provides a way to demonstrate the card and barcode readers on
the DynaFlex and DynaProx devices. Once DemoMode is entered, the device
must be rebooted in order exit Demo Mode. The demo can be run on devices
that do not have a LCD display. The LEDs and beeps will indicate the
state of the demo.

### Preparation for Demo Mode

To use the contactless reader, contactless events must be enabled.
Writing 03000000 to OID 1.2.7.1.2.1 will the enable events for the
contactless reader. See [**Property 1.2.7.1.2.1 User Event Notification
Controls
Enable**](#property-1.2.7.1.2.1-user-event-notification-controls-enable)
for more information.

The device must be powered using a USB charger to enter Demo Mode. Demo
Mode will not start when the device is powered from a USB host or when
running from the battery.

If an image is to be displayed in place of the prompt, download the
image to the fourth image file (02000003). See [**Command 0xD812 - Start
Send File to Device
(Unsecured)**](#command-0xd812---start-send-file-to-device-unsecured)
for more information.

### Running the Demo

To run the demo, execute the following steps:

1)  Power the device from a USB charger. The device will boot. Do not
    remove power until you are finished running the demo. Wait for the
    device to display the Welcome screen.

2)  On the back of the device, near the USB port, is a small oval
    button. Press and hold the button until the device beeps exactly
    five times then release the button.

3)  A series of short beeps will sound to indicate that the demo has
    started. If an image has been stored in the fourth image file, the
    image will be displayed. If no image has been saved, the device will
    prompt for a card. If the device has a barcode reader, the prompt
    will also prompt for a barcode and the barcode reader’s light will
    turn on. The first LED will be green, and the rest will be off.

4)  Insert, tap, or swipe a card or scan a barcode.

5)  When a card or barcode is read, the device will sound a specific
    number of beeps, display a results text and light an LED. The
    following table shows the result of each type of read:

<table>
<caption><p>Table 1192 - LED Display</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Reader</th>
<th>Beeps</th>
<th>LED</th>
<th>Displayed Text</th>
</tr>
</thead>
<tbody>
<tr>
<td>Barcode</td>
<td>1</td>
<td>1<sup>st</sup> Blue</td>
<td>“MSR Read Successful”</td>
</tr>
<tr>
<td>MSR</td>
<td>2</td>
<td>2<sup>nd</sup> Blue</td>
<td><p>“Contactless EMV Read</p>
<p>Successful”</p></td>
</tr>
<tr>
<td>Contact</td>
<td>3</td>
<td>3<sup>rd</sup> Blue</td>
<td><p>“Contact EMV Read</p>
<p>Successful”</p></td>
</tr>
<tr>
<td>Contactless</td>
<td>4</td>
<td>4<sup>th</sup> Blue</td>
<td>“MSR Read Successful”</td>
</tr>
</tbody>
</table>

6)  The results will display for four seconds.

7)  If a card is still in the contact reader or in range of the
    contactless reader, a prompt to remove the card will be displayed
    and an error beep l also sound about once a second until the card is
    removed.

8)  Return to step 3.

#### Exiting the Demo

Unplug the USB cable to shut down the device. After unplugging the USB
cable, WLAN devices will have to be turned off using the button on the
back of the device. Press the button for two beeps and release the
button. The device will power off.

<span class="mark">  
</span>

### Barcode Reader Symbologies 

A Barcode symbology refers to the way in which data is encoded in a
barcode. It uses either spaced lines, dots or squares. When read, these
symbols are decoded and converted to data. The table below lists all of
the supported Symbologies and which are enabled by default.

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

Table D8.7‑1 – Barcode Reader Supported Symbologies

#### Erasing EMV Configurations

###### Load CAPK with AID: 0000000000 to erase all current CAPK keys with this CAPK key:

**Table 1193 - Get Request Example**

| Example (Hex) |
|----|
| AA00810401CED8128444D812810400000300A22B81040000008D8201048320B9C1F228E41A1F0B6173E00423C5B58A952DE1111E0CC5E33C3044A5D3FD2FCAA30A81083030303030333030870101 |

**Table 1194 - Get Response Example**

| Example (Hex)                |
|------------------------------|
| AA00810482CED812820400000000 |

**Table 1195 - Get Request Example**

| Example (Hex) |
|----|
| AA0081080400D8120000030084818D4D47544B41503130C10400000300CE7D000000000000016000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000583F99A8DF1A414B11A1607402AE67722C4F59B9 |

**Table 1196 - Get Response Example**

| Example (Hex)                |
|------------------------------|
| AA0081048200D812820400000000 |

###### Empty Amex DRL: Load AMEX DRL file with “EMPTY” content

**Table 1197 - Get Request Example**

| Example (Hex) |
|----|
| AA008104018DD8128444D812810400000500A22B81040000001182010483205E39BD3937CF6B80DECC2B6FD0ABED138D5CC69A6CE55C8790BBA58254B66ED5A30A81083030303030353030870101 |

**Table 1198 - Get Response Example**

| Example (Hex)                |
|------------------------------|
| AA008104828DD812820400000000 |

**Table 1199 - Get Request Example**

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA0081080400D8120000050084114D47544B41503130C10400000500CE01AA |

**Table 1200 - Get Response Example**

| Example (Hex)                |
|------------------------------|
| AA0081048200D812820400000000 |

###### Empty Terminal: Load Terminal file with “EMPTY” content

**Table 1201 - Get Request Example**

| Example (Hex) |
|----|
| AA0081040114D8128444D812810400000000A22B8104000000118201048320543666037C01700B9215F365346E7C883290F201E0D844D9F32B0D05A098B519A30A81083030303030303030870101 |

**Table 1202 - Get Response Example**

| Example (Hex)                |
|------------------------------|
| AA0081048214D812820400000000 |

**Table 1203 - Get Request Example**

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA0081080400D8120000000084114D47544B41503130C10400000000CE01AA |

**Table 1204 - Get Response Example**

| Example (Hex)                |
|------------------------------|
| AA0081048200D812820400000000 |

######## Empty Processing: Load Processing file with “EMPTY” content and 1 delimiter (FF33)

**Table 1205 - Get Request Example**

| Example (Hex) |
|----|
| AA008104011BD8128444D812810400000100A22B8104000000288201048320B25A77AD6582338898AA0498D1C15512AC9AE7C1B021884238813A28423B20E9A30A81083030303030313030870101 |

**Table 1206 - Get Response Example**

| Example (Hex)                |
|------------------------------|
| AA008104821BD812820400000000 |

**Table 1207 - Get Request Example**

| Example (Hex) |
|----|
| AA0081080400D8120000010084284D47544B41503130C10400000100CE18AA9A6CCE52123D2315BF3759D466BC0F7C4572A754FF3300 |

**Table 1208 - Get Response Example**

| Example (Hex)                |
|------------------------------|
| AA0081048200D812820400000000 |

######## Empty Entry Point: Load Entry file with “EMPTY” content and 1 delimiter (FF35)

**Table 1209 - Get Request Example**

| Example (Hex) |
|----|
| AA0081040135D8128444D812810400000200A22B8104000000288201048320d747a07102af345bbe0f41669ebd63aac8770aef5fa37ca00a2eaaf4112b8a2cA30A81083030303030323030870101 |

**Table 1210 - Get Response Example**

| Example (Hex)                |
|------------------------------|
| AA0081048235D812820400000000 |

**Table 1211 - Get Request Example**

| Example (Hex) |
|----|
| AA0081080400D8120000020084284D47544B41503130C10400000200CE18AA3dcfbc51fcdfd06ada36181f1cd3aee3f8f879bcFF3500 |

**Table 1212 - Get Response Example**

| Example (Hex)                |
|------------------------------|
| AA0081048200D812820400000000 |

##### Tip & Tax Display Limits (Touch Only)

These are the display limits that are supported.

The maximum number of digits for “preset” tip in \$ buttons is 6
(\$9,999.99).

The range for “preset” tip in % buttons is 0% to 100%

The maximum number of digits for custom tip is 9 (\$9,999,999.99).

The maximum number of digits for sale amount + tip + tax is 12
(\$9,999,999,999.99).

###### Physical Button (DynaFlex Only)

Every DynaFlex device features a single physical button. On the DynaFlex
II Go, this button is located on the left side of the device. For all
other models, it is located on the bottom of the device near the USB
port. Pressing and holding this button can activate additional functions
on the device. To active a specific function, press and hold the button
until a specific number of beeps are heard. Table G8.7-48 shows which
functions can be activated. Beep counts that are not listed are not
supported.

<table>
<caption><p>Table G8.7‑48 – Button Functions</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">Beep Count</th>
<th style="text-align: center;">Function</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">2</td>
<td><p>Power Off</p>
<p>Power the device off, The device will reboot if it is connected to
USB.</p></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td><p>WLAN Setup</p>
<p>WLAN devices only.</p></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td><p>BLE Pairing</p>
<p>BLE devices only.</p></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td><p>Demo</p>
<p>See Appendix C for more information.</p></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td><p>Battery Level</p>
<p>Light the LEDs to indicate the current state of charge of the
battery. The LEDs will light for 3 seconds then return to their original
state.</p>
<p><img
src="C:\Users\andrews\OneDrive - MagTek, Inc\AndrewS\Files to MD\media/media/image20.png"
style="width:4.9375in;height:1.57292in"
alt="A table with green and black text AI-generated content may be incorrect." /></p>
<p>The DynaFlex II Go has only green LEDs. Instead of lighting the first
LED in amber, it will slowly flash the first LED. Instead of Red, the
first LED will flash quickly.</p></td>
</tr>
</tbody>
</table>

###### Battery Charge Status

As mentioned in **Appendix G Physical Button (DynaFlex Only)**, there is
only one physical button on DynaFlex devices. Pressing and holding this
button until the device beeps six times then releasing it causes the
LEDs on the front of the device to display the current charge state of
the battery. The LEDs will return to their previous state after three
seconds.

| Battery Level | Transactions and Firmware Update Allowed | LED Color | LEDs On When Button is Pressed |  |  |  |  |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 100% - 90% | Yes | Green | 4 LEDs |  |  |  |  |
| 89% - 70% | Yes | Green | 3 LEDs |  |  |  |  |
| 69% - 50% | Yes | Green | 2 LEDs |  |  |  |  |
| 49% - 20% | Yes | Amber | 1 LED |  |  |  |  |
| 19% - 6% | Yes | Red | 1 LED |  |  |  |  |
| 5% - 0% | No | Red | 1 LED |  |  |  |  |

Table 1213 - Battery Charged Example

The DynaFlex II Go has only green LEDs. Instead of lighting the first
LED in amber, it will slowly flash the first LED. Instead of Red, the
first LED will flash quickly.
