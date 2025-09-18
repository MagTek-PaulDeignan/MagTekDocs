---
title: Command 0x1008 Cancel Transaction
layout: home
parent: Command Group 0x10nn
nav_order: 5
---

# Command 0x1008 Cancel Transaction

Cancel the in‑progress transaction and return to Idle.

---

## When to Use
- User cancel, app timeout, tender switch.

## Preconditions
- A transaction is active or paused (idempotent if not).

## Postconditions
- Prompts cleared; ICC may require Remove Card before Idle.

## Sequence
```
Host SEND 0x1008  →  Device aborts  →  Response
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

## Notes
- Send once and wait for response before issuing a new 0x1001.
