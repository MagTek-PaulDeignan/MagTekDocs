---
title: 0x1003 — Finalize Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 3
---

# 0x1003 — Finalize Transaction

Complete a managed transaction when the device expects a final host step.

---

## When to Use
- After an EMV kernel indicates the host must finalize with a result code.

## Preconditions
- Transaction is awaiting finalization from host.

## Postconditions
- Device clears prompts and returns to Idle (or next step per kernel).

## Sequence
```
Host SEND 0x1003(+8A)  →  Device completes  →  Response
```

---

## Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 03 00 04 8A 02 30 30 |

## Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 03 00 00 90 00 |

---

## Status / Errors
- `90 00` success
- `69 85` no finalizable transaction
- `6A 80` invalid data

## Notes & Gotchas
- Include `8A` (Authorization Response Code) as required by the flow.
