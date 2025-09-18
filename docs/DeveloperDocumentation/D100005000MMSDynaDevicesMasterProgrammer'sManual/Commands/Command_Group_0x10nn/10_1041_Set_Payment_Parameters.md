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

**Preconditions**
- Device is Idle.
- Parameter container prepared for target firmware/device.

**Steps**
1. Host issues **0x1041 — Set Payment Parameters** with parameter container TLVs.
2. Device validates container version and dependencies.
3. Device applies parameters.
4. Device returns status word.

**Error/Recovery**
- On `6A 80`/`6A 84`/`6A 88`, correct the container (format/memory/dependency) and resend.

---

## Applicability Matrix

| Transaction Interface | DynaFlex | DynaFlex II PED | DynaProx | DynaFlex II GO |
|----------------------:|:--------:|:---------------:|:--------:|:--------------:|
| All (out of band)     | ✅       | ✅              | ✅       | ✅             |

---

## Command Syntax

| Field   | Length | Value  | Description                |
|---------|--------|--------|----------------------------|
| Command | 2      | 0x1041 | Set Payment Parameters     |
| TLVs    | var.   | —      | Parameter container (DF10) |

---

## Examples

> No public request/response APDU examples are provided in D100005000-103. Use the device‑specific container format documented for your firmware.

---

## Error Conditions

| SW1SW2 | Meaning                    |
|--------|-----------------------------|
| 9000   | Success                     |
| 6A80   | Invalid data / bad format   |
| 6A84   | Insufficient memory         |
| 6A88   | Referenced data not found   |
| 6F00   | Unknown error               |

---

## Notes
- Maintain a versioned baseline of parameters; limit writes to changes only.
