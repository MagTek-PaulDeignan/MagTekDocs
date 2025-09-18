---
title: 0x1004 — Resume Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 4
---

# 0x1004 — Resume Transaction

Resumes a paused transaction and supplies issuer/host data as required.

---

## Sequence of Events
1. Host issues **0x1004 — Resume Transaction**.
2. Device processes the request.
3. Device returns status.

---

## Command Syntax
| Field   | Length | Value   | Description |
|---------|--------|---------|-------------|
| Command | 2      | 0x1004 | Resume Transaction      |
| TLVs    | var.   | –       | See examples|

---

## Examples
### Request
```
0x1004
  ; (no TLVs unless specified)
```
**Payload**
```
1004
```

### Response
```
0x1004
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
- Ensure TLVs 81/91/8A are correctly formed.
