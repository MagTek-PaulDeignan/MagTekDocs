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

**Preconditions**
- A transaction was initiated with **0x1001** and is currently paused by the device.
- The device indicated "continue" without requiring host-supplied TLVs.

**Steps**
1. Host issues **0x1002 — Continue Transaction**.
2. Device resumes the in-progress kernel/flow.
3. Device updates UI/prompts as needed.
4. Device returns a response to **0x1002** and then continues with the normal transaction outcome (status/notifications).

**Error/Recovery**
- If `69 85` (no resumable state) is returned, issue **0x1009 — Close/Clear**, optionally **0x1014 — Get Status**, then restart with **0x1001**.

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

| Field   | Length | Value  | Description            |
|---------|--------|--------|------------------------|
| Command | 2      | 0x1002 | Continue Transaction   |
| TLVs    | var.   | —      | None required          |

---

## Examples

> No public request/response APDU examples are provided in D100005000-103 for this command.

---

## Error Conditions

| SW1SW2 | Meaning                         |
|--------|----------------------------------|
| 9000   | Success                          |
| 6985   | No resumable transaction         |
| 6F00   | Unknown error                    |

---

## Notes
- Use **0x1004 — Resume Transaction** when the device is explicitly waiting for host/issuer data (e.g., ARPC).
