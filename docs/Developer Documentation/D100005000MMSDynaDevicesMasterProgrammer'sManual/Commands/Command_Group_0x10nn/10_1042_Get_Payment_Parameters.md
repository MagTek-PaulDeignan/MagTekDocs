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

**Preconditions**
- None.

**Steps**
1. Host issues **0x1042 — Get Payment Parameters**.
2. Device returns the requested container or an error status.

**Error/Recovery**
- If not found, verify container IDs/versions and retry.

---

## Applicability Matrix

| Transaction Interface | DynaFlex | DynaFlex II PED | DynaProx | DynaFlex II GO |
|----------------------:|:--------:|:---------------:|:--------:|:--------------:|
| All (out of band)     | ✅       | ✅              | ✅       | ✅             |

---

## Command Syntax

| Field   | Length | Value  | Description                |
|---------|--------|--------|----------------------------|
| Command | 2      | 0x1042 | Get Payment Parameters     |
| TLVs    | var.   | —      | Parameter query (DF10)     |

---

## Examples

> No public request/response APDU examples are provided in D100005000-103. Use the device‑specific container identifiers defined for your firmware.

---

## Error Conditions

| SW1SW2 | Meaning              |
|--------|----------------------|
| 9000   | Success              |
| 6A82   | Not found            |
| 6A80   | Invalid query        |
| 6F00   | Unknown error        |

---

## Notes
- Response size may require segmentation depending on transport; keep queries narrow.
