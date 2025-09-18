---
title: 0x1042 — Get Payment Parameters
layout: home
parent: 0x10nn – Transactions
nav_order: 9
---

# 0x1042 — Get Payment Parameters

Reads payment parameter block(s) from the device.

---

## When to Use
- Verification, export, or diagnostics.

## Preconditions
- None.

## Postconditions
- Returned block(s) reflect the currently applied parameters.

## Sequence
```
Host SEND 0x1042 → Device returns block(s) → Response
```

---

## TLV Reference — Request
*(none)*

## TLV Reference — Response
| Tag  | Len | Name / Description |
|-----:|:---:|---------------------|
| DF10 | var | Payment parameter container |

---

## Examples — Full APDUs

### Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 42 00 00 |

### Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 42 00 06 DF 10 04 01 02 03 04 90 00 |

---

## Status / Errors
- `90 00` — success
- `6A 82` — not found
- `6A 80` — invalid query

## Implementation Notes
- Keep queries narrow. Large responses may require segmentation depending on transport.
