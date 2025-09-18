---
title: 0x1001 — Start Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 1
---

# 0x1001 — Start Transaction

Initiates a card-present transaction. The host sends TLVs with amount, currency, and transaction type, plus entry-mode options. The device conducts MSR/ICC/CTLS interactions and returns TLVs with SW1SW2.

---

## When to Use
- To begin any payment that requires cardholder interaction.
- To prepare the reader for specific entry modes (configure `DF01`).

## Preconditions
- Device in **Idle** state; required payment parameters (AIDs/CAPK) installed; adequate power.

## Postconditions
- Device remains engaged until completion, cancellation, or error. Returned TLVs reflect the selected path (MSR/EMV).

## Sequence
```
Host SEND 0x1001 → Device prompts/reads → Response TLVs (EMV/MSR)
```

---

## TLV Reference — Request

| Tag   | Len | Format | Name / Description |
|------:|:---:|:------:|--------------------|
| 9F02  | 06  | BCD    | Amount Authorized (minor units) |
| 9A    | 03  | BCD    | Transaction Date (YYMMDD) |
| 9C    | 01  | Bin    | Transaction Type (`00` Purchase) |
| 5F2A  | 02  | Bin    | Currency Code (ISO‑4217 numeric) |
| 5F36  | 01  | Bin    | Currency Exponent (optional) |
| DF01  | 01  | Bitmask| Allowed Entry Modes: `01` MSR, `02` ICC, `04` CTLS, `08` MCE |
| DF02  | 02  | U16    | Transaction Timeout (seconds) |
| DF03  | var | Bin    | CTLS kernel/TTQ options (optional) |
| DF04  | 01  | Bin    | Locale/Language hint (optional) |

## TLV Reference — Response

| Tag   | Format | Name / Description |
|------:|:------:|--------------------|
| 57    | Bin    | Track 2 Equivalent (do not log in clear) |
| 5A    | Bin    | PAN (do not log in clear) |
| 9F27  | Bin    | Cryptogram Information Data (CID) |
| 9F26  | Bin    | Application Cryptogram |
| 9F10  | Bin    | Issuer Application Data (IAD) |
| 9F34  | Bin    | CVM Results |
| 9F36  | Bin    | Application Transaction Counter (ATC) |
| 9F37  | Bin    | Unpredictable Number |

---

## Examples — Full APDUs

### MSR — Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 01 00 23 9F 02 06 00 00 00 00 50 00 9A 03 25 09 18 9C 01 00 5F 2A 02 08 40 5F 36 01 02 DF 01 01 01 DF 02 02 00 3C |

### MSR — Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 01 00 21 57 13 99 99 99 99 99 99 99 99 D2 51 22 01 12 34 56 78 9F 5A 08 99 99 99 99 99 99 99 99 90 00 |

### Contactless EMV — Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 01 00 1F 9F 02 06 00 00 00 00 25 00 9A 03 25 09 18 9C 01 00 5F 2A 02 08 40 5F 36 01 02 DF 01 01 04 DF 02 02 00 1E |

### Contactless EMV — Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 01 00 1F 9F 27 01 40 9F 26 08 11 22 33 44 55 66 77 88 9F 10 07 06 01 12 03 A0 B0 01 9F 34 03 1E 03 00 90 00 |

### Contact (ICC, fallbacks allowed) — Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 01 00 1C 9F 02 06 00 00 00 01 00 00 9A 03 25 09 18 9C 01 00 5F 2A 02 08 40 DF 01 01 07 DF 02 02 00 3C |

### Contact (ICC) — Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 01 00 1B 9F 27 01 40 9F 26 08 AA BB CC DD EE FF 00 11 9F 10 07 06 01 12 03 A0 B0 02 9F 36 02 00 2A 9F 37 04 12 34 56 78 90 00 |

---

## Status / Errors
- `90 00` — success
- `69 85` — conditions not satisfied (incorrect state or interface unavailable)
- `6A 80` — invalid data (malformed TLV set)
- `6F 00` — unknown error

## Implementation Notes
- Select a single entry mode for optimal user experience; enable fallbacks only when required.
- Mask `5A` and `57` in logs; never persist cryptograms or track data in clear text.
- Do not issue another `0x1001` until the current flow completes or is canceled with `0x1008`.
