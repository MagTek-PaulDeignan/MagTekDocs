---
title: 0x1008 — Cancel Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 5
---

# 0x1008 — Cancel Transaction

Cancel the in‑progress transaction and return to Idle.

---

## When to Use
- User cancel, app timeout, tender switch, or navigation away from payment.

## Preconditions
- A transaction is active or paused (idempotent if not).

## Postconditions
- Device clears prompts; EMV contact may require **Remove Card** prompt.

## Sequence
```
Host SEND 0x1008  →  Device aborts/clears prompts  →  Response
```

---

## Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 08 00 00 |

## Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 08 00 00 90 00 |

---

## Status / Errors
- `90 00` success
- `69 85` no transaction in progress

## Notes & Gotchas
- Send once and wait for the response before issuing a new **0x1001**.
