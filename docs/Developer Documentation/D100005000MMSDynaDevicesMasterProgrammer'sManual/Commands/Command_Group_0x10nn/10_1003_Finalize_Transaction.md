---
title: 0x1003 — Finalize Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 3
---

# 0x1003 — Finalize Transaction

Completes a transaction when the device expects a final host action (e.g., Authorization Response Code).

---

## Sequence of Events
1. Host issues **0x1003 — Finalize Transaction**.
2. Device processes the request.
3. Device returns status.

---

## Command Syntax
| Field   | Length | Value   | Description |
|---------|--------|---------|-------------|
| Command | 2      | 0x1003 | Finalize Transaction      |
| TLVs    | var.   | –       | See examples|

---

## Examples
### Request
```
0x1003
  ; (no TLVs unless specified)
```
**Payload**
```
1003
```

### Response
```
0x1003
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
- Provide correct 8A value matching host decision.
