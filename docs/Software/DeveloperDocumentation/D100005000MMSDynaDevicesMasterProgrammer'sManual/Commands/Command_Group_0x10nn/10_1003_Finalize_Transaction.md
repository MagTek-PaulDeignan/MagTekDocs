---
title: 0x1003 — Finalize Transaction
layout: home
parent: 0x10nn – Transactions
nav_order: 3
---

# 0x1003 — Finalize Transaction

Completes a transaction when the device expects a final host step (for example, applying the Authorization Response Code).

---

## Sequence of Events

**Preconditions**
- The transaction was started with **0x1001** and has reached a kernel state requiring final host action (e.g., EMV finalization step).
- No additional issuer authentication data is required (use **0x1004** if ARPC/scripts are needed).

**Steps**
1. Host determines the final decision (approve/decline/offline result).
2. Host sends **0x1003 — Finalize Transaction** with the required TLVs (e.g., `8A` — Authorization Response Code) if applicable.
3. Device applies the decision in the kernel.
4. Device returns a response and, if needed, prompts for **Remove Card** (ICC).

**Error/Recovery**
- On `69 85` (no finalizable transaction), perform recovery: **0x1009 → (optional) 0x1014 → 0x1001**.

---

## Applicability Matrix

| Transaction Interface | DynaFlex | DynaFlex II PED | DynaProx | DynaFlex II GO |
|----------------------:|:--------:|:---------------:|:--------:|:--------------:|
| MSR (Swipe)           | ❌       | ❌              | ❌       | ❌             |
| EMV Contact           | ✅       | ✅              | ❌       | ✅             |
| EMV Contactless       | ✅       | ✅              | ✅       | ✅             |
| MCE (Manual)          | ❌       | ❌              | ❌       | ❌             |

---

## Command Syntax

| Field   | Length | Value  | Description             |
|---------|--------|--------|-------------------------|
| Command | 2      | 0x1003 | Finalize Transaction    |
| TLVs    | var.   | —      | May include `8A` (ARC)  |

---

## Examples

> No public request/response APDU examples are provided in D100005000-103 for this command.

---

## Error Conditions

| SW1SW2 | Meaning                          |
|--------|-----------------------------------|
| 9000   | Success                           |
| 6985   | No finalizable transaction        |
| 6A80   | Invalid data (malformed TLVs)     |
| 6F00   | Unknown error                     |

---

## Notes
- Ensure `8A` (ARC) is consistent with the host decision and any prior kernel state.
