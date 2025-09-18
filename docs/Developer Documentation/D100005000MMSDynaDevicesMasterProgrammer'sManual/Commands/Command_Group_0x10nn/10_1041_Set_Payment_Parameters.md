---
title: 0x1041 — Set Payment Parameters
layout: home
parent: 0x10nn – Transactions
nav_order: 8
---

# 0x1041 — Set Payment Parameters

Writes payment parameter block(s) to the device.

---

## When to Use
- During initialization or parameter updates (not during a transaction).

## Preconditions
- Valid container format for the target device and firmware.

## Postconditions
- Parameters are validated and applied. The device remains idle or busy depending on the operation.

## Sequence
```
Host SEND 0x1041 (+container) → Device validates/applies → Response
```

---

## TLV Reference — Request
| Tag  | Len | Name / Description |
|-----:|:---:|---------------------|
| DF10 | var | Payment parameter container |

## TLV Reference — Response
*(none)*

---

## Examples — Full APDUs

### Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 41 00 06 DF 10 04 01 02 03 04 |

### Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 41 00 00 90 00 |

---

## Status / Errors
- `90 00` — success
- `6A 80` — invalid data
- `6A 84` — insufficient memory
- `6A 88` — dependency missing

## Implementation Notes
- Maintain a versioned “golden” parameter set; avoid unnecessary writes.
