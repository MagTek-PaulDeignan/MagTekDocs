---
title: 0x1004 — Resume Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 4
---

# 0x1004 — Resume Transaction

Resumes a paused transaction and supplies issuer/host data (for example, ARPC).

---

## When to Use
- The device is waiting for host or issuer data to proceed.

## Preconditions
- The transaction is paused and specifically awaiting host input.

## Postconditions
- The device processes the provided data and continues the flow.

## Sequence
```
Host SEND 0x1004 (+TLVs) → Device resumes → Response
```

---

## TLV Reference — Request
| Tag | Len | Name / Description |
|----:|:---:|---------------------|
| 81  |  01 | Resume Code |
| 91  |  08 | Issuer Authentication Data / ARPC |
| 8A  |  02 | Authorization Response Code |

## TLV Reference — Response
*(none)*

---

## Examples — Full APDUs

### Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 04 00 0E 81 01 00 91 08 12 34 56 78 90 AB CD EF 8A 02 30 30 |

### Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 04 00 00 90 00 |

---

## Status / Errors
- `90 00` — success
- `69 85` — no resumable transaction
- `6A 80` — invalid data

## Implementation Notes
- Ensure `81`/`91`/`8A` are constructed as required by the transaction flow.
