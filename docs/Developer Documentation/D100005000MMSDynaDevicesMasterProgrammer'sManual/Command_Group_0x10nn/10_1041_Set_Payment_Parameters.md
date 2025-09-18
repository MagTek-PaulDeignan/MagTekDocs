---
title: 0x1041 — Set Payment Parameters
layout: home
parent: 0x10nn – Transactions
nav_order: 8
---

# 0x1041 — Set Payment Parameters

Write payment parameter block(s) to the device.

---

## When to Use
- During initialization or parameter updates (not mid-transaction).

## Preconditions
- Valid container format for the target device/firmware.

## Postconditions
- Parameters validated/applied; device remains idle/busy per operation.

## Sequence
```
Host SEND 0x1041(+container)  →  Device validates/applies  →  Response
```

---

## Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 41 00 07 DF 10 04 01 02 03 04 |

## Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 41 00 00 90 00 |

---

## Status / Errors
- `90 00` success
- `6A 80` invalid data
- `6A 84` not enough memory
- `6A 88` dependency missing

## Notes & Gotchas
- Keep a versioned “golden” set; avoid sending unnecessary groups.
