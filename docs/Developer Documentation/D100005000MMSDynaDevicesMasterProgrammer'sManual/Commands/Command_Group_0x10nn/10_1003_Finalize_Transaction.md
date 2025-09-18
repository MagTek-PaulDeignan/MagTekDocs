---
title: Command 0x1003 Finalize Transaction
layout: home
parent: Command Group 0x10nn
nav_order: 3
---

# Command 0x1003 Finalize Transaction

Complete a managed transaction when the device expects a final host step.

---

## When to Use
- After EMV decision requiring a final host action code (8A).

## Preconditions
- Transaction awaiting finalization from host.

## Postconditions
- Device returns to Idle or next step per kernel.

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

## Notes
- Always include a correct `8A` value per host decision.
