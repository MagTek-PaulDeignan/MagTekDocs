## 6.1.1 Command 0x1001 - Start Transaction

The host uses this command to start a payment transaction.

### Transaction Sequence

The sequence of events for transactions with card readers enabled is as follows:

#### General Transaction Flow:

1. If the device is configured with **User Event Notification Controls Enable** (Property 1.2.7.1.2.1), cardholders may present cards before the host initiates this command.

   - **MSR Only:** Device temporarily stores swipe data based on **User Event Notification MSR Data Timeout** (Property 1.2.7.1.2.2).
   - **EMV Contact/Contactless Only:** The host must quickly call this command after a card is presented.

2. Host sends command request.

3. Device sends response, awaits cardholder input.

4. **Barcode Reader (BCR Only):** Scanning barcode sends notification 0x0101 with barcode data, terminating transaction.

5. Device sends notification 0x0101 to report the payment technology.

6. **Fallback Operations (MSR Only):** Device-driven fallback behavior occurs based on Property 1.2.1.1.1.1.

7. **EMV Contact Only (multiple applications):**

   - **Display Only:** Device prompts cardholder for app selection.
   - **No Display:** Device sends notification 0x1803 for host-managed selection.

8. Device sends notification 0x0101 with ARQC update.

9. **Quick Chip Transaction Flow:**

   - Device constructs internal ARPC, sends notification 0x0105.
   - Device displays REMOVE CARD or sends host notification 0x1803.
   - Host processes ARQC, finalizes transaction independently, displays outcome.

10. **EMV Transaction Flow:**

    - Host processes ARQC, sends ARPC (Command 0x1004).
    - Device waits (ARPC Receive Timeout), sends ARQC retry if needed.
    - Device sends notification 0x0105 with outcome.

11. **Touch Only (Signature Capture):** Device prompts signature if Property 1.2.1.1.2.1 is set.

12. Device sends notification 0x0101 with batch data.

13. Device sends notification 0x0105 for transaction completion.

14. **Host-driven fallback (MSR Only):** If device-driven fallback disabled, host implements fallback logic based on Card Type tag DFDF52.

15. **Touch Only (Host-driven Signature):** Host manages signature capture within Signature Timing Window.

16. **EMV Contactless Only (NFC Tag):**

    - Device sends notifications 0x0101 for tag type and UID.
    - No ARQC or BATCH data; host manages via pass-through commands.

17. **Manual Card Entry (MCE Only):**

    - Host initiates transaction with manual entry parameters.
    - Device shows input screens, sends notification 0x0101 (Data Entered, ARQC, Batch Data).
    - Device completes with notification 0x0105.

18. **Tip Feature (Touch Only):**

    - Mode 1A: Tag A4 for tip/tax options; host specifies tip parameters.
    - Mode 1B: START SALE initiates custom amount entry; device manages tip/tax calculations.

19. **Audio Transducer (Beep Flow):** NFC detection flow involving host commands and beep notifications.

20. **Optional Functional Button (Display Only):**

    - Host command enables "Present a Card" page with a functional button.
    - Device notifies host upon button press.



### Command Request Data (Table 6.1 1)

| Tag | Len | Value / Description | Type | Req | Default |
|-----|-----|---------------------|------|-----|---------|
| 81  | 01  | Reserved | | O | |
| 82  | 01  | Transaction Timeout (seconds).<br>0x00 = No timeout<br>0x01-0xFF = 1 to 255 seconds | B | R | |
| A3  | var | **Reader Options** | T | O | |
| /81 | 01  | **Magnetic Stripe Reader Mode (MSR Only)**<br>0x00 = Disabled<br>0x01 = EMV<br>0x80 = Non-EMV (MAGTEK INTERNAL ONLY) | B | O | 0x01 |
| /82 | 01  | **Contact Reader Mode (EMV Contact Only)**<br>0x00 = Disabled<br>0x01 = EMV | B | O | 0x01 |
| /83 | 01  | **Contactless Reader Mode (EMV Contactless Only)**<br>0x00 = Disabled<br>0x01 = EMV<br>0x02 = NFC<br>0x03 = EMV and NFC | B | O | 0x01 |
| /84 | 03  | **Manual Entry Mode (Touch Only)**<br>Byte 1: Card Number Format (0x00 = PAN 8-21 digits)<br>Byte 2: UI Sequence (0x00 = Property 1.2.1.1.5.1)<br>Byte 3: Beeper Feedback (0x00 = Disabled, 0x01 = Enabled) | B | O | |
| /85 | 02  | **Barcode Reader Mode (BCR Only)**<br>Byte 1: Barcode Reader (0x00 = Disabled, 0x01 = Enabled)<br>Byte 2: Encrypt Barcode Data (0x00 = Disabled, 0x01 = Enabled) | B | O | 0x0000 |
| /86 | 01  | **PIN Block Format (Touch Only)**<br>0x00 = ISO Format 0<br>0x03 = ISO Format 3<br>0x04 = ISO Format 4 | B | O | 0x00 |
| A4  | var | **Tip and Tax Options**<br>Byte 1: Tip Mode<br>(0x00 = Disable, 0x01 = % GUI, 0x02 = $ GUI, 0x11 = +Tip %value, 0x12 = +Tip $ amount)<br>Bytes 2-31: Buttons 1-6 configuration (%, $, Custom, No Tip, Disabled) | B | O | |
| /82 | 06  | Tax or Surcharge Amount Display | B | O | |
| 84  | 02  | **Transaction Options**<br>Byte 1: Apple VAS Mode (0x00-0x04)<br>Wallet Mode (Bits 4-6): Apple, Google, Reserved<br>Byte 2: Transaction Flow Control (Quick Chip, DynaPro Response, Signature Capture, Display Amount) | B | O | 0x0003 |
| 86  | var | **Transaction TLV**<br>EMV tags: 9C, 9F02, 9F03, 9F7C, 5F2A, 5F36, 9F53, 9F15, 9F16 | B | R/O | |
| A8  | 00  | MAGTEK INTERNAL ONLY | | O | |
| 8A  |     | MAGTEK INTERNAL ONLY - Notification Options | | | |
| AC  | var | **User Interface Options** | T | O | null |
| /81 | 00  | Suppress Thank You Message | T | O | null |
| /82 | 01  | Override Final Transaction Message | B | O | null |
| /83 | 02  | Functional button Right option (User presses, sends notification 0x1803) | B | O | null |

### Command 0x1001 - Response and Request Examples

#### Response Example: Command Not Executed (Battery Charge State)

```hex
AA 00 81 04 82 01 10 01 82 04 80 02 03 16
```

> If the request started successfully, the Request Status in the message wrapper is "OK, Started / Running, All good / requested operation was successful."

#### Request Example (MSR, Contact, and Contactless Enabled)

```hex
AA 00 81 04 01 00 10 01 84 3D 10 01 82 01 3C A3 09 81 01 01 82 01 01 83 01 01 84 02 00 03 86 27 9C 01 00 9F 02 06 00 00 00 00 01 00 9F 03 06 00 00 00 00 00 00 5F 2A 02 08 40 5F 36 01 02 9F 15 02 00 00 9F 53 01 00
```

#### Request Example (Contactless Only)

```hex
AA 00 81 04 01 00 10 01 84 3D 10 01 82 01 3C A3 09 81 01 00 82 01 00 83 01 01 84 02 00 03 86 27 9C 01 00 9F 02 06 00 00 00 00 01 00 9F 03 06 00 00 00 00 00 00 5F 2A 02 08 40 5F 36 01 02 9F 15 02 00 00 9F 53 01 00
```

#### Response Example

```hex
AA 00 81 04 82 01 10 01 82 04 01 00 00 00
```
