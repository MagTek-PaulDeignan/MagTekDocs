---
title: Command 0x1014 Get Transaction Status
layout: home
parent: Command Group 0x10nn
nav_order: 7
---

# Command 0x1014 Get Transaction Status

Query the current transaction state for recovery/verification.

---

## When to Use
- Recovery or verification when event-driven updates are unavailable.

## Preconditions
- None.

## Postconditions
- Returns current status; use properties/notifications for detail.

## Sequence
```
Host SEND 0x1014  →  Device returns state  →  Response
```

---

## Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 14 00 00 |

## Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 14 00 00 90 00 |

---

## Status / Errors
- `90 00` success
- `69 85` no active/suspended transaction

## Notes
- Prefer notifications; limit polling to recovery scenarios.
