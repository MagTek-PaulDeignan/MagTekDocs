---
title: 0x1014 — Get Transaction Status
layout: home
parent: 0x10nn – Transactions
nav_order: 7
---

# 0x1014 — Get Transaction Status

Queries the current transaction state for recovery or verification.

---

## Sequence of Events
1. Host issues **0x1014 — Get Transaction Status**.
2. Device processes the request.
3. Device returns status.

---

## Command Syntax
| Field   | Length | Value   | Description |
|---------|--------|---------|-------------|
| Command | 2      | 0x1014 | Get Transaction Status      |
| TLVs    | var.   | –       | See examples|

---

## Examples
### Request
```
0x1014
  ; (no TLVs unless specified)
```
**Payload**
```
1014
```

### Response
```
0x1014
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
- Prefer notifications; use polling only for recovery.
