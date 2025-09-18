---
title: 0x1014 — Get Transaction Status
layout: home
parent: 0x10nn – Transactions
nav_order: 7
---

# 0x1014 — Get Transaction Status

Queries the current transaction state for recovery and verification.

---

## Sequence of Events

**Preconditions**
- None.

**Steps**
1. Host issues **0x1014 — Get Transaction Status**.
2. Device returns the current state/flags and SW1SW2.
3. Host acts based on state (resume, cancel, or restart).

**Error/Recovery**
- If `69 85` (no active/suspended transaction), proceed to new **0x1001**.

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

| Field   | Length | Value  | Description            |
|---------|--------|--------|------------------------|
| Command | 2      | 0x1014 | Get Transaction Status |
| TLVs    | var.   | —      | None required          |

---

## Examples

> No public request/response APDU examples are provided in D100005000-103 for this command.

---

## Error Conditions

| SW1SW2 | Meaning                          |
|--------|-----------------------------------|
| 9000   | Success                           |
| 6985   | No active/suspended transaction   |
| 6F00   | Unknown error                     |

---

## Notes
- Prefer event-driven notifications; use 0x1014 primarily for recovery.
