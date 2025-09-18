---
title: Command 0x1009 Close / Clear Transaction
layout: home
parent: Command Group 0x10nn
nav_order: 6
---

# Command 0x1009 Close / Clear Transaction

Clear residual transaction state and return the device to Idle.

---

## When to Use
- After transport drops, app restarts, or uncertain state.

## Preconditions
- None (safe to call in any state).

## Postconditions
- Device ends in Idle; may prompt Remove Card for ICC.

## Sequence
```
Host SEND 0x1009  →  Device clears state  →  Response
```

---

## Request
| Example (Hex) |
|---------------|
| AA 00 81 04 10 09 00 00 |

## Response
| Example (Hex) |
|---------------|
| AA 00 82 04 10 09 00 00 90 00 |

---

## Status / Errors
- `90 00` success
- `69 85` nothing to clear

## Notes
- Recovery handshake: 0x1009 → (optional) 0x1014 → 0x1001.
