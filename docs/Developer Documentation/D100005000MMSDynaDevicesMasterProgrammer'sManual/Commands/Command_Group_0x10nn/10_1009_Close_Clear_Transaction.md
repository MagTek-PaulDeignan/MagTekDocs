---
title: 0x1009 — Close / Clear Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 6
---

# 0x1009 — Close / Clear Transaction

Clears residual transaction state and returns the device to **Idle**.

---

## When to Use
- After transport interruptions, application restarts, or any uncertain state.
- Immediately after reconnecting, before starting a new transaction.

## Preconditions
- None. This command is safe to issue in any state.

## Postconditions
- Prompts are dismissed; volatile caches are reset; the device is idle (or awaiting **Remove Card** if an ICC is present).

## Sequence
```
Host SEND 0x1009 → Device clears state → Response
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
| AA 00 81 04 10 09 00 00 |

### Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 09 00 00 90 00 |

---

## Status / Errors
- `90 00` — success
- `69 85` — nothing to clear

## Implementation Notes
- This command is idempotent. If an ICC is inserted, the device may prompt for removal before becoming idle.
- Recommended recovery sequence: `0x1009` → (optional) `0x1014` → `0x1001`.
