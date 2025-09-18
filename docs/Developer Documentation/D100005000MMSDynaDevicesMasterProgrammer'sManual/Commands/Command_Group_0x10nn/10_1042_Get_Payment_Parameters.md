---
title: 0x1042 — Get Payment Parameters
layout: home
parent: 0x10nn – Transactions
nav_order: 9
---

# 0x1042 — Get Payment Parameters

Reads payment parameter block(s) from the device.

---

## Sequence of Events
1. Host issues **0x1042 — Get Payment Parameters**.
2. Device processes the request.
3. Device returns status.

---

## Command Syntax
| Field   | Length | Value   | Description |
|---------|--------|---------|-------------|
| Command | 2      | 0x1042 | Get Payment Parameters      |
| TLVs    | var.   | –       | See examples|

---

## Examples
### Request
```
0x1042
  ; (no TLVs unless specified)
```
**Payload**
```
1042
```

### Response
```
0x1042
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
- Large responses may be segmented by transport.
