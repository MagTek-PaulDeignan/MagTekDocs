---
title: 0x1009 — Close / Clear Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 6
---

# 0x1009 — Close / Clear Transaction

Clear residual transaction state and return the device to **Idle**.

---

## When to Use
- After transport drops, app restarts, or uncertain state.
- Immediately after reconnecting, before starting a new transaction.

## Preconditions
- None. Safe to call in any state.

## Postconditions
- Prompts cleared; volatile caches reset; device in **Idle** (or waiting for **Remove Card** if ICC present).

## Sequence
```
Host SEND 0x1009  →  Device clears state  →  Response
```

---

## Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 09 00 00 |

## Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 09 00 00 90 00 |

---

## Status / Errors
- `90 00` success
- `69 85` nothing to clear

## Notes & Gotchas
- Idempotent. If an ICC card is inserted, user may be prompted to remove before Idle.
- Recovery handshake: 1) `0x1009` → 2) optional `0x1014` → 3) `0x1001`.
