---
title: Command 0x1001 Start Transaction
layout: home
parent: Command Group 0x10nn
nav_order: 1
---

# Command 0x1001 Start Transaction

The host uses this command to start a payment transaction.

---

## Sequence of Events

1. If user event notifications are enabled, a card may be presented **before** this command. The device will notify the host to initiate a transaction.
2. **MSR only:** If the card is swiped early, the device temporarily stores swipe data for a configurable timeout.
3. The host calls **Start Transaction** (`0x1001`).
4. The device guides the cardholder (MSR, EMV Contact, Contactless, or MCE) and returns transaction data with a status.

---

## Applicability Matrix

| Transaction Interface | DynaFlex | DynaFlex II PED | DynaProx | DynaFlex II GO |
|----------------------:|:--------:|:---------------:|:--------:|:--------------:|
| MSR (Swipe)           | ✅       | ✅              | ❌       | ✅             |
| EMV Contact           | ✅       | ✅              | ❌       | ✅             |
| EMV Contactless       | ✅       | ✅              | ✅       | ✅             |
| MCE (Manual)          | ✅       | ✅              | ❌       | ❌             |
| Barcode Reader        | ✅       | ✅              | ✅       | ✅             |

---

## Command Syntax

| Field   | Length | Value   | Description           |
|---------|--------|---------|-----------------------|
| Command | 2      | 0x1001  | Start Transaction     |
| TLVs    | var.   | –       | See below             |

### Required TLVs

| Tag    | Name                       | Description                                        |
|--------|----------------------------|----------------------------------------------------|
| DFDF4D | Transaction Control Flags  | Controls available interfaces and flow             |
| RAAT   | Reader Action/Access Type *(internal)* | Sets which actions the reader should allow |

---

## Examples

### Example 1 — MSR (Swipe)

**Request TLVs**
<div class="code-box" data-label="Payload">

```text
9F0206000000001000
9A03250821
9C0100
5F2A020840
DF010101
DF0202003C
```

</div>

**Full APDU — Request**
| Example (Hex) |
|---------------|
| AA 00 81 04 10 01 00 17 9F 02 06 00 00 00 00 10 00 9A 03 25 08 21 9C 01 00 5F 2A 02 08 40 DF 01 01 01 DF 02 02 00 3C |

**Response TLVs**
<div class="code-box" data-label="Payload">

```text
9000
57 13 54 13 33 00 89 01 23 45 D2 51 22 01 12 34 56 78 90 F
5A 08 54 13 33 00 89 01 23 45
```

</div>

**Full APDU — Response**
| Example (Hex) |
|---------------|
| AA 00 82 04 10 01 00 1B 57 13 54 13 33 00 89 01 23 45 D2 51 22 01 12 34 56 78 90 F 5A 08 54 13 33 00 89 01 23 45 90 00 |

---

### Example 2 — EMV Contact (Insert)

**Request TLVs**
<div class="code-box" data-label="Payload">

```text
9F0206000000005000
9A03250821
9C0100
5F2A020840
DF010102
DF0202003C
```

</div>

**Full APDU — Request**
| Example (Hex) |
|---------------|
| AA 00 81 04 10 01 00 17 9F 02 06 00 00 00 00 50 00 9A 03 25 08 21 9C 01 00 5F 2A 02 08 40 DF 01 01 02 DF 02 02 00 3C |

**Response TLVs**
<div class="code-box" data-label="Payload">

```text
9000
5A 08 54 13 33 00 89 01 23 45
9F36 02 00 32
9F27 01 80
9F26 08 4F 9A 83 D1 24 75 A1 C2
```

</div>

**Full APDU — Response**
| Example (Hex) |
|---------------|
| AA 00 82 04 10 01 00 15 5A 08 54 13 33 00 89 01 23 45 9F 36 02 00 32 9F 27 01 80 9F 26 08 4F 9A 83 D1 24 75 A1 C2 90 00 |

---

### Example 3 — Contactless (Tap)

**Request TLVs**
<div class="code-box" data-label="Payload">

```text
9F0206000000002500
9A03250821
9C0100
5F2A020840
DF010104
DF0202001E
DF03079F6604E0F0C800
```

</div>

**Full APDU — Request**
| Example (Hex) |
|---------------|
| AA 00 81 04 10 01 00 20 9F 02 06 00 00 00 00 25 00 9A 03 25 08 21 9C 01 00 5F 2A 02 08 40 DF 01 01 04 DF 02 02 00 1E DF 03 07 9F 66 04 E0 F0 C8 00 |

**Response TLVs**
<div class="code-box" data-label="Payload">

```text
9000
57 13 54 13 33 00 89 01 23 45 D2 51 22 01 12 34 56 78 90 F
5A 08 54 13 33 00 89 01 23 45
9F27 01 40
9F26 08 7A B4 5C 11 88 23 01 F4
```

</div>

**Full APDU — Response**
| Example (Hex) |
|---------------|
| AA 00 82 04 10 01 00 23 57 13 54 13 33 00 89 01 23 45 D2 51 22 01 12 34 56 78 90 F 5A 08 54 13 33 00 89 01 23 45 9F 27 01 40 9F 26 08 7A B4 5C 11 88 23 01 F4 90 00 |

---

### Example 4 — Manual Card Entry (MCE)

**Request TLVs**
<div class="code-box" data-label="Payload">

```text
9F0206000000001000
9A03250821
9C0100
5F2A020840
DF010108
DF0202003C
DF0406011016010100
```

</div>

**Full APDU — Request**
| Example (Hex) |
|---------------|
| AA 00 81 04 10 01 00 1F 9F 02 06 00 00 00 00 10 00 9A 03 25 08 21 9C 01 00 5F 2A 02 08 40 DF 01 01 08 DF 02 02 00 3C DF 04 06 01 10 16 01 01 00 |

**Response (Success) TLVs**
<div class="code-box" data-label="Payload">

```text
9000
DF10 08 54 13 33 00 89 01 23 45
DF11 02 25 12
DF12 03 31 32 33
```

</div>

**Full APDU — Response**
| Example (Hex) |
|---------------|
| AA 00 82 04 10 01 00 13 DF 10 08 54 13 33 00 89 01 23 45 DF 11 02 25 12 DF 12 03 31 32 33 90 00 |

---

## Error Conditions

| SW1SW2 | Description |
|--------|-------------|
| 9000   | Success |
| 6A80   | Invalid data |
| 6985   | Conditions not satisfied |
| 6A82   | File/record not found |
| 6A83   | Authentication method blocked |
| 6A84   | Not enough memory space |
| 6A88   | Referenced data not found |
| 6F00   | Unknown error |
