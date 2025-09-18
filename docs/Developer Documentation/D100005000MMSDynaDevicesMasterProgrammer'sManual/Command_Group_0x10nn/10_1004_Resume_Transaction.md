---
title: 0x1004 — Resume Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 4
---

# 0x1004 — Resume Transaction

Resume a paused transaction and provide issuer/host data (e.g., ARPC).

---

## When to Use
- Device is waiting for host data to proceed (ARPC, updated TLVs).

## Preconditions
- Transaction is paused/suspended and specifically awaiting host input.

## Postconditions
- Device processes provided data and continues the flow.

## Sequence
```
Host SEND 0x1004(+TLVs)  →  Device resumes  →  Response
```

---

## Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 04 00 11 81 01 00 91 08 12 34 56 78 90 AB CD EF 8A 02 30 30 |

## Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 04 00 00 90 00 |

---

## Status / Errors
- `90 00` success
- `69 85` no resumable transaction
- `6A 80` invalid data

## Notes & Gotchas
- Use `81` (Resume Code) and include `91` (ARPC data) / `8A` as your flow requires.
