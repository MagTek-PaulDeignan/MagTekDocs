---
title: 0x1042 — Get Payment Parameters
layout: home
parent: 0x10nn – Transactions
nav_order: 9
---

# 0x1042 — Get Payment Parameters

Read payment parameter block(s) from the device.

---

## When to Use
- Verification, export, or diagnostics.

## Preconditions
- None.

## Postconditions
- Returned block(s) reflect current applied parameters.

## Sequence
```
Host SEND 0x1042  →  Device returns block(s)  →  Response
```

---

## Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 42 00 00 |

## Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 42 00 07 DF 10 04 01 02 03 04 90 00 |

---

## Status / Errors
- `90 00` success
- `6A 82` not found
- `6A 80` invalid query

## Notes & Gotchas
- Keep queries narrow; large responses may segment based on transport.
