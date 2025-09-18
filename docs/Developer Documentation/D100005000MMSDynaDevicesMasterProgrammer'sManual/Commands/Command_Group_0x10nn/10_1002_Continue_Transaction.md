---
title: 0x1002 — Continue Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 2
---

# 0x1002 — Continue Transaction

Resumes a suspended transaction when no additional TLVs are required.

---

## Sequence of Events
1. Host issues **0x1002 — Continue Transaction**.
2. Device processes the request.
3. Device returns status.

---

## Command Syntax
| Field   | Length | Value   | Description |
|---------|--------|---------|-------------|
| Command | 2      | 0x1002 | Continue Transaction      |
| TLVs    | var.   | –       | See examples|

---

## Examples
### Request
```
0x1002
  ; (no TLVs unless specified)
```
**Payload**
```
1002
```

### Response
```
0x1002
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
- Use 0x1004 if issuer data is required.
