---
title: 0x1008 — Cancel Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 5
---

# 0x1008 — Cancel Transaction

Cancels the in‑progress transaction and returns the device to Idle.

---

## When to Use
- User cancellation, application timeout, tender change, or navigation away from payment.

## Preconditions
- A transaction is active or paused (idempotent if not).

## Postconditions
- Prompts are cleared. For EMV Contact, the device may require **Remove Card** before becoming idle.

## Sequence
```
Host SEND 0x1008 → Device aborts / clears prompts → Response
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
| AA 00 81 04 10 08 00 00 |

### Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 08 00 00 90 00 |

---

## Status / Errors
- `90 00` — success
- `69 85` — no transaction in progress

## Implementation Notes
- Send once and wait for the response prior to issuing a new `0x1001`.
