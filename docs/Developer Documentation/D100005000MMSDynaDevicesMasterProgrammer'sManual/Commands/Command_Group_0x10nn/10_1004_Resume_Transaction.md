---
title: Command 0x1004 Resume Transaction
layout: home
parent: Command Group 0x10nn
nav_order: 4
---

# Command 0x1004 Resume Transaction

Resume a paused transaction and provide issuer/host data (e.g., ARPC).

---

## When to Use
- Device is waiting for host/issuer data to proceed.

## Preconditions
- Transaction paused and awaiting host input.

## Postconditions
- Device processes provided TLVs and continues.

## Sequence
```
Host SEND 0x1004(+TLVs)  →  Device resumes  →  Response
```

---

## Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 04 00 0E 81 01 00 91 08 12 34 56 78 90 AB CD EF 8A 02 30 30 |

## Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 04 00 00 90 00 |

---

## Status / Errors
- `90 00` success
- `69 85` no resumable transaction
- `6A 80` invalid data

## Notes
- Include `81` (resume code) and `91` (issuer data) as required by flow.
