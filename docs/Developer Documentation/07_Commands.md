---
title: Commands
layout: home
parent: DynaFlex Family Programmer's Manual
nav_order: 6
---

# Commands

## Command Group 0x10nn - Transactions

### Command 0x1001 - Start Transaction

The host uses this command to start a payment transaction.

The sequence of events for transactions with card readers enabled is roughly as follows.

**(MCE Only)** The sequence for Manual Entry Mode is provided further below.

1.  If the device is configured to enable user action event notifications using **Property 1.2.7.1.2.1 User Event Notification Controls Enable**, the cardholder may present a card or payment device before the host calls this command, and the device sends **Notification 0x1001 - Device Information Update** to the host to indicate it should call this command to start a transaction.
    1.  **(MSR Only)** In the case where the cardholder has swiped before the transaction started, the device temporarily stores the card swipe data for the period of time specified by **Property 1.2.7.1.2.2 User Event Notification MSR Data Timeout (MSR Only)** to make it available during the transaction. Later in this sequence, when the device would ordinarily prompt the cardholder to swipe, insert, or tap, the device briefly displays the same cardholder prompt, then automatically proceeds with the transaction using the temporarily stored card data. The cardholder does not have to swipe again.
    2.  **(EMV Contact Only \| EMV Contactless Only)** In the case where the cardholder has inserted or tapped before the transaction started, the host should call this command as quickly as possible while the card is still in the slot, or while the card or contactless payment device is still within tap range. The device does not begin contact or contactless reads until after the host invokes this command and does not store any data from the cardholder action event before the transaction is in process.
2.  The host composes a command request in the format below, and sends it to the device. It may cancel the transaction in process by calling **Command 0x1008 - Cancel Transaction**.
3.  The device sends a response in the format below, and waits for the cardholder to present payment using one of the enabled payment technologies.
4.  **(BCR Only)** If the cardholder scans a barcode, the device sends **Notification 0x0101 - Transaction Information Update** to report Barcode / Barcode Event / Type / Data Attached with the barcode data attached and terminates the transaction.
5.  After the cardholder presents payment, the device sends **Notification 0x0101 - Transaction Information Update** to report the payment technology being used / **Card Event**.
6.  **(MSR Only)** If **Property 1.2.1.1.1.1 Device-Driven Fallback Behavior (MSR Only)** is configured so the device automatically performs fallback operations, it performs them at this time following roughly the same sequence of steps as host-driven fallback described below. Device-driven fallback occurs at this point in the sequence within one iteration of this command, whereas host-driven fallback requires the host to re-send this command for each retry attempt.
7.  **(EMV Contact Only)** If the cardholder has inserted a chip card and there is more than one application the device and card mutually support:
    1.  **(Display Only)** The device prompts the cardholder to select the application to use.
    2.  **(No Display Only)** The device sends **Notification 0x1803 - User Interface Host Action Request** to report **Cardholder Selection Request**/ **Notification Payload** to prompt the cardholder to select the application to use. The host should respond by showing the prompt, receiving input from the cardholder, and calling **Command 0x1802 - Report Cardholder Selection** to report the selection result to the device.
8.  The device sends **Notification 0x0101 - Transaction Information Update** to report the payment technology being used / **Data Update / ARQC Update / Data Attached**.
9.  If the host specified **Quick Chip Transaction Flow** in the **Transaction Flow** parameter:
    1.  The device immediately constructs its own internal ARPC Response, with tag 8A set to ‘Z3’ to coordinate the transaction with the card or other payment method, and sends the host **Notification 0x0105 - Transaction Operation Complete** to report the payment technology being used / **Kernel Outcome** / **Quick Chip Deferred** /outcome detail. A Transaction Option parameter can be set to display on amount or not.
    2.  **(Display Only)** The device shows the message **REMOVE CARD** to notify the cardholder the card can be removed.
    3.  **(No Display only)** The device sends the host **Notification 0x1803 - User Interface Host Action Request** to report **Display**/**Display Message**/**Data Attached** with message **REMOVE CARD** to notify the cardholder the card can be removed.
    4.  The host should then process the ARQC Message data, including replacing the default amount with the final transaction amount, and should coordinate with the transaction processor to retrieve a final transaction result. Because in this case the device is not involved in determining the final transaction result, it does not send a notification to the host to show **APPROVED** or **DECLINED**.
        1.  **(Display Only)** Instead, the host should call **Command 0x1803 - Display Message (Display Only)** to show an appropriate message to the cardholder, such as **APPROVED** or **DECLINED**, based on the final transaction result.
        2.  **(No Display Only)** Instead, the host should use its local display to show an appropriate message to the cardholder, such as **APPROVED** or **DECLINED**, based on the final transaction result.
10. If the host specified **EMV Transaction Flow** in the **Transaction Flow** parameter:
    1.  The host processes the ARQC Message data and uses it to coordinate with the transaction processor to receive an ARPC Response, which it processes and sends to the device using **Command 0x1004 - Resume Transaction**.
    2.  The device waits for the period of time specified in **Property 1.1.1.1.1.5 ARPC Receive Timeout**. If an ARPC timeout occurs, the device sends the ARQC again based on the setting in **Property 1.1.1.1.1.6 ARPC Retry Attempts**.
    3.  **(EMV Contact Only)** If the cardholder inserted a contact chip card, the device communicates with the card to determine whether to approve or decline the transaction.
    4.  The device sends the host **Notification 0x0105 - Transaction Operation Complete** to report the payment technology being used / **Kernel Outcome** / **Approved** or **Declined** /outcome.
    5.  **(Display Only)** The device shows **APPROVED** or **DECLINED** to notify the cardholder of the transaction result.
    6.  **(No Display Only)** The device sends the host **Notification 0x1803 - User Interface Host Action Request** to report **Display**/**Display Message**/**Data Attached** with message **APPROVED** or **DECLINED** to notify the cardholder of the transaction result.
11. **(Touch Only)** If the card requires a signature, and if **Property 1.2.1.1.2.1 Signature Capture Control** is set to **Device-driven Signature Capture**, and if the **Signature Capture Control (MSR Only)** command parameter does not apply to the current transaction, the device prompts the cardholder to sign.
12. The device sends **Notification 0x0101 - Transaction Information Update** to report the payment technology used / **Data Update / Batch Data / Data Attached**. **(Touch Only)** Depending on the setting in **Property 1.2.1.1.2.2 Include Signature Data in EMV Batch Data (Touch Only)**, the device includes any acquired signature data with the batch data.
13. The device sends **Notification 0x0105 - Transaction Operation Complete** to report the payment technology used / **Outcome** / the final result of the transaction.
14. **(MSR Only)** If **Property 1.2.1.1.1.1 Device-Driven Fallback Behavior (MSR Only)** is configured so the device does not perform fallback operations, and if the solution design requires payment brand fallback logic, the host may use the contents of the notifications above to implement fallback flow according to the following rules, which mimic the automatic fallback behaviors the device implements during a single invocation of this command. The primary difference is that the host must keep track of its own final **Fallback Indicator** instead of receiving it from the device in the **EMV ARQC Type**:
    1.  If the transaction was successful and the notification indicates Payment Technology is **EMV Contact** or **EMV Contactless**, there is no need to perform fallback-related operations.
    2.  If the transaction was successful and the notification indicates Payment Technology is **Magnetic Stripe Reader**, the host should check the contents of the **Card Type** tag DFDF52 in the **EMV ARQC Type** from the notification. Per payment brand fallback rules:
        1.  If **Card Type** is NOT **MSR Financial and Contact Chip Card (ICC)**, the host may continue with the current transaction attempt using the magnetic stripe data. There is no need to perform fallback-related operations.
        2.  If **Card Type** is **MSR Financial and Contact Chip Card (ICC)**, and the host has restarted the same transaction because a previous attempt failed with the notification indicating **MSR Fallback**, the chip card and the device communicated during the previous invocation of this command, and determined they are not compatible. The host may continue the current transaction using the magnetic stripe data.
        3.  If **Card Type** is **MSR Financial and Contact Chip Card (ICC)** and the host has NOT restarted the same transaction three times and failed with the notification indicating **Technical Fallback**, the card has a chip the cardholder should use so the transaction will be more secure. The host should guide the cardholder to use the chip card interface by sending **Command 0x1803 - Display Message** to direct the device to display **USE CHIP READER**, then repeat **Command 0x1001 - Start Transaction** and arm the device with the contact interface enabled. The host may opt to also arm the contactless interface.
        4.  If **Card Type** is **MSR Financial and Contact Chip Card (ICC)** and the host has restarted the same transaction three times and failed with the notification indicating **Technical Fallback**, the host may continue the current transaction using the magnetic stripe data.
    3.  If the transaction has failed and the notification indicates Payment Technology is **None**, something went wrong at the very beginning of the transaction (for example, the host canceled), and the host may simply end all attempts at performing the transaction, or it may opt to repeat the original transaction with the same payment technologies enabled.
    4.  If the transaction has failed and the notification indicates Payment Technology is **EMV Contact**, the host should examine the contents of the notification. Per payment brand fallback rules:
        1.  If the notification indicates **MSR Fallback**, the chip card and the device have communicated and have determined they are not compatible. The host should guide the cardholder to use the magnetic stripe interface by sending **Command 0x1803 - Display Message** to direct the device to display **USE MAGSTRIPE**, then repeat **Command 0x1001 - Start Transaction** and arm the device with the Magnetic Stripe Reader interface enabled. The host may opt to also arm the contactless interface.
        2.  If the host has NOT restarted the same transaction three times and failed with the notification indicating a **Technical Fallback**, the host should guide the cardholder to re-insert the chip card by sending **Command 0x1803 - Display Message** to direct the device to display **TRY AGAIN**, then repeat **Command 0x1001 - Start Transaction** and arm the device with the contact interface enabled. The host may opt to also arm the contactless interface.
        3.  If the host has restarted the same transaction three times and failed with the notification reporting **Technical Fallback**, the host should guide the cardholder to use the magnetic stripe reader by sending **Command 0x1803 - Display Message** to direct the device to display **USE MAGSTRIPE**, then repeat **Command 0x1001 - Start Transaction** and arm the device with the Magnetic Stripe Reader interface enabled. The host may opt to also arm the contactless interface.
15. (Touch Only) If **Property 1.2.1.1.2.1 Signature Capture Control** is set to **Host-driven Signature Capture** and the card requires a signature, the host should perform host-driven signature capture at this time. The device waits for the time period specified by **1.2.1.1.2.3 Signature Timing Window (Touch Only)**, providing a time window for the host to end the transaction by sending **Command 0x1801 - Request Cardholder Signature**. At the end of that time window, if the host has not called that command, the device returns to the idle state.
16. **(EMV Contactless Only)** For NFC Tag, the flow is as follows:
17. Use Start Transaction command with the NFC enabled in Contactless Reader Mode
18. If an NFC Tag is Detected
    1.  the terminal will send a notification that identifies the NFC card type, see **Notification 0x0101 - Transaction Information Update**
    2.  the terminal will send another notification with the UID as a payload, see \*\*

### [Table 7.12](#table-7-12) - Notification Payload for Data Update, ARQC Update (Quick Chip), Data Attached\*\*. If a card is configured with a random ID, its value will be changed every time the card gets detected. The host is responsible to retrieve the real UID.

19. No ARQC or BATCH data will be sent
20. The host application can continue interfacing with the NFC tag by sending pass-through commands
21. When an NFC Tag gets out of the field, the terminal sends **Notification 0x0105 – 20 05 00 00 (PICC, NFC Tag, Tag Removed, Reserved)** indicating that the Tag has been removed.
22. **(MCE Only)** For manual card entry, the sequence of events is as follows:
23. The host composes a command request in the format below with **Manual Entry Mode** parameters defined and other reader modes empty and sends it to the device. The host may cancel the transaction in process by calling **Command 0x1008 - Cancel Transaction**.

#### The device presents a sequence of pages based on the setting of Property 1.2.1.1.4.5 MIFARE Plus AES_Key1.

### [[Table 8.35](#table-8-35)1](\#table-8-351) - Property 1.2.1.1.4.5 MIFARE Plus AES_Key1.

| Property Description |                                                                                                                                                                                                                                                                                                                                    |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Property OID         | 1.2.1.1.4.5 / 0x0102010100405                                                                                                                                                                                                                                                                                                      |
| Name                 | MIFARE Plus AES_Key1.                                                                                                                                                                                                                                                                                                              |
| Description          | The device uses this property to set 16-byte of the AES_Key1 for MIFARE Plus. On example of the ASE Key = 000102030405060708090A0B0C0D0E0Fh, the setting should be 000102030405060708090A0B0C0D0E0F For security, the Get request for this property will always return 4-MSB of KCV. This key will be encrypted and stored in KPM. |
| Securing Key         | None                                                                                                                                                                                                                                                                                                                               |
| Min. Len (b)         | 16                                                                                                                                                                                                                                                                                                                                 |
| Max. Len (b)         | 16                                                                                                                                                                                                                                                                                                                                 |
| Data Type            | Binary                                                                                                                                                                                                                                                                                                                             |
| Valid Values         |                                                                                                                                                                                                                                                                                                                                    |
| Default              | 00000000 00000000 00000000 00000000                                                                                                                                                                                                                                                                                                |

### [[Table 8.35](#table-8-35)2](\#table-8-352) - Get Request Example

| Example (Hex)                                                                                               |
|-------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 C5 00 |

### [[Table 8.35](#table-8-35)3](\#table-8-353) - Get Response Example

| Example (Hex)                                                                                    |
|--------------------------------------------------------------------------------------------------|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406C504763CBCDE |

### [[Table 8.35](#table-8-35)4](\#table-8-354) - Set Request Example

| Example (Hex)                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C5 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

### [[Table 8.35](#table-8-35)5](\#table-8-355) - Set Response Example

| Example (Hex)                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412C510000102030405060708090A0B0C0D0E0F |

#### Property 1.2.1.1.4.6 MIFARE Plus AES_Key2.

### [[Table 8.35](#table-8-35)6](\#table-8-356) - Property 1.2.1.1.4.6 MIFARE Plus AES_Key2.

| Property Description |                                                                                                                                                                                                                                                                                                                                    |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Property OID         | 1.2.1.1.4.6 / 0x0102010100406                                                                                                                                                                                                                                                                                                      |
| Name                 | MIFARE Plus AES_Key2.                                                                                                                                                                                                                                                                                                              |
| Description          | The device uses this property to set 16-byte of the AES_Key2 for MIFARE Plus. On example of the ASE Key = 000102030405060708090A0B0C0D0E0Fh, the setting should be 000102030405060708090A0B0C0D0E0F For security, the Get request for this property will always return 4-MSB of KCV. This key will be encrypted and stored in KPM. |
| Securing Key         | None                                                                                                                                                                                                                                                                                                                               |
| Min. Len (b)         | 16                                                                                                                                                                                                                                                                                                                                 |
| Max. Len (b)         | 16                                                                                                                                                                                                                                                                                                                                 |
| Data Type            | Binary                                                                                                                                                                                                                                                                                                                             |
| Valid Values         |                                                                                                                                                                                                                                                                                                                                    |
| Default              | 00000000 00000000 00000000 00000000                                                                                                                                                                                                                                                                                                |

### [[Table 8.35](#table-8-35)7](\#table-8-357) - Get Request Example

| Example (Hex)                                                                                               |
|-------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 C6 00 |

### [[Table 8.35](#table-8-35)8](\#table-8-358) - Get Response Example

| Example (Hex)                                                                                    |
|--------------------------------------------------------------------------------------------------|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406C604763CBCDE |

### [[Table 8.35](#table-8-35)9](\#table-8-359) - Set Request Example

| Example (Hex)                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C6 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

### [[Table 8.36](#table-8-36)0](\#table-8-360) - Set Response Example

| Example (Hex)                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412C610000102030405060708090A0B0C0D0E0F |

#### Property 1.2.1.1.4.7 MIFARE Plus AES_Key3.

### [[Table 8.36](#table-8-36)1](\#table-8-361) - Property 1.2.1.1.4.7 MIFARE Plus AES_Key3.

| Property Description |                                                                                                                                                                                                                                                                                                                                    |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Property OID         | 1.2.1.1.4.7 / 0x0102010100407                                                                                                                                                                                                                                                                                                      |
| Name                 | MIFARE Plus AES_Key3.                                                                                                                                                                                                                                                                                                              |
| Description          | The device uses this property to set 16-byte of the AES_Key3 for MIFARE Plus. On example of the ASE Key = 000102030405060708090A0B0C0D0E0Fh, the setting should be 000102030405060708090A0B0C0D0E0F For security, the Get request for this property will always return 4-MSB of KCV. This key will be encrypted and stored in KPM. |
| Securing Key         | None                                                                                                                                                                                                                                                                                                                               |
| Min. Len (b)         | 16                                                                                                                                                                                                                                                                                                                                 |
| Max. Len (b)         | 16                                                                                                                                                                                                                                                                                                                                 |
| Data Type            | Binary                                                                                                                                                                                                                                                                                                                             |
| Valid Values         |                                                                                                                                                                                                                                                                                                                                    |
| Default              | 00000000 00000000 00000000 00000000                                                                                                                                                                                                                                                                                                |

### [[Table 8.36](#table-8-36)2](\#table-8-362) - Get Request Example

| Example (Hex)                                                                                               |
|-------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 C7 00 |

### [[Table 8.36](#table-8-36)3](\#table-8-363) - Get Response Example

| Example (Hex)                                                                                    |
|--------------------------------------------------------------------------------------------------|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406C704763CBCDE |

### [[Table 8.36](#table-8-36)4](\#table-8-364) - Set Request Example

| Example (Hex)                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C7 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

### [[Table 8.36](#table-8-36)5](\#table-8-365) - Set Response Example

| Example (Hex)                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412C710000102030405060708090A0B0C0D0E0F |

#### Property 1.2.1.1.4.8 MIFARE Plus AES_Key4.

### [[Table 8.36](#table-8-36)6](\#table-8-366) - Property 1.2.1.1.4.8 MIFARE Plus AES_Key4.

| Property Description |                                                                                                                                                                                                                                                                                                                                    |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Property OID         | 1.2.1.1.4.8 / 0x0102010100408                                                                                                                                                                                                                                                                                                      |
| Name                 | MIFARE Plus AES_Key4.                                                                                                                                                                                                                                                                                                              |
| Description          | The device uses this property to set 16-byte of the AES_Key4 for MIFARE Plus. On example of the ASE Key = 000102030405060708090A0B0C0D0E0Fh, the setting should be 000102030405060708090A0B0C0D0E0F For security, the Get request for this property will always return 4-MSB of KCV. This key will be encrypted and stored in KPM. |
| Securing Key         | None                                                                                                                                                                                                                                                                                                                               |
| Min. Len (b)         | 16                                                                                                                                                                                                                                                                                                                                 |
| Max. Len (b)         | 16                                                                                                                                                                                                                                                                                                                                 |
| Data Type            | Binary                                                                                                                                                                                                                                                                                                                             |
| Valid Values         |                                                                                                                                                                                                                                                                                                                                    |
| Default              | 00000000 00000000 00000000 00000000                                                                                                                                                                                                                                                                                                |

### [[Table 8.36](#table-8-36)7](\#table-8-367) - Get Request Example

| Example (Hex)                                                                                               |
|-------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 C8 00 |

### [[Table 8.36](#table-8-36)8](\#table-8-368) - Get Response Example

| Example (Hex)                                                                                    |
|--------------------------------------------------------------------------------------------------|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406C804763CBCDE |

### [[Table 8.36](#table-8-36)9](\#table-8-369) - Set Request Example

| Example (Hex)                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C8 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

### [[Table 8.37](#table-8-37)0](\#table-8-370) - Set Response Example

| Example (Hex)                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412C810000102030405060708090A0B0C0D0E0F |

#### Property 1.2.1.1.4.9 MIFARE Plus AES_Key5.

### [[Table 8.37](#table-8-37)1](\#table-8-371) - Property 1.2.1.1.4.9 MIFARE Plus AES_Key5.

| Property Description |                                                                                                                                                                                                                                                                                                                                    |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Property OID         | 1.2.1.1.4.9 / 0x0102010100409                                                                                                                                                                                                                                                                                                      |
| Name                 | MIFARE Plus AES_Key5.                                                                                                                                                                                                                                                                                                              |
| Description          | The device uses this property to set 16-byte of the AES_Key5 for MIFARE Plus. On example of the ASE Key = 000102030405060708090A0B0C0D0E0Fh, the setting should be 000102030405060708090A0B0C0D0E0F For security, the Get request for this property will always return 4-MSB of KCV. This key will be encrypted and stored in KPM. |
| Securing Key         | None                                                                                                                                                                                                                                                                                                                               |
| Min. Len (b)         | 16                                                                                                                                                                                                                                                                                                                                 |
| Max. Len (b)         | 16                                                                                                                                                                                                                                                                                                                                 |
| Data Type            | Binary                                                                                                                                                                                                                                                                                                                             |
| Valid Values         |                                                                                                                                                                                                                                                                                                                                    |
| Default              | 00000000 00000000 00000000 00000000                                                                                                                                                                                                                                                                                                |

### [[Table 8.37](#table-8-37)2](\#table-8-372) - Get Request Example

| Example (Hex)                                                                                               |
|-------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 C9 00 |

### [[Table 8.37](#table-8-37)3](\#table-8-373) - Get Response Example

| Example (Hex)                                                                                    |
|--------------------------------------------------------------------------------------------------|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406C904763CBCDE |

### [[Table 8.37](#table-8-37)4](\#table-8-374) - Set Request Example

| Example (Hex)                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 C9 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

### [[Table 8.37](#table-8-37)5](\#table-8-375) - Set Response Example

| Example (Hex)                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412C910000102030405060708090A0B0C0D0E0F |

#### Property 1.2.1.1.4.A MIFARE Plus AES_Key6.

### [[Table 8.37](#table-8-37)6](\#table-8-376) - Property 1.2.1.1.4.A MIFARE Plus AES_Key6.

| Property Description |                                                                                                                                                                                                                                                                                                                                    |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Property OID         | 1.2.1.1.4.A / 0x010201010040A                                                                                                                                                                                                                                                                                                      |
| Name                 | MIFARE Plus AES_Key6.                                                                                                                                                                                                                                                                                                              |
| Description          | The device uses this property to set 16-byte of the AES_Key6 for MIFARE Plus. On example of the ASE Key = 000102030405060708090A0B0C0D0E0Fh, the setting should be 000102030405060708090A0B0C0D0E0F For security, the Get request for this property will always return 4-MSB of KCV. This key will be encrypted and stored in KPM. |
| Securing Key         | None                                                                                                                                                                                                                                                                                                                               |
| Min. Len (b)         | 16                                                                                                                                                                                                                                                                                                                                 |
| Max. Len (b)         | 16                                                                                                                                                                                                                                                                                                                                 |
| Data Type            | Binary                                                                                                                                                                                                                                                                                                                             |
| Valid Values         |                                                                                                                                                                                                                                                                                                                                    |
| Default              | 00000000 00000000 00000000 00000000                                                                                                                                                                                                                                                                                                |

### [[Table 8.37](#table-8-37)7](\#table-8-377) - Get Request Example

| Example (Hex)                                                                                               |
|-------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 06 D1 01 84 1A D1 01 81 07 2B 06 01 04 01 F6 09 85 01 01 89 0A E2 08 E1 06 E1 04 E4 02 CA 00 |

### [[Table 8.37](#table-8-37)8](\#table-8-378) - Get Response Example

| Example (Hex)                                                                                    |
|--------------------------------------------------------------------------------------------------|
| AA00810482D3D1018204000000008482001ED10181072B06010401F609850101890EE20CE10AE108E406CA04763CBCDE |

### [[Table 8.37](#table-8-37)9](\#table-8-379) - Set Request Example

| Example (Hex)                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 55 D1 11 84 1F D1 11 85 01 01 87 04 02 01 01 04 89 12 CA 10 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F |

### [[Table 8.38](#table-8-38)0](\#table-8-380) - Set Response Example

| Example (Hex)                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------|
| AA00810482E5D1118204000000008482002AD11181072B06010401F609850101891AE218E116E114E412CA10000102030405060708090A0B0C0D0E0F |

24. Property 1.2.1.1.5.1 MCE Mode Setting.
25. The device creates Track 1 and 2 data based on the entered values.
26. The device sends instances of **Notification 0x0101 - Transaction Information Update** to report each of the following:
    1.  Manual Card Entry, Card Event, Data Entered, Reserved
        1.  Manual Card Entry, Data Update, ARQC Update, Data Attached
            1.  Manual Card Entry, Data Update, Batch Update, Data Attached
27. The device sends **Notification 0x0105 - Transaction Operation Complete** to report **Manual Card Entry, Transaction Completed, Reserved, Reserved**.
28. Tip Feature **(Touch Only)**

Tip Operation Use Case Mode 1A

1.  Use Tag A4 for Tip and Tax Options
2.  Use Byte 1 of Tag 81 under A4 to specify Tip mode
    1.  0x01 = Use % mode
    2.  0x02 = Use Amount mode
3.  Bytes 2 through 31 of Tag 81 specifies the % or \$ value to show for Buttons 1 thru 6. There is a button mode to control whether the button is going to show \$/%, CUSTOM, NO TIP, or is disabled.
4.  Tag 82 is the Tax Amount to Display
5.  DF5D = Tip Amount, DF5E = Tax Amount are used for reporting back to the host application.
6.  If available, tags DF5D and DF5E will be sent in the ARQC Data, see \*\*

### [Table 4.51](#table-4-51) - EMV ARQC (DynaPro Format) Type\*\* .

7.  The value of Tag 9F02 provided in command 0x1001 will be updated by the Device by adding TIP and TAX before passing that value to the kernels.
8.  See **Tip & Tax Display Limits (Touch Only)** for display limitations.

Tip Operation Use Case Mode 1B

1.  If **Property 1.1.1.1.2.1 Start Transaction on Touchscreen Event Control(Touch Only)** is Enabled, and there is a socket connection with the host, the device will show the **START SALE** button.
2.  When the cardholder touches the **START SALE** button, the device will automatically start a transaction by asking cardholder to enter the transaction amount. The device will show the **CUSTOM AMOUN**T screen. Press **ENTER** to set transaction amount. The Start Transaction parameters are taken from the settings of these properties
    1.  **Property 1.1.1.1.2.2 Tip Mode(Touch Only)**
    2.  Property 1.1.1.1.2.6 Tip Mode Enable Submit on Amount Button Press
    3.  **Property 1.1.1.1.3.2 Reader Options (Touch Only)**
    4.  **Property 1.1.1.1.3.3 Transaction Options (Touch Only)**
3.  The Device automatically sends a Notification – Transaction Information Update that a transaction has started, \*\*

### [Table 7.11](#table-7-11) - Notification Detail Codes\*\*.

4.  If the **CANCEL** button is touched, the device automatically sends a Notification – Transaction Information Update that a transaction is canceled, \*\*

### [Table 7.11](#table-7-11) - Notification Detail Codes\*\*.

5.  After amount is entered, device checks **Property 1.1.1.1.2.2 Tip Mode(Touch Only)** to determine if TIP mode is enabled, as well as the TIP parameters. The Device will show the **TIP SCREEN** or **CUSTOM AMT** screen per cardholder selection. Press **SUBMIT** to set TIP amount.
6.  The device checks **Property 1.1.1.1.2.3 Tax Rate (Touch Only**) to determine if taxes need to be calculated. If enabled, device calculates the Taxes per the tax rate specified in the property.
7.  If tax function is enabled, the device checks **Property 1.1.1.1.2.4 Display Tax or Surcharge (Touch Only)** to determine how to show the label, tax or surcharge in the **SUMMARY SCREEN**
8.  Tax is only calculated on the amount entered, excluding TIP.
9.  Total Amount = Amount + Tip + Tax Total Amount is the value that will be used for Tag 9F02 of the transaction flow.
10. See **Tip & Tax Display Limits (Touch Only)** for display limitations.
11. Audio Transducer Beep Flow:
12. Upon NFC tag detection, notify HOST
13. Host sends 0x1001 to Start Transaction
14. After NFC is activated - No Beep
15. Host goes thru several Pass-Through commands to R/W NFC
16. A parameter will be added to the Pass-Through command API to indicate if this is the last command
17. If this is the last command, Device -\> Single Beep to indicate CARD CAN BE REMOVED. Turn-Off RF to shut down-card.
18. If an error condition is detected, the device will end session, double-beep, Turn-Off RF to shut down the card.
19. Command 0x1001 – Start a Payment Transaction with an option to show functional button Right **(Display Only)**

The host uses this command to start a payment transaction with an option to display a **Present a Card** page and a green functional button Right (e.g. Service Request button).

![A close-up of a card reader Description automatically generated](media/f70764952a929c699175c5e2a77562c1.png)![A white paper with black text Description automatically generated](media/5736d9f86e309218763966df10451b56.png)

When the cardholder presses the **Service Request** button, the device will send a notification, show **PLEASE WAIT** and await the next command from the host.

![](media/c1e61c1b3177e454bb19be3f4f8d42d6.png)

The host uses **Command 0x1001** to start a payment transaction. If the battery charge is five percent or less, a response is returned indicating that the command has not been executed. See \*\*

### [Table 6.13](#table-6-13) - Response Example for Command 0x1001 – Start Transaction Command not executed due to Battery Charge State\*\*.

### [Table 6.11](#table-6-11) - Request Data for Command 0x1001 - Start Transaction

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     |     |         |
| 1001 = **Command 0x1001 - Start Transaction**                                            |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     |     |         |
| 81                                                                                       | 01  | Reserved                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |     | O   |         |
| 82                                                                                       | 01  | Transaction Timeout, in seconds This parameter defines how long the device waits for the cardholder to take action on any cardholder input, for example, when waiting for the cardholder to present payment after the host starts the transaction. 0x00 = No timeout 0x01 to 0xFF = 1 to 255 seconds                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | B   | R   |         |
| A3                                                                                       | var | Reader Options The parameters inside this TLV data object allow the host to enable and disable the various payment method interfaces.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | T   | O   |         |
| /81                                                                                      | 01  | Magnetic Stripe Reader Mode (MSR Only) 0x00 = Disabled 0x01 = EMV 0x80 = Non-EMV (disables other readers) (MAGTEK INTERNAL ONLY FOR NOW)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | B   | O   | 0x01    |
| /82                                                                                      | 01  | Contact Reader Mode (EMV Contact Only) 0x00 = Disabled 0x01 = EMV                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | B   | O   | 0x01    |
| /83                                                                                      | 01  | Contactless Reader Mode (EMV Contactless Only) 0x00 = Disabled 0x01 = EMV 0x02 = NFC 0x03 = EMV and NFC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | B   | O   | 0x01    |
| /84                                                                                      | 03  | Manual Entry Mode (Touch Only) Populate this parameter to enable manual card entry. When using this feature, all other Reader Mode parameters must be set to **Disabled**. Byte 1 Card Number Valid Format 0x00 = PAN min 8, max 21 digits Byte 2 User Interface Sequence 0x00 = Based on the setting of **Property 1.2.1.1.4.5 MIFARE Plus AES_Key1.** Byte 3 Beeper Feedback 0x00 = On keypress sound disabled 0x01 = On keypress sound enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | B   | O   |         |
| /85                                                                                      | 02  | Barcode Reader Mode (BCR Only) Populate this parameter to enable the device’s barcode reader. This feature can be enabled alongside all other reader modes except Manual Entry Mode. Byte 1 Barcode Reader Enable 0x00 = Disabled 0x01 = Enabled Byte 2 Encrypt Non-EMV Barcode Data 0x00 = Disabled 0x01 = Enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | B   | O   | 0x0000  |
| /86                                                                                      | 01  | PIN Block Format (Touch Only) 0x00 = ISO Format 0 0x03 = ISO Format 3 0x04 = ISO Format 4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | B   | O   | 0x00    |
| A4                                                                                       | var | Tip and Tax Options                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | B   | O   |         |
| /81                                                                                      | 1F  | Byte 1 Tip Mode 0x00 – Disable Tip Mode 0x01 – Show Tip GUI immediately using % value 0x02 – Show Tip GUI immediately using \$ amount 0x11 - Enable Read Channel(s), with +Tip Button, %value 0x12 - Enable Read Channel(s), with +Tip Button, \$ Amount For Tip Modes 0x01 and 0x02, the Tip GUI is shown immediately with selected read channels disabled. They get enabled after the Tip information are entered. For Tip Modes 0x11 and 0x12, the read channels are enabled and “+Tip” button is shown. If no tip is desired, just present the card. If “+Tip” button is selected, read channels are first disabled, then show the Tip GUI. Byte 2, Display Mode for Button1 0 - % or Amount 1 – Display Custom 2 – Display NO TIP 3 – Disabled (An OID controls whether the button is blank, grayed out or not showing, see **Property 1.1.1.1.2.5 Disabled Tip Button Display Mode (Touch Only)**) Bytes 3 to 6 Value in % or Amount for Button 1, if applicable Byte 7, Display Mode for Button 2 (See Byte 2 for Details) Bytes 8 to 11 Value in % or Amount for Button 2, if applicable Byte 12, Display Mode for Button 3 (See Byte 2 for Details) Bytes 13 to 16 Value in % or Amount for Button 3, if applicable Byte 17, Display Mode for Button 4 (See Byte 2 for Details) Bytes 18 to 21 Value in % or Amount for Button 4, if applicable Byte 22, Display Mode for Button 5 (See Byte 2 for Details) Bytes 23 to 26 Value in % or Amount for Button 5, if applicable Byte 27, Display Mode for Button 6 (See Byte 2 for Details) Bytes 28 to 31 Value in % or Amount for Button 6, if applicable **See Property 1.1.1.1.2.2 Tip Mode(Touch Only) for a suggested default value**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | B   | O   |         |
| /82                                                                                      | 06  | Tax or Surcharge Amount to Display See **Property 1.1.1.1.2.4 Display Tax or Surcharge (Touch Only)** to configure display Tax or Surcharge                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | B   | O   |         |
| 84                                                                                       | 02  | Transaction Options This parameter is a bitmask (ORed bits) that sets various device behaviors that change the transaction flow or the way the device reports transaction results, as follows: Byte 1 Apple VAS Mode (**Apple / Google VAS Only, set to 0 if not supported**) Bits 0, 1 0x00 = **Apple/Google VAS Support Disabled** 0x01 = **VAS App OR Payment Mode (Single Mode)**. The device reads only Apple/Google VAS data from a tapped smartphone, or reads EMV payment data from a tapped card. When the device sends ARQC to conclude the transaction, it only includes either EMV payment data in container FC for cards, or includes VAS data in container FE for smartphones 0x02 = **VAS App and Payment Mode (Dual Mode)**. The device reads both Apple/Google VAS data and EMV payment data from a tapped smartphone, or reads EMV payment data from a tapped card. When device sends ARQC to the host to conclude the transaction, it includes EMV payment data in container FC and includes VAS data, if available, in container FE 0x03 = **VAS App Only Mode (VAS Mode)**. The device reads only Apple/Google VAS data from a tapped smartphone, and does not read data from a tapped card. If the tapped smartphone does not support VAS, the device does not detect or read from the smartphone. When the device send ARQC to conclude the transaction, it includes VAS data in container FE and does not include EMV payment data in container FC 0x04 = **Payment Only Mode (Payment Mode)**. The device operates the same as EMV mode (01). It reads only EMV payment data from a tapped smartphone or a tapped card. When the device sends ARQC to conclude the transaction, it includes EMV payment data in container FC and does not include VAS data in container FE. Bits 4, 5, 6 Wallet Mode 4 -Apple 5 - Google 6 - Reserved 0x000 = Wallet Support Disabled 0x001 = Apple VAS Enable 0x002 = Google VAS Enabled 0x003 = –Apple and Google VAS Enabled Bit 7 Apple VAS Protocol Mode o Value 0 – URL VAS Protocol o Value 1 – FULL VAS Protocol Byte 2 Transaction Flow Control Bit 0 Transaction Flow Value 1 = Quick Chip Transaction Flow Value 0 = EMV Transaction Flow Bit 1 Response Format Value 1 = DynaPro Response Format. For sending ARQC data and batch data, the device uses **EMV ARQC (DynaPro Format) Type** and **EMV Batch Data (DynaPro Format) Type**. Value 0 = Reserved. Bit 2 Signature Capture Control (MSR Only). Value 1 = Skip Signature Capture On Service Code. The device skips signature capture during an MSR-only transaction if the card’s service code indicates it is a chip card. Value 0 = Do Not Skip Signature Capture. Bit 3 Display Amount for Quick Chip Transaction Flow Value 1 = Display Amount Value 0 = Do not Display Amount | B   | O   | 0x0003  |
| 86                                                                                       | var | Transaction TLV This is a list of self-contained TLV data objects that defines the basic parameters for the transaction. It may contain any of the following tags in the formats defined in the **EMV 4.3** specification or payment brand specifications, but at minimum it must contain 9C and 9F02, plus 9F03 if the transaction includes cash back. This parameter is optional for Manual Card Entry; to show a transaction amount when using Manual Card Entry, include 9F02 and 5F2A: 9C Transaction Type 9F02 Amount Authorized. If the **Transaction Flow** parameter specifies **Quick Chip Transaction Flow**, the host must specify a non-zero amount. 9F03 Amount Other 9F7C Merchant Custom Data 5F2A Transaction Currency Code 5F36 Transaction Currency Exponent 9F53 Transaction Category Code 9F15 Merchant Category Code 9F16 Merchant ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | B   | R/O |         |
| A8                                                                                       | 00  | (MAGTEK INTERNAL ONLY FOR NOW) Tag Lists                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |     | O   |         |
| 8A                                                                                       |     | (MAGTEK INTERNAL ONLY FOR NOW) Notification Options ??                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |     |     |         |
| AC                                                                                       | var | User Interface Options                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | T   | O   | null    |
| /81                                                                                      | 00  | Suppress Thank You Message By default, devices with a display signal the end of a transaction by briefly showing “THANK YOU,” then “WELCOME.” The host can include this parameter to direct the device to suppress the “THANK YOU” message during this transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | T   | O   | null    |
| /82                                                                                      | 01  | Override Final Transaction Message By default, devices with a display signal the end of a transaction by returning to the idle page and showing “WELCOME.” The host can include this parameter to direct the device to show a different message, chosen from the list of available Display String IDs in section **4.3 Display Strings**. This option completely overrides the device’s idle page behavior until the next transaction, power cycle, or other similar state change.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | B   | O   | null    |
| /83                                                                                      | 02  | Functional button Right option. String ID = Enable the present card page with a green functional button Right – label with a String ID associates with a configured String message. See \*\*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |     |     |         |
|                                                                                          |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     |     |         |

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings.\*\* This button can fit about 15 characters. When user presses this button, device sends notification to the host to indicate the present card functional button Right is pressed. See **Notification 0x1803 - User Interface Host Action Request** If host wants to disable this button, do not include this tag. \| B \| O \| null \|

\| End of any wrappers, at minimum including **Request Message** found on page **55** \| \| \| \| \| \|

### [Table 6.12](#table-6-12) - Response Data for Command 0x1001 - Start Transaction

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1001 = **Command 0x1001 - Start Transaction**                                             |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.13](#table-6-13) - Response Example for Command 0x1001 – Start Transaction Command not executed due to Battery Charge State

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 01 10 01 82 04 80 02 03 16 |

If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**.

### [Table 6.14](#table-6-14) - Request Example (MSR, Contact, and Contactless Only)

| Example (Hex)                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 00 10 01 84 3D 10 01 82 01 3C A3 09 81 01 01 82 01 01 83 01 01 84 02 00 03 86 27 9C 01 00 9F 02 06 00 00 00 00 01 00 9F 03 06 00 00 00 00 00 00 5F 2A 02 08 40 5F 36 01 02 9F 15 02 00 00 9F 53 01 00 |

### [Table 6.15](#table-6-15) - Request Example (Contactless Only)

| Example (Hex)                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 00 10 01 84 3D 10 01 82 01 3C A3 09 81 01 00 82 01 00 83 01 01 84 02 00 03 86 27 9C 01 00 9F 02 06 00 00 00 00 01 00 9F 03 06 00 00 00 00 00 00 5F 2A 02 08 40 5F 36 01 02 9F 15 02 00 00 9F 53 01 00 |

### [Table 6.16](#table-6-16) - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 01 10 01 82 04 01 00 00 00 |

### Command 0x1002 - Continue Transaction (MAGTEK INTERNAL ONLY FOR NOW)

Reserved for future use in operations where **Command 0x1001 - Start Transaction** must suspend for some reason, e.g., waiting for an ARPC response, waiting for a host-driven application selection, etc.

### Command 0x1003 - Finalize (MAGTEK INTERNAL ONLY FOR NOW)

### Command 0x1004 - Resume Transaction

The host uses this command to provide the device with additional / modified data to resume a transaction that is currently paused.

### [Table 6.17](#table-6-17) - Request Data for Command 0x1004 - Resume Transaction

| Tag                                                                                | Len | Value / Description                                                                             | Typ | Req | Default |
|------------------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including Request Message found on page 55   |     |                                                                                                 |     |     |         |
| 1004 = **Command 0x1004 - Resume Transaction**                                     |     |                                                                                                 |     |     |         |
| 81                                                                                 | 01  | Resume Code Indicates the pause state the transaction will resume from: 0x00 = Waiting for ARPC | B   | R   |         |
| 83                                                                                 | var | Reserved                                                                                        | B   | O   |         |
| 84                                                                                 | var | ARPC Data This contains an **EMV ARPC Type**.                                                   | B   | R   |         |
| 86                                                                                 | var | Transaction TLV Update Not applicable when Resume Code = **Waiting for ARPC**                   | B   | O   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                 |     |     |         |

### [Table 6.18](#table-6-18) - Response Data for Command 0x1004 - Resume Transaction

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1004 = **Command 0x1004 - Resume Transaction**                                            |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**.

### [Table 6.19](#table-6-19) - Request Example

| Example (Hex)                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 00 10 04 84 21 10 04 81 01 00 82 01 78 84 17 FF 74 14 DF DF 25 08 99 26 90 E1 16 12 07 10 FA 06 70 04 8A 02 30 30 |

### [Table 6.11](#table-6-11)0 - Response Example

| Example (Hex)                                         |
|-------------------------------------------------------|
| AA 00 81 04 82 06 10 04 82 04 00 00 00 00 84 02 10 04 |

### Command 0x1008 - Cancel Transaction

The host can use this command to cancel a transaction in progress that it initiated using **Command 0x1001 - Start Transaction**.

The sequence of events is as follows:

1.  The host has already called **Command 0x1001 - Start Transaction** and the transaction is still in process.
2.  The host constructs the command request in the format below.
3.  The host sends the command request to the device.
4.  The device sends a response in the format below to the host.
    1.  If the transaction is in a state where it can not be canceled, the device’s response returns operation status detail **Failed, Device State Issue, Cannot Cancel**.
    2.  If there is no transaction in progress, the device’s response returns operation status detail codes **Failed, Device State Issue, No Transaction**.
5.  If the device successfully cancels the transaction, the device’s response returns operation status detail **All Good, Requested Operation Was Successful**, shows **CANCELED** on the display (if any), and returns to the idle state.

### [Table 6.11](#table-6-11)1 - Request Data for Command 0x1008 - Cancel Transaction

| Tag                                                                                      | Len | Value / Description | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                     |     |     |         |
| 1008 = **Command 0x1008 - Cancel Transaction**                                           |     |                     |     |     |         |
| No parameters.                                                                           |     |                     |     |     |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                     |     |     |         |

### [Table 6.11](#table-6-11)2 - Response Data for Command 0x1008 - Cancel Transaction

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1008 = **Command 0x1008 - Cancel Transaction**                                            |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.11](#table-6-11)3 - Request Example

| Example (Hex)                       |
|-------------------------------------|
| AA 00 81 04 01 13 10 08 84 02 10 08 |

### [Table 6.11](#table-6-11)4 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 13 10 08 82 04 00 00 00 00 |

### Command 0x1009 - Close / Clear Transaction (MAGTEK INTERNAL ONLY FOR NOW)

Reserved for future use per Dave.

### Command 0x1014 - Get Transaction Status (MAGTEK INTERNAL ONLY FOR NOW)

Reserved for future use per Dave.

### Command 0x1041 - Set Payment Parameters (MAGTEK INTERNAL ONLY FOR NOW)

Reserved for future use per Dave. MAC.

### Command 0x1042 - Get Payment Parameters (MAGTEK INTERNAL ONLY FOR NOW)

Reserved for future use per Dave.

## Command Group 0x11nn - NFC/MIFARE Pass Through Commands (Contactless Only)

### Command 0x1100 – Pass Through Command For NTag/MIFARE Ultralight, Type 2

After an NTag/MIFARE Ultralight is activated, the host uses this command to send commands and receive responses to and from a Ntag/MIFARE Ultralight. Do not change the address 0x00 for read protection of Ultralight C/AES card because the device will fail to access the card if the address 0x00 is read protected.

### [Table 6.21](#table-6-21) - Request Data for Command 0x1100 – Pass Through Command For NTag/MIFARE Ultralight, Type 2.

| Tag                                                                                  | Len | Value / Description       | Typ | Req | Default |
|--------------------------------------------------------------------------------------|-----|---------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page 55 |     |                           |     |     |         |
| 1100 = **Command 0x1100 – Pass Through Command For NTag/MIFARE Ultralight, Type** 2  |     |                           |     |     |         |
| 81                                                                                   | var | Command to Send. See \*\* |     |     |         |
|                                                                                      |     |                           |     |     |         |

### [Table 6.22](#table-6-22) – NTag Commands\*\* See \*\*

### [Table 6.23](#table-6-23) – MIFARE Ultralight EV1 Commands\*\* See \*\*

### [Table 6.24](#table-6-24) – MIFARE Ultralight C Commands\*\* See \*\*

### [Table 6.25](#table-6-25) – MIFARE Ultralight AES Commands\*\* \| B \| R \| \|

\| 82 \| 01 \| 00 – No Encrypt 01 - Encrypt \| B \| R \| \| \| 83 \| 01 \| 00 – Expect More Commands 01 – FF (Last Command) If the pass-through command is the last successful command, the device will end the transaction with a single beep, indicating success. If an error arises, the device will end the transaction but will sound two beeps to indicate the error. The user should then remove the card. \| B \| R \| \| \| End of any wrappers, at minimum including Request Message found on page **55** \| \| \| \| \| \|

### [Table 6.22](#table-6-22) – NTag Commands

| Command             | Length | Field Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Get Version         | 1      | The GET_VERSION command is used to retrieve information on the NTAG family, the product version, storage size and other product data required to identify the specific NTAG21x. Byte 0 = 0x60                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Read                | 2-3    | The READ command requires a start page address, and returns the 16 bytes of four NTAG21x pages. For example, if address is 03h then pages 03h, 04h, 05h, 06h are returned. Special conditions apply if the READ command address is near the end of the accessible memory area. The special conditions also apply if at least part of the addressed pages is within a password protected area. The READ command with an option of end page address returns the all n\*4 bytes of the addressed pages. For example if the start address is 03h and the end address is 07h then pages 03h, 04h, 05h, 06h and 07h are returned. Byte 0 = 0x30 Byte 1 = Start Page Address Byte 2 = (optional) End Page Address                                                                                                                                                                                         |
| Fast Read           | 3      | The FAST_READ command requires a start page address and an end page address and returns the all n\*4 bytes of the addressed pages. For example, if the start address is 03h and the end address is 07h then pages 03h, 04h, 05h, 06h and 07h are returned. Byte 0 = 0x3A Byte 2 = Start Page Address Byte 3 = End Page Address                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Write               | 6      | The WRITE command requires a block address, and writes 4 bytes of data into the addressed NTAG21x page. Byte 0 = 0xA2 Byte 1 = Address to Write Byte 2 to 5 = 4 Bytes of Data to Write                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Compatibility Write | 18     | The COMPATIBILITY_WRITE command is implemented to guarantee interoperability with the established MIFARE Classic PCD infrastructure, in case of coexistence of ticketing and NFC applications. Even though 16 bytes are transferred to NTAG21x, only the least significant 4 bytes (bytes 0 to 3) are written to the specified address. Set all the remaining bytes, 04h to 0Fh, to logic 00h. Byte 0 = 0xA0 Byte 1 = Address to Write Byte 2 to 17 = 16 Bytes of Data to Write (only least significant 4 bytes are written) Note: This command is sent in 2 steps, which the Firmware will handle \<CMD\>\<Address to Write\>\<CRCH\>\<CRCL\> \<16 Bytes of Data to Write\>\<CRCH\>\<CRCL\>                                                                                                                                                                                                       |
| READ_CNT            | 2      | The READ_CNT command is used to read out the current value of the NFC one-way counter of the NTAG213, NTAG215 and NTAG216. The command has a single argument specifying the counter number and returns the 24-bit counter value of the corresponding counter. If the NFC_CNT_PWD_PROT bit is set to 1b the counter is password protected and can only be read with the READ_CNT command after a previous valid password authentication Byte 0 = 0x39 Byte 1 = 0x02 (NFC Counter Address)                                                                                                                                                                                                                                                                                                                                                                                                           |
| PWD_AUTH            | 5      | A protected memory area can be accessed only after a successful password verification using the PWD_AUTH command. The AUTH0 configuration byte defines the protected area. It specifies the first page that the password mechanism protects. The level of protection can be configured using the PROT bit either for write protection or read/write protection. The PWD_AUTH command takes the password as parameter and, if successful, returns the password authentication acknowledge, PACK. By setting the AUTHLIM configuration bits to a value larger than 000b, the number of unsuccessful password verifications can be limited. Each unsuccessful authentication is then counted in a counter featuring anti-tearing support. After reaching the limit of unsuccessful attempts, the memory access specified in PROT, is no longer possible. Byte 0 = 0x1B Byte 1..4 = password (4 bytes) |
| READ_SIG            | 2      | The READ_SIG command returns an IC specific, 32-byte ECC signature, to verify NXP Semiconductors as the silicon vendor. The signature is programmed at chip production and cannot be changed afterwards. Byte 0 = 0x3C Byte 1 = 0x00, RFU                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

### [Table 6.23](#table-6-23) – MIFARE Ultralight EV1 Commands

| Command             | Length | Field Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Get Version         | 1      | The GET_VERSION command is used to retrieve information on the MIFARE family, product version, storage size and other product data required to identify the MF0ULx1. Byte 0 = 0x60                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Read                | 2-3    | The READ command requires a start page address, and returns the 16 bytes of four MIFARE Ultralight pages. For example if address (Addr) is 03h then pages 03h, 04h, 05h, 06h are returned. A rollover mechanism is implemented if the READ command address is near the end of the accessible memory area. This rollover mechanism is also used when at least part of the addressed pages is within a password protected area. The READ command with an option of end page address returns the all n\*4 bytes of the addressed pages. For example if the start address is 03h and the end address is 07h then pages 03h, 04h, 05h, 06h and 07h are returned. Byte 0 = 0x30 Byte 1 = Start Page Address Byte 2 = (optional) End Page Address                                                                                                                                                          |
| Fast Read           | 3      | The FAST_READ command requires a start page address and an end page address and returns the all n\*4 bytes of the addressed pages. For example if the start address is 03h and the end address is 07h then pages 03h, 04h, 05h, 06h and 07h are returned. Byte 0 = 0x3A Byte 2 = Start Page Address Byte 3 = End Page Address                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Write               | 6      | The WRITE command requires a block address, and writes 4 bytes of data into the addressed MIFARE Ultralight EV1 page. Byte 0 = 0xA2 Byte 1 = Address to Write Byte 2 to 5 = 4 Bytes of Data to Write                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Compatibility Write | 18     | The COMPATIBILITY_WRITE command is implemented to accommodate the established MIFARE Classic PCD infrastructure. Even though 16 bytes are transferred to the MF0ULx1, only the least significant 4 bytes (bytes 0 to 3) are written to the specified address. Set all the remaining bytes, 04h to 0Fh, to logic 00h Byte 0 = 0xA0 Byte 1 = Address to Write Byte 2 to 17 = 16 Bytes of Data to Write (only least significant 4 bytes are written) Note: This command is sent in 2 steps, which the Firmware will handle \<CMD\>\<Address to Write\>\<CRCH\>\<CRCL\> \<16 Bytes of Data to Write\>\<CRCH\>\<CRCL\>                                                                                                                                                                                                                                                                                   |
| READ_CNT            | 2      | The READ_CNT command is used to read out the current value of one of the 3 one-way counters of the MF0ULx1. The command has a single argument specifying the counter number and returns the 24-bit counter value of the corresponding counter. The counters are always readable, independent on the password protection settings. Byte 0 = 0x39 Byte 1 = 0x00..0x02 (counter number from 0x00 to 0x02)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| INCR_CNT            | 6      | The INCR_CNT command is used to increment one of the 3 one-way counters of the MF0ULx1. The two arguments are the counter number and the increment value. Byte 0 = 0xA5 Byte 1 = 0x00..0x02 (counter number from 0x00 to 0x02) Byte 2 to 5 = 4 bytes increment value (only the 3 least significant bytes are relevant)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PWD_AUTH            | 5      | A protected memory area can be accessed only after a successful password verification using the PWD_AUTH command. The AUTH0 configuration byte defines the protected area. It specifies the first page that the password mechanism protects. The level of protection can be configured using the PROT bit either for write protection or read/ write protection. The PWD_AUTH command takes the password as parameter and, if successful, returns the password authentication acknowledge, PACK. By setting the AUTHLIM configuration bits to a value larger than 000b, the number of unsuccessful password verifications can be limited. Each unsuccessful authentication is then counted in a counter featuring anti-tearing support. After reaching the limit of unsuccessful attempts, the memory access specified in PROT, is no longer possible. Byte 0 = 0x1B Byte 1..4 = password (4 bytes) |
| READ_SIG            | 2      | The READ_SIG command returns an IC specific, 32-byte ECC signature, to verify NXP Semiconductors as the silicon vendor. The signature is programmed at chip production and cannot be changed afterwards. Byte 0 = 0x3C Byte 1 = 0x00, RFU                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| CHECK TEARING_EVENT | 2      | The CHECK_TEARING_EVENT command enables the application to identify if a tearing event happened on a specified counter element. It takes the counter number as single argument and returns a specified valid flag for this counter. If the returned valid flag is not equal to the predefined value, a tearing event happened. Note, although a tearing event might have happened on the counter, a valid value corresponding to the last valid counter status is still available using the READ_CNT command. Byte 0 = 0x3E Byte 1 = 0x00..0x02 (counter number from 0x00 to 0x02)                                                                                                                                                                                                                                                                                                                  |
| VCSL                | 21     | The VCSL command is used to enable a unique identification and selection process across different MIFARE product-based cards and card implementations on mobile devices. The command requires a 16-byte installation identifier IID and a 4-byte PCD capability value as parameters. The parameters are present to support compatibility to other MIFARE product-based devices but are not used or checked inside the MF0ULx1. Nevertheless, the number of bytes is checked for correctness. The answer to the VCSL command is the virtual card type identifier VCTID. This identifier indicates the type of card or ticket. Using this information, the reader can decide whether the ticket belongs to the installation or not. Byte 0 = 0x4B Byte 1 to 16 = 16-byte IID (installation identifier, can be any number) Byte 17 to 20 = 4-byte PCDCAPS (PCD capabilities, can be any number)        |

### [Table 6.24](#table-6-24) – MIFARE Ultralight C Commands

| Command             | Length | Field Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Read                | 2-3    | The READ command takes the page address as a parameter. Only addresses 00h to 2Bh are decoded. For higher addresses the MF0ICU2 returns a NAK. The MF0ICU2 responds to the READ command by sending 16 bytes starting from the page address defined in the command (e.g. if ADR is 03h, pages 03h, 04h, 05h, 06h are returned) A roll-over mechanism is implemented to continue reading from page 00h once the end of the accessible memory is reached. For example, reading from address 29h on a MF0ICU2 results in pages 29h, 2Ah, 2Bh and 00h being returned. The following conditions apply if part of the memory is protected by the 3DES authentication for read access: • if the MF0ICU2 is in the ACTIVE state – addressing a page which is equal or higher than AUTH0 results in a NAK response – addressing a page lower than AUTH0 results in data being returned with the roll-over mechanism occurring just before the AUTH0 defined page • if the MF0ICU2 is in the AUTHENTICATED state – the READ command behaves like on a MF0ICU2 without access protection. The READ command with an option of end page address returns the all n\*4 bytes of the addressed pages. For example if the start address is 03h and the end address is 07h then pages 03h, 04h, 05h, 06h and 07h are returned. Byte 0 = 0x30 Byte 1 = Start Page Address Byte 2 = (optional) End Page Address |
| Write               | 6      | The WRITE command is used to program the lock bytes in page 02h, the OTP bytes in page 03h, data bytes in pages 04h to 27h, configuration data from page 28h to 2B and keys from page 2Ch to 2Fh. A WRITE command is performed page-wise, programming 4 bytes in a page. Byte 0 = 0xA2 Byte 1 = Address to Write Byte 2 to 5 = 4 Bytes of Data to Write                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Compatibility Write | 18     | The COMPATIBILITY WRITE command was implemented to accommodate the established MIFARE PCD infrastructure. Even though 16 bytes are transferred to the MF0ICU2, only the least significant 4 bytes (bytes 0 to 3) will be written to the specified address. It is recommended to set the remaining bytes 4 to 15 to all 0. Byte 0 = 0xA0 Byte 1 = Address to Write Byte 2 to 17 = 16 Bytes of Data to Write (only least significant 4 bytes are written) Note: This command is sent in 2 steps, which the Firmware will handle \<CMD\>\<Address to Write\>\<CRCH\>\<CRCL\> \<16 Bytes of Data to Write\>\<CRCH\>\<CRCL\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| AUTHENTICATE        | 2      | The AUTHENTICATE command is used to authenticate the MF0ICU2 using 2 keys 3DES encryption in Cipher-Block Chaining (CBC) mode as described in ISO/IEC 10116. The 16-byte of the 2keys 3DES are programmed to card memory pages from 2Ch to 2Fh. The key itself can be written during personalization or at any later stage using the WRITE or COMPATIBILITY WRITE with Byte 0 is always sent first. On example of Key1 = 0001020304050607h and Key2 = 08090A0B0C0D0E0Fh, the command sequence needed for key programming with WRITE command is: • A2 2C 07 06 05 04 • A2 2D 03 02 01 00 • A2 2E 0F 0E 0D 0C • A2 2F 0B 0A 09 08 The 16-byte of the same 2keys 3DES are programed to the Device using **Property 1.2.1.1.4.1 MIFARE Ultralight C 2keys3DES** Byte 0 = 0x1A Byte 1 = 0x00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

### [Table 6.25](#table-6-25) – MIFARE Ultralight AES Commands

| Command      | Length | Field Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Get Version  | 1      | The GET_VERSION command is used to retrieve information on the MIFARE family, product version, storage size and other product data required to identify the MIFARE Ultralight AES. Byte 0 = 0x60                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Read         | 2-3    | The READ command requires a start page address, and returns the 16 bytes of four pages. For example, if address (Addr) is 03h then pages 03h, 04h, 05h, 06h are returned. So called roll-over mechanism (described later) applies if the READ command address is near the end of the accessible memory area. Same mechanism applies if at least part of the addressed pages is within an authentication protected area In the default state of MIFARE Ultralight AES, all memory pages in the range from 00h to 3Bh are allowed as Addr parameter to the READ command. Addressing a memory page above the limit results in a NAK response. A roll-over mechanism is implemented to continue reading from page 00h once the end of the accessible memory is reached if at least first addressed page is within allowed limit. **Remark**: AES key values can never be directly read out of the memory. When reading from the pages holding key values, all 00h bytes are returned. The READ command with an option of end page address returns the all n\*4 bytes of the addressed pages. For example if the start address is 03h and the end address is 07h then pages 03h, 04h, 05h, 06h and 07h are returned. Byte 0 = 0x30 Byte 1 = Start Page Address Byte 2 = (optional) End Page Address                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Fast Read    | 3      | The FAST_READ command requires a start page address and an end page address and returns bytes of addressed pages. For example if the start address is 03h and the end address is 07h then pages 03h, 04h, 05h, 06h, and 07h are returned. If either start or end address is outside accessible area, then MIFARE Ultralight AES replies with a NAK. Byte 0 = 0x3A Byte 2 = Start Page Address Byte 3 = End Page Address                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Write        | 6      | The WRITE command requires a block address, and writes 4 bytes of data into the addressed MIFARE Ultralight AES page. Byte 0 = 0xA2 Byte 1 = Address to Write Byte 2 to 5 = 4 Bytes of Data to Write                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| READ_CNT     | 2      | The READ_CNT command is used to read out the current value of one of the 3 one-way counters of MIFARE Ultralight AES. The command has a single argument specifying the counter number and returns the 24-bit counter value of the corresponding counter. Counters are always readable, except in case of the counter "0x02" with the optional AES authentication protection enabled. In that case, the counter 0x02 is readable only in the AUTHENTICATE state. Byte 0 = 0x39 Byte 1 = 0x00..0x02 (counter number from 0x00 to 0x02)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| INCR_CNT     | 6      | The INCR_CNT command is used to increment one of the 3x one-way counters of the MIFARE Ultralight AES. Two arguments are the counter number and the increment value. Counters are always incrementable, except in case of the counter "0x02" with the optional AES authentication protection enabled. In that case, the counter 0x02 can be incremented only in the AUTHENTICATE state. Byte 0 = 0xA5 Byte 1 = 0x00..0x02 (counter number from 0x00 to 0x02) Byte 2 to 5 = 4 bytes increment value (only the 3 least significant bytes are relevant)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| READ_SIG     | 2      | The READ_SIG command returns an IC-specific, 48-byte ECC signature. The originality signature can be changed if it has been unlocked with the LOCK_SIG command. Byte 0 = 0x3C Byte 1 = 0x00, RFU                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| WRITE_SIG    | 6      | The WRITE_SIG command allows the writing of a customized originality signature into the dedicated originality signature memory. The WRITE_SIG command requires an originality signature block address, and writes 4 bytes of data into the addressed originality signature block. In the initial state of MIFARE Ultralight AES, the following originality signature blocks 00h to 0Bh are valid Addr parameters to the WRITE_SIG command. Addressing a memory block beyond the limits above results in a NAK response from MIFARE Ultralight AES. If the originality signature is locked or permanently locked, a WRITE_SIG command results in a NAK response from the MIFARE Ultralight AES. Byte 0 = 0xA9 Byte 1 = signature block address Byte 2 to 5 = signature bytes to be written                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| LOCK_SIG     | 2      | The LOCK_SIG command allows the user to unlock, lock or permanently lock the dedicated originality signature memory. The originality signature can only be unlocked, if the originality signature is not permanently locked. There is no command to unlock the originality signature, if the originality signature is permanently locked. Byte 0 = 0xAC Byte 1 = lock option 0x00 = unlock 0x01 = lock 0x02 = permanently lock                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| VCSL         | 21     | The VCSL command is used to enable a unique identification and selection process across different physical MIFARE product-based cards and virtual MIFARE implementations. The command requires a 16-byte installation identifier IID and a 4-byte PCD capability value as parameters. The parameters are present to support compatibility to other MIFARE product-based devices, but are not used or checked inside the MIFARE Ultralight AES. Nevertheless, the number of bytes is checked for correctness. The answer to the VCSL command is the VCTID value stored in the user configuration segment. This identifier indicates the type of card or ticket. Using this information, the contactless reader can decide whether the ticket belongs to the installation or not. Byte 0 = 0x4B Byte 1 to 16 = 16-byte IID (installation identifier, can be any number) Byte 17 to 20 = 4-byte PCDCAPS (PCD capabilities, can be any number)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| AUTHENTICATE | 2      | The AUTHENTICATE command is used to authenticate with a 3-pass mutual authentication the MIFARE Ultralight AES and PCD. The cryptographic method is based on AES in Cipher-Block chaining (CBC) mode according to NIST Special Publication 800-38A. The used key is a 128-bit AES Key. Remark: To reduce the risk on card-only side channel attack to the AES keys, a failed authentication limit (AUTH_LIM) can be set. The 16 bytes of the AES [DataProtKey] are programmed to memory pages from 30h to 33h. Keys themselves can be written during personalization or at any later stage in a secure environment, as long as the key is not locked for update in the user configuration segment. AES [UIDRetrKey] is stored in memory addresses from 34h until 37h. In case keys are not locked, MIFARE Ultralight AES allows to change AES-keys without authentication as long as AUTH0 is not set to a page address before or at page address where keys bytes are stored. Otherwise MIFARE Ultralight AES requires to be in the AUTHENTICATED state to allow to write AES keys. The key itself can be written using the WRITE with Byte 0 is always sent first. On example of AES [DataProtKey] = 000102030405060708090A0B0C0D0E0Fh, the command sequence needed for key programming with WRITE command is: • A2 30 0F 0E 0D 0C • A2 31 0B 0A 09 08 • A2 32 07 06 05 04 • A2 33 03 02 01 00 On example of AES [UIDRetrKey] = 000102030405060708090A0B0C0D0E0Fh, the command sequence needed for key programming with WRITE command is: • A2 34 0F 0E 0D 0C • A2 35 0B 0A 09 08 • A2 36 07 06 05 04 • A2 37 03 02 01 00 The 16-byte of the same AES [DataProtKey] are programed to the Device using **Property 1.2.1.1.4.2 MIFARE Ultralight AES DataProtKey**. The 16-byte of the same AES [UIDRetrKey] are programed to the Device using **Property 1.2.1.1.4.3 MIFARE Ultralight AES UIDRetrKey**. The 16-byte of the AES [OriginalityKey] are programed to the Device using **Property 1.2.1.1.4.4 MIFARE Ultralight AES OriginalityKey.** This key value is only known by NXP. Byte 0 = 0x1A Byte 1 = Key option 0x00 = DataProtKey 0x01 = UIDRetrKey 0x02 = OriginalityKey |

### [Table 6.26](#table-6-26) - Response Data for Command 0x1100 – Pass Through Command For NTag/MIFARE Ultralight, Type 2

| Tag                                                                                                 | Len | Value / Description                            | Typ | Req | Default |
|-----------------------------------------------------------------------------------------------------|-----|------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including Response Message found on page **56**               |     |                                                |     |     |         |
| 1100 = Command 0x1100 – Pass Through Command For NTag/MIFARE Ultralight, Type 2 Command For NFC Tag |     |                                                |     |     |         |
| 81                                                                                                  | 01  | Tag Response Code 0x00 = Success 0x01 = Failed | B   | R   | N/A     |
| 82                                                                                                  | var | Encryption Control If encrypted, see           |     |     |         |
|                                                                                                     |     |                                                |     |     |         |

### [Table 6.29](#table-6-29) - Payload for Encrypted NFC/MIFARE Data If unencrypted see

### [Table 6.21](#table-6-21)0 – Unencrypted NFC/MIFARE Data \| B \| O \| N/A \|

\| End of any wrappers, at minimum including Response Message found on page **56** \| \| \| \| \| \|

If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**.

### [Table 6.27](#table-6-27) - Request Example (Get Version)

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA 00 81 04 01 39 11 00 84 0B 11 00 81 01 60 82 01 00 83 01 00 |

### [Table 6.28](#table-6-28) - Response Example (Get Version)

| Example (Hex)                                                                                               |
|-------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 82 39 11 00 82 04 01 00 00 00 84 14 11 00 81 01 00 82 0D FC 0B DF 7A 08 01 02 03 04 05 06 07 08 |

#### Encrypted Data Format

### [Table 6.29](#table-6-29) - Payload for Encrypted NFC/MIFARE Data

| Tag     | Len | Value / Description                                                                                                                                                                                                                                                               | Typ | Req | Default |
|---------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| /DFDF59 | var | Encrypted Data Primitive Decrypt the value of this TLV data object using the algorithm and variant specified in the **Encrypted Data KSN** parameter and the **Encrypted Data Encryption Type** parameter to read its contents. The format of the decrypted data is shown in \*\* |     |     |         |
|         |     |                                                                                                                                                                                                                                                                                   |     |     |         |

### [Table 6.21](#table-6-21)0 – Unencrypted NFC/MIFARE\*\* Data. \| B \| R \| \|

\| /DFDF50 \| var \| Encrypted Data KSN \| B \| R \| \| \| /DFDF51 \| 01 \| Encrypted Data Encryption Type See section 4.4 Encryption Type for a list of valid values. \| B \| R \| \| \| End of Notification Message found on page **62** \| \| \| \| \| \|

### [Table 6.21](#table-6-21)0 – Unencrypted NFC/MIFARE Data

| Tag   | Len | Value / Description | Typ | Req | Default |
|-------|-----|---------------------|-----|-----|---------|
| FC    | var | NFC Data Container  | T   | R   |         |
| /DF7A | var | NFC Data            | B   | O   |         |

### Command 0x1101 – Pass Through Command for MIFARE Classic/MINI®/Plus SL1 (Security Level 1), Type 2

After a MIFARE Tag is activated, the host uses this command to send commands and receive responses to and from a MIFARE tag.

For MIFARE Plus EV1/EV2/SE/X at SL1 (Security Level 1), the tag is discovered as MIFARE Classic, and can use the same functionality as MIFARE Classic 1K/4K commands in \*\*

### [Table 6.21](#table-6-21)2 – MIFARE Classic/MINI\*\*® Commands\*\*.\*\* Furthermore, an additional optional AES authentication is available in this level without affecting the MIFARE Classic 1K/4K functionality. The authenticity of the card can be proven using strong cryptographic means with this additional functionality. In addition to the backwards compatibility mode, MIFARE Plus card can be switched to higher security levels. After MIFARE Plus is authenticated with AES Security Level 1 Key, the Device doesn’t auto detect an error from the MIFARE Tag has been removed to end the pass-through session. To end the pass-through session, the Host application can send the last command, CANCEL command (0xFF), or receive error response from the MIFARE Tag.

### [Table 6.21](#table-6-21)1 - Request Data for Command 0x1101 - Pass Through Command for MIFARE Classic/MINI®/Plus SL1 (Security Level 1)

| Tag                                                                                                           | Len | Value / Description       | Typ | Req | Default |
|---------------------------------------------------------------------------------------------------------------|-----|---------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page 55                          |     |                           |     |     |         |
| 1101 = **Command 0x1101 – Pass Through Command for MIFARE Classic/MINI®/Plus SL1 (Security Level 1), Type 2** |     |                           |     |     |         |
| 81                                                                                                            | var | Command to Send. See \*\* |     |     |         |
|                                                                                                               |     |                           |     |     |         |

### [Table 6.21](#table-6-21)2 – MIFARE Classic/MINI\*\*® Commands See \*\*

### [Table 6.21](#table-6-21)3 – MIFARE Plus EV1/EV2/SE/X SL1 (Security Level 1)\*\* Commands \| B \| R \| \|

\| 82 \| 01 \| 00 – No Encrypt 01 - Encrypt \| \| \| \| \| 83 \| 01 \| 00 – Expect More Commands 01 – FF (Last Command) If last command, Device will provide a single beep after receiving a successful response from tag, otherwise, device will provide a double beep \| B \| R \| \| \| End of any wrappers, at minimum including Request Message found on page **55** \| \| \| \| \| \|

### [Table 6.21](#table-6-21)2 – MIFARE Classic/MINI® Commands

| Command          | Length | Field Value                                                                                                                                                                                                                               |
|------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MIFARE Read      |        | Byte 0 – 0x30 – Read Command Byte 1- Sector Number to Read Byte 2 – Start Block Number Byte 3 – End Block Number Byte 4 – Key Type, 0 = A, 1 = B Byte 5 to 10 = 6 Byte Key                                                                |
| MIFARE Write     |        | Byte 0 – 0xA0 – Write Command Byte 1- Sector Number to Write Byte 2 – Start Block Number Byte 3 – End Block Number Byte 4 – Key Type 0 = A, 1 = B Byte 5 to 10 = 6 Byte Key Byte 11 to x = Variable length Byte Data (16 bytes per block) |
| MIFARE Increment |        | Byte 0 – 0xC1 – Increment Command Byte 1 – Source Sector Number Byte 2- Source Block number Byte 3 – Key Type 0 = A, 1 = B Byte 4 to 9 = 6 Byte Key Byte 10 to 13 = 4 Byte Operand                                                        |
| MIFARE Decrement |        | Byte 0 – 0xC0 – Decrement Command Byte 1 – Source Sector Number Byte 2- Source Block number Byte 3 – Key Type 0 = A, 1 = B Byte 4 to 9 = 6 Byte Key Byte 10 to 13 = 4 Byte Operand                                                        |
| MIFARE Restore   |        | Byte 0 – 0xC2 – Restore Command Byte 1 – Source Sector Number Byte 2 - Source Block number Byte 3 – Key Type 0 = A, 1 = B Byte 4 to 9 = 6 Byte Key                                                                                        |
| MIFARE Transfer  |        | Byte 0 – 0xB0 – Write the value from the Transfer Buffer into destination block number Byte 1 – Destination Sector Number Byte 2 - Destination Block number Byte 3 – Key Type 0 = A, 1 = B Byte 4 to 9 = 6 Byte Key                       |

### [Table 6.21](#table-6-21)3 – MIFARE Plus EV1/EV2/SE/X SL1 (Security Level 1) Commands

| Command                                  | Length | Field Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | EV1 | EV2 | SE | X |
|------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|----|---|
| First Authenticate (part1 and part2)     | 3      | First Authenticate. Use this command to switch to higher security levels. This command is behaved as the last command. Device will provide a single beep after receiving a successful response from a card, otherwise, device will provide a double beep. Byte 0 = 0x70 Byte 1-2 = Level 2 Switch Key (MIFARE Plus X only), or Level 3 Switch Key. See NXP doc ds206234, table 113. Byte 3 = MIFARE Plus AES_Key\# 0x01 = AES_Key1 = 16 bytes value stored in **Property 1.2.1.1.4.5 MIFARE Plus AES_Key1.** 0x02 = AES_Key2 = 16 bytes value stored in **Property 1.2.1.1.4.6 MIFARE Plus AES_Key2.** 0x03 = AES_Key3 = 16 bytes value stored in **Property 1.2.1.1.4.7 MIFARE Plus AES_Key3.** 0x04 = AES_Key4 = 16 bytes values stored in **Property 1.2.1.1.4.8 MIFARE Plus AES_Key4.** 0x05 = AES_Key5 = 16 bytes values stored in **Property 1.2.1.1.4.9 MIFARE Plus AES_Key5.** 0x06 = AES_Key6 = 16 bytes values stored in **Property 1.2.1.1.4.A MIFARE Plus AES_Key6.**                                                                                                          | Y   | Y   | Y  | Y |
| Following Authenticate (part1 and part2) | 3      | Following Authenticate. Use this command for an option to put the NFC tag in Security Level 1 AES Authenticated before sending MIFARE Classic commands. Byte 0 = 0x76 Byte 1-2 = Security Level 1 Card Authentication Key. See NXP doc ds206234, table 113. Byte 3 = MIFARE Plus AES_Key\# 0x01 = AES_Key1 = 16 bytes value stored in **Property 1.2.1.1.4.5 MIFARE Plus AES_Key1.** 0x02 = AES_Key2 = 16 bytes value stored in **Property 1.2.1.1.4.6 MIFARE Plus AES_Key2.** 0x03 = AES_Key3 = 16 bytes value stored in **Property 1.2.1.1.4.7 MIFARE Plus AES_Key3.** 0x04 = AES_Key4 = 16 bytes values stored in **Property 1.2.1.1.4.8 MIFARE Plus AES_Key4.** 0x05 = AES_Key5 = 16 bytes values stored in **Property 1.2.1.1.4.9 MIFARE Plus AES_Key5.** 0x06 = AES_Key6 = 16 bytes values stored in **Property 1.2.1.1.4.A MIFARE Plus AES_Key6.**                                                                                                                                                                                                                                  | Y   | Y   | Y  | Y |
| READ_SIG                                 | 2      | The READ_SIG command returns an IC-specific, 48-byte ECC originality check signature. Byte 0 = 0x3C Byte 1 = 0x00, RFU                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Y   | Y   | N  | N |
| Personalize UID                          | 2      | Set anti-collision, selection and authentication behavior. The execution of this command requires an authentication to MF Classic sector 0. Once this command has been issued and accepted by the PICC, the configuration is automatically locked. A subsequently issued ‘Personalize UID Usage’ command is not executed and fails. Byte 0 = 0x40 Byte 1 = Encoded type of UID usage: 0x00 = UIDF0 = anti-collision and selection with the double size UID (7-byte) according to ISO/IEC14443-3 0x40 = UIDF1 = anti-collision and selection with the double size UID (7-byte) according to ISO/IEC 14443-3 and optional usage of a selection process shortcut 0x20 = UIDF2 = anti-collision and selection with a single size random ID (4-byte) according to ISO/IEC14443-3. After the card is configured with random ID, it won’t be able perform any MF Classic authentication since MF Classic authentication requires UID. 0x60 = UIDF3 = anti-collision and selection with a single size NUID (4-byte) according to ISO/IEC14443-3 where the NUID is calculated out of the 7-byte UID | Y   | Y   | N  | N |
| CANCEL                                   | 1      | This command is used to terminate the pass-through command session. Byte 0 = 0xFF                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Y   | Y   | Y  | Y |

### [Table 6.21](#table-6-21)4 - Response Data for Command 0x1101 – Pass Through Command for MIFARE Classic/MINI®/Plus SL1 (Security Level 1), Type 2

| Tag                                                                                                           | Len | Value / Description                                                                                                                                   | Typ | Req | Default |
|---------------------------------------------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including Response Message found on page **56**                         |     |                                                                                                                                                       |     |     |         |
| 1101 = **Command 0x1101 – Pass Through Command for MIFARE Classic/MINI®/Plus SL1 (Security Level 1), Type 2** |     |                                                                                                                                                       |     |     |         |
| 81                                                                                                            | var | Tag Response Code Byte 0 = 0x00 = Success Byte 0 = 0x01 = I/O Failed Byte 0 = 0x02 Authentication Failed Byte 1 = 0x01 = Block that Failed (optional) | B   | R   | N/A     |
| 82                                                                                                            | var | Encryption Control If encrypted, see \*\*                                                                                                             |     |     |         |
|                                                                                                               |     |                                                                                                                                                       |     |     |         |

### [Table 6.29](#table-6-29) - Payload for Encrypted NFC/MIFARE\*\* Data If unencrypted see \*\*

### [Table 6.21](#table-6-21)0 – Unencrypted NFC/MIFARE\*\* Data \| B \| O \| N/A \|

\| End of any wrappers, at minimum including Response Message found on page **56** \| \| \| \| \| \|

If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**.

### [Table 6.21](#table-6-21)5 - Request Example (Read Sector 0, Block Number Start 0 - End 0, KeyType A, Key = FFFFFFFFFFFF)

| Example (Hex)                                                                                |
|----------------------------------------------------------------------------------------------|
| AA 00 81 04 01 19 11 01 84 15 11 01 81 0B 30 00 00 00 00 FF FF FF FF FF FF 82 01 00 83 01 00 |

### [Table 6.21](#table-6-21)6 - Response Example (Read Sector 0, Block Number Start 0 - End 0, KeyType A, Key = FFFFFFFFFFFF)

| Example (Hex)                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 82 19 11 01 82 04 01 00 00 00 84 1C 11 01 81 01 00 82 15 FC 13 DF 7A 10 A4 FB 0D 3E 6C 08 04 00 03 0D C0 90 EE BF BB 1D |

#### Encrypted Data Format

### [Table 6.21](#table-6-21)7 - Payload for Encrypted NFC/MIFARE Data

| Tag                                                                             | Len | Value / Description                                                                                                                                                                                                                                                                                     | Typ | Req | Default |
|---------------------------------------------------------------------------------|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| /DFDF59                                                                         | var | Encrypted Data Primitive Decrypt the value of this TLV data object using the algorithm and variant specified in the **Encrypted Data KSN** parameter and the **Encrypted Data Encryption Type** parameter to read its contents. The format of the decrypted data is shown in [Table 7.59](#table-7-59). | B   | R   |         |
| /DFDF50                                                                         | var | Encrypted Data KSN                                                                                                                                                                                                                                                                                      | B   | R   |         |
| /DFDF51                                                                         | 01  | Encrypted Data Encryption Type See section 4.4 Encryption Type for a list of valid values.                                                                                                                                                                                                              | B   | R   |         |
| End of any wrappers, at minimum including Response Message found on page **56** |     |                                                                                                                                                                                                                                                                                                         |     |     |         |

### [Table 6.21](#table-6-21)8 – Unencrypted NFC/MIFARE Data

| Tag   | Len | Value / Description       | Typ | Req | Default |
|-------|-----|---------------------------|-----|-----|---------|
| FC    | var | NFC/MIFARE Data Container | T   | R   |         |
| /DF7A | var | NFC/MIFARE Data           | B   | O   |         |

### Command 0x1102 – Pass Through Command for MIFARE DESFire, Type 4

After a MIFARE DESFire Light/EV1/EV2/EV3 Tag is activated, the host uses this command to send commands and receive responses to and from a MIFARE DESFire Tag.

There will be a fixed 30 second timeout for commands that require multiple command/responses.

### [Table 6.21](#table-6-21)9 - Request Data for Command 0x1102 – Pass Through Command for MIFARE DESFire, Type 4

| Tag                                                                                  | Len | Value / Description                                                                                                                                                                              | Typ | Req | Default |
|--------------------------------------------------------------------------------------|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page 55 |     |                                                                                                                                                                                                  |     |     |         |
| 1102 **=** **Command 0x1102 – Pass Through Command for MIFARE DESFire, Type 4**      |     |                                                                                                                                                                                                  |     |     |         |
| 81                                                                                   | var | Command to Send. See DESFire Data Sheet (MF2DLHX0) Should follow ISO 7816-4 APDU format C-APDU CLA INS P1 P2 Lc Data Le                                                                          | B   | R   |         |
| 82                                                                                   | 01  | 00 – No Encrypt 01 - Encrypt                                                                                                                                                                     |     |     |         |
| 83                                                                                   | 01  | 00 – Expect More Commands 01 – FF (Last Command) If last command, Device will provide a single beep after receiving a successful response from tag, otherwise, device will provide a double beep | B   | R   |         |
| End of any wrappers, at minimum including Request Message found on page **55**       |     |                                                                                                                                                                                                  |     |     |         |

### [Table 6.22](#table-6-22)0 - Response Data for Command 0x1102 – Pass Through Command for MIFARE DESFire, Type 4

| Tag                                                                                   | Len | Value / Description                                                                                                                                                        | Typ | Req | Default |
|---------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including Response Message found on page **56** |     |                                                                                                                                                                            |     |     |         |
| 1102 = **Command 0x1102 – Pass Through Command for MIFARE DESFire, Type 4**           |     |                                                                                                                                                                            |     |     |         |
| 81                                                                                    | 02  | Tag Response (SW1 SW2) See DESFire Data Sheet (MF2DLHX0) Should follow ISO 7816-4 APDU format SW1 and SW2 of R-APDU If card is not able to respond: SW1 = 0x64, SW2 = 0x00 | B   | R   | N/A     |
| 82                                                                                    | var | Tag Data Data of R-APDU Encryption Control If encrypted, see \*\*                                                                                                          |     |     |         |
|                                                                                       |     |                                                                                                                                                                            |     |     |         |

### [Table 6.29](#table-6-29) - Payload for Encrypted NFC/MIFARE\*\* Data If unencrypted see \*\*

### [Table 6.21](#table-6-21)0 – Unencrypted NFC/MIFARE\*\* Data \| B \| O \| N/A \|

\| End of any wrappers, at minimum including Response Message found on page **56** \| \| \| \| \| \|

If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**.

### [Table 6.22](#table-6-22)1 - Request Example (Get Version Part 1)

| Example (Hex)                                                              |
|----------------------------------------------------------------------------|
| AA 00 81 04 01 13 11 02 84 0F 11 02 81 05 90 60 00 00 00 82 01 00 83 01 00 |

### [Table 6.22](#table-6-22)2 - Response Example (Get Version Part 1)

| Example (Hex)                                                                                               |
|-------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 82 13 11 02 82 04 01 00 00 00 84 14 11 02 81 02 91 AF 82 0C FC 0A DF 7A 07 04 08 01 30 00 13 05 |

#### Encrypted Data Format

### [Table 6.22](#table-6-22)3 - Payload for Encrypted NFC/MIFARE Data

| Tag                                              | Len | Value / Description                                                                                                                                                                                                                                                                                     | Typ | Req | Default |
|--------------------------------------------------|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| /DFDF59                                          | var | Encrypted Data Primitive Decrypt the value of this TLV data object using the algorithm and variant specified in the **Encrypted Data KSN** parameter and the **Encrypted Data Encryption Type** parameter to read its contents. The format of the decrypted data is shown in [Table 7.59](#table-7-59). | B   | R   |         |
| /DFDF50                                          | var | Encrypted Data KSN                                                                                                                                                                                                                                                                                      | B   | R   |         |
| /DFDF51                                          | 01  | Encrypted Data Encryption Type See section **4.4 Encryption Type** for a list of valid values.                                                                                                                                                                                                          | B   | R   |         |
| End of Notification Message found on page **62** |     |                                                                                                                                                                                                                                                                                                         |     |     |         |

### [Table 6.22](#table-6-22)4 – Unencrypted NFC/MIFARE Data

| Tag   | Len | Value / Description       | Typ | Req | Default |
|-------|-----|---------------------------|-----|-----|---------|
| FC    | var | NFC/MIFARE Data Container | T   | R   |         |
| /DF7A | var | NFC/MIFARE Data           | B   | O   |         |

### Command 0x1103 – Pass Through Command for MIFARE Plus, Type 2

After a MIFARE Plus EV1/EV2/SE/X Tag is activated, the Host uses this command to send commands and receive responses to and from a MIFARE Plus tag.

For MIFARE Plus SE/X, the Device will not auto detect an error from the MIFARE Tag that has been removed to end the pass-through session. To end the pass-through session, the Host application can send the last command, CANCEL command (0xFF), or receive error response from the MIFARE Tag.

After the card is configured to successfully switch to Security Level 1, the card will be discovered as MIFARE Classic 1K/4K and can use the same functionality as MIFARE Classic 1K/4K commands.

For more details, please refer to NXP NDA documentation ds206234-Product data sheet MIFARE Plus Functionality of implementations on smart card controllers (3.4)

### [Table 6.22](#table-6-22)5 - Command 0x1103 – Pass Through Command for MIFARE Plus, Type 2

| Tag                                                                                  | Len | Value / Description       | Typ | Req | Default |
|--------------------------------------------------------------------------------------|-----|---------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page 55 |     |                           |     |     |         |
| **1103 = Command 0x1103 – Pass Through Command for MIFARE Plus, Type 2**             |     |                           |     |     |         |
| 81                                                                                   | var | Command to Send. See \*\* |     |     |         |
|                                                                                      |     |                           |     |     |         |

### [Table 6.22](#table-6-22)6 - MIFARE Plus EV1/EV2/SE/X SL0 (Security Level 0) Commands\*\* See \*\*

### [Table 6.22](#table-6-22)7 – MIFARE Plus EV1/EV2/SE/X SL3 (Security Level 3) Commands\*\* \| B \| R \| \|

\| 82 \| 01 \| 00 – No Encrypt 01 - Encrypt \| \| \| \| \| 83 \| 01 \| 00 – Expect More Commands 01 – FF (Last Command) If this is the last command, the Device will provide a single beep after receiving a successful response from the tag, otherwise, the device will provide a double beep \| B \| R \| \| \| End of any wrappers, at minimum including Request Message found on page **55** \| \| \| \| \| \|

### [Table 6.22](#table-6-22)6 - MIFARE Plus EV1/EV2/SE/X SL0 (Security Level 0) Commands

| Command      | Length | Field Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | EV1 | EV2 | SE | X |
|--------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|----|---|
| GET_VERSION  | 1      | The GET_VERSION command is used to retrieve manufacturing related data of the MIFARE Plus EV1/EV2 cards Byte 0 = 0x60                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Y   | Y   | N  | N |
| READ_SIG     | 2      | The READ_SIG command returns an IC-specific, 48-byte ECC originality check signature of MIFARE Plus EV1/EV2 cards. Byte 0 = 0x3C Byte 1 = 0x00, RFU                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Y   | Y   | N  | N |
| WRITE_PERSO  | 19     | The WRITE_PERSO command is used to pre-personalize AES keys and data from the initial delivery configuration to a customer specific value. Byte 0 = 0xA8 Byte 1-2 = Number of Block or Key to be written to (MSB first). See NXP doc ds206234, table 113. Byte 3 to 18 = 16 bytes value of the key or data which shall be written (in plain)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Y   | Y   | Y  | Y |
| COMMIT_PERSO | 2      | The COMMIT_PERSO command is used to finalize the personalization and switch up to security level 1 or security level 3. For MIFARE Plus EV1/EV2, the following mandatory AES keys must be written using the WRITE_PERSO command before it can be switched to security level 1 or security level 3. Card Configuration Key Card Master Key Level 2 Switch Key Level 3 Switch Key For MIFARE Plus SE, the following mandatory AES keys must be written using the WRITE_PERSO command before it can be switched to security level 1 (for L1 card) or security level 3 (for L3 card). Card Configuration Key Card Master Key Level 3 Switch Key For MIFARE Plus X, the following mandatory AES keys must be written using the WRITE_PERSO command before it can be switched to security level 1 (for L1 card) or security level 3 (for L3 card). Card Configuration Key Card Master Key Level 2 Switch Key (for L1 card) Level 3 Switch Key (for L1 card) Byte 0 = 0xAA Byte 1 = Security Level Option for EV1 and EV2 cards 0x01 = Security Level 1 0x03 = Security Level 3 Other values = Invalid. Device will return error. Byte 1 = 0x00 for SE and X cards. The Device will return error for other values. It is also highly recommended to change all sector AES keys as well as the data within this security level in a secure environment. This command is behaved as the last command. The Device will provide a single beep after receiving a successful response from a card, otherwise, device will provide a double beep. | Y   | Y   | Y  | Y |
| CANCEL       | 1      | This command is used to terminate the pass-through command session. Byte 0 = 0xFF                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Y   | Y   | Y  | Y |

### [Table 6.22](#table-6-22)7 – MIFARE Plus EV1/EV2/SE/X SL3 (Security Level 3) Commands

| Command                                  | Length   | Field Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | EV1 | EV2 | SE | X |
|------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|----|---|
| **MIFARE Plus Authenticate commands**    |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |     |    |   |
| First Authenticate (part1 and part2)     | 3        | First Authenticate Byte 0 = 0x70 Byte 1-2 = Key Number of the key to be authenticated (MSB first). See NXP doc ds206234, table 113. Byte 3 = MIFARE Plus AES_Key\# 0x01 = AES_Key1 = 16 bytes value stored in **Property 1.2.1.1.4.5 MIFARE Plus AES_Key1.** 0x02 = AES_Key2 = 16 bytes value stored in **Property 1.2.1.1.4.6 MIFARE Plus AES_Key2.** 0x03 = AES_Key3 = 16 bytes value stored in **Property 1.2.1.1.4.7 MIFARE Plus AES_Key3.** 0x04 = AES_Key4 = 16 bytes values stored in **Property 1.2.1.1.4.8 MIFARE Plus AES_Key4.** 0x05 = AES_Key5 = 16 bytes values stored in **Property 1.2.1.1.4.9 MIFARE Plus AES_Key5.** 0x06 = AES_Key6 = 16 bytes values stored in **Property 1.2.1.1.4.A MIFARE Plus AES_Key6.**                                                 | Y   | Y   | Y  | Y |
| Following Authenticate (part1 and part2) | 3        | Following Authenticate Byte 0 = 0x76 Byte 1-2 = Key Number of the key to be authenticated (MSB first). See NXP doc ds206234, table 113. Byte 3 = MIFARE Plus AES_Key\# 0x01 = AES_Key1 = 16 bytes value stored in **Property 1.2.1.1.4.5 MIFARE Plus AES_Key1.** 0x02 = AES_Key2 = 16 bytes value stored in **Property 1.2.1.1.4.6 MIFARE Plus AES_Key2.** 0x03 = AES_Key3 = 16 bytes value stored in **Property 1.2.1.1.4.7 MIFARE Plus AES_Key3.** 0x04 = AES_Key4 = 16 bytes values stored in **Property 1.2.1.1.4.8 MIFARE Plus AES_Key4.** 0x05 = AES_Key5 = 16 bytes values stored in **Property 1.2.1.1.4.9 MIFARE Plus AES_Key5.** 0x06 = AES_Key6 = 16 bytes values stored in **Property 1.2.1.1.4.A MIFARE Plus AES_Key6.**                                             | Y   | Y   | Y  | Y |
| ResetAuth                                | 1        | Reset the authentication Byte 0 = 0x78                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Y   | Y   | Y  | Y |
| **READ commands**                        |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |     |    |   |
| Read                                     | 4        | Reading encrypted, no MAC on response, MAC on command. This command offers the possibility to read the data from one or multiple blocks in an encrypted way. A MAC is only used on the command sent to the PICC, no MAC is attached to the response. Byte 0 = 0x30 Byte 1-2 = Block number of the 1st block to be read (MSB first). See NXP doc ds206234, table 113. Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers do not count if Byte 3 \> 1. Use Byte 3 = 1 for reading Sector Trailer.                                                                                                                                                                                                                                                                  | Y   | Y   | Y  | Y |
| Read MACed                               | 4        | Reading encrypted, MAC on response, MAC on Command. This command offers the possibility to read the data from one or multiple blocks in an encrypted way. A MAC is used on the command sent to the PICC and on the response received. Byte 0 = 0x31 Byte 1-2 = Block number of the 1st block to be read (MSB first). See NXP doc ds206234, table 113. Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers do not count if Byte 3 \> 1. Use Byte 3 = 1 for reading Sector Trailer.                                                                                                                                                                                                                                                                                 | Y   | Y   | Y  | Y |
| Read Plain                               | 4        | Reading in plain, no MAC on response, MAC on command. This command offers the possibility to read the data in plain from one or multiple blocks. A MAC is used on the command and not on the response. Byte 0 = 0x32 Byte 1-2 = Block number of the 1st block to be read (MSB first). See NXP doc ds206234, table 113. Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers do not count if Byte 3 \> 1. Use Byte 3 = 1 for reading Sector Trailer.                                                                                                                                                                                                                                                                                                                | Y   | Y   | Y  | Y |
| Read Plain MACed                         | 4        | Reading in plain, MAC on response, MAC on command. This command offers the possibility to read the data in plain from one or multiple blocks. A MAC is used on the command and the response. Byte 0 = 0x33 Byte 1-2 = Block number of the 1st block to be read (MSB first). See NXP doc ds206234, table 113. Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers do not count if Byte 3 \> 1. Use Byte 3 = 1 for reading Sector Trailer.                                                                                                                                                                                                                                                                                                                          | Y   | Y   | Y  | Y |
| Read UnMACed                             | 4        | Reading encrypted, no MAC on response, no MAC on command This command offers the possibility to read the data from one or multiple blocks in an encrypted way. By default, Read with MAC on command is required. To Read with no MAC on command, needs to modify the card MFP Configuration Block. Byte 0 = 0x34 Byte 1-2 = Block number of the 1st block to be read (MSB first). See NXP doc ds206234, table 113. Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers do not count if Byte 3 \> 1. Use Byte 3 = 1 for reading Sector Trailer.                                                                                                                                                                                                                    | Y   | Y   | Y  | Y |
| Read UnMACed, Response MACed             | 4        | Reading encrypted, MAC on response, no MAC on command This command offers the possibility to read the data from one or multiple blocks in an encrypted way. A MAC is used only on the response received. By default, Read with MAC on command is required. To Read with no MAC on command, needs to modify the card MFP Configuration Block. Byte 0 = 0x35 Byte 1-2 = Block number of the 1st block to be read (MSB first). See NXP doc ds206234, table 113. Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers do not count if Byte 3 \> 1. Use Byte 3 = 1 for reading Sector Trailer.                                                                                                                                                                          | Y   | Y   | Y  | Y |
| Read Plain UnMACed                       | 4        | Reading in plain, no MAC on response, no MAC on command. This command offers the possibility to read the data in plain from one or multiple blocks. AMAC is not used on the response and not on the command. By default, Read with MAC on command is required. To Read with no MAC on command, needs to modify the card MFP Configuration Block. Byte 0 = 0x36 Byte 1-2 = Block number of the 1st block to be read (MSB first). See NXP doc ds206234, table 113. Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers do not count if Byte 3 \> 1. Use Byte 3 = 1 for reading Sector Trailer.                                                                                                                                                                      | Y   | Y   | Y  | Y |
| Read Plain UnMACed, Response MACed       | 4        | Reading in plain, MAC on response, no MAC on command This command offers the possibility to read the data in plain from one or multiple blocks. A MAC is used on the response and not on the command. By default, Read with MAC on command is required. To Read with no MAC on command, needs to modify the card MFP Configuration Block. Byte 0 = 0x37 Byte 1-2 = Block number of the 1st block to be read (MSB first). See NXP doc ds206234, table 113. Byte 3 = 0x01 – 0x0F = Number of blocks to be read. Sector Trailers do not count if Byte 3 \> 1. Use Byte 3 = 1 for reading Sector Trailer.                                                                                                                                                                             | Y   | Y   | Y  | Y |
| **WRITE commands**                       |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Y   | Y   | Y  | Y |
| Write                                    | 20/36/52 | Writing encrypted, no MAC on response, MAC on Command. This command offers the possibility to write the data to up to three blocks in an encrypted way. MAC is only used on the command sent to the PICC. Byte 0 = 0xA0 Byte 1-2 = Block number of the 1st to be written block (MSB first). See NXP doc ds206234, table 113. Byte 3 = 0x01/0x02/0x03 = number of blocks (16 byte) of the data to be written Byte 4 – n = Data to be written, equal to number of blocks \* 16.                                                                                                                                                                                                                                                                                                     | Y   | Y   | Y  | Y |
| Write MACed                              | 20/36/52 | Writing encrypted, MAC on response, MAC on command. This command offers the possibility to write the data to up to three blocks in an encrypted way. A MAC is used on the command sent to the PICC and on the response received from the PICC. Byte 0 = 0xA1 Byte 1-2 = Block number of the 1st to be written block (MSB first). See NXP doc ds206234, table 113. Byte 3 = 0x01/0x02/0x03 = number of blocks (16 byte) of the data to be written Byte 4 – n = Data to be written, equal to number of blocks \* 16.                                                                                                                                                                                                                                                                | Y   | Y   | Y  | Y |
| Write Plain                              | 20/36/52 | Writing in plain, no MAC on response, MAC on command This command offers the possibility to write the data to up to three blocks in plain. A MAC is only used on the command sent to the PICC. Byte 0 = 0xA2 Byte 1-2 = Block number of the 1st to be written block (MSB first). See NXP doc ds206234, table 113. Byte 3 = 0x01/0x02/0x03 = number of blocks (16 byte) of the data to be written Byte 4 – n = Data to be written, equal to number of blocks \* 16.                                                                                                                                                                                                                                                                                                                | Y   | Y   | Y  | Y |
| Write Plain MACed                        | 20/36/52 | Writing in plain, MAC on response, MAC on command. This command offers the possibility to write the data to up to three blocks in plain. A MAC is used on the command sent to the PICC as well as on the response from the PICC Byte 0 = 0xA3 Byte 1-2 = Block number of the 1st to be written block (MSB first). See NXP doc ds206234, table 113. Byte 3 = 0x01/0x02/0x03 = number of blocks (16 byte) of the data to be written Byte 4 – n = Data to be written, equal to number of blocks \* 16.                                                                                                                                                                                                                                                                               | Y   | Y   | Y  | Y |
| **VALUE operations**                     |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |     |    |   |
| Increment                                | 7        | Increment encrypted, no MAC on response, MAC on command This command offers the possibility to increment a value block where the command is secured by a MAC calculated, but not on the response. Byte 0 = 0xB0 Byte 1-2 = Source Block number. Block Number of the block to be incremented (MSB first). See NXP doc ds206234, table 113. Byte 3-6 = The 4 bytes value to be incremented in LSB order. For example, if the value to be incremented by 1, then the value will be 0x01 00 00 00                                                                                                                                                                                                                                                                                     | Y   | Y   | Y  | Y |
| Increment MACed                          | 7        | Increment encrypted, MAC on response, MAC on command. This command offers the possibility to increment a value block where the command is secured by a MAC calculated, but not on the response. Byte 0 = 0xB1 Byte 1-2 = Source Block number. Block Number of the block to be incremented (MSB first). See NXP doc ds206234, table 113. Byte 3-6 = The 4 bytes value to be incremented in LSB order. For example, if the value to be incremented by 1, then the value will be 0x01 00 00 00                                                                                                                                                                                                                                                                                       | Y   | Y   | Y  | Y |
| Decrement                                | 7        | Decrement encrypted, no MAC on response, MAC on command. This command offers the possibility to decrement a value block where the command is secured by a MAC calculated, but not on the response. Byte 0 = 0xB2 Byte 1-2 = Source Block number. Block Number of the block to be decremented (MSB first). See NXP doc ds206234, table 113. Byte 3-6 = The 4 bytes value to be decremented in LSB order. For example, if the value to be decremented by 1, then the value will be 0x01 00 00 00                                                                                                                                                                                                                                                                                    | Y   | Y   | Y  | Y |
| Decrement MACed                          | 7        | Decrement encrypted, MAC on response, MAC on command This command offers the possibility to decrement a value block where the command is secured by a MAC calculated, as well as on the response. Byte 0 = 0xB3 Byte 1-2 = Source Block number. Block Number of the block to be decremented (MSB first). See NXP doc ds206234, table 113. Byte 3-6 = The 4 bytes value to be decremented in LSB order. For example, if the value to be decremented by 1, then the value will be 0x01 00 00 00                                                                                                                                                                                                                                                                                     | Y   | Y   | Y  | Y |
| Transfer                                 | 3        | Transfer, no MAC on response, MAC on command. The Transfer command stores the content of the Transfer Buffer to the specified address. The Transfer command can be applied to any block. The Transfer command can only be executed after an Increment, Decrement, IncrementTransfer, DecrementTransfer or Restore command has been successfully executed since the latest authentication. The command is secured by a MAC on a command. No MAC is calculated on the response. Byte 0 = 0xB4 Byte 1-2 = Destination Block number, whose content is to be replaced by the content of the Transfer Buffer (MSB first). See NXP doc ds206234, table 113.                                                                                                                              | Y   | Y   | Y  | Y |
| Transfer MACed                           | 3        | Transfer, MAC on response, MAC on command. The Transfer command stores the content of the Transfer Buffer to the specified address. The Transfer command can be applied to any block. The Transfer command can only be executed after an Increment, Decrement, IncrementTransfer, DecrementTransfer or Restore command has been successfully executed since the latest authentication. The command is secured by a MAC on a command. A MAC is calculated on the response. Byte 0 = 0xB5 Byte 1-2 = Destination Block number, whose content is to be replaced by the content of the Transfer Buffer (MSB first). See NXP doc ds206234, table 113.                                                                                                                                  | Y   | Y   | Y  | Y |
| Increment Transfer                       | 9        | Increment Transfer encrypted, no MAC on response, MAC on Command. This command offers the possibility to make a combined increment and transfer within one command on a value block where the command is secured by a MAC calculated, no MAC on the response. The command updates the Transfer Buffer in the same way as if a separate Increment and Transfer commands were given Byte 0 = 0xB6 Byte 1-2 = Source Block number. Block Number of the block to be incremented. Byte 3-4 = Destination Block number, whose content is to be replaced by the content of the Transfer Buffer. Byte 5-8 = The 4 bytes value to be incremented in LSB order. For example, if the value to be incremented by 1, then the value will be 0x01 00 00 00                                      | Y   | Y   | Y  | Y |
| Increment Transfer MACed                 | 9        | Increment Transfer encrypted, MAC on response, MAC on command. This command offers the possibility to make a combined increment and transfer within one command on a value block where the command is secured by a MAC calculated, and as well as a MAC on the response. The command updates the Transfer Buffer in the same way as if a separate Increment and Transfer commands were given. Byte 0 = 0xB7 Byte 1-2 = Source Block number. Block Number of the block to be incremented (MSB first). Byte 3-4 = Destination Block number, whose content is to be replaced by the content of the Transfer Buffer (MSB first). Byte 5-8 = The 4 bytes value to be incremented in LSB order. For example, if the value to be incremented by 1, then the value will be 0x01 00 00 00. | Y   | Y   | Y  | Y |
| Decrement Transfer                       | 9        | Decrement Transfer encrypted, no MAC on response, MAC on command This command offers the possibility to make a combined decrement and transfer within one command on a value block where the command is secured by a MAC, but no MAC on the response. The command updates the Transfer Buffer in the same way as if a separate Decrement and Transfer commands were given. Byte 0 = 0xB8 Byte 1-2 = Source Block number. Block Number of the block to be decremented (MSB first). Byte 3-4 = Destination Block number, whose content is to be replaced by the content of the Transfer Buffer (MSB first). Byte 5-8 = The 4 bytes value to be incremented in LSB order. For example, if the value to be decremented by 1, then the value will be 0x01 00 00 00.                    | Y   | Y   | Y  | Y |
| Decrement Transfer MACed                 | 9        | Decrement Transfer encrypted, MAC on response, MAC on Command This command offers the possibility to make a combined decrement and transfer within one command on a value block where both the command and the response are secured by a MAC. The command updates the Transfer Buffer in the same way as if a separate Decrement and Transfer commands were given. Byte 0 = 0xB9 Byte 1-2 = Source Block number. Block Number of the block to be decremented (MSB first). Byte 3-4 = Destination Block number, whose content is to be replaced by the content of the Transfer Buffer (MSB first). Byte 5-8 = The 4 bytes value to be incremented in LSB order. For example, if the value to be decremented by 1, then the value will be 0x01 00 00 00.                            | Y   | Y   | Y  | Y |
| Restore                                  | 3        | Restore encrypted, no MAC on response, MAC on command The Restore command copies the Content found in the Value Block at the given address to the Transfer Buffer. The Restore command can only be applied to value blocks. The command is secured by a MAC on a command, no MAC is calculated on the response. Byte 0 = 0xC2 Byte 1-2 = Source Block number. Block Number of the block which content is to be copied to the Transfer Buffer.                                                                                                                                                                                                                                                                                                                                     | Y   | Y   | Y  | Y |
| Restore MACed                            | 3        | Restore encrypted, MAC on response, MAC on command. The Restore command copies the Content found in the Value Block at the given address to the Transfer Buffer. The Restore command can only be performed to value blocks. The command is secured by a MAC on a command and a MAC is calculated on the response. Byte 0 = 0xC3 Byte 1-2 = Source Block number. Block Number of the block which content is to be copied to the Transfer Buffer.                                                                                                                                                                                                                                                                                                                                   | Y   | Y   | Y  | Y |
| **Others**                               |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |     |    |   |
| GET_VERSION                              | 1        | The GET_VERSION command is used to retrieve manufacturing related data of the MIFARE Plus EV1/EV2 cards Byte 0 = 0x60                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Y   | Y   | N  | N |
| READ_SIG                                 | 2        | The READ_SIG command returns an IC-specific, 48-byte ECC originality check signature of MIFARE Plus EV1/EV2 cards. Byte 0 = 0x3C Byte 1 = 0x00, RFU                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Y   | Y   | N  | N |
| CANCEL                                   | 1        | This command is used to terminate the pass-through command session. Byte 0 = 0xFF                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Y   | Y   | Y  | Y |

### [Table 6.22](#table-6-22)8 - Response Data for Command 0x1103 – Pass Through Command for MIFARE Plus, Type 2

| Tag                                                                                   | Len | Value / Description                            | Typ | Req | Default |
|---------------------------------------------------------------------------------------|-----|------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including Response Message found on page **56** |     |                                                |     |     |         |
| 1103 = **Command 0x1103 – Pass Through Command for MIFARE Plus, Type 2**              |     |                                                |     |     |         |
| 81                                                                                    | 01  | Tag Response Code 0x00 = Success 0x01 = Failed | B   | R   | N/A     |
| 82                                                                                    | Var | Encryption Control If encrypted, see \*\*      |     |     |         |
|                                                                                       |     |                                                |     |     |         |

### [Table 6.29](#table-6-29) - Payload for Encrypted NFC/MIFARE\*\* Data If unencrypted see \*\*

### [Table 6.21](#table-6-21)0 – Unencrypted NFC/MIFARE\*\* Data \| B \| O \| N/A \|

\| End of any wrappers, at minimum including Response Message found on page **56** \| \| \| \| \| \|

If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**.

### [Table 6.22](#table-6-22)9 - Request Example (Get Version)

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA 00 81 04 01 DA 11 03 84 0B 11 03 81 01 60 82 01 00 83 01 00 |

### [Table 6.23](#table-6-23)0 - Response Example (Get Version)

| Example (Hex)                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 82 DA 11 03 82 04 01 00 00 00 84 28 11 03 81 01 00 82 21 FC 1F DF 7A 1C 04 02 01 11 00 16 04 04 02 01 01 01 16 04 04 4D 59 5A 3E 18 90 CF 8D 15 61 51 21 23 |

#### Encrypted Data Format

### [Table 6.23](#table-6-23)1 - Payload for Encrypted NFC/MIFARE Data

| Tag                                              | Len | Value / Description                                                                                                                                                                                                                                                                                     | Typ | Req | Default |
|--------------------------------------------------|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| /DFDF59                                          | var | Encrypted Data Primitive Decrypt the value of this TLV data object using the algorithm and variant specified in the **Encrypted Data KSN** parameter and the **Encrypted Data Encryption Type** parameter to read its contents. The format of the decrypted data is shown in [Table 7.59](#table-7-59). | B   | R   |         |
| /DFDF50                                          | var | Encrypted Data KSN                                                                                                                                                                                                                                                                                      | B   | R   |         |
| /DFDF51                                          | 01  | Encrypted Data Encryption Type See section **4.4 Encryption Type** for a list of valid values.                                                                                                                                                                                                          | B   | R   |         |
| End of Notification Message found on page **62** |     |                                                                                                                                                                                                                                                                                                         |     |     |         |

### [Table 6.23](#table-6-23)2 – Unencrypted NFC/MIFARE Data

| Tag   | Len | Value / Description       | Typ | Req | Default |
|-------|-----|---------------------------|-----|-----|---------|
| FC    | var | NFC/MIFARE Data Container | T   | R   |         |
| /DF7A | var | NFC/MIFARE Data           | B   | O   |         |

## Command Group 0x18nn - User Interface

### Command 0x1801 - Request Cardholder Signature (Touch Only)

The host uses this command to prompt a cardholder for a signature.

The sequence of events is as follows:

1.  The device completes a transaction after the host invokes **Command 0x1001 - Start Transaction**. At the end of the transaction, the device has provided data to the host in **Notification 0x0105 - Transaction Operation Complete**.
2.  The host decides whether to request a signature from the cardholder. For example:
    1.  If the Notification Detail in **Notification 0x0105 - Transaction Operation Complete** indicates Signature Capture Requested.
    2.  If an application-specific rule requires requesting a signature.
3.  If the host determines it should request a signature, it composes a command request in the format below.
4.  The device presents a signature capture interface to the cardholder on the display.
5.  The device sends **Notification 0x1805 - User Interface Operation Complete** to the host to report data available, timeout, or hardware failure.
6.  If the device reported data available, the host uses **Command 0xD821 - Start Get File from Device** to request file type **Signature Capture File** to retrieve the data as a **Signature Capture File Type**.

### [Table 6.31](#table-6-31) - Request Data for Command 0x1801 - Request Cardholder Signature (Touch Only)

| Tag                                                                                      | Len | Value / Description                                                                                       | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|-----------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                           |     |     |         |
| 1801 = **Command 0x1801 - Request Cardholder Signature (Touch Only)**                    |     |                                                                                                           |     |     |         |
| 81                                                                                       | 01  | Timeout Timeout in seconds that the device should wait for the cardholder to sign and confirm completion. | B   | R   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                           |     |     |         |

### [Table 6.32](#table-6-32) - Response Data for Command 0x1801 - Request Cardholder Signature (Touch Only)

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1801 = **Command 0x1801 - Request Cardholder Signature (Touch Only)**                     |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**.

### [Table 6.33](#table-6-33) - Request Example

| Example (Hex)                                |
|----------------------------------------------|
| AA 00 81 04 01 00 18 01 84 05 18 01 81 01 1E |

### [Table 6.34](#table-6-34) - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 00 18 01 82 04 01 00 00 00 |

### Command 0x1802 - Report Cardholder Selection

The host uses this command to provide a cardholder selection to the device when the device itself does not have a display or inputs to prompt the cardholder for a selection.

The sequence of events is as follows:

1.  The host has already invoked **Command 0x1001 - Start Transaction** and the transaction is still in process.
2.  During the transaction, if the device does not have a display or touchscreen but needs to show information to the cardholder or needs the cardholder to make a selection, it sends the host **Notification 0x1803 - User Interface Host Action Request** to report Display / Cardholder Selection and supporting information.
3.  The host uses its user interface to request a selection from the cardholder based on the information and selectable items provided by the notification message.
4.  The host sends the user selection to the device by sending the command in the format below.

### [Table 6.35](#table-6-35) - Request Data for Command 0x1802 - Report Cardholder Selection

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                                                                                                     | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                                                                                                         |     |     |         |
| 1802 = **Command 0x1802 - Report Cardholder Selection**                                  |     |                                                                                                                                                                                                                                                                         |     |     |         |
| 81                                                                                       | 01  | Cardholder Selection Request Status 0x00 = Cardholder Selection Request completed, see Selection Result parameter. 0x01 = Cardholder Selection Request canceled by cardholder, Transaction Aborted. 0x02 = Cardholder Selection Request timed out, Transaction Aborted. | B   | R   |         |
| 82                                                                                       | 01  | Selection Result Menu item index the cardholder selected. If the cardholder made no selection or the operation terminated abnormally, the device does not include this parameter.                                                                                       | B   | O   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                                                                                                                                                                         |     |     |         |

### [Table 6.36](#table-6-36) - Response Data for Command 0x1802 - Report Cardholder Selection

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1802 = **Command 0x1802 - Report Cardholder Selection**                                   |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**.

### [Table 6.37](#table-6-37) - Request Example

| Example (Hex)                                         |
|-------------------------------------------------------|
| AA 00 81 04 01 00 18 02 84 08 18 02 81 01 00 82 01 00 |

### [Table 6.38](#table-6-38) - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 00 18 02 82 04 01 00 00 00 |

### Command 0x1803 - Display Message (Display Only)

The host uses this command to request that the device display a message for the cardholder.

The sequence of events is as follows:

1.  The host ensures the device is not currently running another command, for example, that it is not running a transaction using **Command 0x1001 - Start Transaction**.
2.  The host selects the message it wants to display from the list of available pre-determined strings.
3.  The host composes a command request in the format below, and sends it to the device.
4.  The device displays the requested message.
    1.  If the Timeout parameter is set to Infinite, the device returns a command response message with Response Status, Operation Status Summary byte set to 0x00 (OK, Done) after which the host is free to send further commands.
    2.  If the timeout parameter is not set to Infinite:
        1.  The device returns a command response message with its Response Status, Operation Status Summary byte set to 0x01 (OK, Started / Running).
        2.  While the host is waiting for the timeout to expire, it should not send any commands to the device, because the device is busy processing the current command.
        3.  After the timeout period expires, the device blanks the display and sends **Notification 0x1805 - User Interface Operation Complete** to inform the host.

### [Table 6.39](#table-6-39) - Request Data for Command 0x1803 - Display Message (Display Only)

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                         | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                             |     |     |         |
| 1803 = **Command 0x1803 - Display Message (Display Only)**                               |     |                                                                                                                                                                                             |     |     |         |
| 81                                                                                       | 01  | Timeout 0x00 = Infinite. Device leaves the requested message on the display until the host initiates a change. All other values = Timeout in seconds for the device to display the message. | B   | O   | 0x00    |
| 82                                                                                       | 01  | Message ID Specify a Display String ID from section **4.3 Display Strings**.                                                                                                                | B   | O   | 0x14    |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                                                                                             |     |     |         |

### [Table 6.31](#table-6-31)0 - Response Data for Command 0x1803 - Display Message (Display Only)

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1803 = **Command 0x1803 - Display Message (Display Only)**                                |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.31](#table-6-31)1 - Request Example

| Example (Hex)                             |
|-------------------------------------------|
| AA00 810401551803 8408 1803 810102 820116 |

### [Table 6.31](#table-6-31)2 - Response Example

| Example (Hex)                           |
|-----------------------------------------|
| AA00 810482551803 820401000000 84021803 |

### Command 0x1804 - Read Barcode (BCR Only)

The host uses this command to direct the device to arm or disarm the barcode reader for reading a barcode outside the scope of a transaction. This is an immediate directive. To read barcodes within the scope of a transaction, use **Command 0x1001 - Start Transaction** and its barcode reader parameters instead.

The sequence of events is as follows:

1.  The host ensures the device is not currently running another command, for example, that it is not running a transaction using **Command 0x1001 - Start Transaction**.
2.  The host composes a command request in the format below and sends it to the device.
3.  If the device has a display, it shows a prompt **SCAN BARCODE**.
4.  The device enables the barcode reader.
    1.  If the **Timeout** parameter is set to **Infinite**:
        1.  The device returns a command response message with Response Status, Operation Status Summary byte set to 0x00 (OK, Done) after which the host is free to send further commands.
        2.  The host may end the barcode reading session by calling this command again with the **Enable** parameter set to **Disable**.
    2.  If the **Timeout** parameter is set to a value other than **Infinite**:
        1.  The device returns a command response message with its Response Status, Operation Status Summary byte set to 0x01 (OK, Started / Running).
        2.  While the host is waiting for the timeout to expire, it should not send any commands to the device, because the device is busy processing the current command.
        3.  After the device reads a barcode or the timeout period expires, the device sends **Notification 0x1805 - User Interface Operation Complete** to report Barcode Reader / Read Barcode Result and additional supporting information.

### [Table 6.31](#table-6-31)3 - Request Data for Command 0x1804 - Read Barcode (BCR Only)

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                  | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |     |     |         |
| 1804 = **Command 0x1804 - Read Barcode (BCR Only)**                                      |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |     |     |         |
| 81                                                                                       | 01  | Enable 0x00 = Disable. The device disables the barcode reader. In this case, the device ignores all other parameters. 0x01 = Enable. The device enables the barcode reader.                                                                                                                                                                                                                                                                          | B   | R   | 0x00    |
| 82                                                                                       | 01  | Timeout 0x00 = Infinite. The device leaves the barcode reader enabled until it reads a barcode, or until the host sends this command again to disable the barcode reader. All other values = Timeout in seconds for the device to leave the barcode reader enabled without reading a barcode.                                                                                                                                                        | B   | O   | 0x00    |
| 83                                                                                       | 01  | Encrypt Barcode Data 0x00 = Do Not Encrypt. The device does not encrypt the barcode data when it sends **Notification 0x1805 - User Interface Operation Complete**. 0x01 = Encrypt. The device encrypts the barcode data when it sends **Notification 0x1805 - User Interface Operation Complete**.                                                                                                                                                  | B   | O   | 0x00    |
| 99                                                                                       | var | (MAGTEK INTERNAL ONLY) Send Command to Barcode Reader The device sends the command to the barcode reader. The host can use these commands to change the reader’s internal configuration. See **UM10089_NLS-N1_User_Guide** for command details. If tag 0x99 is included in the command, the device ignores all other tags. **Do not change communication settings with this feature. Changes may result is loss of communications with the reader.** | B   | O   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |     |     |         |

### [Table 6.31](#table-6-31)4 - Response Data for Command 0x1804 - Read Barcode (BCR Only)

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1804 = **Command 0x1804 - Read Barcode (BCR Only)**                                       |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.31](#table-6-31)5 - Request Example

| Example (Hex)                                    |
|--------------------------------------------------|
| AA00 810401031804 840B 1804 810101 82010F 830101 |

### [Table 6.31](#table-6-31)6 - Response Example

| Example (Hex)                  |
|--------------------------------|
| AA00 810482031804 820401000000 |

### Command 0x1805 - Buzzer

The host uses this command to start a buzzer for playing a sequence of tones. Each sequence can have a minimum of 1 to maximum of 10 tones.

The sequence of events is as follows:

1.  The host ensures the device is not currently running another command, for example, that it is not running a transaction using **Command 0x1001 - Start Transaction**.
2.  The host composes a command request in the format below and sends it to the device.
3.  The device plays a specific tone sequence as the command specified. After finish, the device sends **Notification 0x1805 - User Interface Operation Complete** to report Buzzer/Buzzer Result.

    The host should wait for **Notification 0x1805 - User Interface Operation Complete** before sending another command.

    If the buzzer is current playing a sequence of tones and any transaction that uses the buzzer to make a sound is started, the device will stop the buzzer for that transaction to take over.

### [Table 6.31](#table-6-31)7 - Request Data for Command 0x1805 - Buzzer

| Tag                                                                                      | Len  | Value / Description                                                                                                                                                                                                                                                                                                                                                                    | Typ | Req | Default |
|------------------------------------------------------------------------------------------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |      |                                                                                                                                                                                                                                                                                                                                                                                        |     |     |         |
| 1805 = **Command 0x1805 - Buzzer**                                                       |      |                                                                                                                                                                                                                                                                                                                                                                                        |     |     |         |
| 81                                                                                       | N\*4 | N = Number of tones 0x01 – Min (1 tone) 0x0A – Max (10 tones) 4 = 4 bytes data parameter for each tone in the sequence Byte0-Byte1 – Frequency in units of 1 Hz 0x0000..0x0031 (\< 50 Hz, Silent) 0x0032 - Min (50 Hz) 0x0FA0 - Max (4000 Hz) 0x0FA1..0xFFFF (\> 4000 Hz, Error) Byte 2-Byte3 – Duration of tone in units of 1 millisecond 0x0001 – Min (1 ms) 0xFFFF – Max (65535 ms) | B   | R   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |      |                                                                                                                                                                                                                                                                                                                                                                                        |     |     |         |

### [Table 6.31](#table-6-31)8 - Response Data for Command 0x1805 - Buzzer

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1805 = **Command 0x1805 - Buzzer**                                                        |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.31](#table-6-31)9 - Request Example for a sequence of 5 tones

| Example (Hex)                                                                      |
|------------------------------------------------------------------------------------|
| AA00 810401031805 8418 1805 8114 00C8 01F4 0190 01F4 0258 01F4 0190 01F4 00C8 01F4 |

### [Table 6.32](#table-6-32)0 - Response Example

| Example (Hex)                  |
|--------------------------------|
| AA00 810482031805 820401000000 |

### Command 0x1821 - Show Image (Display Only)

The host uses this command to trigger the device to immediately show a pre-loaded image on the display, provided the device is not in a mode that has exclusive use of the display (such as during a transaction). This is an immediate and temporary directive. For a solution that affects the device’s idle page behavior on a more permanent basis, see **Property 1.2.3.1.1.1 Custom Idle Page Image**. This command is different from **Command 0x1823 - Show Bitmap Image** in that the bitmaps are pre-loaded and persistently stored in the device and can not be composited with each other.

The sequence of events is as follows:

1.  The host makes sure it has loaded the image into at least one of the device’s Custom Idle Page Image slots using **Command 0xD812 - Start Send File to Device (Unsecured)**.
2.  The host makes sure the device is in Active/Idle state (meaning the display is fully powered on and is not in a mode that has exclusive use of the display, such as processing a transaction).
3.  The host calls this command to show the image loaded into the desired slot number.
4.  The device shows the specified image on the display until the device is no longer in Active/Idle.

### [Table 6.32](#table-6-32)1 - Request Data for Command 0x1821 - Show Image (Display Only)

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |     |     |         |
| 1821 = **Command 0x1821 - Show Image (Display Only)**                                    |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |     |     |         |
| 81                                                                                       | 01  | Custom Idle Page Image Number 0x01 = Show custom image 1 0x02 = Show custom image 2 0x03 = Show custom image 3 0x04 = Show custom image 4                                                                                                                                                                                                                                                                                                                                                                   | B   | R   |         |
| 82                                                                                       | 01  | Display Option 0x00 = Default to cover/uncover the top status bar depends on the current status of the display. If the current display shows the top status bar, the Show Image command won’t cover the top status bar. If the current display doesn’t show the top status bar, the Show Image command will cover the top status bar. 0x01 = Cover the top status bar regardless of the current status of the display. 0x02 = Not cover the top status bar regardless of the current status of the display. | B   | O   | 0       |
| 83                                                                                       | 01  | Display Time 0x00 = Show image until device changes state                                                                                                                                                                                                                                                                                                                                                                                                                                                   | B   | O   | 0       |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |     |     |         |

### [Table 6.32](#table-6-32)2 - Response Data for Command 0x1821 - Show Image (Display Only)

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1821 = **Command 0x1821 - Show Image (Display Only)**                                     |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

If the request started successfully, the Request Status in the message wrapper is **All Good, Requested Operation Was Successful**.

### [Table 6.32](#table-6-32)3 - Request Example

| Example (Hex)                                         |
|-------------------------------------------------------|
| AA 00 81 04 01 2C 18 21 84 08 18 21 81 01 03 83 01 00 |

### [Table 6.32](#table-6-32)4 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 2C 18 21 82 04 00 00 00 00 |

### Command 0x1822 - Show QR Code (Display Only)

The host uses this command to direct the device to immediately show a QR code on the display, provided the device is not in a mode that has exclusive use of the display (such as during a transaction).

The sequence of events is as follows:

1.  The host ensures the device is not currently running another command, for example, that it is not running a transaction using **Command 0x1001 - Start Transaction**.
2.  The host selects the data for the QR code it wants to display.
3.  The host composes a command request in the format below and sends it to the device.
4.  The device generates and displays the QR code.
    1.  If the **Display Time** parameter is set to **Indefinite**, the device returns a command response message with Response Status, Operation Status Summary byte set to 0x00 (OK, Done) after which the host is free to send further commands.
    2.  If the **Display Time** parameter is set to a number of seconds:
        1.  The device returns a command response message with its Response Status, Operation Status Summary byte set to 0x01 (OK, Started / Running).
        2.  While the host is waiting for the timeout to expire, it should not send any commands to the device, because the device is busy processing the current command.
        3.  After the timeout period expires, the device unlocks to allow other commands and sends **Notification 0x1805 - User Interface Operation Complete** to report **Display** / **Display Message** / **Timed Out** / **Reserved**.

### [Table 6.32](#table-6-32)5 - Request Data for Command 0x1822 - Show QR Code (Display Only)

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                 | Typ | Req | Default          |
|------------------------------------------------------------------------------------------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|------------------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |     |     |                  |
| 1822 = Command 0x1822 - Show QR Code (Display Only)                                      |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |     |     |                  |
| 81                                                                                       | 01  | Display Time 0x00 = Indefinite 0x01 to 0xFF = 1 to 255 seconds                                                                                                                                                                                                                                                                                                                                                                                      | B   | O   | 0x00             |
| 82                                                                                       | var | Data to Encode See **ISO/IEC 18004:2015**                                                                                                                                                                                                                                                                                                                                                                                                           | B   | R   |                  |
| 83                                                                                       | 01  | Error Correction 0x00 = Low 0x01 = Medium 0x02 = Quartile 0x03 = High See **ISO/IEC 18004:2015**                                                                                                                                                                                                                                                                                                                                                    | B   | O   | 0x00             |
| 84                                                                                       | 01  | Mask Pattern 0x00 to 0x07 = Mask Pattern 0xFF = Device Select Optimal Mask Pattern See **ISO/IEC 18004:2015**                                                                                                                                                                                                                                                                                                                                       | B   | O   | 0xFF             |
| 85                                                                                       | 01  | Minimum Version Must be less than or equal to Maximum Version 0x01 to 0x28 = Version 1 to Version 40 See **ISO/IEC 18004:2015**                                                                                                                                                                                                                                                                                                                     | B   | O   | 0x01             |
| 86                                                                                       | 01  | Maximum Version Must be greater than or equal to Minimum Version 0x01 to 0x28 = Version 1 to Version 40 See **ISO/IEC 18004:2015**                                                                                                                                                                                                                                                                                                                  | B   | O   | 0x28             |
| 87                                                                                       | 03  | Block Color Use RRGGBB format.                                                                                                                                                                                                                                                                                                                                                                                                                      | B   | O   | 0x000000 (Black) |
| 88                                                                                       | 03  | Background Color Use RRGGBB format.                                                                                                                                                                                                                                                                                                                                                                                                                 | B   | O   | 0xFFFFFF (White) |
| 89                                                                                       | var | Prompt Text for the device to display below the QR code. Because the device shows the Prompt using a proportional font, the maximum length that fits the display depends on the text and the device’s orientation set by Property 1.2.3.1.1.2 Custom Idle Page Image Device Locked (Display Only)**.** In Landscape orientation, the upper limit is approximately 30 characters. In Portrait orientation, the limit is approximately 22 characters. | B   | O   | No prompt        |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |     |     |                  |

### [Table 6.32](#table-6-32)6 - Response Data for Command 0x1822 - Show QR Code (Display Only)

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1822 = **Command 0x1822 - Show QR Code (Display Only)**                                   |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

If the request started successfully, the Request Status in the message wrapper is **All Good, Requested Operation Was Successful**.

### [Table 6.32](#table-6-32)7 - Request Example

| Example (Hex)                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 05 18 22 84 41 18 22 81 01 3C 82 0F 54 68 69 73 20 69 73 20 61 20 74 65 73 74 21 83 01 00 84 01 FF 85 01 01 86 01 28 87 03 00 00 00 88 03 FF FF FF 89 13 50 6c 65 61 73 65 20 73 63 61 6e 20 51 52 20 63 6f 64 65 |

Table 629 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 2C 18 22 82 04 00 00 00 00 |

Table 630 - Notification Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 83 00 18 05 82 04 02 01 00 00 |

### Command 0x1823 - Show Bitmap Image (Display Only)

The host uses this command to trigger the device to immediately show a bitmap file the host includes as a parameter, provided the device is not in a mode that has exclusive use of the display (such as during a transaction).

This is an immediate and temporary directive. For a solution that affects the device’s idle page behavior on a more permanent basis, see **Property 1.2.3.1.1.1 Custom Idle Page Image**. This command is different from **Command 0x1821 - Show Image (Display Only)** in that the host sends bitmaps as parameters instead of pre-loading them, and the host can call this command multiple times without clearing the display to show multiple bitmaps on the display at the same time.

The sequence of events is as follows:

1.  The host ensures the device is not currently running another command, for example, that it is not running a transaction using **Command 0x1001 - Start Transaction**.
2.  The host selects a bitmap file it wants to display.
3.  The host composes a command request in the format below and sends it to the device.
4.  If the host includes the **Background Color** parameter, the device clears the display using the specified color. If the host does not include that parameter, the device does not clear the display.
5.  The device shows the bitmap with the upper left corner at the specified **X Position** and **Y Position**. If the host omits either parameter, the device centers the bitmap along the unspecified axis.
    1.  If the **Display Time** parameter is **Indefinite** or is not included, the device returns a command response message with Response Status, Operation Status Summary byte set to 0x00 (OK, Done) after which the host is free to send further commands.
    2.  If the timeout parameter is set to a specific number of seconds:
        1.  The device returns a command response message with its Response Status, Operation Status Summary byte set to 0x01 (OK, Started / Running).
        2.  While the host is waiting for the timeout to expire, it should not send any commands to the device, because the device is busy processing the current command.
        3.  After the timeout period expires, the device unlocks to allow other commands and sends **Notification 0x1805 - User Interface Operation Complete** to inform the host.

### [Table 6.32](#table-6-32)8 - Request Data for Command 0x1823 - Show Bitmap Image (Display Only)

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Typ | Req | Default  |
|------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|----------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |     |     |          |
| 1823 = **Command 0x1823 - Show Bitmap Image (Display Only)**                             |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |     |     |          |
| 81                                                                                       | 01  | Display Time 0x00 = Indefinite 0x01 to 0xFF = 1 to 255 seconds                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | B   | O   | 0x00     |
| 82                                                                                       | 03  | Background Color Use RRGGBB format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | B   | O   | N/A      |
| 83                                                                                       | 02  | X Position The device places the left edge of the image at this pixel position relative to the left edge of the display, which is position 0x0000. This parameter plus the pixel width of the image must be less than the pixel width of the display. The display’s pixel width depends on the device’s orientation set by Property 1.2.3.1.1.2 Custom Idle Page Image Device Locked (Display Only)For information about the resolution of the display, see the specifications in the device’s **Installation and Operation Manual**.    | B   | O   | Centered |
| 84                                                                                       | 02  | Y Position The device places the top edge of the image at this pixel position relative to the top edge of the display, which is position 0x0000. This parameter plus the pixel height of the image must be less than the pixel height of the display. The display’s pixel height depends on the device’s orientation set by Property 1.2.3.1.1.2 Custom Idle Page Image Device Locked (Display Only). For information about the resolution of the display, see the specifications in the device’s **Installation and Operation Manual**. | B   | O   | Centered |
| 85                                                                                       | var | Bitmap Image encoded in full BMP file format as defined by Microsoft (e.g., starting with “BM”)                                                                                                                                                                                                                                                                                                                                                                                                                                          | B   | R   |          |
| 86                                                                                       | 01  | Display Option 0x00 = Default to cover/uncover the top status bar depends on the current status of the display. If the current display shows the top status bar, the Show Bitmap Image command won’t cover the top status bar. If the current display doesn’t show the top status bar, the Show Bitmap Image command will cover the top status bar. 0x01 = Cover the top status bar regardless of the current status of the display. 0x02 = Not cover the top status bar regardless of the current status of the display.                | B   | O   | 0        |
| End of any wrappers, at minimum including Request Message found on page 55               |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |     |     |          |

### [Table 6.32](#table-6-32)9 - Response Data for Command 0x1823 - Show Bitmap Image (Display Only)

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1823 = **Command 0x1823 - Show Bitmap Image (Display Only)**                              |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

If the request started successfully, the Request Status in the message wrapper is **All Good, Requested Operation Was Successful**.

### [Table 6.33](#table-6-33)0 - Request Example

| Example (Hex)                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 05 18 22 84 41 18 22 81 01 3C 82 0F 54 68 69 73 20 69 73 20 61 20 74 65 73 74 21 83 01 00 84 01 FF 85 01 01 86 01 28 87 03 00 00 00 88 03 FF FF FF 89 13 50 6c 65 61 73 65 20 73 63 61 6e 20 51 52 20 63 6f 64 65 |

Table 629 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 2C 18 22 82 04 00 00 00 00 |

Table 630 - Notification Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 83 00 18 05 82 04 02 01 00 00 |

### Command 0x1830 - Display Flexible UI Pages (Display Only)

**DF II PED Operation Flow Proposal with Flexible UI Framework**

![A diagram of a device Description automatically generated](media/def4ebbb357938168ddd5610cc932dfe.png)

![A screenshot of a document Description automatically generated](media/93f7fda714e67ad29e1850c4f39ceab0.png)

![A screenshot of a diagram Description automatically generated](media/80ef48eaffdb76c130b599420e7a3acf.png)

![A screenshot of a computer program Description automatically generated](media/bb36b51150ceace522be858f2e05cd2d.png)

The host uses this command to display Flexible UI pages in the following layout:

#### UI Page Option 0x00 Layout

The host uses this option to display a maximum of 5 lines of host provided text, and 1 optional green functional button, Middle – label with a String ID that associates it with a configured String message. See

\*\*

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings\*\*. When the user presses this button, the device sends a notification to the host to indicate this button is pressed. See **Notification 0x1803 - User Interface Host Action Request.** After that, the host will decide what to do next.

Recommend maximum number of characters setting for this page:

-   Landscape Screen Orientation:

    Each text line can fit about 18 Upper case wide size characters like “WM”, 23 Upper case regular size characters such as “ABC”, 21 lower case wide size characters like “wm”, or 30 lower case regular size characters like “abc”.

    Button text can fit about 5 Upper case wide size characters like “WM”, 8 Upper case regular size characters like “ABC”, 6 lower case wide size characters like “wm”, or 9 lower case regular size characters like “abc”.

-   Portrait Screen Orientation:

    Each text line can fit about 13 Upper case wide size characters like “WM”, 17 Upper case regular size characters like “ABC”, 14 lower case wide size characters like “wm”, or 20 lower case regular size characters like abc.

    Button text can fit about 4 Upper case wide size characters like “WM”, 6 Upper case regular size characters like “ABC”, 5 lower case wide size characters like “wm”, or 7 lower case regular size characters like “abc”.

![A screenshot of a computer program Description automatically generated](media/a0f1f5dde7ac6b27978afd2364cdfc5b.png)![A screenshot of a computer Description automatically generated](media/103ffd0e8a8a2f705c3c507b899406a0.png)

#### UI Page Option 0x01 and 0x02 Layout

The host uses UI Page Option **0x01** to display a page with a title, a maximum of 6 data buttons (2 rows and 3 columns in Landscape Screen Orientation, 3 rows and 2 columns in Portrait Screen Orientation) with text, and maximum 3 functional buttons with a color option of red, green, or yellow.

The host uses UI Page Option **0x01** to display a page with a title, maximum of 4 data buttons (2 rows and 2 columns in Landscape Screen Orientation, 2 rows and 2 columns in Portrait Screen Orientation) with text, and maximum 3 functional buttons with a color option of red, green, or yellow.

The host uses UI Page Option **0x02** to display a page with a title, maximum of 6 data buttons (2 rows and 3 columns in Landscape Screen Orientation, 3 rows and 2 columns in Portrait Screen Orientation) with \$Amount, and maximum 3 functional buttons with a color option of red, green, or yellow.

The host uses UI Page Option **0x02** to display a page with a title, maximum of 4 data buttons (2 rows and 2 columns in Landscape Screen Orientation, 2 rows and 2 columns in Portrait Screen Orientation) with \$Amount, and maximum 3 functional buttons with a color option of red, green, or yellow.

The button with **\$** Amount value is host provided. The title, data buttons text, and functional buttons are labeled with String IDs associated with configured String messages. See

\*\*

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings\*\*. When the user presses any button, the device sends a notification to the host to indicate the corresponding button is pressed. See **Notification 0x1803 - User Interface Host Action Request.** After that, the host will decide what to do next.

Recommend maximum number of character settings for this page:

-   Landscape Screen Orientation:
    -   The title text can fit about 18 Upper case wide size characters like “WM”, 23 Upper case regular size characters like “ABC”, 21 lower case wide size characters like “wm”, or 30 lower case regular size characters like “abc”.
    -   The 3 columns data button’s text can fit about 5 Upper case wide size characters like “WM”, 8 Upper case regular size characters like “ABC”, 6 lower case wide size characters like “wm”, or 9 lower case regular size characters like “abc”.
    -   The 2 columns data button’s text can fit about 9 Upper case wide size characters like “WM”, 13 Upper case regular size characters like “ABC”, 9 lower case wide size characters like “wm”, or 15 lower case regular size characters like “abc”.
    -   The Functional button’s text can fit about 5 Upper case wide size characters like “WM”, 8 Upper case regular size characters like “ABC”, 6 lower case wide size characters like “wm”, or 9 lower case regular size characters like “abc”.
-   Portrait Screen Orientation:
    -   The title text can fit about 13 Upper case wide size characters like “WM”, 17 Upper case regular size characters like “ABC”, 14 lower case wide size characters like “wm”, or 20 lower case regular size characters like “abc”.
    -   The 2 columns data button’s text can fit about 6 Upper case wide size characters like “WM”, 10 Upper case regular size characters like “ABC”, 7 lower case wide size characters like “wm”, or 11 lower case regular size characters like “abc”.
    -   The functional button’s text can fit about 4 Upper case wide size characters like “WM”, 6 Upper case regular size characters like “ABC”, 5 lower case wide size characters like “wm”, or 7 lower case regular size characters like “abc”.

**The Layout for a page with a title, a maximum of 4 data buttons with text/\$Amount, and a maximum of 3 functional buttons:**

![A screenshot of a computer program Description automatically generated](media/945c87124f1a9c317e8b9faab53dcd1e.png) ![A screenshot of a phone Description automatically generated](media/f16057f5091b82996a792e75f0213c48.png)

**The Layout for a page with a title, 5 to 6 data buttons with a text/\$Amount, and maximum of 3 functional buttons:**

![A screenshot of a computer program Description automatically generated](media/219cc30e7a2f9143040a544ef3760c62.png) ![A screenshot of a computer Description automatically generated](media/3d299df47ab524daf0bd4c31518df85b.png)

#### UI Page Option 0x03 Layout

The host uses this option to display a page with the following elements: a title, a section for uploading a custom image, an option at the bottom-left corner to display either the Device Serial Number or host-provided text, and a maximum of one functional green button positioned on the right.

The title and functional button are labeled with String IDs associated with configured String message. See

\*\*

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings\*\*. When the user presses this button, the device sends a notification to the host to indicate the corresponding button is pressed. See **Notification 0x1803 - User Interface Host Action Request.** After that, the host will decide what to do next.

Recommend maximum number of characters and bitmap image setting for this page:

-   Landscape Screen Orientation:
    -   Title text can fit about 18 Upper case wide size characters like “WM”, 23 Upper case regular size characters like “ABC”, 21 lower case wide size characters like “wm”, or 30 lower case regular size characters like “abc”.
    -   Bottom left corner text can fit about 8 Upper case wide size characters like “WM”, 12 Upper case regular size characters like “ABC”, 9 lower case wide size characters like “wm”, or 15 lower case regular size characters like “abc”.
    -   Functional button text can fit about 5 Upper case wide size characters like “WM”, 8 Upper case regular size characters like “ABC”, 6 lower case wide size characters like “wm”, or 9 lower case regular size characters like “abc”.
    -   Bitmap image maximum width is 320px, height is 140px. Color depth can be 24-bit (True Color, RGB), 16-bit (5:5:5:1, RGB Hi Color), 8-bit (256 Color), 4-bit (16 Color), or 1-bit (monochrome)
-   Portrait Screen Orientation:
    -   Title text can fit about 13 Upper case wide size characters like “WM”, 17 Upper case regular size characters like “ABC”, 14 lower case wide size characters like “wm”, or20 lower case regular size characters like “abc”.
    -   Bottom left corner text can fit about 8 Upper case wide size characters like “WM”, 12 Upper case regular size characters like “ABC”, 9 lower case wide size characters like “wm”, or 15 lower case regular size characters like “abc”.
    -   Functional button text can fit about 4 Upper case wide size characters like “WM”, 6 Upper case regular size characters like “ABC”, 5 lower case wide size characters like “wm”, or 7 lower case regular size characters like “abc”.
    -   Bitmap image maximum width is 240px, height is 220px. Color depth can be 24-bit (True Color, RGB), 16-bit (5:5:5:1, RGB Hi Color), 8-bit (256 Color), 4-bit (16 Color), or 1-bit (monochrome)

![A screenshot of a computer error Description automatically generated](media/4bbf7095f6039523570921d1f5705819.png) ![A screenshot of a computer Description automatically generated](media/96fbbb72332b5d65b4157c9bd8e58b49.png)

### [Table 6.33](#table-6-33)1 – Request Data for Command 0x1830

| Tag                                                                                       | Len | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |     |     |         |
| 1830 = **Command 0x1830 - Display Flexible UI Pages (Display Only)**                      |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |     |     |         |
| 81                                                                                        | 01  | Display Time 0x00 – Infinitive. Device leaves the requested page on the display until the host initiates a change. 0x01 to 0xFF = RFU                                                                                                                                                                                                                                                                                                                                                 | B   | R   |         |
| 82                                                                                        | 01  | UI page option 0x00 – Page with up to 5 lines of text and up to 1 functional button Middle. See Tag A1. 0x01 – Page with a title, up to 6 buttons with text, and up to 3 functional buttons. See Tag 83, A2 and A4. 0x02 – Page with a title, up to 6 buttons with \$Amount, and up to 3 functional buttons. See Tag 83, A3 and A4. 0x03 – Page with a title, a custom image, an optional bottom left corner with SN or Text, and up to 1 functional button Right. See Tag 83 and A5. | B   | R   |         |
| 83                                                                                        | 02  | Text String ID for a tile of UI page option: 0x01, 0x02, 0x03 See \*\*                                                                                                                                                                                                                                                                                                                                                                                                                |     |     |         |
|                                                                                           |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |     |     |         |

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings\*\* If host wants to disable this title, do not include this tag. \| B \| O \| \|

\| A1 \| var \| Text string parameters for UI page option: 0x00 The parameter in this TLV data object allow the host to enable and disable the data base for UI page option 0x00 \| B \| O \| \| \| /81 \| var \| Text string (\<= 30 characters) for line 1, end with NULL char. If host wants to disable this line, do not include this tag. \| B \| O \| \| \| /82 \| var \| Text string (\<= 30 characters) for line 2, end with NULL char. If host wants to disable this line, do not include this tag. \| B \| O \| \| \| /83 \| var \| Text string (\<= 30 characters) for line 3, end with NULL char. If host wants to disable this line, do not include this tag. \| B \| O \| \| \| /84 \| var \| Text string (\<= 30 characters) for line 4, end with NULL char. If host wants to disable this line, do not include this tag. \| B \| O \| \| \| /85 \| var \| Text string (\<= 30 characters) for line 5, end with NULL char. If host wants to disable this line, do not include this tag. \| B \| O \| \| \| /86 \| 02 \| Function button Middle option. String ID = Enable functional button Middle with a String ID associates with a configured String message. See \*\*

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings\*\* When user presses this button, device sends notification to the host to indicate the functional button Middle is pressed. See **Notification 0x1803 - User Interface Host Action Request** If host wants to disable this button, do not include this tag \| B \| O \| \|

\| A2 \| var \| Button text String ID parameters for UI page option: 0x01 and 0x02. The parameter in this TLV data object allows the host to enable and disable the data base. When user presses any button, device sends notification to the host to indicate which button is pressed. See **Notification 0x1803 - User Interface Host Action Request** \| B \| O \| \| \| /81 \| 02 \| Text String ID for button 1. See \*\*

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings\*\*. If host wants to disable this button, don’t include this tag. \| B \| O \| \|

\| /82 \| 02 \| Text String ID for button 2. See \*\*

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings\*\*. If host wants to disable this button, don’t include this tag. \| B \| O \| \|

\| /83 \| 02 \| Text String ID for button 3. See \*\*

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings\*\*. If host wants to disable this button, don’t include this tag. \| B \| O \| \|

\| /84 \| 02 \| Text String ID for button 4. See \*\*

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings\*\* . If host wants to disable this button, don’t include this tag. \| B \| O \| \|

\| /85 \| 02 \| Text String ID for button 5. See \*\*

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings\*\* . If host wants to disable this button, don’t include this tag. \| B \| O \| \|

\| /86 \| 02 \| Text String ID for button 6. See \*\*

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings\*\* . If host wants to disable this button, don’t include this tag. \| B \| O \| \|

\| A3 \| var \| Button \$Amount parameters for UI page option: 0x01, 0x02 The parameter in this TLV data object allows the host to enable and disable the data base for UI page option 0x01 and 0x02 When user presses any button, device sends notification to the host to indicate which amount button is pressed. See **Notification 0x1803 - User Interface Host Action Request** \| B \| O \| \| \| /81 \| 04 \| Value \$Amount for button 1. If host wants to disable this button, don’t include this tag. \| B \| O \| \| \| /82 \| 04 \| Value \$Amount for button 2. If host wants to disable this button, don’t include this tag. \| B \| O \| \| \| /83 \| 04 \| Value \$Amount for button 3. If host wants to disable this button, don’t include this tag. \| B \| O \| \| \| /84 \| 04 \| Value \$Amount for button 4. If host wants to disable this button, don’t include this tag. \| B \| O \| \| \| /85 \| 04 \| Value \$Amount for button 5. If host wants to disable this button, don’t include this tag. \| B \| O \| \| \| /86 \| 04 \| Value \$Amount for button 6. If host wants to disable this button, don’t include this tag. \| B \| O \| \| \| A4 \| var \| Functional buttons parameters for UI page option: 0x01 and 0x02. The parameter in this TLV data object allows the host to enable and disable the data base. When user presses any button, the device sends notification to the host to indicate which functional button is pressed. See **Notification 0x1803 - User Interface Host Action Request** \| B \| O \| \| \| /81 \| 03 \| Text String ID and color option for functional button Left. See \*\*

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings\*\*. Byte 0-1: String ID Byte 2: color option 0x00 = red 0x01 = green 0x02 = yellow If host wants to disable this button, don’t include this tag. \| B \| O \| \|

\| /82 \| 03 \| Text String ID and color option for functional button Middle. See \*\*

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings\*\* . Byte 0-1: String ID Byte 2: color option 0x00 = red 0x01 = green 0x02 = yellow If host wants to disable this button, don’t include this tag. \| B \| O \| \|

\| /83 \| 03 \| Text String ID and color option for functional button Right. See \*\*

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings\*\* . Byte 0-1: String ID Byte 2: color option 0x00 = red 0x01 = green 0x02 = yellow If host wants to disable this button, don’t include this tag. \| B \| O \| \|

\| A5 \| var \| Parameters for UI page option 0x03 The parameter in this TLV data object allow the host to enable and disable the data base \| B \| O \| \| \| /81 \| 02 \| Text String ID for green functional button Right. See \*\*

### [[Table 7.51](#table-7-51)0](\#table-7-510) – Default User Interface String IDs and Strings\*\* . When user presses this button, device sends notification to the host to indicate the functional button Right is pressed. See **Notification 0x1803 - User Interface Host Action Request** If host wants to disable this button, don’t include this tag. \| B \| O \| \|

\| /82 \| 02 \| X Position. If host wants device to display the image in the center of the loading image area, don’t include this tag. \| B \| O \| \| \| /83 \| 02 \| Y Position. If host want device to display the image in the center of the loading image area, don’t include this tag Note: Y pos \> = 50px Y pos + Image Height \<= 190px Landscape Screen Orientation Y pos + Image Height \<= 270px Portrait Screen Orientation \| B \| O \| \| \| /84 \| var \| Bitmap Image encoded in full BMP file format as defined by Microsoft (e.g, starting with “BM”) Image Width Max = 320px Landscape Screen Orientation Image Height Max = 140px Landscape Screen Orientation Image Width Max = 240px Portrait Screen Orientation Image Height Max = 220px Portrait Screen Orientation \| B \| O \| \| \| /85 \| var \| Bottom left corner option Byte 0 = option 0x00 = Disable 0x01 = show Device Serial Number 0x02 = show text 0x03..0x0F = invalid Byte 1 = length of the text, should be less than 16 characters. Byte 2..N = text string value. \| B \| 0 \| \| \| End of any wrappers, at minimum **Response Message** found on page **56** \| \| \| \| \| \|

### [Table 6.33](#table-6-33)2 - Response Data for Command 0x1830 - Display Flexible UI Pages (Display Only)

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1830 = **Command 0x1830 - Display Flexible UI Pages (Display Only)**                      |     |                     |     |     |         |
| No parameters                                                                             |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

If the request started successfully, the Request Status in the message wrapper is **All good / requested operation was successful**.

### [Table 6.33](#table-6-33)3 - Request Example

| Example (Hex)                                                                                               |
|-------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 2C 18 30 84 1A 18 30 81 01 00 82 01 00 83 02 00 05 A1 0C 83 0A 54 48 41 4E 4B 20 59 4F 55 00 |

### [Table 6.33](#table-6-33)4 - Response Example

| Example (Hex)                |
|------------------------------|
| AA008104822C1830820400000000 |

### Command 0x1840 – Card Emulation

Card emulation is initiated by receiving a 0x1840 command from the host. The device will prepare card emulation with the parameters provided in the command and start card emulation.

The sequence of events is as follows:

1.  The host ensures the device is not currently running another command, for example, that it is not running a transaction or PIN entry.
2.  The host composes a command request in the format below and sends it to the device.
3.  The device receives the command and verifies that the parameters are valid and the device is in a state that allows the execution of card emulation.
4.  If the device has a display, a prompt will be displayed asking the customer to tap their phone to the device.
5.  If the timeout parameter is not included or set to 0x00, then there is no timeout. Or, if the timeout parameter is set to a specific number of seconds, the device returns a command response message with its Operation Status Summary byte set to 0x01 (OK, Started / Running).
6.  The host may issue a 0x1840 command with Tag 0x81 set to 0x00 to cancel the execution of card emulation.
7.  After the timeout expires, host cancel or the card is read, the device sends a 0x1805 notification to inform the host.

### [Table 6.33](#table-6-33)5 - Request Data for Command 0x1840 – Card Emulation

| Tag | Len     | Value / Description                                                                                                                                 | Req | Default |
|-----|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----|---------|
| /81 | 01      | Start/Cancel 0x00 = Cancel (See the example of 0x1840 cancel command below) 0x01 = Start                                                            | R   |         |
| /82 | 01      | Timeout in seconds 0x00 = No timeout 0x01 to 0xFF = 1 to 255 seconds                                                                                | O   | 0x00    |
| /83 | \<= 254 | URL URL to use as card data. Required when starting card emulation. Optional and ignored if canceling emulation. Example: <https://www.magtek.com/> | O/R |         |

### [Table 6.33](#table-6-33)6 - Request Example

| Example (Hex)                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 01 18 40 84 21 18 40 81 01 01 82 01 00 83 17 68 74 74 70 73 3A 2F 2F 77 77 77 2E 6D 61 67 74 65 6B 2E 63 6F 6D 2F |

### [Table 6.33](#table-6-33)7 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 01 18 40 82 04 01 00 00 00 |

### [Table 6.33](#table-6-33)8 - Example of 0x1840 Cancel Command

| Example (Hex)                                |
|----------------------------------------------|
| AA 00 81 04 01 01 18 40 84 05 18 40 81 01 00 |

## Command Group 0x1Fnn - Device Control

### Command 0x1F01 - Reset Device

The host uses this command to reset the device.

The sequence of events is as follows:

1.  The host constructs the command request for **Command 0x1F01 - Reset Device** in the format below.
2.  The host sends the command request to the device.
3.  The device sends a response in the format below to the host.
4.  The device starts an automatic reset within 500ms.

### [Table 6.41](#table-6-41) - Request Data for Command 0x1F01 - Reset Device

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                                            | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                                                |     |     |         |
| 1F01 = **Command 0x1F01 - Reset Device**                                                 |     |                                                                                                                                                                                                                |     |     |         |
| 81                                                                                       | 01  | Power Off Option 0x00 = Reset 0x01 = Power Off Power off only works while a device is running on its battery. If a device is powered off while it is powered by USB, the device will immediately turn back on. | B   | O   | 0x00    |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                                                                                                                |     |     |         |

### [Table 6.42](#table-6-42) - Response Data for Command 0x1F01 - Reset Device

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1F01 = **Command 0x1F01 - Reset Device**                                                  |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.43](#table-6-43) - Request Example

| Example (Hex)                       |
|-------------------------------------|
| AA 00 81 04 01 12 1F 01 84 02 1F 01 |

### [Table 6.44](#table-6-44) - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 12 1F 01 82 04 00 00 00 00 |

### Command 0x1F02 - Set Notification Subscriptions

The host uses this command to specify which notifications the device should send on each of its available interfaces. By default, the device sends notifications to the host on all interfaces.

The sequence of events is as follows:

1.  The host constructs the command request in the format below.
2.  The host sends the command request to the device.
3.  The device sends a response in the format below to the host.
4.  The device immediately begins routing notifications per the request.
5.  If the device restarts or loses power, the device resets its notification subscriptions to defaults, and the host must call this command again to change them.

### [Table 6.45](#table-6-45) - Request Data for Command 0x1F02 - Set Notification Subscriptions

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                 | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |     |     |         |
| 1F02 = **Command 0x1F02 - Set Notification Subscriptions**                               |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |     |     |         |
| 81                                                                                       | 01  | Subscribe 0x00 = Unsubscribe 0x01 = Subscribe                                                                                                                                                                                                                                                                                                                                                                                                       | B   | O   | 0x01    |
| 82                                                                                       | 01  | Notifications Affected 0x00 = Only subscribe or unsubscribe to notification messages in the Notification Message ID List parameter 0x01 = Subscribe or unsubscribe to all notifications                                                                                                                                                                                                                                                             | B   | O   | 0x01    |
| 83                                                                                       | var | Notification Message ID List List of two-byte Notification Message IDs (MSB first) from section **7 Notifications** to be subscribed / unsubscribed by this command. For example, to subscribe to **Notification 0x0105 - Transaction Operation Complete** on the interface being used to send this command, the host would include 0x0105 as two bytes in the list. The device ignores any Notification Message IDs in the list that do not exist. | B   | O   | Null    |
| A4                                                                                       | var | Interfaces List of interfaces this command should change the subscription settings for. If the host does not specify any interfaces here, the command applies only to the interface the host is using to send the command.                                                                                                                                                                                                                          | B   | O   | Null    |
| /81                                                                                      | 00  | Apply changes to the USB interface                                                                                                                                                                                                                                                                                                                                                                                                                  |     | O   |         |
| /82                                                                                      | 00  | Apply changes to the WLAN interface                                                                                                                                                                                                                                                                                                                                                                                                                 |     | O   |         |
| /83                                                                                      | 00  | Apply changes to the Bluetooth® LE interface                                                                                                                                                                                                                                                                                                                                                                                                        |     | O   |         |
| /84                                                                                      | 00  | Apply changes to the UART interface                                                                                                                                                                                                                                                                                                                                                                                                                 |     | O   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |     |     |         |

### [Table 6.46](#table-6-46) - Response Data for Command 0x1F02 - Set Notification Subscriptions

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1F02 = **Command 0x1F02 - Set Notification Subscriptions**                                |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.47](#table-6-47) - Request Example

| Example (Hex)               |
|-----------------------------|
| AA00 810401551F02 8402 1F02 |

### [Table 6.48](#table-6-48) - Response Example

| Example (Hex)                            |
|------------------------------------------|
| AA00 810482551F02 820400000000 8402 1F02 |

### Command 0x1F03 - Extend Session (Session Management Only)

The host can use this command to extend a session for open protocol interfaces, such as the WLAN interface, which require session management to meet PCI requirements.

The sequence of events is as follows:

1.  The host establishes a session with the device on a given interface. For the WLAN interface, a session starts when the host establishes a TLS websocket connection with the device.
2.  The device starts a countdown timer for a 30 minute session timeout period.
3.  Five minutes before the session timeout period expires, the device starts repeatedly (every minute) sending **Notification 0x1001 - Device Information Update** to report **Session Management / Session Expiring Soon**.
4.  The host may extend the session multiple times, until the device automatically resets to meet PCI’s 24 hour self-test requirement, by sending any command request using the same interface before the timeout occurs. Upon receiving the command, the device resets the session countdown timer to 30 minutes. This helps prevent the session from expiring while the host is actively using the device, including when the device is performing a transaction. If the host wants to extend the session but does not need to send another command, it may follow these steps at any time during the session:
    1.  The host constructs the command request in the format below.
    2.  The host sends the command request to the device.
    3.  The device sends a response in the format below to the host.
    4.  The device resets the session countdown timer to 30 minutes.
5.  When the session expires, the device closes the websocket connection.

For the WLAN interface, if the device is configured to allow connections to more than one client at the same time with **Property 1.2.2.1.1.A Maximum Client Connections** and more than one client is connected, then the following applies. There is always only a single session and it applies to all clients. There is not a separate session for each client. The session starts when the first client connects. Only one client needs to send a command on its connection to extend the session. The other clients do not need to send any commands. When the session expires, all clients will be disconnected.

### [Table 6.49](#table-6-49) - Request Data for Command 0x1F03 - Extend Session (Session Management Only)

| Tag                                                                                      | Len | Value / Description | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                     |     |     |         |
| 1F03 = **Command 0x1F03 - Extend Session (Session Management Only)**                     |     |                     |     |     |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                     |     |     |         |

### [Table 6.41](#table-6-41)0 - Response Data for Command 0x1F03 - Extend Session (Session Management Only)Extend Session

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1F03 = **Command 0x1F03 - Extend Session (Session Management Only)**                      |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.41](#table-6-41)1 - Request Example

| Example (Hex)               |
|-----------------------------|
| AA00 810401551F03 8402 1F03 |

### [Table 6.41](#table-6-41)2 - Response Example

| Example (Hex)                            |
|------------------------------------------|
| AA00 810482551F03 820400000000 8402 1F03 |

### Command 0x1F04 – Terminate Bluetooth® LE Connection (Bluetooth® LE Only)

The host can use this command to terminate a Bluetooth® LE connection. The host may also be able to terminate a Bluetooth® LE connection directly without using this command.

The sequence of events is as follows:

1.  The host constructs the command request for **Device in** the format below.
2.  The host sends the command request to the device.
3.  The device sends a response in the format below to the host.
4.  The device terminates the Bluetooth® LE connection within around 500ms.

### [Table 6.41](#table-6-41)3 - Request Data for Command 0x1F04 – Terminate Bluetooth® LE Connection

| Tag                                                                                      | Len | Value / Description | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                     |     |     |         |
| 1F04 = **Command 0x1F04 – Terminate Bluetooth® LE Connection**                           |     |                     |     |     |         |
| No parameters.                                                                           |     |                     |     |     |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                     |     |     |         |

### [Table 6.41](#table-6-41)4 - Response Data for Command 0x1F04 – Terminate Bluetooth® LE Connection

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1F04 = **Command 0x1F04 – Terminate Bluetooth® LE Connection**                            |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.41](#table-6-41)5 - Request Example

| Example (Hex)                       |
|-------------------------------------|
| AA 00 81 04 01 55 1F 04 84 02 1F 04 |

### [Table 6.41](#table-6-41)6 - Response Example

| Example (Hex)                                         |
|-------------------------------------------------------|
| AA 00 81 04 82 55 1F 04 82 04 00 00 00 00 84 02 1F 04 |

### Command 0x1F05 – Erase All Bluetooth® LE Bonds (Bluetooth® LE Only)

The host can use this command to erase all Bluetooth® LE bonds. The user should then forget the device and re-pair the device on any host that it was previously paired with if that host needs to communicate with the device again.

The sequence of events is as follows:

1.  The host constructs the command request for **Command 0x1F01 - Reset Device** in the format below.
2.  The host sends the command request to the device.
3.  The device sends a response in the format below to the host.
4.  The device erases all Bluetooth® LE bonds within around 500ms.

### [Table 6.41](#table-6-41)7 - Request Data for Command 0x1F05 – Erase All Bluetooth® LE Bonds

| Tag                                                                                      | Len | Value / Description | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                     |     |     |         |
| 1F05 = **Command 0x1F05 – Erase All Bluetooth® LE Bonds**                                |     |                     |     |     |         |
| No parameters.                                                                           |     |                     |     |     |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                     |     |     |         |

### [Table 6.41](#table-6-41)8 - Response Data for Command 0x1F05 – Erase All Bluetooth® LE Bonds

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| 1F05 = **Command 0x1F05 – Erase All Bluetooth® LE Bonds**                                 |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.41](#table-6-41)9 - Request Example

| Example (Hex)                       |
|-------------------------------------|
| AA 00 81 04 01 55 1F 05 84 02 1F 05 |

### [Table 6.42](#table-6-42)0 - Response Example

| Example (Hex)                                         |
|-------------------------------------------------------|
| AA 00 81 04 82 55 1F 05 82 04 00 00 00 00 84 02 1F 05 |

## Command Group 0x20nn - Banking Functions (Touch/Display Only)

### Command 0x2001 - Request PIN with Host Supplied Account Data (Banking Functions Only)

This command directs the device to prompt the cardholder to enter a PIN when a card is not present or is not presented. The host is aware of the account information and the device is not. To prompt the cardholder to present a card before prompting for a PIN, use **Command 0x2002 - Request PIN with Card Supplied Account Data (Banking Functions Only)** instead.

When the host calls this command, the device enters **PIN Entry Mode**, meaning it starts a “PIN Entry session.” While in PIN Entry Mode:

-   The device ignores most other commands from the host, similar to the way it behaves while **Command 0x1001 - Start Transaction** is running: Only essential commands and those that are relevant to the current PIN entry session are allowed.
-   When the device is waiting for the host to take action, it resets the timeout clock and shows an interstitial **PLEASE WAIT** page until one of the following occurs:
    -   The host calls the same PIN entry command again to show another UI sequence or to end the PIN entry session, or
    -   The host calls another allowed command (ending the PIN entry session), or
    -   The device has shown **PLEASE WAIT** until the **Timeout** the host specified in the command has expired (ending the PIN entry session).
-   The host can call this command again and again as needed, to invoke any number and any combination of available PIN Entry User Interface Sequences. This allows the host to determine the number of retries, and to exercise flexible fine-grained control over the end to end “sequence of sequences.”
-   The host may cancel the PIN entry session by calling this command again with **User Interface Sequence = Cancel PIN Session**. In response, the device shows an interstitial page **PIN Entry Canceled** for 2 seconds, then returns to idle.

The usual sequence is as follows:

1.  The host invokes this command using the format in [Table 6.51](#table-6-51).
2.  If an error occurs, the device returns a command response message as shown in [Table 6.52](#table-6-52) with Response Status, Operation Status Summary byte set to 0x80 (Failed to start operation), and terminates the command.
3.  If no error occurs, the device returns a command response message as shown in [Table 6.52](#table-6-52) with Response Status, Operation Status Summary byte set to 0x01 (OK, Started / Running), and enters PIN Entry Mode.
4.  The device shows one of the predefined messages specified by the **User Interface Sequence** parameter and waits up to the specified **Timeout** for the cardholder to enter a PIN.
5.  If the host has specified **User Interface Sequence** = **Enter PIN / Enter PIN Again**, the device automatically prompts the cardholder to enter the PIN a second time.
6.  When the command completes (PIN entry done, cardholder or operator canceled, or **Wait Time** timeout), the device sends **Notification 0x0205 - Banking Functions Operation Complete** to report **Touchscreen** / **PIN Entry**. If PIN entry is successful, the report also contains a payload as shown in [Table 7.23](#table-7-23). The EPB format the device uses depends on the parameters the host specified in the command:
    1.  If the host provided the **Account Number** data in the command, the device creates the EPB using the **PIN Block Format** the host specified in the command.
    2.  If the host did not provide the **Account Number** data in the command, the device creates the EPB using ISO format 1.
7.  If the host is performing a PIN Verification function (such as **User Interface Sequence** = **Enter PIN**), the host software uses the financial institution’s backend systems to compare the EPB to the account information on file, receives a result as to whether the entered PIN was correct, and reports the results to the teller and to the device.
    1.  If the PIN is correct, the host calls the same command again with parameter **User Interface Sequence = PIN Entry Successful** to indicate success and exit PIN Entry Mode. The device responds by showing an interstitial page **PIN Entry Successful** for 2 seconds, then returns to idle mode. The device sounds the EMV success tone to audibly report the result and call the cardholder’s attention to the display.
    2.  If the PIN is incorrect, depending on host-driven retry rules and the history of the session:
        1.  The host may call the same command again with parameter **User Interface Sequence = PIN Incorrect, Try Again** to show the **PIN Incorrect, Try Again** prompt. The device sounds the EMV failure tone to audibly report the result and call the cardholder’s attention to the display.
        2.  The host may call the same command again with other **User Interface Sequences** as desired.
        3.  The host must eventually finalize by calling the same command again with parameters to end the PIN entry session. If the host calls the command with **User Interface Sequence = PIN Entry Failed** to trigger final failure (as opposed to final success described above), the device shows an interstitial page **PIN Entry Failed** for 2 seconds, then returns to idle. The device also sounds the EMV failure tone to audibly report the result and call the cardholder’s attention to the display.
8.  If the host is performing a PIN Entry / Re-PIN function (such as **User Interface Sequence** = **Enter PIN / Enter PIN Again**), after the cardholder enters the PIN a second time:
    1.  If the PINs match:
        1.  The device sends the Encrypted PIN block to the host by sending **Notification 0x0205 - Banking Functions Operation Complete** to report **Touchscreen / PIN Entry / Success / Data Attached**. The host may pass this PIN block to backend systems for processing and storage.
        2.  The host calls the same command again with parameter **User Interface Sequence = PIN Entry Successful** to indicate success and exit PIN Entry Mode. The device responds by showing an interstitial page **PIN Entry Successful** for 2 seconds, then returns to idle mode. The device also sounds the EMV success tone to audibly report the result and call the cardholder’s attention to the display.
    2.  If the PINs do not match, the device sends **Notification 0x0205 - Banking Functions Operation Complete** to report **Touchscreen** / **PIN Entry / Operation Failed / PIN Verify Failed**. Depending on host-driven retry rules and the history of the session:
        1.  The host may call the same command again with parameter **User Interface Sequence = Enter PIN /Enter PIN Again** to prompt the cardholder to enter a PIN twice again.
        2.  The host must eventually finalize by calling the same command again with parameters to end the PIN entry session. If the host calls the command with **User Interface Sequence = PIN Entry Failed** to trigger final failure (as opposed to final success described above), the device shows an interstitial page **PIN Entry Failed** for 2 seconds, then returns to idle. The device also sounds the EMV failure tone to audibly report the result and call the cardholder’s attention to the display.

### [Table 6.51](#table-6-51) - Request Data for Command 0x2001 - Request PIN with Host Supplied Account Data (Banking Functions Only)

| Tag                                                                                              | Len | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Typ | Req | Default |
|--------------------------------------------------------------------------------------------------|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55**         |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |     |     |         |
| 2001 = **Command 0x2001 - Request PIN with Host Supplied Account Data (Banking Functions Only)** |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |     |     |         |
| 81                                                                                               | 01  | Timeout Timeout in seconds that the device should wait for the cardholder to enter PIN and confirm completion. 0x00 = Reserved, Not Allowed 0x01 to 0xFF = 1 to 255 seconds                                                                                                                                                                                                                                                                                                                             | B   | R   |         |
| 82                                                                                               | 01  | User Interface Sequence 0x00 = Enter PIN (start session) 0x02 = PIN Incorrect, Try Again (continue session) 0x03 = Enter PIN / Enter PIN Again (start session) 0x05 = Enter PIN Again (continue session) 0xFD = Cancel PIN Session (end session) 0xFE = PIN Entry Failed (end session) 0xFF = PIN Entry Successful (end session)                                                                                                                                                                        | B   | R   |         |
| 83                                                                                               | 02  | PIN Length Limits Byte 1 Maximum PIN Length (\<= 0x0C) Byte 2 Minimum PIN Length (\>=0x04)                                                                                                                                                                                                                                                                                                                                                                                                              | B   | R   |         |
| A1                                                                                               | var | Account Number Options                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | T   | R   |         |
| /81                                                                                              | 01  | Account Number Length When host specifies **PIN Block Format** parameter = **ISO Format 1** the Account Number length must be 0 When host specifies **PIN Block Format** parameter = **ISO Format 0 or 3** the Account Number length must be 12 When host specifies **PIN Block Format** parameter = **ISO Format 4** the Account Number length must be between 12 and 19 , if this length is not an even number, the device ignores the rightmost nibble, which the host should generally set to zero. | B   | R   |         |
| /82                                                                                              | var | Account Number If the host does provide an account number, it must provide it in Compressed Numeric (CN) format as defined by **EMV 4.3 Book 3**, section **Data Element Format Conventions**                                                                                                                                                                                                                                                                                                           | CN  | O   |         |
| 85                                                                                               | 01  | PIN Block Format 0x00 = ISO Format 0 0x01 = ISO Format 1 0x03 = ISO Format 3 0x04 = ISO Format 4                                                                                                                                                                                                                                                                                                                                                                                                        | B   | R   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**               |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |     |     |         |

### [Table 6.52](#table-6-52) - Response Data for Command 0x2001 - Request PIN with Host Supplied Account Data (Banking Functions Only)

| Tag                                                                                              | Len | Value / Description | Typ | Req | Default |
|--------------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56**        |     |                     |     |     |         |
| 2001 = **Command 0x2001 - Request PIN with Host Supplied Account Data (Banking Functions Only)** |     |                     |     |     |         |
| No parameters.                                                                                   |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**              |     |                     |     |     |         |

If the request started successfully, the Response Status in the message wrapper is **OK, Started/Running**.

### [Table 6.53](#table-6-53) - Request Example for Command 0x2001 - Request PIN with Host Supplied Account Data (Banking Functions Only)

| Example (Hex)                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 09 20 01 84 1C 20 01 81 01 3C 82 01 00 83 02 08 04 85 01 00 A1 0B 81 01 0C 82 06 12 34 56 78 90 12 |

### [Table 6.54](#table-6-54) - Response Example Command 0x2001 - Request PIN with Host Supplied Account Data (Banking Functions Only)

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 09 20 01 82 04 01 00 00 00 |

### Command 0x2002 - Request PIN with Card Supplied Account Data (Banking Functions Only)

This command directs the device to prompt the cardholder to present their card by swiping, dipping or tapping, and to enter a PIN. To prompt the cardholder for a PIN without presenting a card when the host knows the account number already, use **Command 0x2001 - Request PIN with Host Supplied Account Data (Banking Functions Only)** instead.

When the host calls this command, the device enters **PIN Entry Mode**, meaning it starts a “PIN Entry session.” While in PIN Entry Mode:

-   The device ignores most other commands from the host, similar to the way it behaves while **Command 0x1001 - Start Transaction** is running: Only essential commands and those that are relevant to the current PIN Entry session are allowed.
-   When the device is waiting for the host to take action, it resets the timeout clock and shows an interstitial **PLEASE WAIT** page until one of the following occurs:
    -   The host calls the same PIN entry command again to show another UI sequence or to end the PIN entry session, or
    -   The host calls another allowed command (ending the PIN entry session), or
    -   The device has shown **PLEASE WAIT** until the **Timeout** the host specified in the command has expired (ending the PIN entry session).
-   The host can call this command again and again as needed, to invoke any number and any combination of available PIN Entry User Interface Sequences. This allows the host to determine number of retries, and to exercise flexible fine-grained control over the end to end “sequence of sequences.”
-   The host may cancel the PIN entry session by calling this command again with **User Interface Sequence = Cancel PIN Session**. In response, the device shows an interstitial page **PIN Entry Canceled** for 2 seconds, then returns to idle.

The usual sequence is as follows:

1.  The host invokes this command using the format in [Table 6.55](#table-6-55).
2.  If an error occurs, the device returns a command response message as shown in [Table 6.56](#table-6-56) with Response Status, Operation Status Summary byte set to 0x80 (Failed to start operation), and terminates the command.
3.  If no error occurs, the device returns a command response message as shown in [Table 6.56](#table-6-56) with Response Status, Operation Status Summary byte set to 0x01 (OK, Started / Running), and enters PIN Entry Mode.
4.  The device shows a prompt requesting the cardholder present one of the payment technologies specified in the **Reader Options** parameter, and waits up to the specified **Timeout** for the cardholder to respond.
5.  After the cardholder presents a card, the device sends **Notification 0x0201 - Banking Functions Information Update** to report the payment technology being used / Card Event / Detected.
6.  If the cardholder swiped a magnetic stripe card, the device reads Track 2 data.
7.  If cardholder inserts an ICC or taps a PICC, the device reads records from the card and attempts to retrieve tags 57 (Track 2 Equivalent Data) and 5A (Primary Account number). It then powers off the card without performing the first Generate Application Cryptogram, so the card does not increment its transaction counters.
8.  If an error occurs, the device terminates the command and PIN entry session and sends **Notification 0x0205 - Banking Functions Operation Complete** to report Touchscreen / PIN Entry / Operation Failed / Account Data Capture Failed.
9.  The device shows one of the predefined messages specified by the **User Interface Sequence** parameter, and waits up to the specified **Timeout** for the cardholder to enter a PIN.
10. If the host has specified **User Interface Sequence** = **Enter PIN / Enter PIN Again**, the device automatically prompts the cardholder to enter the PIN a second time.
11. When the command completes (PIN entry done, cardholder or operator canceled, or **Wait Time** timeout), the device sends a **Notification 0x0205 - Banking Functions Operation Complete** to report **Touchscreen** **PIN Entry**. If PIN entry is successful, the report also contains a payload as shown in [Table 7.24](#table-7-24). The device creates the EPB using the **PIN Block Format** the host specified in the command.
12. If the host is performing a PIN Verification function (such as **User Interface Sequence** = **Enter PIN**), the host software uses the financial institution’s backend systems to compare the EPB to the account information on file, receives a result as to whether the entered PIN was correct, and reports the results to the teller and to the device.
    1.  If the PIN is correct, the host calls the same command again with parameter **User Interface Sequence = PIN Entry Successful** to indicate success and exit PIN Entry Mode. The device responds by showing an interstitial page **PIN Entry Successful** for 2 seconds, then returns to idle mode. The device sounds the EMV success tone to audibly report the result and call the cardholder’s attention to the display.
    2.  If the PIN is incorrect, depending on host-driven retry rules and the history of the session:
        1.  The host may call the same command again with parameter **User Interface Sequence = PIN Incorrect, Try Again** to show the **PIN Incorrect, Try Again** prompt. The device sounds the EMV failure tone to audibly report the result and call the cardholder’s attention to the display.
        2.  The host may call the same command again with other **User Interface Sequences** as desired.
        3.  The host must eventually finalize by calling the same command again with parameters to end the PIN entry session. If the host calls the command with **User Interface Sequence = PIN Entry Failed** to trigger final failure (as opposed to final success described above), the device shows an interstitial page **PIN Entry Failed** for 2 seconds, then returns to idle. The device also sounds the EMV failure tone to audibly report the result and call the cardholder’s attention to the display.
13. If the host is performing a PIN Entry / Re-PIN function (such as **User Interface Sequence** = **Enter PIN / Enter PIN Again**), after the cardholder enters the PIN a second time:
    1.  If the PINs match:
        1.  The device sends the Encrypted PIN block to the host by sending **Notification 0x0205 - Banking Functions Operation Complete** to report **Touchscreen / PIN Entry / Success / Data Attached**. The host may pass this PIN block to backend systems for processing and storage.
        2.  The host calls the same command again with parameter **User Interface Sequence = PIN Entry Successful** to indicate success and exit PIN Entry Mode. The device responds by showing an interstitial page **PIN Entry Successful** for 2 seconds, then returns to idle mode. The device also sounds the EMV success tone to audibly report the result and call the cardholder’s attention to the display.
    2.  If the PINs do not match, the device sends **Notification 0x0205 - Banking Functions Operation Complete** to report **Touchscreen** / **PIN Entry / Operation Failed / PIN Verify Failed**. Depending on host-driven retry rules and the history of the session:
        1.  The host may call the same command again with parameter **User Interface Sequence = Enter PIN /Enter PIN Again** to prompt the cardholder to enter a PIN twice again.
        2.  The host must eventually finalize by calling the same command again with parameters to end the PIN entry session. If the host calls the command with **User Interface Sequence = PIN Entry Failed** to trigger final failure (as opposed to final success described above), the device shows an interstitial page **PIN Entry Failed** for 2 seconds, then returns to idle. The device also sounds the EMV failure tone to audibly report the result and call the cardholder’s attention to the display.

### [Table 6.55](#table-6-55) - Request Data for Command 0x2002 - Request PIN with Card Supplied Account Data (Banking Functions Only)

| Tag                                                                                              | Len | Value / Description                                                                                                                                                                                                                                                                                                                                                                        | Typ | Req | Default |
|--------------------------------------------------------------------------------------------------|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55**         |     |                                                                                                                                                                                                                                                                                                                                                                                            |     |     |         |
| 2002 = **Command 0x2002 - Request PIN with Card Supplied Account Data (Banking Functions Only)** |     |                                                                                                                                                                                                                                                                                                                                                                                            |     |     |         |
| 81                                                                                               | 01  | Timeout Timeout in seconds that the device should wait for the cardholder to present card, enter PIN and confirm completion.                                                                                                                                                                                                                                                               | B   | R   |         |
| A3                                                                                               | 09  | Reader Options The parameters inside this TLV data object allow the host to enable and disable the various payment method interfaces                                                                                                                                                                                                                                                       | TC  | R   |         |
| /81                                                                                              | 01  | Magnetic Stripe Reader Mode 0x00 = Disabled 0x01 = Enabled                                                                                                                                                                                                                                                                                                                                 | B   | R   |         |
| /82                                                                                              | 01  | Contact Reader Mode 0x00 = Disabled 0x01 = Enabled                                                                                                                                                                                                                                                                                                                                         | B   | R   |         |
| /83                                                                                              | 01  | Contactless Reader Mode 0x00 = Disabled 0x01 = Enabled                                                                                                                                                                                                                                                                                                                                     | B   | R   |         |
| A4                                                                                               | 0A  | PIN Entry Options                                                                                                                                                                                                                                                                                                                                                                          | B   | R   |         |
| /82                                                                                              | 01  | User Interface Sequence 0x00 = Reserved 0x01 = Present Card / Enter PIN (start session) 0x02 = PIN Incorrect, Try Again (continue session) 0x03 = Enter PIN / Enter PIN Again (continue session) 0x04 = Present Card / Enter PIN / Enter PIN Again (start session) 0xFD = Cancel PIN Session (end session) 0xFE = PIN Entry Failed (end session) 0xFF = PIN Entry Successful (end session) | B   | R   |         |
| /83                                                                                              | 02  | PIN Length Limits (Only when PIN is requested) Byte 1 Maximum PIN Length (\<= 0x0C) Byte 2 Minimum PIN Length (\>=0x04)                                                                                                                                                                                                                                                                    | B   | R   |         |
| /85                                                                                              | 01  | PIN Block Format (Only when PIN is requested) 0x00 = ISO Format 0 0x01 = Reserved / Invalid 0x03 = ISO Format 3 0x04 = ISO Format 4.                                                                                                                                                                                                                                                       | B   | R   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**               |     |                                                                                                                                                                                                                                                                                                                                                                                            |     |     |         |

### [Table 6.56](#table-6-56) - Response Data for Command 0x2002 - Request PIN with Card Supplied Account Data (Banking Functions Only)

| Tag                                                                                              | Len | Value / Description | Typ | Req | Default |
|--------------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56**        |     |                     |     |     |         |
| 2002 = **Command 0x2002 - Request PIN with Card Supplied Account Data (Banking Functions Only)** |     |                     |     |     |         |
| No parameters.                                                                                   |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**              |     |                     |     |     |         |

If the request started successfully, the Request Status in the message wrapper is **OK / Operation Started**.

### [Table 6.57](#table-6-57) - Request Example Command 0x2002 - Request PIN with Card Supplied Account Data (Banking Functions Only)

| Example (Hex)                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 0C 20 02 84 1C 20 02 81 01 3C A3 09 81 01 01 82 01 01 83 01 01 A4 0A 82 01 01 83 02 08 04 85 01 00 |

### [Table 6.58](#table-6-58) - Response Example Command 0x2002 - Request PIN with Card Supplied Account Data (Banking Functions Only)

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 0C 20 02 82 04 01 00 00 00 |

## Command Group 0xD1nn - Settings and Information

### Command 0xD101 - Get Property

The host uses this command to get information about the device or its configuration / settings.

Each data element representing device information or device configuration is part of a tree of values and is uniquely identified by an Object Identifier (also known as an Object ID or OID) as defined in **ITU-T X.660 \| ISO/IEC 9834-1**, which can be found by searching for **X.660** in the publications on [www.itu.int](http://www.itu.int). This document refers to these data elements collectively as **Properties**. The list of all properties and their corresponding OIDs and other characteristics is provided in section **8 Configuration**.

This command can be used in multiple ways. For simplicity, this document describes one possible way that does not require detailed knowledge of the **X.660** specification.

To get a property, the sequence of events is as follows:

1.  The host determines which property or tree branch of properties it wants to get from the device (see section **8 Configuration**).
2.  The host composes the command request in the format below, and sends it to the device.
3.  The device sends a response. If the request succeeded, the response includes the value(s) of the requested property or properties. If it did not succeed, the device returns a failure response with no command-specific parameters.

### [Table 6.61](#table-6-61) - Request Data for Command 0xD101 - Get Property

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Typ | Req | Default              |
|------------------------------------------------------------------------------------------|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|----------------------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |     |     |                      |
| D101 = **Command 0xD101 - Get Property**                                                 |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |     |     |                      |
| 81                                                                                       | var | Company ID This value is the root of the “long form” of the Property OID, and is the same for all MagTek devices. Leave this parameter empty and use the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | B   | O   | 2B 06 01 04 01 F6 09 |
| 82                                                                                       | 03  | Device Family ID This value is the second portion of the “long form” of the Property OID, and is the same for all similar MagTek devices within the same product family. Unless you have a specific use case that uses this parameter, leave this parameter empty and use the default otherwise your software may not work with multiple products. Byte 1 Platform 0x02 = Apollo Platform Byte 2 Product 0x01 = DynaFlex, 0x02 = DynaProx, 0x03 = DynaFlex II PED, 0x04 = DynaFlex II, 0x05 = DynaFlex II Go Byte 3 Device Variant 0x00 = Standard                                                                                                                                                                  | B   | O   | Product dependent    |
| 85                                                                                       | 01  | Property Type This parameter contains the first number of the Property OID as documented in section **8 Configuration**. 0x01 = Device Settings 0x02 = Device Information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | B   | R   |                      |
| 87                                                                                       | var | Property OID Tree Prefix This optional parameter contains subsequent numbers of the Property’s OID as documented in section **8 Configuration**, but can not include the final number. This can also be populated with fewer numbers from the OID, in which case the remaining numbers of the OID of the Property or set of Properties you wish to retrieve must be included in the **Property OID Remainder**. For simplicity, populate this with the 2nd through the second-to-last number in the property’s OID.                                                                                                                                                                                                 | B   | O   | Null                 |
| 89                                                                                       | var | Property OID Remainder This contains the remaining numbers of the Property’s OID, BER TLV encoded per **X.660** section **8 Basic encoding rules**. For details about TLV encoding an OID. To request a set of properties in a branch of the Property OID structure, the host should pass a partial Property OID, and the device returns the value of all properties from the specified tree level downward. For simplicity, include all numbers except the final number of the property’s OID in **Property Type** and **Property OID Tree Prefix**, and include the final number of the OID OR 0xC0 here, then append constant byte 0x00. These two bytes represent a single empty BER TLV primitive data object. | B   | R   |                      |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |     |     |                      |

### [Table 6.62](#table-6-62) - Response Data for Command 0xD101 - Get Property

| Tag                                                                                       | Len | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |     |         |
| D101 = **Command 0xD101 - Get Property**                                                  |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |     |         |
| 81                                                                                        | var | Company ID This contains the Company ID the host included in the request message. If this parameter is not included in the request, the response does not include it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | B   | O   | N/A     |
| 82                                                                                        | 03  | Device Family ID This contains the Device Family ID the host included in the request message. If this parameter is not included in the request, the response does not include it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | B   | O   | N/A     |
| 85                                                                                        | 01  | Property Type This contains the Property Type the host included in the request message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | B   | R   | N/A     |
| 87                                                                                        | var | Property OID Tree Prefix This contains the Property OID Tree Prefix the host included in the request message. If this parameter is not included in the request, the response does not include it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | B   | O   | N/A     |
| 89                                                                                        | var | Property OID Remainder This contains the same TLV-encoded portion of the OID the host included in the Property OID Remainder of the request message, with leaf nodes populated with actual values. If the host requested a set of properties in a branch of the Property OID structure, this contains the set of requested branches, including branch OIDs, leaf node IDs, and values. If the host follows the “for simplicity” recommendation in the request message to request a single property, it can retrieve the value of the requested property by stripping off the first few bytes, which represent the TLV-encoded last number in the OID and the length of the property’s value, as follows; the remaining bytes are the value of the property: If the second byte is 7F or less, strip off the first two bytes. If the second byte is 81, strip off the first three bytes. If the second byte is 82, strip off the first four bytes. | B   | R   | N/A     |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |     |         |

If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**.

### [Table 6.63](#table-6-63) - Request Example

| Example (Hex)                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Get **Property 1.2.7.1.1.1 Device Reset Occurred Notification Control** using “simple” form: AA00 8104 0155D101 840F D101 8501 01 8704 02070101 8902 C100 |

### [Table 6.64](#table-6-64) - Response Example

| Example (Hex)                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Get **Property 1.2.7.1.1.1 Device Reset Occurred Notification Control** using “simple” form: AA00 8104 8255D101 8204 00000000 84820010 D101 8501 01 8704 02070101 8903 C101 00 |

### [Table 6.65](#table-6-65) - Request Example

| Example (Hex)                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Get **Property 1.2.7.1.1.1 Device Reset Occurred Notification Control** using longer Property OID Remainder: AA00 8104 0155D101 8411 D101 8501 01 890A E208 E706 E104 E102 C100 |

### [Table 6.66](#table-6-66) - Response Example

| Example (Hex)                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Get **Property 1.2.7.1.1.1 Device Reset Occurred Notification Control** using longer Property OID Remainder: AA00 8104 8255D101 8204 00000000 84820012 D101 8501 01 890B E209 E707 E105 E103 C101 00 |

### [Table 6.67](#table-6-67) - Request Example

| Example (Hex)                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------|
| Get **Property Subgroup 2.1.2.2.nn Core Firmware Information** using “simple” form: AA00 8104 0155D101 840D D101 8501 02 8702 0102 8902 C200 |

### [Table 6.68](#table-6-68) - Response Example

| Example (Hex)                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Get **Property Subgroup 2.1.2.2.nn Core Firmware Information** using “simple” form: AA00 81 04 8255D101 82 04 00000000 84 820056 D101 85 01 02 87 02 0102 89 820049 E2 820045 E1 820004 C1 00 C2 00 E2 820039 C1 0D 44796E61466C65782050726F00 C2 13 313030303030373138332D41352D5043490000 C3 00 C4 0B 3130303030303731383300 C5 00 C6 02 FF00 |

### Command 0xD111 - Set Property (Unsecured)

| ![](media/03555afcb3177a7ebf5f264c12d86851.png)                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Properties are stored in flash memory, which inherently has a limited number of read-write cycles before it begins to wear. For this reason, MagTek recommends setting properties as few times as possible over the lifecycle of the device. |

The host uses this command to set device configuration / settings that do not require security. For setting properties that require security see **Command 0xD112 - Set Property (Secured)**.

Each data element representing device configuration is part of a tree of values and is uniquely identified by an Object Identifier (also known as an Object ID or OID) as defined in **ITU-T X.660 \| ISO/IEC 9834-1**, which can be found by searching for **X.660** in the publications on [www.itu.int](http://www.itu.int). This document refers to these data elements collectively as **Properties**. The list of all properties and their corresponding OIDs and other characteristics is provided in section **8 Configuration**.

This command can be used in multiple ways. For simplicity, this document describes one possible way that does not require detailed knowledge of the **X.660** specification.

To set a property, the sequence of events is as follows:

1.  The host determines which property it wants to set and the value it wants to set in the device (see section **8 Configuration**).
2.  The host composes a command request in the format below, and sends it to the device.
3.  The device sends a response in the format below. If the request succeeded, the response payload is identical to the request payload. If it did not succeed, the device returns a failure response with no command-specific parameters.

### [Table 6.69](#table-6-69) - Request Data for Command 0xD111 - Set Property (Unsecured)

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Typ | Req | Default              |
|------------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|----------------------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |     |     |                      |
| D111 = **Command 0xD111 - Set Property (Unsecured)**                                     |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |     |     |                      |
| 81                                                                                       | var | Company ID This value is the root of the “long form” of the Property OID, and is the same for all MagTek devices. Leave this parameter empty and use the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | B   | O   | 2B 06 01 04 01 F6 09 |
| 82                                                                                       | 03  | Device Family ID This value is the second portion of the “long form” of the Property OID, and is the same for all similar MagTek devices within the same product family. Unless you have a specific use case that uses this parameter, leave this parameter empty and use the default otherwise your software may not work with multiple products. Byte 1 Platform 0x02 = Apollo Platform Byte 2 Product 0x01 = DynaFlex, 0x02 = DynaProx, 0x03 = DynaFlex II PED, 0x04 = DynaFlex II, 0x05 = DynaFlex II Go Byte 3 Device Variant 0x00 = Standard                                                                                                                                                                                                                   | B   | O   | Product dependent    |
| 85                                                                                       | 01  | Property Type This parameter contains the first number of the Property OID as documented in section **8 Configuration**. 0x01 = Device Settings 0x02 = Device Information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | B   | R   |                      |
| 87                                                                                       | var | Property OID Tree Prefix This optional parameter contains subsequent numbers of the Property’s OID as documented in section **8 Configuration**, but can not include the final number. For simplicity, populate this with the 2nd through the second-to-last number in the property’s OID. This can also be populated with fewer numbers from the OID, in which case the remaining numbers of the OID must be included in the **Property OID Remainder**.                                                                                                                                                                                                                                                                                                            | B   | O   | Null                 |
| 89                                                                                       | var | Property OID Remainder This contains the remaining numbers of the Property’s OID, BER TLV encoded per **X.660** section **8 Basic encoding rules**. For details about TLV encoding an OID. For simplicity, include all numbers except the final number of the property’s OID in **Property Type** and **Property OID Tree Prefix**, and include the final number of the OID OR 0xC0 here, then append a length corresponding one of the following, then append the value to set the property to: If the length of the value you are setting is 0x7F or shorter, include one byte equal to the length of the value. If the length of the value you are setting is greater than 0x7F but less than 0xFFFF, append 82, then two bytes equal to the length of the value. | B   | R   |                      |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |     |     |                      |

### [Table 6.61](#table-6-61)0 - Response Data for Command 0xD111 - Set Property (Unsecured)

| Tag                                                                                       | Len | Value / Description                                                                                                                                                                               | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                                                                                                                                                                                                   |     |     |         |
| D111 = **Command 0xD111 - Set Property (Unsecured)**                                      |     |                                                                                                                                                                                                   |     |     |         |
| 81                                                                                        | var | Company ID This contains the Company ID the host included in the request message. If this parameter is not included in the request, the response does not include it.                             | B   | O   | N/A     |
| 82                                                                                        | 03  | Device Family ID This contains the Device Family ID the host included in the request message. If this parameter is not included in the request, the response does not include it.                 | B   | O   | N/A     |
| 85                                                                                        | 01  | Property Type This contains the Property Type the host included in the request message.                                                                                                           | B   | R   | N/A     |
| 87                                                                                        | var | Property OID Tree Prefix This contains the Property OID Tree Prefix the host included in the request message. If this parameter is not included in the request, the response does not include it. | B   | O   | N/A     |
| 89                                                                                        | var | Property OID Remainder This contains the same TLV-encoded portion of the OID the host included in the Property OID Remainder of the request message.                                              | B   | R   | N/A     |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                                                                                                                                                                                                   |     |     |         |

### [Table 6.61](#table-6-61)1 - Request Example

| Example (Hex)                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set **Property 1.2.7.1.1.1 Device Reset Occurred Notification Control** AA 00 81 04 01 55 D1 11 84 10 D1 11 85 01 01 87 04 02 07 01 01 89 03 C1 01 00 |

### [Table 6.61](#table-6-61)2 - Response Example

| Example (Hex)                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set **Property 1.2.7.1.1.1 Device Reset Occurred Notification Control** AA 00 81 04 82 55 D1 11 82 04 00 00 00 00 84 82 00 10 D1 11 85 01 01 87 04 02 07 01 01 89 03 C1 01 00 |

### Command 0xD112 - Set Property (Secured)

| ![A black and white sign with letters Description automatically generated](media/03555afcb3177a7ebf5f264c12d86851.png)                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Properties are stored in flash memory, which inherently has a limited number of read-write cycles before it begins to wear. For this reason, MagTek recommends setting properties as few times as possible over the lifecycle of the device. |

The host uses this command to set device configuration / settings securely. Properties that require security should specify that they do in their documentation. This command can also be used for properties that do not require security.

The details, request data and response data of this command are identical to what is documented in **Command 0xD111 - Set Property (Unsecured),** however, the command must be structured and sent according to what is documented in sequence of events 1-5 of **Command 0xD811 - Start Send File to Device (Secured)**.

### Command 0xD201 - Reset Properties to Defaults (MAGTEK INTERNAL ONLY FOR NOW)

The host uses this command to reset the device’s Command 0xD201 - Reset Properties to Defaults (MAGTEK INTERNAL ONLY FOR NOW) Properties to their default values. It does not reset configuration values that are set using **Command 0xD111 - Set Property (Unsecured)** or **Command 0xD112 - Set Property (Secured)**.

The sequence of events is as follows:

1.  The host composes a command request in the format below and sends it to the device.
2.  The device resets all properties to the default values specified by the command.
3.  The device sends a response in the format below.
4.  The device automatically resets and applies the new settings.

### [Table 6.61](#table-6-61)3 - Request Data for Command 0xD201

| Tag                                                                                       | Len | Value / Description                                                                                           | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55**. |     |                                                                                                               |     |     |         |
| D201= Command 0xD112 - Set Property (Secured)                                             |     |                                                                                                               |     |     |         |
| 81                                                                                        | 01  | Default Values to Use 0x01 = Use Firmware Defaults (see section **8**) Other Values = Reserved for future use | B   | R   | 01      |
| End of any wrappers, at minimum including **Request Message** found on page **55**        |     |                                                                                                               |     |     |         |

### [Table 6.61](#table-6-61)4 - Response Data for Command 0xD201

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| D201= Command 0xD112 - Set Property (Secured)                                             |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.61](#table-6-61)5 - Request Example

| Example (Hex)                      |
|------------------------------------|
| AA00 81040101D201 8405 D201 810101 |

### [Table 6.61](#table-6-61)6 - Response Example

| Example (Hex)                  |
|--------------------------------|
| AA00 81048201D201 820400000000 |

## Command Group 0xD8nn - File Operations

### About Files

Large blobs of data uploaded to / downloaded from the device are referred to as “files” and share a common set of commands documented here, and special message type **Data File Message**. Some file types can be sent in the File Payload fields in “raw” form (e.g. certificates and images) with metadata coming from the command request and response. Other file types require the addition of MagTek metadata included inside the File Payload blob; these are documented in the “File Type” subsections of section **4 Data Types and Shared TLV Data Objects**.

Files Types that may come from the host include:

-   EMV configuration
-   Firmware updates
-   Public Key Infrastructure (PKI) Certificates
-   User interface images and prompts
-   EMV kernels
-   SRED BIN tables

File Types that may come from the device include:

-   Read back of the above file types
-   Signature Capture
-   Logs
-   Certificate Requests

The commands in this section share a common list of 4-byte file types, listed in Table. File types marked as Secured = Yes must be loaded using **Command 0xD811 - Start Send File to Device (Secured)**; file types that are marked as Secured = No can be loaded using **Command 0xD812 - Start Send File to Device (Unsecured)**.

### [Table 6.71](#table-6-71) - File Types

| Description                                                                                            | Secured          | File Type | File Type Version | File Subtype | File Instance |
|--------------------------------------------------------------------------------------------------------|------------------|-----------|-------------------|--------------|---------------|
| EMV configuration, terminal file. See file definition in section 4.8 on page 87.                       | Get: No Set: No  | 0x00      | 0x00              | 0x00         | 0x00          |
| EMV configuration, processing file. See file definition in section 4.9 on page 89.                     | Get: No Set: No  | 0x00      | 0x00              | 0x01         | 0x00          |
| EMV configuration, entry point file. See file definition in section 4.10 on page 91.                   | Get: No Set: No  | 0x00      | 0x00              | 0x02         | 0x00          |
| EMV configuration, CA keys file. See file definition in section 0 on page 104.                         | Get: No Set: No  | 0x00      | 0x00              | 0x03         | 0x00          |
| EMV configuration, Visa DRL set. Reserved for future use.                                              | Get: No Set: No  | 0x00      | 0x00              | 0x04         | 0x00          |
| EMV configuration, American Express DRL set. See file definition in section 4.12 on page 109.          | Get: No Set: No  | 0x00      | 0x00              | 0x05         | 0x00          |
| EMV configuration, MasterCard update conditions. Reserved for future use.                              | Get: No Set: No  | 0x00      | 0x00              | 0x06         | 0x00          |
| EMV configuration, American Express update conditions. Reserved for future use.                        | Get: No Set: No  | 0x00      | 0x00              | 0x08         | 0x00          |
| EMV configuration, Discover update conditions. Reserved for future use.                                | Get: No Set: No  | 0x00      | 0x00              | 0x09         | 0x00          |
| EMV configuration, CA revocation list. Reserved for future use.                                        | Get: No Set: No  | 0x00      | 0x00              | 0x0A         | 0x00          |
| EMV configuration, exception file list. Reserved for future use.                                       | Get: No Set: No  | 0x00      | 0x00              | 0x0B         | 0x00          |
| EMV configuration, DPAS data storage. Reserved for future use.                                         | Get: No Set: No  | 0x00      | 0x00              | 0x0C         | 0x00          |
| (Touch Only) Signature capture file. See file definition in section 4.15 on page 113.                  | Get: No Set: NA  | 0x01      | 0x00              | 0x00         | 0x00          |
| (Display Only) Custom Idle Page Image 1. For details, see Property 1.2.3.1.1.1 Custom Idle Page Image. | Get: NA Set: No  | 0x02      | 0x00              | 0x00         | 0x00          |
| (Display Only) Custom Idle Page Image 2. For details, see Property 1.2.3.1.1.1 Custom Idle Page Image. | Get: NA Set: No  | 0x02      | 0x00              | 0x00         | 0x01          |
| (Display Only) Custom Idle Page Image 3. For details, see Property 1.2.3.1.1.1 Custom Idle Page Image. | Get: NA Set: No  | 0x02      | 0x00              | 0x00         | 0x02          |
| (Display Only) Custom Idle Page Image 4. For details, see Property 1.2.3.1.1.1 Custom Idle Page Image. | Get: NA Set: No  | 0x02      | 0x00              | 0x00         | 0x03          |
| (WLAN Only) Apollo root CA certificate See Certificate File Types.                                     | Get: No Set: Yes | 0x03      | 0x00              | 0x00         | 0x00          |
| (WLAN Only) Apollo intermediate CA certificate See Certificate File Types.                             | Get: No Set: Yes | 0x03      | 0x00              | 0x01         | 0x00          |
| (WLAN Only) Apollo server certificate See Certificate File Types.                                      | Get: No Set: No  | 0x03      | 0x00              | 0x02         | 0x00          |
| (WLAN Only) Customer root CA certificate See Certificate File Types.                                   | Get: No Set: Yes | 0x03      | 0x00              | 0x03         | 0x00          |
| (WLAN Only) Customer intermediate CA certificate See Certificate File Types.                           | Get: No Set: Yes | 0x03      | 0x00              | 0x04         | 0x00          |
| (WLAN Only) Customer server certificate See Certificate File Types.                                    | Get: No Set: No  | 0x03      | 0x00              | 0x05         | 0x00          |
| (WLAN Only) Commercial root CA certificate See Certificate File Types.                                 | Get: No Set: Yes | 0x03      | 0x00              | 0x06         | 0x00          |
| (WLAN Only) Commercial intermediate CA certificate See Certificate File Types.                         | Get: No Set: Yes | 0x03      | 0x00              | 0x07         | 0x00          |
| (WLAN Only) Commercial server certificate See Certificate File Types.                                  | Get: No Set: No  | 0x03      | 0x00              | 0x08         | 0x00          |
| (WLAN Only) Apollo trust certificate See Certificate File Types.                                       | Get: No Set: No  | 0x03      | 0x00              | 0x09         | 0x00          |
| (WLAN Only) Customer trust certificate See Certificate File Types.                                     | Get: No Set: No  | 0x03      | 0x00              | 0x0A         | 0x00          |
| (WLAN Only) Apollo client certificate See Certificate File Types.                                      | Get: No Set: No  | 0x03      | 0x00              | 0x0B         | 0x00          |
| (WLAN Only) Certificate signing request (CSR) See Certificate Signing Request (CSR) File Types.        | Get: No Set: N/A | 0x04      | 0x00              | 0x00         | 0x00          |
| (WLAN Only) WebSocket Trust configuration file, Request file from MagTek.                              | Get: N/A Set: No | 0x05      | 0x00              | 0x00         | 0x00          |
| (WLAN Only) MQTT Trust configuration file, Request file from MagTek.                                   | Get: N/A Set: No | 0x05      | 0x00              | 0x01         | 0x00          |
| UI configuration file. See file definition in section 4.29 UI Configuration File Type.                 | Get: No Set: No  | 0x06      | 0x00              | 0x00         | 0x00          |

### Command 0xD801 - Load Firmware File

The host uses this command to send a firmware image file, signed by MagTek, to the device as the first step in updating firmware. The host also uses this command to send a firmware image file, signed by MagTek, to the device as the first step in updating firmware. If the battery charge is five percent or less, a response is returned indicating that the command has not been executed. See \*\*

### [Table 6.74](#table-6-74) - Response Example for Command 0xD801\*\*.

The sequence of events is as follows:

1.  The host is assumed to have access to a binary file containing a firmware image signed by MagTek, which contains a complete instance of **Firmware File Type (MAGTEK INTERNAL ONLY)**.
2.  The host composes a command request in the format below, using the binary file as the **Payload**, and sends it to the device.
3.  The device sends a response to the host in the format below to acknowledge it has received the request. The device will not allow the Load Firmware File command to execute if the battery charge is 5 percent or lower.
4.  The device validates the request and authenticates the firmware file with the algorithm specified in the firmware file payload.

    If the upload was not successful, then go to the next step. If the upload was successful and auto-commit was disabled, then go to the next step. Else, the device will commit the image automatically. If it was successful, the device sends **Notification 0x0905 - Firmware Update Successful** to the host. If it was unsuccessful, the device sends **Notification 0x0906 - Firmware Update Failed**to the host. Commit Firmware Notification Detail Codes are used for auto-commit mode. In both cases, the device automatically resets.

### [Table 6.72](#table-6-72) - Request Data for Command 0xD801 - Load Firmware File

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                                                               | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                                                                   |     |     |         |
| D801 = **Command 0xD801 - Load Firmware File**                                           |     |                                                                                                                                                                                                                                   |     |     |         |
| 81                                                                                       | 01  | Progress Indicator Reserved for future use. Populate with 0x03.                                                                                                                                                                   | B   | R   |         |
| 85                                                                                       | 02  | Image Type 0x0000 = Boot Loader 1 image 0x0001 = Main App image 0x0002 = WiFi Module image 0x0003 = BLE Module image                                                                                                              | B   | R   |         |
| 86                                                                                       | 20  | Hash Checksum This is a SHA-256 hash of the entire object **Firmware File** **Type (MAGTEK INTERNAL ONLY)** being uploaded. For backward compatibility, this TLV is required in Default Mode, it is Optional in Auto-Commit Mode. | B   | R/O |         |
| 87                                                                                       | var | Payload This is the binary file or **Firmware File** **Type (MAGTEK INTERNAL ONLY)** object being loaded into the device.                                                                                                         | B   | R   |         |
| 88                                                                                       | 01  | Load Options 0x00 = Default mode 0x01 = Auto Commit                                                                                                                                                                               | B   | O   | 0x00    |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                                                                                                                                   |     |     |         |

### [Table 6.73](#table-6-73) - Response Data for Command 0xD801 - Load Firmware File

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| D801 = **Command 0xD801 - Load Firmware File**                                            |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.74](#table-6-74) - Response Example for Command 0xD801 Battery Charge State

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 01 D8 01 82 04 80 02 03 16 |

If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**.

### [Table 6.75](#table-6-75) - Request Example

| Example (Hex)                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 01 D8 01 84 83 0C 76 58 D8 01 81 01 03 85 02 00 01 86 20 DF C7 1E 09 A3 CE 8E 86 B0 F5 B6 75 BE B7 7A 0E 82 33 BF F1 8A CD 8F 38 34 B0 DB 20 D9 40 4B 28 87 83 0C 76 28 Plus 0C7628 bytes of firmware Payload, excluded here for brevity. |

### [Table 6.76](#table-6-76) - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 01 D8 01 82 04 00 00 00 00 |

### Command 0xD811 - Start Send File to Device (Secured)

The host uses this command to start sending secured files to the device for storage or processing. It is similar to **Command 0xD812 - Start Send File to Device (Unsecured)**, but is used to send a different subset of file types that impact device security and require some form of authentication from the host. Refer to [Table 6.71](#table-6-71) to determine which file type requires a secure command All files require the command to be authorized via a secure wrapper. In some cases, files include additional signatures within the file structure itself. This command is paired with **Command 0xD821 - Start Get File from Device**, which the host can use to retrieve files. However, some file types are “one way only” and can not be retrieved using that command after the host sends them to the device.

The sequence of events is as follows:

1.  The host uses **Command 0xE001 - Get Challenge** to establish a secure session with the device.
2.  The host determines which file type it will send to the device (see section **6.7.1 About Files**), and either opens an existing file in its file system for reading, or begins constructing it.
3.  The host constructs **Command 0xD811 - Start Send File to Device (Secured)** per [Table 6.77](#table-6-77).
4.  The host constructs **Command 0xEEEE - Send Secured Command to Device** using the previously constructed command as the payload, and sends that command to the device as a **Request Message** to start the process of uploading a file.
    1.  Use **Command 0xEF04 – Load LTPK Protection Key (MAGTEK INTERNAL ONLY FOR NOW)** to gather information about the key to use to secure the message payload(s). Because this command requires a MAC, use key slot 1111.
    2.  Build the **Security Parameters Type** portion of the wrapper with:
        1.  **Security Operation Type** populated with the following values:
            1.  Operation Type = **Command Authorization Using MAC**
            2.  Operation Algorithm = CMAC
            3.  Operation Cipher=AES-256
            4.  Padding = One and zeros
            5.  **MAC Block Size** with any number
        2.  **Key Information Type** populated with the key information gathered earlier.
5.  The device sends a **Response Message** so the host knows it can begin sending the file.
6.  The host sends a **Data File Message** to the device. If the device does not receive file data within a reasonable period of time, it times out and stops listening for the data file.
7.  The device checks to make sure the **File ID** and the length and hash of the File Payload match with the values the host specified in this command.
8.  The device repeats the same **Response Message**, this time with the **Message Reference Number** set to the same value the host used in the **Data File Message**.

### [Table 6.77](#table-6-77) - Request Data for Command 0xD811 - Start Send File to Device (Secured)

| Tag                                                                                      | Len | Value / Description                                                                                                                        | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|--------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                            |     |     |         |
| D811 = **Command 0xD811 - Start Send File to Device (Secured)**                          |     |                                                                                                                                            |     |     |         |
| 81                                                                                       | 04  | File ID from [Table 6.71](#table-6-71)                                                                                                     | B   | R   |         |
| A2                                                                                       | var | File transfer properties                                                                                                                   | T   | R   |         |
| /81                                                                                      | var | Length of File Payload This is the length of the **File Payload** parameter in the **Data File Message** the host sends to the device.     | B   | R   |         |
| /82                                                                                      | 01  | Hash Checksum Type 0x04 = SHA-256                                                                                                          | B   | R   |         |
| /83                                                                                      | 20  | Hash Checksum Anticipated checksum calculated against the **File Payload**, according to the standard specified in **Hash Checksum Type**. | B   | R   |         |
| A3                                                                                       | var | File Description The host should populate this value to help identify the file using **Command 0xD825 - Get File Info from Device**.       | T   | R   |         |
| /81                                                                                      | var | File Name Maximum length 32 bytes Reserved for future use. Leave empty.                                                                    | B   | O   | Null    |
| /82                                                                                      | var | File Label Maximum length 16 bytes Reserved for future use. Leave empty.                                                                   | B   | O   | Null    |
| /83                                                                                      | var | File Version Maximum length 7 bytes Reserved for future use. Leave empty.                                                                  | B   | O   | Null    |
| /84                                                                                      | var | File Date Maximum length 20 bytes Reserved for future use. Leave empty.                                                                    | B   | O   | Null    |
| 87                                                                                       | 01  | Reserved for future use. Leave empty.                                                                                                      | B   | O   | Null    |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                                            |     |     |         |

### [Table 6.78](#table-6-78) - Response Data for Command 0xD811 - Start Send File to Device (Secured)

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| D811 = **Command 0xD811 - Start Send File to Device (Secured)**                           |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**.

**Note: For additional support, please contact MagTek Support.**

### [Table 6.79](#table-6-79) - Request Example

| Example (Hex)                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 04 D8 11 84 81 8F EE EE A1 19 81 05 03 03 06 02 08 84 00 85 00 A8 0A 81 02 11 02 82 00 86 00 88 00 A9 00 82 04 FF FF FF F0 83 08 C9 65 45 F2 97 69 85 B1 84 4E D8 11 81 04 00 00 03 00 A2 2B 81 04 00 00 02 99 82 01 04 83 20 87 A4 B3 54 61 C5 CB D3 1D DC BA 9D 65 25 5A D4 6A 22 FA 51 5E FD 65 87 AF AC A8 8C 4F AF 80 9B A3 14 38 31 30 38 33 30 33 30 33 30 33 30 33 30 33 33 33 30 33 30 87 01 01 9E 10 7D E4 27 C8 A0 70 72 08 19 0A 1E 0A 3F 48 BB F1 |

### [Table 6.71](#table-6-71)0 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 0C D8 11 82 04 00 00 00 00 |

### Command 0xD812 - Start Send File to Device (Unsecured)

The host uses this command to start sending unsecured files to the device for storage or processing. It is similar to **Command 0xD811 - Start Send File to Device (Secured)** but is used to send a different subset of file types that do not impact device security, Refer to [Table 6.71](#table-6-71) to determine which file type can use unsecure command This command is paired with **Command 0xD821 - Start Get File from Device**, which the host can use to retrieve files. However, some file types are “one way only” and can not be retrieved using that command after the host sends them to the device.

The sequence of events is as follows:

1.  The host determines which file type it will send to the device (see section **6.7.1 About Files**), and either opens an existing file in its file system for reading, or begins constructing it.
2.  The host constructs **Command 0xD812 - Start Send File to Device (Unsecured)** per [Table 6.71](#table-6-71)**1**.
3.  The host sends that command to the device as a **Request Message** to start the process of uploading a file.
4.  The device sends a **Response Message** so the host knows it can begin sending the file.
5.  The host sends a **Data File Message** to the device. (MAGTEK INTERNAL ONLY FOR NOW) If the device does not receive file data within a reasonable period of time, it times out and stops listening for the data file.
6.  The device checks to make sure the **File ID** and the length and hash of the **File Payload** match with the values the host specified in this command.
7.  The device repeats the same **Response Message**, this time with the **Message Reference Number** set to the same value the host used in the **Data File Message**.

### [Table 6.71](#table-6-71)1 - Request Data for Command 0xD812 - Start Send File to Device (Unsecured)

| Tag                                                                                      | Len | Value / Description                                                                                                                        | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|--------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                            |     |     |         |
| D812 = **Command 0xD812 - Start Send File to Device (Unsecured)**                        |     |                                                                                                                                            |     |     |         |
| 81                                                                                       | 04  | File ID from [Table 6.71](#table-6-71)                                                                                                     | B   | R   |         |
| A2                                                                                       | var | File transfer properties                                                                                                                   | T   | R   |         |
| /81                                                                                      | var | Length of File Payload This is the length of the **File Payload** parameter in the **Data File Message** the host sends to the device.     | B   | R   |         |
| /82                                                                                      | 01  | Hash Checksum Type 0x04 = SHA-256                                                                                                          | B   | R   |         |
| /83                                                                                      | 20  | Hash Checksum Anticipated checksum calculated against the **File Payload**, according to the standard specified in **Hash Checksum Type**. | B   | R   |         |
| A3                                                                                       | var | File Description The host should populate this value to help identify the file using **Command 0xD825 - Get File Info from Device**.       | T   | R   |         |
| /81                                                                                      | var | File Name Maximum length 32 bytes Reserved for future use. Leave empty.                                                                    | B   | O   | Null    |
| /82                                                                                      | var | File Label Maximum length 16 bytes Reserved for future use. Leave empty.                                                                   | B   | O   | Null    |
| /83                                                                                      | var | File Version Maximum length 7 bytes Reserved for future use. Leave empty.                                                                  | B   | O   | Null    |
| /84                                                                                      | var | File Date Maximum length 20 bytes Reserved for future use. Leave empty.                                                                    | B   | O   | Null    |
| 87                                                                                       | 01  | Reserved for future use. Leave empty.                                                                                                      | B   | O   | Null    |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                                            |     |     |         |

### [Table 6.71](#table-6-71)2 - Response Data for Command 0xD812 - Start Send File to Device (Unsecured)

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| D812 = **Command 0xD812 - Start Send File to Device (Unsecured)**                         |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**.

**Note: For additional support, please contact MagTek Support.**

### [Table 6.71](#table-6-71)3 - Request Example

| Example (Hex)                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 07 D8 12 84 44 D8 12 81 04 02 00 00 00 A2 2B 81 04 00 02 58 38 82 01 04 83 20 D5 B8 BF 2F 3A 15 D9 EE 1D 0D E5 8E DD 68 37 73 18 51 C7 3C 3D 79 58 2B A6 07 90 5C 2B 86 3C E5 A3 0A 81 08 30 32 30 30 30 30 30 30 87 01 01 |

### [Table 6.71](#table-6-71)4 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 07 D8 12 82 04 00 00 00 00 |

### Command 0xD821 - Start Get File from Device

The host uses this command to request a file stored on the device. File types include standard files (images and certificates), MagTek custom files (configuration, firmware), and in some cases even large data blob output (such as signature capture data). In many cases, the files retrieved by this command have been sent by a host previously using **Command 0xD811 - Start Send File to Device (Secured)** or **Command 0xD812 - Start Send File to Device (Unsecured)**. In other cases, such as retrieving signature capture data, the data may originate with the device and the host uses this command to retrieve it. Such data and is not persistent, in the sense that the device does not retain it through power cycles.

The sequence of events is as follows:

1.  The host composes a command request in the format below, and sends it to the device.
2.  The device sends a response in the format below so the host knows it can begin listening for a file message.
3.  The device sends a **Data File Message** to the host. If the host does not receive file data within a reasonable period of time, it should time out and stop listening for the data file.
4.  Upon receiving the end of the **Data File Message**, the host should check to make sure the **File ID**, length, and hash of the **File Payload** in the **Data File Message** match the values the device specified in its response to ensure the file has not been tampered with.

### [Table 6.71](#table-6-71)5 - Request Data for Command 0xD821 - Start Get File from Device

| Tag                                                                                      | Len | Value / Description                                                                              | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|--------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                  |     |     |         |
| D821 = **Command 0xD821 - Start Get File from Device**                                   |     |                                                                                                  |     |     |         |
| 81                                                                                       | 04  | File ID from [Table 6.71](#table-6-71)                                                           | B   | R   |         |
| 87                                                                                       | 01  | Progress indicator behavior (Reserved for future use / Subject to change) 0x00 = None 0x01 = LED | B   | O   | Null    |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                  |     |     |         |

### [Table 6.71](#table-6-71)6 - Response Data for Command 0xD821 - Start Get File from Device

| Tag                                                                                       | Len | Value / Description                                                                                                                          | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                                                                                                                                              |     |     |         |
| D821 = **Command 0xD821 - Start Get File from Device**                                    |     |                                                                                                                                              |     |     |         |
| 81                                                                                        | 04  | File ID from [Table 6.71](#table-6-71)                                                                                                       | B   | R   |         |
| A2                                                                                        | var | File transfer properties                                                                                                                     | T   | R   |         |
| /81                                                                                       | var | Length of File Payload This is the length of the **File Payload** parameter in the **Data File Message** the device sends to the host.       | B   | R   |         |
| /82                                                                                       | 01  | Hash Checksum Type 0x04 = SHA-256                                                                                                            | B   | R   |         |
| /83                                                                                       | 20  | Hash Checksum Anticipated checksum calculated against the **File Payload**, according to the standard specified in **Hash Checksum Type**.   | B   | R   |         |
| A3                                                                                        | var | File Description The values the host populated for convenience when it sent the file to help identify the file. Not all values are required. | T   | R   |         |
| /81                                                                                       | var | File Name Maximum length 32 bytes Reserved for future use.                                                                                   | B   | O   | Null    |
| /82                                                                                       | var | File Label Maximum length 16 bytes Reserved for future use.                                                                                  | B   | O   | Null    |
| /83                                                                                       | var | File Version Maximum length 7 bytes Reserved for future use.                                                                                 | B   | O   | Null    |
| /84                                                                                       | var | File Date Maximum length 20 bytes Reserved for future use.                                                                                   | B   | O   | Null    |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                                                                                                                                              |     |     |         |

If the request started successfully, the Request Status in the message wrapper is **OK, Done.**

### [Table 6.71](#table-6-71)7 - Request Example

| Example (Hex)                                                  |
|----------------------------------------------------------------|
| AA 00 81 04 01 08 D8 21 84 0B D8 21 81 04 00 00 00 01 87 01 01 |

### [Table 6.71](#table-6-71)8 - Response Example

| Example (Hex)                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 82 08 D8 21 82 04 00 00 00 00 84 54 D8 21 81 04 00 00 00 01 A2 2B 81 04 00 00 00 40 82 01 04 83 20 FD EA B9 AC F3 71 03 62 BD 26 58 CD C9 A2 9E 8F 9C 75 7F CF 98 11 60 3A 8C 44 7C D1 D9 15 11 08 A3 1D 81 0B 54 45 53 54 5F 31 4B 2E 62 69 6E 82 05 4C 61 62 65 6C 83 07 31 2E 30 2E 30 2E 31 |

**Note: For additional support, please contact MagTek Support.**

### Command 0xD825 - Get File Info from Device

The host uses this command to request the file information of a file stored on the device. File types include standard files (images and certificates), MagTek custom files (configuration, firmware), and in some cases even large data blob output (such as signature capture data). In many cases, the file information retrieved by this command have been sent by a host previously using **Command 0xD811 - Start Send File to Device (Secured)** or **Command 0xD812 - Start Send File to Device (Unsecured)**. In other cases, such as retrieving file information of signature capture data, the data may originate with the device and the host uses this command to retrieve the information. Such information is not persistent, in the sense that the device does not retain it through power cycles.

The sequence of events is as follows:

1.  The host composes a command request in the format below, and sends it to the device.
2.  The device sends a response in the format below. The response contains the file information.
3.  If the file can not be found, then a response of failure will be sent to the host.

### [Table 6.71](#table-6-71)9 - Request Data for Command 0xD825 - Get File Info from Device

| Tag                                                                                      | Len | Value / Description                    | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|----------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                        |     |     |         |
| D825 = **Command 0xD825 - Get File Info from Device**                                    |     |                                        |     |     |         |
| 81                                                                                       | 04  | File ID from [Table 6.71](#table-6-71) | B   | R   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                        |     |     |         |

### [Table 6.72](#table-6-72)0 - Response Data for Command 0xD825 - Get File Info from Device

| Tag                                                                                       | Len | Value / Description                                                                                                                          | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                                                                                                                                              |     |     |         |
| D825 = **Command 0xD825 - Get File Info from Device**                                     |     |                                                                                                                                              |     |     |         |
| 81                                                                                        | 04  | File ID from [Table 6.71](#table-6-71)                                                                                                       | B   | R   |         |
| A2                                                                                        | var | File transfer properties                                                                                                                     | T   | R   |         |
| /81                                                                                       | var | Length of File This is the length of the file.                                                                                               | B   | R   |         |
| /82                                                                                       | 01  | Hash Checksum Type 0x04 = SHA-256                                                                                                            | B   | R   |         |
| /83                                                                                       | 20  | Hash Checksum Anticipated checksum calculated against the file, according to the standard specified in **Hash Checksum Type**.               | B   | R   |         |
| A3                                                                                        | var | File Description The values the host populated for convenience when it sent the file to help identify the file. Not all values are required. | T   | R   |         |
| /81                                                                                       | var | File Name Maximum length 32 bytes Reserved for future use.                                                                                   | B   | O   | Null    |
| /82                                                                                       | var | File Label Maximum length 16 bytes Reserved for future use.                                                                                  | B   | O   | Null    |
| /83                                                                                       | var | File Version Maximum length 7 bytes Reserved for future use.                                                                                 | B   | O   | Null    |
| /84                                                                                       | var | File Date Maximum length 20 bytes Reserved for future use.                                                                                   | B   | O   | Null    |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                                                                                                                                              |     |     |         |

If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**.

### [Table 6.72](#table-6-72)1 - Request Example

| Example (Hex)                                         |
|-------------------------------------------------------|
| AA 00 81 04 01 08 D8 21 84 08 D8 25 81 04 00 00 00 01 |

### [Table 6.72](#table-6-72)2 - Response Example

| Example (Hex)                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 82 08 D8 25 82 04 00 00 00 00 84 54 D8 25 81 04 00 00 00 01 A2 2B 81 04 00 00 00 40 82 01 04 83 20 FD EA B9 AC F3 71 03 62 BD 26 58 CD C9 A2 9E 8F 9C 75 7F CF 98 11 60 3A 8C 44 7C D1 D9 15 11 08 A3 1D 81 0B 54 45 53 54 5F 31 4B 2E 62 69 6E 82 05 4C 61 62 65 6C 83 07 31 2E 30 2E 30 2E 31 |

**Note: For additional support, please contact MagTek Support.**

### Command 0xD831 – Delete File from Device

The host uses this command to request the deletion of a file stored on the device. File types include

Custom Idle Page Image 1 to 4 in [Table 6.71](#table-6-71)**1**.

The sequence of events is as follows:

1.  The host composes a command request in the format below and sends it to the device.
2.  The device reads and erases the file and sends a response to the host in the format below.
3.  If the file read or the file erase fails, a response of failure will be sent to the host.

### [Table 6.72](#table-6-72)3 - Request Data for Command 0xD831 – Delete File from Device

| Tag                                                                                      | Len | Value / Description                    | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|----------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                        |     |     |         |
| D831 = **Command 0xD831 – Delete File from Device**                                      |     |                                        |     |     |         |
| 81                                                                                       | 04  | File ID from [Table 6.71](#table-6-71) | B   | R   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                        |     |     |         |

### [Table 6.72](#table-6-72)4 - Response Data for Command 0xD831 – Delete File from Device

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| D831 = **Command 0xD831 – Delete File from Device**                                       |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.72](#table-6-72)5 - Request Example

| Example (Hex)                                         |
|-------------------------------------------------------|
| AA 00 81 04 01 05 D8 31 84 08 D8 31 81 04 02 00 00 00 |

### [Table 6.72](#table-6-72)6 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 05 D8 31 82 04 00 00 00 00 |

## Command Group 0xD9nn - Process Files

### Command 0xD901 - Commit Firmware from File

The host uses this command to commit a file previously uploaded using **Command 0xD801 - Load Firmware File** into the device’s permanent memory after the device has authenticated the file.

The sequence of events is as follows:

1.  The host composes a command request in the format below, and sends it to the device.
2.  The device sends a response in the format below.
3.  The device writes the image file to permanent storage.
4.  If the commit operation was successful, the device sends **Notification 0x0905 - Firmware Update Successful** to the host. If the commit operation was not successful, the device sends **Notification 0x0906 - Firmware Update Failed** to the host. In both cases, the device automatically resets.

### [Table 6.81](#table-6-81) - Request Data for Command 0xD901 - Commit Firmware from File

| Tag                                                                                      | Len | Value / Description                                                                                                     | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                         |     |     |         |
| D901 = **Command 0xD901 - Commit Firmware from File**                                    |     |                                                                                                                         |     |     |         |
| 81                                                                                       | 01  | Progress Indicator Reserved for future use. Populate with 0x03.                                                         | B   | R   |         |
| 82                                                                                       | 01  | Operation Options Reserved for future use. Populate with 0x00.                                                          | B   | R   |         |
| 85                                                                                       | 02  | Image Type 0x0000 = Boot Loader 1 image 0x0001 = Main App image 0x0002 = WiFi Module image 0x0003 = BLE Module image    | B   | R   |         |
| 86                                                                                       | 20  | Hash Checksum This is a SHA-256 hash of the entire **Firmware File Type (MAGTEK INTERNAL ONLY)** object being uploaded. | B   | R   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                         |     |     |         |

### [Table 6.82](#table-6-82) - Response Data for Command 0xD901 - Commit Firmware from File

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| D901 = **Command 0xD901 - Commit Firmware from File**                                     |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**.

### [Table 6.83](#table-6-83) - Request Example

| Example (Hex)                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 02 D9 01 84 2E D9 01 81 01 03 82 01 00 85 02 00 01 86 20 DF C7 1E 09 A3 CE 8E 86 B0 F5 B6 75 BE B7 7A 0E 82 33 BF F1 8A CD 8F 38 34 B0 DB 20 D9 40 4B 28 |

### [Table 6.84](#table-6-84) - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 02 D9 01 82 04 00 00 00 00 |

### [Table 6.85](#table-6-85) - Notification Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 83 00 09 05 82 04 08 01 0A 03 |

**Note: For additional support, please contact MagTek Support.**

## Command Group 0xDFnn - Diagnostics and Utilities

### Command 0xDF01 - Echo

The host uses this command to prompt the device for a response that contains the same payload it sent.

The sequence of events is as follows:

1.  The host constructs the command request for **Command 0xDF01 - Echo** in the format below, populating any of the available parameters with any data. The total length of data to be echoed across all parameters must not exceed 128 bytes.
2.  The host sends the command request to the device.
3.  The device sends a command response in the format below to the host, echoing back the exact parameters the host sent in the command request.

### [Table 6.91](#table-6-91) - Request Data for Command 0xDF01 - Echo

| Tag                                                                                      | Len | Value / Description | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                     |     |     |         |
| DF01 = **Command 0xDF01 - Echo**                                                         |     |                     |     |     |         |
| 81                                                                                       | var | Data to be echoed   | B   | O   |         |
| 82                                                                                       | var | Data to be echoed   | B   | O   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                     |     |     |         |

### [Table 6.92](#table-6-92) - Response Data for Command 0xDF01 - Echo

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| DF01 = **Command 0xDF01 - Echo**                                                          |     |                     |     |     |         |
| 81                                                                                        | var | Data being echoed   | B   | O   |         |
| 82                                                                                        | var | Data being echoed   | B   | O   |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.93](#table-6-93) - Request Example

| Example (Hex)                                      |
|----------------------------------------------------|
| AA 00 81 04 01 01 DF 01 84 07 DF 01 81 03 01 02 03 |

### [Table 6.94](#table-6-94) - Response Example

| Example (Hex)                                                        |
|----------------------------------------------------------------------|
| AA 00 81 04 82 01 DF 01 82 04 00 00 00 00 84 07 DF 01 81 03 01 02 03 |

### Command 0xDF02 - Convert Binary Tag Data to Text (MAGTEK INTERNAL ONLY FOR NOW)

Reserved for future use per Dave.

## Command Group 0xEnnn - Security

### Command 0xE001 - Get Challenge

The host uses this command to request challenge data from the device, which the host can then use to perform a specific sensitive operation / modify a specific type of device setting. Information about how the host should pass the required challenge data to the device is included in the documentation for all commands that use this security mechanism.

The sequence of events is as follows:

1.  The host already wants to perform a secured operation that requires a challenge [for example **Command 0xEEEE - Send Secured Command to Device**].
2.  The host constructs the command request for **Command 0xE001 - Get Challenge** in the format below.
3.  The host sends the command request to the device.
4.  The device generates a random number for the challenge, stores it locally, and sends a response in the format below to the host.
5.  The device starts a 5 minute countdown timer during which the challenge is valid. If the host takes no action within 5 minutes, the timer expires, the device erases the challenge data, and the device must retrieve a fresh challenge to perform the operation it wants to perform. This binding of the command to a specific time period allows the device to detect and reject commands that have been captured/intercepted at one point in time and replayed later.

### [Table 6.101](#table-6-101) - Request Data for Command 0xE001 - Get Challenge

| Tag                                                                                      | Len | Value / Description        | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|----------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                            |     |     |         |
| E001 = **Command 0xE001 - Get Challenge**                                                |     |                            |     |     |         |
| 81                                                                                       | 02  | Request ID to be protected | B   | R   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                            |     |     |         |

### [Table 6.102](#table-6-102) - Response Data for Command 0xE001 - Get ChallengeGet Challenge

| Tag                                                                                       | Len | Value / Description                                                                                                                                                                                                                                                     | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                                                                                                                                                                                                                                                                         |     |     |         |
| E001 = **Command 0xE001 - Get Challenge**                                                 |     |                                                                                                                                                                                                                                                                         |     |     |         |
| 81                                                                                        | 02  | Request ID to be protected                                                                                                                                                                                                                                              | B   | R   |         |
| 82                                                                                        | 04  | Device Serial Number                                                                                                                                                                                                                                                    | B   | R   |         |
| 83                                                                                        | 08  | Challenge Token A challenge token includes 8 byte random numbers and must be used within 5 minutes of being issued. Only one token can be active at a time. Attempts to use a token for requests other than the one specified will cause the token to be revoked/erased | B   | R   |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                                                                                                                                                                                                                                                                         |     |     |         |

### [Table 6.103](#table-6-103) - Request Example

| Example (Hex)                                   |
|-------------------------------------------------|
| AA 00 81 04 01 13 E0 01 84 06 E0 01 81 02 F0 12 |

### [Table 6.104](#table-6-104) - Response Example

| Example (Hex)                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 82 13 E0 01 82 04 00 00 00 00 84 16 A2 14 81 02 E0 01 82 04 B5 03 3D A0 83 08 3B 4F A0 62 69 BB 73 38 |

### Command 0xEEEE - Send Secured Command to Device

The host uses this command to transmit another command securely. This “secure wrapper” mechanism provides the device a means to ensure the wrapped command originated from an authentic, authorized host. In addition, its implementation includes an operation that starts a countdown timer, which ensures the command is current and is not an unauthorized replay of a previously intercepted / stored command. This command can use multiple authentication methods, including MAC or ECDSA Signature. The method and parameters to use are specific to the command being wrapped, and are specified in the documentation for that command.

The sequence of events is as follows:

1.  The host determines what command it wants to call from section **6 Commands**, determines the command must be secured, and uses the Request Data table for that command to compose **Message Payload**.
2.  The host uses **Command 0xE001 - Get Challenge** to retrieve a **Challenge Token** and unlock the device for receiving the desired command for a limited period of time. When the time expires, the device will no longer accept the Challenge Token and the host will have to retrieve another one.
3.  The host creates an instance of **Command 0xEEEE - Send Secured Command to Device** in the format below, and includes the Message Payload and Challenge Token inside it. In the **Request Message**, it fills in **Command ID** as the command number of the wrapped Message Payload, instead of 0xEEEE. Some parameters are command-specific; see the documentation for the command that is being wrapped to determine what values to use.
4.  The host sends the resulting composite command request to the device.
5.  The device validates the serial number and challenge token, then examines the parameters to determine which authentication method is being used, and authenticates the command accordingly.
6.  If the device determines the command request is authentic, it will start executing the secure command defined by the Message Payload.
7.  The device sends a response to the host reporting success or failure. In both cases, the response uses the format that corresponds to the command invoked by the Message Payload. See the documentation for that command to determine the format of the response.

### [Table 6.105](#table-6-105) - Request Data for Command 0xEEEE - Send Secured Command to Device

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                                                                                                               | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                                                                                                                   |     |     |         |
| EEEE = **Command 0xEEEE - Send Secured Command to Device**                               |     |                                                                                                                                                                                                                                                                                   |     |     |         |
| A1                                                                                       | var | Security Parameters This parameter describes how the Signature parameter in this data object is calculated, and is a **Security Parameters Type** TLV data object. To determine which values to use in that TLV data object, see the documentation for the command being wrapped. | T   | R   |         |
| 82                                                                                       | 04  | Serial Number                                                                                                                                                                                                                                                                     | B   | R   |         |
| 83                                                                                       | 08  | Challenge Token The token the device returned when the host called **Command 0xE001 - Get Challenge**.                                                                                                                                                                            | B   | R   |         |
| 84                                                                                       | var | Message Payload                                                                                                                                                                                                                                                                   | B   | R   |         |
| 9E                                                                                       | var | MAC or Signature                                                                                                                                                                                                                                                                  | B   | R   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                                                                                                                                                                                   |     |     |         |

### [Table 6.106](#table-6-106) - Request Example Using MAC

| Example (Hex)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| This example wraps **Command 0xD811 - Start Send File to Device (Secured)**. AA 00 81 04 01 04 D8 11 84 81 8F EE EE A1 19 81 05 03 03 06 02 08 84 00 85 00 A8 0A 81 02 11 02 82 00 86 00 88 00 A9 00 82 04 FF FF FF F0 83 08 C9 65 45 F2 97 69 85 B1 84 4E D8 11 81 04 00 00 03 00 A2 2B 81 04 00 00 02 99 82 01 04 83 20 87 A4 B3 54 61 C5 CB D3 1D DC BA 9D 65 25 5A D4 6A 22 FA 51 5E FD 65 87 AF AC A8 8C 4F AF 80 9B A3 14 38 31 30 38 33 30 33 30 33 30 33 30 33 30 33 33 33 30 33 30 87 01 01 9E 10 7D E4 27 C8 A0 70 72 08 19 0A 1E 0A 3F 48 BB F1 |

### [Table 6.107](#table-6-107) - Request Example Using ECDSA

| Example (Hex)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| This example wraps **Command 0xF015 - Read Log & Clear Tamper (MAGTEK INTERNAL ONLY)**: AA 00 // Marker 81 04 01 0F F0 15 // Message Information 84 81 C8 // Request Payload EE EE // 0xEEEE, Secure Wrapper A1 24 // P4-A1, Security Parameters 81 04 02 01 04 05 // 02=Cmd Auth-sign, 01=ECDSA, 04=SHA-256, 05=P-521 84 00 // Data (for IV, nonce, as needed) 85 00 // Extra data item (reserved for future use) A8 16 // Key Info 81 02 00 00 // Key Slot ID 82 07 45 43 43 53 49 47 4E // Key Label, “ECCSIGN” 86 05 45 43 44 53 41 // KSN or derive info, ECDSA 88 00 // Added Info A9 00 // 2nd Key Info (reserved for future use) 82 04 B5 03 3D A0 // P4-P2, Device Serial Number 83 08 5B 6B 45 4B 00 5B CE 31 // P4-P3, Challenge Token 84 02 F0 15 // P4-P4, Payload Command 0xF015 9E 81 89 // P4-P30, Signature for Secure Wrapper 30 81 86 02 41 // Sig-\>R 52 5B 04 9A C7 CC 56 DE 5A EA 89 62 47 BB B8 0D 93 80 CE C8 AD 6E 16 F7 6E DA 08 42 0B 9C 69 77 61 B0 99 FC 05 7D AE AF 75 79 9C 7B B3 81 72 5C 4E 5B 92 DC F3 B6 85 5E B3 A2 71 0D 1D 93 B5 0D 0C 02 41 // Sig-\>S 46 47 0A EF 6F D5 97 ED 4F 41 E8 3C FD 20 A1 CE 7D E5 CA D3 E8 22 3B ED BC 2A 8A A0 BF 73 72 81 35 4F CB 52 B6 A9 07 6F 36 7F 5D 35 D5 29 3D 5D 78 17 0E B2 D6 AA A5 0D B3 4D B9 04 2C 03 6A AC A5 |

**Note: For additional support, please contact MagTek Support.**

### Command 0xEF01 - Load Key Using TR-31

The host uses this command to load a key into one of several available slots in the device’s secure memory.

### [Table 6.108](#table-6-108) - Device Key ID / Slot

| **ID** | **Label** | **Description**                   | **Load TK** |
|--------|-----------|-----------------------------------|-------------|
| 1000   | TMPTK     | Temporary KBPK                    | agree       |
| 1001   | MTK       | Master Transport                  | TMPTK       |
| 1002   | DEVTK     | Device Master                     | MTK         |
| 1003   | FINTK     | Financial Master                  | MTK         |
| 1021   | PRODTK    | Production - MagTek Internal Only | DEVTK       |
| 1022   | MFGTK     | MagTek Only Internal/External     | DEVTK       |
| 1081   | MKIFTK    | MagTek KIF Financial Keys         | FINTK       |
| 1101   | FREQMK    | Factory Request MAC               | PRODTK      |
| 1102   | MREQMK    | Mfg Device Request MAC            | MFGTK       |
| 1111   | MFRQMK    | Mfg Financial Request MAC         | MKIFTK      |
| 20xx   | DKPTM0-1F | MagTek DUKPT Initial Key          | MKIFTK      |

To inject a specific key in the above table, the corresponding Load TK shall be injected previously

As shown in the table, MTK injection requires that a TMPTK has been created. See **Command 0xF017 - Establish Ephemeral KBPK**.

After MTK has been injected successfully, the sequence of injecting other keys is as follows:

1.  The host uses **Command 0xE001 - Get Challenge** to establish a secure session with the device.
2.  The host constructs a TR-31 (X9.143) key block for the key it is going to load. (Note that the Load Key must be injected previously.)
3.  The host constructs the command request for **Command 0xEF01 - Load Key Using TR-31** in the format below.
4.  The host sends the command request to the device.
5.  The device sends a response in the format below to the host.

### [Table 6.109](#table-6-109) - Request Data for Command 0xEF01 - Load Key Using TR-31

| Tag                                                                                      | Len | Value / Description                                              | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                  |     |     |         |
| EF01 = **Command 0xEF01 - Load Key Using TR-31**                                         |     |                                                                  |     |     |         |
| 84                                                                                       | var | Key Block This is a populated, secured **TR-31 Key Block Type**. | B   | R   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                  |     |     |         |

### [Table 6.101](#table-6-101)0 - Response Data for Command 0xEF01 - Load Key Using TR-31

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| EF01 = **Command 0xEF01 - Load Key Using TR-31**                                          |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.101](#table-6-101)1 - Request Example

| Example (Hex)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 1A EF 01 84 82 01 36 EF 01 84 82 01 30 44 30 33 30 34 42 31 54 58 30 30 4E 30 36 30 30 49 4B 31 38 46 46 46 46 39 38 37 36 35 34 33 32 31 30 33 30 30 30 30 30 32 31 35 38 4D 47 54 4B 31 30 30 31 54 31 31 30 34 32 30 30 37 31 32 30 34 31 30 38 31 32 31 30 34 30 30 33 46 33 31 30 37 42 35 30 41 46 44 32 33 32 31 30 43 39 33 36 31 39 44 44 41 41 32 31 33 36 43 37 33 33 31 30 32 30 32 30 31 32 30 34 54 31 37 31 36 33 30 5A 4B 50 30 45 30 31 39 33 36 46 41 33 32 45 4B 43 30 41 30 30 34 35 30 30 54 53 31 34 32 30 32 30 30 39 30 32 54 31 35 35 38 30 32 5A 50 42 30 34 35 37 32 31 37 46 33 34 37 31 34 43 32 42 38 38 46 33 39 35 35 32 32 32 46 46 35 39 41 41 30 35 37 44 39 39 41 46 38 32 41 37 35 37 32 46 39 33 38 46 38 33 38 42 43 36 35 45 45 35 34 46 39 34 37 46 35 39 41 30 36 43 44 34 35 35 31 39 32 32 37 41 32 35 35 43 37 44 35 44 37 43 38 36 37 34 35 30 33 46 41 43 36 46 41 37 31 33 32 43 38 46 41 39 39 36 42 34 45 42 36 41 41 31 31 34 46 45 |

### [Table 6.101](#table-6-101)2 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 1A EF 01 82 04 00 00 00 00 |

**Note: For additional support, please contact MagTek Support.**

### Command 0xEF02 – Generate CSR keys (WLAN Only)

The host uses this command to generate a key pair to be used for a certificate signing request (CSR). The key pair generated will be 256 bit elliptic-curve (EC) keys. The key pair generated will be saved to non-volatile memory in the device and will overwrite any existing CSR key pair. The key pair will persist in non-volatile memory associated with a CSR until it is either overwritten or until a leaf certificate is loaded into the device with **Command 0xD811 - Start Send File to Device (Secured)** that contains a public key that matches the key pair at which point the key pair will be associated with that certificate instead of a CSR.

The sequence of events is as follows:

1.  The host constructs the command request in the format below and sends it to the device.
2.  The device sends a response in the format below to the host to indicate that key pair generation has been started.
3.  Once the device finishes generating the key pair, it will send **Notification 0x1001 - Device Information Update** with the category set to key management and the reason set to CSR keys generated to indicate that the key pair generation process has completed. The device typically takes around a second or two to generate a 256 bit EC key pair. If this command is extended in the future to support 2048 bit RSA keys, then it will take an average of 30 seconds and sometimes much longer to generate the RSA keys. That is why a notification is used to indicate that the key pair has been generated instead of a command response that indicates that it is complete.
4.  The host will typically send **Command 0xEF03 – Generate CSR (WLAN Only)** as the next step. See this command for more detail and more potential steps.

### [Table 6.101](#table-6-101)3 - Request Data for Command 0xEF02 – Generate CSR keys (WLAN Only)

| Tag                                                                                      | Len | Value / Description | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                     |     |     |         |
| EF02 = **Command 0xEF02 – Generate CSR keys (WLAN Only)**                                |     |                     |     |     |         |
| No parameters.                                                                           |     |                     |     |     |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                     |     |     |         |

### [Table 6.101](#table-6-101)4 - Response Data for Command 0xEF02 – Generate CSR keys (WLAN Only)

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| EF02 = **Command 0xEF02 – Generate CSR keys (WLAN Only)**                                 |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.101](#table-6-101)5 - Request Example

| Example (Hex)                  |
|--------------------------------|
| AA00 81 04 0155EF02 84 02 EF02 |

### [Table 6.101](#table-6-101)6 - Response Example

| Example (Hex)                                 |
|-----------------------------------------------|
| AA00 81 04 8205EF02 82 04 01000000 84 02 EF02 |

### Command 0xEF03 – Generate CSR (WLAN Only)

The host uses this command to generate a certificate signing request (CSR) in PEM format. The CSR generated will be saved to volatile memory in the device and will overwrite any existing CSR. The CSR will persist in volatile memory until it is overwritten, fetched with **Command 0xD821 - Start Get File from Device** or the device is power cycled or reset.

The sequence of events is as follows:

1.  The host will use **Command 0xEF02 – Generate CSR keys (WLAN Only)** if it wants generate a CSR using a new CSR key pair.
2.  The host constructs the command request in the format below and sends it to the device.
3.  The device sends a response in the format below to the host to indicate that CSR generation has completed.
4.  The host fetches the CSR with **Command 0xD821 - Start Get File from Device.**
5.  The CSR is used to create a certificate.
6.  The host loads the certificate into the device with **Command 0xD811 - Start Send File to Device (Secured)**.

### [Table 6.101](#table-6-101)7 - Request Data for Command 0xEF03 – Generate CSR (WLAN Only)

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Typ | Req | Default                                                                                                                          |
|------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|----------------------------------------------------------------------------------------------------------------------------------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |     |     |                                                                                                                                  |
| EF03 = **Command 0xEF03 – Generate CSR (WLAN Only)**                                     |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |     |     |                                                                                                                                  |
| 81                                                                                       | 1   | Key Identifier The key identifier to use to generate the CSR. The key pair associated with the identifier must already be present in the device for the command to succeed. 0 = CSR keys 1 = Apollo server cert keys 2 = Customer server cert keys 3 = Commercial server cert keys 4 = Apollo client cert keys                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | B   | O   | 0                                                                                                                                |
| 82                                                                                       | var | Subject Including this optional parameter will override the default subject. This parameter should contain a null terminated string. This string should contain a list of attributes separated by commas. If an attribute’s value contains a comma, the comma should be replaced with “\\\\,” Each attribute value should be prefixed with its attribute name followed by “=”. The following is a list of valid attribute names. "CN" "commonName" "C" "countryName” "O" "organizationName" “L” “locality” "R" “OU” "organizationalUnitName" “ST” "stateOrProvinceName" "emailAddress" "serialNumber" “postalAddress” "postalCode" “dnQualifier” "title" “surname” "SN" “givenName” "GN" “initials” "pseudonym" "generationQualifier" “domainComponent” "DC" “O=MagTek Inc,CN= test1.com” is an example with two attributes. | B   | O   | “serialNumber=XXXXXXX,CN=df-xxxxxxx” where XXXXXXX is **Property 2.2.1.1.1.1 Serial Number** and so is xxxxxxx but in lower case |
| 83                                                                                       | var | Subject Alternative Names Including this optional parameter will override the default subject alternative names. This parameter should contain a null terminated string. Only DNS names and IP addresses are supported and only a maximum of two each. DNS names must be prefixed with “DNS=” and IP addresses must be prefixed with “IPA=”. All Subject Alternative Names Must be separated with a comma and not spaces. Subject Alternative Names may not be ordered in the CSR the same as they are ordered here. "DNS=test1.com,DNS=test2.,IPA=1.10.16.255,IPA=2.10.16.254" is an example.                                                                                                                                                                                                                               | B   | O   | “DNS=df-xxxxxxx,IPA=192.168.0.1” where xxxxxxx is **Property 2.2.1.1.1.1 Serial Number** but in lower case                       |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |     |     |                                                                                                                                  |

### [Table 6.101](#table-6-101)8 - Response Data for Command 0xEF03 – Generate CSR (WLAN Only)

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| EF03 = **Command 0xEF03 – Generate CSR (WLAN Only)**                                      |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.101](#table-6-101)9 - Request Example

| Example (Hex)                  |
|--------------------------------|
| AA00 81 04 0155EF03 84 02 EF03 |

### [Table 6.102](#table-6-102)0 - Response Example

| Example (Hex)                                 |
|-----------------------------------------------|
| AA00 81 04 8255EF03 82 04 00000000 84 02 EF03 |

### Command 0xEF04 – Load LTPK Protection Key (MAGTEK INTERNAL ONLY FOR NOW)

The sequence of events is as follows:

1.  The hose uses **Command 0xE001 - Get Challenge** to establish a secure session with the device.
2.  The host determines which file type it will send to the device (See section **6.7.1** About files) and either opens an existing file in its file system for reading or begins constructing it.
3.  The host constructs **Command 0xD811 - Start Send File to Device (Secured)** per [Table 6.77](#table-6-77).
4.  The host constructs **Command 0xEEEE - Send Secured Command to Device** using the previously constructed command as the payload, and send that command to the device as a Request Message to start the process of uploading a file.
    1.  Use **Command 0xEF04 – Load LTPK Protection Key (MAGTEK INTERNAL ONLY FOR NOW)**

The host uses this command to load the 256-bit AES LTPK protection key. The key is encrypted and

MAC’d with the DKEK and DKMK respectively before saving it through KPM. This key can be loaded

at the factory or the customer’s secure site before deployment.

The sequence of events is as follows:

1.  The host composes a command request in the format below, and sends it to the device.
2.  The device reads the Action, if Action == 0, the device will check and return the key status. If Action == 1, the device will verify the CRC-checksum and then save the key through KPM.
3.  If the key status read, key verify or key save fails, then a response of failure will be sent to the host.

### [Table 6.102](#table-6-102)1 - Request Data for Command 0xEF04 – Load LTPK Protection Key (MAGTEK INTERNAL ONLY FOR NOW)

| Tag                                                                                      | Len | Value / Description                                                                                            | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **56** |     |                                                                                                                |     |     |         |
| EF04 = **Command 0xEF04 – Load LTPK Protection Key (MAGTEK INTERNAL ONLY FOR NOW)**      |     |                                                                                                                |     |     |         |
| 81                                                                                       | 1   | Action 0 = Check key status. 1 = Load key. If Action==0, ignore the TLVs below.                                | B   | R   |         |
| 82                                                                                       | 20  | AES-256 Key 32 bytes of key.                                                                                   | B   | R   |         |
| 83                                                                                       | 2   | CRC-16-CCITT Checksum Polynomial X16 + X12 + X5 + 1, initial value=0xFFFF. 2-byte checksum of the 32-byte key. | B   | R   |         |
| End of any wrappers, at minimum including **Request Message** found on page **56**       |     |                                                                                                                |     |     |         |

### [Table 6.102](#table-6-102)2 - Response Data for Command 0xEF04 – Load LTPK Protection Key (MAGTEK INTERNAL ONLY FOR NOW)

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **57** |     |                     |     |     |         |
| EF04 = **Command 0xEF04 – Load LTPK Protection Key (MAGTEK INTERNAL ONLY FOR NOW)**       |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **57**       |     |                     |     |     |         |

### [Table 6.102](#table-6-102)3 - Request Example

| Example (Hex)                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 06 EF 04 84 2B EF 04 81 01 01 82 20 22 F0 66 59 0B DA 04 F7 B9 99 B6 B4 B4 BC 2E 0D 95 92 C2 7A B1 55 98 2A 31 D3 06 CC E6 6B CF 85 83 02 84 99 |

### [Table 6.102](#table-6-102)4 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 06 EF 04 82 04 00 00 00 00 |

### Command 0xEF05 – Load Encrypted LTPK and Version (MAGTEK INTERNAL ONLY FOR NOW)

The host uses this command to load the encrypted LTPK and Version. The data will first be decrypted

using the LTPK protection key, then encrypted and MAC’d with the DKEK and DKMK respectively

before saving it through KPM.

The sequence of events is as follows:

1.  The host composes a command request in the format below, and sends it to the device.
2.  The device reads the Action, if Action == 0, the device will check and return the key status.

If Action == 1, the device will verify the CRC, decrypt and then save the key through KPM.

3.  If the key status read, key verify or key save fails, then a response of failure will be sent to the host.

### [Table 6.102](#table-6-102)5 - Request Data for Command 0xEF05 – Load Encrypted LTPK and Version (MAGTEK INTERNAL ONLY FOR NOW)

| Tag                                                                                                                       | Len | Value / Description                                                                                              | Typ | Req | Default |
|---------------------------------------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **56**                                  |     |                                                                                                                  |     |     |         |
| EF05 = **Command 0xEF05 – Load Encrypted LTPK and Version (MAGTEK INTERNAL ONLY FOR NOW)Load Encrypted LTPK and Version** |     |                                                                                                                  |     |     |         |
| 81                                                                                                                        | 1   | Action 0 = Check key status. 1 = Load key. If Action==0, ignore the TLVs below.                                  | B   | R   |         |
| 82                                                                                                                        | 4   | Key Version 00 00 00 01=0x00000001.                                                                              | B   | R   |         |
| 83                                                                                                                        | 2   | Raw Key Length (before the padding & encryption) 01 23=0x0123 bytes.                                             | B   | R   |         |
| 85                                                                                                                        | var | Encrypted Key Length The length of the encrypted LTPK shall be 16-byte aligned.                                  | B   | R   |         |
| 86                                                                                                                        | 2   | CRC-16-CCITT Checksum Polynomial X16 + X12 + X5 + 1, initial value=0xFFFF. 2-byte checksum of the encrypted key. | B   | R   |         |
| End of any wrappers, at minimum including **Request Message** found on page **56**                                        |     |                                                                                                                  |     |     |         |

### [Table 6.102](#table-6-102)6 - Response Data for Command 0xEF05 – Load Encrypted LTPK and Version (MAGTEK INTERNAL ONLY FOR NOW)

| Tag                                                                                        | Len | Value / Description | Typ | Req | Default |
|--------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **57**  |     |                     |     |     |         |
| EF05 = **Command 0xEF05 – Load Encrypted LTPK and Version (MAGTEK INTERNAL ONLY FOR NOW)** |     |                     |     |     |         |
| 81                                                                                         | 4   | LTPK Key Version    | B   | R   |         |
| End of any wrappers, at minimum including **Response Message** found on page **57**        |     |                     |     |     |         |

### [Table 6.102](#table-6-102)7 - Request Example

| Example (Hex)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 07 EF 05 84 81 96 EF 05 81 01 01 82 04 00 00 00 02 83 02 00 79 85 81 80 A1 9A 2D F7 B9 99 57 9B 89 5E 58 1B AD 26 52 77 EB B8 AC 6F 6A BE A8 21 D6 38 0D 54 0B 24 65 F4 EC D4 1D 73 E1 5A BE 9F 13 6B 85 DD 96 60 FD 33 6C 23 15 14 0B 53 AC FF EF 1C 1B 22 BD 56 D7 86 6D 82 D4 E0 E6 0B F5 07 E6 5D A5 EF C2 89 A1 33 28 E1 C7 D2 00 7C 8C B8 C5 D5 F9 5B D7 4F ED BB 40 9F 10 1D 43 08 97 5B 4A 1F D4 50 EB 2B 73 82 C9 C9 6C 4C 9C BC 05 F0 74 11 3E 7E 9C 60 02 DC 86 02 69 DF |

### [Table 6.102](#table-6-102)8 - Response Example

| Example (Hex)                                                           |
|-------------------------------------------------------------------------|
| AA 00 81 04 82 07 EF 05 82 04 00 00 00 00 84 08 EF 05 81 04 00 00 00 02 |

### Command 0xEF06 – Change Device Lock State

The host can use this command to change the device’s lock state. To get the device’s lock state or to set it using MagTek security see **Property 1.2.5.2.1.1 Device Lock State**. The value of the device lock state will revert to the value of **Property 1.2.5.2.1.2 Device Lock State After Reset** after a reset or a power cycle. See **Device Lock Feature** for more information.

### [Table 6.102](#table-6-102)9 - Request Data for Command 0xEF06 – Change Device Lock State

| Tag                                                                                      | Len   | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **56** |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |     |     |         |
| EF06 = **Command 0xEF06 – Change Device Lock State**                                     |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |     |     |         |
| 81                                                                                       | 01    | Device Lock State 0x00 = Unlocked 0x01 = Locked                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | B   | M   |         |
| 82                                                                                       | 01    | Passcode Format 0x00 = Clear 0x01 = Fixed SHA-256 0x02 = Variable SHA-256                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | B   | M   |         |
| 83                                                                                       | 04-63 | Passcode The value of the passcode depends on the value of the passcode format parameter. If the passcode format is set to clear, then the value of the passcode is the passcode in the clear and can have a length of 4-63 bytes. If the passcode format is set to fixed SHA-256, then the value of the passcode is the 32 byte SHA-256 hash value of the passcode. If the passcode format is set to variable SHA-256, then the value of the passcode is the 32 byte SHA-256 hash value of a 8 byte random challenge token followed by the 4-63 byte passcode. The challenge token must have been retrieved from the device within the last 5 minutes using Command 0xE001 - Get Challenge. | B   | M   |         |
| End of any wrappers, at minimum including **Request Message** found on page **56**       |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |     |     |         |

### [Table 6.103](#table-6-103)0 - Response Data for Command 0xEF06 – Change Device Lock State

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **57** |     |                     |     |     |         |
| EF06 = **Command 0xEF06 – Change Device Lock State**                                      |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **57**       |     |                     |     |     |         |

### [Table 6.103](#table-6-103)1 - Request Example

| Example (Hex)                                              |
|------------------------------------------------------------|
| AA00 81 04 0155EF06 84 0E EF06 810100 820100 8304 34333231 |

### [Table 6.103](#table-6-103)2 - Response Example

| Example (Hex)                           |
|-----------------------------------------|
| AA00 81048255EF06 820400000000 8402EF06 |

### Command 0xEF07 – Change Device Lock Passcode

The host can use this command to change the device’s lock passcode. The value of the device lock passcode is stored in non-volatile memory so changes made to it will persist after the device is reset or power cycled. To change the device lock passcode using MagTek security or to see its default value see **Property 1.2.5.2.1.3 Device Lock Passcode**. See **Device Lock Feature** for more information.

### [Table 6.103](#table-6-103)3 - Request Data for Command 0xEF07 – Change Device Lock Passcode

| Tag                                                                                      | Len   | Value / Description                                                                                                             | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-------|---------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **56** |       |                                                                                                                                 |     |     |         |
| EF07 = Command **0xEF07 – Change Device Lock Passcode**                                  |       |                                                                                                                                 |     |     |         |
| 81                                                                                       | 4-63  | Current Passcode The current passcode in the clear. This must match the value of the current passcode or the command will fail. | B   | M   |         |
| 82                                                                                       | 04-63 | New Passcode The new passcode in the clear. It can only contain any printable ASCII character or the command will fail.         | B   | M   |         |
| End of any wrappers, at minimum including **Request Message** found on page **56**       |       |                                                                                                                                 |     |     |         |

### [Table 6.103](#table-6-103)4 - Response Data for Command 0xEF07 – Change Device Lock Passcode

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **57** |     |                     |     |     |         |
| EF07 = Command **0xEF07 – Change Device Lock Passcode**                                   |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **57**       |     |                     |     |     |         |

### [Table 6.103](#table-6-103)5 - Request Example

| Example (Hex)                                            |
|----------------------------------------------------------|
| AA00 81 04 0155EF07 84 0E EF07 810434333231 820434333231 |

### [Table 6.103](#table-6-103)6 - Response Example

| Example (Hex)                           |
|-----------------------------------------|
| AA00 81048255EF07 820400000000 8402EF07 |

### Command 0xEF08 – Reset Device Lock Passcode (MAGTEK INTERNAL ONLY FOR NOW)

The host can use this command to reset the device’s lock passcode to its default value. The value of the device lock passcode is stored in non-volatile memory so changes made to it will persist after the device is reset or power cycled. To change the device lock passcode using MagTek security or to see its default value see **Property 1.2.5.2.1.3 Device Lock Passcode**. See **Device Lock Feature** for more information.

### [Table 6.103](#table-6-103)7 - Request Data for Command 0xEF08 – Reset Device Lock Passcode (MAGTEK INTERNAL ONLY FOR NOW)

| Tag                                                                                      | Len | Value / Description                                                              | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **56** |     |                                                                                  |     |     |         |
| EF08 = Command **0xEF08 – Reset Device Lock Passcode (MAGTEK INTERNAL ONLY FOR NOW)**    |     |                                                                                  |     |     |         |
| 81                                                                                       | 4   | Device Serial Number. See **Property 2.2.1.1.1.1 Serial Number** for the format. | B   | M   |         |
| End of any wrappers, at minimum including **Request Message** found on page **56**       |     |                                                                                  |     |     |         |

### [Table 6.103](#table-6-103)8 - Response Data for Command 0xEF08 – Reset Device Lock Passcode (MAGTEK INTERNAL ONLY FOR NOW)

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **57** |     |                     |     |     |         |
| EF08 = Command **0xEF08 – Reset Device Lock Passcode (MAGTEK INTERNAL ONLY FOR NOW)**     |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **57**       |     |                     |     |     |         |

### [Table 6.103](#table-6-103)9 - Request Example

| Example (Hex)                                 |
|-----------------------------------------------|
| AA00 81 04 0155EF08 84 08 EF08 81 04 BE001BB0 |

### [Table 6.104](#table-6-104)0 - Response Example

| Example (Hex)                                 |
|-----------------------------------------------|
| AA00 81 04 8255EF08 82 04 00000000 84 02 EF08 |

### Command 0xEF11 - Get Key Info

The host uses this command to retrieve information about a key slot, including details about the key stored in that slot. It can be used for several purposes, including:

-   Determine if a key exists / has been loaded
-   Get key derivation data to derive a DUKPT key
-   Get transport key information to retrieve the appropriate transport key

The sequence of events is as follows:

1.  The host constructs the command request in the format below.
2.  The host sends the command request to the device.
3.  The device sends a response in the format below to the host.

### [Table 6.104](#table-6-104)1 - Request Data for Command 0xEF11 - Get Key Info

| Tag                                                                                      | Len | Value / Description  | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|----------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                      |     |     |         |
| EF11 = **Command 0xEF11 - Get Key Info**                                                 |     |                      |     |     |         |
| 81                                                                                       | 02  | Key Slot ID See \*\* |     |     |         |
|                                                                                          |     |                      |     |     |         |

### [Table 4.196](#table-4-196) - Key Slot ID\*\* on page **117**. \| B \| R \| \|

\| End of any wrappers, at minimum including **Request Message** found on page **55** \| \| \| \| \| \|

### [Table 6.104](#table-6-104)2 - Response Data for Command 0xEF11 - Get Key Info

| Tag                                      | Len | Value / Description                                                                                                                                                                                                        | Typ | Req | Default |
|------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| EF11 = **Command 0xEF11 - Get Key Info** |     |                                                                                                                                                                                                                            |     |     |         |
| 81                                       | 04  | Key Slot Information                                                                                                                                                                                                       | B   | R   |         |
| /null                                    | (1) | Key Slot Status 0x00 = Empty 0x01 = Loaded (Key not assigned purpose) 0x02 = Loaded & Active 0x03 = Exhausted (End of DUKPT key sequence 0x04 = Expired (Reserved, certificate status) 0xFF = Not supported in this device | B   | R   |         |
| /null                                    | (1) | Key Slot Type First byte of the Key Slot ID in the host’s request message.                                                                                                                                                 | B   | R   |         |
| /null                                    | (2) | Transport Key Slot ID This specifies the key used to secure and load the key that the host is retrieving information about. See \*\*                                                                                       |     |     |         |
|                                          |     |                                                                                                                                                                                                                            |     |     |         |

### [Table 4.196](#table-4-196) - Key Slot ID\*\* on page **117**. \| B \| R \| \|

\| 82 \| 06 \| Loaded Key Information \| B \| O \| \| \| /null \| (1) \| Key Environment ‘T’ = Test ‘P’ = Production \| A \| R \| \| \| /null \| (4) \| TR-31 Attributes See \*\*

### [Table 4.192](#table-4-192) - TR-31 Key Type Table - Usage/Algorithm/Mode.\*\* \| B \| R \| \|

\| /null \| (1) \| Encoding of Algorithm & Length 0x01 = DEA 0x02 = 2TDEA 0x03 = 3TDEA 0x04 = AES128 0x05 = AES192 0x06 = AES256 \| B \| R \| \| \| 83 \| var \| Key Check Value For AES-CMAC, 5 bytes. For TDES-CMAC or TDES-CBCMAC, 3 bytes \| B \| O \| \| \| 84 \| var \| Key Derivation Information This contains the derivation block, key serial number (KSN), or key label, as appropriate for the key type. \| B \| O \| \| \| A6 \| var \| Restrictions Reserved. Do not include. \| B \| O \| \| \| 81 \| 02 \| DUKPT Restrictions These restrictions come from the TR-31 block. \| B \| O \| \| \| 89 \| var \| Timestamp This comes from the TR-31 block or from device’s real-time clock. \| B \| O \| \|

### [Table 6.104](#table-6-104)3 - Request Example

| Example (Hex)                                   |
|-------------------------------------------------|
| AA 00 81 04 01 21 EF 11 84 06 EF 11 81 02 20 07 |

### [Table 6.104](#table-6-104)4 - Response Example

| Example (Hex)                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 82 21 EF 11 82 04 00 00 00 00 84 34 A2 32 81 04 02 20 10 81 82 06 54 42 31 54 58 03 84 0A FF FF 98 76 54 32 10 30 00 00 A6 04 81 02 00 3F 89 10 32 30 32 30 30 39 30 32 54 31 35 35 38 30 32 5A |

**Note: For additional support, please contact MagTek Support.**

## Command Group 0xFnnn - Manufacturing

### Command 0xF012 - Force Tamper (MAGTEK INTERNAL ONLY)

This command is used to force the device’s tamper protection mechanisms to register a tamper event.

The sequence of events is as follows:

1.  The device’s tamper protection features must first be enabled. See **Command 0xF016 - Activate Device Security (MAGTEK INTERNAL ONLY)**.
2.  The host uses **Command 0xE001 - Get Challenge** to establish a secure session with the device.
3.  The host constructs the command request for **Command 0xF012 - Force Tamper (MAGTEK INTERNAL ONLY)** in the format below.
4.  The host constructs **Command 0xEEEE - Send Secured Command to Device** using the previously constructed command request as the payload, and sends that command request to the device as a **Request Message**.
    1.  Because this command is secured using a signature, read **Property 2.1.2.2.2.6 Key Type** to determine which fixed key to use to generate the signature.
    2.  Build the **Security Parameters Type** portion of the wrapper with:
        1.  **Security Operation Type** populated with the following values:
            1.  Operation Type = **Command Authorization Using Signature**
            2.  Operation Algorithm = **ECDSA (indeterministic)**
            3.  Operation Hash = **SHA-256**
            4.  Operation Curve = **P521**.
5.  The device validates the request:
    1.  If the request is valid and properly authenticated, it forces the tamper event and automatically resets. The device does not send a response to the host in this case.
    2.  If the request fails validation, the device sends a response in the format below to report the failure to the host.

### [Table 6.11](#table-6-11)1 - Request Data for Command 0xF012 - Force Tamper (MAGTEK INTERNAL ONLY)

| Tag                                                                                      | Len | Value / Description | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                     |     |     |         |
| F012 = **Command 0xF012 - Force Tamper (MAGTEK INTERNAL ONLY)**                          |     |                     |     |     |         |
| No parameters.                                                                           |     |                     |     |     |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                     |     |     |         |

### [Table 6.11](#table-6-11)2 - Response Data for Command 0xF012 - Force Tamper (MAGTEK INTERNAL ONLY)

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| F012 = **Command 0xF012 - Force Tamper (MAGTEK INTERNAL ONLY)**                           |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

### [Table 6.11](#table-6-11)3 - Request Example

| Example (Hex)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 14 F0 12 84 81 CA EE EE A1 24 81 04 02 01 04 05 84 00 85 00 A8 16 81 02 00 00 82 07 45 43 43 53 49 47 4E 86 05 45 43 44 53 41 88 00 A9 00 82 04 B5 03 3D A0 83 08 3B 4F A0 62 69 BB 73 38 84 02 F0 12 9E 81 8B 30 81 88 02 42 01 F7 60 F4 89 8A 81 6D E2 4E 6C 5D D1 66 41 A4 34 54 E7 32 93 48 3D E5 7D 2C C6 16 F6 E8 CC 98 C6 5D 26 A6 20 60 B7 D1 EF 78 DB 85 32 82 72 67 23 8B 04 00 93 98 14 4E 2C 47 1A 3B F6 B6 B8 93 D2 EA 02 42 01 84 B4 A4 5C 9F D8 EC AD E2 29 F8 AD 8B DD AF 4C 4E 85 F9 B9 E2 AC 7E 7D 3B AE DB 83 47 AD 1B 95 91 32 C4 AA 0F 31 B0 8C 1B 2D AD C0 76 4C A1 AB D2 9F 3B 25 6A 87 36 AC 40 67 B9 33 5B 20 36 50 30 |

### [Table 6.11](#table-6-11)4 - Response Example

| Example (Hex)                                                                       |
|-------------------------------------------------------------------------------------|
| Response only occurs in the failure case. AA 00 81 04 82 0F F0 12 82 04 81 00 00 00 |

### Command 0xF014 - Read Log (MAGTEK INTERNAL ONLY)

The host uses this command to read the system event log from the device.

The sequence of events is as follows:

1.  The host uses **Command 0xE001 - Get Challenge** to establish a secure session with the device.
2.  The host constructs the command request for **Tamper in** the format below.
3.  The host constructs **Command 0xEEEE - Send Secured Command to Device** using the previously constructed command request as the payload, and sends that command request to the device as a **Request Message**.
    1.  Because this command is secured using a signature, read **Property 2.1.2.2.2.6 Key Type** to determine which fixed key to use to generate the signature.
    2.  Build the **Security Parameters Type** portion of the wrapper with:
        1.  **Security Operation Type** populated with the following values:
            1.  Operation Type = **Command Authorization Using Signature**
            2.  Operation Algorithm = **ECDSA (indeterministic)**
            3.  Operation Hash = **SHA-256**
            4.  Operation Curve = **P521**.
4.  The device validates the request, then read the system event log.
5.  The device sends a response in the format below to report the result to the host.

### [Table 6.11](#table-6-11)5 - Request Data for Command 0xF014 - Read Log (MAGTEK INTERNAL ONLY)

| Tag                                                                                      | Len | Value / Description | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                     |     |     |         |
| F014 = **Command 0xF014 - Read Log (MAGTEK INTERNAL ONLY)**                              |     |                     |     |     |         |
| No parameters.                                                                           |     |                     |     |     |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                     |     |     |         |

### [Table 6.11](#table-6-11)6 - Response Data for Command 0xF014 - Read Log (MAGTEK INTERNAL ONLY)

| Tag                                                                                       | Len   | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |     |     |         |
| F014 = **Command 0xF014 - Read Log (MAGTEK INTERNAL ONLY)**                               |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |     |     |         |
| 83                                                                                        | var   | System Event Log                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | B   | R   |         |
| /null                                                                                     | (2)   | Number of Events This specifies the number of events in the log that follows.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | B   | R   |         |
| /null                                                                                     | (2)   | Length of Each Event This specifies the fixed length used for each event reported in the log that follows.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | B   | R   |         |
| /null                                                                                     | (var) | Event Log This text blob contains the specified **Number of Events**, up to 10 events total, of constant length equal to **Length of Each Event**. If there are any empty events, they are filled with 0x00 (Null). Each non-null contains: 20 bytes of human readable date-time indicating when the device wrote the entry into the log. If the device is powered on when a tamper occurs, it records the event, reboots, then writes the event to the log. If the device is powered off when a tamper occurs, it records the event, then write the event to the log the next time it powers on. A block of human readable text describing the event Padding with 0x20 (Space) | AN  | R   |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |     |     |         |

Each Event Log text block can contain one of several human readable strings describing the event. The following is an example of two log entries indicating Forced Tamper:

2023-12-08 02:57 @ID:0, sensor_status=0x1, active_sensors=0xaa0374

2023-12-08 02:57 @ID:0, tamper_time_in_seconds=1702004228

In the first log entry above:

-   The value after **sensor_status=** is a 32-bit hex encoded number with a bit set to 1 for each tamper sensor that registered an actual tamper event.
-   The value after **active_sensors =** is a 32-bit hex encoded number with a bit set to 1 for each tamper sensor that was active when the device logged the tamper event.
-   The bit values for both numbers are listed in [Table 6.11](#table-6-11)**12 below**.

In the second log entry above, the value after **tamper_time_in_seconds=** is the value of the device’s real time clock at the time the tamper occurred, expressed as a decimal a number of seconds in Unix epoch time format. This is expected to differ from the human readable date-time stamp that indicates when the device wrote the event to the log, because the device’s always-active security subsystem registers a basic but indelible version of the tamper event immediately, whereas the logging subsystem may need to wait for the device to automatically reboot after tamper, or wait to be powered up after a powered-off tamper, before system resources are available to write the event to the log.

### [Table 6.11](#table-6-11)7 - Sensor Bit Values In Tamper Log

| Bit    | Tamper Sensor                                                                                                                                                                                                        |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0      | Any Tamper: This is only used for **sensor_status=**. It is reserved and set to 0 for **active_sensors=**. Note that if **Command 0xF012 - Force Tamper (MAGTEK INTERNAL ONLY)** is used, only this bit will be set. |
| 1      | Reserved and set to 0                                                                                                                                                                                                |
| 2      | Time Overflow                                                                                                                                                                                                        |
| 3      | Reserved and set to 0                                                                                                                                                                                                |
| 4      | Voltage                                                                                                                                                                                                              |
| 5      | Clock                                                                                                                                                                                                                |
| 6      | Temperature                                                                                                                                                                                                          |
| 7      | Reserved and set to 0                                                                                                                                                                                                |
| 8      | Flash Security                                                                                                                                                                                                       |
| 9      | Test Mode                                                                                                                                                                                                            |
| 10..16 | Reserved and set to 0                                                                                                                                                                                                |
| 17     | Tamper Pin Input 1                                                                                                                                                                                                   |
| 18     | Reserved and set to 0                                                                                                                                                                                                |
| 19     | Tamper Pin Input 3                                                                                                                                                                                                   |
| 20     | Reserved and set to 0                                                                                                                                                                                                |
| 21     | Tamper Pin Input 5                                                                                                                                                                                                   |
| 22     | Reserved and set to 0                                                                                                                                                                                                |
| 23     | Tamper Pin Input 7                                                                                                                                                                                                   |
| 24..31 | Reserved and set to 0                                                                                                                                                                                                |

### [Table 6.11](#table-6-11)8 - Request Example

| Example (Hex)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 32 F0 14 84 81 CA EE EE A1 24 81 04 02 01 04 05 84 00 85 00 A8 16 81 02 00 00 82 07 45 43 43 53 49 47 4E 86 05 45 43 44 53 41 88 00 A9 00 82 04 BE 00 06 80 83 08 88 D3 F5 28 2B CF 07 ED 84 02 F0 14 9E 81 8B 30 81 88 02 42 00 99 F6 96 30 7D 27 CB 59 B8 A9 F1 C1 7A C5 A8 D1 62 C2 8A 5A 9A F2 82 25 DD AF A7 C6 62 D3 57 70 DB 52 E6 EC 77 7F 20 2D CE DB F0 5E 84 77 B4 7B EA 8F 42 FB 6B 49 41 6F 78 33 08 DB 31 94 D0 2A 18 02 42 00 93 06 2A CF 5C 29 4E D5 FE 7B 1D 00 3E 68 C9 DA 4D 94 16 DA F9 86 CC BB 18 54 2E C4 44 28 B8 1C 62 CF 9E 47 46 20 7C 20 EF DF 71 05 49 B7 F9 F7 A0 0B 4D 7C 6C 77 EB 93 AF D3 40 ED 3A 28 10 A9 B4 |

### [Table 6.11](#table-6-11)9 - Response Example

| Example (Hex)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 82 32 F0 14 82 04 00 00 00 00 83 82 03 4C 00 02 00 54 32 30 32 33 2D 31 32 2D 30 38 20 30 32 3A 35 37 20 20 20 20 40 49 44 3A 30 2C 20 73 65 6E 73 6F 72 5F 73 74 61 74 75 73 3D 30 78 31 2C 20 61 63 74 69 76 65 5F 73 65 6E 73 6F 72 73 3D 30 78 61 61 30 33 37 34 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 32 30 32 33 2D 31 32 2D 30 38 20 30 32 3A 35 37 20 20 20 20 40 49 44 3A 30 2C 20 74 61 6D 70 65 72 5F 74 69 6D 65 5F 69 6E 5F 73 65 63 6F 6E 64 73 3D 31 37 30 32 30 30 34 32 32 38 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 |

### Command 0xF015 - Read Log & Clear Tamper (MAGTEK INTERNAL ONLY)

The host uses this command to clear the device’s tamper status and read the system event log from the device.

The sequence of events is as follows:

1.  The host uses **Command 0xE001 - Get Challenge** to establish a secure session with the device.
2.  The host constructs the command request for **Command 0xF015 - Read Log & Clear Tamper** in the format below.
3.  The host constructs **Command 0xEEEE - Send Secured Command to Device** using the previously constructed command request as the payload, and sends that command request to the device as a **Request Message**.
    1.  Because this command is secured using a signature, read **Property 2.1.2.2.2.6 Key Type** to determine which fixed key to use to generate the signature.
    2.  Build the **Security Parameters Type** portion of the wrapper with:
        1.  **Security Operation Type** populated with the following values:
            1.  Operation Type = **Command Authorization Using Signature**
            2.  Operation Algorithm = **ECDSA (indeterministic)**
            3.  Operation Hash = **SHA-256**
            4.  Operation Curve = **P521**.
4.  The device validates the request, then does the following:
    1.  Read and clear the system event log.
    2.  Clear the device’s tamper status.
    3.  Check the device’s tamper status.
5.  The device sends a response in the format below to report the result to the host. If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**. If the device is still in a tampered state after it clears the tamper, the response reports a failure.

### [Table 6.11](#table-6-11)10 - Request Data for Command 0xF015 - Read Log & Clear Tamper (MAGTEK INTERNAL ONLY)

| Tag                                                                                      | Len | Value / Description | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                     |     |     |         |
| F015 = **Command 0xF015 - Read Log & Clear Tamper (MAGTEK INTERNAL ONLY)**               |     |                     |     |     |         |
| No parameters.                                                                           |     |                     |     |     |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                     |     |     |         |

### [Table 6.11](#table-6-11)11 - Response Data for Command 0xF015 - Read Log & Clear Tamper (MAGTEK INTERNAL ONLY)

| Tag                                                                                       | Len   | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |     |     |         |
| F015 = **Command 0xF015 - Read Log & Clear Tamper (MAGTEK INTERNAL ONLY)**                |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |     |     |         |
| 83                                                                                        | var   | System Event Log                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | B   | R   |         |
| /null                                                                                     | (2)   | Number of Events This specifies the number of events in the log that follows.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | B   | R   |         |
| /null                                                                                     | (2)   | Length of Each Event This specifies the fixed length used for each event reported in the log that follows.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | B   | R   |         |
| /null                                                                                     | (var) | Event Log This text blob contains the specified **Number of Events**, up to 10 events total, of constant length equal to **Length of Each Event**. If there are any empty events, they are filled with 0x00 (Null). Each non-null contains: 20 bytes of human readable date-time indicating when the device wrote the entry into the log. If the device is powered on when a tamper occurs, it records the event, reboots, then writes the event to the log. If the device is powered off when a tamper occurs, it records the event, then write the event to the log the next time it powers on. A block of human readable text describing the event Padding with 0x20 (Space) | AN  | R   |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |     |     |         |

Each **Event Log** text block can contain one of several human readable strings describing the event. The following is an example of two log entries indicating **Tamper Pin 3 Input** tampered:

2021-02-05 00:16 @ID:0, sensor_status=0x80001, active_sensors =0xaa0374

2021-02-05 00:16 @ID:0, tamper_time_in_seconds=1612484188

In the first log entry above:

-   The value after **sensor_status=** is a 32-bit hex encoded number with a bit set to 1 for each tamper sensor that registered an actual tamper event.
-   The value after **active_sensors =** is a 32 bit hex encoded number with a bit set to 1 for each tamper sensor that was active when the device logged the tamper event.
-   The bit values for both numbers are listed in [Table 6.11](#table-6-11)**12 below**.

In the second log entry above, the value after **tamper_time_in_seconds=** is the value of the device’s real time clock at the time the tamper occurred, expressed as a decimal a number of seconds in Unix epoch time format. This is expected to differ from the human readable date-time stamp that indicates when the device wrote the event to the log, because the device’s always-active security subsystem registers a basic but indelible version of the tamper event immediately, whereas the logging subsystem may need to wait for the device to automatically reboot after tamper, or wait to be powered up after a powered-off tamper, before system resources are available to write the event to the log.

### [Table 6.11](#table-6-11)12 - Sensor Bit Values in Tamper Log

| Bit    | Tamper Sensor                                                                                                                                                                                                        |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0      | Any Tamper: This is only used for **sensor_status=**. It is reserved and set to 0 for **active_sensors=**. Note that if **Command 0xF012 - Force Tamper (MAGTEK INTERNAL ONLY)** is used, only this bit will be set. |
| 1      | Reserved and set to 0                                                                                                                                                                                                |
| 2      | Time Overflow                                                                                                                                                                                                        |
| 3      | Reserved and set to 0                                                                                                                                                                                                |
| 4      | Voltage                                                                                                                                                                                                              |
| 5      | Clock                                                                                                                                                                                                                |
| 6      | Temperature                                                                                                                                                                                                          |
| 7      | Reserved and set to 0                                                                                                                                                                                                |
| 8      | Flash Security                                                                                                                                                                                                       |
| 9      | Test Mode                                                                                                                                                                                                            |
| 10..16 | Reserved and set to 0                                                                                                                                                                                                |
| 17     | Tamper Pin Input 1                                                                                                                                                                                                   |
| 18     | Reserved and set to 0                                                                                                                                                                                                |
| 19     | Tamper Pin Input 3                                                                                                                                                                                                   |
| 20     | Reserved and set to 0                                                                                                                                                                                                |
| 21     | Tamper Pin Input 5                                                                                                                                                                                                   |
| 22     | Reserved and set to 0                                                                                                                                                                                                |
| 23     | Tamper Pin Input 7                                                                                                                                                                                                   |
| 24..31 | Reserved and set to 0                                                                                                                                                                                                |

### [Table 6.11](#table-6-11)13 - Request Example

| Example (Hex)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 0F F0 15 84 81 C8 EE EE A1 24 81 04 02 01 06 05 84 00 85 00 A8 16 81 02 00 00 82 07 45 43 43 53 49 47 4E 86 05 45 43 44 53 41 88 00 A9 00 82 04 B5 03 3D A0 83 08 5B 6B 45 4B 00 5B CE 31 84 02 F0 15 9E 81 89 30 81 86 02 41 52 5B 04 9A C7 CC 56 DE 5A EA 89 62 47 BB B8 0D 93 80 CE C8 AD 6E 16 F7 6E DA 08 42 0B 9C 69 77 61 B0 99 FC 05 7D AE AF 75 79 9C 7B B3 81 72 5C 4E 5B 92 DC F3 B6 85 5E B3 A2 71 0D 1D 93 B5 0D 0C 02 41 46 47 0A EF 6F D5 97 ED 4F 41 E8 3C FD 20 A1 CE 7D E5 CA D3 E8 22 3B ED BC 2A 8A A0 BF 73 72 81 35 4F CB 52 B6 A9 07 6F 36 7F 5D 35 D5 29 3D 5D 78 17 0E B2 D6 AA A5 0D B3 4D B9 04 2C 03 6A AC A5 |

### [Table 6.11](#table-6-11)14 - Response Example

| Example (Hex)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 82 0F F0 15 // Message Info 82 04 00 00 00 00 // Status is OK 83 82 03 50 // Payload, System Event LOG 00 02 // 2 events in the LOG 00 54 // 0x54 (84) bytes per event 32 30 32 30 2D 30 38 2D 32 36 2D 31 34 3A 30 30 // Event \#1: 2020-08-26-14:00 @ID:0, 20 20 20 20 40 49 44 3A 30 2C 20 73 65 6E 73 6F // sensor_status=0x1, active_sensors=0xaa0374 72 5F 73 74 61 74 75 73 3D 30 78 31 2C 20 61 63 74 69 76 65 5F 73 65 6E 73 6F 72 73 3D 30 78 61 61 30 33 37 34 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 32 30 32 30 2D 30 38 2D 32 36 2D 31 34 3A 30 30 // Event \#2: 2020-08-26-14:00 @ID:0, 20 20 20 20 40 49 44 3A 30 2C 20 74 61 6D 70 65 // tamper_time_in_seconds=1598450397 72 5F 74 69 6D 65 5F 69 6E 5F 73 65 63 6F 6E 64 73 3D 31 35 39 38 34 35 30 33 39 37 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 |

### Command 0xF016 - Activate Device Security (MAGTEK INTERNAL ONLY)

The host uses this command to activate the security on the device. This allows the manufacturer to perform initial operations on an unsecured device, then enable security before shipping. This command is intended to only be executed once during manufacturing, and can not be undone or redone.

The sequence of events is as follows:

1.  The host uses **Command 0xE001 - Get Challenge** to establish a secure session with the device.
2.  The host constructs a request for **Command 0xF016 - Activate Device Security** as shown below.
3.  The host constructs **Command 0xEEEE - Send Secured Command to Device** using the previously constructed command request as the payload, and sends that command request to the device as a **Request Message**.
    1.  Because this command is secured using a signature, read **Property 2.1.2.2.2.6 Key Type** to determine which fixed key to use to generate the signature.
    2.  Build the **Security Parameters Type** portion of the wrapper with:
        1.  **Security Operation Type** populated with the following values:
            1.  Operation Type = **Command Authorization Using Signature**
            2.  Operation Algorithm = **ECDSA (indeterministic)**
            3.  Operation Hash = **SHA-256**
            4.  Operation Curve = **P521**.
4.  The device does the following:
    1.  Validates the secure wrapper around the command and terminates if the signature is invalid.
    2.  Set the specified date and time on the device’s real-time clock (RTC).
    3.  Store the specified PCI Hardware ID in the device’s battery backed secure RAM.
    4.  Store the specified Hardware Configuration Profile in the device’s battery backed secure RAM.
    5.  Store the specified MAC Address in the device’s battery backed secure RAM.
    6.  Enable the 23-hour automatic restart.
    7.  Generate the Master Key Derivation Key (MKDK) and four Derived Key Encrypting Keys (DKEK/DDEK/DKMK/DDMK).
    8.  Store the specified WLAN SoftAP MagTek Password in the device’s EEPROM AES 256 CBC encrypted using the DKEK.
    9.  Activate and lock the tamper protection mechanism.
5.  The device sends a **Response Message** to the host to indicate the result.

### [Table 6.11](#table-6-11)15 - Request Data for Command 0xF016 - Activate Device Security (MAGTEK INTERNAL ONLY)

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |     |     |         |
| F016 = **Command 0xF016 - Activate Device Security (MAGTEK INTERNAL ONLY)**              |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |     |     |         |
| 81                                                                                       | 07  | Current Date and Time This initializes the device’s real-time clock (RTC) to the specified date and time. The specified date and time should be Universal Time Coordinated (UTC).                                                                                                                                                                                                                                                                                                                                                                                                      | B   | R   |         |
| /null                                                                                    | (1) | Month From 0x01 January to 0x0C December.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | B   | R   |         |
| /null                                                                                    | (1) | Day of Month From 0x01 to 0x1F (31st).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | B   | R   |         |
| /null                                                                                    | (1) | Hour Hour in 24-hour format from 0x00 Midnight to 0x17 11PM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | B   | R   |         |
| /null                                                                                    | (1) | Minute Minutes after the hour from 0x00 0 minutes after the hour to 0x3B 59 minutes after the hour.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | B   | R   |         |
| /null                                                                                    | (1) | Seconds Seconds after the minute from 0x00 0 seconds to 0x3B 59 seconds after the minute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | B   | R   |         |
| /null                                                                                    | (1) | Reserved. Set to 0x00.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | B   | R   |         |
| /null                                                                                    | (1) | Year Current year minus 2008                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | B   | R   |         |
| 85                                                                                       | var | PCI Hardware ID This specifies the PCI Hardware ID the device uses to uniquely identify its model family on the touchscreen and via host commands.                                                                                                                                                                                                                                                                                                                                                                                                                                     | B   | O   |         |
| 86                                                                                       | var | Hardware Configuration Profile This parameter contains a tightly encoded block of bytes that tells the device’s firmware what hardware is installed. Note some values inside this parameter must be prefixed with explicit lengths, but for compactness they do not include tags. Such values do not have parentheses in the **Len** column. This data is stored in the secure processor’s battery-backed (VBAT) Register File and, like keys, can only be erased by forcing a tamper event. Example: 02 05 01 02 01 02 00 04 01 01 01 01 02 01 01 05 01 00 00 00 01 05 01 01 01 01 01 | B   | O   |         |
| /null                                                                                    | (1) | Hardware Configuration Profile Version This identifies the version of the Hardware Configuration Profile to provide future extensibility. 0x01 = Initial release 0x02 = Added in specification revision 30                                                                                                                                                                                                                                                                                                                                                                             | B   | R   |         |
| /null                                                                                    | 05  | System Core Hardware Length is included in the hardware configuration profile value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | B   | R   |         |
| //null                                                                                   | (1) | Processor / SOC 0x01 = K81                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | B   | R   |         |
| //null                                                                                   | (1) | External Flash RAM 0x00 = None 0x01 = Parallel NOR 2MB 0x02 = Parallel NOR 4MB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | B   | R   |         |
| //null                                                                                   | (1) | External RAM 0x00 = None 0x01 = Parallel PSRAM 2MB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | B   | R   |         |
| //null                                                                                   | (1) | External non-volatile RAM/EEPROM 0x00 = None 0x01 = SPI 32KB 0x02 = SPI 64KB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | B   | R   |         |
| //null                                                                                   | (1) | On-board Host 0x00 = None 0x01 = Android Tablet                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | B   | R   |         |
| /null                                                                                    | 04  | Readers Length is included in the hardware configuration profile value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | B   | R   |         |
| //null                                                                                   | (1) | MSR 0x00 = None 0x01 = 3 Track MagnePrint Head and MagnePrint ASIC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | B   | R   |         |
| //null                                                                                   | (1) | ICCR (Contact) 0x00 = None 0x01 = Contact block with analog chip                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | B   | R   |         |
| //null                                                                                   | (1) | PCD (Contactless) 0x00 = None 0x01 = PN5180 0x02 = PN5190                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | B   | R   |         |
| //null                                                                                   | (1) | BCR (Barcode Reader) 0x00 = None 0x01 = Barcode Reader (NLS-N1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | B   | R   |         |
| /null                                                                                    | 02  | Power Length is included in the hardware configuration profile value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | B   | R   |         |
| //null                                                                                   | (1) | Battery 0x00 = None 0x01 = xxxx LiPo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | B   | R   |         |
| //null                                                                                   | (1) | PMIC 0x00 = None 0x01 = PF1550A9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | B   | R   |         |
| /null                                                                                    | 05  | Communication Length is included in the hardware configuration profile value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |     |     |         |
| //null                                                                                   | (1) | USB 0x00 = None 0x01 = Internal FS available 0x03 = Internal FS available and Apple Authentication Coprocessor present This configuration is bitwise.                                                                                                                                                                                                                                                                                                                                                                                                                                  | B   | R   |         |
| //null                                                                                   | (1) | RS-232 0x00 = None 0x01 = Present                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | B   | R   |         |
| //null                                                                                   | (1) | Ethernet 0x00 = None 0x01 = Present                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | B   | R   |         |
| //null                                                                                   | (1) | Wireless LAN (WLAN) 0x00 = None 0x01 = Present                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | B   | R   |         |
| //null                                                                                   | (1) | Bluetooth® Low Energy 0x00 = None 0x01 = Present                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | B   | R   |         |
| /null                                                                                    | 05  | User Interface Length is included in the hardware configuration profile value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |     |     |         |
| //null                                                                                   | (1) | Display 0x00 = None 0x01 = 320x240 16-bit RGB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | B   | R   |         |
| //null                                                                                   | (1) | Touchpad 0x00 = None 0x01 = 320x240 integrated with display                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | B   | R   |         |
| //null                                                                                   | (1) | LEDs 0x00 = None 0x01 = Four RGB on face 0x02 = Four monochrome on face                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | B   | R   |         |
| //null                                                                                   | (1) | Audio / Sound 0x00 = None 0x01 = Buzzer Transducer 3.6V 2.7kHz 85dB with PMIC output voltage volume control 0x02 = Buzzer Transducer 3V 2kHz 80dB with GPIO high-low volume control                                                                                                                                                                                                                                                                                                                                                                                                    | B   | R   |         |
| //null                                                                                   | (1) | Buttons 0x00 = None 0x01 = One pushbutton and one recessed switch 0x02 = One pushbutton and one virtual recessed switch                                                                                                                                                                                                                                                                                                                                                                                                                                                                | B   | R   |         |
| 88                                                                                       | var | MAC Address For devices with TCP/IP hardware, such as Ethernet or WLAN, this specifies the device’s MAC address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | B   | O   |         |
| 89                                                                                       | var | WLAN SoftAP MagTek Password The length can be a maximum of 63 bytes. For devices with WLAN, this specifies the device’s SoftAP MagTek Password. MagTek shall load this password and it shall be printed on the device’s label. This passwork shall be unique per device. The device will use this password for its SoftAP until a SoftAP Customer Password is loaded.                                                                                                                                                                                                                  | B   | O   |         |
| 8A                                                                                       | 4   | WLAN Firmware Sequence Number The length is 4 bytes, ms byte first                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | B   | O   |         |
| End of any wrappers, at minimum including **Request Message** found on page **55**       |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |     |     |         |

### [Table 6.11](#table-6-11)16 - Response Data for Command 0xF016 - Activate Device Security (MAGTEK INTERNAL ONLY)

| Tag                                                                                       | Len | Value / Description | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|---------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                     |     |     |         |
| F016 = **Command 0xF016 - Activate Device Security (MAGTEK INTERNAL ONLY)**               |     |                     |     |     |         |
| No parameters.                                                                            |     |                     |     |     |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                     |     |     |         |

If the request started successfully, the Request Status in the message wrapper is **OK, Started / Running, All good / requested operation was successful**.

### [Table 6.11](#table-6-11)17 - Request Example

| Example (Hex)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 0F F0 16 84 81 EA EE EE A1 24 81 04 02 01 06 05 84 00 85 00 A8 16 81 02 00 00 82 07 45 43 43 53 49 47 4E 86 05 45 43 44 53 41 88 00 A9 00 82 04 B5 03 3D A0 83 08 BE A5 45 81 90 C9 28 0C 84 22 F0 16 81 07 08 1A 0E 16 28 04 0C 85 0B 44 65 76 65 6C 6F 70 6D 65 6E 74 86 08 31 32 33 34 35 36 37 38 9E 81 8B 30 81 88 02 42 00 CD C1 EC 9E D1 30 A6 19 0A 8D 27 F6 65 26 4A 97 3C 79 94 60 BA 57 4D 64 4A 47 FC 72 6B 83 1F 1F DB 05 40 E3 70 16 17 DB 5E A6 93 77 1D 40 F5 DE 0A 9E 01 7A B3 6D DA 8A 73 94 46 1A 68 99 B6 8C 9F 02 42 01 5E 40 4E 4C F9 BF 1B 10 4D BE 7C F6 F9 FE F8 77 1E D0 1A FE AA FC 8B BD 06 BB 8A E5 A5 B3 0E 2E B4 CC DE 60 48 96 2A 84 38 E0 41 45 CD A2 4B F9 36 DA 61 BE 06 A6 CA F2 2F 17 EC DA 0D 59 D0 01 EC |

### [Table 6.11](#table-6-11)18 - Response Example

| Example (Hex)                             |
|-------------------------------------------|
| AA 00 81 04 82 0F F0 16 82 04 00 00 00 00 |

### Command 0xF017 - Establish Ephemeral KBPK

The host uses this command to complete the **ECDHE-ECDSA Key Exchange** protocol, which enables the host and the device to generate the same TEMP KBPK key to use with **Command 0xEF01 - Load Key Using TR-31** to load the Master Transport Key (MTK).

The sequence of events is as follows:

1.  The host uses **Command 0xE001 - Get Challenge** to establish a secure session with the device.
2.  The host constructs **Command 0xF017 - Establish Ephemeral KBPK** per the request table below.
3.  The host constructs **Command 0xEEEE - Send Secured Command to Device** using the previously constructed command request as the payload, and sends that command request to the device as a **Request Message**.
    1.  Because this command is secured using a signature, read **Property 2.1.2.2.2.6 Key Type** to determine which fixed key to use to generate the signature.
    2.  Build the **Security Parameters Type** portion of the wrapper with:
        1.  **Security Operation Type** populated with the following values:
            1.  Operation Type = **Command Authorization Using Signature**
            2.  Operation Algorithm = **ECDSA (indeterministic)**
            3.  Operation Hash = **SHA-256**
            4.  Operation Curve = **P521**.
4.  The device does the following:
    1.  Validates the secure wrapper around the command, and terminates if the signature is invalid.
    2.  Determine if the Master Transport Key (MTK) has already been loaded. If it has, the device rejects the command request.
    3.  Generates a pair of keys, saves the Device Private Key for calculation.
    4.  Generates and saves 8 bytes of Device Random Token for calculation.
    5.  Calculates the TEMP KBPK based on Host Public Key and Host Random Token passed in with the command request, and the Device Private Key and Device Random Token the device generated.
5.  The device sends a **Response Message** to the host to indicate the result. The response message includes Device Random Token and Device Public Key.
6.  The host calculates a matching TEMP KBPK as defined in as defined in **NIST SP800-56A**, using the Host Private Key, Host Random Token, Device Public Key, and Device Random Token. It can then use this key to perform encryption operations on secret data in the Master Transport Key (MTK).
7.  The device uses its copy of the matching TEMP KBPK to decrypt the secret information encrypted by the host using the same key. On successful MTK load, the device erases the TEMP KBPK. It also erases the TEMP KBPK if the device is power cycled or reset, and the host would need to restart the process with a new TEMP KBPK.

### [Table 6.11](#table-6-11)19 - Request Data for Command 0xF017 - Establish Ephemeral KBPK

| Tag                                                                                      | Len | Value / Description                                                                                                                                                                            | Typ | Req | Default |
|------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Request Message** found on page **55** |     |                                                                                                                                                                                                |     |     |         |
| F017 = **Command 0xF017 - Establish Ephemeral KBPK**                                     |     |                                                                                                                                                                                                |     |     |         |
| A1                                                                                       | var | Security Parameters This contains a **Security Parameters Type** TLV data object with only the first parameter populated with: 01 = Key Agreement, 01 = ECDHE, 05 = Curve P521, 01 = SP800-56A | B   | R   |         |
| 83                                                                                       | var | Host Ephemeral Public Key This parameter is in ASN.1 format. The information of the cipher and key size are included in the ASN.1 Public Key file (PKCS\#8).                                   | B   | R   |         |
| 84                                                                                       | 08  | Host Random Token This contains an 8 byte random number generated by the host.                                                                                                                 | B   | R   |         |

### [Table 6.11](#table-6-11)20 - Response Data for Command 0xF017 - Establish Ephemeral KBPK

| Tag                                                                                       | Len | Value / Description                                                                                                                                                                                        | Typ | Req | Default |
|-------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|---------|
| Beginning of any wrappers, at minimum including **Response Message** found on page **56** |     |                                                                                                                                                                                                            |     |     |         |
| F017 = **Command 0xF017 - Establish Ephemeral KBPK**                                      |     |                                                                                                                                                                                                            |     |     |         |
| A1                                                                                        | var | Security Parameters This contains a **Security Parameters Type** TLV data object populated entirely with 0x00 padding to indicate that all values are the same as the corresponding values in the Request. | B   | R   |         |
| 83                                                                                        | var | Device Ephemeral Public Key This parameter is in ASN.1 format. The information of the cipher and key size are included in the ASN.1 key file.                                                              | B   | R   |         |
| 84                                                                                        | 08  | Device Random Token This contains an 8 byte random number generated by the device.                                                                                                                         | B   | R   |         |
| End of any wrappers, at minimum including **Response Message** found on page **56**       |     |                                                                                                                                                                                                            |     |     |         |

### [Table 6.11](#table-6-11)21 - Request Example

| Example (Hex)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 01 10 F0 17 84 82 01 8C EE EE // Secure Wrapper A1 24 81 04 02 01 04 05 84 00 85 00 A8 16 81 02 00 00 82 07 45 43 43 53 49 47 4E 86 05 45 43 44 53 41 88 00 A9 00 82 04 B5 03 3D A0 83 08 ED B0 79 E6 E3 F1 83 AE 84 81 C3 // payload is 0xF017 command body F0 17 A1 14 // Security parameters 81 04 01 01 05 01 84 00 A8 0A 81 02 00 00 82 00 86 00 88 00 83 81 9E // TL of PKCS8 public key 30 81 9B // V of PKCS8 public key 30 10 06 07 2A 86 48 CE 3D 02 01 06 05 2B 81 04 00 23 03 81 86 00 04 01 64 1C DA 45 C5 56 B3 8B 31 29 8C 94 A1 E7 95 C9 D3 85 C0 4D F3 15 13 D9 91 43 84 58 15 CD 45 6B 67 F6 AC 7C 56 DF F8 0C 65 A7 CF 81 F1 13 2F AA E5 22 10 78 23 C9 4F 1D CD 24 42 EC 1A 3F A4 75 58 00 97 59 96 9E 01 D0 62 47 B7 EF 5F 0B D0 8B E6 CA 12 F0 3C 13 43 AF 15 21 92 3D 6B FE 47 74 68 38 3F DD 1E 90 2B FD 0F D6 DA 7A A1 E9 A1 98 85 3A DA 93 6D EE 05 61 87 8B 81 BF 6A 78 2F 40 A5 E8 66 84 08 BD E3 77 88 83 0C F6 37 // TLV of 8-byte random \# for TEMP-KBPK // end of 0xF017 command body 9E 81 8B 30 81 88 02 42 00 C4 13 1D C2 13 7A F6 FD F0 F1 BB BD 14 C2 4A FE D7 6F BC 80 91 84 26 43 85 40 B6 5D BE 1D 9C 74 90 77 B6 41 62 69 52 04 72 93 C0 9C 59 2A DB 03 31 0F 8A 28 C0 DB 1A B7 1B 51 B3 E6 BD FF 50 77 CA 02 42 01 EE D8 2D 9F A3 D1 98 4E 74 C8 85 11 52 93 15 FF 9D 7D 5A 03 FD 84 B8 B9 09 20 8B 15 98 7A 5E 56 A5 61 71 9A 0A B9 D1 DA 1C 96 1D 0C EF F0 D2 E3 A4 22 84 60 E2 AA 8C AA 2B 8B AE 02 50 D8 B3 CF 84 |

### [Table 6.11](#table-6-11)22 - Response Example

| Example (Hex)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AA 00 81 04 82 10 F0 17 82 04 00 00 00 00 84 81 B5 // Response Payload F0 17 A1 06 81 01 00 82 01 00 83 81 9E // TL of PKCS8 public key 30 81 9B // V of PKCS8 public key 30 10 06 07 2A 86 48 CE 3D 02 01 06 05 2B 81 04 00 23 03 81 86 00 04 01 77 CD 91 56 96 34 2B C6 5A 6C EC 5D 74 96 41 B3 F9 2B 12 85 19 90 F8 73 BF FF 3C 10 44 E3 CB 21 4E CA F6 CE FC F8 C8 80 52 44 13 FA B1 97 A1 8C 44 FE 95 A2 0A F3 3D A4 3A 8F 2E 39 41 23 22 B1 AB 01 29 26 4F CC 0E 86 11 16 92 FF BC E1 BF DA FC 21 BA B1 5A C4 DE 7B C1 6F A9 17 F8 4B 1E B2 1F 5F 21 7D 54 00 15 41 C3 21 75 0D 21 DC 95 13 A7 2C 8C 11 77 96 38 87 51 08 7A 1F 63 EC A8 8F C4 AB B3 84 08 4C 4A EC 0B 47 E4 53 EB // TLV of 8-byte random \# for TEMP-KBPK |

**Note: For additional support, please contact MagTek Support.**

## 
