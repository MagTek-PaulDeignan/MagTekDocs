---
title: Command 0x1041 Set Payment Parameters
layout: home
parent: Command Group 0x10nn
nav_order: 8
---

# Command 0x1041 Set Payment Parameters

Write payment parameter block(s) to the device.

---

## When to Use
- Initialization or parameter updates (not mid-transaction).

## Preconditions
- Valid container format; device idle.

## Postconditions
- Parameters validated/applied.

## Sequence
```
Host SEND 0x1041(+container)  →  Device applies  →  Response
```

---

## Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 41 00 06 DF 10 04 01 02 03 04 |

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

## Notes
- Keep versioned parameter sets; avoid unnecessary writes.
