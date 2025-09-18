---
title: 0x1002 — Continue Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 2
---

# 0x1002 — Continue Transaction

Resumes a suspended transaction when no additional TLVs are required.

---

## When to Use
- The device has paused and indicated continuation without additional data.

## Preconditions
- A transaction is currently paused by the device.

## Postconditions
- The device resumes processing; the outcome is provided by subsequent responses or notifications.

## Sequence
```
Host SEND 0x1002 → Device resumes → Response
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
| AA 00 81 04 10 02 00 00 |

### Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 02 00 00 90 00 |

---

## Status / Errors
- `90 00` — success
- `69 85` — no resumable state

## Implementation Notes
- If the device requires issuer data, use `0x1004 Resume Transaction` instead.
