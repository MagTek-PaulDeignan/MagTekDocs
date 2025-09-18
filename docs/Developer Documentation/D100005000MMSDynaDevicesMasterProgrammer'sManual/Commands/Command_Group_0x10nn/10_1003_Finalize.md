---
title: 0x1003 — Finalize Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 3
---

# 0x1003 — Finalize Transaction

Completes a transaction when the device expects a final host step.

---

## When to Use
- After the EMV kernel indicates a final host action, typically via an authorization response code (`8A`).

## Preconditions
- A transaction is awaiting finalization by the host.

## Postconditions
- The device clears prompts and returns to Idle or proceeds per the kernel’s result.

## Sequence
```
Host SEND 0x1003 (+8A) → Device completes → Response
```

---

## TLV Reference — Request
| Tag | Len | Name / Description |
|----:|:---:|---------------------|
| 8A  |  02 | Authorization Response Code |

## TLV Reference — Response
*(none)*

---

## Examples — Full APDUs

### Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 03 00 04 8A 02 30 30 |

### Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 03 00 00 90 00 |

---

## Status / Errors
- `90 00` — success
- `69 85` — no finalizable transaction
- `6A 80` — invalid data

## Implementation Notes
- Provide a correct `8A` value consistent with the host decision.
