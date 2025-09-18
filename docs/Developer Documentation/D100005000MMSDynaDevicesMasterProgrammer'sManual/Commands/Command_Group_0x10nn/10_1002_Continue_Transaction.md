---
title: Command 0x1002 Continue Transaction
layout: home
parent: Command Group 0x10nn
nav_order: 2
---

# Command 0x1002 Continue Transaction

Resume a suspended transaction when no additional TLVs are required.

---

## When to Use
- Device indicated a pause requiring only continuation.

## Preconditions
- Transaction is paused by the device.

## Postconditions
- Device resumes EMV flow or card processing.

## Sequence
```
Host SEND 0x1002  →  Device resumes  →  Response
```

---

## Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 02 00 00 |

## Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 02 00 00 90 00 |

---

## Status / Errors
- `90 00` success
- `69 85` no resumable state

## Notes
- If device expects issuer data, use 0x1004 instead.
