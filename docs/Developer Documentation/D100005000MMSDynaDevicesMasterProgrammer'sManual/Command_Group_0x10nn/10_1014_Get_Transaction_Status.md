---
title: 0x1014 — Get Transaction Status
layout: home
parent: 0x10nn – Transactions
nav_order: 7
---

# 0x1014 — Get Transaction Status

Query the current transaction state.

---

## When to Use
- Recovery or verification when event-driven updates are unavailable.

## Preconditions
- None.

## Postconditions
- Returns a status word indicating success; use notifications or properties for rich state.

## Sequence
```
Host SEND 0x1014  →  Device returns current state  →  Response
```

---

## Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 14 00 00 |

## Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 14 00 00 90 00 |

---

## Status / Errors
- `90 00` success
- `69 85` no active/suspended transaction

## Notes & Gotchas
- Prefer notifications; polling should be limited to recovery scenarios.
