---
title: 0x1009 — Close / Clear Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 6
---

# 0x1009 — Close / Clear Transaction

Clears residual transaction state and returns the device to Idle.

---

## Sequence of Events
1. Host issues **0x1009 — Close / Clear Transaction**.
2. Device processes the request.
3. Device returns status.

---

## Command Syntax
| Field   | Length | Value   | Description |
|---------|--------|---------|-------------|
| Command | 2      | 0x1009 | Close / Clear Transaction      |
| TLVs    | var.   | –       | See examples|

---

## Examples
### Request
```
0x1009
  ; (no TLVs unless specified)
```
**Payload**
```
1009
```

### Response
```
0x1009
  SW1SW2 9000
```
**Payload**
```
9000
```

---

## Error Conditions
| Status Word | Description |
|-------------|-------------|
| 9000        | Success     |
| 6985        | Conditions not satisfied |

---

## Notes
- Use after recovery before restarting transaction.
