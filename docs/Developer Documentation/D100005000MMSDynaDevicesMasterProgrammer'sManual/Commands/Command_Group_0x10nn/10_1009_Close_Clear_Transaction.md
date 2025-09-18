---
title: 0x1009 — Close / Clear Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 6
---

# 0x1009 — Close / Clear Transaction

Clears residual transaction state and returns the device to Idle. Use for recovery after transport drops or host restarts.

---

## Sequence of Events

**Preconditions**
- None. Safe to issue in any device state.

**Steps**
1. Host issues **0x1009 — Close / Clear Transaction**.
2. Device clears volatile state and prompts (if any).  
   - If ICC is inserted, device may require **Remove Card** first.
3. Device returns a response and idles.

**Error/Recovery**
- If `69 85` (nothing to clear), proceed with **0x1014** (optional) then start a new transaction with **0x1001**.

---

## Applicability Matrix

| Transaction Interface | DynaFlex | DynaFlex II PED | DynaProx | DynaFlex II GO |
|----------------------:|:--------:|:---------------:|:--------:|:--------------:|
| MSR (Swipe)           | ✅       | ✅              | ✅       | ✅             |
| EMV Contact           | ✅       | ✅              | ❌       | ✅             |
| EMV Contactless       | ✅       | ✅              | ✅       | ✅             |
| MCE (Manual)          | ✅       | ✅              | ❌       | ❌             |

---

## Command Syntax

| Field   | Length | Value  | Description                  |
|---------|--------|--------|------------------------------|
| Command | 2      | 0x1009 | Close / Clear Transaction    |
| TLVs    | var.   | —      | None required                |

---

## Examples

> No public request/response APDU examples are provided in D100005000-103 for this command.

---

## Error Conditions

| SW1SW2 | Meaning              |
|--------|----------------------|
| 9000   | Success              |
| 6985   | Nothing to clear     |
| 6F00   | Unknown error        |

---

## Notes
- Recommended recovery sequence: **0x1009 → (optional) 0x1014 → 0x1001**.
