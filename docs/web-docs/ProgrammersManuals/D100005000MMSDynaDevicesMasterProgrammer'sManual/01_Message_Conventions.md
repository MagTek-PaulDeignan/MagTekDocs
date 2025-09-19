---
title: Message Conventions
layout: home
parent: Dyna Devices Master Programmer's Manual
nav_order: 3
---

# Message Conventions

MagTek devices use a **Request/Response** wrapper with embedded **TLV (Tag-Length-Value) payloads**. Notifications also use the same framing.

---

## Wrapper Format

All messages are framed with:

- **Header** – includes message type, length, and command ID.  
- **Payload** – TLVs (Tag-Length-Value).  
- **Status Word (SW1SW2)** – returned in responses to indicate outcome.

Example wrapper (hex):

```text
AA 00 81 04 01 00 10 01 ...
```

Where `1001` = Start Transaction command.

---

## TLV Encoding

- **Tag**: 1–3 bytes identifying the field (e.g., `9F02`).  
- **Length**: short or extended (`81 nn`, `82 nn nn`).  
- **Value**: raw data (binary, BCD, or ASCII depending on tag).

**Worked Example:**

```text
9F02 06 000000010000
```

- `9F02` = Amount Authorized  
- `06` = length (6 bytes)  
- `000000010000` = $100.00 in cents

---

## Common Tags

| Tag   | Field                | Direction      | Notes                    |
|-------|----------------------|----------------|--------------------------|
| 9F02  | Amount Authorized    | Host → Device  | 6-byte BCD               |
| 9A    | Transaction Date     | Host → Device  | YYMMDD                   |
| 9C    | Transaction Type     | Host → Device  | 00 = Purchase            |
| 5F2A  | Currency Code        | Host → Device  | ISO 4217 numeric (e.g., USD = 0840) |
| 57    | Track 2 Equivalent   | Device → Host  | Masked in logs           |
| 5A    | PAN                  | Device → Host  | Sensitive, mask in logs  |
| 9F26  | Cryptogram           | Device → Host  | EMV-generated value      |

---

## Status Words (SW1SW2)

- `9000` — Success  
- `6985` — Conditions not satisfied (wrong state, no card)  
- `6A80` — Invalid data (bad TLV, unsupported tag)  
- `6F00` — Unknown error

**Error Handling Flow:**

1. If `9000` → proceed.  
2. If `6985` → check device state, possibly retry.  
3. If `6A80` → rebuild TLV set, resend.  
4. If `6F00` → reset or re-establish connection.

---

## Notifications

Devices may emit notifications without a host command:

- **Device Info** (on connect)  
- **Battery State** (when low or charging)  
- **Transaction Updates** (during card interaction)

Your application must be prepared to receive and parse these asynchronously.

---

## Logging Guidelines

- **Never log clear PAN, Track, or cryptograms.**  
- Truncate or mask sensitive fields (`5A`, `57`).  
- Do not persist encrypted blobs unless required for audit.  
- Always scrub logs in compliance with PCI DSS.
