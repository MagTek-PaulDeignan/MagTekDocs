---
title: 0x1002 — Continue Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 2
---

# 0x1002 — Continue Transaction

Resume a suspended transaction when no additional TLVs are required.

---

## When to Use
- Device indicated a pause that only needs continuation (no ARPC/host data).

## Preconditions
- A transaction is suspended/paused by the device.

## Postconditions
- Device resumes processing; subsequent outcome delivered by normal flow.

## Sequence
```
Host SEND 0x1002  →  Device resumes  →  Response
```

---

## Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 02 00 00 |

## Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 02 00 00 90 00 |

---

## Status / Errors
- `90 00` success
- `69 85` no resumable state

## Notes & Gotchas
- If the device requires issuer data, use **0x1004 Resume** instead.
