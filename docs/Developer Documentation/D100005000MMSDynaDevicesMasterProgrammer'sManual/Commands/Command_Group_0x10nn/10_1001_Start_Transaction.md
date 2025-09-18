---
title: 0x1001 — Start Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 1
---

# 0x1001 — Start Transaction

The host uses this command to start a payment transaction.

---

## Sequence of Events

For transactions with card readers enabled, the flow is:

1. If user event notifications are enabled via [Property 1.2.7.1.2.1 – User Event Notification Controls Enable](../Properties/#property-1-2-7-1-2-1),  
   the cardholder may present a card before the host calls this command.  
   In that case, the device sends [Notification 0x1001 – Device Information Update](../Notifications/#notification-0x1001),  
   prompting the host to start a transaction.

2. **MSR Only**: If the cardholder swipes before the transaction starts,  
   the device temporarily stores card swipe data for the period defined by  
   [Property 1.2.7.1.2.2 – User Event Notification MSR Data Timeout](../Properties/#property-1-2-7-1-2-2).  

3. The host calls **Start Transaction** (`0x1001`).

4. The device guides the cardholder through interaction (MSR, EMV Contact, Contactless, or MCE).

5. The device sends transaction data and status responses back to the host.

---

## Applicability Matrix

| Transaction Interface | DynaFlex | DynaFlex II PED | DynaProx | DynaFlex II GO |
|------------------------|----------|-----------------|----------|----------------|
| MSR (Swipe)           | ✅       | ✅              | ❌       | ✅              |
| EMV Contact           | ✅       | ✅              | ❌       | ✅              |
| EMV Contactless       | ✅       | ✅              | ✅       | ✅              |
| MCE (Manual)          | ✅       | ✅              | ❌       | ❌              |
| Barcode Reader        | ✅       | ✅              | ✅       | ✅              |

---

## Command Syntax

| Field   | Length | Value   | Description           |
|---------|--------|---------|-----------------------|
| Command | 2      | 0x1001  | Start Transaction     |
| TLVs    | var.   | –       | See below             |

---

### Required TLVs

| Tag    | Name                       | Description                                        |
|--------|----------------------------|----------------------------------------------------|
| DFDF4D | Transaction Control Flags  | Controls available interfaces and flow             |
| RAAT   | Reader Action/Access Type *(MagTek Internal Only)*  | Specifies what action the reader should allow      |

---

### Parameter Table

| Parameter | Type     | Description                                                   |
|-----------|----------|---------------------------------------------------------------|
| DFDF4D    | Bitfield | Defines which card technologies are enabled for this transaction. |
| RAAT      | Reader Action/Access Type *(MagTek Internal Only)* | Specifies what action the reader should allow |

---

## Examples

### Example 1 — MSR (Swipe)

**Applicability:** MSR Only — DynaFlex, DynaFlex II PED  

**Request**
```
0x1001
  9F02 06 000000001000      ; Amount 10.00
  9A   03 250821            ; Date YYMMDD
  9C   01 00                ; Purchase
  5F2A 02 0840              ; Currency USD
  DF01 01 01                ; Entry modes = MSR
  DF02 02 003C              ; Timeout = 60s
```
**Payload**
```
9F02060000000010009A032508219C01005F2A020840DF010101DF0202003C
```

**Response**
```
0x1001
  SW1SW2 9000
  57   13 5413330089012345D25122011234567890F  ; Track 2 equiv
  5A   08 5413330089012345                      ; PAN (may be present)
```
**Payload**
```
900057135413330089012345D25122011234567890F5A085413330089012345
```

---

### Example 2 — EMV Contact (Insert)

**Applicability:** EMV Contact Only — DynaFlex, DynaFlex II PED  

**Request**
```
0x1001
  9F02 06 000000005000      ; Amount 50.00
  9A   03 250821
  9C   01 00
  5F2A 02 0840
  DF01 01 02                ; Entry modes = EMV Contact
  DF02 02 003C
```
**Payload**
```
9F02060000000050009A032508219C01005F2A020840DF010102DF0202003C
```

**Response**
```
0x1001
  SW1SW2 9000
  5A   08 5413330089012345
  9F36 02 0032
  9F27 01 80                ; 80 = ARQC
  9F26 08 4F9A83D12475A1C2  ; Application Cryptogram
```
**Payload**
```
90005A0854133300890123459F360200329F2701809F26084F9A83D12475A1C2
```

---

### Example 3 — Contactless (Tap)

**Applicability:** Contactless Only — DynaProx, DynaFlex II GO  

**Request**
```
0x1001
  9F02 06 000000002500      ; Amount 25.00
  9A   03 250821
  9C   01 00
  5F2A 02 0840
  DF01 01 04                ; Entry modes = CTLS
  DF02 02 001E              ; Timeout = 30s
  DF03 07 9F66 04 E0F0C800  ; TTQ/options
```
**Payload**
```
9F02060000000025009A032508219C01005F2A020840DF010104DF0202001EDF03079F6604E0F0C800
```

**Response**
```
0x1001
  SW1SW2 9000
  57   13 5413330089012345D25122011234567890F
  5A   08 5413330089012345
  9F27 01 40                ; 40 = TC (offline approve)
  9F26 08 7AB45C11882301F4
```
**Payload**
```
900057135413330089012345D25122011234567890F5A0854133300890123459F2701409F26087AB45C11882301F4
```

---

### Example 4 — Manual Card Entry (MCE)

**Applicability:** MCE — DynaFlex II PED, DynaFlex II GO  

**Request**
```
0x1001
  9F02 06 000000001000      ; Amount 10.00
  9A   03 250821
  9C   01 00
  5F2A 02 0840
  DF01 01 08                ; Entry modes = MCE
  DF02 02 003C              ; Timeout = 60s
  DF04 06 01 10 16 01 01 00 ; Prompt config (flags/min/max/CVV requirement/etc.)
```
**Payload**
```
9F02060000000010009A032508219C01005F2A020840DF010108DF0202003CDF0406011016010100
```

**Interactivity:**  
Device prompts PAN → Expiry → CVV2 as directed by `DF04`.

**Response (Success)**
```
0x1001
  SW1SW2 9000
  DF10 08 5413330089012345  ; PAN
  DF11 02 2512              ; Expiry YYMM
  DF12 03 313233            ; "123" (ASCII)
```
**Payload**
```
9000DF10085413330089012345DF11022512DF1203313233
```

**Response (Failure)**
```
0x1001
  SW1SW2 6A80
  DFE0 12 4349565620666F726D6174206572726F72  ; "CIVV format error"
```
**Payload**
```
6A80DFE0124349565620666F726D6174206572726F72
```

---

## Error Conditions

| Status Word (SW1SW2) | Description & Context                                                                 |
|-----------------------|---------------------------------------------------------------------------------------|
| **9000**             | **Success** – The command completed successfully.                                     |
| **6A80**             | **Invalid data** – Command data malformed or not acceptable.                          |
| **6985**             | **Conditions not satisfied** – Required conditions not met (e.g., interface disabled).|
| **6A82**             | **File/record not found** – Requested TLV/key/file is not present.                    |
| **6A83**             | **Authentication method blocked** – Too many failed PIN/auth attempts.                |
| **6A84**             | **Not enough memory space** – Insufficient buffer or storage.                         |
| **6A88**             | **Referenced data not found** – Dependency (e.g., key/certificate) missing.           |
| **6F00**             | **Unknown error / technical issue** – Generic failure; retry after device reset.      |

---

## Notes

- **MSR Only**: Temporary storage of swiped card data is controlled by [Property 1.2.7.1.2.2 – User Event Notification MSR Data Timeout](../Properties/#property-1-2-7-1-2-2).  
- **EMV Contact Only**: An ICC must be physically present in the reader.  
- **Contactless Only**: NFC must be enabled and configured.  
- **MCE Only**: The cardholder uses the device keypad or host UI to enter account data.  
- **(MagTek Internal Only)** Certain DFDF4D/RAAT TLV combinations are reserved and must not be used by host applications.
