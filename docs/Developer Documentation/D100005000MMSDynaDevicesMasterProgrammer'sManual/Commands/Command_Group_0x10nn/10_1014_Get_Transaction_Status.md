---
title: 0x1014 — Get Transaction Status
layout: home
parent: 0x10nn – Transactions
nav_order: 7
---

# 0x1014 — Get Transaction Status

Queries the current transaction state.

---

## When to Use
- Recovery or verification when event-driven updates are unavailable.

## Preconditions
- None.

## Postconditions
- Returns a status word indicating success; use notifications or properties for detailed state.

## Sequence
```
Host SEND 0x1014 → Device returns current state → Response
```

---

## TLV Reference — Request
*(none)*

## TLV Reference — Response
*(none)*

---

## Examples — Full APDUs

### Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 14 00 00 |

### Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 14 00 00 90 00 |

---

## Status / Errors
- `90 00` — success
- `69 85` — no active or suspended transaction

## Implementation Notes
- Prefer notifications for real-time state; use polling only for recovery scenarios.
