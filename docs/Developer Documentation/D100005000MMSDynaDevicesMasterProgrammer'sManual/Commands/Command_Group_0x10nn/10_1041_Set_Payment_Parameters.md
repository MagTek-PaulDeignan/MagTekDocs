---
title: 0x1041 — Set Payment Parameters
layout: home
parent: 0x10nn – Transactions
nav_order: 8
---

# 0x1041 — Set Payment Parameters

Writes payment parameter block(s) to the device.

---

## Sequence of Events
1. Host issues **0x1041 — Set Payment Parameters**.
2. Device processes the request.
3. Device returns status.

---

## Command Syntax
| Field   | Length | Value   | Description |
|---------|--------|---------|-------------|
| Command | 2      | 0x1041 | Set Payment Parameters      |
| TLVs    | var.   | –       | See examples|

---

## Examples
### Request
```
0x1041
  ; (no TLVs unless specified)
```
**Payload**
```
1041
```

### Response
```
0x1041
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
- Maintain a versioned baseline; avoid unnecessary writes.
